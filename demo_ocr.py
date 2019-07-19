#_*_coding:UTF-8_*_
#创建于2019/4/17:13:26

import tkinter
from tkinter import filedialog  #导入的文件插件
from datetime import datetime
import threading

from demo_weixin import handle_path

#实例化一个窗口widget
win=tkinter.Tk()

#设置标题
win.title("图片转文本工具")
# win.geometry("400x200")

#实例化Label
label_info=tkinter.Label(win,text='暂时还没有选择文件')
display_info=tkinter.Listbox(win,width=80)

def translate_dir(dir,label_info,display_info):
    label_info.config(text=f'正在转换{dir},请耐心等待...')
    display_info.insert(0, f'{datetime.now().strftime("%H:%M:%S")} {dir} 对应的文件开始转换')
    try:
        handle_path(dir)
    except Exception as err:
        display_info.insert(0, f'{datetime.now().strftime("%H:%M:%S")} {dir} 转换出错:{str(err)}')
    else:
        label_info.config(text='转换完成')
        display_info.insert(0, f'{datetime.now().strftime("%H:%M:%S")} {dir} 已转换完成')

def translate():
    dir=filedialog.askdirectory()
    if dir:
        thread = threading.Thread(target=translate_dir, args=(dir,label_info,display_info))
        thread.start()
    else:
        label_info.config(text='还没有选择文件夹')

#选择文件夹按钮,command是button事件触发按钮函数
translate_btn=tkinter.Button(win,text='选择文件夹',command=translate)


# 装载
label_info.pack()
translate_btn.pack()
display_info.pack()

# 事件(消息)循环机制，可以理解成运行起来随时去监听按钮点击等事件
tkinter.mainloop()

#打包处理 :安装pyinstaller
# pyinstaller --onefile demo_ocr.py -w