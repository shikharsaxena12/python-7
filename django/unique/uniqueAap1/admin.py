from django.contrib import admin
from .models import cal_history


@admin.register(cal_history)
class cal_historyAdmin(admin.ModelAdmin):
    list_display = ("id", "num1", "op", "num2", "result", "Created_at")
    search_fields = ("num1", "num2", "result")
    list_filter = ("op", "Created_at")
    ordering = ("-Created_at",)

