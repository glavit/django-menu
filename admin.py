# -*- coding: utf-8 -*
from django.contrib import admin
from django.conf import settings
from menu.models import Group
from menu.models import Item
from menu.models import GroupAttribute
from menu.models import ItemAttribute


if 'hvad' in settings.INSTALLED_APPS and hasattr(settings, 'LANGUAGES'):
	from hvad.admin import TranslatableAdmin
	BaseAdminModel = TranslatableAdmin
else:
	BaseAdminModel = admin.ModelAdmin


class GroupAttributeInline(admin.StackedInline):
	model = GroupAttribute
	extra = 0


class GroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'description', 'public', 'menu', 'count')
	search_fields = ('name', 'slug', 'description', 'id')
	list_editable = ['public']
	list_filter = ['public']
	inlines = [GroupAttributeInline]

admin.site.register(Group, GroupAdmin)


class ItemAttributeInline(admin.StackedInline):
	model = ItemAttribute
	extra = 0


class ItemAdmin(BaseAdminModel):
	list_display = ('display', 'get_absolute_url', 'group', 'sort', 'public', 'url_type', 'access', 'icon_preview')
	search_fields = ('name', 'url', 'group', 'sort', 'public')
	list_editable = ('public', 'sort')
	list_filter = ('public', 'group', 'access')
	inlines = [ItemAttributeInline]

admin.site.register(Item, ItemAdmin)
