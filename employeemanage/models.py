from django.db import models
from mongoengine import Document, EmbeddedDocument, fields


class Project(EmbeddedDocument):
    projectId = fields.StringField(max_length=10, required=True, null=False)
    name = fields.StringField(max_length=50,required=True)
    startDate = fields.DateTimeField()
    endDate = fields.DateTimeField()

class Skill(EmbeddedDocument):
    tech=fields.StringField(max_length=50, required=True, null=False)
    experience=fields.IntField()
    level=fields.StringField(max_length=50,null=False)

class Employee(Document):
    empId = fields.StringField(max_length=10, required=True, null=False)
    empName = fields.StringField(max_length=100, required=True)
    workLocation = fields.StringField(max_length=255, required=False)
    skills = fields.EmbeddedDocumentListField(Skill)
    projects = fields.EmbeddedDocumentListField(Project)
