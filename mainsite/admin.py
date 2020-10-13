from django.contrib import admin
from .models import *
# Register your models here.

class AddressInline(admin.TabularInline):
    model = Address
    fields = [
        'physical_address',
        'postal_address',
        'postal_code',
        'city',
        'site_map'
    ]
    extra = 0

class ContactInline(admin.StackedInline):
    model = Contact
    fields = ['phone', 'whatsapp', 'email', 'facebook', 'twitter']
    extra = 0


class ObjectiveInline(admin.TabularInline):
    model = Objective
    fields = ['objective']
    extra = 0

class ValueInline(admin.TabularInline):
    model = Value
    fields = ['core_value']
    extra = 0

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Profile', {'fields':['brand', 'about', 'slogan']}),
        ('Mission', {'fields': ['mission']}),
        ('Vision', {'fields': ['vision']}),
    ]

    inlines = [ObjectiveInline, ValueInline, AddressInline, ContactInline]

    list_display = ['brand', 'slogan', 'mission', 'vision']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Bio data', {'fields': ['first_name', 'last_name', 'other_names', 'id_number', 'date_of_birth']}),
        ('Contact information', {'fields': ['phone_number', 'email_address']}),
        ('Other information', {'fields': ['designation', 'profession', 'occupation']}),
        ('Profile photo', {'fields': ['profile_photo']})
    ]

    list_display = ['first_name', 'last_name', 'id_number', 'date_of_birth', 'phone_number', 'email_address', 'designation']
    list_filter = ['designation']
    list_editable = ['date_of_birth']
    list_per_page = 10



class ImpactInline(admin.TabularInline):
    model = Impact
    fields = ['impact_text']
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project info', {'fields': ['thematic_area', 'project_name', 'project_description']}),
        ('Support', {'fields': ['partners', 'donations']}),
        ('Project Timeline', {'fields': ['start_date', 'end_date']}),
        ('Project Media', {'fields': ['media']}),
    ]
    inlines = [ImpactInline]
    list_display = ['project_name', 'start_date', 'has_ended', 'show_donors', 'show_partners']
    list_filter = ['thematic_area', 'start_date']
    search_fields = ['project_name']
    list_per_page = 10
    date_hierarchy = 'start_date'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = (('sender_name', 'phone_number', 'email'), 'message')
    list_display = ['sender_name', 'phone_number', 'email', 'time_of_receipt']
    readonly_fields = ['sender_name', 'phone_number', 'email', 'message']
    date_hierarchy = 'time_of_receipt'


class DescriptionInline(admin.TabularInline):
    model = Job_Description
    fields = ['responsibility']
    extra = 0

class RequirementInline(admin.TabularInline):
    model = Job_Requirement
    fields = ['requirement']
    extra = 0

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['position', 'date_posted']
    inlines = [DescriptionInline, RequirementInline]
    date_hierarchy = 'date_posted'



@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    list_display = ['headline', 'pub_date', 'external_link']
    list_filter = ['pub_date']
    list_per_page = 10
    date_hierarchy = 'pub_date'
    filter_vertical = ['media']


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['donor_name', 'donor_category']
    list_filter = ['donor_category']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['partner_name', 'partner_category']
    list_filter = ['partner_category']


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    #fields = (('caption', 'picture'), 'carousel')
    fieldsets = [
        (None, {'fields': ['picture', 'caption', 'carousel'],
         'description': '<h1 style="color: brown">Take great care not to upload too many or unnecessary photos</h1>'})
    ]
    list_display = ('caption', 'picture', 'carousel')
    list_per_page = 10
