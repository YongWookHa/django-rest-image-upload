from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # fieldsets : 관리자 리스트 화면에서 출력될 폼 설정 부분
    UserAdmin.fieldsets[1][1]['fields']+=('api_key', )
    UserAdmin.readonly_fields+=('api_key', )
    UserAdmin.search_fields+=('api_key',)
    UserAdmin.list_display = ('username', 'email', 'api_key', )
    
    # add_fieldsets : User 객체 추가 화면에 출력될 입력 폼 설정 부분
    UserAdmin.add_fieldsets += (
        (('Additional Info'),{'fields':('email','groups', 'user_permissions')}),
    )