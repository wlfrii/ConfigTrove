# SSH Configuration

Linux 系统默认带 SSH 客户端（ssh, scp, sftp等命令），但不一定默认启用。Win10 之后的新系统默认安装了 OpenSSH Client 但未安装 OpenSSH server.

__Content__

- [1. Ubuntu/Debian环境](#1)
    - [1.1 快速验证](#1.1)
- [2. Windows 环境](#2)
    - [2.1 快速验证](#2.1)
    - [2.2 安装和启用SSH server](#2.2)
- [3. 测试 SSH 连接](#3)

---

<h2 id=1> 1. Ubuntu/Debian环境 </h2>

Ubuntu/Debian 系统默认带 SSH 客户端（ssh, scp, sftp等命令）。

<h3 id=1.1> 1.1 快速验证 </h3>

1 检查 SSH client：
```bash
ssh -V
which ssh
```
输出版本、显示路径（如 /usr/bin/ssh）= 正常可用。

2 检查 SSH server

```bash
# 查看服务状态
systemctl status ssh
# 查看是否安装包
dpkg -l | grep openssh-server
```

提示“未找到服务 或 未安装”= 没装服务端。

若安装了 ssh-server 但未启用服务，可以使用以下命令启动：
```bash
sudo systemctl start ssh
```

如果还没有安装 SSH，可以通过以下命令安装 ssh-server：
```shell
sudo apt update
sudo apt install openssh-server
```

然后再次测试`ssh/scp`应该就OK了。

<h2 id=2> 2. Windows 环境 </h2>

确保你在 Windows 上使用的终端（如 CMD、PowerShell、Git Bash 等）支持 scp 命令。一般来说，Git Bash 或 Windows 10 及以上的 PowerShell 支持此命令。

<h3 id=2.1> 2.1 快速验证 </h3>

1 检查 SSH client:
```powershell
ssh -V
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH.Client*'
```
显示版本、状态为 Installed = 正常。

2 检查服务段（默认未安装）：
```powershell
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH.Server*'
```
显示 NotPresent = 未安装。

<h3 id=2.2> 2.2 安装和启用SSH server </h3>

安装方法1：进入“系统设置-系统-可选功能”，点击查看功能，搜索`OpenSSH`，然后添加。

安装方法2：
```powershell
# 安装 OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

设置开机启动ssh服务：
```powershell
# 启动并设开机自启
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic
# 放行防火墙 22 端口
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH-Server' -Direction Inbound -Protocol TCP -LocalPort 22 -Action Allow
```

<h2 id=3> 3. 测试 SSH 连接 </h3>

在尝试 scp 之前，先测试 SSH 连接。使用以下命令从 Windows/Ubuntu 连接到 Ubuntu/Windows：
```shell
 ssh user@ubuntu_host_ip
```
如果能够成功连接，说明 SSH 服务正常；如果仍然收到 "connection refused" 错误，需检查 SSH 配置和防火墙设置。
