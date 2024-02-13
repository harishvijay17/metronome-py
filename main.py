from tkinter import *
import winsound

class Metronome:
    def __init__(self):
        self.root = Tk()

        self.tempo = 40
        self.beat = 1

        time_signatures = ["4/4", "2/4", "3/4", "5/4", "6/4"]
        self.variable = StringVar(self.root)
        self.variable.set("4/4")

        self.tempo_label = Label(self.root, text = f"{self.tempo} bpm", bg="#d3d3d3", borderwidth=2, relief="ridge")
        self.tempo_label.config(font=("Arial", 36))
        self.tempo_label.grid(row=0, column=1)

        self.tempo_word = Label(self.root, bg="#d3d3d3", borderwidth=2)
        self.tempo_word.config(font=("Arial", 14))
        self.tempo_word.grid(row=1, column=1, pady=5)

        self.started = False

        start_btn = Button(self.root, text = "Start", command=self.play_start, background="#90EE90")
        start_btn.grid(row=2, column=0, padx=5, pady=5)

        stop_btn = Button(self.root, text = "Stop", command=self.stop, background="#FF7F7F")
        stop_btn.grid(row=2, column=2, padx=5, pady=5)

        self.slider = Scale(self.root, length=300, from_=40, to=220, orient=HORIZONTAL, command=self.update_label)
        self.slider.config(background="#ADD8E6", troughcolor="#d3d3d3")

        self.slider.set(80)
        self.slider.grid(row=2, column=1)

        ts_select = OptionMenu(self.root, self.variable, *time_signatures)
        ts_select.config(bg="#ADD8E6")
        ts_select.grid(row=3, column=1, pady=5)

        self.update_label()
        mainloop()
    
    def play(self):
        if self.started:
            if self.beat > int(self.variable.get()[0:1]):
                self.beat = 1

            self.update_label()
            self.tempo = self.slider.get()
            winsound.Beep(440 if self.beat != 1 else 880, 100)

            self.root.after(int(60000 / self.tempo - 100), self.play)
            self.beat += 1

    def play_start(self):
        if self.started == True:
            return
    
        self.started = True
        self.play()

    def stop(self):
        self.started = False
    
    def update_label(self, event = 0):
        self.tempo = self.slider.get()
        self.tempo_label.configure(text=f"{self.tempo} bpm")

        text = ""
        if self.tempo <= 60:
            text = "Largo"
        elif self.tempo <= 76:
            text = "Adagio"
        elif self.tempo <= 108:
            text = "Andante"
        elif self.tempo <= 120:
            text = "Allegretto" 
        elif self.tempo <= 156:
            text = "Allegro" 
        elif self.tempo <= 200:
            text = "Presto" 
        else:
            text = "Prestissimo"

        self.tempo_word.configure(text=text)

def main():
    Metronome()

if __name__ == "__main__":
    main()
