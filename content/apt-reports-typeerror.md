Title: APT 返回 TypeError 的错误
Date: 2018-06-22 09:43
modified: 2018-06-22 10:15
Tags: server, install, apt
Category: Linux
Slug: apt-reports-typeerror
Author: Levi G
Status: published

最近在为公司整理工作环境，部署 OMV 4 时，发现 `apt update` 指令会引发如下错误：

```text
Exception ignored in: <function WeakValueDictionary.__init__.<locals>.remove at 0x............>
Traceback (most recent call last):
  File "/usr/lib/python3.5/weakref.py", line 117, in remove
TypeError: 'NoneType' object is not callable
Exception ignored in: <function WeakValueDictionary.__init__.<locals>.remove at 0x............>
Traceback (most recent call last):
  File "/usr/lib/python3.5/weakref.py", line 117, in remove
TypeError: 'NoneType' object is not callable
```

找了一下，根据 [OVM 的论坛回复](https://forum.openmediavault.org/index.php/Thread/19658-Upgrade-Debian-9-and-4-x/?postID=154150#post154150)，应该是 python 的 [bug](https://bugs.python.org/issue29519)，同时提供了 [fix](https://github.com/python/cpython/commit/9cd7e17640a49635d1c1f8c2989578a8fc2c1de6) 。

具体方法就是修改 `/usr/lib/python3.5/weakref.py` 文件的 109 行和 117 行：

```diff
@@ -106,15 +106,15 @@ def __init__(*args, **kw):
         self, *args = args
         if len(args) > 1:
             raise TypeError('expected at most 1 arguments, got %d' % len(args))
-        def remove(wr, selfref=ref(self)):
+        def remove(wr, selfref=ref(self), _atomic_removal=_remove_dead_weakref):
             self = selfref()
             if self is not None:
                 if self._iterating:
                     self._pending_removals.append(wr.key)
                 else:
                     # Atomic removal is necessary since this function
                     # can be called asynchronously by the GC
-                    _remove_dead_weakref(d, wr.key)
+                    _atomic_removal(d, wr.key)
         self._remove = remove
         # A list of keys to be removed
         self._pending_removals = []
```

