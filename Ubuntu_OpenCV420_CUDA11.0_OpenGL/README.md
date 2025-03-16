#! https://zhuanlan.zhihu.com/p/425143325
# 【Ubuntu - OpenCV-CUDA】 with CUDA 11.0 and OpenGL 详细流程

在 Windows 上折腾了多次之后，非常顺利的在 Ubuntu 上完成配置。
参照：[【Win10 - OpenCV-CUDA】with VS2017 and CUDA 10.0 (cuDNN)](https://zhuanlan.zhihu.com/p/425133410)

2020.9.21 补充：1. 由于我下载的 CUDA toolkit 的 runtime 版本大于 CUDA driver 版本，导致运行出错。2. 由于 CUDA driver 问题导致 Ubuntu 无法检测到多个显示器。问题已解决，见补充内容。

---

<h2 id="1">1.准备</h2>
<h3 id="1.1"> 1.1 下载 OpenCV</h3> 

[源码下载](https://opencv.org/releases/)，找到相应的版本，然后下载
[opencv_contrib](https://github.com/opencv/opencv_contrib)进入页面后，看右边的 **Releases** -> __32 tags__，然后点击tags，找到对应的 opencv-contrib 然后进行下载

<h3 id="1.2"> 1.2 安装 CMake 和 CMake-GUI </h3> 

```
$ sudo apt install -y cmake
$ sudo apt install -y cmake-qt-gui
```
使用时，直接在终端输入 `cmake-gui`。个人觉得通过 gui 编译 OpenCV+ contrib (CUDA, cvDNN) 时候更加一目了然。\
注意，通过 apt 安装的 cmake 版本要低一些，如果需要高版本的 cmake，可 [CMake官方下载](https://cmake.org/download/)，然后手动安装。

<h3 id="1.3"> 1.3 安装 CUDA</h3> 

下载地址[https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu)
![](./img/cuda_download.png)

注意，按照图中指令 `sudo sh cuda.......`执行之后，需要等待一段时间（并不是电脑卡了...），之后在弹出的选择中敲 `accept`，之后选择安装选项，可以取消掉 `samples` 和 `documents` 选项。\
如果安装不成功，则重新执行 `sudo sh cuda.......`，然后把第一个`driver` 选项也取消掉，因为 ubuntu 本身已经装了驱动了。


## 2. Configure

打开`cmake-gui`，设定 OpenCV 源码路径和 build 路径，如下

![](./img/cmake_gui.png)

然后先点击 "__Configure__"，出现如下界面

![](./img/cmake_setup.png)

使用默认选择，直接点击 "__Finish__"

然后输出窗口中可能会出现如下的 ippicv 的安装失败错误（通常网络不好就会无法下载 ippicv 加速库）。

![](./img/ippicv_error.png)

可通过手动配置，ippicv的下载地址[[https://github.com/opencv/opencv_3rdparty/tree/ippicv/master_20180723/ippicv](https://github.com/opencv/opencv_3rdparty/tree/ippicv/master_20180723/ippicv)]

关于下载对应的 opencv 的 ippicv 的方法是打开文件夹 `opencv.x.x.x/3rdparty/ippicv/` 下的ippicv.cmake文件，查看各个系统下对应的ippicv版本号，然后进行下载即可。
具体安装可参照 [[手动安装OpenCV下的IPP加速库]](https://www.cnblogs.com/yongy1030/p/10293178.html)，或如下：
>将下载好的ippicv文件（例如`ippicv_2019_lnx_intel64_general_20180723.tgz`）放在`opencv.x.x.x/3rdparty/ippicv/` 路径下。

之后再次 "__Configure__"，可发现 ippicv 的问题已解决。

### 2.1 增加 CUDA

● 搜索框中搜 `OPENCV_EXTRA_MODULES_PATH`，并在之后的value中输入下载好的 `opencv_contrib-x.x.x/modules` 的路径。

● 搜索 cuda，选中如下选项，

![](./img/with_cuda.png)

● 再搜索勾选上 `BUILD_opencv_world`，勾选上这个选项，编译出的带有 CUDA 的 OpenCV 库就会存在一个 `opencv_world.hpp` 文件，这个文件包含了 OpenCV 所有的头文件。

● 点击 "__Configure__" 后可能会出现如下的错误

![](./img/error.png)

因为 cuda 11 移除了 nppicom 库， 解决方法是，在 `opencv-x.x.x/cmake/` 文件夹下，找到 `OpenCVDetectCUDA.cmake` 文件，找到下述 `if(CUDA_FOUND)` 的位置，在下面加上去掉 nppicom 的库的指令（行后有 add 的）。
```CMake
...
if(CUDA_FOUND)
  set(HAVE_CUDA 1)
  if(CUDA_VERSION VERSION_GREATER_EQUAL "11.0")     # add
    ocv_list_filterout(CUDA_nppi_LIBRARY "nppicom") # add
    ocv_list_filterout(CUDA_npp_LIBRARY "nppicom")  # add
  endif()                                           # add

  if(WITH_CUFFT)
    set(HAVE_CUFFT 1)
...
```
如果还不能解决，可参照 [[Fix cuda11 #17499]](https://github.com/opencv/opencv/pull/17499/files)。

然后再次 "__Configure__" 应该是没有错误了，不要着急点击 "__Generate__"，先看看还需要增加什么，如果不需要增加，直接略过下一部分。

### 2.2 安装其他可编译项

●  __安装Eigen__

```Shell
$ sudo apt install libeigen3-dev
```

●  __安装 gtk__

(如果需要同时编译opengl，需要安装gtk2.0)
```Shell
$ sudo apt install libgtk2.0-dev
```
安装完之后输入
```Shell
$ pkg-config --modversion gtk+-2.0
```
检验。详细安装步骤可参照 [[Ubuntu16安装GTK+2.0教程]](https://www.cnblogs.com/cbattle/p/9782783.html).

之后再次 "__Configure__" 可看到 `cmake-gui` 输出窗口中，GUI: GTK -> Yes

● __安装gtkglext__

gtkGlExt 这一项必须能够通过 CMake 检测到，否则即使安装了OpenGL，CMake 也无法检测得到。
执行
```Shell
$ sudo apt install -y libgtkglext1 libgtkglext1-dev
```

● __安装opengl__

执行
```Shell
$ sudo apt-get install build-essential libgl1-mesa-dev
$ sudo apt-get install freeglut3-dev
$ sudo apt-get install libglew-dev libsdl2-dev libsdl2-image-dev libglm-dev libfreetype6-dev
```
然后 `cmake-gui` 中勾选上 `WITH_OPENGL`，继续 "__Configure__"，可看到输出窗口中出现如下结果
![](./img/cmake_gtk.png)

## 3. make

点击 "__Generate__"，生成成功后，cd 到 cmake 的 build 的目录（就是 `cmake-gui` 上指定的 build 目录），执行
```Shell
$ make -j11
```
-j表示指定的线程数，根据自己计算机的线程数来设定。(建议线程数不大于最大线程数，否则容易卡死 (栽过一次了)......本人计算机支持最大线程数为12，所以-j11）

（此处等待大约1-2小时...）
![](./img/1000_years_later.png)


make 完之后执行
```Shell
$ sudo make install
```

大功告成~

![](./img/smile_cat.png)

---

## 补充

### 1. CUDA driver version is insufficient for CUDA runtime version

这个问题主要是由于cuda版本与cuda驱动版本不匹配导致的。
cuda与驱动的对应如下图所示（来源[NVIDIA CUDA Toolkit Release Notes](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#abstract)）
![](./img/cuda_toolkit-driver_version.png)

首先检查自己当前的cuda driver，启动terminal输入
```
$ cat /proc/driver/nvidia/version 
```
可查看到自己当前的cuda driver版本，如下
```
NVRM version: NVIDIA UNIX x86_64 Kernel Module  450.57  Sun Jul  5 14:42:25 UTC 2020
GCC version:  gcc version 9.3.0 (Ubuntu 9.3.0-10ubuntu2) 
```
cuda driver 版本号为 450.57， 可对应到上图中的cuda 11，因此可安装最新的cuda。

当发现自己的cuda driver版本号较低而cuda版本高时，可以选择：
1. 升级cuda driver 
\
NVIDIA 驱动程序下载[[https://www.nvidia.cn/Download/index.aspx?lang=cn#]](https://www.nvidia.cn/Download/index.aspx?lang=cn#)
根据自己的显卡型号，下载相应的cuda driver，之后进行安装（安装时可能会提示建议通过Linux Softwares&Updates中的Additional Drivers进行安装，可以不管）
**安装完之后重启电脑即可。**
\
更新cuda driver还可以解决 ubuntu不能扩展显示器的问题.
\
\
也可以使用apt进行安装。首先查看支持的显卡驱动，在终端输入 ` ubuntu-drivers devices `，出现下图结果，
![](./img/ubuntu_driver.png)
\
然后，选择其中一个可选 driver 进行安装，`sudo apt install nvidia-driver-450`，安装完之后重启。

2. 重新安装低版本cuda
\
下载地址[[https://developer.nvidia.com/cuda-downloads]](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu)

NVIDIA 相关包的卸载
```
# remove nvidia-related package
sudo apt purge nvidia*
# remove the remind package
sudo apt autoremove
```

### 2. Ubuntu 无法检测到多个显示器

随着前一个问题解决，这个问题就能同时解决。

首先查看 Setting -> About -> Software Updates -> Additional drivers（或者搜索 Software Updates） 中是否有其他 Drivers，如果没有，则打开终端 ，输入
```
$ sudo add-apt-repository ppa:graphics-drivers/ppa && sudo apt update
```

更新一下图形驱动，更新完之后打开系统设置 Setting -> About -> Software Updates -> Additional Drivers
然后能看到如下图所示，多了新的 Driver

![](./img/ubuntu_nvidia_driver.png)

选择一个，点击 “Apply Changes”，等更新完之后，重启计算机看看是可行，不行了再更换一个 Driver，再更新下。

参考自[[ubuntu16.04 检测不到扩展屏幕（解决方案）]](https://blog.csdn.net/zou_albert/article/details/106521647)
