from django.shortcuts import render,HttpResponse
from django.views import View
from app01 import models
# Create your views here.


class Index(View):
    def get(self,request):
        """
        基于双下划线的跨表查询
        :param request:
        :return:
        """
        #一对一
        #ret = models.Author.objects.filter(name="fc").values("au__telephone") #正向查用属性
        #ret = models.AuthorDetail.objects.filter(author__name="LYJJ").values("telephone").first() #反向查用表名


        #一对多
        # ret = models.Book1.objects.filter(title="hlm").values("publishs__name") #正向
        # ret = models.Publish.objects.filter(book1__title="hlm").values("name") #反向

        # ret = models.Publish.objects.filter(name="大幅度").values("book1__title")#反向
        # ret = models.Book1.objects.filter(publishs__name="大幅度").values("title")


        # 多对多
        # ret = models.Book1.objects.filter(title="xyj").values("authors__name")
        # ret = models.Author.objects.filter(book1__title="xyj").values("name")
        #
        # print(ret)


        # 聚合查询

        from django.db.models import Avg,Sum,Max,Count,F,Q
        # ret = models.Book1.objects.all().aggregate(Avg("price"))
        # ret = models.Book1.objects.all().aggregate(Max("price"))


        # 分组查询

        # ret = models.Book1.objects.values("publishs","title").annotate(Avg("price"))
        # ret = models.Publish.objects.annotate(a=Avg("book1__price")).values("a")


        # F查询
        # Book1表中 comment>good
        # ret = models.Book1.objects.filter(comment__gt=F("good"))
        # ret = models.Book1.objects.filter(comment__lt=F("good"))
        # models.Book1.objects.all().update(
        #     price = F("price")+100
        # )


        # Q查询 价格大于112或者评论小于100
        #ret = models.Book1.objects.filter(Q(price__gt=112)|Q(comment__lt=100))

        # 执行原生sql语句
        #models.Book1.objects.raw("原生sql语句")

        print(ret)





        return HttpResponse("ok1")