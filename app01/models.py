from django.db import models

# Create your models here.


from django.db import models
from datetime import datetime
# Create your models here.


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10,null=True)
    bday = models.DateField()
    sex = models.CharField(max_length=5,choices=(("1","boy"),("2","girl")))
    checked = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=7)
    publish = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    """
    作者表
    """
    name=models.CharField( max_length=32,null=True)
    age=models.IntegerField()
    # authorDetail=models.OneToOneField(to="AuthorDetail",to_field="nid",on_delete=models.CASCADE)
    au=models.OneToOneField("AuthorDetail",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class AuthorDetail(models.Model):
    """
    作者详细信息表
    """
    birthday=models.DateField()
    telephone=models.CharField(max_length=11,null=True)
    addr=models.CharField(max_length=64,null=True)
    # class Meta:
        # db_table='authordetail' #指定表名
        # ordering = ['-id',]
    def __str__(self):
        return self.telephone


class Publish(models.Model):
    """
    出版社表
    """
    name=models.CharField( max_length=32,null=True)
    city=models.CharField( max_length=32,null=True)


class Book1(models.Model):
    """
    书籍表
    """
    title = models.CharField( max_length=32,null=True)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    comment = models.FloatField(default=100)
    good = models.FloatField(default=100)
    publishs=models.ForeignKey(to="Publish",on_delete=models.CASCADE,)
    authors=models.ManyToManyField('Author',)

    def __str__(self):
        return self.title