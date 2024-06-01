【WhitelistCompare】  
    白名单对比小工具，提高安全运营效率。使用python3编写的白名单比对小工具，避免误封IP。

【使用方式】
   使用前确保相关的python模块已安装！
   同一目录下需要有一个白名单txt文件，一行一个地址，支持IP，网段，IPV6格式。运行可以使用python或者直接双击打包好的exe。  
  
【版本发布1.0】  
   目前1.0版本还无法使用快捷键功能，后续不断测试进行优化。  

【功能展示】 
    目前仅提供判断给定IP是否在白名单的功能。  
![image](https://github.com/Bluecap666/WhitelistCompare/assets/83532219/d17062c3-3f98-4ee4-9ff3-891ffc80d835)


【版本发布1.1】  
   新版本优化了输入空格没有去除的问题，同时增加了更好的颜色提示和地址异常处理，以及标题、尾注。后续将补充资产信息查询。  
 编辑好代码后执行打包命令：pyinstaller --onefile --windowed .\whitelistGUI.py  
 更新展示：  
 
 ![image](https://github.com/Bluecap666/WhitelistCompare/assets/83532219/0f93a6de-be4a-4069-b067-5bd97768b4d8)  
 
![image](https://github.com/Bluecap666/WhitelistCompare/assets/83532219/7514bd3f-78ff-48b7-b3a2-123c66ae0606)  

![image](https://github.com/Bluecap666/WhitelistCompare/assets/83532219/0e0e661f-6042-4f1d-bcb6-59dd87644964)  

【版本发布2.0】

 新增批量查询，支持列表或者逗号分隔格式
 
 127.0.0.1
 
 127.0.0.2
 
 127.0.0.3
 
 ...
 或者 127.0.0.1，127.0.0.2，127.0.0.3
 
 ![image](https://github.com/Bluecap666/WhitelistCompare/assets/83532219/e09d7ce2-4fc5-4442-92f5-65b476101115)

