# Configure PyTorch in Conda

在 Ubuntu 上使用 Conda 创建一个能够同时支持 CPU 和 GPU 版的 PyTorch 环境的详细教程如下：

### 1. 安装 Anaconda

如果尚未安装 Anaconda，请参考之前的回答完成安装。

### 2. 创建新的 Conda 环境并激活

打开终端并输入以下命令以创建一个新的 Conda 环境（命名为 env_pytorch，Python 版本为 3.9）：
```shell
$ conda create -n env_pytorch python=3.9
```

激活新创建的环境：
```shell
$ conda activate env_pytorch
```

### 3. 安装 PyTorch

根据你的硬件和需求选择适合的安装命令。

#### 3.1. 只安装 CPU 版本的 PyTorch

如果只需要 CPU 版本，运行以下命令：
```
$ conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

#### 3.2. 安装 GPU 版本的 PyTorch

如果你的机器有 NVIDIA GPU，并且已安装了适当的 CUDA 驱动程序，可以安装 GPU 版本。根据你的 CUDA 版本选择相应的命令。
查看 CUDA 版本：
```shell
$ nvidia-smi
```
查看“CUDA Version”，以我这里的 CUDA 12.4 为例，安装 PyTorch：
```shell
$ conda install pytorch torchvision torchaudio cudatoolkit=12.4 -c pytorch
```
对于其他 CUDA 版本，需要将上面的版本号修改以下。

执行上述指令后，收到下面的报错：
```
......
Solving enviroment: failed

PackagesNotFoundError: The following packages are not available from current channels:

 - cudatoolkit=12.4*

Current channels:
 - https://conda.anaconda.org/pytorch
 - https://repo.anaconda.com/pkgs/main
 - https://repo.anaconda.com/pkgs.r

......
```
这主要是因为当前 Conda 通道中没有你指定版本的 cudatoolkit。PyTorch 的 Conda 包通常不支持最新版本的 CUDA。解决方法如下：

##### 方法1：安装低版本 CUDA

CUDA是能够向前兼容的，因此可以继续通过 conda 安装低版本的 CUDA 版本，这样会比较方便省事。

搜索目前支持的CUDA版本：
```shell
$ conda search cudatoolkit
```

例如当前查到的能够支持的最新的版本为：`cudatoolkit=11.8`，则可以将 CUDA 版本降为 11.8，再进行安装。

##### 方法2：从 PyTorch 官方安装命令获取 (推荐方式)

1. 访问 [PyTorch 官方网站](https://pytorch.org/get-started/locally/)。
2. 选择适当的配置: 在页面上选择你的操作系统、包管理器（Conda）、语言（Python）和 CUDA 版本。官网会生成具体的安装命令。
   界面如下：
   <img src="./__md__/conda_configure_pytorch.png" scale="70%">


### 4. 验证安装

安装完成后，可以通过以下 Python 代码检查 PyTorch 是否正确安装：

```shell
$ python # 进入python运行环境"
```

参考下述代码进行验证：
```python
>>> import torch
>>> print(torch.__version__) # 以我这里为例，输出2.5.1
>>> print("CUDA available:", torch.cuda.is_available()) # 输出 CUDA available: True 表示 GPU 支持已启用
>>> print("CUDA version:", torch.version.cuda)  # 打印 CUDA 的版本号，输出12.4
>>> print("cuDNN available", torch.backends.cudnn.enabled) # 输出 cuDNN available: True 表示已启用
>>> print("cuDNN version:", torch.backends.cudnn.version())  # 打印 cuDNN 的版本号，输出901.00

# 测试加法
>>> x = torch.rand(2, 3)
>>> y = torch.rand(2, 3)
>>> z = x+y
>>> print(z)
# 输出
tensor([[value1, value2, value3],
        [value4, value5, value6]])
```

