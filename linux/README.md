# linux 常用命令

cd /xxx/xx  到指定目录
cd ..  返回上层
cd / 返回主

linux所有的都是文件，要到指定文件下进行操作

touch  文件名.后缀   #用于创建一个文件
mv 路径/fileName newPath/newFileName  #移动或者重命名文件  其中路径可省略，就变成修改当前文件夹中的文件名


mkdir [选项] DirName  创建文件夹

rm -r DirName 删除文件夹
-i 删除前逐一询问确认。
-f 即使原档案属性设为唯读，亦直接删除，无需逐一确认。
-r 将目录及以下之档案亦逐一删除,递归所有的子目录,逐一询问。


vi 文件名   #创建并用vi打开一个文件 可以用vim的方式编辑
esc  
i 进入插入模式，可进行输入操作

：或者 / 命令模式 输入相应的命令
wq  保存并退出
q 退出
q！ 强制退出
wq！ 强制保存退出
