# C++ Dev Environment on Debian/Ubuntu

记录一些 C++ 开发中，常用基础配置，方便后期脚本化。
持续更新...

__Content__

- [1. 更新系统](#1)
- [2. 安装核心 C++ 编译工具](#2)
    - [2.1 安装编译器（gcc/g++）](#2.1)
    - [2.2 安装CMake](#2.2)
- [3. 安装常用依赖库和工具](#3)
    - [3.1 安装常用依赖库（开发常用）](#3.1)
    - [3.2 安装 gdb 调试器](#3.2)
    - [3.3 安装 Qt6](#3.3)

---
<!-- ======================================================================= -->

<h2 id=1> 1. 更新系统 </h2>

更新软件源列表，确保安装的是最新版本。
```bash
sudo apt update
sudo apt upgrade -y
```

---
<!-- ======================================================================= -->

<h2 id=2> 2. 安装核心 C++ 编译工具 </h2>

<h3 id=2.1> 2.1 安装编译器（gcc/g++） </h2>

C++ 开发最核心工具：
- gcc：C 语言编译器
- g++：C++ 语言编译器

```shell
# 安装 g++, gcc
sudo apt install gcc g++ -y

# 或安装一键打包的开发工具合集
sudo apt install build-essential -y
```
`build-essential` 中包含了：gcc/g++、make、libc-dev、库文件等，装了它，系统就具备完整 C/C++ 编译环境

安装完成后查看状态
```shell
gcc -v
g++ -v
```

<h3 id=2.2> 2.2 安装CMake </h3>

目前 C++ 最主流的项目构建工具.

```shell
sudo apt install cmake -y
```
安装完成后查看状态
```shell
$ cmake --version
```

---
<!-- ======================================================================= -->

<h2 id=3> 3. 安装常用依赖库和工具 </h2>

<h3 id=3.1> 3.1 安装常用依赖库（开发常用）</h3>

```bash
# 标准 C++ 开发库，提供 STL（vector、string、map 等）的头文件和链接库
sudo apt install libstdc++-12-dev -y

# 线性代数库（机器人学，图像算法、SLAM、视觉重建、优化算法）
sudo apt install libeigen3-dev

# 图像格式支持库（jpg/png/tiff/webp）
sudo apt install libjpeg-dev libpng-dev libtiff-dev libwebp-dev

# 相机/视频（相机采集、视频解码）
# libv4l-dev：Linux 相机驱动（USB 摄像头必备）
# ffmpeg 系列：视频解码、MP4/AVI 读取（OpenCV 视频依赖）
sudo apt install libv4l-dev libavcodec-dev libavformat-dev libavutil-dev libswscale-dev

# 点云/3D重建(PCL)
sudo apt install libpcl-dev

```

<h3 id=3.2> 3.2 安装 gdb 调试器</h3>

`gdb`调试器是C++ 官方调试工具，可用来找程序崩溃、查 bug、单步执行代码。
```bash
sudo apt install gdb -y
```

<h3 id=3.3> 3.3 安装 Qt6 </h3>

Qt的常用模块：
+ `qt6-base-dev`：Qt6 基础开发包，包含QtCore（核心数据结构、线程、IO）、QtGui（2D 绘图、图像、字体）、QtWidgets（桌面 UI 控件：按钮、窗口、列表、画布），是写 C++ 桌面程序的基础。
如果只做简单界面加手写Qt界面，只需要安装该模块。

+ `qt6-tools-dev`：提供uic（UI 文件转 C++）、moc（元对象编译器，Qt 信号槽必需）、rcc（资源编译）、Qt Designer（可视化拖放 UI），开发必备工具链。

+ `qt6-multimedia-dev`：处理摄像头采集、视频播放 / 编码、音频，和 OpenCV 的 VideoCapture/VideoWriter 配合，实现相机实时预览、视频流 GUI 显示。

+ `qt6-opengl-widgets-dev`：QOpenGLWidget组件，用于高性能渲染 OpenCV 的 Mat 图像、3D 点云、视觉算法结果，比普通 QLabel 显示图像快很多，适合高帧率视觉场景。

+ `qt6-imageformats-dev`：扩展 Qt 支持的图像格式（WebP、TIFF、JPEG2000 等），避免 OpenCV 读的图 Qt 无法显示。
Qt基础模块支持 JPG/PNG。

+ `qtcreator`：Qt 专属 IDE，自带 CMake/qmake、代码补全、调试、UI 设计，比纯命令行高效。

```bash
# 按照需求，安装常用 qt 模块xxxx
sudo apt install -y xxxx
```