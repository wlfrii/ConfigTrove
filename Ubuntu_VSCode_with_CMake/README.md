#! https://zhuanlan.zhihu.com/p/424998434
# 【Ubuntu - VS Code】with CMake for C++ project

同样是19年整理过的配置方法... 分享出来希望能帮到需要的人。

---

配置过程比较简单，按照以下步骤来就行。

__1__. 安装 **VS Code** 和 **CMake**
+ [Visual Studio Code 下载](https://code.visualstudio.com/) 
+ [CMake 下载](https://cmake.org/download/)

__2__. 添加 `C/C++` 拓展包
+ 在 **VS Code** 中打开 `Extensions`
+ 搜索 `C/C++` 然后 install
+ 搜索 `CMake` 然后 install
+ *(optional)* 搜索 `CMake Tools` 然后 install

__3__. 创建一个测试文件夹，例如 `Hello`，并在 **VS Code** 中打开。
+ 创建主函数 `main.cpp` 
```C++
#include <iostream>

int main()
{
    std::cout << "hello \n";
    return 0;
}
```
+ 创建 `CMakeLists.txt`

```CMake
cmake_minimum_required (VERSION 3.0)
project(Hello)
file(GLOB SRC_FILE *.cpp)
add_executable (${PROJECT_NAME} ${SRC_FILE})
```

__4__. 在 `main.cpp` 窗口中按 `F5`，启动 Debug (第一次启动时会创建 `launch.json`)
+ 选择 `C++ (GDB/LLDB)`
![](img/01.png)
+ 选择 `g++ build and debug active file`
![](img/02.png)
+ 编辑 `launch.json`，如下
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch Debug",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/build/Hello",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            "miDebuggerPath": "/usr/bin/gdb",

            "preLaunchTask": "build debug",
        }
    ]
}
```
`"program"` is the location of the program. \
`"preLaunchTask"` is the pre task before launch, which will be defined below.

__5__. 按下 `ctrl+shift+B` 运行 task (第一次运行时会创建 `task.json`)
+ 选择 `C/C++: g++ build active file`
    ![](img/03.png)
+ 编辑 `tasks.json`
```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "build debug",
            "type": "shell",
            "command": "mkdir -p build && cd build && cmake -DCMAKE_BUILD_TYPE=Debug ../ && make",
            "args": [],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "always"
            },
            "problemMatcher": "$msCompile"
        }
    ]
}
```

__6__. 随后项目目录如下，在 `main.cpp` 函数中设置 **断点**， 然后按 `F5` 开始调试

![](img/05.png)


## Reference

[用VSCode和CMake编写调试C/C++](https://www.jianshu.com/p/c3806d2ad1f8)

[【Win10 - VS Code】 配置 MSVC 编译器 for LeetCode](https://zhuanlan.zhihu.com/p/424985289)

