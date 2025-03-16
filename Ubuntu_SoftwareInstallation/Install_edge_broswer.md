
# Install Edge Browser on Ubuntu

1. 进入官网: [Microsoft Edge](https://www/microsoft.com/en-us/edge)，点击“Download Edge”，然后在弹出的声明中点击“Accept and download”，之后会开始下载文件`microsotft-edge-stable_xxx.x.xxxx_amd64.deb`。其中`xxx`表示版本号。
2. `Ctrl+Alt+t`打开终端，`ls`查看下载的`deb`文件，下载好了之后应该是能看到文件的。
3. 运行安装
   ```shell
   $ sudo apt install ./microsotft-edge-stable_xxx.x.xxxx_amd64.deb
   ```
   这时，`apt`工具也会找`apt`下的包`microsoft-edge-stable`，如果这个包比较新，会提示安装该报，部分提示内容如下：
   ```
   The following NEW packages will be installed:
     microsoft-edge-stable
   ......
   ```

