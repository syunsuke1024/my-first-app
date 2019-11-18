from django.contrib import admin

# Register your models here.
from .models import Category,Shosha,Kounyu,Shozoku

class KounyuAdmin(admin.ModelAdmin):
    list_display = ('date','category','shozoku','memo')
admin.site.register(Shosha)
admin.site.register(Category)
admin.site.register(Kounyu,KounyuAdmin)
admin.site.register(Shozoku)