from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Setup Contact section in Admin Panel
    """

    list_display = (
        'subject',
        'full_name',
        'email',
        'message',
        'date',
    )

    readonly_fields = (
        'subject',
        'full_name',
        'email',
        'message',
        'date',
    )

    search_fields = (
        'subject',
        'message',
        'full_name',
    )

    ordering = ['-date']


admin.site.register(Contact, ContactAdmin)
