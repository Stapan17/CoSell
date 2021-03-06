from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', views.home, name='home'),
    #     path('', PostListView.as_view(), name='home'),
    path('user/<str:username>/', UserPostListView.as_view(),
         name='user-college-products'),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('payment', views.payment, name='pay'),
    path('profile/', views.profile, name='profile'),
    path('product/<int:pk>/', PostDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update/',
         PostUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/',
         PostDeleteView.as_view(), name='product-delete'),
    path('product/new/', PostCreateView.as_view(), name='product-create'),
    path('error', views.error, name='error'),
    path('success_take/', views.success_take, name='success_take'),
    path('faq', views.faq, name='faq'),
    path('faq_ask', views.faq_ask, name="faq_ask"),
    path('about', views.about, name="about"),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/',
         views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
    path('recivedMessages', views.recivedMessages, name='recivedMessages'),
]
