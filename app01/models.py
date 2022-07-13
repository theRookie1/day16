from django.db import models

# Create your models here.

class Department(models.Model):
    """
    部门表
    id 自动生成
    部门名称
    """
    title=models.CharField(verbose_name='部门标题',max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """员工表"""
    name=models.CharField(verbose_name='员工姓名',max_length=32)
    password=models.CharField(verbose_name='密码',max_length=64)
    age=models.IntegerField(verbose_name='年龄')
    #Django自带的约束
    gender_choices=(
        (1,'男'),
        (2,'女')
    )
    sex=models.SmallIntegerField(verbose_name='性别',choices=gender_choices)
    account=models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0)
    create_time=models.DateField(verbose_name='创建时间')
    #无约束
    #depart_id=models.BigIntegerField()

    #添加约束
    #虽然写的是depart但是内部自动添加_id
    #列名为depart_id

    # 级联删除
    #depart=models.ForeignKey(to='Department',to_field='id',on_delete=models.CASCADE)
    # 置空
    depart=models.ForeignKey(verbose_name="部门",to='Department',to_field='id',null=True,blank=True,on_delete=models.SET_NULL)


class PrettyNum(models.Model):
    """
    靓号管理数据库
    """
    """
    ID
    mobile
    price
    level(choice)
    status(choice)
    """
    mobile=models.CharField(verbose_name='手机号',max_length=11)
    price=models.DecimalField(verbose_name='价格',max_digits=10,decimal_places=2,default=0)
    level_choices=(
        (1,'1级'),
        (2,'2级'),
        (3,'3级'),
        (4,'4级'),
        (5,'5级'),
    )
    level=models.SmallIntegerField(verbose_name='等级',choices=level_choices,default=1)
    status_choices=(
        (1,'已占用'),
        (2,'未使用'),
    )
    status=models.SmallIntegerField(verbose_name='状态',choices=status_choices,default=2)