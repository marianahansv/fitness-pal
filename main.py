import tkinter
from tkinter import ttk
import random

light_pink = "#FFB6C1"
white = "#FFFFFF"
hot_pink = "#FF69B4"
yellow = "#FFFF00"
light_blue = "#ADD8E6"

window = tkinter.Tk()
window.geometry("500x550")
window.configure(bg=hot_pink)

# fonts
font_main = ("Arial", 12, "bold")
font_title = ("Arial", 20, "bold")

finalWorkout = ""  # stores the workout text to save later

# get values from the inputs (handles empty cases too)
def getWorkoutSpecs():
    sets = sets_input.get()
    rounds = rounds_input.get()
    exercises = exercises_input.get()
    
    if sets == "" or rounds == "" or exercises == "":
        return [0, 0, 0]
    else:
        return [int(sets), int(rounds), int(exercises)]

# turn list into text
def listToText(workout_list):
    text = ""
    for line in workout_list:
        text += "\t" + line + "\n"
    return text

# make the workout based on inputs
def generateWorkout(box):
    global finalWorkout
    values = getWorkoutSpecs()
    sets = values[0]
    rounds = values[1]
    exercises_per_set = values[2]
    
    exercises = ["15 Push-up", "15 Squat", "15 Pull-up", "15 Deadlift", "15 Bench press", "15 Lunges", "15 Plank", "15 Bicep curl",
                 "15 Tricep dip", "15 Leg press", "15 Leg curl", "15 Lat pull-down", "15 Dumbbell row", "15 Overhead press",
                 "15 Kettlebell swing", "15 Jump squat", "15 Mountain climber", "15 Russian twist", "15 Bicycle crunch", "15 Side plank",
                 "15 Dumbbell chest press", "15 Barbell squat", "15 Calf raise", "15 Glute bridge", "15 Box jump", "15 Jumping jack",
                 "15 Burpee", "15 Wall sit", "15 Bulgarian split squat", "15 Cable row", "15 Hip thrust", "15 Jump lunge",
                 "15 Flutter kick", "15 Tricep pushdown", "15 Chest fly", "15 Upright row", "15 Dumbbell snatch",
                 "15 Leg extension", "15 Renegade row", "15 Step-up", "15 Romanian deadlift", "15 Lateral raise"]
    
    finalWorkout = "Repeat " + str(rounds) + " times\n"
    
    for n in range(sets):
        set = []
        finalWorkout += "Set " + str(n + 1) + "\n"
        for _ in range(exercises_per_set):
            i = random.randint(0, len(exercises) - 1)
            if exercises[i] not in set:
                set.append(exercises[i])
            else:
                while exercises[i] in set:
                    i = random.randint(0, len(exercises) - 1)
                set.append(exercises[i])
        finalWorkout += listToText(set) + "\n"

    box.delete(1.0, tkinter.END)
    box.insert("insert", finalWorkout)

# clear all fields
def clearForm(box, sets, rounds, exercises):
    box.delete(1.0, tkinter.END)
    sets.delete(0, tkinter.END)
    rounds.delete(0, tkinter.END)
    exercises.delete(0, tkinter.END)

# save the workout to a file
def saveWorkout(box):
    global finalWorkout
    if finalWorkout:
        with open("workouts.txt", "a") as file:
            file.write("Workout:\n" + finalWorkout)

title = tkinter.Label(window, text="Fitness Pal ;)", font=font_title, bg=hot_pink, fg=light_blue)
title.pack(pady=15)

# input 
sets_label = tkinter.Label(window, text="How many sets?", bg="#FF69B4", fg=yellow, font=font_main)
sets_label.pack()
sets_input = ttk.Entry(window, font=font_main)
sets_input.configure(background=light_pink, foreground=hot_pink)
sets_input.pack()

rounds_label = tkinter.Label(window, text="How many rounds?", bg="#FF69B4", fg=yellow, font=font_main)
rounds_label.pack()
rounds_input = ttk.Entry(window, font=font_main)
rounds_input.configure(background=light_pink, foreground=hot_pink)
rounds_input.pack()

exercises_label = tkinter.Label(window, text="How many exercises per set?", bg="#FF69B4", fg=yellow, font=font_main)
exercises_label.pack()
exercises_input = ttk.Entry(window, font=font_main)
exercises_input.configure(background=light_pink, foreground=hot_pink)
exercises_input.pack()

# workout box
box = tkinter.Text(window, height=10, width=40, font=font_main, bg=white, fg=hot_pink)
box.pack(pady=15)

# buttons (put them in a frame so they’re in a row)
button_frame = tkinter.Frame(window, bg=hot_pink)
button_frame.pack()

genWorkoutButton = tkinter.Button(button_frame, text="Generate Workout", command=lambda: generateWorkout(box), font=font_main, bg=light_blue, fg=hot_pink)
genWorkoutButton.grid(row=0, column=0, padx=5, pady=5)

clearButton = tkinter.Button(button_frame, text="Clear", command=lambda: clearForm(box, sets_input, rounds_input, exercises_input), font=font_main, bg=light_blue, fg=hot_pink)
clearButton.grid(row=0, column=1, padx=5, pady=5)

saveButton = tkinter.Button(button_frame, text="Save Workout", command=lambda: saveWorkout(box), font=font_main, bg=light_blue, fg=hot_pink)
saveButton.grid(row=0, column=2, padx=5, pady=5)

window.mainloop()
