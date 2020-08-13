"""tempPjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
''' 
프로젝트 기본 URL에서 전체를 관리하기에는 URL이 많아 유지 보수가 어려울 수 있으므로
include를 추가로 import하여 각 application에서 작성한 urls.py를 찾아볼 수 있게 처리함 
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')), # 각 application의 urls.py 위치를 등록함
]
