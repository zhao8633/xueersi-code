def show(dic):
    max1 = 0
    max2 = 0
    for k in dic:
        if len(str(k).encode('GBK')) > max1:
            max1 = len(str(k).encode('GBK'))
        if len(str(dic[k]).encode('GBK')) > max2:
            max2 = len(str(dic[k]).encode('GBK'))
    if max1 < 20:
        max1 = 20
    if max2 < 20:
        max2 = 20
    print("-"*(max1+max2+5))
    for k in dic:
        print('| {a:<{len1}} | {b:<{len2}}|'.format(a =str(k),b = str(dic[k]),len1=max1-len(str(k).encode('GBK'))+len(str(k)),len2=max2-len(str(dic[k]).encode('GBK'))+len(str(dic[k]))))
    print("-"*(max1+max2+5))
    
def show_green(dic):
    dic1 = {}
    for k in dic:
        k1 = "\033[1;32m"+str(k)+"\033[0m"
        dic1[k1] = "\033[1;33m"+str(dic[k])+"\033[0m"
    max1 = 0
    max2 = 0
    for k in dic1:
        if len(str(k).encode('GBK')) > max1:
            max1 = len(str(k).encode('GBK'))
        if len(str(dic1[k]).encode('GBK')) > max2:
            max2 = len(str(dic1[k]).encode('GBK'))
    if max1 < 25:
        max1 = 25
    if max2 < 25:
        max2 = 25
    print("-"*(max1+max2-16))
    for k in dic1:
        print('| {a:<{len1}} | {b:<{len2}}|'.format(a = k,b =dic1[k] ,len1=max1-len(str(k).encode('GBK'))+len(k),len2=max2-len(str(dic1[k]).encode('GBK'))+len(str(dic1[k]))))
    print("-"*(max1+max2-16))

def show_blue(dic):
    dic1 = {}
    for k in dic:
        k1 = "\033[1;36m"+str(k)+"\033[0m"
        dic1[k1] = "\033[1;32m"+str(dic[k])+"\033[0m"
    max1 = 0
    max2 = 0
    for k in dic1:
        if len(str(k).encode('GBK')) > max1:
            max1 = len(str(k).encode('GBK'))
        if len(str(dic1[k]).encode('GBK')) > max2:
            max2 = len(str(dic1[k]).encode('GBK'))
    if max1 < 25:
        max1 = 25
    if max2 < 25:
        max2 = 25
    print("-"*(max1+max2-16))
    for k in dic1:
        print('| {a:<{len1}} | {b:<{len2}}|'.format(a = k,b =dic1[k] ,len1=max1-len(str(k).encode('GBK'))+len(k),len2=max2-len(str(dic1[k]).encode('GBK'))+len(str(dic1[k]))))
    print("-"*(max1+max2-16))