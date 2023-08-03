import tkinter as tk
import ipaddress
import traceback

def check_ip(event=None):
    try:
        ip = entry.get()
        with open('whitelists.txt', 'r') as file:
            whitelist = file.read().splitlines()
            if check_ip_in_whitelist(ip, whitelist):
                result_label.config(text=ip+" 在白名单中！")
            else:
                result_label.config(text=ip+" 不在白名单中！")
        entry.delete(0, tk.END)  # 查询完后清空文本框内容
    except Exception as e:
        traceback.print_exc()
        result_label.config(text="无法打开白名单文件！")
        result_label.config(text="发生异常：{}".format(str(e)))

def check_ip_in_whitelist(ip, whitelist):
    ip_obj = ipaddress.ip_address(ip)
    for item in whitelist:
        if '/' in item:  # IP地址段
            if ipaddress.ip_address(ip) in ipaddress.ip_network(item):
                return True
        elif ':' in item:  # IPv6地址或地址段
            if ipaddress.ip_address(ip) in ipaddress.ip_network(item, False):
                return True
        else:  # 单个IP地址
            if ipaddress.ip_address(ip) == ipaddress.ip_address(item):
                return True
    return False

def clear_result(event=None):
    result_label.config(text="")

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()
entry.bind("<Return>", check_ip)  # 绑定回车键触发check_ip函数

result_label = tk.Label(root, text="")
result_label.pack()

# 设置快捷键
root.bind('<Control-KeyPress-greater>', check_ip)  # 绑定Ctrl+>键触发check_ip函数
root.bind('<BackSpace>', clear_result)  # 绑定Backspace键触发clear_result函数

root.mainloop()
