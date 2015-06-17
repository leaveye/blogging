Title: 你好，世界
Date: 2015-06-14 10:20
Tags: try, pelican, test
Category: blogging
Slug: just-test-pelican
Author: Levi G
Summary: 试一下水

[TOC]

# [试水](id:try)

正文文字。
断行同段落。

新段落。

* item 1, 公式 $E=mc^2$ 。
* item 2, 嵌入代码 `onFileReadable()` 。

> 引用文字。

0. numbered 1
0. numbered 2

$$E=mc^2$$

```
:::html
<link rel="stylesheet" type="text/css" href="stylesheets/stylesheet.css" media="screen">
<link rel="stylesheet" type="text/css" href="stylesheets/github-dark.css" media="screen">
<link rel="stylesheet" type="text/css" href="stylesheets/print.css" media="print">
```

```
:::cpp
#define _IDENT_JOIN(PACKAGENAME, FUNCTIONNAME) PACKAGENAME##FUNCTIONNAME
#define JavaIdent(FUNCTIONNAME) _IDENT_JOIN(Java_com_abc_abc_JniUtils_, FUNCTIONNAME)

class sigslot_connection
{
public:
    sigslot_connection(std::function<void()> func) : disconnect_(func) {}
    void disconnect() { disconnect_(); }
private:
    std::function<void()> disconnect_;
};

template<class F>
class sigslot;

template<typename RET, typename... Args>
class sigslot < RET(Args...) >
{
public:
    sigslot() : ret_handler_(nullptr), next_id_(0) {}
    template<typename F>
    sigslot_connection connect(F&& f)
    {
        int id = next_id_++;
        slots_.insert(std::make_pair(id, std::forward<F>(f)));
        return sigslot_connection(std::bind(&sigslot::disconnect, this, id));
    }
    RET operator()(Args... args)
    {
        RET ret = ret_init_;
        for (auto& f : slots_)
        {
            RET ret2 = f.second(args...);
            if (ret_handler_)
                ret = ret_handler_(ret, ret2);
            else
                ret = ret2;
        }
        return ret;
    }
    size_t size() const { return slots_.size(); }

    void set_init_return_code(RET ret) { ret_init_ = ret; }
    void set_return_code_handler(std::function<RET(RET, RET)> ret_handler) { ret_handler_ = ret_handler; }
private:
    void disconnect(int id)
    {
        slots_.erase(id);
    }
private:
    typedef std::function<RET(Args...)> TFunc;
    std::map<int, TFunc> slots_;
    std::function<RET(RET, RET)> ret_handler_;
    RET ret_init_;
    int next_id_;
};
```

---

A | B
--|--
C | D
E | F

[跳转到小标题](#try)[^split]


[^split]: 分割线