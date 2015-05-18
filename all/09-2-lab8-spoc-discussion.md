# lab8 文件系统 (lec 22) spoc 思考题


- 有"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的ucore_code和os_exercises的git repo上。

## 个人思考题

### 总体介绍
 1. 文件系统中的文件、目录、索引节点和安装点这几种数据结构分别支持些什么操作？
 2. 请简要描述ucore文件系统支持的文件系统抽象

 > 文件、目录、索引节点和安装点

### ucore 文件系统架构

 1. 请简要阐述ucore 文件系统架构的四个组成部分

 > 系统调用接口、VFS、SFS和I/O接口

 2. 请简要说明进程proc_struct、文件file、inode之间的关系。 
 
 3. ucore中的进程打开文件表和系统打开文件表对应到具体的哪个数据结构上？

### Simple File System分析

 1. SFS在硬盘上的四大部分主要是什么，有何作用？
 
 > superblock, root-dir inode, freeman, data block

 2. 硬盘上的SFS是如何加载到ucore中并初始化的？
 3. 硬盘上的inode和内存中的inode的关系和区别是什么?
 4. 描述file, dir, inode在内存和磁盘上的格式和相关操作。

### Virtual File System分析

 1. file数据结构的主要内容是什么？与进程的关系是什么？
 2. inode数据结构的主要内容是什么？与file的数据结构的关系是什么？
 3. inode_ops包含哪些与文件相关的操作？
 4. VFS是如何把键盘、显示输出和磁盘文件统一到一个系统调用访问框架下的？ 

### I/O 设备接口分析

 1. device数据结构的主要内容是什么？与fs的关系是什么？与inode的关系是什么？
 2. 比较ucore中I/O接口、SFS文件系统接口和文件系统的系统调用接口的操作函数有什么异同？
 
## 小组思考题

1. (spoc) 理解文件访问的执行过程，即在ucore运行过程中通过`cprintf`函数来完整地展现出来读一个文件在ucore中的整个执行过程，(越全面细致越好)
完成代码填写，并形成spoc练习报告，需写练习报告和简单编码，完成后放到git server 对应的git repo中
```
$ [sys_read]
[sysfile_read]
[file_read]
[vfs inode read]
h[sys_read]
[sysfile_read]
[file_read]
[vfs inode read]
e[sys_read]
[sysfile_read]
[file_read]
[vfs inode read]
l[sys_read]
[sysfile_read]
[file_read]
[vfs inode read]
l[sys_read]
[sysfile_read]
[file_read]
[vfs inode read]
o[sys_read]
[sysfile_read]
[file_read]
[vfs inode read]
[sys open arg :hello] 0
[sysfile open]path: hello 1
[file_open] 2
[vfs open] 3 
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs_load_inode]
[sfs_rbuf]
[disk io]
[vfs inode open] 4
[sfs inode sfs_openfile] 5
[sysfile open]path: hello 6
[file_open] 7
[vfs open] 8 
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs dirent read]
[sfs_rbuf]
[disk io]
[sfs_load_inode]
[sfs_rbuf]
[disk io]
[vfs inode open] 9
[sfs inode sfs_openfile] 10
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[sfs_rbuf]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[sfs_rbuf]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[sfs_rbuf]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[sfs_rbuf]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[sfs_rbuf]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[sfs_rbuf]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[sfs_rbuf]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[sfs_rbuf]
[disk io]
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[sfs_rbuf]
[disk io]
[sys open arg :stdin:] 0
[sysfile open]path: stdin: 1
[file_open] 2
[vfs open] 3 
[vfs inode open] 4
[sys open arg :stdout:] 0
[sysfile open]path: stdout: 1
[file_open] 2
[vfs open] 3 
[vfs inode open] 4
Hello world!!.
I am process 14.
hello pass.
$ [sys_read]
[sysfile_read]
[file_read]
[vfs inode read]

从上面的输出结果大概可以看出读文件过程
首先我输入一个命令hello
每输入一个字母都会执行 sys_read->sysfile_read->file_read->vfs_inode_read

然后
[sys open arg :hello] 0
[sysfile open]path: hello 1
[file_open] 2
[vfs open] 3 
[vfs inode open] 4
[sfs inode sfs_openfile] 5
从sycall 一直到 sfs_openfile 打开文件

然后是从文件中读取数据
[sysfile_read]
[file_read]
[vfs inode read]
[sfs inode io]
[disk io]
按照文件系统->vfs->sfs->disk这样的顺序调用
```

2. （spoc） 在下面的实验代码的基础上，实现基于文件系统的pipe IPC机制

### 练习用的[lab8 spoc exercise project source code](https://github.com/chyyuu/ucore_lab/tree/master/labcodes_answer/lab8_result)
