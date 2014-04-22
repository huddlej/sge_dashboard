from django.db import models


class Job(models.Model):
    """
    Represents a completed job from a grid engine system as reported by
    ``qacct``.

    Only a subset of all reported fields are represented here.
    """
    jobnumber = models.IntegerField()
    qname = models.CharField(max_length=20)
    hostname = models.CharField(max_length=100)
    owner = models.CharField(max_length=8)
    jobname = models.CharField(max_length=100)
    slots = models.IntegerField()
    exit_status = models.IntegerField()
    ru_wallclock = models.IntegerField(help="Run time")
    ru_maxrss = models.IntegerField(help="Max memory used")
    ru_inblock = models.IntegerField()
    ru_oublock = models.IntegerField()
