#coding=utf-8
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Person(models.Model):
    SEX=((True,'先生'),
         (False,'女士'))
    USE=((True,'允许登录'),
         (False,'不许登录'))
    user=models.OneToOneField(User)
    realName=models.CharField(max_length=20,verbose_name='真实姓名',help_text='真实姓名（交流使用），或者昵称')
    role=models.IntegerField(default=1,help_text='用户的角色 1：普通用户，2：商店维护者')
    male=models.BooleanField(choices=SEX,help_text='性别，你懂得！')
    isWork=models.BooleanField(choices=USE,default=True,help_text='设置该账户的状态（是否允许登录）')

    class Admin():
        pass
    def __unicode__(self):
        return '%s--%s' %(self.user.get_full_name(),self.realName)


class Address(models.Model):
    user=models.ForeignKey(User)
    province=models.CharField(max_length=20,verbose_name='行政省',help_text='例如：河南')
    city=models.CharField(max_length=20,verbose_name='行政市',help_text='例如：郑州')
    area=models.CharField(max_length=20,verbose_name='行政区',help_text='例如：南开区')
    add=models.CharField(max_length=100,verbose_name='详细地址',help_text='例如：XX街 XX号')
    tel=models.CharField(max_length=20,verbose_name='联系电话',help_text='手机，座机')
    lastUseDate=models.DateField(auto_now=True,verbose_name='最后一次使用',help_text='最后一次使用，默认使用该地址')

    class Admin():
        pass
    def __unicode__(self):
        return '%s--%s' %(self.user.get_full_name(),self.add)


class Kind(models.Model):
    name=models.CharField(max_length=20,verbose_name='种类名称',help_text='男装')
    father=models.ForeignKey('Kind',null=True,blank=True,verbose_name='父级种类',help_text='上一级种类')

    class Admin():
        pass
    def __unicode__(self):
        return '%s' % self.name

class Tags(models.Model):
    tags=models.CharField(max_length=50,verbose_name='产品标签',help_text='产品介绍中的关键字，')

class ProductInfo(models.Model):
    name=models.CharField(max_length=50,verbose_name='产品名称',help_text='蓝色连衣裙')
    sn=models.CharField(max_length=50,verbose_name='序列号',help_text='产品序列号，货号')
    kind=models.ForeignKey(Kind,verbose_name='种类',help_text='男装类')
    tags=models.ManyToManyField(Tags,verbose_name='产品标签',help_text='产品表述的关键字')
    desc=models.CharField(max_length=40,verbose_name='产品介绍',help_text='产品介绍，内容无限制大小，内容会被保存\
    为文本，放在服务器上，数据库记录路径')
    htmldesc=models.TextField(verbose_name='html格式详细简介')
    total=models.IntegerField(verbose_name='总数量',help_text='产品库存总数量')
    preImg=models.ImageField(upload_to='photo/pre',verbose_name='产品缩略图')
    dateTime=models.DateTimeField(auto_created=True,verbose_name='上架时间',help_text='上架时间')

    class Admin():
        pass
    def __unicode__(self):
        return '%s' % self.name

class ProductPreference(models.Model):
    product=models.ForeignKey(ProductInfo,verbose_name='对应的产品信息')
    type=models.BooleanField(default=True,verbose_name='属性类型',help_text='该属性是单选还是复选')
    name=models.CharField(max_length=40,verbose_name='属性名称')
    class Admin():
        pass
    def __unicode__(self):
        return '%s--%s--%s' % (self.product.name,self.name,self.type)

class Preferences(models.Model):
    prodpre=models.ForeignKey(ProductPreference,verbose_name='对应的属性名')
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='浮动价格',help_text='的价格')
    name=models.CharField(max_length=20,verbose_name='具体属性名',help_text='如2L装、4L装')
    isDel=models.BooleanField(default=False,verbose_name='该条信息是否可用',help_text='是否废弃')
    class Admin():
        pass
    def __unicode__(self):
        return '%s--%s--%s' % (self.prodpre.name,self.name,self.price)
class ProductImg(models.Model):
    product=models.ForeignKey(ProductInfo,verbose_name='对应的产品信息')
    img=models.ImageField(upload_to='photo/img',verbose_name='产品图片')

class Product(models.Model):
    PAYCODE=(('nomal','本店售价'),
             ('cheap','促销价'),
             ('discount','打折价'),
    )
    productInfo=models.ForeignKey(ProductInfo,verbose_name='产品信息',help_text='产品信息')
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='产品价格',help_text='产品的价格')
    cheapPrice=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='促销价格',help_text='产品的促销价格')
    discount=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='折扣率',help_text='产品的折扣率，如0.5为5折，0.75为七五折，以产品价格为基数')
    type=models.CharField(max_length=10,default='nomal',choices=PAYCODE,verbose_name='使用的价格类型')

    class Admin():
        pass
    def __unicode__(self):
        return '%s---%s' %(self.productInfo.name,self.type)


#class ProductType(models.Model):
#    productInfo=models.ForeignKey(ProductInfo,verbose_name='产品信息',help_text='产品信息')
#    prodName=models.CharField(max_length=50,verbose_name='规格名称',help_text='与产品价格无关的规格，比如衣服的型号。')
#    desc=models.CharField(max_length=200,null=True,blank=True,verbose_name='规格描述',help_text='规格的详细信息，如果很通俗也可以不再描述，也可以把这部分写在产品信息中')
#    isUsed=models.BooleanField(default=True,verbose_name='是否在使用')
#    num=models.IntegerField(default=0,verbose_name='库存数量',help_text='产品库存数量，为0后就不可再添加进购物车了。')
#
#    class Admin():
#        pass
#    def __unicode__(self):
#        return '%s---%s' %(self.productInfo.name,self.prodName)

class Order(models.Model):
    STATUSCODE=(('u','未发货'),
                ('w','未送达'),
                ('s','已送达'),
                ('b','申请退货'),
                ('sb','已退货'),
                )
    PAYCODE=(('no','未付款'),
             ('yes','已付款'),
             ('back','已退款'),
    )
    PAYTYPE=(('zfb','支付宝'),
             ('kq','快钱'),
             ('mail','邮局汇款'),
             ('qq','财付通'),
    )
    user=models.ForeignKey(User,verbose_name='发起订单人')
    orderNumber=models.CharField(max_length=25,verbose_name='订单编号',help_text='订单编号，要求唯一，日期 20110101 + 时分秒 122031+用户id')
    productStatus=models.CharField(max_length=5,default='u',choices=STATUSCODE,verbose_name='订单状态',help_text='主要描述订单中货物的状态')
    moneyStatus=models.CharField(max_length=5,default='no',choices=PAYCODE,verbose_name='付款状态',help_text='主要描述付款的状态')
    isPayOnline=models.BooleanField(default=True,verbose_name='是否网上付款',help_text='默认是网上付款')
    payType=models.CharField(max_length=5,choices=PAYTYPE,null=True,blank=True,verbose_name='付款途径',help_text='支付宝、块钱、财付通、邮局汇款 等等途径')
    changePrice=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='订单修改金额值',help_text='订单折扣、免运费、促销等免去的费用（+为增加的钱数，-为免去的钱数）')
    changeDesc=models.CharField(max_length=200,null=True,blank=True,verbose_name='订单修改金额的原因',help_text='订单修改金额的原因')
    changeUser=models.ForeignKey(User,related_name='admin',null=True,blank=True,verbose_name='订单金额修改人',help_text='订单修改金额员工，应该是工作人员')
    userDesc=models.CharField(max_length=20,null=True,blank=True,verbose_name='用户备注',help_text='用户留下的订单备注信息')
    orderPrice=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='订单金额总数',help_text='用户订单的最后金额')
    class Admin():
        pass
    def __unicode__(self):
        return '%s---%s' %(self.orderNumber,self.user.get_full_name())

class OrderProduct(models.Model):
    order=models.ForeignKey(Order,verbose_name='对应订单',help_text='订单产品列表')
    productInfo=models.ForeignKey(ProductInfo,verbose_name='产品信息',help_text='订单产品信息')
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='产品实际销售价',help_text='产品实际销售价')
    nomalprice=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='产品原价',help_text='产品原价')
#    product=models.ForeignKey(Product,verbose_name='产品价格',help_text='订单中产品价格')
    desc=models.CharField(max_length=200,verbose_name='产品的价格类型',help_text='下订单时，产品的价格是原价、促销价、折扣价')
    count=models.IntegerField(default=1,verbose_name='数量',help_text='产品在订单中数量')

    class Admin():
        pass
    def __unicode__(self):
        return '%s---%s----%s' %(self.order.orderNumber,self.product.prodName,self.count)

class OrderProductProd(models.Model):
    prod=models.ForeignKey(OrderProduct,verbose_name='订单中的产品',help_text='描述订单里的产品属性信息')
    pref=models.ForeignKey(Preferences,verbose_name='订单中的产品的属性',help_text='用户选择的产品的属性')
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='产品实际波动价',help_text='产品实际波动价')
    class Admin():
        pass
    def __unicode__(self):
        return '%s---%s----%s' %(self.prod.productInfo.name,self.pref.name.prodName,self.price)

class Eshop(models.Model):
    PAYTYPE=(('standard','标准'),
            
    )
    site=models.OneToOneField(Site)
    keyword=models.CharField(max_length=50,verbose_name='网站关键词',help_text='描述网站的业务领域')
    desc=models.CharField(max_length=500,verbose_name='网站简介',help_text='描述网站的业务领域')
    templatecode=models.CharField(max_length=20,verbose_name='网站主题',help_text='网站的样式主题',default='standard')

    class Admin():
        pass
    def __unicode__(self):
        return '%s' % self.site.name

class Ad(models.Model):
    title=models.CharField(max_length=100,verbose_name='广告标题',help_text='广告标题')
    href=models.CharField(max_length=200,verbose_name='目标地址',help_text='超链接')
    img=models.ImageField(upload_to='photo/ad',verbose_name='广告图片')
    places=models.CharField(max_length=20,verbose_name='广告位置标签',help_text='广告位置标签')
    num=models.IntegerField(default=0,verbose_name='点击次数',help_text='点击次数')

    class Admin():
        pass
    def __unicode__(self):
        return '%s' % self.title




    