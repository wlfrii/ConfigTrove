# Install NVIDIA driver on Ubuntu

## 1. 官网下载

进入英伟达[驱动下载官网](https://www.nvidia.cn/geforce/drivers/)，然后根据显卡类型下载相应的驱动，能够支持的驱动版本比较多，选比较新的驱动下载即可。

下载完之后，进入`Donwloads`目录，以此处的驱动文件为例，给驱动文件附加权限：
```shell
$ sudo chmod 777 NVIDIA-Linux-x86_64_550.135.run
```
`xxx`表示版本号，替换成下载的实际版本号。

然后安装：
```shell
$ sudo ./NVIDIA-Linux-x86_64_550.135.run
```

之后按步骤安装即可。

**但是**，上述方法可能会出错，安装不成功，这时可以使用下面的方法安装。

## 2. 使用apt工具

搜索一下可用shell的驱动版本：
```
$ apt search nvidia-driver
```

会出现一大堆东西，找一下跟官网中下载的驱动版本号`xxx`相同或相似的驱动，名称应该为`nvidia-driver-550`，然后终端安装
```shell
$ sudo apt install nvidia-driver -y
```

安装过程中会安装一些依赖项，时间可能会略久一点点，安装完成之后，查看
```shell
$ ll /usr/src/ | grep nvidia
```
若安装成功后，以我这里为例，会输出
```shell
drwxr-xr-x   9 root root XXXX N月 DD HH:ss nvidia-550.120
```

## 3. 检查驱动

终端运行：
```shell
$ nvidia-smi
```

若出现
```
NVIDIA-SMI has failed because t couldn't communicate with NVIDIA driver. Make sure that 
the latest NVIDIA driver is installed and running.
```

则检查下一下Toolkit，
```shell
$ nvcc -V
```

没安装的话，会出现：
```
Command 'nvcc' not found, but can be installed with:
sudo apt install nvidia-cuda-toolkit
```
按照提示，安装Toolkit：
```shell
sudo apt install nvidia-cuda-toolkit
```

安装结束之后，运行`nvidia-smi`还会出现上述`NVIDIA-SMI has failed because t couldn't communicate ...`之类的错误。

则先重启，重启之后应该就OK了
```
$ reboot
```

### 3.1 其他相关操作

#### 3.1.1 dkms安装

Ubuntu系统会预安装`dkms` (Dynamic Kernel Module Support)工具，如果没有，可以手动安装
```shell
$ sudo apt install dkms
```

NVIDIA显卡驱动的`dkms`包应该在安装显卡的同时安装了，可以通过直接安装的方式检查一下：
```shell
$ apt search nvidia-dkms
```
应该能够搜到`nvidia-dkms-550`包，与前面搜到的显卡驱动是对应的，然后直接安装
```shell
$ sudo apt install nvidia-dkms-550
```
如果已经安装过了，终端会有信息提示。

#### 3.1.2 通过dkms安装驱动

一般来说，前面安装好驱动之后就能将驱动安装在内核中。
当系统存在多个内核版本时，可能会出现显卡驱动未能安装在内核中，此时可以使用`dkms`将驱动手动安装在使用的内核中：
```shell
$ sudo dkms install -m nvidia -v 550.120
```
之后会输出：
```
Module nvidia/550.120 already installed on kernal 6.8.0-49-generic (x86_64).
```

#### 3.1.3 检查驱动挂载

在查看驱动是否被加载：
```shell
lsmod | grep nvidia
```
无任何返回表示NVIDIA驱动没有被正确加载。
正确挂载驱动的话，终端会输出类似下面的信息
```
nvidia_uvm            nnnnnnn
nvidia_drm             nnnnnn
nvidia_modeset        nnnnnnn
nvidia               nnnnnnnn
......
```



## Reference

尊重版权，标注好相关引用！
[1] [解决NVIDIA-SMI has failed because it couldn‘t communicate with the NVIDIA driver. Make sure that the l](https://blog.csdn.net/very_big_house/article/details/135626122)