from django.contrib.auth.models import AbstractUser
from django.db import models


# 장고는 기본적으로 user모델을 가지고 있는데, 이 user모델을 사용하지 않고 사용자 정의 user모델을 사용하고 싶을때
# AUTH_USER_MODEL 을 사용해서 연결을 해준다.
# ------ 사용자화 유저 인증 모델 ------
class User(AbstractUser):
    pass
