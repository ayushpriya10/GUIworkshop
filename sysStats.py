import psutil
from tkinter import *
import time

def drawBar(window, canvas, x, mx):
    l = list(range(200))
    l.reverse()

    if mx < 50:
        color = 'cyan'
    elif mx > 50 and mx <76:
        color = 'orange'
    elif mx > 75:
        color = 'red'

    for i in l:
        if i == 200 - 2*mx:
            break
        canvas.create_line(x,  200, x, i, width = 20, fill = color)
        canvas.after(3)
        canvas.update()

    label = Label(window, text = str(mx)+'%')
    label.place(x = x-12, y = 180 - 2*mx)

def popup():
    window = Tk()

    cpu = int(psutil.cpu_percent(interval = 1) + 0.5)
    ram = int(psutil.virtual_memory().percent + 0.5)
    partitions = psutil.disk_partitions()
    partitions = [x.device for x in partitions if x.opts == 'rw,fixed']
    hdd_total = sum([psutil.disk_usage(x).total for x in partitions])
    hdd_used = sum([psutil.disk_usage(x).used for x in partitions])
    #hdd = int((hdd_used/hdd_total)*100 + 0.5)

    def hide():
        window.destroy()
        time.sleep(5)
        popup()

    window.title('Stats')
    canvas = Canvas(window, height = 270, width = 160)
    canvas.pack()

    drawBar(window, canvas, 40, cpu)
    Label(window, text = 'CPU').place(x = 25, y = 200)

    drawBar(window, canvas, 80, ram)
    Label(window, text = 'RAM').place(x = 65, y = 200)

    #drawBar(window, canvas, 120, hdd)
    #Label(window, text = 'HDD').place(x = 105, y = 200)

    b1 = Button(window, text = 'Okay', command = hide)
    b1.place(x = 60, y = 230)

    window.mainloop()

popup()
