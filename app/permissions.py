# classe de permissão global
from rest_framework import permissions


class GlobalDefaultPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        # variavel para montar a logica da string
        model_permission_codename = self.__get_model_permission_codename(
            request.method,
            view=view,
        )
        # se der algum erros na logica da string
        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)

    # logica da string
    def __get_model_permission_codename(self, method, view):
        try:
            # buscar o model
            model_name = view.queryset.model._meta.model_name
            # buscar o app
            app_label = view.queryset.model._meta.app_label
            # buscar a ação
            action = self.__get_action_sufix(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return False

    # bliblioteca de metodos
    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }

        return method_actions.get(method, '')
