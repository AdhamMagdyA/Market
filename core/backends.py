from django.contrib.auth.backends import ModelBackend
from users.models import User
from sellers.models import Seller
from django.db.models import Q

from django.contrib.auth.models import User as SuperUser



class SuperUserBackend(ModelBackend):
    def authenticate(self, request, username=None,password=None,**Kwargs):
        try:
            admin=SuperUser.objects.get(
                Q(email=username)
            )
        except SuperUser.DoesNotExist:
            return None
        # except MultipleObjectsReturned:
        #         return user.objects.get(email=email).ordered_by['email'].first()

        else:
            if admin.check_password(password) and self.user_can_authenticate(admin):
                return admin

    
    def get_user(self, user_id):
        try:
            admin=SuperUser.objects.get(pk=user_id)
        except:
            return None

        return admin if self.user_can_authenticate(admin) else None




class NormalUserBackend(ModelBackend):
    def authenticate(self, request, username=None,password=None,**Kwargs):
        try:
            user=User.objects.get(
                Q(email=username)
            )
        except User.DoesNotExist:
            return None
        # except MultipleObjectsReturned:
        #         return user.objects.get(email=email).ordered_by['email'].first()

        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                if user.is_active == True :
                    return user

    
    def get_user(self, user_id):
        try:
            user=User.objects.get(pk=user_id)
        except:
            return None

        return user if self.user_can_authenticate(user) else None


class SellerBackend(ModelBackend):
    def authenticate(self, request, username=None,password=None,**Kwargs):
        try:
            seller=Seller.objects.get(
                Q(email=username)
            )
        except Seller.DoesNotExist:
            return None

        else:
            print('model password check')
            if seller.check_password(password) and self.user_can_authenticate(seller):
                print('passed user_can_authenticate seller function')
                if seller.is_active == True:
                    return seller

    
    def get_user(self, user_id):
        try:
            seller=Seller.objects.get(pk=user_id)
        except:
            return None
        return seller if self.user_can_authenticate else None

