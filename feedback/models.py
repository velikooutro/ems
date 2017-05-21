from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator


class Feedback(models.Model):

	CATEGORY_CHOICES = (
			('1', 'General'),
			('2', 'Management'),
			('3', 'Compensation'),
			('4', 'Suggestions'),
			('5', 'Complaint'),
		)

	name = models.CharField(max_length=100)
	subject = models.CharField(max_length=200)
	category = models.CharField(max_length=10, default='1', choices=CATEGORY_CHOICES)
	email = models.CharField(max_length=150, validators=[EmailValidator(),MinLengthValidator(7),MaxLengthValidator(10,message="too long")])
	comment = models.CharField(max_length=500)
	is_read = models.BooleanField(default=False)
	created_on = models.DateTimeField(default=timezone.now, null=False)

	def __str__(self):
		return self.email

	class Meta:
		db_table = 'feedback'