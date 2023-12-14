import pyautogui
import tkinter as tk
import time
import random
import threading

is_automation_running = threading.Event()

def move_mouse_randomly():
    screen_width, screen_height = pyautogui.size()
    x, y = random.randint(0, screen_width), random.randint(0, screen_height)
    pyautogui.moveTo(x, y, duration=0.25)

def start_automation():
    global is_automation_running

    if is_automation_running.is_set():
        return

    minutes = float(minutes_entry.get())

    total_time = minutes * 60

    print(f"Automação será executada por {minutes} minutos.")
    is_automation_running.set()

    def automation_thread():
        for _ in range(int(total_time // 10)):
            if not is_automation_running.is_set():
                break
            move_mouse_randomly()
            time.sleep(10)

        is_automation_running.clear()

    automation_thread = threading.Thread(target=automation_thread)
    automation_thread.start()

def stop_automation():
    global is_automation_running
    is_automation_running.clear()
    print("Automação interrompida.")

app = tk.Tk()
app.title("Automação de Mouse")
app.geometry("300x100+0+0")  # Define o tamanho e a posição da janela

# Criação de widgets
label1 = tk.Label(app, text="Digite o tempo em minutos:")
minutes_entry = tk.Entry(app)
start_button = tk.Button(app, text="Iniciar Automação", command=start_automation)
stop_button = tk.Button(app, text="Parar Automação", command=stop_automation)

# Layout dos widgets
label1.pack()
minutes_entry.pack()
start_button.pack()
stop_button.pack()

app.mainloop()
