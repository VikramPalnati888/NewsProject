from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from NewsApp.views import *

urlpatterns = [
    path('login/', login,name='login'),
    path('home/', home,name='home'),
    path('logout/', Logout,name='logout'),
    # path('news/', newsHtml,name='news'),
    path('newspost/', NewsPost,name='news_post'),
    path('newsget/', NewsGet,name='news_get'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)