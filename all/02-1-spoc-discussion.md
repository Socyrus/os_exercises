#lec 3 SPOC Discussion

## 第三讲 启动、中断、异常和系统调用-思考题

## 3.1 BIOS
 1. 比较UEFI和BIOS的区别。

    

 1. 描述PXE的大致启动流程。

## 3.2 系统启动流程
 1. 了解NTLDR的启动流程。
 1. 了解GRUB的启动流程。
 1. 比较NTLDR和GRUB的功能有差异。
 1. 了解u-boot的功能。

## 3.3 中断、异常和系统调用比较
 1. 举例说明Linux中有哪些中断，哪些异常？
 1. Linux的系统调用有哪些？大致的功能分类有哪些？  (w2l1)

```
  + 采分点：说明了Linux的大致数量（上百个），说明了Linux系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
 >Linux 系统调用有两百多个  
 >有下列几种功能分类  
 >一、进程控制  
 >二、文件系统控制  
 >   1.文件读写操作  
 >   2.文件系统操作  
 >三、系统控制  
 >四、内存管理  
 >五、网络管理  
 >六、socket管理  
 >七、用户管理  
 >八、进程间通信  
 >   1.信号  
 >   2.消息  
 >   3.管道  
 >   4.信号量  
 >   5.共享内存  
 
 1. 以ucore lab8的answer为例，uCore的系统调用有哪些？大致的功能分类有哪些？(w2l1)
 
 ```
  + 采分点：说明了ucore的大致数量（二十几个），说明了ucore系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
 >有22个系统调用
 >大致的功能分类有：  
 >一、进程管理
       sys_exit,  
       sys_fork,  
       sys_wait,  
       sys_exec,  
       sys_yield,    
       sys_kill,   
       sys_getpid,    
       sys_lab6_set_priority,  
       sys_sleep,  
 >二、内存管理  
        sys_pgdir,  
 >三、文件操作  
       sys_open,  
       sys_close,  
       sys_read,  
       sys_write,  
       sys_seek,  
       sys_fstat,  
       sys_fsync,  
       sys_getcwd,  
       sys_getdirentry,  
       sys_dup,  
 
## 3.4 linux系统调用分析
 1. 通过分析[lab1_ex0](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex0.md)了解Linux应用的系统调用编写和含义。(w2l1)
 

 ```
  + 采分点：说明了objdump，nm，file的大致用途，说明了系统调用的具体含义
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 
 ```
 
 >objdump的作用：反汇编机器码，得到汇编代码  
 >nm的作用：列出目标文件的符号清单。  
 >nm的参数：  
 >-a或--debug-syms：显示调试符号。  
-B：等同于--format=bsd，用来兼容MIPS的nm。  
-C或--demangle：将低级符号名解码(demangle)成用户级名字。这样可以使得C++函数名具有可读性。  
-D或--dynamic：显示动态符号。该任选项仅对于动态目标(例如特定类型的共享库)有意义。  
-f format：使用format格式输出。format可以选取bsd、sysv或posix，该选项在GNU的nm中有用。默认为bsd。  
-g或--extern-only：仅显示外部符号。  
-n、-v或--numeric-sort：按符号对应地址的顺序排序，而非按符号名的字符顺序。  
-p或--no-sort：按目标文件中遇到的符号顺序显示，不排序。  
-P或--portability：使用POSIX.2标准输出格式代替默认的输出格式。等同于使用任选项-f posix。  
-s或--print-armap：当列出库中成员的符号时，包含索引。索引的内容包含：哪些模块包含哪些名字的映射。  
-r或--reverse-sort：反转排序的顺序(例如，升序变为降序)。  
--size-sort：按大小排列符号顺序。该大小是按照一个符号的值与它下一个符号的值进行计算的。  
-t radix或--radix=radix：使用radix进制显示符号值。radix只能为“d”表示十进制、“o”表示八进制或“x”表示十六进制。  
--target=bfdname：指定一个目标代码的格式，而非使用系统的默认格式。  
-u或--undefined-only：仅显示没有定义的符号(那些外部符号)。  
-l或--line-numbers：对每个符号，使用调试信息来试图找到文件名和行号。对于已定义的符号，查找符号地址的行号。对于未定义符号，查找指向符号重定位入口的行号。如果可以找到行号信息，显示在符号信息之后。  
-V或--version：显示nm的版本号。  
--help：显示nm的任选项。  

>file的作用:探测给定文件的类型  
>常用参数  
>--help  
显示帮助信息  
-v,--version  
输出版本信息并退出  
-b,--brief  
不显示文件名字  
-f,--files-fromFILE  
读取待测试的名称文件  
-F,--seperatorSTRING  
使用字符串作为分隔符，不再使用“：”  
-i,--mime  
显示文件的mime类型  
--mime-type  
--mime-encoding  
-L,--dereference  
显示符号链接所指向文件信息  
-h,--no-dereference  
-d,--debug  
输出调试信息  
 
 1. 通过调试[lab1_ex1](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex1.md)了解Linux应用的系统调用执行过程。(w2l1)
 

 ```
  + 采分点：说明了strace的大致用途，说明了系统调用的具体执行过程（包括应用，CPU硬件，操作系统的执行过程）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
## 3.5 ucore系统调用分析
 1. ucore的系统调用中参数传递代码分析。
 1. ucore的系统调用中返回结果的传递代码分析。
 1. 以ucore lab8的answer为例，分析ucore 应用的系统调用编写和含义。
 1. 以ucore lab8的answer为例，尝试修改并运行代码，分析ucore应用的系统调用执行过程。
 
## 3.6 请分析函数调用和系统调用的区别
 1. 请从代码编写和执行过程来说明。
   1. 说明`int`、`iret`、`call`和`ret`的指令准确功能
 