man = []
try:
    data = open('mcnetest.txt') #打开要去重的文件
    man_file = open('mcnewtest.txt', 'w+')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split('n3 ', 1) #用对应的标识获取需要的数据
            line_spoken = line_spoken.strip()
            man.append(line_spoken)
        except ValueError:
            pass
    man = list(set(man)) #去重

    #写入新建的文件
    for item in man:
        man_file.write(str(item) + "\n")
    data.close()
    man_file.close()
except IOError:
    print('fail to open file')
