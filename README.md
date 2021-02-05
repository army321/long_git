# long_git
本地修改内容，测试上传正常

常用git命令：
git add file_name   如果是文件夹，则为：  文件夹名/    ---注意有一个斜杠
git commit -m "这里写注释的内容"

git remote add origin git@github.com:army321/long_git.git  --这个是设置远程仓库的  这个应该只要设置一次就好了，后续没改就不用再设置

git push -u origin master  把提交的内容同步到远程仓库
git push  origin master 

git log --查看log 查看log状态下，按 Q 键可以退出


Git鼓励大量使用分支：

查看分支：git branch

创建分支：git branch <name>

切换分支：git checkout <name>或者git switch <name>

创建+切换分支：git checkout -b <name>或者git switch -c <name>

合并某分支到当前分支：git merge <name>

删除分支：git branch -d <name>

github 同步 可断点续传
git fetch git://…..git

Git clone，  同步 不能断点续传，可能中断

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