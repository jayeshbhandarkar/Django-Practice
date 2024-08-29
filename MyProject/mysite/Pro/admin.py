from django.contrib import admin
from Pro.models import Contact

from Pro.models import TeamMember
from .models import Musician, Album

# Register your models here.
admin.site.register(Contact),
admin.site.register(TeamMember),
admin.site.register(Musician),
admin.site.register(Album)