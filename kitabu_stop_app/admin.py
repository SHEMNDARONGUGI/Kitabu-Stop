from django.contrib import admin
from kitabu_stop_app.models import user, Category, Product, Order, Contact
# from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.register(user)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Contact)
































#https://youtu.be/KNvSWubOaQY?si=QALtjBcztjS0x0YB

#Unregister Groups
# admin.site.unregister(Group)

#Extend User Model
# class UserAdmin(admin.ModelAdmin):
#     model = User
    
    #Just display username fields on admin page
    # fields=['username', 'email', 'password']

#Unregister initial User
# admin.site.unregister(User)

#Re-register User
# admin.site.register(User, UserAdmin)