"""测试Entry组件的基本用法，使用面向对象的方法"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):   # Frame为虚拟区域

    def __init__(self, master=None):
        super().__init__(master)   # super代表的是父类的定义，而不是父类的方法
        self.master = master   # 使root和app挂钩
        self.pack()
        self.createWidget()   # 调用下一步

    def createWidget(self):
        """创建登录界面的组件"""
        self.label01 = Label(self, text="用户名")
        self.label01.pack()

        # StringVar变量绑定到指定的组件
        # 变量的值发生变化，组件内容也变化
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set("admin")  # 设置固定值输出
        print(v1.get());print(self.entry01.get())



        # 创建密码框
        self.label02 = Label(self, text="密码")
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*") # 将密码隐藏
        self.entry02.pack()

        self.btn01 = Button(self, text="登录", command=self.login)
        self.btn01.pack()
    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()


        print("用户名:"+username)
        print("密码:" + pwd)

        if username=="admin" and pwd=="123456":
            messagebox.showinfo(("gobang", "登录成功!"))
        else:
            messagebox.showinfo(("gobang", "登陆失败！重新输入"))

if __name__ == '__main__':  # 相对规范，将文件作为独立运行调用方法
    root = Tk()
    root.geometry("400x130+200+100")
    app = Application(master=root)
    root.mainloop()