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
        ret = models.Book1.objects.filter(title="hlm").values("publishs__name") #正向
        # ret = models.Publish.objects.filter(book1__title="hlm").values("name") #反向

        ret = models.Publish.objects.filter(name="大幅度").values("book1__title")#反向
        #ret = models.Book1.objects.filter(publishs__name="大幅度").values("title")


        print(ret)
        return HttpResponse("ok")