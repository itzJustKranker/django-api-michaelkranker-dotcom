from django.db import models
from config.models import AuditedEntity


class Contact(AuditedEntity):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"


class RequestForProposal(AuditedEntity):
    class Relationship(models.IntegerChoices):
        PROJECT_BASED = 0
        MAINTENANCE = 1
        RETAINER = 2

    class SiteType(models.IntegerChoices):
        DYNAMIC = 0
        STATIC = 1
        N_A = 2

    class Timeline(models.IntegerChoices):
        ONE_THREE = 0
        THREE_SIX = 1
        SIX_PLUS = 2
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    company_overview = models.TextField()
    project_overview = models.TextField()
    goals_objectives = models.TextField()
    relationship = models.IntegerField(
        choices=Relationship.choices,
        default=0
    )
    problem = models.TextField()
    site_type = models.IntegerField(
        choices=SiteType.choices,
        default=0
    )
    website_url = models.CharField(max_length=250)
    budget = models.CharField(max_length=250)
    timeline = models.IntegerField(
        choices=Timeline.choices,
        default=0
    )
    referral = models.TextField()
    comments = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.company_name}"
