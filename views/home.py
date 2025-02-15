#Main User Interface

import tkinter as tk
from tkinter import ttk, messagebox
from controllers.user_controller import register_user
from controllers.diet_controller import recommend_diet

class HomeScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("AI-Based Pet Diet Recommendation")
        self.master.geometry("500x400")
        frame = ttk.Frame(self.master, padding=20)
        frame.grid()
        ttk.Label(frame, text="Owner Name:").grid(row=0, column=0)
        self.entry_name = ttk.Entry(frame)
        self.entry_name.grid(row=0, column=1)
        ttk.Label(frame, text="Pet Name:").grid(row=1, column=0)
        self.entry_pet_name = ttk.Entry(frame)
        self.entry_pet_name.grid(row=1, column=1)
        ttk.Button(frame, text="Register", command=self.register_user).grid(row=2, column=0)
        ttk.Button(frame, text="Recommend Diet", command=self.recommend_diet).grid(row=2, column=1)
    
    def register_user(self):
        register_user(self.entry_name.get(), "email@example.com", self.entry_pet_name.get(), 2, "Breed")
        messagebox.showinfo("Success", "User Registered Successfully")
    
    def recommend_diet(self):
        diet = recommend_diet(2, 10)
        messagebox.showinfo("Diet Recommendation", f"Recommended Diet: {diet}")

