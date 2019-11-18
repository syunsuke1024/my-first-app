from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table="category"
        verbose_name = "ｶﾃｺﾞﾘ"
        verbose_name_plural = "ｶﾃｺﾞﾘ"

    category_name=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.category_name

class Shosha(models.Model):
    class Meta:
        db_table = "shosya"
        verbose_name = "商社"
        verbose_name_plural = "商社"

    category_name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.category_name
class Shozoku(models.Model):
    class Meta:
        db_table = "shozoku"
        verbose_name = "所属"
        verbose_name_plural = "所属"

    category_name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.category_name

class Kounyu(models.Model):
    class Meta:
        db_table = "kounyu"
        verbose_name = "購入"
        verbose_name_plural = "購入"

    date = models.DateField(verbose_name="購入日",default=datetime.now)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,verbose_name="ｶﾃｺﾞﾘ")
    shozoku = models.ForeignKey(Shozoku,on_delete=models.PROTECT,verbose_name="所属")
    shosha = models.ForeignKey(Shosha,on_delete=models.PROTECT,verbose_name="商社")
    tanka = models.IntegerField(verbose_name="金額",help_text="税抜価格")
    kazu = models.IntegerField(verbose_name="数")
    memo = models.CharField(max_length=255,verbose_name="備考",blank=True,help_text="ｶﾀｶﾅ、ｱﾙﾌｧﾍﾞｯﾄは半角で")
    def __str__(self):
        return self.memo