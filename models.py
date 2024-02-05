import uuid

from django.db import models

"""
Create an "Exercise" class with the following specifications:
1) Name
2) Number of Sets
3) Number of Reps
4) Primary Tags
5) Secondary Tags
6) Compound/Isolation Tag
"""


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=100)
    num_sets = models.IntegerField(default=0)
    num_reps = models.IntegerField(default=0)
    primary_tag = models.CharField(max_length=100, blank=True)
    secondary_tag = models.CharField(max_length=100, blank=True)
    compound_iso_tag = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.exercise_name

"""
Create an "ExerciseLog" class with the following specifications:
1) Associated exercise via ForeignKey
2) Timestamp
3) Current Set
4) Current Weight
5) Target Weight
"""
class ExerciseLog(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    set = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    target_weight = models.FloatField(default=0)

"""
Create a "Workouts" class with the following specifications:
1) Name
2) Associated Exercises via ManyToMany relationship
3) Primary Tags
4) Secondary Tags
5) ID
"""


class Workout(models.Model):
    workout_name = models.CharField(max_length=100)
    primary_tag = models.CharField(max_length=100, blank=True)
    secondary_tag = models.CharField(max_length=100, blank=True)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.workout_name
    # Test in use here


"""
Create a "Rotation" class with the following specifications:
1) ID
2) Name
3) Selected Workouts via ManyToMany relationship
"""


class Rotation(models.Model):
    rotation_name = models.CharField(max_length=100)
    workouts = models.ManyToManyField('Workout')

    def __str__(self):
        return self.rotation_name

"""
Create a "Session" class with the following specifications:
2) Start time
3) End time
4) Selected rotation via ForeignKey
5) An iterating tracker of specified number of cycles through the selected rotation
"""

class Session(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    rotation = models.ForeignKey(Rotation, on_delete=models.CASCADE)
    exercise_activity = models.ManyToManyField('ExerciseLog') # set of ExerciseLog
    # Later implementation: an autoincrementing integer that increments once a rotation is finished:
    # num_cycle = models.AutoField()
