# long_git


常用git命令：
git add file_name   如果是文件夹，则为：  文件夹名/    ---注意有一个斜杠

git commit -m "这里写注释的内容"

git remote add origin git@github.com:army321/long_git.git  --这个是设置远程仓库的  这个应该只要设置一次就好了，后续没改就不用再设置

git push -u origin master  把提交的内容同步到远程仓库
git push  origin master   直接git push 也可

git pull 下载远程的内容
git pull origin master:master   把远程的内容与本地的内容合并，  git pull <远程主机名> <远程分支名>:<本地分支名>

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



python 打包exe
要打包的文件放C:\Users\Administrator 下
pyinstaller -F 要打包的名字.py -w

-F：打包后只生成单个exe格式文件；
-D：默认选项，创建一个目录，包含exe文件以及大量依赖文件；
-c：默认选项，使用控制台(就是类似cmd的黑框)；
-w：不使用控制台；
-p：添加搜索路径，让其找到对应的库；
-i：改变生成程序的icon图标。
git fetch和git pull的区别

git fetch：相当于是从远程获取最新版本到本地，不会自动合并。
$ git fetch origin master
$ git log -p master..origin/master
$ git merge origin/master
Shell
以上命令的含义：

首先从远程的origin的master主分支下载最新的版本到origin/master分支上然后比较本地的master分支和origin/master分支的差别最后进行合并
上述过程其实可以用以下更清晰的方式来进行：
$ git fetch origin master:tmp
$ git diff tmp 
$ git merge tmp
Shell
2. git pull：相当于是从远程获取最新版本并merge到本地 
git pull origin master
Shell
上述命令其实相当于git fetch 和 git merge在实际使用中，git fetch更安全一些，因为在merge前，我们可以查看更新情况，然后再决定是否合并。

