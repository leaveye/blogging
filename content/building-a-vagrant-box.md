Title: 从头到尾做 Vagrant Box
Date: 2016-12-19 14:21
Tags: vagrant, virtualization, server
Category: Server
Slug: building-a-vagrant-box
Author: Levi G

译自：[https://blog.engineyard.com/2014/building-a-vagrant-box](https://blog.engineyard.com/2014/building-a-vagrant-box)  
![Original LOGO](https://blog.engineyard.com/images/blog-images/vagrant-box.png)

> **注：**本文原发布于 tylerbird.org 今年的 blog 。最近在 Engine Yard 发布大众更新版本。

[TOC]

Vagrant 的目标是简化在本地创建开发环境，接触上之后，你再也不会想用其它方式了。只用两个简单的命令，你就可以安装你的第一个 vagrant 环境；再使用第三个命令，就可以连接到你的第一个 vagrant box 了，这些总共也用不了几分钟。

	vagrant init precise32 http://files.vagrantup.com/precise32.box
	vagrant up
	vagrant ssh # 你连进来了！

这工具效率高的惊人，而且对那些在许多不同项目中工作的自由职业者，或是需要让队伍新成员尽快上手的公司来说，太有用了。使用 Vagrant ，开发环境与生成环境的配置可以极快地转化。那些“在我机器上好好的”的错误可以成为历史了。

如果你已经是个 Vagrant 的粉了，我可能是在班门弄斧。要了解 Vagrant 还可以做什么，可以看它的精美文档，或是和我一样，找本 Vagrant 的作者 Mitchell Hashimoto 编写，O'Reilly 出版的书 [Vagrant: Up and Running](http://shop.oreilly.com/product/0636920026358.do) 来读。它打包了你要了解 Vagrant 需要的细节，内外兼顾且短小精悍。

## 为什么制作 Box

在类似 [vagrentbox.es](http://www.vagrantbox.es/) 和 [vagrantcloud.com](https://vagrantcloud.com/) 的网站上，已经有了很多很好的可用 box ，那为什么你要做自己的 box 呢？

也许你要在你的基础（一两个运行时，比如 Julia 、Erlang 、JVM 或 Python 等等）上加一点点额外东西，然后作为你的新“基础”。

也许你想让你的 box 有更多的内存，或者想让它更接近于你的生产镜像以及你在搭建个有多种 provisioner 的更多内存的服务器集群，好吧……要爬座大山，你需要装备。

## 定义

package.box 文件是什么？使用 VirtualBox 做 provider 时，它是个包含下列内容的，tar 过的 gzip 文件：

	Vagrantfile
	box-disk.vmdk
	box.ovf
	metadata.json

* `Vagrantfile` 包含的信息会在你某个目录里运行 `vagrant init boxname` 时，合并到你的 Vagrantfile 中。
* `box-disk.vmdk` 是虚拟磁盘文件。
* `box.ovf` 定义了这个 box 的虚拟硬件。
* `metadata.json` 告诉 vagrant ，这个 box 在什么 provider 下工作。

注意：这些内容在其它 provider（如 VMWare ）下是不同的。参考 vagrant 关于 [box 的文档](http://docs.vagrantup.com/v2/vmware/boxes.html)查找更多信息。

## 大叫一声

我是个 Vagrant 粉，也喜欢自动化所有的事，它们让我的生活轻松很多。首先要表明我主要取材于：

* Ryan Skoblenick 的博文 [Creating a Custom Box from Scratch](http://www.skoblenick.com/vagrant/creating-a-custom-box-from-scratch/) 。
* 以及 Mitchell Hashimoto 的这本书[《Vagrant: Up and Running》](http://shop.oreilly.com/product/0636920026358.do)。

既然 Ryan 的已经存在了，我为什么还要写这篇博文？好问题。

距离目的地，它只带了我 90% 的路程。参考他的文章安装 Guest Tools 和为操作系统配置 SSH 用户的时候，我还是有些问题。

所以我希望这篇文章，能够为需要自制 box 的朋友推进这个进度、增加理智的声音。

## 准备工作

如果你还没有 Vagrant 和 VirtualBox ，装一份。

* [下载](http://www.vagrantup.com/downloads.html)适用于你操作系统的 Vagrant 安装器。
* [下载](https://www.virtualbox.org/wiki/Downloads)适用于你操作系统的 VirtualBox 安装器。

注意：也要下载 VirtualBox Extenstion Pack 。关于它的更多功能可以[看这里](https://www.virtualbox.org/manual/ch01.html#intro-installing)。

> 在有安装包之前，Vagrant 是通过 RubyGem 发布的。现在，使用安装包是安装 Vagrant 的推荐方法，所以你应该卸载 RubyGem 版本，并遵循适用与你的平台的步骤说明。基于 RubyGem 安装的版本支持到 Vagrant 1.0.x ，后续将不再提供支持。
> —— 《Vagrant: Up and Running》, O'Relly, Mitchell Hashimoto, 第8页，978-1-449-33583-0

RUBY 用户：如果你已有 rubygem 安装的 Vagrant ，安装前先卸载它：

	gem uninstall vagrant

运行 Vagrant 安装器，VirtualBox 和 VirtualBox Extension Pack 安装器，完成后，看情况重新启动一下。

[下载](http://www.ubuntu.com/download/server) ubuntu 服务器版，后续指令参考 ubuntu ，但若你选择的其它发行版，你可能需要调整后面的指令。

## 建立 Box

我们要用 VirtualBox 来从零建立个 ubuntu 服务器。这是因为 Vagrant 原生支持 VirtualBox 。有很多插件支持像 VMWare 、Parallels 或 Vagrant-LXC 等等的其它 provider 。本篇指导中一直使用 VirtualBox 。

安装 ubuntu 服务器的时候，它会提示我们设置个缺省用户。我们得命名这个用户为 `vagrant` ，它也就是缺省用户。这使它成为缺省 SSH 用户，以便继续后续过程。

### 设置虚拟硬件

以下面的设置新建虚拟机：

* 名字：vagrant-ubuntu64
* 类型：Linux
* 版本：Ubuntu64
* 内存：512MB (to taste)
* 新建虚拟硬盘：[Type: VMDK, Size: 40 GB]

修改虚拟机的硬件设置，调优性能，因为 SSH 需要为 vagrant user 打开端口转发：

* 禁用音频
* 禁用 USB
* 确保网络适配器 1 设置为 NAT
* 增加端口转发规则：【名字：SSH，协议：TCP，主机地址：空白，主机端口：2222，客户机地址：空白，客户机端口：22】

挂载 Linux 安装镜像 ISO 并启动客户机。

### 安装操作系统

安装 ubuntu 很简单。跟着屏幕上的提示走即可。当提示设置用户的时候，设置用户名为 `vagrant` 密码为 `vagrant` 。它会提示你这是弱密码而有被入侵的风险。别让它动摇你，坚强点战斗下去。

### 设置根密码

为了设置超级用户，也就是 root 用户，你要能以这个用户登录。因为我在上一步安装操作系统时，让你把 vagrant 作为缺省用户了，这些命令将帮你设置根密码，然后以 root 登录，来做下一步的改动。

	sudo passwd root

这会提示你输入两次密码，我建议密码设置为“vagrant”。现在为了设置超级用户，以 root 用户登录。

	su -

### 设置超级用户

Vagrant 必须可以无密码提示运行 sudo 命令，如果此时不设置 ubuntu ，确保禁用了 vagrant 用户的 `requiretty` 。

设置 vagrant 用户运行 sudo 时无提示密码，我发现的最有效率的方法是这样把它加入 sudoers 列表：

	sudo visudo -f /etc/sudoers.d/vagrant

`/etc/sudoers.d/*` 文件夹中的，root 用户创建的任何东西，都会被加入 “sudoers” 权限。

打开文件，把这些内容加进去，保存退出。

	# add vagrant user
	vagrant ALL=(ALL) NOPASSWD:ALL

现在你可以运行这个简单的命令，测试一下是否有效：

	sudo pwd

如果一切设置正确，它会返回 home 目录，无提示输入密码。如果你被提示输入密码，就是有哪里不对了。这一步对我来说**极为重要**，所以一定要确保你的这个测试通过。

### 更新操作系统

我们制作 box 的一个原因就是为了节省时间，更新时间当然是其中一部分。所以先来更新吧。

	sudo apt-get update -y
	sudo apt-get upgrade -y

通常如果有内核更新，你会希望重启该服务器。这样做。

	sudo shutdown -r now

### 安装 Vagrant 密钥

所有 vagrant 命令，要通过 ssh 进行主机与客户服务器的通讯，就要看客户服务器是否已安装了“不安全的 vagrant 密钥”。称它“不安全”是因为本质上所有人都有这个相同密钥，如果你用了它，任何人都可以黑进所有人的 vagrant box 。

但同时，我们希望你没有在你的 vagrant box 上放入所有公司内最有价值的数据，好吧？**明白**没？嗯，好了。

	mkdir -p /home/vagrant/.ssh
	chmod 0700 /home/vagrant/.ssh
	wget --no-check-certificate \
	    https://raw.github.com/mitchellh/vagrant/master/keys/vagrant.pub \
	    -O /home/vagrant/.ssh/authorized_keys
	chmod 0600 /home/vagrant/.ssh/authorized_keys
	chown -R vagrant /home/vagrant/.ssh

### 安装配置 OpenSSH 服务器

如果你在安装过程中没有安装 SSH ，现在可以做了：

	sudo apt-get install -y openssh-server

我们需要编辑下文件 `/etc/ssh/sshd_config` ：

	sudo nano /etc/ssh/sshd_config

找到这一行，并去注释，因为我们把 Vagrant 密钥加入了这个 authorized_keys 文件：

	AuthorizedKeysFile %h/.ssh/authorized_keys

然后重启 SSH ：

	sudo service ssh restart

### 安装 Guest Tools

Guest Tools 帮助操作系统处理共享文件夹并“优化客户系统以获得更好的性能与可用性”。<sup>[2](http://tylerbird.com/blog/2014/01/27/building-a-vagrant-box-from-start-to-finish/#foot)</sup>

安装 Guest Tools 需要个编译器，输入命令：

	sudo apt-get install -y gcc build-essential linux-headers-server

在 VirtualBox 中，浏览在顶部的“设备”菜单，在下拉列表中，点击“插入 Guest Addition CD 镜像”。

这会把一个 ISO 镜像插入客户服务器的虚拟 CDROM 中。运行这些命令，挂载你的 cdrom 然后运行脚本。注意：那些关于 cdrom 只读的消息没关系。

	sudo mount /dev/cdrom /mnt 
	cd /mnt
	sudo ./VBoxLinuxAdditions.run

### 打包整个 box

打包整个 box 之前，你会希望将磁盘“零化”。“这会修复下属磁盘的碎片化问题，使得后续的压缩更有效率。”<sup>[3](http://tylerbird.com/blog/2014/01/27/building-a-vagrant-box-from-start-to-finish/#foot)</sup>

	sudo dd if=/dev/zero of=/EMPTY bs=1M
	sudo rm -f /EMPTY

现在我们准备好打包整个 box 了。我一般这样建个目录来装 box ：

	mkdir ~/code/personal/vagrant_boxes
	cd ~/code/personal/vagrant_boxes

这个是最终将上面定义的 box 打包成压缩的 gzip tarball 的命令，它也生成并包含了 `Vagrantfile` 和 `metadata.json` 文件。

	vagrant package --base vagrant-ubuntu64

Vagrant 之后会检查 VirtualBox 的任意一个名为 vagrant-ubuntu64 的实例，尝试 ssh 进去并控制它。

	→ vagrant package --base vagrant-ubuntu64
	[vagrant-ubuntu64] Attempting graceful shutdown of VM...
	[vagrant-ubuntu64] Forcing shutdown of VM...
	[vagrant-ubuntu64] Clearing any previously set forwarded ports...
	[vagrant-ubuntu64] Exporting VM...
	[vagrant-ubuntu64] Compressing package to: /Users/tbird/code/personal/virtual_boxes/package.box

在你的 `~/code/personal/vagrant_boxes` 文件夹留下个 `package.box` 文件。

### 测试你的 box

就在这同一个 `vagrant_boxes` 文件夹，你可以运行这些最终测试指令。所有重量级的提升工作都是此时做的。如果你有点东西搞砸了，那可能是在上面步骤弄的。

你应该在 `~/code/personal/vagrant_boxes/` 输入：

	vagrant box add ubuntu64 package.box
	vagrant init ubuntu64
	vagrant up

连接到你从头到尾创建的服务器！

	vagrant ssh

你成功了，值得击掌庆祝。

## Packer

当你觉得从头手动做这些事够安全的时候…就有了 [Packer](http://www.packer.io/intro) 。你问 Packer 是什么？嗯，Packer 自动化了我们做刚刚的所有事情。/扶额

总之… 一旦你安装好了 Vagrant 、VirtualBox 和 Packer ，你可以这样定义个 `quick-start.json` 文件：

	{
	  "builders": [{
	    "type": "amazon-ebs",
	    "access_key": "YOUR KEY HERE",
	    "secret_key": "YOUR SECRET KEY HERE",
	    "region": "us-east-1",
	    "source_ami": "ami-de0d9eb7",
	    "instance_type": "t1.micro",
	    "ssh_username": "ubuntu",
	    "ami_name": "packer-example "
	  }]
	}

改过 access_key 和 secret_key 后，你可以带着这个 `quick-start.json` 文件运行 packer 命令：

	packer build quick-start.json

Packer 就会自动化这个 quick-start.json 定义的 Amazon EC2 机器镜像的创建过程。这可以可选地包含一个 Vagrant box 的创建过程。

Packer 的目的是让那些镜像兼容于所有的 provider ：Amazon EC2（AMI）、DigitalOcean 、Docker 、Google Compute Engine 、OpenStack 、KVM 或 Xen 的 QEMU 实例、或是 VirtualBox 或 VMWare 软件。（完整列表见[平台](http://www.packer.io/intro/platforms.html)。）

## 我们学到什么

在这个制作 Vagrant box 的过程中，我们学到了什么？

自动化（automation）的过程，就是摘除你自己的过程。“自动（auto）”是自描述的，后缀“ation” 定义为动作（action）。所以如果我们考虑自动化你的开发环境或生产环境的工作，让它无需你参与地运行，那你的行为（action）就做对了！

甚若我们要手工或用 Packer ，知道事情怎么做要远远强过猜测事情怎么做。在自动化掉那些无聊部分之前，我喜欢体会几次，再关注那些新的更有趣的挑战。
