from django.db import models

# Create your models here.
class Userinfo(models.Model):
    """
    用户表
    """
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    is_super=models.IntegerField(null=True,blank=True,verbose_name="是否是管理员")
    class Meta:
        verbose_name_plural="用户表"
    def __str__(self):
        return self.username
class Confernce(models.Model):
    """
    会议室表
    """
    title=models.CharField(max_length=32,verbose_name="会议室名称")
    nunm=models.IntegerField(verbose_name="容纳人数")
    position=models.CharField(max_length=64,verbose_name="位置",default=None,null=True,blank=True)
    class Meta:
        verbose_name_plural="会议室"
    def __str__(self):
        return self.title
class Confernce_detail(models.Model):
    """
    会议室详细
    """
    confernce=models.ForeignKey("Confernce",verbose_name="所属会议室")
    caption=models.CharField(max_length=64,verbose_name="时间段")
    user=models.OneToOneField("Userinfo",verbose_name="预定人")
    class Meta:
        verbose_name_plural="会议室详细"
    def __str__(self):
        return self.confernce.title+':'+self.user.username+'：'+self.caption