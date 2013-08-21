from django.db import models


class User(models.Model):
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.username


class IssueType(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name		


class IssueRecord(models.Model):
	issueName = models.CharField(max_length = 100)
	solution  = models.CharField(max_length = 100)
	qq = models.CharField(max_length = 20, blank=True)
	phone = models.CharField(max_length = 20, blank=True)

	def __unicode__(self):
		return self.issueName