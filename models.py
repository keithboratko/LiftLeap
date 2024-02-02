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
7) ID
8) Primary Key(id)
"""


class Exercise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    exercise_name = models.CharField(max_length=100)
    num_sets = models.IntegerField(default=0)
    num_reps = models.IntegerField(default=0)
    primary_tag = models.CharField(max_length=100, blank=True)
    secondary_tag = models.CharField(max_length=100, blank=True)
    compound_iso_tag = models.CharField(max_length=100, blank=True)


"""
Questions for Mike:
    - Is a model field required by default unless we specify 'blank=True'?
    - The ID variable above is an autofill; does this look correct?
"""

"""
Create a "Workouts" class with the following specifications:
1) Name
2) Associated Exercises via ManyToMany relationship
3) Primary Tags
4) Secondary Tags
5) ID
"""


class Workout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    workout_name = models.CharField(max_length=100)
    primary_tag = models.CharField(max_length=100, blank=True)
    secondary_tag = models.CharField(max_length=100, blank=True)
    exercises = models.ManyToManyField('Exercise')


"""
For Mike:
    - Is the definition of 'exercises' correct here or should the "ManyToManyField" relationship be defined elsewhere?
"""

"""
Create a "Rotation" class with the following specifications:
1) ID
2) Name
3) Selected Workouts via ManyToMany relationship
"""


class Rotation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    rotation_name = models.CharField(max_length=200)
    workouts = models.ManyToManyField('Workout')


"""
Create a "Session" class with the following specifications:
1) ID
2) Start time
3) End time
4) Selected rotation via ForeignKey
5) An iterating tracker of specified number of cycles through the selected rotation
"""

"""
For Mike:
    - We specified that we wanted the "Macrocycle" section to be internal logic and to skip it for now. I feel like this is the point where that would come into play: defining how many iterations through a Rotation are performed... how do we approach this internally? Do we hardcode it for now?
"""


class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    rotation = models.ForeignKey(Rotation, on_delete=models.CASCADE)
    # Iterating tracker of (hardcoded for now?) number of cycles through a selected Rotation here...
