# Git Skill Notes

Git常用指令笔记。

__Content__

- [1. 基本指令](#1)
    - [1.1 创建 / 克隆仓库](#1.1)
    - [1.2 查看状态](#1.2)
    - [1.3 添加 / 提交代码](#1.3)
    - [1.4 同步远程仓库](#1.4)
    - [1.5 分支操作](#1.5)
    - [1.6 撤销 / 回退](#1.6)
- [2. 子模块](#2)
    - [2.1 添加子模块](#2.1)
    - [2.2 拉取子模块](#2.2)
    - [2.2 更新子模块](#2.3)
    - [2.4 删除子模块](#2.4)
- [3 Git仓库拆解为多个独立仓库并保留提交记录](#3)
    - [3.1 克隆原始仓库并提取子目录](#3.1)
    - [3.2 为子目录绑定新仓库](#3.2)
    - [3.3 删除原始仓库中的子目录](#3.3)
- [Appendix](#10)
    - [A.1 git变基的作用](#10.1)

---
<!-- ======================================================================= -->

<h2 id=1> 1. 基本指令 </h2>

<h3 id=1.1> 1.1 创建 / 克隆仓库 </h3>

```bash
# 1. 把当前文件夹变成 Git 仓库（新项目用）
git init

# 2. 克隆远程仓库（从 GitHub/GitLab 拉代码）
git clone 仓库地址
```

<h3 id=1.2> 1.2 查看状态 </h3>

```bash
# 查看文件修改状态（最常用）
git status

# 查看提交历史
git log
```

<h3 id=1.3> 1.3 添加 / 提交代码 </h3>

```bash
# 1.1 添加单个文件
git add 文件名

# 1.2 添加文件夹xxx下的所有文件
git add 文件夹路径

# 1.3 添加所有修改
git add .

# 1.4 添加当前目录所有已追踪的文件（最常用）
git add ./ -u

# 2. 提交到本地仓库
git commit -m "这里写本次修改说明"
```

<h3 id=1.4> 1.4 同步远程仓库 </h3>

```bash
# 推送到远程（上传代码）
git push

# 拉取远程最新代码（下载代码）
git pull
```

当希望将当前本质分支推送到远程不同分支时：
```bash
# 例如希望推送到远程的 main 分支
git push origin main # 或 git push origin HEAD:main
# origin = 远程仓库
# HEAD   = 当前所在的本地分支（自动识别）
# main   = 要推送到的远程目标分支
```

当希望拉取远程指定分支最新代码，并用“变基”方式合并时：
```bash
# 例如希望拉取远程 main 分支
git pull -r origin main
# -r = rebase，变基，让提交历史变成一条直线，更干净，无多余提交
# origin main = 指定拉取远程的 main 分支
```

有关 `git pull` 和 `git pull -r` 的区别，见 [A.1 git变基的作用](#10.1)。

<h3 id=1.5> 1.5 分支操作 </h3>

```bash
# 查看所有分支
git branch

# 创建新分支
git branch 分支名

# 切换分支
git checkout 分支名
# 或新版命令
git switch 分支名

# 创建并直接切换到新分支
git checkout -b 分支名

# 合并分支（比如把 dev 合并到 main）
git merge 分支名
```

<h3 id=1.6> 1.6 撤销 / 回退 </h3>

```bash
# 撤销文件修改（回到上次提交状态）
git checkout -- 文件名

# 撤销 add
git reset HEAD 文件名

# 回退到某个版本
git reset --hard 提交ID
```

---
<!-- ======================================================================= -->

<h2 id=2> 2. 子模块 </h2>

<h3 id=2.1> 2.1 添加子模块 </h3>

1、在原始仓库中，使用以下命令完成子模块添加：
```bash
git submodule add <子仓库地址> <存放路径/名称>

# 例如把 https://github.com/xxx/lib.git 放到项目里的 libs/my-lib 目录
# git submodule add https://github.com/xxx/lib.git libs/my-lib
```

2、添加子模块后必须提交
```bash
git add .gitmodules
git add 子模块目录
git commit -m "add submodule xxx"
```
**不提交的话，其他人拉代码时看不到子模块！**

<h3 id=2.2> 2.2 拉取子模块 </h3>

其他人克隆仓库时，普通克隆不会自动下载子模块：
```bash
git clone https://xxx/your-project.git
```

要自动获取子模块，必须执行
```bash
git submodule init
git submodule update

# 或者一步到位，clone时指定拉取子模块
git clone --recurse-submodules https://xxx/your-project.git
```

<h3 id=2.3> 2.3 更新子模块 </h3>

**情况1**：子模块更改后其他模块更新方法

如果直接在子模块进行了更改，完成提交推送后，在添加了该子模块的其他主仓库中按照下边方法更新子模块的绑定：
```bash
cd <主仓库路径/子模块文件夹中>
# 拉取最新更改
git pull

# 提交子模块更新
cd <主仓库路径>
git add <子模块文件名>
git commit -m"update submodule to latest version"
```
**注意**：在子模块中使用 `git pull`时，只会拉取子模块自身的提交，因为子模块不知道原始仓库中引用的变更。

另一种较极端的方法是在主仓库中直接更新所有的子模块：
```bash
git submodule update --remote
```

<h3 id=2.4> 2.4 删除子模块 </h3>

需要按照取消初始化、删除、提交删除的顺序执行：
```bash
# 1. 反注册
git submodule deinit 子模块目录

# 2. 删除文件夹
git rm 子模块目录

# 3. 提交
git commit -m "remove submodule"
```

---
<!-- ======================================================================= -->

<h2 id=3> 3 Git仓库拆解为多个独立仓库并保留提交记录 </h2>

<h3 id=3.1> 3.1 克隆原始仓库并提取子目录 </h3>

```bash
# 1. clone原始仓库
git clone <原始仓库地址>
cd <原始仓库目录>

# 2. 提取文件夹并保存历史记录
# 使用 git filter-repo 提取指定文件夹的历史记录。假设你要提取的文件夹名为 my_folder：
git filter-repo --subdirectory-filter my_folder

# 如果你没有安装 git filter-repo，
# (1) 可以使用 git filter-branch：
# git filter-branch --subdirectory-filter my_folder -- --all
# (2) 可以通过 pip3 安装：
# pip3 install git-filter-repo
```

在提取 `my_folder` 后，其他内容已经被移除。你可以确认一下当前目录只包含 `my_folder` 的历史记录。

<h3 id=3.2> 3.2 为子目录绑定新仓库 </h3>

现在，将 `my_follder` 创建cheng一个新的 Git 仓库：

```bash
# 1. 移除 my_folder 文件夹中存在的原始仓库信息
git remote remove origin

# 2. 为 my_folder 添加一个新的远端仓库地址
git remote add origin <新仓库地址>

# 3. 将本地同步至远端
git push -u origin master
```

<h3 id=3.3> 3.3 删除原始仓库中的子目录 </h3>

在将 `my_folder` 独立为单独仓库后，可以在原始仓库中删除 `my_folder` 文件夹。

```bash
git rm -r my_folder

# 删除后提交更改
git commit -m "remove my_folder"
```

<h2 id=10> Appendix </h2>

<h3 id=10.1> A.1 git变基的作用 </h3>

前置基础
```bash
git pull    = git fetch + git merge
git pull -r = git fetch + git rebase
```

假设存在一个场景：
- 远程 main 有 2 次提交：A → B
- 本地 main 基于 A，自己做了 2 次提交：A → C → D

此时本地和远程分叉了

**例子 1**：普通 git pull（默认 merge 方式）
```bash
git pull origin main
```
执行后，拉取远程 B 提交，然后会自动创建一条 Merge 合并提交，进而导致分支历史变成分叉 + 打结。
提交历史长成这样
```plaintext
      C --- D
     /       \
A --- B ------ M  (M是自动生成的Merge提交)
```
多了一条没用的合并记录 M。随着提交记录增加，提交历史会产生大量冗余 Merge 提交，版本历史不线性，查问题、回滚都麻烦。

**例子 2**：git pull -r（rebase 变基方式）
```bash
git pull -r origin main
```
执行后，先拉取远程最新 B，其次把本地的 C、D 先临时摘下来，然后以远程最新 B 为基底，把你的 C、D 按顺序重新接在后面，使得提交历史变成一条直线。提交历史长成这样
```plaintext
A --- B --- C --- D
```
历史中没有任何多余 Merge 提交，干净、线性、一目了然；回滚、查日志、代码评审都比较方面。

