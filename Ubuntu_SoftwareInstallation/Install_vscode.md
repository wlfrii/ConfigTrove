# Install Visual Studio Code on Ubuntu

## 1. 下载

去 [VS code官网下载](https://code.visualstudio.com/download) Linux版本的安装包。当前能够下载的最新版本为`code_1.95.3-1731513102_amd64.deb`。

## 2. 安装

进入到下载文件所在的目录，然后进行安装。
我常用的两个安装`.deb`文件的指令如下：
```shell
$ sudo apt install ./code_1.95.3-1731513102_amd64.deb
```
或者
```shell
$ sudo dpkg -i ./code_1.95.3-1731513102_amd64.deb
```



## 3. 配置

以下选择，按需配置。这里的配置只记录了我需要用的内容。

### 3.1 基础功能

#### 1. 自动保存

在 vs code 左下角打开`Manage`->`Settings`，搜索 "Save"，然后：
+ 找到 “Files: Auto Save”，设置为 “afterDelay”；
+ 找到 “Files: Auto Save Delay”，按需设置 Delay 的时间，单位是毫秒。

#### 2. 关闭Minimap
在 vs code 左下角打开`Manage`->`Settings`，搜索 "Minimap"，然后：
+ 找到`Editor> Minimap: Enabled`，取消勾选。

### 3.1 程序开发

#### 1. C++

#### 2. CMake

#### 3. Python

在 vscode 的 `Extensions`（快捷键`Ctrl+Shift+X`） 工具栏中搜索 `Python`，然后在搜索结果中，安装以下插件：
+ Microsoft 开发的 "__Python__"。
+ Microsoft 开发的 "__Python Debugger__"

运行 python 程序前，在 vs code 中按 `Ctrl+Shift+P`，然后搜索 “Interpreter”，选择 “Python: Select Interpreter”，然后在新的下拉框中选择需要的运行环境。

### 3.2 文档编辑

#### 1. Markdown

当前最受欢迎的 Markdown 插件如下，可按需安装：

1. __Markdown Preview Enhanced__
   开发者：Yiyi Wang
   特点:
   + 增强的预览功能: 提供比内置预览更多的功能，包括数学公式、图表、任务列表等支持。
   + 自定义 CSS: 允许用户自定义预览样式。
   + 导出功能: 支持将 Markdown 文件导出为 PDF、HTML 等格式。

2. __Markdown All in One__
   开发者：Yu Zhang
   特点:
   + 综合功能: 提供一系列实用功能，包括快捷键、自动完成、预览、格式化和 TOC（目录）生成。
   + 实时预览: 支持实时查看 Markdown 内容的格式。
   + 快捷键支持: 提供多种快捷键，简化 Markdown 编辑。

#### 2. Doxygen