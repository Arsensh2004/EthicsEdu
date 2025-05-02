from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

# URL для переключения языка
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# Основные маршруты с поддержкой i18n
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('ethics.urls')),
    prefix_default_language=False
)

# Подключение статики (если нужно для продакшена)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
