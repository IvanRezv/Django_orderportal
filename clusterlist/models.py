from django.db import models


class Cluster(models.Model):
    system_name = models.CharField(max_length=100, null=True)
    rds_link = models.CharField(max_length=100, null=True)
    rds_status = models.CharField(max_length=100, null=True)
    lt_namespace = models.CharField(max_length=100, null=True)
    lt_cluster = models.CharField(max_length=100, null=True)
    prod_namespace = models.CharField(max_length=100, null=True)
    prod_cluster = models.CharField(max_length=100, null=True)
    acc_requests = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.system_name
