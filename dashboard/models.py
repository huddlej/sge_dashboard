from django.db import models


class Job(models.Model):
    """
    Represents a completed job from a grid engine system as reported by
    ``qacct``.

    Only a subset of all reported fields are represented here.
    """
    job_id = models.IntegerField()
    queue = models.CharField(max_length=20)
    hostname = models.CharField(max_length=100)
    owner = models.CharField(max_length=8)
    job_name = models.CharField(max_length=100)
    slots = models.IntegerField()
    exit_status = models.IntegerField()
    run_time = models.IntegerField()
    memory_used = models.IntegerField()
    block_input_operations = models.IntegerField()
    block_output_operations = models.IntegerField()
