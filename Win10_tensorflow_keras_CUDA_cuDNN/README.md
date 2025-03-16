#! https://zhuanlan.zhihu.com/p/424991762
# 【Win10 - Python Keras】with CUDA and cuDNN

本来是想使用 **keras**，参考了一堆博客之后，发现到处都是坑......
![](./img/keng.jpg)


其实配置 **keras** 已经变得非常简单，如官网所说，只需要配置好 **tensorflow** 就好了。

![](./img/keras_installation.png)

使用 **keras** 的时候只需要从 **tensorflow** 导入就行。
```python
from tensorflow import keras
```

踩了一堆坑之后，为了避免下次配置时候在踩坑，把这次的经验整理下来~

对应好 Python, tensorflow, CUDA, cuDNN 版本是关键！！！
--- 

---

# Do it

首先查看自己电脑 **CUDA** 的驱动版本，在电脑桌面右键 "__NVIDIA 控制面板__"

![](./img/right_button_nvidia.jpg)

![](./img/nvidia_control_panal.png)

比如我当前的电脑，驱动版本为 **11.2**。这个 **CUDA** 驱动版本对应着 **CUDA runtime** 版本的限制不大于该版本，也就是 **CUDA toolkit** 版本需要小于 **11.2**。**CUDA toolkit** 官网下载地址：[CUDA Toolkit Downloads | NVIDIA Developer](https://developer.nvidia.com/cuda-toolkit-archive)。

然后需要对照这个 **CUDA toolkit** 版本下载相应版本的 **cuDNN**。版本对照如下图。图片源地址为：[https://www.tensorflow.org/install/source#gpu](https://www.tensorflow.org/install/source#gpu)

![](./img/tensorflow_python_cudnn_cuda_version.jpg)

**cuDNN** 的官网下载地址：[cuDNN Archive | NVIDIA Developer](https://developer.nvidia.com/rdp/cudnn-archive)。

下载上述响应的 **CUDA** 和 **cuDNN** 之后，在安装对应版本的 **Python**，然后使用 `pip` 安装相应版本的 **tensorflow**。

我是在 Anaconda 环境中进行操作的。我当前的 **CUDA toolkit** 版本是 **11.0**， 所以安装 **Python-3.8 + tensorflow-2.4.0**。
1. 创建新环境
```shell
conda create -n tensorflow2 python=3.8 
conda activate tensorflow2
```
2. 安装 **tensorflow**。
```shell
 pip install --upgrade tensorflow=2.4.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
```
3. 测试安装结果。
```shell
 python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```
如下为测试成功的结果。最后会返回 tf.Tensor()就说明安装成功了。

![tensorflow测试](./img/test_tensorflow.jpg)

## References

[使用 pip 安装 TensorFlow](https://www.tensorflow.org/install/pip#virtual-environment-install)

[GPU 支持  |  TensorFlow](https://www.tensorflow.org/install/gpu)

[Getting started (keras.io)](https://keras.io/getting_started/#installing-keras)