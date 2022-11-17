from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "api-v1"

router = DefaultRouter()
router.register('post',views.PostViewSet,basename='post')
urlpatterns = router.urls

#urlpatterns = [
    #path('post/<int:id>',views.PostDetail, name="post-detail"),
    #path('post/',views.PostList.as_view(), name="post-list"),
    #path('post/<int:id>',views.PostDetail.as_view(), name="post-detail"),
    #path('post/<int:id>',views.PostDetail.as_view(), name="post-list"),
    #path('post/',views.PostViewSet.as_view({'get':'list','post':'create'}), name="post-list"),
   # path('post/<int:pk>',views.PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}), name="post-list")

#]
    #path('post/',views.PostList, name="post-list"),