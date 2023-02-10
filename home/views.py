from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.decorators import has_role_decorator
from rolepermissions.permissions import revoke_permission, grant_permission

# Create your views here.
#@has_role_decorator('vendedor')
def home(request):

    #revoke_permission(request.user, 'ver_metas')
    #grant_permission(request.user, 'ver__metas')
    #print(get_user_roles(request.user))
    #return HttpResponse ('Estou na Home')
    return render(request, 'home.html')

def criar_usuario(request):
    user = User.objects.create_user(username='caio', password='123123')
    user.save()
    assign_role(user, 'gerente')
    return HttpResponse('Usuário salvo com sucesso')