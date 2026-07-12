import faiss
import numpy as np
import json
import os
from sentence_transformers import SentenceTransformer
from django.conf import settings
class FaissVectorStore:

    def __init__(self, dim: int, index_file: str = None, meta_file: str = None):
        if index_file is None:
            index_file = os.path.join(settings.BASE_DIR, 'static', 'Faiss_vector_databases', 'vector.index')
        if meta_file is None:
            meta_file = os.path.join(settings.BASE_DIR, 'static', 'Faiss_vector_databases', 'meta.json')
        self.dim = dim
        self.index_file=index_file
        self.meta_file=meta_file
        self.index=None
        self.meta={} # id -> metadata (e.g., text, url, etc.)
        self._init_index()

    def _init_index(self):
        """初始化 FAISS 索引（带 ID 映射）"""
        # 使用 IndexFlatIP（内积，适合归一化后的向量）或 IndexFlatL2
        # 如果向量已 L2 归一化，IP 等价于余弦相似度
        base_index=faiss.IndexFlatL2(self.dim)
        self.index=faiss.IndexIDMap(base_index)
        # 尝试加载已有数据
        if os.path.exists(self.index_file):
            self.load()
    def add(self,vectors:np.ndarray,ids:list,metas:list=None):
        """
        添加向量到索引
        :param vectors: shape (n, dim), dtype=np.float32
        :param ids: list of int or str (will be converted to int for FAISS)
        :param metas: list of dict or str (optional metadata)
        """
        assert len(vectors)==len(ids) #"Vectors and IDs must have same length"
        vectors=np.array(vectors)
        # FAISS ID 必须是 int64，若传入字符串 ID，需映射为整数
        int_ids=[]
        for i,_id in enumerate(ids):
            if isinstance(_id,str):
                int_id=len(self.meta)+1
                self.meta[int_id]={"original_id":_id,"meta":metas[i] if metas else None}
                int_ids.append(int_id)
            else:
                int_ids.append(_id)
                if metas:
                    self.meta[_id]={'original_id':_id,"meta":metas[i] if metas else None}
        self.index.add_with_ids(vectors,np.array(int_ids,dtype=np.int64))

    def search(self, query_vector: np.ndarray, k: int = 5):
        """
        搜索最相似的 k 个向量
        :param query_vector: shape (dim,) or (1, dim)
        :return: list of (id, score, metadata)
        """
        query_vector = np.array(query_vector, dtype=np.float32).reshape(1, -1)
        faiss.normalize_L2(query_vector)
        distances, ids = self.index.search(query_vector, k)
        results = []
        for dist, _id in zip(distances[0], ids[0]):
            if _id == -1:
                continue  # 无效结果
            meta = self.meta.get(int(_id), {})
            results.append({
                "id": meta.get("original_id", _id),
                "score": float(dist),
                "metadata": meta.get("meta")
            })

        return results

    def save(self):
        #保存索引和元数据到磁盘
        faiss.write_index(self.index,self.index_file)
        with open(self.meta_file,'w',encoding='utf-8') as f:
            json.dump(self.meta,f,ensure_ascii=False,indent=4)

    def load(self):
        #加载索引和元数据
        if os.path.exists(self.index_file):
            self.index=faiss.read_index(self.index_file)
        if os.path.exists(self.meta_file):
            with open(self.meta_file,'r',encoding='utf-8') as f:
                self.meta=json.load(f)
            self.meta={int(k): v for k,v in self.meta.items()}
    def __len__(self):
        return  self.index.ntotal
    #获取现有最大ids
    def __get_max_ids(self)->int:
        max_ids=0
        # 遍历元数据中的原始ID（original_id）
        for meta in self.meta.values():
            original_id=meta.get("original_id")
            if not original_id or  not  isinstance(original_id,str):
                continue
            if original_id.startswith("doc_"):
                num_str=original_id.split("doc_")[-1]
                if num_str.isdigit():
                    current_id=int(num_str)
                    if current_id > max_ids:
                        max_ids=current_id
        return max_ids
    def get_ids(self,count):
        max_id=self.__get_max_ids()
        new_ids=[]
        for i in range(count):
            new_num=max_id+1+i
            new_id=f"doc_{new_num:03d}"
            new_ids.append(new_id)
        return new_ids

    def text_to_vectors(self,texts: list) -> np.ndarray:

        model_path=os.path.join(settings.BASE_DIR, 'static', 'Vector_model')
        model = SentenceTransformer(model_path)
        """将文本列表转换为768维向量数组（shape: [n, 768]）"""
        vectors = model.encode(texts, convert_to_numpy=True)
        vectors = vectors.astype(np.float32)
        faiss.normalize_L2(vectors)
        return vectors

    def save_vectors(self,texts:list,metas:list=None):
        if metas is None:
            metas=[{'text':t} for t in texts]
        vectors = self.text_to_vectors(texts)
        new_ids=self.get_ids(len(vectors))
        self.add(vectors=vectors,
                 ids=new_ids,
                 metas=metas)
        self.save()
        print("当前数据库总量：", len(self))


if __name__=="__main__":
    store = FaissVectorStore(dim=768)
    metas = [
        {"text": "人工智能是未来", "url": "https://example.com/1"},
        {"text": "机器学习很强大", "url": "https://example.com/2"},
        {"text": "FAISS 加速向量搜索", "url": "https://example.com/3"}
    ]
    texts=[m["text"] for m in metas]
    store.save_vectors(texts=texts,metas=metas)

