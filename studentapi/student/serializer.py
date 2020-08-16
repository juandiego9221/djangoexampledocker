#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers 
from student.models import Student

class StudentSerializer(serializers.Serializer):
    pk=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    age=serializers.IntegerField()

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.save()
        return instance

