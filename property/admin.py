from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatshipInline(admin.TabularInline):
    model = Owner.flats_have.through
    raw_id_fields = ("owner", "flat",)

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)

    readonly_fields = ('created_at',)
    raw_id_fields = ("liked_by",)
    inlines = [
        FlatshipInline,
    ]

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats_have",)
    inlines = [
        FlatshipInline,
    ]
    exclude = ('flats_have',)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", "flat",)



admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
