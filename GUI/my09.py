"""测试canvas组件的基本用法"""
from tkinter import *
from tkinter import messagebox
import random


class Application(Frame):   # Frame为虚拟区域

    def __init__(self, master=None):
        super().__init__(master)   # super代表的是父类的定义，而不是父类的方法
        self.master = master   # 使root和app挂钩
        self.pack()
        self.createWidget()   # 调用下一步

    def createWidget(self):
        self.canvas = Canvas(self, width=300, height=200, bg="green")
        self.canvas.pack()
        # 画一条直线
        line = self.canvas.create_line(10, 10, 30, 20, 40, 50)
        # 画一个矩形
        rect = self.canvas.create_rectangle(50, 50, 100, 100)
        # 画一个椭圆，坐标两双。为椭圆的边界矩形左上角和底部右下角
        oval = self.canvas.create_oval(50, 50, 100, 100)

        global photo
        photo = PhotoImage(file="imgs/R-C.gif")
        self.canvas.create_image(150, 170, image=photo)

        Button(self, text="画10个矩形", command=self.draw50Recg).pack(side="left")

    def draw50Recg(self):
        for i in range(1, 10):
            x1 = random.randrange(int(self.canvas["width"])/2)
            y1 = random.randrange(int(self.canvas["height"]) / 2)
            x2 = x1+random.randrange(int(self.canvas["width"]) / 2)
            y2 = y1+random.randrange(int(self.canvas["height"]) / 2)
            self.canvas.create_rectangle((x1, y1, x2, y2))


if __name__ == '__main__':  # 相对规范，将文件作为独立运行调用方法
    root = Tk()
    root.geometry("400x300+200+300")
    app = Application(master=root)
    root.mainloop()