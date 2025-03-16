

双系统情况可能会出现启动 Ubuntu 系统时的卡死问题，解决方法如下：

1. 强制重启电脑，然后在引导选择页面选择`Advanced options for Ubuntu`；
2. 选择后面带有`(recovery mode)`的内核，敲回车；
3. 之后会弹出`Recovery Menu`，选择`root Drop to root shell prompt`，随后界面下方会弹出一个小终端；
4. 在终端中敲回车，进入`root`，然后输入下述指令来修改grub文件。
    ```
    $ sudo vi /etc/default/grub
    ```
5. 修改引导程序内容，在
   ```
   GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
   ```
   中添加`nomodeset`，修改后的结果为`GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"`
   vi的使用提示：按`i`键进入编辑模式，通过键盘的上下左右可以移动光标；按`Esc`退出编辑模式；在按下`Esc`后，输入`:wq`可保存并退出。
6. 更新引导程序内容：
   ```
   $ sudo update-grub
   ```
7. 重启：
   ```
   $ reboot
   ```

之后应该就能成功进入系统了。、
