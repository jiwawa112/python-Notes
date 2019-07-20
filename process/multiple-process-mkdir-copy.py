#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import multiprocessing

# 多任务copy文件夹
# 在copy的同时 显示copy进度百分比

def copy_file(q,file_name,old_folder_name,new_folder_name):
    """完成文件的复制"""
    #print("=====>模拟copy文件: 从%s--->到%s 文件名时:%s" % (old_folder_name,new_folder_name,file_name))
    old_f = open(old_folder_name + "/" + file_name,"rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name,"wb")
    new_f.write(content)
    new_f.close()

    # 如果copy完一个文件，那么就向队列中写入一个消息，表示已经完成
    q.put(file_name)

def main():
    # 1.获取用户要copy的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹路径: ")

    # 2.创建一个新的文件夹
    try:
        new_folfer_name = old_folder_name + "[附件]"
        os.mkdir(new_folfer_name)
    except:
        pass

    # 3.获取文件夹中所有待copy的文件名字 listdir()
    file_names = os.listdir(old_folder_name)
    #print(file_names)

    # 4.创建进程池
    po = multiprocessing.Pool(5)

    # 5.创建一个队列
    q = multiprocessing.Manager().Queue()

    # 6.复制源文件夹中的文件，到新文件夹中的文件去
    for file_name in file_names:
        po.apply_async(copy_file,args=(q,file_name,old_folder_name,new_folfer_name))

    po.close()
    # po.join()
    all_file_num = len(file_names)      #所有文件个数
    copy_ok_num = 0
    while True:
        file_name = q.get()
        #print("已经完成copy: %s" % (file_name))
        copy_ok_num += 1
        print("拷贝进度为: %.2f %%" % (copy_ok_num*100/all_file_num),end='')
        if copy_ok_num >= all_file_num:
            break

    print()

if __name__ == '__main__':
    main()
