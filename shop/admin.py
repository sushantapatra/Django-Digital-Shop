from django.contrib import admin
from django.utils.html import format_html

from instamojo_wrapper import Instamojo
from digitalShop.settings import PAYMENT_API_KEY, PAYMENT_AUTH_TOKEN
api = Instamojo(api_key=PAYMENT_API_KEY, auth_token=PAYMENT_AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

from shop.models import Product, ProductImages,User,Payment

# Register your models here.


class ProductImageModel(admin.StackedInline):
    model=ProductImages

class ProductModel(admin.ModelAdmin):
    list_display=['id','name','small_description','get_price','show_discount','sell_price','file','get_thumbnail']
    inlines=[ProductImageModel]

    def small_description(self, obj):
        return  format_html(f'<span  title="{ obj.description}">{obj.description[:15]}..</span>') 

    def get_price(self, obj):
        return  format_html(f'<span>₹ {obj.price}</span>')

    def show_discount(self, obj):
        return  format_html(f'<span>{obj.discount} %</span>') 

    def sell_price(self, obj):
        return f"₹  {(obj.price - (obj.price*obj.discount)/100)}"

    def get_thumbnail(self,obj):
        return format_html(f''' <img height='50'  src='{obj.thumbnail.url}'/>''')


    small_description.short_description="Description"
    get_price.short_description="Price"
    show_discount.short_description="Discount"


class UserModel(admin.ModelAdmin):
    list_display=['id','name','email','phone','active']
    sortable_by=['name','id']
    list_editable=['active','name']

class PaymentModel(admin.ModelAdmin):
    list_display=['id','get_user','get_product','payment_request_id','payment_id','get_status','get_amount']
    sortable_by=['user','product','status']

    def get_user(self,obj):
        return format_html(f'<a href="/admin/shop/user/{obj.user.id}/change/">{obj.user}</a>')

    def get_product(self,obj):
        return format_html(f'<a href="/admin/shop/product/{obj.product.id}/change/" target="_blank">{obj.product}</a>')

    def get_status(self, obj):
        response = api.payment_request_payment_status(obj.payment_request_id, obj.payment_id)
        # if response['success'] !='False':
        #     print(response['success'])
        obj.paymentDetails=response
        if obj.status !='False':
            return True
        

    def get_amount(self, obj):
        return obj.paymentDetails['payment_request']['amount']


    get_user.short_description="User Name"
    get_product.short_description="Product Name"
    get_status.boolean=True

  

admin.site.register(Product,ProductModel)
#admin.site.register(ProductImages, ProductImageModel)
admin.site.register(User,UserModel)
admin.site.register(Payment,PaymentModel)