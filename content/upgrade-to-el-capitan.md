Title: 升级 OS X El Capitan
Date: 2015-10-03 14:27:31
Edited: 2015-10-03 14:28:01
Tags: os x, el capitan, kernel_task, sip
Category: macOS
Slug: upgrade-to-el-capitan
Author: Levi G
Status: published

10 月 1 日发现 Apple 推送了 El Capitan 的更新。第一时间点击升级，准备体验一下。

几小时后，升级包终于下载完成了，在电脑上多了个『安装 El Capitan』的软件。果断打开。

回答确认了安装程序的一系列问题，并且第一次重启电脑后，进度条走的非常慢，最后卡在 30% 左右不动了。

担心了 1 个小时变砖的问题，决定还是强行关机。重启后没有继续安装，而是自动进入到升级前的系统。庆幸了一下。再次点击安装软件，重启进入安装过程。

这次虽然进度条依旧很慢，但是顺利完成了安装过程。登录系统后，发现又再次出现了一年前修复的 `kernel_task` 进程 CPU 占用率暴高的问题。搜索到了[结果](http://www.zhihu.com/question/19611376)，准备照此办理。

查询到我的设备型号是 `MacBookPro8,2`，要删除的文件没有权限：

```
$ pwd && ls -lO@ MacBookPro8_2.plist
/System/Library/Extensions/IOPlatformPluginFamily.kext/Contents/PlugIns/ACPI_SMC_PlatformPlugin.kext/Contents/Resources
-rw-r--r--  1 root  wheel  restricted   14K  9 17 09:20 MacBookPro8_2.plist
```

尝试过安全模式下，仍然没有权限。搜索得知，这个 `restricted` 属性是 El Capitan 新加功能 SIP (System Intregrity Protection) 的一部分。常规启动下的 root 用户并没有这部分操作权限。有的说通过设置 `nvrom bootarg='rootless=0'` 来尝试解决，似乎这样风险有点大。还是根据[这里](https://forums.developer.apple.com/thread/3981)，使用 OS X 自带的 Recovery OS 来弄吧。这里我还因为硬盘里没有恢复分区而折腾了两个小时，又是找制作修复磁盘的工具又是借 U 盘的，直到后来看到帖子说只需要能连到网络就可以进入恢复系统……

进入 Recovery OS 的方法是启动电脑时，播放声音后，苹果 Logo 前，按 Command+R 键即可。可我这已经没有启动声音很久了，只好在黑屏就开始反复按这个组合键。

在恢复系统中，进入终端后：

```
# 进入硬盘 我这里硬盘卷标叫做『Macintosh HD』
cd /Volumes/Macintosh\ HD
# 进入文件所在路径
cd System/Library/Extensions/IOPlatformPluginFamily.kext/Contents/PlugIns/ACPI_SMC_PlatformPlugin.kext/Contents/Resources
# 关闭 SIP
csrutil disable
# 删除文件
rm MacBookPro8_2.plist
# 还原 SIP
csrutil enable
```

> 这里我先关闭 SIP 才删除文件的，怀疑不必关闭 SIP 直接就能操作，不过我没有验证。

再次重启，系统终于恢复正常了。