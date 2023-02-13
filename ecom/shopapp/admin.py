from django.contrib import admin
from.models import category,Product

# Register your models here.
class shopadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(category,shopadmin)


class proadmin(admin.ModelAdmin):
    list_display = ['name', 'price','stock','available','mfd','update']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Product,proadmin)
