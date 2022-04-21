# -*- encoding: utf-8 -*-
"""
@File    :   test.py   
@Contact :   936956317@qq.com
  
@Modify Time      @Author      @Version   
------------      -------      --------    
2022/4/18 16:34   potatomine     1.0  
@Description : 
"""
import tkinter
import tkinter.messagebox


def but():

    print(a)


root = tkinter.Tk()
root.title('GUI')  # 标题
root.geometry('0x0')  # 窗体大小
a = tkinter.messagebox.askokcancel('提示', '要执行此操作吗')
print(a)
root.mainloop()
