from django.contrib import admin
from apps.core.models import Items
# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display=('id','item','status')

admin.site.register(Items,ItemsAdmin)