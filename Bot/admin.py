from django.contrib import admin

# Register your models here.
from .models import Team, Member, Sprint, Commitment, VoiceChannelLog, Question, Answer, Checklist

admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Sprint)
admin.site.register(Commitment)
admin.site.register(VoiceChannelLog)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Checklist)