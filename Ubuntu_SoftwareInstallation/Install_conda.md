# Install conda on Ubuntu

## 1. 下载

下述 Miniconda 和 Anaconda 是同一家的产品，二者主要区别：
<table>
<tr> <th>\</th> <th>Anaconda</th> <th>Miniconda</th> </tr>
<tr> <td>安装包的大小</td> <td>默认安装时包含了大量的科学计算和数据科学相关的包（如 NumPy, Pandas, Matplotlib 等），安装包通常超过 3 GB。</td> <td>是一个轻量级的安装器，仅包含 Conda 及其基本依赖。初始安装包只有几 MB，用户可以根据需要安装额外的包。</td> </tr>
<tr> <td>预装包</td> <td>提供了数百个常用的科学计算和数据分析包，适合新手或希望快速开始数据科学项目的用户。</td> <td>安装后是一个干净的环境，用户需要手动安装所需的包，适合有特定需求的用户或开发者。</td> </tr>
<tr> <td>灵活性</td> <td>灵活性较差，由于预装了很多包，用户可能会安装一些不需要的工具，增加了系统负担。</td> <td>更灵活，用户可以根据自己的项目需求，选择安装所需的包，保持环境精简</td> </tr>
<tr> <td>选择建议</td> <td>适合初学者、数据科学家和需要快速启动项目的用户。
可以立即使用多个常用的库，适合教育和实验环境</td> <td>适合有经验的开发者、希望精简环境的用户，或者需要自定义环境的用户。适合需要安装特定版本或特定包的项目。</td> </tr>
<table>

按需选择一个进行安装。

### 下载 Miniconda
在终端中运行以下命令下载 Miniconda：
```shell
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

安装 Miniconda:
```shell
$ bash Miniconda3-latest-Linux-x86_64.sh
```

按照提示进行操作，选择安装路径等。安装完成后，关闭终端并重新打开，或运行以下命令以使更改生效：
```shell
$ source ~/.bashrc
```

### 下载 Anaconda:

打开终端并运行以下命令下载 Anaconda 的最新安装脚本：
```shell
$ wget https://repo.anaconda.com/archive/Anaconda3-latest-Linux-x86_64.sh
```

安装 Anaconda：
```shell
$ bash Anaconda3-latest-Linux-x86_64.sh
```

按照提示进行安装。在安装过程中，你会看到以下几条提示：
1. 阅读许可协议: 按 Enter 键查看许可协议，最后输入 yes 同意协议。
2. 选择安装路径: 你可以选择默认路径（通常是 ~/anaconda3），或者输入自定义路径。
3. 初始化 Conda: 安装结束时，会询问是否将 Conda 添加到你的 PATH 中。建议选择 yes。
4. 激活安装

安装完成后，关闭终端并重新打开，或者在终端中运行以下命令以激活 Conda：
```shell
$ source ~/anaconda3/bin/activate
```

### 网页手动下载：

如果前述两种方式无法下载，则通过浏览器直接访问：
```html
https://repo.anaconda.com/archive/
```
进行最新版的下载。下载后的安装方法同上。

## 2. 激活安装

安装完成后，“关闭终端并重新打开”或者“在终端中运行以下命令以激活 Conda”：
```shell
surce source ~/anaconda3/bin/activate
```
之后终端的名称前会多一个`(base)`表示当前激活的conda环境。

## 3. 验证安装

检查 Anaconda 是否安装成功：
```shel
$ conda --version
```
安装成功会返回版本号：
```
conda xx.x.x
```

## 4. 更新 Conda

建议在第一次使用前更新 Conda：
```shell
$ conda update conda
```

## 5. 可选配置

### 5.1 设置自动补全

#### 方法1：添加配置（不推荐）

打开`~/.bashrc`，添加以下代码：
```bash
# Enable conda command auto-completion
__conda_auto_complete() {
    COMPREPLY=( $(COMP_WORDS="${COMP_WORDS[@]}" COMP_CWORD=$COMP_CWORD command conda "$@") )
    return 0
}
complete -o nospace -F __conda_auto_complete conda
```
保存后，重新加载配置文件：
```shell
$ source ~/.bashrc
```

验证：新建一个终端，输入指令之后按`Tab`键可以自动补全。
测试下来发现这个方法的补全功能太傻了，例如输入`conda acti`后按下`Tab`，出现的结果如下：
```shell
conda actiusage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...
conda: error: argument COMMAND: invalid choice: 'conda' (choose from 'activate', 'clean', 'commands', 'compare', 'config', 'create', ....)
```
并不是想要的自动补全。

#### 方法2：使用官方插件（推荐）

安装插件：
```shell
$ conda install -c conda-forge conda-bash-completion
```
然后在`~/.bashrc`文件最后添加以下指令以启用`conda-bash-completion`：
```bash
# Enable conda bash completion
if [ -f "$(conda info --base)/etc/profile.d/conda.sh" ]; then
    . "$(conda info --base)/etc/profile.d/conda.sh"
fi
```
保存后，重新加载配置文件：
```shell
$ source ~/.bashrc
```
验证：新建一个终端，输入指令之后按`Tab`键可以自动补全。
例如输入`conda acti`后按下`Tab`，出现的结果为：`conda activate`。
