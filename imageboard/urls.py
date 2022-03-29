from . import views
from django.urls import path
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(
    url='/static/imageboard/favicon.ico', permanent=True)


urlpatterns = [
    path('', views.ThreadListView.as_view(), name='home'),
    path('new-thread', views.ThreadCreateView.as_view(), name='new-thread'),
    path('thread/<int:pk>', views.thread_detail, name='thread'),
    path('thread/<int:pk>/delete', views.thread_delete, name='delete-thread'),
    path('thread/<int:pk>/edit',
         views.ThreadEditView.as_view(), name='edit-thread'),
    path('thread/<int:pk>/reply/<int:reply_id>/delete',
         views.reply_delete, name='delete-reply'),
    path('thread/<int:pk>/reply/<int:reply_id>/edit',
         views.ReplyEditView.as_view(), name='edit-reply'),
    path('favicon.ico', favicon_view),
]
