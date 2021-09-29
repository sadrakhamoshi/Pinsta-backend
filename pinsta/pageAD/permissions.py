from rest_framework.permissions import BasePermission
from .models import PageAD


class PageAdRequestPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            try:
                object = PageAD.objects.all().get(id=request.data.get('page_ad'))
                return request.user == object.owner
            except:
                self.message = 'You do not have permission to perform this action or your object does not Exist'
                return False
        return request.user.is_staff
