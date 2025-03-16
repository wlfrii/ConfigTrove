# 【Windows + Ubuntu】 组装机的双系统安装

得空自己组装了台式机，组装教程推荐B站：[【装机教程】全网最好的装机教程，没有之一](https://www.bilibili.com/video/BV1BG4y137mG/?spm_id_from=333.999.0.0&vd_source=78f0bc01933d5520a1502d2f92fd3b77)，视频做的真的好！

这里记录一下双系统安装的时建议和遇到的问题。

## 1. 准备工作

### 1.1 制作启动盘

先使用其他电脑做一个启动盘，例如这里我用另一个windows系统的电脑制作。制作工具推荐 [Ventoy](https://www.ventoy.net/cn/index.html)，好用！
用Ventoy做好启动盘后，可以放 **N** 个系统的 iso 文件，方便多系统安装。

下载后的 Vectoy 文件夹下的内容参考如下：
![](./img/ventoy_installation_file.png)

双击`Ventoy2Disk.exe`后的界面参考如下（如果插上U盘，`设备`那一行会自动检测到）：
![](./img/ventoy_ui.png)

制作启动盘时候有几个注意点：
1. U盘内存尽量大一些（不小于8G）
2. 点击左上角`配置选项`->`分区类型`->`GPT`。
  > 补充说明：`MBR`是比较老的分区策略了，当前为了能够识别更大的硬盘，绝大多数新的主板都设置`GPT`分区了。以我用的华硕 Z790 为例，如果这里设置`MBR`会导致win11系统无法识别硬盘而导致无法安装的问题。**这里参考你使用的主板**。
3. 点击左上角`配置选项`->`分区设置`，这里根据需求设置，我的U盘会用在多个系统，包括Mac，所以设置了`exFAT`。

上述注意点搞好后，确保选择好了U盘（提前备份好数据，第一次制作会格式化U盘），然后点集`安装`。

安装好了之后，后续只需要把你要安装的系统放入U盘即可，后续安装系统的时候可以选择安装哪个系统。

### 1.2 系统下载

既然微软已经官宣后续不在维护 Win10 了，那么大家还是安装 Win11 吧。

win11[官网下载](https://www.microsoft.com/zh-cn/software-download/windows11)。因为我这里使用 Vectoy 工作来装，所以下载第三个：**下载适用于 x64 设备的 Windows 11 磁盘映像 (ISO)**。

ubuntu[官网下载](https://cn.ubuntu.com/download)。

## 2. 系统安装

在安装双系统（Windows 和 Linux）时，**建议先安装 Windows，然后再安装 Linux**。原因如下：

+ 引导管理：
> Windows 安装程序会覆盖启动加载器（boot loader），这意味着如果先安装 Linux，然后再安装 Windows，Windows 会将 Linux 的引导记录删除，导致无法启动 Linux。
安装 Windows 后，Linux 的引导加载器（如 GRUB）可以识别 Windows，并且可以将其添加到启动菜单中。

+ 兼容性：
> 大多 Linux 发行版会考虑到 Windows 的存在，因此在安装时可能更容易处理已存在的 Windows，特别是在设置多重启动时。

### 2.1 关闭安全启动


### 2.1 安装Win11

1. 首先进入BIOS，不同主板进入BIOS的指令不同，例如`F2, F12, DELETE`等等，具体可自行搜一下。
2. 关闭“安全启动”，如果不关闭，直接使用U盘安装系统时，会出现 “**Verification failed: (0x1A) Security Violation**” 之类的错误。以我在用的 华硕Z790 主板为例，进入BIOS后，找到`Boot`，然后在 Boot Secure 中找到 `OS Type`，修改为 `Other OS`，就表示关闭安全启动了。
   这里我没有截图，大家可以参考华硕官网：[[主板]如何开启或者关闭安全开机(Secure Boot)](https://www.asus.com.cn/support/faq/1049829/).
3. 然后 `Exit`，保存、重启。
4. 重启后进入 BIOS 选择 U 盘启动。应该就可以看到 Ventoy 界面了。选择 win11 系统，之后一步一步：（1）boot in normal mode; (2) ...
   安装就好。
   > 有几个注意点提一下：
   > 1. 密钥跳过；
   > 2. 到了联网的那一步，可能会出现不能直接跳过，参考微软官网的方法：[安装系统时没有网络无法完成设置进入系统](https://answers.microsoft.com/zh-hans/windows/forum/all/%E5%AE%89%E8%A3%85%E7%B3%BB%E7%BB%9F%E6%97%B6/972194a6-4a7d-44e5-bbc3-a870a1fc09ea) ，操作之后就会在网络连接那个页面多一个 “<u>`我没有Internet连接`</u>” 的选项了。

5. 系统安装之后，连接网线开始各种驱动、软件的安装就好了。如果主板支持WIFI，也可以用别的电脑，搜索你的主板对应的无线网卡驱动，安装之后也能用。

以下配置看需求，无需求的话，直接跳过吧。

（以下步骤需要先激活系统，直接买正版就好了）
6. 关闭任务栏左下角的组件：`设置`->`个性化`->`任务栏`->`小组件`->选择`关闭`。
7. 关闭锁屏状态下，桌面下方的组件：`设置`->`个性化`->`锁屏界面`->`锁屏界面状态`->选择`无`。

#### 安装 SSH

1. 首先进入系统的`设置`->`系统`->`可选功能`，点击`选择添加功能`右侧的`查看功能`，搜索`ssh`，勾选`OpenSSH客户端`和`OpenSSH服务器`，然后直接点`下一步`，自动安装。
2. 安装之后，在`设置`->`系统`->`可选功能`页面下，查看已安装列表下是否包含了`OpenSSH客户端`和`OpenSSH服务器`这两项，不包含的话就重启一下再看一下。确保安装好了。
3. 可以终端检查一下，输入
   ```Shell
   $ Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
   ```
   之后应该会输出下述结果
   ```Shell
   Name  : OpenSSH.Client~~~~0.0.1.0
   State : Installed

   Name  : OpenSSH.Server~~~~0.0.1.0
   State : Installed
   ```
4. 管理员打开`powershell`，输入
   ```Shell
   $ net start sshd
   ```
   之后输出
   ```Shell
   OpenSSH SSH Server 服务正在启动 ..
   OpenSSH SSH Server 服务已经启动成功
   ```
5. `ping`一下测试一下，如果`ping`通了，正常ssh功能就可用了。
   如果`ping`不通，则找到：
   1. `设置`->`网络和Internet`，打开你在用的网络，例如我这里用的是有线，那么打开 `以太网` 页面，看一下你用的是“公用网络”还是“专用网络”，设置成哪个都可以。
   2. 进入 `设置`->`网络和Internet`->`高级网络设置`->`高级共享设置` 页面，将你在用的网络，“公用网络”或“专用网络”，中的“网络发现”、“文件和打印机共享”全部勾选上。
   3. 在`ping`一下测试，应该就OK了。


### 2.2 安装Ubuntu

0. 磁盘准备：windows安装好之后，在windows中`计算机管理`-`磁盘管理`中给 Ubuntu 分出来一部分空间。
   1. 如果你的Ubuntu和Windows系统共用一个硬盘，那么就在已有的硬盘中压缩、删除卷出来。
   2. 如果是两个独立的硬盘分别安装系统，以我这里的情况为例，两个固态分别安装两个系统，那么需要在Windows中对另一个磁盘做初始化，否则无法识别磁盘。初始化时候选“GPT”即可。
1. 同前面“安装Win11”中的前两步，首先要在BIOS中关闭“安全启动”。
2. 重启后进入 BIOS 选择 U 盘启动。应该就可以看到 Ventoy 界面了。选择 win11 系统，之后一步一步安装就好：
   1. boot in normal mode;  
   2. Try and install ubuntu; 
   3. Install Ubuntu (同时选择语言，建议English);
   4. continue;
   5. Normal installation (内存够的话建议选正常安装); Download updates while installing Ubuntus.
   6. Installation type(安装类型)中选择 "Something else"。然后找到预留给Ubuntu系统的磁盘，点击选中磁盘，然后点下边的加号“+”：
      1. 设置**引导分区**：勾选“Primary(主分区)”，“Beginning of this space(空间起始位置)”，Use as(用于)：`EFI System Partition(EFI系统分区)`，我设置了500MB, 大小设置参考下面的详细介绍；
      2. 设置**交换分区**：勾选“Primary(主分区)”，“Beginning of this space(空间起始位置)”，Use as(用于)：`swap area(交换空间)`，我设置了32G，大小设置参考下面的详细介绍；
      3. 设置**根分区**：勾选“Primary(主分区)”，“Beginning of this space(空间起始位置)”，Use as(用于)：*`Ext4 journaling file system(Ext4 日志文件系统)`，Mount point(挂载点)：**“/”**，我设置了50G， 大小设置参考下面的详细介绍；
      4. 设置**var分区**（非必须）：勾选“Primary(主分区)”，“Beginning of this space(空间起始位置)”，Use as(用于)：`Ext4 journaling file system(Ext4 日志文件系统)`，Mount point(挂载点)：**“/var”**，我设置了10G， 大小设置参考下面的详细介绍；
      5. 设置**home分区**（非必须）：勾选“Primary(主分区)”，“Beginning of this space(空间起始位置)”，Use as(用于)：`Ext4 journaling file system(Ext4 日志文件系统)`，Mount point(挂载点)：**“/home”**，**剩下的所有空间都给home**， 大小设置参考下面的详细介绍；
      
      `Device for boot loader installation(安装启动引导器的设备)`设置：
      1. 一些建议中说要设置成引导分区对应的分区，例如我这里的“Device=/dev/nvme0n1p1, Type=efi, Size=499MB”的分区，但是实际上可能选不了；
      2. 直接设置成对应的磁盘，例如我这里的“/dev/nvme0n1p1 Samsung SSD ...”。
   7. `Install Now` -> Continue, 设置地区，等待安装完成。
   

这里主要讲一下 Ubuntu 系统安装的分区说明。以我这里的硬件为例：1T SSD，32G RAM，分区建议如下：
<table>
<tr> <th>分区</th> <th>建议大小</th> <th>说明</th> </tr>
<tr> <td>/boot（引导分区）</td> <td>500MB - 1GB</td> <td>引导分区用于存放引导加载器和内核文件。500MB 足以，但如果计划安装多个内核或有特殊需求，可以分配到 1GB</td> </tr>
<tr> <td>swap（交换分区）详细介绍在下边</td> <td>8GB - 16GB</td> <td>对于 32GB 的 RAM，8GB 的 swap 通常足够。如果计划使用休眠功能，建议将 swap 大小设置为与 RAM 大小相等（32GB），但一般情况下，8GB - 16GB 足以满足需求</td> </tr>
<tr> <td>/（根分区）</td> <td>30GB - 50GB</td> <td>根分区包含系统文件和大部分应用程序。对于一般用途，30GB 通常足够，但如果打算安装很多软件，可以增加到 50GB</td> </tr>
<tr> <td>/home（用户目录）</td> <td>其余空间（约 900GB - 950GB）</td> <td>/home 是用户数据存储的位置，包括文档、下载、配置文件等。由于您有 1TB 的 SSD，分配大部分空间给 /home 是合理的</td> </tr>
<tr> <td>/var（可变数据）非必须，详细介绍在下边</td> <td>5GB - 10GB</td> <td>/var 存储动态数据，如日志文件、缓存等。一般情况下，5GB - 10GB 足够，但根据使用情况可以适当调整</td> </tr>
</table>

**额外建议**：
+ 使用 LVM（逻辑卷管理）：如果希望在未来更灵活地调整分区大小，考虑使用 LVM。在安装过程中选择 LVM，可以更方便地管理分区。

#### swap分区说明

很多人不清楚“swap分区”的作用，这里扩展一下swap的主要用途：
1. **虚拟内存扩展**：
当系统的物理内存（RAM）使用完时，swap 分区可以临时存储不活跃的内存页面，从而释放 RAM 中的空间给当前正在使用的程序。

1. **内存管理**：
操作系统可以将不常用的数据或进程移动到 swap 中，这样可以确保系统在高负载情况下仍然正常运行，而不会因为内存不足而崩溃。

1. **休眠功能**：
如果启用了休眠（suspend to disk）功能，系统会将当前的内存状态保存到 swap 分区中。当计算机重新启动时，操作系统可以从 swap 中恢复到先前的状态。

1. **性能提升**：
在某些情况下，swap 可以帮助优化系统性能，尤其是在运行大型应用程序或多个进程时，即使速度比 RAM 慢，它仍然提供了一种缓解内存压力的方式。
**但是**，请注意，swap 的读写速度比 RAM 慢得多，因此如果系统频繁使用 swap，会导致性能下降。理想情况下，系统应该有足够的物理内存来避免过度依赖 swap。

#### /var分区说明

设置 /var 分区是可选的，具体取决于使用需求，该分区的作用如下：

1. **日志文件管理**: /var 目录通常存储系统和应用程序的日志文件。如果日志文件增长过快，单独分区可以防止它们占用根分区的空间。
2. **缓存和临时文件**: /var 还包含邮件、缓存和其他动态数据，分开管理可以提高系统的稳定性和安全性。
3. **提高安全性**: 将 /var 分区设置为只读模式（如果适用）或限制其大小，可以提高系统的安全性。
分区类型

类型: EXT4（推荐）
大小: 根据预期的数据量设置，通常建议至少 10GB，具体视应用和使用情况而定。

