# 安装 Jekyll

Jekyll 是基于 Ruby 语言开发的网站搭建工具，可以用来构建 Github Pages！

__Content__

- [1. 安装 Ruby 环境](#1)
   - [1.1. Linux 安装 Ruby](#1.1)
   - [1.2. Windows 安装 Ruby](#1.2)
   - [1.3. 安装 bunlder 和 jekyll](#1.3)
- [2. 测试 Jekyll](#2)
- [3. 发布 Github Pages](#3)
- [References](#n)

---

<!-- ------------------------------------------------------------------------- -->
<h2 id="1"> 1. 安装 Ruby 环境 </h2>

使用 Jekyll 前要先安装 Ruby 环境。

<h3 id="1.1"> 1.1. Linux 安装 Ruby </h3>

1、**使用 Ubuntu 存储库安装（不推荐）**

Ubuntu 22.04 存储库包括 Ruby，方便安装，但不是最新版本。
```bash
# 更新 apt 软件包系统：
sudo apt update

# 安装Ruby：
sudo apt install ruby-full

# Ruby安装完成后，检查版本：
ruby -v
```

安装成功后检查版本时应该会输出例如下面的消息：
```
ruby 3.0.2p107 (2021-07-07 revision 0db68f0233) [x86_64-linux-gnu]
```

通过上述方法安装 Ruby，并按照后文进行 jekyll 安装以及新建网页之后，会出现很多（1）bundle版本与已有工程不同导致要 `bundle install`时候可能出现问题；（2）权限问题，例如
```
......
Bundler: Fetching webrick 1.9.1Retrying download gem from https://rubygems.org/ due to error (2/4): Bundler::PermissionError There was an error while trying to write to `/var/lib/gems/3.0.0/cache/rake-13.2.1.gem`. It is likely that you need to grant write permissions for that path.
  Bundler: Retrying download gem from https://rubygems.org/ due to error (3/4): Bundler::PermissionError There was an error while trying to write to `/var/lib/gems/3.0.0/cache/rake-13.2.1.gem`. It is likely that you need to grant write permissions for that path.
......
```
等等，相当的烦。

2、使用 Rbnev 或者 RVM

直接参考后文 [References [2]](#n).

<h3 id="1.2"> 1.2. Windows 安装 Ruby </h3>

1、在[官网下载](https://www.cnblogs.com/pergrand/p/12875597.html) Ruby 安装器。下载页面会有版本推荐，可按照推荐下载相应的安装工具，例如`Ruby+Devkit 3.3.X (x64)`。
2、 按步骤正常安装软件即可。
3、 验证安装结果。打开终端：
```shell
# 查看版本
ruby -v
```
正确安装后输出
```shell
ruby 3.3.X ......
```

<h3 id="1.3"> 1.3. 安装 bunlder 和 jekyll </h3>

安装成功 Ruby 后，可以在终端输入 `gem`，会看到下面的介绍：
```
RubyGems is a package manager for Ruby.

  Usage:
    gem -h/--help
    gem -v/--version
    gem command [arguments...] [options...]
  ......
```

打开终端，执行安装

```bash
# Linux 安装 bundler 和 jekyll，一定要 sudo，不然有 write permission 问题
sudo gem install bundler jekyll

# Windows 安装 bundler 和 jekyll
gem install bundler jekyll

# 上面安装过程稍微有点久
# 等待安装完所有依赖包之后，验证 Jekyll 安装结果
jekyll -v
```
   
正确安装后输出
```shell
jekyll X.x.x
```

后续需要更新上面安装好的包的话，在终端执行
```shell
gem update --system 3.3.X  # 这里的版本号取决于前面安装的版本好
``` 

<!-- ------------------------------------------------------------------------- -->
<h2 id="2"> 2. 测试 Jekyll </h2>

在终端中，使用 jekyll 新建一个页面：
```shell
jekyll new test_page
```
随后终端出现一下log，
```shell
Running bundle install in xxx/test_page...
  Bundler: Fetching gem metadata from https://rubygems.org/...........
  Bundler: Resolving dependencies...
  Bundler: Fetching wdm 0.2.0
  Bundler: Fetching tzinfo 2.0.6
  Bundler: Fetching jekyll-feed 0.17.0
  Bundler: Fetching jekyll-seo-tag 2.8.0
  Bundler: Installing wdm 0.2.0 with native extensions
  Bundler: Installing tzinfo 2.0.6
  Bundler: Fetching tzinfo-data 1.2024.2
  Bundler: Installing jekyll-feed 0.17.0
  Bundler: Installing jekyll-seo-tag 2.8.0
  Bundler: Fetching minima 2.5.2
  Bundler: Installing tzinfo-data 1.2024.2
  Bundler: Installing minima 2.5.2
  Bundler: Bundle complete! 7 Gemfile dependencies, 38 gems now installed.
  Bundler: Use `bundle info [gemname]` to see where a bundled gem is installed.
New jekyll site installed in xxx/test_page.
```

如果网络不好，也没有更改 RubyGems 的源，则可能只会在终端出现下面的一条提示，然后就停滞了
```shell
Running bundle install in xxx/test_page...
```
此时可以更改源，操作如下，
```shell
gem sources --remove https://rubygems.org/  # 删除默认源
gem sources -a https://gems.ruby-china.com/ # 添加新源，或https://ruby.taobao.org/等等
```

然后：
```shell
# 进入到新建的页面的目录中
cd test_page

# 执行
bundle exec jekyll serve

# ---------- 以下是可能出现的问题和解决方法
# 如果出现一对红色错误‘Cound not find .....’，则按照提示安装缺失的库
bundle install
# 有时候是因为已有的 jekyll 工程跟当前使用的 bundler 版本不同导致的
# 此时可以选择执行上一行的指令来更新 bundle。
# 若可以不使用新版本的 bundle，可以尝试更心 Gemfile.lock 文件以使用当前版本的 bundler。
```
结束后出现一下提示
```shell
Run in verbose mode to see all warnings.
                    done in 4.601 seconds.
 Auto-regeneration: enabled for 'xxx/test_page'
    Server address: http://127.0.0.1:4000/
  Server running... press ctrl-c to stop.
```
在浏览器中打开上述地址查看结果，默认网页入下：
<img src=./jekyll_generated_default_page.png/>

上述操作之后生成的默认网页比较简单，可进一步参考“引用-[3]”中的说明，直接下载和编译模板。

<!-- ------------------------------------------------------------------------- -->
<h2 id="3"> 3. 发布 Github Pages </h2>

如果上述生成的网页要发布在 github 中，则需要首先修改一下 `Gemfile`，按照该文件中的提示，删除
```Ruby
gem "jekyll", "~> x.x.x"
```
然后添加
```Ruby
gem "github-pages", group: :jekyll_plugins
```
然后在终端运行下述指令以更新依赖项。
```Bash
bundle update
```
这里如果卡住，可以修改 `Gemfile` 中 source 指向的源后再试。

> 如果上述尝试后还有问题，则要确保下 Bundler 是否已安装，如果您没有安装 Bundler，可以通过以下命令安装：
> ` gem install bundler `
> 确保您使用的是最新版本的 Bundler。可以运行以下命令更新：
> ` gem update bundler `

将上述相关文件上传至 github 之后，Action 会自动编译和部署，之后可以进入`https://{your_git_account}.github.io/{you_repo_name}/`查看网页效果。


<h2 id="n"> References </h2>

注明引用，尊重创作。

[1] [下载Ruby](https://www.ruby-lang.org/zh_cn/downloads/) 
[2] [如何在 Ubuntu 22.04 上安装 Ruby](https://cn.linux-console.net/?p=15044)
[2] [Windows 系统上安装 Jekyll（简单详细教程）](https://www.cnblogs.com/pergrand/p/12875597.html)
[3] [保姆级教程：从零构建GitHub Pages静态网站](https://blog.csdn.net/qq_20042935/article/details/133920722)
