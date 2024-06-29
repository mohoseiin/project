from audioop import reverse
from django.contrib import admin
from .models import buylist, food,week,material,reqq
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

class materialAdmin(admin.ModelAdmin):
    list_display = ('id','name','count','typework','url')

class reqqAdmin(admin.ModelAdmin):
    list_display = ('id','count')

class reqqInline(admin.TabularInline):
    model = food.reqqs.through

class foodAdmin(admin.ModelAdmin):
    inlines = [reqqInline]
    list_display = ('id',"name","persons")

class weekAdmin(admin.ModelAdmin):
    list_display = ('id',"type","year","month","day","status" , 'button')
    
    def button(self,obj):
        if obj.status == False:
            return mark_safe(f'<a href="/update/week/food/{obj.id}" style="background: #264B5D;padding:5px;border-radius: 5px">update access</a>')
        else :
            return mark_safe('<span style="background: green;padding:5px;border-radius: 5px">Accepted</span>')
        
class buylistAdmin(admin.ModelAdmin):
    list_display = ('id','datastart',"dataend","status" , 'button')

    def button(self,obj):
        if obj.status == False:
            return mark_safe(f'<a href="/update/buylist/{obj.id}" style="background: #264B5D;padding:5px;border-radius: 5px">update access</a>')
        else :
            return mark_safe('<span style="background: green;padding:5px;border-radius: 5px">Accepted</span>')
        
    def datastart(self,obj):
        return mark_safe(f'{obj.s_year}/{obj.s_month}/{obj.s_day}')
    
    def dataend(self,obj):
        return mark_safe(f'{obj.e_year}/{obj.e_month}/{obj.e_day}')

admin.site.register(food,foodAdmin)
admin.site.register(week,weekAdmin)
admin.site.register(material,materialAdmin)
admin.site.register(reqq,reqqAdmin)
admin.site.register(buylist,buylistAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)