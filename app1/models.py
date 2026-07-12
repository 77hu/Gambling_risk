from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User

class URLAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField(max_length=500)
    url_legitimacy = models.CharField(max_length=100)
    gambling_risk = models.BooleanField(default=False)
    risk_analysis = models.TextField()
    keywords = models.JSONField(default=list)  # 存 ['关键词1', '关键词2']
    raw_text = models.TextField()  # ← 关键！用于 TF-IDF 的原始文本（拼接后的）
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    def get_display_text(self):
        """生成用于 TF-IDF 的文本，可自定义组合字段"""
        return " ".join([
            self.url or "",
            self.url_legitimacy or "",
            "涉赌" if self.gambling_risk else "非涉赌",
            self.risk_analysis or "",
            " ".join(self.keywords)
        ])