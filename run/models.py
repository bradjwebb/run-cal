from django.db import models
from django.utils import timezone

# under construction

class Day(models.Model):
    runner = models.ForeignKey('auth.user')
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.TextField(editable=False)
    run_type = models.CharField(max_length=2)
    pace_fast = models.DurationField()
    pace_slow = models.DurationField()
    pace_mid = models.DurationField()
    elapsed_time = models.DurationField()
    special = models.TextField()
    run_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # def set_pace(self):
    #     if self.pace_fast and self.pace_slow:


    # def set_title(self):
    #     run_type = self.run_type
    #     distance = self.distance
    #     pace = self.pace
    #     run_title = '{0} mile {1} run, @{2}/mi'.format(run_type, distance, pace)
    #     self.title = run_title
    #     return self.title

    def __str__(self):
        return self.title
