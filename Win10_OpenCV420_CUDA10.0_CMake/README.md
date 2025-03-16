#! https://zhuanlan.zhihu.com/p/425133410
# 【Win10 - OpenCV-CUDA】with VS2017 and CUDA 10.0 (cuDNN)

2021.10.24 补充：CUDA toolkit 版本受计算机的 CUDA driver 版本限制，确定 CUDA driver 版本之后再去下载可用的 CUDA toolkit，对应好了 CUDA toolkit 版本才能确定好相应的 cuDNN 版本，否则版本不匹配会导致程序运行时有 dll 找不到的问题。
这里可参照 [【Win10 - Python Keras】with CUDA and cuDNN](https://zhuanlan.zhihu.com/p/424991762) 来确定 CUDA (cuDNN) 版本。

---

下面的配置过程是 19 年写的，当时是为了使用 cv::GpuMat 传数据和 cv::cuda 命名空间下的一些方法。

## 1. 环境

我配置 OpenCV 时的环境如下：

+  OS - Windows 10
+  VS 2017. [Visual Studio Download](https://visualstudio.microsoft.com/zh-hans/downloads/?rr=https%3A%2F%2Fcn.bing.com%2F)
+  CUDA 10.0. [CUDA Download](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork) 
+  CMake 3.17. [CMake Download](https://cmake.org/download/)
+  OpenCV 4.2.0 [OpenCV Download](https://opencv.org/releases/)
+  opencv_contrib 4.2.0 [opencv_contrib Download](https://github.com/opencv/opencv_contrib)


## 2. 在 VS 中测试 CUDA

安装 CUDA 时候会选择集成在 VS 中，安装之后有 samples，试着跑一下测试下。关于库路径正常添加就可以了。

![](./imgs/1589251468(1).jpg)

## 3. 使用 CMake 编译支持 CUDA 的 OpenCV

### 3.1 Configure OpenCV
打开 `cmake_gui.exe`, 最上方两个文本框，分别输入 OpenCV 源代码路径下的 `xxx/opencv/source/` 的路径，和将要存储生成文件的路径，如`xxx/opencv_cmake/`。

然后点击 "__Configure__"，第一次会弹出下框，选择对应的版本即可。**注意一定要联网**，配置过程中需要下几个包。

![cmake](./imgs/1589252024(1).jpg)

然后可能会出现个python的错误，忽略就行
```Shell
CMake Warning at cmake/OpenCVDetectPython.cmake:81 (message):
  CMake's 'find_host_package(PythonInterp 2.7)' founds wrong Python version:

  PYTHON_EXECUTABLE=D:/Python3.8.1/python.exe

  PYTHON_VERSION_STRING=3.8.1

  Consider specify 'PYTHON2_EXECUTABLE' variable via CMake command line or
  environment variables

Call Stack (most recent call first):
  cmake/OpenCVDetectPython.cmake:271 (find_python)
  CMakeLists.txt:585 (include) 
```

下面这个错误也忽略

```Shell
CMake Warning at cmake/OpenCVGenSetupVars.cmake:54 (message):
  CONFIGURATION IS NOT SUPPORTED: validate setupvars script in install
  directory
Call Stack (most recent call first):
  CMakeLists.txt:947 (include) 
```

然后，**对于opencv 4.0以上版本**，再勾选上`BUILD_opencv_world`。编译出的带有 CUDA 的 OpenCV 库就会存在一个 `opencv_world.hpp` 文件，这个文件包含了 OpenCV 所有的头文件。

### 3.2 Configure 'opencv_contrib'

搜索框中搜 `OPENCV_EXTRA_MODULES_PATH`，并在之后的 value 中输入路径。
![](./imgs/1589252431(1).jpg)

然后再在搜索框中搜 `cuda`，对 `BUILD_CUDA_STUBS` 和 `WITH_CUDA`，以及 `CUDA_FAST_MATH` 打勾

![](./imgs/1589252721(1).jpg)

再点击 "__Configure__"

之后的 `CUDA_ARCH_BIN` 后面的数字表示GPU支持的算力，要找对应的算力保留就行。

![](./imgs/1589252834(1).jpg)

例如`Quadro P1000`算力是6.1，`GTX 2060`算力是7.5，部分笔记本显卡的算力情况如下图，其他可自查 [GPU Compute Capability](https://developer.nvidia.com/cuda-gpus)

![](./imgs/1589253943(1).jpg)

### 3.3 (可选) 添加 cuDNN

若需要在 CUDA 上进行深度学习，则还需要安装 cdDNN，介绍参见[CUDA与cuDNN](https://www.jianshu.com/p/622f47f94784)

下载安装 cdDNN 后，使用 `cmake_gui` 进行 OpenCV 的 "__Configure__"时，在输出框中会看见结果中显示，cuDNN 后面显示的是 YES。如下图，我没有配置 cuDNN，所以相应项为 NO。

![](./imgs/1589254650(1).jpg)

然后在搜索框搜 `BULID_CUDA_DNN`，打上勾，再 `Configure` 即可。

### 3.3 编译生成INSTALL

检查输出结果中没问题后，点击 "__Generate__"，之后显示如下与 cuda有关的项。

<img src="./imgs/1589271745(1).png">

点击 `cmake_gui` 上的 "__Open Project__"，进入 VS，在解决方案资源管理器中找到 "__CMakeTargets__"，然后选择 `All_BUILD -> 右键"生成"`。（debug 和 release 两个模式下都可以生成下）。

![](./imgs/1589255387(1).png)

然后选择 `INSTALL -> 右键"仅用于项目" -> 仅生成INSTALL`。

之后在指定的文件夹 `xxx/opencv_cmake/` 下会有一个 `xxx/opencv_cmake/install/`文件夹，将该文件夹下的 OpenCV 库已经将 CUDA 添加进去了。


## Reference

[OpenCV4 | 如何让传统图像处理实现三十倍加速的顶级技能](https://cloud.tencent.com/developer/article/1523416)

[YOLOv3Tiny 仅需 2.17ms，OpenCV 4.2 DNN with CUDA 示例](https://bbs.cvmart.net/topics/1417)