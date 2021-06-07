
vim 知识点

操作符+动作命令 = 操作

常用操作
c 修改
d 删除
y 复制
g~ 转换大小写
gu  转换为小写
gU 转换为大写
> 缩进
< 
=
! 使用外部程序的motion


键盘功能划分：

移动类： h j k l 

行首 0

行尾 $  A可以直接进入insert模式 

o 换行 并进入insert mode

gg 文件头

[[ 文件头

]] 文件尾

H 屏幕顶行

L 屏幕底行

w next word

e 词尾

b 前一个单词 

n 查找下一处 N 查找上一处



<C-k>  Ctrl + k 
<CR> 回车键
 可视模式 用来选中内容 然后修改 
 3种可视模式 v 字符可视模式
 V 行可视模式
 ctrl+v 面向块的可视模式


修改大小写锁定键为esc键，
新建文本文件并写入以下内容：

Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout]
"Scancode Map"=hex:00,00,00,00,00,00,00,00,02,00,00,00,01,00,3a,00,00,00,00,00

然后重命名为xx.reg 写入注册表后，再双击注入注册表即可。
重启后就生效。
