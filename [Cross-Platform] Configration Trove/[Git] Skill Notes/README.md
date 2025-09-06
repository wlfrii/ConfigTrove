# Git Skills

<h2 id="2.1"> 2.1 现有Git仓库添加子模块 </h2>

1、添加子模块
在原始仓库中，使用以下命令完成子模块添加：
```bash
git submodule add <仓库地址> <仓库名称>

# 原始仓库中提交初始化和更新子模块
git submodule init
git submodule update

# 原始仓库中提交提交子模块更改
git commit -m "Add lib_gl_util as a submodule"
```
2、子模块更改后其他模块更新方法

如果直接在子模块进行了更改，完成提交推送后，在添加了该子模块的仓库中：
```bash
cd <仓库路径/子模块文件夹中>
# 拉取最新更改
git pull

# 提交子模块更新
cd <仓库路径>
git add <子模块文件名>
git commit -m"update submodule to latest version"
```
**注意**：在子模块中使用 `git pull`时，只会拉取子模块自身的提交，因为子模块不知道原始仓库中引用的变更。

3、原始仓库修改了子模块的情况

如果在原始仓库中修改了子模块并提交和推送，那么在子模块中直接使用 git pull 并不足以获取原始仓库的更新。因为原始仓库中的修改只是更新了子模块的引用（指向特定提交的指针），而不是直接影响子模块的内容。

TO BE COMPLETED


<h2 id="3.1"> 3.1 将现有Git仓库子目录分离为独立仓库并保留历史记录 </h2>

1、克隆原始仓库并提取
```bash
# Clone原始仓库
git clone <原始仓库地址> 
cd <原始仓库目录>

# 提取文件夹并保存历史记录
# 使用 git filter-repo 提取指定文件夹的历史记录。假设你要提取的文件夹名为 my_folder：
git filter-repo --subdirectory-filter my_folder

# 如果你没有安装 git filter-repo，
# (1) 可以使用 git filter-branch：
# git filter-branch --subdirectory-filter my_folder -- --all
# (2) 可以通过 pip3 安装：
# pip3 install git-filter-repo
```

在提取 my_folder 后，其他内容已经被移除。你可以确认一下当前目录只包含 my_folder 的历史记录。

2、创建新的仓库
现在，创建一个新的 Git 仓库：
```bash
git remote remove origin
git remote add origin <新仓库地址>
git push -u origin master
```

3、删除原始仓库中的相应文件夹
```bash
git rm -r my_folder

# 删除后提交更改
git commit -m "remove my_folder"
```