# -*- coding: utf-8 -*-
# @Time    : 2019-2-16 15:25
# @Author  : GongLH
# @Email   : gonglinhuan@gmail.com
# @File    : learn_git.py
# @Software: PyCharm

a = 1
'''
安装完成后，在命令行输入：
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
创建一个版本库非常简单，首先，选择一个合适的地方，创建一个空目录：
$ mkdir learngit
$ cd learngit
$ pwd  # pwd命令用于显示当前目录

# 初始化
$ git init
# 修改仓库
$ git add readme.txt # 添加文件
$ git commit -m "wrote a readme file" #提交
-m后面输入的是本次提交的说明，可以输入任意内容，当然最好是有意义的，这样你就能从历史记录里方便地找到改动记录。
# 查看仓库状态
$ git status # 查看状态
$ git diff readme.txt # 查看不同
$ git log # 查看改动日志
$ git log --pretty=oneline # 精简模式

# 回滚
首先，Git必须知道当前版本是哪个版本，在Git中，用HEAD表示当前版本，也就是最新的提交1094adb...（注意我的提交ID和你的肯定不一样），上一个版本就是HEAD^，上上一个版本就是HEAD^^，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100。
$ git reset --hard HEAD^
$ cat readme.txt # 查看
$ git reset --hard 1094a # 回到指定版本号，只要写开头几个
$ git reflog # 记录每次的命令

$ git checkout -- readme.txt  # 撤销修改，使工作区退回到版本库或者暂存区的状态
$ git reset HEAD readme.txt  # 把暂存区的修改撤销掉（unstage），重新放回工作区
小结
场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。
场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD <file>，就回到了场景1，第二步按场景1操作。
场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。
# 删除
$ git rm test.txt
$ git commit -m "remove test.txt"

$ git checkout -- test.txt  # 用版本库替换工作区 

# 远程库
$ git remote add origin https://github.com/HuanGe666/learningit.git # 关联远程库，在本地仓库的主目录下运行命令
$ git push -u origin master # 同步 到远程
由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。
$ git push origin master
# 从远程库克隆 # 会克隆到当前目录下
$ git clone https://github.com/HuanGe666/learn_git.git

# 分支
$ git checkout -b dev # 创建分支并切换
相当于$ git branch dev  +  $ git checkout dev
$ git branch # 查看当前分支
$ git checkout master # 切换到主分支
$ git merge dev # 将dev分支合并到主分支
$ git branch -d dev # 删除分支

Git鼓励大量使用分支：
查看分支：git branch
创建分支：git branch <name>
切换分支：git checkout <name>
创建+切换分支：git checkout -b <name>
合并某分支到当前分支：git merge <name>
删除分支：git branch -d <name>

# 合并冲突
vi read.txt 查看文档
$ git log --graph --pretty=oneline --abbrev-commit # 查看合并情况
'''
'''
这是开发分支
'''
