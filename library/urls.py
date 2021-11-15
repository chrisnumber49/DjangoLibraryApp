from django.urls import path
from . import views
from DjangoLibraryApp.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='uploadBook'),
    # bookId will be sent into update and delete functions in views.py
    path('update/<int:bookId>', views.update, name='updateBook'),
    path('delete/<int:bookId>', views.delete, name='deleteBook')
]

# for uploading and showing the image
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
