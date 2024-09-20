from tkinter import Button, Canvas, Tk, PhotoImage, Label
import math

# ---------------------------- CONSTANTS ------------------------------- #
ORANGE = "#FC6736"
RED = "#FE0000"
GREEN = "#5D9C59"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
BLUE="#0079FF"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


def reset_timer():
  global timer, reps
  reps = 0
  window.after_cancel(timer)
  check_mark.config(text="")
  timer_label.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timer_text, text="00:00")

 
def start_timer():
  global reps 
  reps += 1
  work_min = WORK_MIN * 60
  short_break_min = SHORT_BREAK_MIN * 60
  long_break_min = LONG_BREAK_MIN * 60
  print(f"este es el valor de reps {reps}")
  if str(reps) == "8" :
    timer_label.config(text="LONG BREAK", fg=RED, font=(FONT_NAME, 20, "bold"))
    count_down(long_break_min)
  elif reps % 2 != 0 :
    timer_label.config(text="LEARNING", fg=GREEN, font=(FONT_NAME, 20, "bold"))
    count_down(work_min)
  else :
    timer_label.config(text="SHORT BREAK", fg=ORANGE, font=(FONT_NAME, 20, "bold"))
    count_down(short_break_min)

def count_down(count):
  global reps
  count_min = math.floor(count/60)
  count_sec = count % 60
  if count_sec < 10 or count_sec == 0:
    count_sec = f"0{count_sec}"
  if count_min < 10 or count_min == 0:
    count_min = f"0{count_min}"
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    marks = ""
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
      marks += "✔"
      check_mark.config(text=marks)
    start_timer()

window = Tk()
window.title("Pomodoro technique By Aaron D.")
window.config(padx=30, pady=25, width=400, height=300, bg=YELLOW)
window.resizable(False, False)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=3)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_label.grid(column=1, row=1)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25))
check_mark.grid(column=1, row=5)

start_boton = Button(text="Start", highlightthickness=0, command=start_timer)
start_boton.grid(column=0, row=4)

reset_boton = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_boton.grid(column=2, row=4)

window.mainloop()

