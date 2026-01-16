def calculate_calories_burned(exercise_type, duration_minutes, intensity):
    if exercise_type == "cardio":
        if intensity == "low":
            rate = 8
        elif intensity == "medium":
            rate = 12
        else:
            rate = 16
    elif exercise_type == "strenght":
        if intensity == "low":
            rate = 6
        elif intensity == "medium":
            rate = 9
        else:
            rate = 12
    else:
        if intensity == "low":
            rate = 3
        elif intensity == "medium":
            rate = 5
        else:
            rate = 7
    return rate * duration_minutes

def calculate_heart_rate_zone(age, resing_hr, exercise_hr):
    max_hr = 220 - age
    heart_rate_reserve = max_hr - resing_hr
    intensity_percent = (exercise_hr - resing_hr) / heart_rate_reserve * 100
    return intensity_percent

def determine_training_zone(intensity_percent):
    if intensity_percent < 50:
        return "Warm-up Zone"
    elif intensity_percent < 60:
        return "Fat Burn Zone"
    elif intensity_percent < 70:
        return "Cardio Zone"
    elif intensity_percent < 85:
        return "Performance Zone"
    else:
        return "Maximum Effort Zone"
    
def calculate_workout_score(calories, duration, zone_multiplier):
    base_score = calories * 0.1 + duration * 2
    final_score = base_score * zone_multiplier
    return round(final_score, 1)

def needs_rest_day(consecutive_days, total_minutes, avg_intensity):
    if consecutive_days >= 6:
        return True
    if total_minutes > 450 and avg_intensity > 70:
        return True
    if consecutive_days >= 4 and avg_intensity >80:
        return True
    return False

def generate_workout_report(name, exercise_type, duration, intensity, age, resting_hr, exercise_hr, consecutive_days):
    calories = calculate_calories_burned(exercise_type, duration, intensity)
    intensity_percent = calculate_heart_rate_zone(age, resting_hr, exercise_hr)
    zone = determine_training_zone(intensity_percent)

    if zone == "Warm-up Zone":
        multiplier = 0.5
    elif zone == "Fat Burn Zone":
        multiplier = 1.0
    elif zone == "Cardio Zone":
        multiplier = 1.2
    elif zone == "Performance Zone":
        multiplier = 1.5
    else:
        multiplier = 1.8

    score = calculate_workout_score(calories, duration, multiplier)
    rest_needed = needs_rest_day(consecutive_days, duration, intensity_percent)

    print("========================================")
    print(f"Workout Report for: {name}")
    print("----------------------------------------")
    print(f"Exercise Type: {exercise_type}")
    print(f"Duration: {duration} minutes")
    print(f"Intensity Level: {intensity}")
    print(f"Calories Burned: {calories}")
    print("Heart Rate Analysis:")
    print(f"  Age: {age}, Resting HR: {resting_hr}, Exercise HR: {exercise_hr}")
    print(f"  Intensity: {round(intensity_percent, 1)}%")
    print(f"  Training Zone: {zone}")
    print(f"Workout Score: {score}")
    print(f"Consecutive Training Days: {consecutive_days}")
    print(f"Rest Day Recommended: {'Yes' if rest_needed else 'No'}")
    print()

print("FITNESS PERFORMANCE TRACKER")

generate_workout_report("Alex", "cardio", 45, "high", 28, 65, 155, 3)
generate_workout_report("Jordan", "strenght", 60, "medium", 35, 70, 140, 5)
generate_workout_report("Casey", "flexibily", 30, "low", 42, 68, 95, 7)
