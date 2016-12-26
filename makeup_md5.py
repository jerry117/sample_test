import hashlib

# 组装要转换的数据
def chanege_md5(str1,str2,str3,str4,str5='18432se526ge963387ewd1449pu22550'):
        return str1+str2+str3+str4+str5

m1 = chanege_md5('1','56371624','10','1482718768000') #传入对应的数据
#使用md5转换数据
m2 = hashlib.md5()
m2.update(bytes(m1,encoding='utf8'))
print (m2.hexdigest())
