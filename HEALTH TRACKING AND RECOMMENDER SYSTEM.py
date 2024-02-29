import tkinter as tk
from tkinter import ttk, messagebox
import json
import random

# Function to save user data to a JSON file
def save_user_data():
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)

# Function to load user data from a JSON file
def load_user_data():
    global user_data
    try:
        with open('user_data.json', 'r') as file:
            data = file.read()
            if data:
                user_data = json.loads(data)
            else:
                user_data = {}
    except (FileNotFoundError, json.JSONDecodeError):
        user_data = {}

# Global dictionary to store user registration data
user_data = {}

# Call the function to load user data
load_user_data()

# Function to register a new user
def register_user():
    username = username_var.get()
    password = password_var.get()
    
    # Check if the username already exists
    if username in user_data:
        messagebox.showerror("Registration Error", "Username already exists. Please choose a different username.")
    else:
        user_data[username] = password
        save_user_data()
        messagebox.showinfo("Registration Successful", "You have successfully registered!")

# Function to log in a user
def login_user():
    username = login_username_var.get()
    password = login_password_var.get()
    
    # Check if the username and password match
    if username in user_data and user_data[username] == password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        open_health_tracking_frame()  # Open the health tracking frame after successful login
    else:
        messagebox.showerror("Login Error", "Invalid username or password. Please try again.")

# Function to open the health tracking frame
def open_health_tracking_frame():
    # Hide the login frame
    login_frame.pack_forget()
    
    # Create and display the health tracking frame
    health_tracking_frame = ttk.Frame(root)
    health_tracking_frame.pack()
    
    # Add widgets and functionality for the health tracking page here
    # For example, you can add labels, entry widgets, buttons, etc.

# Function to initialize the health tracking system frame
def initialize_health_tracking():
    global health_tracking_frame
    health_tracking_frame = ttk.Frame(root)
    
    # Add widgets and functionality for the health tracking page here
    # For example, you can add labels, entry widgets, buttons, etc.

    # Initially, keep the health tracking frame hidden
    health_tracking_frame.pack_forget()

# ...

# Create the main application window
root = tk.Tk()
root.title('HEALTH TRACKING AND RECOMMENDER SYSTEM')
root.config(bg='#37C6FF')

# Create variables for registration and login input
username_var = tk.StringVar()
password_var = tk.StringVar()
login_username_var = tk.StringVar()
login_password_var = tk.StringVar()

# Create a frame for registration
register_frame = ttk.Frame(root)

# Create a label for the registration page
register_label = ttk.Label(register_frame, text='Registration', font=("Helvetica", 16, "bold"))
register_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create labels and entry widgets for registration input
username_label = ttk.Label(register_frame, text='Username:')
username_label.grid(row=1, column=0, padx=10, pady=5)
username_entry = ttk.Entry(register_frame, textvariable=username_var)
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_label = ttk.Label(register_frame, text='Password:')
password_label.grid(row=2, column=0, padx=10, pady=5)
password_entry = ttk.Entry(register_frame, textvariable=password_var, show='*')
password_entry.grid(row=2, column=1, padx=10, pady=5)

register_button = ttk.Button(register_frame, text='Register', command=register_user)
register_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create a frame for login
login_frame = ttk.Frame(root)

# Create a label for the login page
login_label = ttk.Label(login_frame, text='Login', font=("Helvetica", 16, "bold"))
login_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create labels and entry widgets for login input
login_username_label = ttk.Label(login_frame, text='Username:')
login_username_label.grid(row=1, column=0, padx=10, pady=5)
login_username_entry = ttk.Entry(login_frame, textvariable=login_username_var)
login_username_entry.grid(row=1, column=1, padx=10, pady=5)

login_password_label = ttk.Label(login_frame, text='Password:')
login_password_label.grid(row=2, column=0, padx=10, pady=5)
login_password_entry = ttk.Entry(login_frame, textvariable=login_password_var, show='*')
login_password_entry.grid(row=2, column=1, padx=10, pady=5)

login_button = ttk.Button(login_frame, text='Login', command=login_user)
login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create buttons to switch between registration and login pages
register_page_button = ttk.Button(root, text='Register Page', command=register_frame.pack)
register_page_button.pack(padx=10, pady=10)

login_page_button = ttk.Button(root, text='Login Page', command=login_frame.pack)
login_page_button.pack(padx=10, pady=10)

# Function to log out and switch back to the login frame
def logout_user():
    health_tracking_frame.pack_forget()
    login_frame.pack()

# ...

# Create a frame for the health tracking system
initialize_health_tracking()

root.mainloop()



import tkinter as tk
from tkinter import ttk, messagebox
import random





# Global dictionary to store user registration data
user_data = {}

def submit_details():
    name = name_var.get()
    gender = gender_var.get()
    age = age_var.get()
    height = height_var.get()
    weight = weight_var.get()
    bp_level = bp_level_var.get()
    heart_beat = heart_beat_var.get()

    # Display the details in a pop-up message
    details = f"Name: {name}\nGender: {gender}\nAge: {age}\nHeight: {height} cm\nWeight: {weight} kg\nBP Level: {bp_level}\nHeart Beat: {heart_beat}"
    messagebox.showinfo("User Details", details)

def calculate_bmi():
    user_height = height_var.get() / 100
    user_weight = weight_var.get()
    bmi = user_weight / (user_height ** 2)

    # Display BMI in a pop-up message
    messagebox.showinfo("BMI Calculator", f"Your BMI is: {bmi:.2f}")

    # Call the function to provide recommendations based on the calculated BMI
    provide_bmi_recommendations(bmi)

def calculate_bp_level():
    bp_level = bp_level_var.get()

    if bp_level <= 90:
        messagebox.showinfo("Blood Pressure Level", "Your BP level is LOW (Hypotension). Consult a doctor.")
    elif 90 < bp_level <= 120:
        messagebox.showinfo("Blood Pressure Level", "Your BP level is GOOD and HEALTHY.")
    else:
        messagebox.showinfo("Blood Pressure Level", "Your BP level is HIGH (Hypertension). Consult a doctor.")

def calculate_heart_beat():
    # Add your heart rate calculation logic here (if needed)
    messagebox.showinfo("Heart Beat Checker", "Your heart rate has been checked.")

def provide_bmi_recommendations(bmi):
    # Add your BMI-based diet recommendations here based on the calculated BMI
    if bmi < 18.5:
        recommendations = "You are underweight. Consider increasing your calorie intake."
    elif 18.5 <= bmi < 24.9:
        recommendations = "You have a normal weight. Maintain a balanced diet."
    elif 24.9 <= bmi < 29.9:
        recommendations = "You are overweight. Consider reducing your calorie intake and exercising regularly."
    else:
        recommendations = "You are obese. Consult a doctor for a personalized weight management plan."

    messagebox.showinfo("BMI Diet Recommender", recommendations)

def show_health_recommendations():
    # You can customize these recommendations based on the user's health parameters
    recommendations = [
        "Maintain a balanced diet with plenty of fruits and vegetables.",
        "Engage in regular physical activity (e.g., 30 minutes of brisk walking daily).",
        "Get adequate sleep (7-9 hours per night).",
        "Stay hydrated by drinking enough water throughout the day.",
        "Manage stress through relaxation techniques or meditation.",
        "Avoid smoking and limit alcohol consumption.",
    ]

    # Display recommendations in a messagebox
    messagebox.showinfo("Health Recommendations", "\n".join(recommendations))

health_quotes = [
    "Health is wealth.",
    "A healthy outside starts from the inside.",
    "The greatest wealth is health.",
    "Take care of your body. It's the only place you have to live.",
    "An apple a day keeps the doctor away."]


def health_quote():
    random_quote = random.choice(health_quotes)
    messagebox.showinfo("Health Quote", random_quote)

def provide_dish_recommendations(bmi, bp_level):
    recommendations = []

    if bmi < 18.5:
        recommendations.append("For your BMI, consider meals with healthy fats and proteins.")
    elif 18.5 <= bmi < 24.9:
        recommendations.append("Maintain a balanced diet with a variety of fruits, vegetables, and lean proteins.")
    elif 24.9 <= bmi < 29.9:
        recommendations.append("To manage your weight, focus on portion control and exercise. Try salads and grilled chicken.")
    else:
        recommendations.append("For your BMI, consult a nutritionist for personalized dietary advice.")

    if bp_level <= 90:
        recommendations.append("For low BP, include more salt and fluids in your diet.")
    elif 90 < bp_level <= 120:
        recommendations.append("Maintain your current diet for healthy BP levels.")
    else:
        recommendations.append("For high BP, reduce sodium intake and avoid processed foods.")

    messagebox.showinfo("Dish Recommendations", "\n".join(recommendations))

def show_dish_recommendations():
    # Calculate BMI (you can reuse your existing calculation code)
    user_height = height_var.get() / 100
    user_weight = weight_var.get()
    bmi = user_weight / (user_height ** 2)

    # Get BP level from the input
    bp_level = bp_level_var.get()

    # Call the function to provide dish recommendations
    provide_dish_recommendations(bmi, bp_level)

# Create the main application window
root = tk.Tk()
root.title('HEALTH TRACKING AND RECOMMENDER SYSTEM')
root.config(bg='#37C6FF')

# Create variables for user input
name_var = tk.StringVar()
gender_var = tk.StringVar()
age_var = tk.IntVar()
height_var = tk.IntVar()
weight_var = tk.IntVar()
bp_level_var = tk.IntVar()
heart_beat_var = tk.IntVar()

# Create the main frame
main_frame = ttk.Frame(root)
main_frame.pack()

# Create labels and entry widgets for user input
name_label = ttk.Label(main_frame, text='Name:')
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = ttk.Entry(main_frame, textvariable=name_var)
name_entry.grid(row=0, column=1, padx=10, pady=5)

gender_label = ttk.Label(main_frame, text='Gender:')
gender_label.grid(row=1, column=0, padx=10, pady=5)
gender_entry = ttk.Combobox(main_frame, textvariable=gender_var, values=['Male', 'Female'])
gender_entry.grid(row=1, column=1, padx=10, pady=5)
gender_entry.set('Male')  # Default value

age_label = ttk.Label(main_frame, text='Age:')
age_label.grid(row=2, column=0, padx=10, pady=5)
age_entry = ttk.Entry(main_frame, textvariable=age_var)
age_entry.grid(row=2, column=1, padx=10, pady=5)

height_label = ttk.Label(main_frame, text='Height (in cm):')
height_label.grid(row=3, column=0, padx=10, pady=5)
height_entry = ttk.Entry(main_frame, textvariable=height_var)
height_entry.grid(row=3, column=1, padx=10, pady=5)

weight_label = ttk.Label(main_frame, text='Weight (in kg):')
weight_label.grid(row=4, column=0, padx=10, pady=5)
weight_entry = ttk.Entry(main_frame, textvariable=weight_var)
weight_entry.grid(row=4, column=1, padx=10, pady=5)

bp_level_label = ttk.Label(main_frame, text='BP Level:')
bp_level_label.grid(row=5, column=0, padx=10, pady=5)
bp_level_entry = ttk.Entry(main_frame, textvariable=bp_level_var)
bp_level_entry.grid(row=5, column=1, padx=10, pady=5)

heart_beat_label = ttk.Label(main_frame, text='Heart Beat:')
heart_beat_label.grid(row=6, column=0, padx=10, pady=5)
heart_beat_entry = ttk.Entry(main_frame, textvariable=heart_beat_var)
heart_beat_entry.grid(row=6, column=1, padx=10, pady=5)

# Create buttons for actions
submit_button = ttk.Button(main_frame, text='Submit', command=submit_details)
submit_button.grid(row=7, column=0, padx=10, pady=10)

bmi_button = ttk.Button(main_frame, text='Calculate BMI', command=calculate_bmi)
bmi_button.grid(row=7, column=1, padx=10, pady=10)

bp_level_button = ttk.Button(main_frame, text='Check BP Level', command=calculate_bp_level)
bp_level_button.grid(row=8, column=0, padx=10, pady=10)

heart_beat_button = ttk.Button(main_frame, text='Check Heart Beat', command=calculate_heart_beat)
heart_beat_button.grid(row=8, column=1, padx=10, pady=10)

health_recommender_button = ttk.Button(main_frame, text='Health Recommendations', command=show_health_recommendations)
health_recommender_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)


health_quote_button = ttk.Button(main_frame, text='Health Quote', command=health_quote)
health_quote_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)




dish_recommendations_button = ttk.Button(main_frame, text='Dish Recommendations', command=show_dish_recommendations)
dish_recommendations_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

