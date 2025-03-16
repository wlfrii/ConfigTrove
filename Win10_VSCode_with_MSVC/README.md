#! https://zhuanlan.zhihu.com/p/424985289
# 【Win10 - VS Code】 配置 MSVC 编译器 for LeetCode

## VS Code 配置 MSVC 编译器

整理电脑发现之前整理过的配置方法...分享出来希望能帮到需要的人。
记得19年用VS Code配置 MSVC 真是头都大了，硬怼了好几天之后终于成了~

---

Visual Studio Code是一款轻量级编辑器，但也是一款具有强大的拓展功能的编辑器。通常很少有人在安装的 Visual Studio 的情况下去使用 VSCode, 除非像我一样为了方便使用 VSCode 刷 LeetCode。
废话不多说，进入正文。

## Reference
[Configure VS Code for Microsoft C++](https://code.visualstudio.com/docs/cpp/config-msvc)

[Developer Command Prompt for Visual Studio](https://docs.microsoft.com/en-us/dotnet/framework/tools/developer-command-prompt-for-vs#visualstudio)

---

## 1. 准备工作

Win10系统。
如果已经下载并安装了 Visual Studio 和 Visual Studio Code，则跳过该步骤。**VS版本建议17或以上**。

[Visual Studio 下载](https://visualstudio.microsoft.com/zh-hans/downloads/)  并安装

[Visual Studio Code 下载](https://code.visualstudio.com/)

## 2. 找到 Developer Command Prompt

### 2.1 搜索 Developer Command Prompt

在win10 (或win8.1,win8,win7) 开始菜单栏搜索或查找 `Developer Command Prompt` 如图
![](./image/developer-cmd-prompt-menu.png) 
打开后会发现相当于Cmd窗口。若安装的Visual Studio软件不包含 Developer Command Prompt，按照如下方法建立自己的 Developer Command Prompt。

### 2.2 手动查找电脑上的文件

通常，已安装的命令提示符`VsDevCmd.bat`位置在，例如 `C:\Program Files(x86)\Microsoft Visual Studio\2017\Community\Common7\Tools`（路径更改取决于 Visual Studio 版本和安装位置）。

### 2.3 在 Visual Studio 中建立

在 Visual Studio 菜单栏选择 **工具** -> **外部工具** 打开，如图所示
![](./image/external_tool.jpg)
   1. 在标题行中输入一个自己的标题，如 `mycmd`；
   2. 在命令行中输入`C:\Windows\System32\cmd.exe`;
   3. 在参数行中输入命令提示符的路径`/k "C:\Program Files(x86)\Microsoft Visual Studio\2017\Community\Common7\Tools\VsDevCmd.bat"`，如果找到的VsDevCmd.bat文件不在这个文件夹中，则输入其所在文件夹路径。这个命令是用于启动安装在Vsiual Studio 2017内部的 Developer Command Prompt 的；
   4. 选择一个初始目录，如 `项目目录`;
   5. 点击'确定'，会发现在 **工具** 中新加了一个 `mycmd` 项目。
![](./image/external_tool1.jpg)

## 3.使用 Developer Command Prompt 启动 VS Code

打开刚刚新建的`mycmd`，输入以下指令来生成目录。
```Shell
$ mkdir E:/VSCodeProjects
```
![](./image/4bc2b4c87eecdd5621f030557150a52.png)

然后继续在mycmd窗口中输入
```Shell
$ code E:/VSCodeProjects
```
![](./image/4c15a80dd8e573264ca5a3426ad8f0a.png)
会启动 VS Code 程序，且默认工作目录为 `E:\VSCodeProjects`
![](./image/15d8052a02c744a3be3d8de8bdb9540.png)

## 4. 配置编译及启动文件

- `c_cpp_properties.json` (compiler path and IntelliSense settings)
- `tasks.json` (build instructions)
- `launch.json` (debugger settings)

### 4.1 配置`c_cpp_properties.json`
首先新建一个main.cpp（稍后测试使用），文件会自动保存在工作目录上
![](./image/d7a6bcca06dd80a390ec46b6b590ca6.png)

在 VS Code 拓展工具中搜索`C/C++`，安装如下
![](./image/1040b5e3479b3131f1aaf1b2a838e82.png)

之后按`ctrl+shift+p`，在搜索栏搜`C/C++`，选择`C/C++: Edit Configuration(UI)`
![](./image/a410dd1a76d72e86454378b01f6670e.png)

打开后主要编辑 **编译器路径**，**C,C++版本号**

![](./image/23846f45cd2d9e88ad13c47e10ceb9e.png)
![](./image/46a2aab2874b7006f6437f40a28e3ab.png)

若出现下图所示无法检测到编译器的情况，可手动解决，打开`.vscode`文件夹中的`c_cpp_properties.json`文件，手动添加安装路径下的`"...Microsoft Visual Studio\\2017\\Community\\VC\\Tools\\MSVC\\14.16.27023\\bin\\Hostx64\\x64\\cl.exe"`路径
![](./image/ae19f873da2b451f95056d963c2a461.png)
最后的`c_cpp_properties.json`文件如下
```json
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}/**"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "intelliSenseMode": "msvc-x64",
            "compilerPath": "\"C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\VC\\Tools\\MSVC\\14.16.27023\bin\\Hostx64\\x64\\cl.exe\"",
            "cppStandard": "c++17",
            "cStandard": "c11",
            "windowsSdkVersion": "10.0.17763.0"
        }
    ],
    "version": 4
}
```

### 4.2 配置`tasks.json`
[官网](https://code.visualstudio.com/docs/cpp/config-msvc)上给的教程是
![task_tutorial](./image/1573710636(1).jpg)
但有可能行不通，此时可以在`.vscode`目录下，手动创建`tasks.json`文件，然后输入以下代码
```json
{
    "tasks": [
        {
            "type": "shell",
            "label": "cl.exe build active file",
            "command": "cl.exe",
            "args": [
                "/Zi",
                "/EHsc",
                "/Fe:",
                "${fileDirname}\\${fileBasenameNoExtension}.exe",
                "${file}"
            ]
        }
    ],
    "version": "2.0.0"
}
```

### 4.3 配置`launch.json`
工具栏 **Debug** -> **Add Configuration**，如无法创建可手动创建，做法同上，代码如下。
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "cl.exe build and debug active file",
            "type": "cppvsdbg",
            "request": "launch",
            "program": "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "preLaunchTask": "cl.exe build active file"
        }
    ]
}
```

## 5. 测试
在前面建好的`main.cpp`文件中输入
```C
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v = {1,2,3,4,5,6};
    for(const auto & i:v)
        std::cout << v[i] << std::endl;

    return 0;
}
```
进入`dubug`模式运行，结果如下：
![result](./image/0f009edb3a32ccf471ff9b962d77ce7.png)

**之后使用时，直接在建好的 VSCodePriject 目录中建立自己的项目即可**