import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
import cv2



class App:
    def __init__(self, window, cap):
        self.window = window
        self.window.title('miptdpo1-078')
        self.cap = cap
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.update_time = 50
        self.brightness_val = 1

        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack()

        self.exit_button = tk.Button(self.window, text='exit', command=self.exit)
        self.exit_button.pack(side=tk.RIGHT, fill=tk.Y)
        self.snapshot_button = tk.Button(self.window, text='snapshot', command=self.snapshot)
        self.snapshot_button.pack(side=tk.LEFT, fill=tk.Y)
        self.entry = tk.Entry(self.window)
        self.entry.pack(fill=tk.X)
        self.scale = tk.Scale(self.window, from_=0, to=10, orient=tk.HORIZONTAL, resolution=0.05, command=self.brightness)
        self.scale.pack(fill=tk.X)
        self.scale.set(1)

        self.video()


    def video(self):
        self.imageCV = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)
        self.imagePIL = Image.fromarray(self.imageCV)
        self.brightener = ImageEnhance.Brightness(self.imagePIL)
        self.imagePIL = self.brightener.enhance(self.brightness_val)
        self.imageTk = ImageTk.PhotoImage(self.imagePIL)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imageTk)
        self.window.after(self.update_time, self.video)


    def exit(self):
        self.window.destroy()
        self.cap.release()

    def snapshot(self):
        self.imagePIL.save(self.entry.get()+'.png', "PNG")

    def brightness(self,_):
        self.brightness_val = self.scale.get()
        #return self.brightness_val
        #print(self.brightness_val)



def main():
    root = tk.Tk()
    app = App(root, cv2.VideoCapture(0))
    root.mainloop()


if __name__ == "__main__":
    main()
