from django.db import models


class ExamIndex(models.Model):
    name = models.CharField(max_length=200)
    university = models.CharField(max_length=100)
    date = models.DateField()
    stream = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name


class ExamDetail(models.Model):
    index = models.ForeignKey(ExamIndex, on_delete=models.CASCADE)
    description = models.TextField()
    syallabus = models.TextField()
    eligibility = models.TextField()
    official_website = models.URLField()
    courses_offered = models.TextField()

    def __str__(self):
        return self.index.name
