from django.db import models


class cal_history(models.Model):
    num1 = models.CharField(max_length=50)
    num2 = models.CharField(max_length=50)
    op = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.num1} {self.op} {self.num2} = {self.result}"

