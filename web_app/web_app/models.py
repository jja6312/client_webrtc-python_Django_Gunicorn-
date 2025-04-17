from django.db import models

class Message(models.Model):
    """간단한 메시지 모델"""
    content = models.TextField(verbose_name="메시지 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 시간")
    
    def __str__(self):
        return f"{self.content[:20]}... ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
    
    class Meta:
        verbose_name = "메시지"
        verbose_name_plural = "메시지 목록"
        ordering = ['-created_at']
