# Install Jekyll on Windows

Jekyll 是基于 Ruby 语言开发的网站搭建工具，因此需要首先安装 Ruby 环境。

## 引用

[1] [下载Ruby](https://www.ruby-lang.org/zh_cn/downloads/) 
[2] [Windows 系统上安装 Jekyll（简单详细教程）](https://www.cnblogs.com/pergrand/p/12875597.html)
[3] [保姆级教程：从零构建GitHub Pages静态网站](https://blog.csdn.net/qq_20042935/article/details/133920722)

## 1. 安装 Ruby 环境

1. 在[官网下载](https://www.cnblogs.com/pergrand/p/12875597.html) Ruby 安装器。下载页面会有版本推荐，可按照推荐下载相应的安装工具，例如`Ruby+Devkit 3.3.X (x64)`。
2. 按步骤正常安装软件即可。
3. 验证安装结果。打开终端，输入
   ```shell
   ruby -v
   ```
   正确安装后输出
   ```shell
   ruby 3.3.X ......
   ```

4. 安装 bundler 和 jekyll。打开终端，输入
   ```shell
   gem install bundler jekyll
   ```
   等待安装完所有依赖包。

5. 验证 Jekyll 安装结果，在终端输入
   ```shell
   jekyll -v
   ```
   正确安装后输出
   ```shell
   jekyll X.x.x
   ```

6. 后续需要更新上面安装好的包的话，在终端执行
   ```shell
   gem update --system 3.3.X
   ``` 

## 2. 测试 Jekyll

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

然后进入到新建的页面的目录中：
```shell
cd test_page
```
执行
```shell
bundle exec jekyll serve
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