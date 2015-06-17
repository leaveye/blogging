Title: 迁移Blog
Date: 2015-06-17 13:37
Tags: pelican, server
Category: blogging
Slug: move-blog
Author: Levi G

之前的 blog 放在朋友的主机上，还没写上几个字呢，在换主机的过程中数据就丢失了。

> 反正没花力气，所以也不用心疼……  
> —— [Levi G.](/author/levi-g.html)

## 选择

三天前决定并开始动手，把 blog 放 Github 上面。用了半天的时间，比较过 jekyll 和 pelican 后，还是选择了 pelican 。毕竟 python 在安装上还是要比 Ruby 方便许多的。这对于我这样时不时换工作机的人还是个很大的优势。

我对 blog 的需求其实还挺烦人的。语法高亮、主题定制是基本的，$Latex$ 是必须的，要是有 graphviz 、序列图的支持就更好了。

现在的各种工具，语法高亮、主题定制都是必备功能了，产生差异的就只是配套内容的多寡了。粗略看了下 [pelican-themes][pelican-themes] 虽然没有 [Jekyll Themes][Jekyll Themes] 看上去那么完整，不过基本样子上还是够用了。毕竟这些『小众』平台比起大 Wordpress 还是差远了。

## 安装

安装、配置过程其实是非常简单的。即使如此，我也踩了进坑里了。

 * Mac OS X 系统自带和 `brew install` 的两个版本的 python 冲突问题，删掉或改名系统自带的版本可以解决。这个问题有时表现得像是权限问题。不管怎样，牢记这一条就好：

   > `brew` 的东西都是无需 `sudo` 的。  
   > —— [Levi G.](/author/levi-g.html)

 * 眼下 `brew` 安装的 pelican 版本是 3.5.0 ，有个 bug 。文章作者的值不能以 `.` 字符结尾。因为对于 San Z. 这个作者，生成的作者页面文件命名是 `san-z.html`，但是页面中作者链接的 URL 写的却是 `san-z..html` 。于是产生坏链了。

这里是安装过程中参考的资源：

* [用pelican在github上创建自己的博客!](http://x-wei.github.io/pelican_github_blog.html)
* [Pelican and Github Pages](http://martinbrochhaus.com/pelican2.html)
* [Migrating from Wordpress to Pelican](http://www.vcheng.org/2014/02/22/migrating-from-wordpress-to-pelican/)
* 以及 pelican 的文档：[HOME](http://pelican-docs-zh-cn.readthedocs.org/en/latest/)，[FAQ](http://pelican-docs-zh-cn.readthedocs.org/en/latest/faq.html)

## 定制

> 革命尚未成功，同志仍需努力。

目前为止我还没弄完，只有了个大概思路。先找了个主题用着，以后慢慢弄。

 功能 | 状态与方向
:-:|-
$Latex$ | MathJax (是这名吧)
SyntaxHighlight | 主题帮助里有
graphviz | 见到过有人开源了编译成 js 的 graphviz ，回头可以考虑试试
序列图 | 这个没找到好的本地解析，实在不行就得尽量少用，偶尔用 [WebSequenceDiagrams](https://www.websequencediagrams.com) 顶一下吧。

----

我用了几乎一整天的时间对比 [pelican 的各种主题][pelican-themes]。各有各的不满意，这当然是符合预期的。

很自然的就想瞧瞧定制的话有多难。看到了文档（[英文](http://docs.getpelican.com/en/3.5.0/themes.html#structure)，[中文](http://pelican-docs-zh-cn.readthedocs.org/en/latest/themes.html#theming-pelican)）觉得很简单，就想从零开始做个自己的主题了。在这之前，把以前喜欢的 Wordpress 主题 port 过来一个吧。

翻了好一段时间才找到当时很喜欢的主题 decode ，下载回来尝试了一下『对照翻译』弄了一下。页面主体弄起来还算容易，可惜 sidebar 的部分就被绕晕了。

> 『这动态效果是怎么实现的？状态保存在哪儿？怎么调整的？』

觉得还是不花时间弄这个了。简单选择了一个完成度比较高的现成主题 [foundation-default-colours](https://github.com/getpelican/pelican-themes/tree/master/foundation-default-colours) 。

选这个主题是因为它已经有了正确的排版并且支持了 $Latex$ 。虽然回头一点点弄的时候再换吧。

----
> 待续……

[pelican-themes]: https://github.com/getpelican/pelican-themes "pelican 主题包"
[Jekyll Themes]: http://jekyllthemes.org "Jekyll 主题包"