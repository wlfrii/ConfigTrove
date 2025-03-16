# SSH Configuration

## ●Issue：在windows上通过scp拷贝Ubuntu文件得到“connection refused”

### 1. 确认 SSH 服务正在运行

确保 Ubuntu 主机上已经安装并启动了 SSH 服务（通常是 OpenSSH）。可以通过以下命令检查 SSH 服务状态：
```shell
$ sudo systemctl status ssh
```

如果没有运行，可以使用以下命令启动：
```shell
$ sudo systemctl start ssh
```

如果还没有安装 SSH，可以通过以下命令安装 ssh-server：
```shell
$ sudo apt update
$ sudo apt install openssh-server
```

然后再次测试`scp`应该就OK了。

如果还有问题，再按照下面的方法试一下。

### 2. 检查防火墙设置
确认 Ubuntu 主机上的防火墙没有阻止 SSH 连接。可以使用以下命令检查 UFW（Uncomplicated Firewall）状态：
```shell
$ sudo ufw status
```

如果 SSH 被阻止，可以使用以下命令允许 SSH 连接：
```shell
sudo ufw allow ssh
```

### 3. 确认 SSH 端口
默认情况下，SSH 使用 22 端口。确认 Ubuntu 主机的 SSH 配置文件（/etc/ssh/sshd_config）中的端口设置没有被更改。如果更改了端口，请使用该端口进行连接：
```shell
$ scp -P [port_number] user@ubuntu_host:/path/to/file C:\path\to\destination
```

### 4. 确认 IP 地址和用户名
确保你在 scp 命令中使用了正确的 Ubuntu 主机的 IP 地址和用户名。可以通过以下命令获取 Ubuntu 主机的 IP 地址：
```shell
$ hostname -I
```

### 5. 使用 Windows 终端
确保你在 Windows 上使用的终端（如 CMD、PowerShell、Git Bash 等）支持 scp 命令。一般来说，Git Bash 或 Windows 10 及以上的 PowerShell 支持此命令。

### 6. 测试 SSH 连接
在尝试 scp 之前，先测试 SSH 连接。使用以下命令从 Windows 连接到 Ubuntu：
```shell
$ ssh user@ubuntu_host
```
如果能够成功连接，说明 SSH 服务正常；如果仍然收到 "connection refused" 错误，需检查 SSH 配置和防火墙设置。

### 7. 检查 SELinux 或 AppArmor 设置
如果你的 Ubuntu 系统启用了 SELinux 或 AppArmor，确保它们没有阻止 SSH 服务的运行。可以暂时禁用 SELinux 或调整 AppArmor 配置进行测试。

### 8. 重启 SSH 服务
如果进行了任何更改，尝试重启 SSH 服务：
```shell
sudo systemctl restart ssh
```


