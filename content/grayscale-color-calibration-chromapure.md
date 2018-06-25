title: 【译】小白也能用 ChromaPure 做灰阶与颜色校准
Date: 2018-4-17 02:19
Tags: video, calibration, projector, home theater
Category: 家庭影院
Slug: calibration-by-chromapure
Author: Levi G
Status: published

原文：[CHROMAPURE GRAYSCALE & COLOR CALIBRATION FOR DUMMIES](http://www.curtpalme.com/forum/viewtopic.php?t=35322)
参考了[旧版本](http://www.curtpalme.com/forum/viewtopic.php?t=10457)的[翻译](http://www.isf.com.tw/tech_article/kal_guide.html)。

![题图](http://www.curtpalme.com/images/728x90/chromapure_header_wide_modified640.jpg)
***本文由 [CurtPalme.com 家庭影院](http://www.curtpalme.com/)的编辑 [Kal](http://www.curtpalme.com/forum/profile.php?mode=viewprofile&u=3) 编写。***
***最近更新于 2017 年 3 月 1 日（Edits for clarity）***

***要获得本向导更新的通知，请查阅[帖子](http://www.curtpalme.com/forum/viewtopic.php?t=35322&watch=topic&start=0)并回复（需先[注册](http://www.curtpalme.com/forum/profile.php?mode=register)并[登录](http://www.curtpalme.com/forum/login.php)），或登记[接收新闻消息](http://www.curtpalme.com/MailingList.shtm)。***

*请勿再版、复制或创建本手册的 PDF 或 DOC 版本。而是简单链接到本页面（[原始页面](http://www.curtpalme.com/forum/viewtopic.php?t=35322)），让读者可以自行打印。这样所有人都有最新的版本。*

*All content (c) copyright 2013-2017 CurtPalme.com.*

---

## 这份手册适合我吗？

这份手册适合想要从任何电视或投影机上获得***绝对最佳***画面的家庭影院玩家。它会告诉你如何尽可能在任何显示器上获得最正确的色彩，不管里面用的是什么技术（等离子、LCD/LED、DLP、SXRD、LCOS、CRT 等）。哪怕是有 20 年历史的模拟显示器和最新的 4K 投影机或电视，都能在调校中获益。

![](http://www.curtpalme.com/images/RS56_129.gif)![](http://www.curtpalme.com/images/HCFR_TV3.gif)![](http://www.curtpalme.com/images/flattv.gif)![](http://www.curtpalme.com/images/HCFR_TV2.gif)![](http://www.curtpalme.com/images/Sony1100.gif)![](http://www.curtpalme.com/images/sonyt105.gif)

无需准备知识以及关于调校的理解。我们会解释它是什么、为什么重要，列出所需工具，如何获得，并且指引从头到尾的过程。

读下去，你会了解要在所有的电视或投影机上取得最佳图像质量，为何执行正确的调校是最重要的操作之一（如果不是唯一）。

希望对你有用！

Kal
[CurtPalme.com 家庭影院](http://www.curtpalme.com/)编辑
[TheElectricBrewery.com](http://www.theelectricbrewery.com/)创始人 …一步步做个自己的酿酒厂。

我最新的著作是一步一步做个自己的酿酒厂。现开放电子书下载：
[![](http://www.theelectricbrewery.com/images/728x90/guide.jpg)](http://www.theelectricbrewery.com/the-complete-guide-to-building-your-brewery)

## 这份手册和之前的调校手册有何不同？

我们之前的调校手册（[英](http://www.curtpalme.com/forum/viewtopic.php?t=10457)/[繁中](http://www.isf.com.tw/tech_article/kal_guide.html)）写于 2008 年，主要针对 CRT 投影机的调校。

而这份新版手册要面对任意的显示技术，它关注新的显示技术下的调校，比如数字投影机和平板电视，因为这些新型显示设备提供了更好控制，尤其是在伽马和色彩校正上。

想最大程度地利用这些新特性的优势，要用到更高级的 [ChromaPure 校准软件](http://www.curtpalme.com/ChromaPure.shtm)，因其更加适合今天的高级显示设备。 ChromaPure 软件相比以前的调校手册所用软件有以下优势：

* 内置了工作流程，更易使用、更符合直觉。
* 高级灰阶、伽马和色彩校正工具。
* 全面报告工具（以前的软件没有报告功能）。
* 出色的内置帮助：你可以在任一界面点击“帮助”按键来获取针对工作模块的详细信息、提示、指引以及步骤。
* 技术支持：ChromaPure 是商用软件，持续更新，生命期内提供支持。
* 更好支持校色仪，包括新的专业级色度计和光谱仪，以及在十余种显示类型上提高了精度。
* 支持信号发生器，包括 [AccuPel 信号发生器](http://www.curtpalme.com/ChromaPure_AccuPel.shtm)出来的 3D 信号。
* 连接了视频处理器后，比如 [Lumagen Radiance](http://www.curtpalme.com/Radiance.shtm) ，能够完全自动化进行校准。包括多达 4913 点（而不是仅仅 6 点）的色彩校正和大幅增加的精度。自动校准几乎无需用户输入，让任何很少训练或没有训练的人都能完全校准显示设备。只需设置几个简单选项，点击 Auto-Calibrate ，就去喝咖啡等待过程结束吧。在 10 分钟内，你的显示设备就完全校准到专业标准了。工具包都帮你做了，这份手册也用不着了。

近年来，我们一直说，ChromaPure 用不着手册。因为它已经易用、直觉，有内置的流程帮助新手。每个人工作方式不同，有人更希望有个手册。希望本文有用吧。

## 介绍

如果你已经在电视或投影机上花了不下 1000 刀，很可能你在认真考虑家庭影院。很多人不知道，一般来说，投影机和电视要让显示的视频信号正确呈现是需要校准的。要得到影院般的画面，最方便的方法之一，就是对显示设备进行专业校准。专业校准（需要专业设备）最重要的因素，就是灰阶、伽马和色彩校正。这些就是本文主题。

专业校准的主要缺点就是价格：通常单一电视需要 350~450 刀，一个复杂的家庭影院设置需要 1000 刀。物有所值，但所耗不菲。另一个缺点是，要达到最佳效果，随着设备变化、组件变旧，若是投影机，还有灯泡老化，都需要再次校准。数字投影机显示的色彩在其 1000~5000 个小时的灯泡寿命内会有显著的变化。对一个有数字投影的画质控来说，每 100~200 小时校准一次并不鲜见（尤其是新灯泡）。

好消息是，近年来设备价格迅速滑落、品质大幅提升，一般的家庭影院 DIY 玩家也负担的起校准了。人们在寻求以最小投入，自行校准显示器，得到比较好的结果。这份手册会在假定你完全不懂校准的情况下，带领你完成这些调校所需的步骤。很容易做，还可以获得 DIY 的成就感和经验。

我们会从校准显示设备的电平（亮度/对比度）开始。因为它是最重要，最容易的步骤。下面是一些可能好奇的附加信息。如果不感兴趣，跳过它，从 **What tools do I need?** 开始吧。

### 什么是视频电平校正？

视频校准的第一步也是最需要的步骤，就是调准电平。也就是白和黑的电平。白电平用**对比度/contrast**控制来调节，黑电平用**亮度/brightness**控制来调节。这个是视频调校中必须由人眼完成的部分。

正确的白电平意味着，显示设备产生足够的照度（也称作“亮度/luminance”）而无需妥协 100% 白和稍微弱一点的信号的区分度。当白和稍次白合并到一块无法区分，就称作“破碎的白/crushed whites”。比如下面的图片，由于对比度控制（白电平）设置的不正确，雪地中的细节丢失：

![](http://www.curtpalme.com/images/ChromaPureGuide_levels_crushed_whites.jpg)

正确的黑电平意味着，显示设备产生非常深邃暗淡的黑色，而不遮盖暗部细节。如果亮度控制设的过低（称作“破碎的黑/crushed blacks”），灰色会显示成黑，效果是丢失暗部信息。如果亮度控制设的过高（称作“拉高的黑/elevated blacks”），黑色会显示成灰，导致画面有洗白感。下图展示了这些：

![](http://www.curtpalme.com/images/ChromaPureGuide_levels_crushed_blacks.jpg)

当白电平（对比度）和黑电平（亮度）都正确设置了，显示设备会输出非常亮、包含丰富细节的极端场景和包含出色暗部细节的暗画面。

### 什么是灰阶校正？

灰阶校正是指调节显示设备的行为，确保从近黑（10% 视频）到全白（100% 视频），显示设备表现出尽可能接近正确灰色的层次，还没有引入其它不必要的颜色。灰色不能有轻微的偏红、偏蓝或偏绿。这要在色度计的帮助下完成。必须要用色度计，因为我们的眼睛作为颜色测量工具简直糟透了。

灰阶校正在不同亮度下，从非常黑（10%）到非常亮（100%），把灰色拉到标准白点。传统上标准白也被描述为 6500 开尔文色温或 6500K 。然而，在北美和欧洲，对显示设备精确白点更精准的描述是 D65 ，这是个严谨定义了的颜色。6500K 实际上描述了很多颜色，D65 只有一个。D65 大约是在北美中午时阳光的颜色。假定你在用的监视器在灰阶表达上非常准确，一个完美的灰阶看上去应该这样：

![](http://www.curtpalme.com/images/Chromapure_IRE.jpg)

不幸的是，大多显示设备在默认设置下，在暗部偏红，在亮部偏蓝。这时它的灰阶看上去更像这样：

![](http://www.curtpalme.com/images/Chromapure_IRE2.jpg)

### 什么是伽马校正？

伽马是描述源设备信号输入和你的显示设备信号输出之间关系的提法。它不是一对一的关系。伽马表达为一个数值，一般在 1.5 和 2.5 之间。

![](http://www.curtpalme.com/images/ChromapureGuide_gamma.gif)

![](http://www.curtpalme.com/images/ChromapureGuide_gamma_chart.gif)

在上图中你可以看到，如你所愿，不同的伽马值在信号输入和照度之间都有一一对应的关系，都开始于 0% 输入产生 0% 输出，结束于 100% 输入产生 100% 输出。然而，在输入和输出之间的细微关系中，一切都不是线性的。并且“伽马曲线”的细微本质是和伽马本身相关多变的。

显示设备的伽马若较低，随着信号输入的增加它的照度增加就更快。如果你观察 10% 输入处，会看到 2.8 伽马时的照度只有 2.1 伽马时照度的 20% 。这显然差异很大。随着输入上升，差异变得越发不显著，以至于显示设备在 80% 输入时 2.8 伽马的输出接近 2.1 伽马时的 86% ，这几乎无法察觉。

正因如此，伽马在图像上的主要效果就是暗部细节。如果伽马过低，你会得到极佳的暗部细节，但你的黑电平会被显著拉高，图像表现得像洗过（对比度糟糕）。如果你把伽马拉得太高，你会看到深邃、幽暗的黑，但丢失暗部细节。见下图：

![](http://www.curtpalme.com/images/ChromaPureGuide_gamma.jpg)

伽马的另一个效果是图像的_感知深度/perceived depth_。即使是常见的 2D 电视模拟的三维空间。显示设备的伽马过低会导致画面趋于扁平，缺乏深度。这问题很常见，显示器厂家为了改善整体照度，一般都把产品的伽马调试得略高。

### 什么是色彩校正？

色彩校正是显示校准的最后一步。色彩校正确保显示设备所用的调色板颜色（the raw colors），如内容创建者的期望，的精准呈现。

很多显示设备颜色不正，绿色太黄、红色偏橙，或是颜色过饱和。下面例子来自一个绿色过饱和的投影机，造成草地像是荧光照在上面的样子。

![](http://www.curtpalme.com/images/HCFR_RS1_comparison3.jpg)

正确的色彩校正要以灰阶校正为基础。除非灰阶首先是正确的，否则不可能有正确的色彩。

### 为什么我该校准灰阶、伽马和色彩？

校准灰阶、伽马和色彩能大幅增强你显示设备的能力，不仅正确地显示黑与白，还有之间的任何颜色。它也能增加对比度，让你的显示设备因工作在最佳状态下而延长寿命。

没有调校好的图像质量很糟糕，表现在颜色不正、缺乏暗部细节（暗部细节丢失）、对比度下降以及影像缺乏“冲击感”。画面没有吸引力、不真实。电影制作且预期播放在 D65 色温下，所以若你的电视正确调校到了 D65 ，你更接近看到内容制作者的意图。

一个常见的错误观念是，你可以经由标准的显示器控制，如色调、饱和度和对比度，来得到正确的灰阶和颜色。这是错的。这些控制不在我们所需的方向上影响灰阶或颜色。要完成灰阶校正，你需要调整从“刚不是黑”到 100% 白的各个亮度下红、绿、蓝的量。要调节颜色本身，你需要更进一步调节“纯”色。大部分高级电视和投影机提供灰阶控制的菜单，一些甚至有色彩控制。这些就是本手册中，我们要在校色仪和 ChromaPure 软件的帮助下要调整的控制项。

有人会试着或声称裸眼校准灰阶和颜色，但人眼在测量亮度和色彩上是很差的工具。结果通常离理想状态非常遥远。一些用过校色仪的人在经过多年练习后，可能裸眼达到相当好的结果，但那是他们有过多年的仪表经验。吊诡的是，都有仪表了，为什么不继续用呢？

### 为什么校准是必要的？

这是个非常好的问题，很多消费者都有（或该有）。回答那些视频调校上最常见的问题就是对它的最好回答。

#### 为什么我的电视不在出厂时就调校好？为什么我得自己或者花钱找人做这事呢？

很不幸，对于确认显示器是否符合或接受电视广播和电影工作室所用的色彩标准，厂商看似不感兴趣。事实上刚好相反！为了卖出更多电视，厂商一直试着用比竞争对手“更亮的蓝”和“更艳的红”。这跟洗衣粉厂家在产品中添加蓝色染料使其看似“更白”是一个道理。在充满不同品牌的展示间，电视厂商为了让他们的电视更能吸引消费者，一直在增加色彩。面对一面墙上相似的屏幕，消费者如何选择要买哪台呢？为什么你选择最亮的，或者颜色最艳的？这样对吗？***大错特错！***

你，消费者，需要了解的是，显示色彩只有<big>唯一</big>正确的方式：遵循工业界广泛认定用于标准画质（SD）以及高画质（HD）的色彩标准。其它方式就是错的。电影和电视节目都是遵循这些存在已久的工业色彩标准一丝不苟地制作。对于电视或投影机，要再现导演想呈现给观众的画面，就必须遵守这些标准。无论销售人员和生产厂家怎么说，任何扩展色域超过这些工业色彩标准的电视，显示的都是**不正确的颜色**！就这么简单。不用任何技巧：电视只有遵循和不遵循标准。在你下次买电视的时候要记得这一点。想知道更多关于厂商搞差电视和其他屏幕来愚弄我们的大脑好选择他们的产品，看 [Digital Video Essentials: HD Basics (Blu-ray)](http://www.amazon.com/exec/obidos/ASIN/B00ADJG56Q/curtpalmecrtp-20) 这个优秀测试碟前面几章的说明。

#### 我的电视有 6500K 色温或 THX 设置，所以用不着灰阶校正。我直接选这个就自动有完美校正了的电视。对吗？

很不幸，不对。没这么简单。在电视/投影机设置菜单中选择 6500K 色温或 THX 选项是走在正确方向的一步。感谢提供这个选项的厂商。不幸的是，这个选项在整个灰阶中很少有接近正确值的地方。它也没有考虑所用的其它设备（包括幕布），或电视或灯泡的老化与损耗。

这个画面来自一台价值 40000 美金的 Sony G90 投影机（很多人认为这是已有显示设备中最好的之一），灰阶设置为出厂缺省的 6500K ：

![](http://www.curtpalme.com/images/HCFR_G90_before.jpg)

现在这个是同一投影机在正确灰阶校正后：

![](http://www.curtpalme.com/images/HCFR_G90_after.jpg)

*来自坛友 Clarence（可以看到第一张照片没有的暗部细节）。摄于他的 Sony G90 。感谢 Clarence ！*

（关于 6500K 和正确的 D65 白点不是一回事，这是个很好的例子。如上面第一幅图，6500K 会有很绿或偏红的倾向。）

假定你在用的屏幕有个合理正确的灰阶，第二幅屏摄会比第一幅看上去好很多。注意第二幅里，Jennifer Aniston 的脸没有了红/蓝色，颜色更加生动的，对比度更好。图像更有层次。正确地灰阶校正后，图像更有“冲击感”，更自然。在没跳对比度的情况下，整幅画面更亮。正如之前提过的，Sony G90 是个专业级投影机，厂商建议零售价 40000 美金，即便如此，出厂默认的 6500K 偏离完美这么多！

正确的灰阶只能在亲眼比较过前后画面才能被真正意识到，屏摄是不够的，经过数码相机和另一个屏幕，丢失了很多细节信息。今天你可能发现投影机或电视看似还好，但在你实际看到它***真正***该有的效果之前，你不会知道你错过了多少。在完成灰阶校正之后，你将认为你在看一个完全不同的屏幕。

#### 我没有蓝光或高清。我的电视/投影机不兼容 1080p 。我只看普通 DVD 和电视节目。校正还有价值吗？

答案是一样的：**值得！**

适当的视频调校跟最新科技没有任何关系，如高清和蓝光。不管你的视频源使用什么图像分辨率（4K、1080p 蓝光/HDTV、480i DVD 或广播电视），适当调校将确保你看到的是系统最佳影像。

尽管今天（不管何时都应该用的）HDMI 线缆传输的高清内容，标清内容还是会在正确的灰阶、颜色校正中获得很大收益。

视频调校在电视刚成熟时就出现了，不是什么新概念。随着新科技和内容的涌现，它也会继续有用下去。只要有电影和电视在的地方，调校总是需要的。

对灰阶校正和色彩校正有兴趣了吗？开始了解下吧！比你想的要简单！

## 我需要什么工具？

你会需要一些东西来调校你的投影仪/电视：

* **<big>视频调校软件</big>**

  我们为此推荐并以折扣价发售 [ChromaPure 软件](http://www.curtpalme.com/ChromaPure.shtm)。它很易用也很管事。也有[带色度计和测试碟的套装](http://www.curtpalme.com/ChromaPure.shtm)。

  [![](http://www.curtpalme.com/images/728x90/ChromaPure.jpg)](http://www.curtpalme.com/ChromaPure.shtm)
  [![](http://www.curtpalme.com/images/x-click-butcc.gif)](http://www.curtpalme.com/ChromaPure.shtm)

* **<big>色度计</big>**

  需要个仪表来测量光度和色度。参考 [FAQ：哪个色度计适合我？](http://www.curtpalme.com/forum/viewtopic.php?t=11436) 中不同流行款的比较。本手册中我们用的是 [X-Rite i1 Display Pro](http://www.amazon.com/gp/product/B0055MBQOW/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B0055MBQOW&linkCode=as2&tag=curtpalmecrtp-20)（有时称作“Display 3”）。尽管 ChromaPure 支持很多不同色度计，这个是现有最合算的。有个增强版本叫做 [Display 3 PRO](http://www.curtpalme.com/ChromaPure_EyeOneDisplay3.shtm) 也可以，精度更高，有 10 种屏幕类型。这个是我们自己用来调校[个人家庭影院](http://www.curtpalme.com/forum/viewtopic.php?t=31098)的。

  [![](http://www.curtpalme.com/images/display3retail.gif)](http://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&linkCode=ur2&pageMinusResults=1&suo=1387161229571&tag=curtpalmecrtp-20&url=search-alias%3Daps#/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=i1display%20pro&sprefix=i1dis%2Caps&rh=i%3Aaps%2Ck%3Ai1display%20pro&sepatfbtf=true&tc=1387161230647)
  [![](http://www.curtpalme.com/images/buy_from_amazoncom200.gif)](http://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&linkCode=ur2&pageMinusResults=1&suo=1387161229571&tag=curtpalmecrtp-20&url=search-alias%3Daps#/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=i1display%20pro&sprefix=i1dis%2Caps&rh=i%3Aaps%2Ck%3Ai1display%20pro&sepatfbtf=true&tc=1387161230647)
  这里也有：[Amazon.ca](http://www.amazon.ca/s/?_encoding=UTF8&camp=15121&creative=390961&field-keywords=i1display%20pro&linkCode=ur2&tag=curtpalme-20&url=search-alias%3Daps)

* **<big>有特定图案的测试盘</big>**

  你需要一个有多种测试图案的测试碟，包含 0% 到 100% 测试图案。这里会用到[专为 ChromaPure 制作的碟片](http://www.curtpalme.com/ChromaPure_Calibration_Disc.shtm)。在特定的 [ChromaPure/色度计包](http://www.curtpalme.com/ChromaPure.shtm)里会免费包含。手册会告诉你在碟片里具体怎么找要用的图案。其他测试碟，比如 [Digital Video Essentials: HD Basics disc](http://www.amazon.com/exec/obidos/ASIN/B00ADJG56Q/curtpalmecrtp-20) ，[Digital Video Essentials（标准 DVD 版）](http://www.amazon.com/exec/obidos/ASIN/B00005PJ70/curtpalmecrtp-20) 或 [Avia II](http://www.amazon.com/exec/obidos/ASIN/B000X4NJNS/curtpalmecrtp-20) 也能用，但碟片菜单不同，所以你必须自己找到具体图案。我们不推荐使用原始 Avia DVD 作为灰阶图案，因其已被确认有误。

  [![](http://www.curtpalme.com/images/ChromaPure_disc_375.jpg)](http://www.curtpalme.com/ChromaPure_Calibration_Disc.shtm)
  
  [![](http://www.curtpalme.com/images/x-click-butcc.gif)](http://www.curtpalme.com/ChromaPure_Calibration_Disc.shtm)

* **<big>三脚架</big>**

  对于投影机/幕布的基础设置，为让传感器固定在屏幕前，你需要个三脚架。直视背投电视就用不着了，因为总是可以直接接触测量的。对直视型的屏幕，使用三脚架也是个不错的练习。确保三脚架至少可以伸长到幕布中央。相对于三脚架，色度计都又小又轻。Display 3 色度计自带三脚架固定座。

  [![](http://www.curtpalme.com/images/HCFR_item3.gif)](http://www.amazon.com/mn/search?_encoding=UTF8&field-keywords=camera%20tripod&url=search-alias%3Daps&_encoding=UTF8&tag=curtpalmecrtp-20&linkCode=ur2&camp=1789&creative=390957)
  
  [![](http://www.curtpalme.com/images/buy_from_amazoncom155.gif)](http://www.amazon.com/mn/search?_encoding=UTF8&field-keywords=camera%20tripod&url=search-alias%3Daps&_encoding=UTF8&tag=curtpalmecrtp-20&linkCode=ur2&camp=1789&creative=390957)

* **<big>运行软件的 Windows PC</big>**

  推荐使用笔记本，但任何运行 Microsoft Windows 7/8/10 的电脑都可以。电脑的速度和容量都不重要。
  
  [![](http://www.curtpalme.com/images/HCFR_item4.gif)](http://www.amazon.com/gp/redirect.html?ie=UTF8&location=http%3A%2F%2Fwww.amazon.com%2Fb%3Fie%3DUTF8%26node%3D565108%26pf%5Frd%5Fm%3DATVPDKIKX0DER%26pf%5Frd%5Fs%3Dgp-left-1%26pf%5Frd%5Fr%3D1C1HZ6S6F5SVWJ929RRK%26pf%5Frd%5Ft%3D101%26pf%5Frd%5Fp%3D382994501%26pf%5Frd%5Fi%3D541966&tag=curtpalmecrtp-20&linkCode=ur2&camp=1789&creative=9325)
  
  [![](http://www.curtpalme.com/images/buy_from_amazoncom255.gif)](http://www.amazon.com/gp/redirect.html?ie=UTF8&location=http%3A%2F%2Fwww.amazon.com%2Fb%3Fie%3DUTF8%26node%3D565108%26pf%5Frd%5Fm%3DATVPDKIKX0DER%26pf%5Frd%5Fs%3Dgp-left-1%26pf%5Frd%5Fr%3D1C1HZ6S6F5SVWJ929RRK%26pf%5Frd%5Ft%3D101%26pf%5Frd%5Fp%3D382994501%26pf%5Frd%5Fi%3D541966&tag=curtpalmecrtp-20&linkCode=ur2&camp=1789&creative=9325)

  ***注：****Mac 也可以。Mac 用户可以在 Parallels 或 Fusion 下运行 PC 软件。*

* **<big>一些效果好的电影，用于测试最终效果</big>**

  你会希望展示下你新校准的屏幕。在我们的[参考级蓝光作品鉴](http://www.curtpalme.com/forum/viewtopic.php?t=9237)中找些 4K 或 1080p（全高清）蓝光碟就很好。里面有对家庭影院的音画质量来说绝对是最好的电影。每个电影集都得有这里的一组电影。你可以从这里的一些五星评价的影片开始…

  |[![](http://www.curtpalme.com/images/HCFR_item5_1new.gif)](http://www.amazon.com/exec/obidos/ASIN/B0083SBJXS/curtpalmecrtp-20)|[![](http://www.curtpalme.com/images/HCFR_item5_2new.gif)](http://www.amazon.com/exec/obidos/ASIN/B001KVZ6G6/curtpalmecrtp-20)|[![](http://www.curtpalme.com/images/HCFR_item5_3new.gif)](http://www.amazon.com/exec/obidos/ASIN/B00E8S2JZ4/curtpalmecrtp-20)|
  |:--:|:--:|:--:|
  |[![](http://www.curtpalme.com/images/buy_from_amazoncom160.gif)](http://www.amazon.com/exec/obidos/ASIN/B0083SBJXS/curtpalmecrtp-20)|[![](http://www.curtpalme.com/images/buy_from_amazoncom160.gif)](http://www.amazon.com/exec/obidos/ASIN/B001KVZ6G6/curtpalmecrtp-20)|[![](http://www.curtpalme.com/images/buy_from_amazoncom160.gif)](http://www.amazon.com/exec/obidos/ASIN/B00E8S2JZ4/curtpalmecrtp-20)|
  
  |[![](http://www.curtpalme.com/images/HCFR_item5_4new.gif)](http://www.amazon.com/exec/obidos/ASIN/B007REV4YI/curtpalmecrtp-20)|[![](http://www.curtpalme.com/images/HCFR_item5_5new.gif)](http://www.amazon.com/exec/obidos/ASIN/B00AZKCU7G/curtpalmecrtp-20)|[![](http://www.curtpalme.com/images/HCFR_item5_6new.gif)](http://www.amazon.com/exec/obidos/ASIN/B007STBUIW/curtpalmecrtp-20)|
  |:--:|:--:|:--:|
  |[![](http://www.curtpalme.com/images/buy_from_amazoncom160.gif)](http://www.amazon.com/exec/obidos/ASIN/B007REV4YI/curtpalmecrtp-20)|[![](http://www.curtpalme.com/images/buy_from_amazoncom160.gif)](http://www.amazon.com/exec/obidos/ASIN/B00AZKCU7G/curtpalmecrtp-20)|[![](http://www.curtpalme.com/images/buy_from_amazoncom160.gif)](http://www.amazon.com/exec/obidos/ASIN/B007STBUIW/curtpalmecrtp-20)|
  
  <big>查看[完整列表](http://www.curtpalme.com/forum/viewtopic.php?t=9237)</big>
  
  ***从我们的链接购买可以支持我们的网站，无需额外费用。感谢你！***

## 要用到的屏幕设置项

实际上所有屏幕都有这些必要的设置项，才能至少做白平衡和灰阶的校准。在你的投影机或电视里，我们要调整十个设置，才能完全校准屏幕。找到并熟悉它们是非常重要的。

* **亮度/Brightness：**这项用来调节黑电平。亮度设置得过低导致暗部细节丢失，变成黑色（称为“黑碎了/black crush”）。亮度设置的过高导致黑色看似灰色。同时，亮度影响所有颜色。
* **对比度/Contrast：**这项用来调节峰值照度。对比度设置过低导致画面昏暗。对比度设置过高导致亮部细节丢失，变成白色（称作“截断白/white clipping”或“碎裂白/white crush”）。同时，对比度影响所有颜色。
* **色度/Color**[^color]**：**所有屏幕都有个主色度控制项。[^allhave]如果你的屏幕没有色彩管理系统，可以用它来调节颜色。
* **色调/Hue/Tint：**所有屏幕都有个主色调控制项。[^allhave]如果你的屏幕没有色彩管理系统，可以用它来调节颜色。
* **锐度/Sharpness：**所有屏幕都有个锐度控制项。[^allhave]只有模拟设备，比如 CRT 显示器，才真正需要这个控制项。但数字设备也有它。
* **图像模式/Picture Mode：**大多数屏幕都有个图像模式。作为全局的预设选项，它选择众多图像参数的大范围。选择正确的图像模式是尤其重要的。
* **低段原色/RGB LowEnd：**这项用来分别调节在灰阶暗部的红、绿或是蓝的量。可把它想成每种颜色单独的亮度控制。厂商都使用不同的命名，如‘Cut’、‘Cutoff’与‘Bias’是最常用的。这份手册里使用低段原色以避免混淆。
* **高段原色/RGB HighEnd：**这项用来分别调节在黑白渐变内亮部的红、绿或是蓝的量。可把它想成每种颜色单独的对比度控制。厂商都使用不同的命名，如‘Drive’和‘Gain’是最常用的。这份手册里使用高段原色以避免混淆。
* **伽马预设/Gamma Preset或伽马控制/Gamma controls：**多数屏幕没有伽马预设，也有很多没有完整的 10 点伽马控制。然而在取得屏幕的良好伽马曲线上，此项没什么价值。
* **色彩管理系统/Color Management System：**在新显示器上越发流行了。全功能的色彩管理系统可以让用于在三个维度上调节颜色，无论主次。分别是色调/Hue，饱和度/Saturation 和亮度/Luminance 。

所有屏幕都有亮度和对比度调节。如果你的投影机或电视有红、绿和蓝的低段原色和高段原色调节，你也能校准灰阶。

鉴于不同厂商给低段原色和高段原色使用不同名称，查阅你的用户手册中关于“灰阶/grayscale”、“白平衡/white balance”或“色温/color temperature”调节的段落，看看你的屏幕上它什么。

这两项上，一般使用的更流行的名字有：

**低段原色：**Bias、Offset、Cuts、Cutoff、Sub-brightness、RGB brightness
**高段原色：**Drive、Gain、Sub-contrast、RGB contrast

这就是信息部分。开始调校吧！

[^color]: 译者注：我猜是指饱和度 saturation 。
[^allhave]: 译者注：All displays have a XXX conntrol. 真的是所有屏幕都有吗。存疑。

## 第一部分：校准前设置

### 步骤1.1：准备测试图案源

本手册中，我们使用 [ChromaPure 校准碟](http://www.curtpalme.com/ChromaPure_Calibration_Disc.shtm)作为测试图案源。校准过程中所需要用到的图案里面都有，也有一些其它经验证有用的。

![](http://www.curtpalme.com/images/ChromaPure_disc_menu.jpg)

***提示：****碟片上的_基本校准_测试图案包含了很多其它使用上的提示和指引。在看这些测试图案的时候，直接按蓝光机遥控上的菜单/Menu键即可查看额外帮助。*

你会被要求在校准过程中的每个阶段手动选择测试图案。如果你要使用这张碟片（或其它的 DVD 、蓝光），无需安装，你可以直接略过去看步骤1.2.

若你希望领略 ChromaPure 的内部测试图案的优势，就需要一些前期安装了。带有 HDMI 输出接口的电脑都可以做到。

***注：****即使你用 ChromaPure 的内部测试图案，你也需要校准碟来设置亮度、对比度和锐度。这些只能根据肉眼来调节。*

* 1.1.1. 启动 ChromaPure 软件

  ![](http://www.curtpalme.com/images/gui_new.png)

  ***注：****ChromaPure 提供三种用户界面。其中两种在左下方有横穿整个底部的导航条。然而缺省用户界面是一个全页的平板界面。本手册后面都用这个界面。*

* 1.1.2. 点击 **Pre-Calibration** 标题下方的 **Initial Setup** 图标，会出现 **Initial Setup** 窗口：

  ![](http://www.curtpalme.com/images/signalGenerator_new.png)

* 1.1.3. 在 Signal Generators 区选择 **ChromaPure Built-in Signal Generator**。
* 1.1.4. 选择要用的 **Pattern Size（图案尺寸）**和 **Intensity（烈度）**。如果你在校准一个等离子、OLED 或 CRT 的屏幕，**Pattern Size（图案尺寸）**选择“Standard Windows”。其它类型的，使用“Fields”。**Intensity（烈度）**推荐 75% 色彩和 100% 白。**Color Format（颜色格式）** 和 **Resolution（分辨率）**由电脑显卡设置。
* 1.1.5. 在 PC 上插入 HDMI 线缆，连接你的显示设备。
* 1.1.6. 使用 Windows 扩展桌面功能，同时激活两个监视器。你电脑的上面显示 ChromaPure ，你要校准的显示测试图案。拖动测试图案到主显示器上，右击选择“Maximize（最大化）”。

  在 ChromaPure 中选择任何色彩或灰阶级别会自动显示相应的测试图案。

### 步骤1.2：校准色度计/初始设置

在你用视频校准软件做任何动作之前，你必须校准色度计，这样它才能测量色度数据并传输到软件上。

* 1.2.1. 你得在设置信号发生器的同一个页面里安装色度计，我们在上一步已经看到过。

  ![](http://www.curtpalme.com/images/gui2_new.png)

* 1.2.2. 将 Display 3 色度计插入可用的 USB 端口。（该仪表使用了 Windows 自带的 HID 框架，所以无需安装驱动）
* 1.2.3. 在下拉列表里选择该仪表。
* 1.2.4. 选择希望的操作模式，再点击 **Connect（连接）**。ChromaPure 会初始化跟色度计的通讯校验，完成时弹出窗口写着“You are now ready to calibrate your display（你现在准备好校准显示器了）”。点击 **Ok** 关闭该窗口。点击 **Initial Setup** 标签的 **X** ，或点击 ChromaPure 右上角的 Home 按钮返回主菜单。

***注：***

- *如果你有个 Display 3 色度计，会出现两个操作模式（_Standard, Plasma, CRT_和_Front Projection Lens_）。如果你有个 Display 3 PRO ，会出现很多的操作模式，其中的每一种都为了更好的精度单独针对特定显示设备类型校准过，比如三星、索尼和 LG 的 LCD、LED 屏幕（[完整列表](http://www.curtpalme.com/ChromaPure_EyeOneDisplay3.shtm)）。*

- *如果你有个 Display 3 或 Display 3 PRO 色度计的新一些的 Rev. B 版本，会出现个 ***Scan Rate*** *。三个选项是：60Hz、50Hz 和 24Hz 。在北美用 60Hz ，除非你知道显示器设成了 24Hz 。如果不确定就用 60Hz 吧。欧洲系统用 50Hz 。*

开始前，有些重要的规则：

* 对于前投的设置，把房间尽量弄暗，最好完全漆黑（就像你在看场电影），确保没有任何散射光照到幕布上。包括来自笔记本或电脑显示器的光。把笔记本或电脑显示器亮度调低，背对幕布。
* 还是前投，色度计要安装在三脚架上，传感器对着幕布中心（传感器扩散件移出光路），距离1 或 2 码[^dist]，带点角度，以免测量自己的影子。
* 校准前，显示设备热机 30 分钟，它会要点时间来稳定下来。
* 若你在校准等离子电视，把色度计用三脚架安装在屏幕前方 1 码左右会是极佳的操作。这能降低等离子屏幕的热量对传感器的影响。

针对显示设备的类型，选择正确的测试图案也很重要。如果你在校准等离子、OLED 或 CRT 屏幕，就用窗口测试图案来校准灰阶、伽马和色彩。窗口测试图案只填充屏幕中间区域，就像这样：

![](http://www.curtpalme.com/images/ChromaPureGuide_window.jpg)

对于 LCD 和前投来说，用全场测试图案。全场测试图案填充整个屏幕，就像这样：

![](http://www.curtpalme.com/images/ChromaPureGuide_fullfield.jpg)

[^dist]: 译者注：1 码 = 0.9144 米。0.9m~2m 。距离不严谨限定。

### 步骤1.3：前校准测量

尽管前校准测量不是严格必须的，它会告诉你个大概，你的屏幕距离工业标准有多远。如果你想最后做个校准前后的性能对比报告，它就是必须的了。

在大多的 ChromaPure 模块里，顶部都会有这些测量工具的工具栏：

![](http://www.curtpalme.com/images/toolbar_new.jpg)

* ![](http://www.curtpalme.com/images/toolbar_m_new.jpg) 单一测量
* ![](http://www.curtpalme.com/images/toolbar_c_new.jpg) 连续测量
* ![](http://www.curtpalme.com/images/toolbar_a_new.jpg) 测量本模块的全部颜色
* ![](http://www.curtpalme.com/images/toolbar_x_new.jpg) 停止测量循环
* ![](http://www.curtpalme.com/images/toolbar_questionmark_new.jpg) 帮助（上下文相关）
* ![](http://www.curtpalme.com/images/toolbar_quickreport_new.jpg) 快速报告
* ![](http://www.curtpalme.com/images/toolbar_moduleoptions_new.jpg) 模块选项
* ![](http://www.curtpalme.com/images/toolbar_applicationoptions_new.jpg) 程序选项

如果你在用一个信号发生器，点击 **A** 可以一次性测量模块内全部颜色。如果你在用一个 DVD 或蓝光碟，你应该点击 **M** ，并且在再次点击 **M** 之前调整碟片到下个测试图案。

要用一个模块执行一组自定义的测试，你总可以只用目标颜色，再用 **M** 来做每个单独的测量。如果是连续测量（并且在用信号发生器），你可以选择列表第一项，再点击 **A** 。

***注：****在测量一个模块内的任何色彩部分之前，你都必须先测量参考白。在预校准、校准和后校准，都有个参考白值。所以在一个模块内，你测量的参考白，会传递到同类的其它模块。*

* 1.3.1. 返回 ChromaPure 的主窗口，点击 **Pre-Calibration/前校准** 标题下方的 **Grayscale/灰阶** 图标。会显示出 **Pre-Calibration Grayscale** 模块：

  ![](http://www.curtpalme.com/images/precalGrayscale_new.png)
  
* 1.3.2. 显示 100% 白的测试图案，在 ChromaPure 校准碟的：*Main Menu/主菜单 -> Grayscale/灰阶 -> Full Field (or 6.5% Window)/全场（或 6.5% 窗口）-> 100% Stimulus/100% 激励*。如果你在用 ChromaPure 内置的测试图案，它会自动显示。摆好传感器，点击 **M**（测量）。

  如果你在使用信号发生器，你可以点击 **A**（测量所有），会测量所有的灰阶等级。

  100% 级的数据会显示出来，包括 xyY、CIE94（$\Delta E$）和 CCT（色温）。伽马和输出数据只在所有级都测完后出现。对于 0% 级，你可以忽略除了 Y 值（亮度）的全部数据，要用来计算对比系数。ChromaPure 会自动跳转到下一级别，准备下次读数。
  
  ***注：****$\Delta E$（或 dE、delta E）对视频校准来说是个无意义的值。它是颜色误差的量度，所以对于测量的颜色，$\Delta E$越低越好。$\Delta E$可以用在灰阶和颜色校准上。有很多的$\Delta E$公式，你可以在_选项_模块里选择。然而我们感觉，在大多数的校准任务中，默认的 CIE94 是最好的。*

* 1.3.3. 重复上面的过程，显示内容调高 10% 然后点击 **M**（测量），直到灰阶的所有级别都测量完毕。伽马数据会显示出来。结束后，模块看上去就是这样：

  ![](http://www.curtpalme.com/images/precalGrayscale-data_new.png)
  
  可以看见在上例中，平均$\Delta E$（误差）是 4.32 ，图中的 RGB 值不平衡。灰阶校正的目标是尽可能让从 5% 到 100% 的这些 RGB 值尽量平衡，且平均$\Delta E$不超过 2.0 。

* 1.3.4. 返回 ChromaPure 主窗口，点击 **Pre-Calibration/前校准** 标题下方的 **Color Gamut/色域** 图标。会显示出 **Pre-Calibration Color Gamut** 模块：

  ![](http://www.curtpalme.com/images/precalGamut_new.png)

* 1.3.5. 显示 100% 白的测试图案，在 ChromaPure 校准碟的：*Main Menu -> Adv. Color Management -> Full Field Amp/100%S (or 6.5% Window Amp/100%S) -> White Sweep -> 100% White*。点击 **M**（测量）。
  
  白色的信息会在上面的数据表中出现，CIE 图中会出现一个色点，颜色选择会调整到红色。

* 1.3.6. 显示 75% 红的测试图案，在 ChromaPure 校准碟的：*Main Menu -> Adv. Color Management -> Full Field Amp/100%S (or 6.5% Window Amp/100%S) -> Red Sweep -> 75% Red*。点击 **M**（测量）。
  
  红色的信息会在上面的数据表中出现，CIE 图中会出现一个色点，亮度图和$\Delta E$图中都会出现一个条，颜色选择会调整到绿色。

* 1.3.7. 重复上述过程，直到所有主色和副色都测量完成。（白、红、绿、蓝、黄、青和洋红[^magenta]）。

  色域包括两个子模块。饱和度和颜色校验。如果你选择测量全部，所有颜色都会测量。要评估你的显示设备在真实条件下的表现，采集这些颜色就很重要了。

  ![](http://www.curtpalme.com/images/Saturationssubmodule_new.png)
  饱和度子模块

  ![](http://www.curtpalme.com/images/ColorCheckersubmodule_new.png)
  颜色校验子模块

[^magenta]: 译者注：或品红，接近紫色

## 第二部分：校准显示

### 步骤2.1：设置正确的画面模式

如果你的显示设备（像大多数一样）提供可选的画面模式，那么在校准前给它选择一个正确的值就很重要了。有些画面模式很精准，只需要很少的调校。其它画面模式就真心不怎么样了，和工业标准相去甚远，在此基础上根本无法完全校准。

这里是一些实际使用的最佳画面模式的例子：

* Panasonic 等离子：Custom/自定义
* Samsung 平板电视：Movie/电影
* Pioneer 标准等离子：Movie/电影
* Pioneer 精品等离子：Pure/纯净
* JVC 投影机：THX 或 Standard/标准
* Sony 投影机：User/用户
* Epson 投影机：Natural/自然 或 THX

如果你不知道选择哪种画面模式，最好办法是对每个模式都运行一下 **Pre-Calibration Grayscale** 模块。然后选择结果里平均灰阶$\Delta E$最小，且伽马最接近 2.22 的。

### 步骤2.2：视频电平校正

要正确设置黑电平，你只需要个好的校准 DVD 或蓝光碟。设置白电平，会看到，就稍微复杂一点。

#### 步骤2.2.1：校准黑电平

* 2.2.1.1 显示亮度（或黑 PLUGE）测试图案。在 ChromaPure 校准碟的：*Main Menu -> Basic Calibration -> Brightness*。

  ![](http://www.curtpalme.com/images/ChromaPureGuide_Brightness.jpg)

* 2.2.1.2. 把显示设备的亮度调到最大。
* 2.2.1.3. 这种设置下，所有的“Below Black（比黑低）”和“Above Black（比黑高）”竖条都能看到。
* 2.2.1.4. 逐渐调低显示亮度，直到“Below Black（比黑低）”刚刚看不见，而“Above Black（比黑高）”都还能看见。如果“Below Black（比黑低）”竖条还能看见，亮度设的就太高。如果“Above Black（比黑高）”都看不见了，亮度设的就太低了。两种情况最终折衷到前面看到的那幅图片：

  ![](http://www.curtpalme.com/images/ChromaPureGuide_levels_crushed_blacks.jpg)

#### 步骤2.2.2：校准白电平

* 2.2.2.1. 显示对比（或白 PLUGE）测试图案。在 ChromaPure 校准碟的：*Main Menu -> Basic Calibration -> Contrast*。

  ![](http://www.curtpalme.com/images/ChromaPureGuide_Contrast.jpg)

* 2.2.2.2. 把对比度设成可调范围的中间值，在看到至少一个“Above Video White”竖条的条件下，逐渐尽可能调高对比度。保持“Below Video White”竖条都能看见。

  当对比度设得过高，会导致在白背景中的“Above Video White/亮过白”和“Below Video White/弱于白”信息看不见。这称为“截断”或“碎裂白”。如果发生了这种情况，你就像在前面的这幅图展示的一样，无法看到视频级别上高端的细节：
  
  ![](http://www.curtpalme.com/images/ChromaPureGuide_levels_crushed_whites.jpg)
  
  ***注：****设置黑电平时，我们会想要所有的“暗过黑”都看不见。在这里你可能也想调整白电平，让所有的“亮过白”都消失。这是不对的。给你的显示设备输出范围上留出一些顶部空间来显示“亮过白”很有用，因为偶尔会有这个范围的内容。*

* 2.2.2.3. 启动 ChromaPure 软件，如果你还没有初始化色度计，初始化一下（见步骤1.2）：

  ![](http://www.curtpalme.com/images/gui_new.png)

* 2.2.2.4. 回到 ChromaPure 主窗口，点击 **Tools/工具** 标题下的 **Raw Data** 图标。

  **Raw Data** 模块会出现：
  
  ![](http://www.curtpalme.com/images/rawData_new.png)

* 2.2.2.5. 显示 100% 白测试图案。在 ChromaPure 校准碟的：*Main Menu -> Adv. Color Management -> Full Field Amp/100%S (or 6.5% Window Amp/100%S) -> White Sweep -> 100% White*。

* 2.2.2.6. 点击 **C**（连续测量）。

  屏幕顶部的 x、y 和 Y 区域会出现数值。现在我们只关注 Y（亮度）值。

* 2.2.2.7. 调节显示对比度，直到量到了输出的参考值。前投设备是 48 $cd/m^2$（或 14 ft-L），平板监视器是 120 $cd/m^2$（或 35 ft-L）。

* 2.2.2.8. 完成后，点击 **Stop** 。

  ***提示：****用另一个单独的照度调节选项总是好过调节对比度。比如，很多前置投影机有手动光圈，LCD 显示器有背光控制。两者都专门用于调节整体照度。*

* 2.2.2.9. 再次显示对比（或白 PLUGE）测试图案。在 ChromaPure 校准碟的：*Main Menu -> Basic Calibration -> Contrast*。

  确认参考输出电平不会导致 clip white（在白背景中的“Above Video White/亮过白”和“Below Video White/弱于白”信息看不见）。你应该还能看到“Above Video White/亮过白”和“Below Video White/弱于白”的竖条。如果参考电平导致显示画面 clip 了，就稍微调低对比度，到能够看见竖条的最高值。
  
  无论何时，只要参考白输出和 clip 有冲突，一直选择那些没有 clip 的。

* 2.2.2.10. 回到 ChromaPure 主窗口，点击 **Calibration/校准** 标题下的 **White Balance/白平衡** 图标。

  白平衡模块会出现：
  
  ![](http://www.curtpalme.com/images/whiteBalance_new.png)

* 2.2.2.11. 再次显示 100% 白测试图案。在 ChromaPure 校准碟的：*Main Menu -> Adv. Color Management -> Full Field Amp/100%S (or 6.5% Window Amp/100%S) -> White Sweep -> 100% White*。

* 2.2.2.12. 点击 **C**（连续测量）。

* 2.2.2.13. 调节显示设备的高段原色，让 RGB 平衡。$\Delta E$（或 dE、delta E）数值应该不超过 2.0 。

  如果你在当前设置下无法达成白平衡，你可能必须调低对比度。在照度和良好白平衡间，最佳的折衷方案是个人喜好。然而，为了有足够的照度（按照 2.2.2.7 节的推荐），也许接收点白平衡的误差更好一些。不能让$\Delta E$上升到大于 4.0 。
  
  当你校准了白电平后，你的显示设备应该：
  
  * 没有截断白或碎裂白的征兆（亮部细节良好）。
  * 在 100% 处表现参考白。
  * 在 100% 处表现良好的白平衡。
  
  记住，你可以对照度和白平衡妥协，但绝不要让显示设备过亮产生截断白。

### 步骤2.3：正确调节锐度

要把锐度调对，目标是最大限度展示真实细节，而不要产生误导，忠实于原始画面。

* 2.3.1. 显示锐度测试图案。在 ChromaPure 校准碟的：*Main Menu -> Basic Calibration -> Sharpness*。这个图案在相对较亮的背景上有横竖方向的暗色的线。

  ![](http://www.curtpalme.com/images/ChromaPureGuide_Sharpness.jpg)

* 2.3.2. 靠近屏幕，要把测试图案看得非常清楚。
* 2.3.3. 把锐度设置尽量调高，但别在横竖线的周围产生可见的轮廓或光晕。一般这会需要把锐度设置调的相当低甚至完全关闭。

### 步骤2.4：灰阶校正

电平设好了，现在你可以进一步校准灰阶。确保 ChromaPure 在运行且传感器已经初始化。

* 2.4.1. 回到 ChromaPure 主窗口，点击 Calibration/校准 标题下的 White Balance/白平衡 图标。
* 2.4.2. 白平衡模块会出现：

  ![](http://www.curtpalme.com/images/whiteBalance2_new.png)

* 2.4.3. 显示 80% 测试图案。在 ChromaPure 校准碟的：*Main Menu -> White Balance -> Full Field (or 6.5% Window) -> 80%*。点击 **C**（连续测量）。

  这 80% 点的实时白平衡信息会出现。

* 2.4.4. 调节你显示设备的高段原色，直到软件界面上显示的 RGB 值几乎相等，同时$\Delta E$低于 2.0 。

* 2.4.5. 当 80% 调到了理想结果，显示 20% 测试图案，并再次做这个过程。这次调整你显示设备的低段原色。20% 测试图案在 ChromaPure 校准碟的：*Main Menu -> White Balance -> Full Field (or 6.5% Window) -> 20%*。操作播放器直接下一节也可以。

  ***注：****通过调节高段原色和低段原色来校准灰阶时，最好只调整红和蓝，保持绿色为默认值。*

* 2.4.6. 在 20% 和 80% 之间来回转，直到他们同时达成良好的 RGB 平衡，并且$\Delta E$低于 2.0 。这可能需要来回测量好几次。在 ChromaPure 校准碟上跳到下一节会无尽循环反复播放 80% 和 20% 。

  ***提示：****一些显示设备没有标准高段原色和低段原色的设置，而是提供在 10 个点的灰阶调整。如果你有这种显示器，我们推荐你如上来回调整 80% 和 20% 两点，因为这几乎达成了 90% 的结果。然后用这 10 点系统来微调特定问题点。（比如：如果你按照下面的 2.4.8 提到的内容完全完成后发现 10% 点掉下去了，就再来一轮 10% 测试图案，单独调整 10% 的点。）*

* 2.4.7. 回到 ChromaPure 主窗口，点击 **Post-Calibration/后校准** 标题下的 **Grayscale/灰阶** 图标。

  后校准灰阶模块会出现：

  ![](http://www.curtpalme.com/images/postCalGrayscale-data_new.png)

* 2.4.8. 像 **Pre-Calibration Grayscale/前校准灰阶** 模块一样，完整测量一遍。
* 2.4.9. 误差（$\Delta E$）会像前面的图一样在 CIE94 中显示。如果所有的都低于 2.0 ，你就已经完成了。如果它们没有，就做必要的关键点调节，尽可能降低误差。

### 步骤2.5：伽马校正

不像灰阶以及颜色校正，伽马校正碍于缺乏控制项。大多厂商不提供专门的伽马调整项。显示设备上的不同图像模式一般都会有特定的伽马曲线。有些显示器会提供一组伽马预设的选择能力。很少显示设备提供全功能 10 点伽马调整功能。一些外部视频处理器，比如 [Lumagen Radiance](http://www.curtpalme.com/Radiance.shtm) 系列，提供 10~20 点甚至更多。

***提示：****我们要一个什么样的伽马曲线？绝大多数用户的伽马曲线应在 40%~90% 的画面测得大约 2.3 。低于 40~90% 的画面，伽马修正量应连续增加，在 10% 起点的伽马值应在 2.1 左右。（伽马修正值越低，就要用越多的伽马修正。）这样的伽马曲线，在家庭影院中的高对比度的投影机上和生活空间中光照良好的平板显示器上，都能表现出色的结果。*

如果你的显示设备只有画面模式匹配的不同伽马值，或只有几种伽马预设值可以选择，就选平均值解决 2.22 的。如果你的显示设备或视频处理器（比如 [Lumagen Radiance](http://www.curtpalme.com/Radiance.shtm) ）提供一个 10 点（或更多）伽马控制，就弄出上述的曲线来。下面的内容假定你有个全 10 点的伽马调整选项。

* 2.5.1. 回到 ChromaPure 主窗口，点击 **Calibration/校准** 标题下的 **Gamma/伽马** 图标。

  伽马模块会出现：
  
  ![](http://www.curtpalme.com/images/gammaModule_new.png)

* 2.5.2. 显示 100% 白测试图案。在 ChromaPure 校准碟的：*Main Menu -> Gamma -> Full Field (or 6.5% Window) -> 100% Stimulus*。点击 **M**（测量）。

  ChromaPure 会自动调整到 90% ，准备下次读数。

* 2.5.3. 调整到 90% 白测试图案，再次点击 **M**（测量）。
* 2.5.4. 重复调整、测量的过程，直到你测量过 5% 。这产生一个基线量值。

  ***提示：****如果你的显示器或视频处理器有 5% 处的伽马调节，校准到这一点会确保优质的暗部细节。否则只能到 10% 。*

  当取得基线量值的时候，屏幕上看起来就是这样：
  
  ![](http://www.curtpalme.com/images/gammaModule-data_new.png)

  如果你的显示器或视频处理器没有全功能的 10 点（或更多）伽马调整功能，你可能需要试一下不同的伽马值，再选择一个在 40%~90% 区间内最佳匹配前文提到的目标值的。这样你该略过步骤 2.5.5 ~ 2.5.9 。

  如果你的显示器或视频处理器提供全功能的 10 点（或更多）伽马调整功能，你可以按照下面的步骤，在各点仔细调整伽马，来得到更佳的精度：

* 2.5.5. 显示 90% 白测试图案。在 ChromaPure 校准碟的：*Main Menu -> Gamma -> Full Field (or 6.5% Window) -> 90% Stimulus*。点击 **C**（持续测量）。

* 2.5.6. 按照你的情况调整伽马值，使得 90% 处的蓝色圆圈落到红色线上。

  ***注：****伽马和亮度在相反的方向上移动。亮度上升时，伽马下降。亮度降低时，伽马上升。*

* 2.5.7. 达到伽马的目标值后，点击 **Stop/停止**

* 2.5.8. 在每个点上重复执行这几步，直到每个等级上测量值都匹配目标值。

* 2.5.9. 因为伽马校正和灰阶校正是相关的，调整完伽马，你几乎必然需要回头调一下灰阶（步骤2.4）。幸运的是，调整伽马对灰阶的影响远大于调整灰阶对伽马的影响。就是说，回头调整灰阶之后，一般不必再进一步调整伽马了。

  一旦视频级别、灰阶和伽马都让你满意了，你可以继续进行色彩校正了。

### 步骤2.6：色彩校正

开始色彩校正之前，我们开始探讨一些基础概念和专门术语。

色彩表现，一般用下图展示的三角形的图来显示：

![](http://www.curtpalme.com/images/cie2.jpg)

该图表示了一种国际公认的，把人眼可以看到的全部色彩或“色彩空间”做映射的方法。称作 CIE 1931 色彩空间。由“国际照明委员会”（Commission Internationale de l'Eclairage，法语。英文是 International Commission on Illumination）或“CIE”于 1931 年创立。一般称为 CIE 图。

可以看到，CIE 图在一个 xy 轴上描绘出了颜色。即，图上任一色彩都可以由一个 xy 坐标组合指定。例如白色可以用点 x=0.3127，y=0.329 定义。

这个图的唯一问题是，它是二维的，而色彩是三维的。这个图描述了色彩中的色调和饱和度，但它忽略的第三个元素，就是亮度（照度）。这必须单独表示，通常用个条状图。

图上高亮的点，标记了 HDTV[^HDTV] 系统中的主色（红、绿、蓝）和副色（黄、青、洋红）。色彩校正的目标就是确保显示设备精确展示出这些颜色，这可以由在图上画出它们来验证。

[^HDTV]: 译者注：高清电视

另有 Rec. 709 作为 HDTV 标准的补充，还有其它色彩系统。比如，标清广播的色彩与 HDTV 略有不同。甚至，北美的 SDTV（SMPTE-C）和欧洲的 SDTV（EBU）都不一样。尽管存在其它的色彩规范，Rec. 709，SMPTE-C 和 EBU 是家庭视频的主用色彩系统，每个都可以这样在 CIE 图上画出来：

**REC 709 (HDTV):** 
Red: x=0.640 / y=0.330 / Y=0.2126 
Green: x=0.300 / y=0.600 / Y=0.7152 
Blue: x=0.150 / y=0.060 / Y=0.0722 
Yellow: x=0.419 / y=0.505 / Y=0.9278 
Cyan: x=0.225 / y=0.329 / Y=0.7874 
Magenta: x=0.321 / y=0.154 / Y=0.2848 
White: x=0.3127 / y=0.3290 / Y=1.0000 

**SMPTE-C / REC 601 (SDTV):** 
Red: x=0.630 / y=0.340 / Y=0.2124 
Green: x=0.310 / y=0.595 / Y=0.7011 
Blue: x=0.155 / y=0.070 / Y=0.0866 
Yellow: x=0.421 / y=0.507 / Y=0.9134 
Cyan: x=0.231 / y=0.326 / Y=0.7876 
Magenta: x=0.314 / y=0.161 / Y=0.2989 
White: x=0.3127 / y=0.3290 / Y=1.0000 

**EBU (PAL/SECAM):** 
Red: x=0.640 / y=0.330 / Y=0.2220 
Green: x=0.290 / y=0.600 / Y=0.7076 
Blue: x=0.150 / y=0.060 / Y=0.0713 
Yellow: x=0.417 / y=0.502 / Y=0.9287 
Cyan: x=0.220 / y=0.329 / Y=0.7780 
Magenta: x=0.327 / y=0.157 / Y=0.2933 
White: x=0.3127 / y=0.3290 / Y=1.0000 

**Rec. 2020 (UHD):** 
Red: x=0.708 / y=0.292 / Y=0.2627 
Green: x=0.170 / y=0.797 / Y=0.678 
Blue: x=0.131 / y=0.046 / Y=0.0593 
Yellow: x=0.446 / y=0.345 / Y=0.9407 
Cyan: x=0.146 / y=0.345 / Y=0.7373 
Magenta: x=0.368 / y=0.147 / Y=0.322 
White: x=0.3127 / y=0.3290 / Y=1.0000

这些就是 ChromaPure 内部使用的，用于计算你的显示设备读数与标准差距的数值。

你可能注意到了，这些规定值里包含了一个 Y 值。这就是亮度，CIE 图里没有覆盖的第三个因子。如果这些数值不是图上的 xy 坐标，那它是什么呢？注意到白色总是 1.0 ，其它颜色只是白色的百分比。所以，拿 Rec.709 的红色来说，红色有白色 21.26% 的亮度。所以，如果白色测量的是 120 $cd/m^2$ ，那么红色就应该测得大约 25.5 $cd/m^2$ 。

如下所示，ChromaPure 用条状图显示这些亮度误差。这个图来自 **Pre-Calibration Color Gamut/前校准色域**模块。校准的目的是让这些值尽量接近零：

![](http://www.curtpalme.com/images/luminance_new.png)

带上这些初步概念，我们开始真正地校准吧。

#### 步骤2.6.1：为没有色彩管理系统（CMS）的显示设备校准颜色

尽管和过去相比，如今色彩管理系统越发常见，你还是可能遇到个没有它的显示设备。这种情况下，色彩校正的选择非常有限。大多数情况下，你所有能做的就是调整主色度、主色调。

* 2.6.1.1. 启动 ChromaPure ，初始化校色仪。（见步骤1.2）
* 2.6.1.2. 回到 ChromaPure 主窗口，点击 **Calibration/校准** 标题下的 **Color/Tint** 图标。

  **Color/Tint** 模块会出现：
  
  ![](http://www.curtpalme.com/images/colorDecoding_new.png)

* 2.6.1.3. 显示 100% 白的测试图案，在 ChromaPure 校准碟的：*Main Menu -> Adv. Color Management -> Full Field Amp/100%S (or 6.5% Window Amp/100%S) -> White Sweep -> 100% White*。(关于显示测试图案的更多信息，见步骤1.1：准备测试图案源）

* 2.6.1.4. 点击 **M**（测量）。

  ChromaPure 会跳转到红色。

* 2.6.1.5. 显示 75% 红的测试图案，在 ChromaPure 校准碟的：*Main Menu -> Adv. Color Management -> Full Field Amp/100%S (or 6.5% Window Amp/100%S) ->  Red Sweep -> 75% Red*。再次点击 **M**（测量）。

  重复此步骤，直到你量完全部的主色和副色。

  图上会用色条来显示误差：

  ![](http://www.curtpalme.com/images/colorDecoding-data_new.png)

* 2.6.1.6. 选中 **Red** 单选按钮。

* 2.6.1.7. 再次显示 75% 红的测试图案，在 ChromaPure 校准碟的：*Main Menu -> Adv. Color Management -> Full Field Amp/100%S (or 6.5% Window Amp/100%S) ->  Red Sweep -> 75% Red*。点击 **C**（持续测量）。

  随着你的调节过程，ChromaPure 会实时显示误差值。

* 2.6.1.8. 调整显示设备的主色度选项，直到在红、绿、蓝中，红色的误差最小。人眼对红色误差极其敏感，所以最好考虑到这点。

* 2.6.1.9. 完成后，点击 **Stop** 。

* 2.6.1.10. 选择 **Magenta** 单选按钮。

* 2.6.1.11. 显示 75% 洋红的测试图案，在 ChromaPure 校准碟的：*Main Menu -> Adv. Color Management -> Full Field Amp/100%S (or 6.5% Window Amp/100%S) -> Magenta Sweep -> 75% Magenta*。点击 **C**（持续测量）。

  随着你的调节过程，ChromaPure 会实时显示误差值。

* 2.6.1.12. 调节显示设备的主色调选项，直到洋红的误差最小。

#### 步骤2.6.2：为有色彩管理系统（CMS）的显示设备校准颜色

如果你的显示设备带 CMS ，你可以在调节其色彩表现上，有更好的控制和精度。

***提示：****即便你的显示设备没有 CMS ，你仍然可以用外购个像 [Lumagen Radiance](http://www.curtpalme.com/Radiance.shtm) 的视频处理器的方式，为其增加 CMS 能力。这种放在信号链路上，显示设备之前的设备，可以提供全功能的灰阶、伽马和色彩工具。*

* 2.6.2.1. 回到 ChromaPure 主窗口，点击 **Calibration/校准** 标题下的 **Color Mgmt** 图标。

  **Color Management** 模块会出现：

  ![](http://www.curtpalme.com/images/colorManagement_new.png)

* 2.6.2.2. 在程序的选项面板，确定你选择了期望的 **Reference Gamut/参考色域** 。大多数情况下，你会想用缺省值，HDTV 标准的 Rec. 709 。

* 2.6.2.3. 选择希望的 **Color Space/色彩空间**。

  有三种色彩空间可选：
  * HSL（色调、饱和度、亮度）
  * RGB（红、绿、蓝）
  * xyY（CIE 图坐标加上亮度）

* 2.6.2.4. 选择匹配你显示设备或处理器的 CMS 的色彩空间。比如三星平板和 Lumagen 用的是 RGB ，DVDO Duo 用的是 xyY ，其它多数 CMS 用的是 HSL（松下等离子和 JVC、Epson、Sony 投影机）。

* 2.6.2.5. 显示 100% 白的测试图案，在 ChromaPure 校准碟的：*Main Menu -> Adv. Color Management -> Full Field Amp/100%S (or 6.5% Window Amp/100%S) -> White Sweep -> 100% White*。点击 **M**（测量）。

* 2.6.2.6. 重复这一步骤，直到量好了白色、所有主色（红、绿、蓝）和副色（黄、青、洋红）。校准碟中的图案位置是：*Main Menu -> Adv. Color Management -> Full Field Amp/100%S (or 6.5% Window Amp/100%S) -> Red, Green, or Blue Sweep -> 75%*。这样保存了一份你的显示设备校准前色彩表现的快照，应该看上去像你在 **Pre-Calibration Color Gamut** 里测量的一样。

  **Color Management** 模块会显示裸数据、CIE 图以及用条状图表示的显示误差。

* 2.6.2.7. 点击 **Red** 颜色选择器，显示 75% 红的测试图案，在 ChromaPure 校准碟的：*Main Menu -> Adv. Color Management -> Full Field Amp/100%S (or 6.5% Window Amp/100%S) -> Red Sweep -> 75% Red*。点击 **C**（持续测量）。
* 2.6.2.8. 使用你显示器或处理器的 CMS ，做必要调节，把色彩误差降低到可以接受的程度。看着条状图，随时显示着三个轴向上颜色的表现。随着你使用 CMS 的校正，上面的值实时变动。目标是让每个颜色的$\Delta E$降到 1.5 或更低。
* 2.6.2.9. 当你达成了预期目标，点击 **Stop** 。

  ***提示：****你可能发现了，三个轴向的调节之间有某种关联。经常这样。尤其是 HSL 色彩空间的亮度和饱和度。这是正常的。就把它们来回调，直到误差可以接受为止。*

* 2.6.2.10. 当你完成了所有颜色的校正，在 **Module Options/模块选项**中，点击 **Erase all data from this module/擦除本模块的所有数据**。
* 2.6.2.11. 再量一下白色和所有主、副色（步骤 2.6.2.5 到 2.6.2.10），确认你已经去除了严重的色差。如果需要就单点做个校正。

## 第三部分：后校准过程

### 步骤3.1：检查结果

一旦你结束了所有的校准过程，是时候检查下结果了。

* 3.1.1. 回到 ChromaPure 主窗口，点击 **Post-Calibration/后校准** 标题下的 **Grayscale** 图标。

  **Post-Calibration Grayscale** 模块会出现。

* 3.1.2. 如你在 **Pre-Calibration Grayscale** 模块中做的测量（见步骤 1.3.1）一样，再完整测一遍。
* 3.1.3. 如果一切还好，你可以结束灰阶和伽马了。如果不是，看情况对个别小点做修正。
* 3.1.4. 回到 ChromaPure 主窗口，点击 **Post-Calibration/后校准** 标题下的 **Color Gamut** 图标。

  **Post-Calibration Color Gamut** 模块会出现。

* 3.1.5. 如你在 **Pre-Calibration Color Gamut** 模块中做的测量（见步骤 1.3.4）一样，再完整测一遍。
* 3.1.6. 如果一切还好，你可以结束了。如果不是，看情况对个别小点做修正。

### 步骤3.2：运行校准报告（可选）

当你对自己的努力满意以后，你可能想运行一下校准报告，给自己保留个记录或分享给别人。

ChromaPure 有三种方法生成报告。

- 快速报告
- 定制报告（内部格式）
- 详细报告（Excel）

#### 步骤3.2.1：生成快速报告

ChromaPure 的许多模块中都可以生成快速报告（Quick Reports）。基本上它再现了模块中展示过的信息。

* 3.2.1.1. 要运行报告，直接点击 **Quick Report** 图标（![](http://www.curtpalme.com/images/toolbar_quickreport_new.jpg)）。

  **Quick Report** 会出现：

  ![](http://www.curtpalme.com/images/quickReport_new.png)

* 3.2.1.2. 要保存报告，直接点击工具栏上的 **Print** 图标，选择 XPR 打印机或 PDF 打印机。如果你没有安装 PDF 打印机，你可以在网络上下载个免费的（太多了）。XPS 和 PDF 都有免费的查看工具能用，可以方便地在网络上分享。

#### 步骤3.2.2：生成定制或 Excel 的校准报告

* 3.2.2.1. 回到 ChromaPure 主窗口，点击 **Post-Calibration/后校准** 标题下的 **Reports** 图标。

  **Reports** 模块会出现。

  ![](http://www.curtpalme.com/images/reportModule_new.png)

* 3.2.2.2. 选择 **Detailed Calibration Report/详细校准报告**或 **Excel Report/Excel 报告** 。

  ***提示：****如果你运行 Excel 报告，你必须安装了 Microsoft Excel 97 或更新的版本。以及，运行报告时，Excel 得是关着的。*

* 3.2.2.3. 点击 **Run Report/运行报告**。

  ***注：****你可以在屏幕左侧选择报告中有哪些页面，调整页面顺序。你也可以指定封面中出现的信息。*

  全面的校准报告会出现。

* 3.2.2.4. 要保存报告，像上面说的，打印成 XPS 或 PDF 。从 Microsoft Office 2007 SP2 开始，Excel 中内置了保存成 PDF 功能。还有，Windows 10 内置了 Microsoft PDF 打印机。

### 步骤3.3：导出校准数据（可选）

作为运行报告的补充，你也可以导出 ChromaPure 的校准数据。数据保存成 CSV 格式。你也可以保存成会话文件（`*.calx`），这种文件以后只能用 ChromaPure 读取。

* 3.3.1. 要把模块数据保存成 CSV 格式，在目标模块中点击 **Module Options** 按钮（![](http://www.curtpalme.com/images/toolbar_moduleoptions_new.jpg)），选择 **Export Mesurements/导出量值**。

  出现一个 Windows 标准的**保存到**对话框。

* 3.3.2. 在**保存为**下拉列表中，选择 CSV（逗号分隔的值）。

  CSV 数据可以在 Excel 或其它 CSV 兼容软件中打开分析。

* 3.3.3. 要保存 ChromaPure 会话文件（`*.calx`），回到 ChromaPure 的主窗口，点击 **Tools/工具**标题下的 **Save Session/保存会话**图标。
* 3.3.4. 要加载 ChromaPure 会话文件（`*.calx`），回到 ChromaPure 的主窗口，点击 **Tools/工具**标题下的 **Load Session/加载会话**图标，并浏览打开你之前保存的 `.calx` 文件。

## 校准 UHD/HDR 源

新型的 4K UHD（超高清）电视和蓝光碟为校准提出了一些特别的挑战。最大的问题是没有商业显示器可以 HDR 所需的动态范围，或是 Rec. 2020 色域所需的全色域。所有的 UHD 蓝光盘都包含了 HDR 和 Rec. 2020 。另一个状况是，为了让显示器进入正确的 HDR 模式，用户必须使用特殊的测试图案。如果是为了这种目的，ChromaPure 校准盘是不起作用的。在本文写成的时候（2017 年早期），仅有一组买得起的 HDR 测试图案。可以[在这里购买](http://rmadvancedcaldisc.com/rm-uhdhdr-10.html)。

要是有了 HDR 测试图案和 HDR 显示器，你可以用 ChromaPure 在 HDR 模式下校准显示器（4K HDR 模式和 2K HD 需要独立校准）。

在 **Initial Setup** 页，**Color Intensity** 选择 50% 。

在 **Options** 模块的 **Gamut** 标签里，**Reference Gamut** 选择 Rec. 2020 。也是在 **Gamut** 标签，**Gamma Target** 选择 HDR10 。

选好后，关闭 **Options** 模块。

打开 **Gamma** 模块，除了你调不了显示器对 60~75% 以上的伽马值以外，像之前的 2K HD 一样校准伽马。当下显示器压根不支持高过它的动态范围。

打开 **Color Managenment** 模块。

在 **Module Options** 里选择 50% 饱和度，点击**Apply/应用**。

像你为标准 2K HD 显示器以其他值为目标一样，校准 50% 饱和度至 Rec. 2020 参考色域。

白平衡/灰阶校正在 HDR 模式下没有区别。

## 关闭评论

我希望这个手册帮你理解了，为达到最佳画面质量，正确校准为什么是所有电视或投影机都该做的，最重要的增强之一。

导演、电影摄影师和动态画面着色师，他们花了极大的力气让内容以正确的颜色呈现。你做一点，校准显示器，就可以保证你在家里看到的完美匹配到那些专业人员想让你看到的。

享受你刚校准的显示器吧！

干杯

Kal
- [CurtPalme.com 家庭影院](http://www.curtpalme.com/) 编辑
- [TheElectricBrewery.com](http://www.theelectricbrewery.com/) 创始人 …一步步做个自己的酿酒厂。

我最新的著作是一步步做个自己的酿酒厂。现开放电子书下载：
[![](http://www.theelectricbrewery.com/images/728x90/guide.jpg)](http://www.theelectricbrewery.com/the-complete-guide-to-building-your-brewery)
