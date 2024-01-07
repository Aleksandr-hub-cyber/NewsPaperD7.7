from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostSearch, PostEdit, PostDelete

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='news_detail'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('edit/<int:pk>', PostEdit.as_view(), name='news_edit'),
    path('delete/<int:pk>', PostDelete.as_view(), name='news_delete'),
    path('search/', PostSearch.as_view(), name='news_search'),
]
