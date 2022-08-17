"""测试一个经典的GUI程序的写法，使用面向对象的方式"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):   # Frame为虚拟区域
    """一个经典的GUI程序的类的写法"""

    def __init__(self, master=None):
        super().__init__(master)   # super代表的是父类的定义，而不是父类的方法
        self.master = master   # 使root和app挂钩
        self.pack()

        self.createWidget()   # 调用下一步

    def createWidget(self):
        """创建组件"""
        self.btn01 = Button(self)   # self为组件容器
        self.btn01["text"] = "点击送花"
        self.btn01.pack()
        self.btn01["command"] = self.songhua

        # 创建一个退出按钮
        self.btnQuit = Button(self, text="退出", command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("送花", "送你99朵玫瑰花")

if __name__ == '__main__':  # 相对规范，将文件作为独立运行调用方法
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个经典的GUI程序类的测试")
    app = Application(master=root)
    root.mainloop()
