from django.db.models import Count, Sum
from django.views.generic import ListView

from models import Job


class JobListView(ListView):
    model = Job

    def get_queryset(self):
        order_by = "-%s" % self.request.GET.get("order_by", "total_memory")
        return Job.objects.values("owner").annotate(total_memory=Sum("ru_maxrss"), total_slots=Sum("slots"), total_jobs=Count("jobnumber")).order_by(order_by)
