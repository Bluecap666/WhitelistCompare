import tkinter as tk
import ipaddress
import traceback

ips_num=0

def start():
    ipstr = entry.get().strip().replace("\n",",")
    global ips_num#指定变量是全局的变量
    if ips_num>0:
        clearGrid(ips_num)
    if ipstr!="":
        dot_num=ipstr.count(".")
        if dot_num>3:
            #ret_label = tk.Label(root, text="")
            #result_label.config(text="")
            ips_num=check_ips(ipstr)# 绑定回车键触发check_ip函数
            entry.delete(0, tk.END)# 查询完后清空文本框内容
        elif dot_num==3:
            #ret_label = tk.Label(root, text="")
            result_label.config(text="")
            check_single_ip(ipstr)
            entry.delete(0, tk.END)
        elif ":" in ipstr:
            #ret_label = tk.Label(root, text="")
            result_label.config(text="")
            check_single_ip(ipstr)
            entry.delete(0, tk.END)
        else:
            ret_label = tk.Label(root, text="")
            result_label.config(text="")
            result_label.config(text="输入内容有误！",foreground="red")
            entry.delete(0, tk.END)
def check_ips(ip):
    try:
        #多个IP的情况处理,默认逗号分割
        ip_lists=ip.split(',')
        with open('whitelists.txt','r') as file:
                # result_label.config(text="读取白名单成功！",foreground="blue")
                whitelist = file.read().splitlines()
                ret=[]
                for ip_one in ip_lists:
                    check_ret=check_ip_in_whitelist(ip_one, whitelist)
                    ret.append(check_ret)
                print(ret)
                #print("check_ret:"+str(check_ret))
                for i in range(len(ret)):
                    ret_label = tk.Label(root, text="")
                    ret_label.grid(row=i+3,column=0)
                    if ret[i]==True:
                        ret_label.config(text=ip_lists[i]+" 在白名单中！",foreground="green")
                    elif ret[i]==False:
                        ret_label.config(text=ip_lists[i]+" 不在白名单中！",foreground="red")
                    else:
                        ret_label.config(text=ip_lists[i]+" 比对失败！",foreground="blue")
                
                return i+1
                        
    except Exception as e:
        traceback.print_exc()
        result_label.config(text="无法打开白名单文件！",foreground="orange")
        result_label.config(text="发生异常：{}".format(str(e)),foreground="orange")



def check_single_ip(ip):
    try:
        print(ip)
        with open('whitelists.txt','r') as file:
            result_label.config(text="读取白名单成功！",foreground="blue")
            whitelist = file.read().splitlines()
            check_ret=check_ip_in_whitelist(ip, whitelist)
            print("check_ret:"+str(check_ret))
            result_label.grid(row=3,column=0)
            if check_ret==True:
                result_label.config(text=ip+" 在白名单中！",foreground="green")
            elif check_ret==False:
                result_label.config(text=ip+" 不在白名单中！",foreground="red")
            # else:
            #     result_label.config(text=ip+" 比对失败！",foreground="yellow")
    except Exception as e:
        traceback.print_exc()
        result_label.config(text="无法打开白名单文件！",foreground="orange")
        result_label.config(text="发生异常：{}".format(str(e)),foreground="orange")

def check_ip_in_whitelist(ip, whitelist):
    flag=False
    try:
        ip_obj = ipaddress.ip_address(ip)
        for item in whitelist:
            if '/' in item:  # IP地址段
                if ipaddress.ip_address(ip) in ipaddress.ip_network(item):
                    flag=True
            elif ':' in item:  # IPv6地址或地址段
                if ipaddress.ip_address(ip) in ipaddress.ip_network(item, False):
                    flag=True
            else:  # 单个IP地址
                if ipaddress.ip_address(ip) == ipaddress.ip_address(item):
                    flag=True

        return flag
    except Exception as e:
        print(e)
        result_label.config(text=ip+" 比对失败！",foreground="blue")

# def clear_result(event=None):
#     result_label.config(text="")

def clearGrid(num):
    if num:
        for i in range(num):
            w=root.grid_slaves(row=i+3,column=0)[0]
            w.grid_forget()


root = tk.Tk()
root.title("资产信息对比工具whitelistGUI2.0")

footer_label = tk.Label(root, text="Made by Bluecap @202308")
# footer_label.pack(side=tk.BOTTOM)
footer_label.grid(row=0,column=0)

title_label=tk.Label(root,text="输入IP(一个或多个，逗号分隔)：")
# title_label.pack(side=tk.TOP)
title_label.grid(row=1,column=0)

entry = tk.Entry(root)
# entry.pack()
entry.grid(row=2,column=0,sticky="nsew")

result_label = tk.Label(root, text="")
# result_label.pack()
# result_label.grid(row=3,column=0)
# result_label.place(x=100,y=50)
entry.bind("<Return>",  lambda event: start())  # 绑定回车键触发check_ip函数
root.mainloop()









# 设置快捷键
# root.bind('<Control-KeyPress-greater>', check_ip)  # 绑定Ctrl+>键触发check_ip函数
# root.bind('<BackSpace>', clear_result)  # 绑定Backspace键触发clear_result函数

