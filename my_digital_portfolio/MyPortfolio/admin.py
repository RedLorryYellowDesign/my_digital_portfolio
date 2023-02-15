from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount

# Register your models here.
# This allows us to see and contriole these objects from the Admin Pannel
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)


# class ListingAdmin(admin.ModelAdmin):
#     list_display = [f.name for f in Listing. _meta. fields]

# admin.site.register (Listing, ListingAdmin)
