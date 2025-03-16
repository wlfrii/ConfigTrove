# Install Chinese pinyin on Ubuntu

>系统版本：Ubuntu 22.04

在Linux上，常见的输入法框架有三种：fcitx、ibus、xim。其中 ibus 在我的一台主机上使用了大半年，总体感受就是非常不智能，即便配置了常用词库、打开了智能化选项，因此在新的Ubuntu主机上准备尝试一下 fcitx 框架。

## 0. 更新系统和包

确保你的系统是最新的，如果不是则建议更新：
```shell
$ sudo apt update
$ sudo apt upgrade
```

## 1. 安装中文支持包

确保你的系统安装了中文语言支持包。在终端中运行：
```shell
$ sudo apt install language-pack-zh-hans
```

（按需）检查系统语言环境：
`System settings`->`Region & Language`，点击 `Manage Installed Languages`，之后会有弹窗提示安装完善输入法支持。可以点`Details`查看下具体的安装项，有需要的就点击`Install`安装就好了。
这里增加一个补充说明：
> 在 `Details` 列表中看到有 ibus 相关的包，因为 Ubuntu 默认会使用 ibus 框架，这里点击 `Install` 后会安装 ibus 的一些包，建议非必须先不要安装，因为两个输入法框架之间可能会有一些共同依赖项，后期如果卸载 ibus 后，可能会导致 fcitx 不能用的问题。

## 2. 安装fctix5框架和拼音输入法

安装 fcitx5 和中文输入法：
```shell
$ sudo apt install fcitx5 fcitx5-chinese-addons fcitx5-pinyin
```

## 3. 配置 Fcitx5

### 3.1 在后台启动 Fcitx5

在终端中运行：
```shell
$ fcitx5 &
```
**稍后将 fcitx5 的启动添加至自动启动项中。**

### 3.2 打开配置工具

1. 打开 Fcitx5 配置工具
```shell
$ fcitx5-configtool
```
界面如下：
<img src="./__md__/fcitx_configuration_1.png" scale="70%"/>

1. 添加输入法
在 Fcitx5 配置窗口中，点击左侧的“Input Method (输入法)”。
点击右侧的“+”按钮，搜索并选择你需要的输入法（如 “Pinyin”），然后点击“OK(确定)”，操作如下：
<img src="./__md__/fcitx_configuration_2.png" scale="70%"/>

3. (按需)设置快捷键
在 Fcitx5 配置工具中，选择“Global Options(全局配置)”选项卡。
在这里，你可以设置切换输入法的快捷键，默认是 `Super + Space`/`Ctrl + Space`。

## 4. 设置环境变量

为了确保 Fcitx5 正常工作，需要设置环境变量。换进变量的设置可以在系统文件`/etc/profile`，用户文件`~/.bash_profile`或`~/.xprofile`中设置，以当前的配置为例，**建议配置在**`~/.xprofile`中。
```shell
export GTK_IM_MODULE=fcitx5
export QT_IM_MODULE=fcitx5
export XMODIFIERS=@im=fcitx5
```

如果是配置在系统文件中的，使配置文件生效的指令如下，无需重启。
```shell
$ source /etc/profile 
```

**错误例子**：我首次是配置在系统文件`/etc/profile`中的，在电脑重启前输入法都是OK的，重启后出现问题 [6.1 输入法无法切换](#section6.1) 的问题。

## 5. 将 Fcitx5 添加至自动启动

1. 打开“Startup Applications (启动应用程序)”软件。
   
2. 点击“Add(添加)”，填写名称（如 Fcitx5）和命令（fcitx5），然后保存。
   <img src="./__md__/fcitx_startup.png" scale="70%" />

## 6. 使用中发现的问题和相应的解决方法

### 6.1 输入法无法切换<a id="section6.1"></a>

首次配置好中文输入法之后，在使用完电脑再重启后，发现 `fcitx5` 正常启动了，但是输入法不生效，无法切换输入法，鼠标点击也无用，在不同的软件中尝试过也都无效。
这里的解决方法是将前面的环境变量设置在`~/.xprofile`文件中，如果无该文件则创建一个：
```shell
$ sudo vi ~/.xprofile
```
然后添加环境变量：
```shell
export GTK_IM_MODULE=fcitx5
export QT_IM_MODULE=fcitx5
export XMODIFIERS=@im=fcitx5
```

重启之后，输入法OK了。多次重启测试后也OK。


