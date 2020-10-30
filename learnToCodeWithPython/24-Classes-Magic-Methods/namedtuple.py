import collections

# Use the namedtuple function to create a GymExercise class whose 
# instances will have three attributes: name, weight, and reps.
GymExercise = collections.namedtuple("GymExercise", ["name", "weight", "reps"])
print("The string produced by GymExercise is ", GymExercise)

# Assign a squat variable to a GymExercise tuple object with a name 
# of “squat”, a weight of 265, and a rep count of 3.
squat = GymExercise("squat", 265, 3)
print("The squat exercise has the following values",squat)

# Assign a bench variable to a GymExercise tuple object with a name 
# of “benchpress”, a weight of 185, and a rep count of 5.
bench_press = GymExercise(name="benchpress", weight=185, reps = 5)
print("The bench press name is ",bench_press[0],"and weight = ",bench_press[1],"and reps =", bench_press[2])

# Assign a deadlift variable to a GymExercise tuple object with a name 
# of “deadlift”, a weight of 225, and a rep count of 6.
deadlift = GymExercise(name="deadlift", weight=225, reps = 6)
print(f"The name is { deadlift.name } and the weight is { deadlift.weight } and the reps is { deadlift.reps}")