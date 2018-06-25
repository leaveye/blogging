Title: 编写 udev 规则
Date: 2016-12-15 19:29
Edited: 2016-12-16 11:03
Tags: linux, udev, rules
Category: Linux
Slug: writing-udev-rules
Author: Levi G
Status: published

by Daniel Drake (dsd)
Version 0.74

本文最新版本可在此处找到：

* [http://www.reactivated.net/writing_udev_rules.html](http://www.reactivated.net/writing_udev_rules.html) (英文版)
* [http://blog.levi-g.info/writing-udev-rules.html](http://blog.levi-g.info/writing-udev-rules.html) (中文版)

## 目录
[TOC]

## 介绍

### 关于本文档

udev 面向 2.6 及以上的 Linux 内核，提供带有固定设备命名的，动态 /dev 目录的，用户空间解决方案。之前的 /dev 实现 *devfs* 现已被废弃，udev 成为继任者。udev vs devfs 是一个敏感的谈话内容，在进行比较之前你应该读一下[这个文档](http://kernel.org/pub/linux/utils/kernel/hotplug/udev_vs_devfs)。

几年间，如同规则自身的弹性，你为之使用 udev 规则的设备变化了。在现代系统中，udev 为系统外的设备类型提供了固定的命名方法，避免了为这些设备提供定制规则。然而一些用户仍然需要额外的定制级别。

本文档假设你已经安装了 udev 并使用缺省配置运行良好。这通常是通过你的 Linux 发行版做到的。

本文档不会覆盖规则书写的方方面面，只集中介绍所有主要概念。更多细节信息可以在 udev 的 man 页面中找到。

本文档使用各种例子（一些完全是虚构的）来阐述观点和概念。不是所有语法都会显式的在附带文本中描述，请确信通过查看例子规则来获取完整的理解。

### 更新历史
(略)

## 概念

### 语义: devfs, sysfs, nodes 等

仅仅是基本介绍，可能并不完全准确。

在典型的基于 Linux 的系统中，*/dev* 目录用来存储文件一样的设备节点（**nodes**），它们指向系统中特定的设备。每一个节点指向系统的一部分（一个设备），可能存在也可能不存在。用户空间应用程序可以使用这些设备节点跟系统硬件打交道，例如，X 服务器“监听” /dev/input/mice 来根据用户的鼠标移动来移动可视鼠标指针。

原始的 */dev* 目录在设备可能在系统中出现时就产生，因此 /dev 目录一般非常大。随之而来的 **devfs** 提供了一种易于管理的途径（注意它仅仅在硬件插入到系统中时产生 /dev ）以及其他功能，但系统会出现无法轻松修复的问题。

**udev** 是一种“新”的管理 */dev* 目录的方法，它的设计清除了以前的 */dev* 实现的一些问题，并提供了鲁棒的路径以向后兼容。为了创建并命名系统中相应的 */dev* 设备结点，udev 需要依赖于根据用户提供的规则从 *sysfs* 中得到的匹配信息。本文着重规则书写的详细过程，udev 相关的任务（或许）要由用户自己完成。

**sysfs** 是 2.6 内核中一个新的文件系统。它由内核管理，并导出当前系统中插入的设备基本信息。udev 可使用这些信息创建对应的硬件设备结点。sysfs 挂载在 */sys* 下且可浏览。你可能很希望在使用 udev 之前刺探下存储在那儿的有关文件。本文中，我将等同地使用 */sys* 和 *sysfs* 术语。

### 为什么？

udev 规则有弹性且非常强大。这里是一些你使用规则可以达成的结果：

* 重命名设备节点的缺省名字为其他名字
* 通过创建符号链接到缺省设备节点来提供一个替代或固定的设备节点名
* 基于程序的输出命名设备节点
* 改变设备节点的权限和所有权
* 当设备节点被创建或删除时（通常是添加设备或拔出设备时）执行一个脚本
* 重命名网络接口

当存在的特定设备没有设备节点时，这_不是_书写规则的工作范围。即使没有匹配的规则，udev 也会利用内核提供的缺省名字来创建设备节点.

拥有固定命名的设备节点有很多好处。假设你有两个 USB 存储设备：一个数码相机，一个是 USB 闪存盘。通常这两个设备被赋予 */dev/sda* 和 */dev/sdb* 设备节点，然而准确的赋值取决于它们连接到系统的顺序。这可能为一些用户造成麻烦，如果每个设备每次都可以固定命名，比如 */dev/camera* 和 */dev/flashdisk*，用户就会获益。

### 内置固定命名方案

udev 为系统外的一些设备类型提供了固定命名。这是一个很有用的特性，在大多情况下意味着你不用书写任何规则。

udev 为存储设备在 */dev/disk* 目录下提供了系统外命名方法。要查看它为你的存储硬件创建的固定命名，你可以使用下列命令：

	#ls -lR /dev/disk

所有存储类型都可以这么用。例如，udev 为我的根分区创建了固定命名链接 */dev/disk/by-id/scsi-SATA\_ST3120827AS\_4MS1NDXZ-part3*。当我插入我的 USB 闪存盘，udev 就会创建另外一个固定命名节点 */dev/disk/by-id/usb-Prolific\_Technology\_Inc.\_USB\_Mass\_Storage\_Device-part1*。

## 规则书写

### 规则文件和语义

为决定如何命名设备以及执行什么额外动作，udev 会读取一系列规则文件。这些文件保存在 */etc/udev/rules.d* 目录下并且都必须有 *.rules* 后缀名。

缺省udev规则存储在 */etc/udev/rules.d/50-udev.rules* 里面。你可能发现整个文件很有意思，它包含了少量例子，继而是一些提供了 devfs 风格 /dev 布局的缺省规则。但是你不应该直接在这个文件里面书写规则。

/etc/udev/rules.d/ 下面的文件按字典序解析，在某些情况下，规则文件的解析顺序很重要。通常来说你希望你的规则可以在缺省规则之前解析，所以我建议你创建一个文件 */etc/udev/rules.d/10-local.rules* 并把自己的所有规则写到这里面去。

在一个规则文件中，以 `#` 开头的行被认为是注释。除此之外每一个非空的行都是一条规则。规则不能跨越多行。

一个设备可以被多条规则匹配到。实用方面这有优势。例如，我们可以写两个匹配同一个设备的规则，每一个规则为设备提供了它自己的替代命名。即使分开在不同的文件中，两个替代命名也都会被创。要明白 udev 在找到一个匹配规则后*不会*停止处理其他规则，它仍然会继续查找并尝试应用已知的每条规则，这很重要。

### 规则语法

每条规则由一系列逗号分隔的键值对组成。**匹配**键是用来识别要应用规则的设备的条件。当规则中对应设备的_所有_匹配键被涉及时，就会应用规则并且触发**赋值**键的行为。每条规则应该包含至少一个匹配键和至少一个赋值键。

这是用来阐述上面内容的一个例子规则：

    KERNEL=="hdb", NAME="my_spare_disk"

上述规则包含一个匹配键（*KERNEL*）以及一个赋值键（*NAME*）。这些键和它们属性的语义将在稍后具体说明。重点注意到匹配键通过连等号（==）与它的值联系起来, 赋值键通过等号（=）与它的值关联。

注意 udev 不支持任何形式的行连接符。不要在你的规则种插入任何断行符，这将会导致 udev 把你的一条规则看做是多条规则，不会按预期工作。

### 基本规则

udev 提供许多用来书写精确匹配规则的匹配键。其中一些常用键将在下面介绍，其他将在文档的后面说明。完整列表可以查看 udev 的 man 页面.

* **KERNEL** - 匹配内核为设备的命名
* **SUBSYSTEM** - 匹配设备的子系统
* **DRIVER** - 匹配支持设备的驱动名称

在你使用一系列匹配键来准确匹配设备后，udev 通过赋值键让你更好的控制接下来发生的事。完整的赋值键列表可以查看 udev 的 man 页面。最基本的赋值键在下面说明，其他的将在文档结束时说明。

* **NAME** - 设备节点应该使用的名字
* **SYMLINK** - 一个设备节点的替代符号链接命名**列表**

正如前文所暗示的，udev 仅仅为设备创建一个真正的设备节点。如果你希望为设备节点提供替代命名，你得使用符号链接功能。通过 *SYMLINK* 赋值，实际上是维护一个符号链接*列表*，这些符号链接都会指向真实的设备节点。为了维护这些链接，我们介绍一个用来追加到列表的新操作符：`+=`。你可以在一个规则中附加多个符号链接到列表中，通过空格分开。

	KERNEL=="hdb", NAME="my_spare_disk"

上面规则意思是：*匹配一个内核命名为 hdb 的设备，把它重新命名为 my\_spare\_disk。*设备节点出现在 */dev/my\_spare\_disk* 。

	KERNEL=="hdb", DRIVER=="ide-disk", SYMLINK+="sparedisk"

上面规则意思是：*匹配一个内核命名为 hdb _同时_驱动为 ide-disk 的设备，以缺省命名设备节点，并创建一个名为 sparedisk 的符号链接指向它。*注意我们没有指明设备节点名字，于是 udev 使用缺省命名。为保留标准 */dev* 布局，你自己的规则通常没有 NAME 但会创建一些 SYMLINK 并/或执行其他赋值操作。

	KERNEL=="hdc", SYMLINK+="cdrom cdrom0"

上面规则很可能就是你要写的典型规则。它在 */dev/cdrom* 和 */dev/cdrom0* 创建了两个指向 */dev/hdc* 的符号链接。也没有指定 NAME 赋值，所以使用缺省的内核命名（hdc）。

### 匹配 sysfs 属性

到目前为止介绍的匹配键仅仅提供了有限的匹配能力。实际上我们需要更加优良的控制：我们想基于设备的高级属性来识别设备，如供应商编码、产品编号、序列号、存储能力、分区数等等。

很多驱动导出这些信息到 sysfs ，udev 允许我们使用 ATTR 键通过稍捎不同的语法来将 sysfs 匹配纳入规则中。

这里有一个匹配 sysfs 中单一属性的例子。文后会提供更多细节来帮助你基于 sysfs 属性书写规则。

	SUBSYSTEM=="block", ATTR{size}=="234441648", SYMLINK+="my_disk"
 
### 设备级联

Linux 内核实际上以树状结构展示设备，这个信息通过 sysfs 显露出来，在书写规则时这非常有用。例如我的硬盘设备展示为一个 SCSI 磁盘设备的孩子，这个 SCSI 磁盘设备又是一个串行 ATA 控制器设备的孩子，该控制器又是 PCI 总线设备的孩子。你很有可能发现你需要从一个讨论中的设备的祖先那里引用信息，比如我的硬盘设备的序列号在设备级别并不暴露出来, 而是在 SCSI 磁盘级别通过它的直接双亲展现。

目前介绍的四个主要匹配键（KERNEL/SUBSYSTEM/DRIVER/ATTR）仅仅跟对应设备的值匹配，不能跟双亲设备的值匹配。udev 提供了在树中向上查找的匹配键变种：

* **KERNELS** - 匹配设备的内核名，或任何祖先设备的内核名
* **SUBSYSTEMS** - 匹配设备的子系统名，或任何祖先设备中的子系统名
* **DRIVERS** - 匹配支持设备的驱动名，或任何支持祖先设备的驱动名
* **ATTRS** - 匹配设备的 sysfs 属性，或任何祖先设备的 sysfs 属性

由于在心里要考虑到级联结构，你可能感觉到规则书写变的有点复杂了。歇一会吧，有工具可以帮助我们的，后文再表。

### 字符串替换

当编写意图要处理多个相似设备的规则时，udev 的 *printf 风格的字符串替换操作符*就非常有用了。你可以在你的规则里面的任何赋值里面包含这些操作符，udev 在执行它们时会对其求值。

最常用的操作符是 **%k** 和 **%n** 。%k 求值为设备的内核命名，例如字符串“sda3”之于（缺省）出现在 */dev/sda3* 的设备。%n 求值为设备的内核号码（存储设备的分区号），例如“3”之于 */dev/sda3* 。

udev 也提供了一些高级功能替换操作符。在读完本文剩下内容后可以查询 udev 的 man 页面。以上例子中的操作符也有一个替代语法—— **\$kernel** 和 **\$number** 。因此如果你希望在规则中匹配字符 % ，你必须写成 %% ；如果你希望匹配字符 \$ ，你必须写成 \$\$ 。

为阐述下字符串替换的概念，我们来展示几个例子：

	KERNEL=="mice", NAME="input/%k"
	KERNEL=="loop0", NAME="loop/%n", SYMLINK+="%k"

第一条规则确保鼠标设备节点仅仅出现在 */dev/input* 目录下（缺省是在 */dev/mice* 下面）。第二条规则确保名为 loop0 的设备节点在 */dev/loop/0* 创建，但也会照常在 */dev/loop0* 创建一个符号链接。

上面规则的使用都比较可疑，因为他们都可以通过不使用任何替换操作符来重写。这些替换的真正威力将会在下一节显现。

### 字符串匹配

不仅有字符串精确匹配，udev 也允许你使用 shell 风格的模式匹配。支持3种模式：

* **\*** - 匹配任何字符，0 次或多次
* **?** - 匹配任何字符一次
* **[]** - 匹配任何方括号中指定的单个字符，可以指定范围

这里有一些例子，注意字符串替换符的使用：

	KERNEL=="fd[0-9]*", NAME="floppy/%n", SYMLINK+="%k"
	KERNEL=="hiddev*", NAME="usb/%k"

第一条规则匹配所有软盘驱动，确保设备节点放置在 */dev/floppy* 目录下，也创建一个缺省命名的符号链接。第二条规则确保 hiddev 设备节点放在 */dev/usb* 目录下面。

## 从 sysfs 中查找信息

### sysfs 树

从 sysfs 中获取关注信息的概念在之前的例子中已经触及。为基于这些信息书写规则，你首先需要知道属性名和他们的当前值。

sysfs 实际上是一个非常简单的结构。逻辑上分成目录形式。每一个目录包含一定量的文件（属性），这些文件往往仅包含一个值。也会有一些符号链接，它们把设备链到双亲那里。级联结构已在上面说明了。

一些目录被作为*顶层设备路径*引用。这些目录表示了拥有对应设备节点的实际设备。顶层设备路径可以被归类为包含 *dev* 文件的 sysfs 目录，下列命令可以列举出这些文件：

	# find /sys -name dev

例如，在我的系统中，*/sys/block/sda* 目录就是我的硬盘设备路径。它通过 */sys/block/sda/device* 符号链接链向它的双亲 SCSI 磁盘设备。

当你书写基于 sysfs 信息的规则时，只是简单的匹配链条上一部分文件的属性内容。例如，我可以这样读我的硬盘的大小：

	# cat /sys/block/sda/size
	234441648

在一个 udev 规则里面，我可以使用 ATTR{size}=="234441648" 来识别这个磁盘。因为 udev 遍历设备链，我可以使用 ATTRS 匹配链中另外一部分的属性（如 */sys/class/block/sda/device* 中的属性），然而在处理链中不同部分时会有一些告诫，稍后描述。

虽然对 sysfs 的结构和具体 udev 如何匹配值来说，梳理 sysfs 都是有用的介绍，但这是个既耗时也没必要的事。

### udevinfo

你构造规则最直白的工具大概就是敲入 *udevinfo* 了。你需要知道的全部，就是问题设备的 sysfs 设备路径。下面是一个精简的例子（udevinfo 输出信息中，每段颜色不同，第一段绿色，第二段蓝色，第三段栗色，译者注）：

	# udevinfo -a -p /sys/block/sda
	
	  looking at device '/block/sda':
	    KERNEL=="sda"
	    SUBSYSTEM=="block"
	    ATTR{stat}=="  128535     2246  2788977   766188    73998   317300  3132216  5735004        0   516516  6503316"
	    ATTR{size}=="234441648"
	    ATTR{removable}=="0"
	    ATTR{range}=="16"
	    ATTR{dev}=="8:0"
	
	  looking at parent device '/devices/pci0000:00/0000:00:07.0/host0/target0:0:0/0:0:0:0':
	    KERNELS=="0:0:0:0"
	    SUBSYSTEMS=="scsi"
	    DRIVERS=="sd"
	    ATTRS{ioerr_cnt}=="0x0"
	    ATTRS{iodone_cnt}=="0x31737"
	    ATTRS{iorequest_cnt}=="0x31737"
	    ATTRS{iocounterbits}=="32"
	    ATTRS{timeout}=="30"
	    ATTRS{state}=="running"
	    ATTRS{rev}=="3.42"
	    ATTRS{model}=="ST3120827AS     "
	    ATTRS{vendor}=="ATA     "
	    ATTRS{scsi_level}=="6"
	    ATTRS{type}=="0"
	    ATTRS{queue_type}=="none"
	    ATTRS{queue_depth}=="1"
	    ATTRS{device_blocked}=="0"
	
	  looking at parent device '/devices/pci0000:00/0000:00:07.0':
	    KERNELS=="0000:00:07.0"
	    SUBSYSTEMS=="pci"
	    DRIVERS=="sata_nv"
	    ATTRS{vendor}=="0x10de"
	    ATTRS{device}=="0x037f"

正如你看到的，udevinfo 简单的产生一个你可以在 udev 规则中作为匹配键的属性列表。从上面例子中我可以为该设备产生下面两条规则（ATTR 绿色，SUBSYSTEMS、ATTRS 蓝色，DRIVERS 栗色，译者注）：

	SUBSYSTEM=="block", ATTR{size}=="234441648", NAME="my_hard_disk"
	SUBSYSTEM=="block", SUBSYSTEMS=="scsi", ATTRS{model}=="ST3120827AS", NAME="my_hard_disk"

你可能发现到例子中使用了颜色，这是为了阐述把问题设备属性和*单个*祖先设备属性并在一起是合法的，你不能混合匹配多个祖先设备属性——这样你的规则不能工作。例如，下列规则（ATTRS 蓝色，DRIVERS 栗色，译者注）是*不合理的*，因为它试图匹配两个祖先设备的属性：

	SUBSYSTEM=="block", ATTRS{model}=="ST3120827AS", DRIVERS=="sata_nv", NAME="my_hard_disk"

通常有大量的属性提供给你，你必须挑选其中一部分来构造你的规则。一般来讲，你希望挑选那些能够稳定标识你的设备并便于理解的属性。上例中我选取的是我的磁盘大小和它的模型号，而没有使用没有意义的数字，诸如 ATTRS{iodone_cnt}=="0×31737" 。

仔细观察下 udevinfo 的输出中的级联结构。对应于设备的绿色部分，使用了标准匹配键如 KERNEL 和 ATTR 。蓝色部分和栗色部分使用了祖先遍历变量如 SUBSYSTEMS 和 ATTRS 。这就是为什么级联结构的复杂性实际上很容易处理的原因，只要确保使用 udevinfo 建议的准确值就行了。

另外一点需要指出的是 udevinfo 输出的文本属性之间用空格填充（例如上面的 ST3120827AS ）是很常见的。在你的规则中你可以添加那些额外的空格，也可以像我那样去掉。

使用 udevinfo 的唯一复杂之处在于要求你知道顶级设备路径（例如上面例子中的 /sys/block/sda ）。这通常并不明显。但是，因为你通常是为已经存在的设备节点写规则，你可以自己使用 udevinfo 查找设备路径：

	#udevinfo -a -p $(udevinfo -q path -n /dev/sda)

### 替代方法 

虽然 udevinfo 差不多是列举你要构建的规则的准确属性的最直接方式，但一些用户仍然乐于使用其它工具。诸如 [usbview](http://www.kroah.com/linux/usb/) 的工具可以显示类似的信息集，这些信息大多也可以用在规则中。

## 高级话题

### 控制权限和所有权

udev 允许你在规则中使用另外的赋值来控制每个设备的所有权和权限属性。

*GROUP* 赋值允许你定义哪个 Unix 组应该拥有设备节点。这里有一个例子规则，它定义 *video* 组拥有 framebuffer 设备：

	KERNEL=="fb[0-9]*", NAME="fb/%n", SYMLINK+="%k", GROUP="video"

*OWNER* 键可能用处不大，它允许你定义哪个 Unix 用户应该具有设备节点的所有权。假设有个奇怪状况要你让 *john* 拥有软盘设备，你可以使用：

	KERNEL="fd[0-9]*", OWNER="john"

udev 缺省用 Unix 的 0660 权限（拥有者和组员可以读写）创建设备节点。需要的话你可以在特定设备的规则中包含 *MODE* 赋值键覆盖这些缺省值。作为例子，下面的规则定义了 inotify 节点可以被每个人读写：

	KERNEL=="inotify", NAME="misc/%k", SYMLINK+="%k", MODE="0666"

### 使用外部程序来命名设备

某些情况下你可能要求比 udev 标准规则提供的更多弹性。这种情况下，你可以请求 udev 运行一个程序并运用程序的标准输出来提供设备命名。

要使用这个功能，你只需简单的在 *PROGRAM* 赋值中指定要运行程序（以及任何参数）的绝对路径，然后在 NAME/SYMLINK 赋值中使用 *%c* 替换及其变种。

下列例子引用一个位于 */bin/device_namer* 的虚构程序。device_namer 接收一个表示内核名字的命令行参数。基于内核名，device_namer 做一些魔幻变换接着产生一些输出到普通 *stdout* 管道，这些输出被分割为很多小块，每一小块是一个单词，块之间用一个空格分开。

在我们的第一个例子中，我们假设 device_namer 输出中，每一个部分形成当前设备的一个符号链接（替代命名）。

	KERNEL=="hda", PROGRAM="/bin/device_namer %k", SYMLINK+="%c"

下一个例子假设 device_namer 有两部分输出，第一部分是设备名字，第二部分是额外符号链接的名字。我们现在介绍 *%c{N}* 替换，它引用命令输出的第 N 个部分：

	KERNEL=="hda", PROGRAM="/bin/device_namer %k", NAME="%c{1}", SYMLINK+="%c{2}"

下一个例子假设 device_namer 输出第一部分是设备名，后面跟着任意数量的部分，形成另外的符号链接。我们现在介绍 *%c{N+}* 替换，它将被求值为第 N 部分及其后的全部内容。

	KERNEL=="hda", PROGRAM="/bin/device_namer %k", NAME="%c{1}", SYMLINK+="%c{2+}"

输出的部分也可在任一赋值键中使用，而不仅限于 NAME 和 SYMLINK 。下个例子使用一个虚构程序来决定哪个 Unix 组拥有设备：

	KERNEL=="hda", PROGRAM="/bin/who_owns_device %k", GROUP="%c"

### 特定事件发生时运行外部程序

书写 udev 规则还有一个原因，就是为了在设备连接或者断开时运行一个特定程序。例如，你可能想在你的数码相机连到系统时执行一个脚本来自动下载相机里面的所有照片。

不要把这个跟上述的 *PROGRAM* 功能弄混淆了，*PROGRAM* 是用来运行产生设备名字（除此之外不应该做其他事情）程序。当执行这些程序时，设备节点还没创建，所以对设备的任何形式的操作都是不可能的。

这里介绍的功能允许你在设备节点到位后运行一个程序。该程序可以作用在设备上，但是它不准超时运行，因为当程序运行时 udev 是暂停运行的。一个变通办法是确保你的程序立即分离（detach）自身。

这里有个展示 *RUN* 列表赋值的例子:

	KERNEL=="sdb", RUN+="/usr/bin/my_program"

当执行 */usr/bin/my_program* 时，udev 环境的多数部分可作为环境变量使用，包括诸如 *SUBSYSTEM* 的键值。你也可以使用 *ACTION* 环境变量来检测设备是否连接或断开，它的对应值是 “add” 和 “remove” 。

udev 并不在任何激活终端中运行这些程序，也不再 shell 上下文中执行。确保你的程序是可执行的，如果它是个 shell 脚本请确保它以适当的 [shebang](http://en.wikipedia.org/wiki/Shebang_(Unix)) 开头（如`#!/bin/sh`），也不要在你的终端上期待任何标准输出。

### 环境交互

udev 为环境变量提供了一个 *ENV* 键，可用于匹配和赋值。

在赋值情况下，你可以设置稍后要匹配的环境变量。你也可以为通过上面提到的技巧调用的任何外部程序设置环境变量。一个虚构的设置环境变量的例子规则如下：

	KERNEL=="fd0", SYMLINK+="floppy", ENV{some_var}="value"

在匹配情况下，你可以确保规则仅仅依赖一个环境变量的值而运行。注意 udev 看到的环境跟你在控制台上得到的用户环境不一样。一个虚构的涉及环境匹配的规则如下：

	KERNEL=="fd0", ENV{an_env_var}=="yes", SYMLINK+="floppy"

上面规则仅当 udev 环境中的 \$an\_env\_var 的值设为 “yes” 时才创建 */dev/floppy* 链接。

### 额外选项

另外一个有用的赋值是 *OPTIONS* 列表。可用的选项不多：

* **all_partitions** - 为一个块设备创建所有可能的分区，而不是初始检测到的那些分区
* **ignore_device** - 完全忽略事件
* **last_rule** - 确保后面的所有规则不会生效

例如，下面规则设置我的硬盘节点的组所有权，并且后面的规则对它没有任何效果：

	KERNEL=="sda", GROUP="disk", OPTIONS+="last_rule"

## 例子

### USB 打印机

我打开了打印机，它就被赋予了一个设备节点 */dev/lp0* 。我不太满意这样乏味的名字，打算使用 udevinfo 帮我写一个规则来提供一个替代名字：

	# udevinfo -a -p $(udevinfo -q path -n /dev/lp0)
	  looking at device '/class/usb/lp0':
	    KERNEL=="lp0"
	    SUBSYSTEM=="usb"
	    DRIVER==""
	    ATTR{dev}=="180:0"
	
	  looking at parent device '/devices/pci0000:00/0000:00:1d.0/usb1/1-1':
	    SUBSYSTEMS=="usb"
	    ATTRS{manufacturer}=="EPSON"
	    ATTRS{product}=="USB Printer"
	    ATTRS{serial}=="L72010011070626380"

我的规则就成了：

	SUBSYSTEM=="usb", ATTRS{serial}=="L72010011070626380", SYMLINK+="epson_680"

### USB相机

跟大多数相机一样, 我的相机标识自己为一个通过 USB 总线来连接，通过 SCSI 传输的外部硬盘。为了访问我的相片，我先挂载分区然后拷贝图片文件到我的硬盘中。

不是所有相机都这样工作，其中一些使用非存储协议，如 [gphoto2](http://www.gphoto.org/) 支持的相机。在 gphoto 情况下，你不用为你的设备写任何规则，因为纯粹由用户空间控制（而不是指定的内核驱动）。

USB 相机设备的一个常见复杂性在于，它们通常标识自己是一个单分区磁盘，就是有 */dev/sdb1* 的 */dev/sdb* 。sdb 节点对我毫无用处，但对 sdb1 有兴趣——这才是我要挂载的。这里有个麻烦因为 sysfs 是链式的，udevinfo 为 /dev/sdb1 产生的有用属性跟为 /dev/sdb 产生的一样，这导致你的规则潜在的匹配到原始磁盘和分区，这不是你想要的，你的规则应该**特化**。

为绕过这个，你只需要考虑下 sdb 和 sdb1 之间有什么区别。夸张地简单：只是名字不同，所以我们可在 NAME 域上使用一个简单的模式匹配。

	# udevinfo -a -p $(udevinfo -q path -n /dev/sdb1)
	  looking at device '/block/sdb/sdb1':
	    KERNEL=="sdb1"
	    SUBSYSTEM=="block"
	
	  looking at parent device '/devices/pci0000:00/0000:00:02.1/usb1/1-1/1-1:1.0/host6/target6:0:0/6:0:0:0':
	    KERNELS=="6:0:0:0"
	    SUBSYSTEMS=="scsi"
	    DRIVERS=="sd"
	    ATTRS{rev}=="1.00"
	    ATTRS{model}=="X250,D560Z,C350Z"
	    ATTRS{vendor}=="OLYMPUS "
	    ATTRS{scsi_level}=="3"
	    ATTRS{type}=="0"

我的规则：

	KERNEL=="sd?1", SUBSYSTEMS=="scsi", ATTRS{model}=="X250,D560Z,C350Z", SYMLINK+="camera"

### USB硬盘

USB 硬盘跟 USB 相机差不多，但典型的使用方式不同。在相机例子中，我解释过对 sdb 节点没有兴趣，它仅仅在分区（如使用fdisk）时才有用，但我为什么要为相机分区呢！？

当然如果你有一个 100GB 的 USB 硬盘，你希望为它分区是完全可以理解的，这种情况下我们可以使用 udev 的字符串替换优势：

	KERNEL=="sd*", SUBSYSTEMS=="scsi", ATTRS{model}=="USB 2.0 Storage Device", SYMLINK+="usbhd%n"

这个规则创建诸如下面的符号链接:

* */dev/usbhd* - 可被 fdisk 的节点
* */dev/usbhd1* - 第一块分区（可挂载）
* */dev/usbhd2* - 第二块分区（可挂载）

### USB读卡器

USB读卡器（CompactFlash，SmartMedia 等）属于 USB 存储设备的另一范围，它有不同的使用需求。

这些设备一般在媒介（指存储卡）改变时不通知主机。所以如果你插入这种设备时不带媒介，再插入一张卡，计算机不会意识到这点，你也不会有媒介的可挂载的 sdb1 分区节点。

一个可能的解决办法是采取 *all\_partttions* 选项的长处，它将为每个规则匹配的块设备创建 16 个分区节点：

	KERNEL="sd*", SUBSYSTEMS=="scsi", ATTRS{model}=="USB 2.0 CompactFlash Reader", SYMLINK+="cfrdr%n", OPTIONS+="all_partitions"

你将得到这些命名节点：cfrdr，cfrdr1，cfrdr2，cfrdr3，…，cfrdr15。

### USB Palm 导航仪

这些设备作为 USB 串行设备工作，所以缺省状态下，你只会得到 *ttyUSB1* 设备节点。palm 工具依赖于 */dev/pilot* ，有很多用户会希望使用一条规则提供它。

[Carsten Clasohm 的博客](http://www.clasohm.com/blog/one-entry?entry%5fid=12096)看上去是它毫无争议上的源头。Carsten 的规则如下：

	SUBSYSTEMS=="usb", ATTRS{product}=="Palm Handheld", KERNEL=="ttyUSB*", SYMLINK+="pilot"

注意到产品字符串因产品不同很多变，所以确保你检查（使用 udevinfo）了哪一个适用于你。

### 光驱

我的电脑有两个光驱：一个 DVD 只读（hdc），一个 DVD 刻录（hdd）。除非我物理性的重新接线，我不希望这些设备节点有变化。然而一些用户喜欢拥有诸如 */dev/dvd* 这么方便的设备节点。

我们知道了 KERNEL 是这些设备的名字，规则书写就很简单了。这是我系统上的一些例子：

	SUBSYSTEM=="block", KERNEL=="hdc", SYMLINK+="dvd", GROUP="cdrom"
	SUBSYSTEM=="block", KERNEL=="hdd", SYMLINK+="dvdrw", GROUP="cdrom"

### 网卡接口

尽管它们都是通过名字引用，网卡往往没有与之关联的设备节点。即便如此，规则书写过程还是几乎一样的。

在规则中简单的匹配网卡 MAC 地址是有意义的，因为它们是唯一的。但是，确信你使用的是 udevinfo 显示的*准确* MAC 地址，因为如果你没有精准匹配，你的规则不会工作。

	# udevinfo -a -p /sys/class/net/eth0
	  looking at class device '/sys/class/net/eth0':
	    KERNEL=="eth0"
	    ATTR{address}=="00:52:8b:d5:04:48"

这是我的规则：

	KERNEL=="eth*", ATTR{address}=="00:52:8b:d5:04:48", NAME="lan"

为了让这个规则生效，你得重启网络驱动。你可以卸载并重新加载模块，或简单的重启系统。你还得重新配置你的系统使用 “lan” 取代 “eth0”。我以前遇到过这样的麻烦（网卡不能重命名）直到我去除了所有对 eth0 的引用。在此之后，你应该可以在任何 ifconfig 或类似的工具的调用中使用 “lan” 取代 “eth0” 了。

## 测试和调试

### 让你的规则跑起来

假如你在一个有 *inotify* 支持的近期内核上工作，udev 将自动监视你的规则目录并且自动挑取你对规则文件的任何修改。

尽管这样，udev 也不会自动重新处理所有设备并试图应用新规则。例如，如果你写了个规则来为你的已连接相机添加一个额外符号链接，你不能指望这个符号链接可以马上显现出来。

为使符号链接显示，你可以断开并重连你的相机，或在设备不可移除时，代之以运行 **udevtrigger** 。

如果你的内核没有 inotify 支持，新规则不会自动被检测到。这种情况下，你必须在做出更改后运行 **udevcontrol reload_rules** 使之生效。

### udevtest

如果你知道 sysfs 中的顶级设备路径，你可以使用 **udevtest** 来显示 udev 将要执行的动作。这也许可以帮你调试你的规则。例如，假设你想调试作用在 */sys/class/sound/dsp* 上的规则：

	# udevtest /class/sound/dsp
	main: looking at device '/class/sound/dsp' from subsystem 'sound'
	udev_rules_get_name: add symlink 'dsp'
	udev_rules_get_name: rule applied, 'dsp' becomes 'sound/dsp'
	udev_device_event: device '/class/sound/dsp' already known, remove possible symlinks
	udev_node_add: creating device node '/dev/sound/dsp', major = '14', minor = '3', mode = '0660', uid = '0', gid = '18'
	udev_node_add: creating symlink '/dev/dsp' to 'sound/dsp'

注意 */sys* 前缀在 udevtest 命令行中被删除了，这是因为 udevtest 在设备路径上操作。还要留意的是 udevtest 是一个纯粹的测试/调试工具，无论输出怎么建议，它不创建任何设备节点。

## 作者以及联系方式 

本文由 Daniel Drake <[dan@reactivated.net](mailto:dan@reactivated.net)> 写就。欢迎反馈信息。

本译文由 Levi G. <[leaveye@hotmail.com](mailto:leaveye@hotmail.com)> 基于旧翻译修改更新。

对于技术支持你可以致信给 linux-hotplug 邮件列表：[linux-hotplug-devel@lists.sourceforge.net](mailto:linux-hotplug-devel@lists.sourceforge.net) 。

Copyright (C) 2003-2006 Daniel Drake。
本文档基于 [GNU General Public License, Version 2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html) 授权。