from django.db import models
from django.contrib import admin

# Create your models here.
class depts(models.Model):
    dname=models.CharField(max_length=50)
    def __unicode__(self):
        return self.dname

class depts2(models.Model):
    dname=models.CharField(max_length=50)
    def __unicode__(self):
        return self.dname


class users(models.Model):
    name=models.CharField(max_length=20)
    uname=models.CharField(max_length=20,unique=True)
    upasswd=models.CharField(max_length=50)
    udept=models.IntegerField()
    addass=models.IntegerField()
    delass=models.IntegerField()
    wxass=models.IntegerField()
    jhass=models.IntegerField()
    beizhu=models.CharField(max_length=150,null=True)
    def __unicode__(self):
        return self.uname
class gdzc(models.Model):
    zcid=models.CharField(max_length=20,unique=True)
    zcm=models.CharField(max_length=20)
    zcxh=models.CharField(max_length=50)
    zxlb=models.CharField(max_length=20)
    ccrq=models.DateField()
    rkrq=models.DateField()
    user=models.IntegerField(null=True)
    stat=models.CharField(max_length=10)
    price=models.FloatField()
    cost=models.IntegerField()
    beizhu=models.CharField(max_length=150,null=True)
    def __unicode__(self):
        return self.zcid
class czjl(models.Model):
    zcid=models.CharField(max_length=20)
    optuser=models.IntegerField()
    opts=models.CharField(max_length=10)
    czrq=models.DateTimeField()
    beizhu=models.CharField(max_length=150,null=True)
    def __unicode__(self):
        return self.zcid
class jcwx(models.Model):
    zcid=models.CharField(max_length=20)
    optuser = models.IntegerField()
    opts=models.CharField(max_length=10)
    xgry=models.IntegerField()
    ckrq=models.DateField()
    rkrq=models.DateField(null=True)
    beizhu=models.CharField(max_length=150,null=True)
    def __unicode__(self):
        return self.zcid
class baofei(models.Model):
    zcid=models.CharField(max_length=20,unique=True)
    optuser = models.IntegerField()
    bfyy=models.CharField(max_length=200)
    bfrq=models.DateField()
    beizhu=models.CharField(max_length=150,null=True)
    def __unicode__(self):
        return self.zcid


admin.site.register(users)
admin.site.register(depts)
admin.site.register(gdzc)
admin.site.register(czjl)
admin.site.register(jcwx)
admin.site.register(baofei)