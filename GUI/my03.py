"""测试Label组件的基本用法，使用面向对象的方法"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):   # Frame为虚拟区域

    def __init__(self, master=None):
        super().__init__(master)   # super代表的是父类的定义，而不是父类的方法
        self.master = master   # 使root和app挂钩
        self.pack()
        self.createWidget()   # 调用下一步

    def createWidget(self):
        """创建组件"""
        self.label01 = Label(self, text="詹永乐", width=10, height=2,
                             bg="black", fg="white")
        self.label01.pack()

        self.label02 = Label(self, text="gobang", width=10, height=2,
                             bg="white", fg="blue", font=("黑体", 30))
        self.label02.pack()

        # 显示图像
        global photo   # 将photo声明成全局变量
        photo = PhotoImage(file="imgs/R-C.gif")   # photo为局部变量时无法显示,本方法执行后，图像对象销毁
        self.label03 = Label(self, image=photo)
        self.label03.pack()   #没显示可能是root.geometry("400x100+200+300")中height太小

        # 显示多行文本
        self.label04 = Label(self, text="五子棋\n詹永乐的第一个\nGitHub项目",
                             borderwidth=5, relief="solid", justify="left")   # borderwidth为边框粗细 relief为效果（groove）
        self.label04.pack()

if __name__ == '__main__':  # 相对规范，将文件作为独立运行调用方法
    root = Tk()
    root.geometry("400x700+200+100")
    app = Application(master=root)
    root.mainloop()
