from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.ADD, name='add'),
    path('edit', views.Edit, name='edit'),
    path('update/<str:id>', views.Update, name='update'),
    path('delete', views.Delete)
]
