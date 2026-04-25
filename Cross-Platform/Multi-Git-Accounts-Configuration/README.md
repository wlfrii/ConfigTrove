# Multi-Git Accounts Configuration

在同一台主机上配置多个不同 Git 账户，以方便项目管理。 Windows, Linux, Mac OS 环境下的配置方式相同，这里以 Linux 为例。

__Content__

- [1. 准备工作](#1)
- [2. 帐号配置](#2)
    - [2.1 生成 SSH 密钥](#2.1)
    - [2.2. 添加 SSH 密钥到 SSH Agent](#2.2)
    - [2.3. 配置 SSH 配置文件](#2.3)
    - [2.4. 使用不同的 Git 账户](#2.4)
    - [2.5. 配置 Git 用户信息](#2.5)

---
<!-- ======================================================================= -->
<h2 id="1"> 1. 准备工作 </h2>

1、首先确保安装好了 `git` 工具：
```shell
sudo apt install git
```

2、提前配置好 `ssh` ，可参考 [[SSH] Configuration](https://github.com/wlfrii/ConfigTrove/tree/main/Cross-Platform/SSH-Configuration)。

---
<!-- ======================================================================= -->

<h2 id="2"> 2. 帐号配置 </h2>

<h3 id="2.1"> 2.1 生成 SSH 密钥 </h3>

为每个 Git 账户生成一个 SSH 密钥。
```bash
# 为第一个账户生成密钥
ssh-keygen -t rsa -b 4096 -C "your_email_1@example.com"
# 在提示时，输入不同的文件名以区分
# 例如：/home/your_user/.ssh/id_rsa_account1

# 为第二个账户生成密钥
ssh-keygen -t rsa -b 4096 -C "your_email_2@example.com"
# 例如：/home/your_user/.ssh/id_rsa_account2
```

<h3 id="2.2"> 2.2. 添加 SSH 密钥到 SSH Agent </h3>

确保 SSH agent 正在运行，并将密钥添加到 agent。
```bash
# 启动 SSH agent
eval "$(ssh-agent -s)"

# 添加第一个密钥
ssh-add ~/.ssh/id_rsa_account1

# 添加第二个密钥
ssh-add ~/.ssh/id_rsa_account2
```

<h3 id="2.3"> 2.3. 配置 SSH 配置文件 </h3>

编辑或创建 ~/.ssh/config 文件，配置不同账户的 SSH 密钥。
```bash
nano ~/.ssh/config
```

添加以下内容：
```plaintext
# 第一个账户
Host github-account1                        // 起个名字
    HostName github.com                     // 这个是远程地址，不用改
    User git                                // 修改为你的用户名
    IdentityFile ~/.ssh/id_rsa_account1     // 修改为用户名对应的密钥

# 第二个账户
Host github-account2
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_account2
```

<h3 id="2.4"> 2.4. 使用不同的 Git 账户 </h3>

1、确保 SSH 密钥在 github 上

确保公钥 (id_rsa_account.pub) 已添加到你的 GitHub 账户中：
1. 登录到 GitHub。
2. 进入 Settings > SSH and GPG keys。
3. 点击 New SSH key，然后将你的公钥(id_rsa_account.pub) 粘贴到文本框中。

2、测试 SSH 连接
```bash
ssh -T git@github.com
# Or
ssh -T git@github-account1.com
```
如果配置正确，你应该看到类似以下的消息：
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

3、在克隆或推送时，使用配置的主机名。
```bash
# 第一个账户
git clone git@github-account1:username/repo.git

# 第二个账户
git clone git@github-account2:username/repo.git
```

<h3 id="2.5"> 2.5. 配置 Git 用户信息 </h3>

在每个仓库中配置用户名和邮箱。
```bash
# 进入第一个账户的仓库
cd path/to/repo1
git config user.name "Your Name 1"
git config user.email "your_email_1@example.com"

# 进入第二个账户的仓库
cd path/to/repo2
git config user.name "Your Name 2"
git config user.email "your_email_2@example.com"
```

之后，可在每个仓库中使用不同账户进行管理。

如果配置用户名和邮箱时，不小心加上了`--global`参数，可以先取消设置，再重新配置。
```bash
# 例如取消设置邮箱
git config --global --unset user.email

# 配置完成后，可以查看当前仓库的配置结果
git config --list
```

---
<!-- ======================================================================= -->

<h2 id=3> 3. Git 使用方法 </h2>

可参考[Git Skill Notes](https://github.com/wlfrii/ConfigTrove/blob/main/Cross-Platform/Git-Skill-Notes/README.md)。