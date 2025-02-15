#Main Application File (Tkinter GUI)

import tkinter as tk
from views import home

def main():
    root = tk.Tk()
    app = home.HomeScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
