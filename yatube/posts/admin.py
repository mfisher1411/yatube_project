from django.contrib import admin
from .models import Post, Group



# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # Перечислим поля, которые должны отображаться в админке
    # Добавим в начало столбец pk
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')

    list_editable = ('group',)

    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)

    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)

     # Это свойство сработает для всех колонок: где пусто - там будет эта строка
    empty_value_display = '-пусто-'

# При регистрацииииииииии модели Post источником конфигурации для нее назначаем
# класс PostAdmin
    
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)