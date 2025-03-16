#! https://zhuanlan.zhihu.com/p/428480219
# 【Win10 - OpenCV】 on MATLAB

最近在使用 MATLAB 做测试，由于要使用 cv::findContours() 函数但又懒得用 C++/Python 再搞一下，所以选择 MEX 一下 OpenCV。
MEX 过程参见[[https://github.com/kyamagu/mexopencv]](https://github.com/kyamagu/mexopencv)，由于踩了非常多的坑，所以整理此篇配置过程，希望能帮到有需要的人！

![](./img/smart_like_me.gif)

## 1. 下载 OpenCV, opencv_contrib, 和 mexopencv

参照 [mexopencv/wiki](https://github.com/kyamagu/mexopencv/wiki/Installation-%28Windows%2C-MATLAB%2C-OpenCV-3%29) 中的安装说明，下载最新的稳定的 OpenCV 版本。

当前的稳定版本为 opencv-3.4.1

然后下载 mexopencv341 源码 [[https://github.com/kyamagu/mexopencv/releases/tag/v3.4.1]](https://github.com/kyamagu/mexopencv/releases/tag/v3.4.1)

## 2. 配置 OpenCV

这里需要 [CMake](https://cmake.org/download/) 和 [C++ 编译器](https://www.mathworks.com/support/requirements/supported-compilers.html)，我的电脑上是 VS 2017.
为确保自己计算机上的 C++ 编译器可用，可以先在 MATLAB 命令行中输入 `mex -setup` 然后可以看到如下所示的结果，则表示 MATLAB 可以识别 VS2017 为编译工具。
```MATLAB
>> mex -setup
MEX 配置为使用 'Microsoft Visual C++ 2017 (C)' 以进行 C 语言编译。
警告: MATLAB C 和 Fortran API 已更改，现可支持
	 包含 2^32-1 个以上元素的 MATLAB 变量。您需要
	 更新代码以利用新的 API。
	 您可以在以下网址找到更多的相关信息:
	 https://www.mathworks.com/help/matlab/matlab_external/upgrading-mex-files-to-use-64-bit-api.html。

要选择不同的语言，请从以下选项中选择一种命令:
 mex -setup C++ 
 mex -setup FORTRAN
```

然后启动 `cmake-gui.exe`，以下步骤主要参照[mexopencv/wiki](https://github.com/kyamagu/mexopencv/wiki/Installation-%28Windows%2C-MATLAB%2C-OpenCV-3%29)，有坑的地方我会黑体标注出来：

1. 设置源代码路径为 `xxx/opencv341/` （根据自己目录修改）

2. 设置生成路径为 `xxx/opencv341_build/`（根据自己目录修改）

3. 点击 "__Configure__"，然后默认会选择 Visual Studio 15 2017 作为编译器，**注意，一定要在第二个选项中选择 x64，否则后面编译会有问题**，然后点击 "__Finish__" \
![](./img/cmake_configure.jpg) \
**这里我的编译窗口中出现 `ffmpeg` 和 `ippicv` 的编译警告，查看了 `CMakeDownloadLog.txt` 之后发现是下载错误，尝试了多次手动下载安装之后还是不行，我选择不编译这两项**了。（因为我只是需要在 MATLAB 中进行部分 OpenCV 函数的调用，用不到视频库 `ffmpeg` 和异步计算库`ippicv`）
![](./img/cmake_warning.jpg) \
在 `cmake-gui` 的搜索框搜索 “with”， 将 `WITH_FFMPEG` 和 `WITH_IPP` 取校勾选，再次点击 "__Configure__" 应该就没有报错了。

4. 取校勾选 [mexopencv/wiki](https://github.com/kyamagu/mexopencv/wiki/Installation-%28Windows%2C-MATLAB%2C-OpenCV-3%29) 中列出的 "BUILD" 项（有一些项不存在，有一些默认没有勾选，只要确保下面这些项是没有勾选上的就行）： \
    BUILD_DOCS, BUILD_EXAMPLES, BUILD_PACKAGE, BUILD_PERF_TESTS, BUILD_TESTS, BUILD_JAVA, BUILD_opencv_apps, BUILD_opencv_cuda*, BUILD_opencv_cudev, BUILD_opencv_js, BUILD_opencv_java*, BUILD_opencv_python*, BUILD_opencv_ts, BUILD_opencv_viz, BUILD_opencv_world

5. **设置 `opencv_contrib341/modules` 路径，这里如果添加了这个模块路径，并进行 "__Configure__" 的话，**会报 CMake Error**，`.cmake` 文件看了下，有点复杂，所以...放弃调试和修改了。 \
因此建议不添加 `opencv_contrib` 模块，毕竟只是为了方便在 MATLAB 上进行一些测试和验证 ~** \
![](./img/cmake_error.jpg)

6. 重新进行 "__Configure__" 并确保没有错误和警告之后，点击 "__Generate__" 生成 `.sln` 文件。然后点击 "__Open Project__"，会默认打开 VS 2017。 \
1- **首先设置编译输出为 "Release"，必须是 Release 版本**； \
2- 然后 （1）“右键 ALL_BUILD”-“生成”； （2）“右键 INSTALL” - “生成”，随后会在 `cmake-gui` 指定的生成目录`xxx/opencv341_build/`中多一个 `install` 文件夹；\
3- 再将生成文件夹下的 `xxx/opencv341_build/install/x64/vc15/bin/` 目录添加至系统环境变量中，**因为在 MATLAT 中调用 OpenCV 函数时候，会去加载这些编译生成的 .dll 文件，如果找不到就会报错。**

## 3. Mex OpenCV 

上面添加了环境变量，所以这里操作之前先重启以下 MATLAB，以确保加载了新的路径。

这里继续参照 [mexopencv/wiki](https://github.com/kyamagu/mexopencv/wiki/Installation-%28Windows%2C-MATLAB%2C-OpenCV-3%29)，首先在 MATLAB 命令行中执行以下操作，
```MATLAB
>> cd('xxx/mexopencv')      
>> addpath('xxx/mexopencv')                         
>> mexopencv.make('opencv_path', 'xxx/opencv341_build/install') % 设置OpenCV路径为通过VS编译生成的路径，并开始make
```

**注意，这里会有错误 ...Unknown MEX argument '-R2017b-largeArrayDims'...**，这是因为无法识别 **-R2017b** 参数，找到下载的 mexopencv341 路径下的 `xxx/mexopencv341/+mexopencv/make.m` 文件，打开，定位到 276 行，如下，将这几行注释掉。
```MATLAB
    ......
276 | %     if ~mexopencv.isOctave() && ~verLessThan('matlab', '9.4')
277 | %         % keep using the "separate complex storage", as opposed to the
278 | %         % "interleaved complex storage" introduced in R2018a
279 | %         % (see MX_HAS_INTERLEAVED_COMPLEX)
280 | %         mex_flags = ['-R2017b' mex_flags];
281 | %     end
    ......
```

然后重新 make，
```MATLAB
>> mexopencv.make('opencv_path', 'xxx/opencv341_build/install')
```

等待一点点时间， ![](./img/yidiandian.png)

直到 mex 编译完成~

## 4. 测试

然后，在 MATLAB 命令行中，执行 `addpath('xxx/mexopencv') ` 和 `cv.getBuildInformation()`，没错的话会得到如下结果，
```MATLAB
>> addpath('xxx/mexopencv') 
>> cv.getBuildInformation()

General configuration for OpenCV 3.4.1 =====================================
  Version control:               unknown

  Platform:
    Timestamp:                   2021-11-01T10:48:46Z
    Host:                        Windows 10.0.19043 AMD64
    CMake:                       3.17.2
    CMake generator:             Visual Studio 15 2017
    CMake build tool:            C:/MyProgramFiles/Microsoft Visual Studio/2017/Community/MSBuild/15.0/Bin/MSBuild.exe
    MSVC:                        1916

  CPU/HW features:
    Baseline:                    SSE SSE2 SSE3
      requested:                 SSE3
    Dispatched code generation:  SSE4_1 SSE4_2 FP16 AVX AVX2
      requested:                 SSE4_1 SSE4_2 AVX FP16 AVX2 AVX512_SKX
      SSE4_1 (3 files):          + SSSE3 SSE4_1
      SSE4_2 (1 files):          + SSSE3 SSE4_1 POPCNT SSE4_2
      FP16 (1 files):            + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 AVX
      AVX (5 files):             + SSSE3 SSE4_1 POPCNT SSE4_2 AVX
      AVX2 (9 files):            + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2

  C/C++:
    Built as dynamic libs?:      YES
    C++11:                       YES
  ......
```

如果报 "**找不到 .dll 文件**" 的错误的话，检查下环境变量中编译生成的 opencv 路径是否正确。

成功之后，每次使用的时候要包含下 mexopencv 的路径！即
```MATLAB
>> addpath('xxx/mexopencv') 
```
通过 "`help cv`" 指令可以查看可用的 opencv 函数。

![](./img/done.jpg)