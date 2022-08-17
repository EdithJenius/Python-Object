"""Checkbutton复选按钮 Radiobutton单选按钮"""
from tkinter import *
from tkinter import messagebox


class Application(Frame):   # Frame为虚拟区域

    def __init__(self, master=None):
        super().__init__(master)   # super代表的是父类的定义，而不是父类的方法
        self.master = master   # 使root和app挂钩
        self.pack()
        self.createWidget()   # 调用下一步

    def createWidget(self):
        self.v = StringVar();
        self.v.set("F")

        self.r1 = Radiobutton(self, text="男性", value="M",variable=self.v)
        self.r2 = Radiobutton(self, text="女性", value="F", variable=self.v)

        self.r1.pack(side="left");self.r2.pack(side="left")

        Button(self, text="确定", command=self.confirm).pack(side="left")

    def confirm(self):
        messagebox.showinfo("测试", "选择的性别："+self.v.get())

if __name__ == '__main__':  # 相对规范，将文件作为独立运行调用方法
    root = Tk()
    root.geometry("400x130+200+100")
    app = Application(master=root)
    root.mainloop()