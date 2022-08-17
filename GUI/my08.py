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
        self.codeHobby = IntVar();
        self.videoHobby = IntVar()

        print(self.codeHobby.get()) # 默认值是0
        self.c1 = Checkbutton(self, text="敲代码",
                              variable=self.codeHobby, onvalue=1, offvalue=0)
        self.c2 = Checkbutton(self, text="看视频",
                              variable=self.videoHobby, onvalue=1, offvalue=0)

        self.c1.pack(side="left");self.c2.pack(side="left")

        Button(self, text="确定", command=self.confirm).pack(side="left")

    def confirm(self):
        if self.videoHobby.get()==1:
            messagebox.showinfo("测试", "正常人")
        if self.codeHobby.get() == 1:
            messagebox.showinfo("测试", "野生钢铁侠")


if __name__ == '__main__':  # 相对规范，将文件作为独立运行调用方法
    root = Tk()
    root.geometry("400x130+200+100")
    app = Application(master=root)
    root.mainloop()