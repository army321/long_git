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