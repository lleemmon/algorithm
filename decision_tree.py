import math as m
import xlrd

# import tensorflow.compat.v1 as tf
# tf.disable_eager_execution()

keypos_list = []
all_route = []
value_index_dic = {}
index_value_dic = {}

def getdata(file):
    fp = xlrd.open_workbook(file)
    data = fp.sheets()[0]
    row = data.nrows
    X = []
    Y = []
    type_name = data.row_values(0)[:-1]
    for i in range(1, row):
        text = data.row_values(i)
        X.append(text[:-1])
        Y.append(text[-1])
    return type_name, X, Y

def decision_tree(X, Y, type_name):
    row = len(X)
    col = len(type_name)
    dic_y = {}
    if col == 0:#特征选取完了，就把路径丢到all——route种 采用值放入 直接丢keypos_list是引用 99行的弹出会导致值被清空
        temp = []
        for x in keypos_list:
            temp.append(x)
        all_route.append(temp)
        return#结束
    for i in range(row):#统计T和F的个数
        if Y[i] not in dic_y:
            dic_y[Y[i]] = 1
        else:
            dic_y[Y[i]] += 1
    p = 0
    for one in dic_y:
        p -= dic_y[one] / row * m.log(dic_y[one] / row, 2)
    print("总熵:%.4f" % p)
    if p == 0:#shang为0无需再分
        print("此部分已最优，无需划分")
        return
    increase = 0
    key_pos = 0
    dic_all = []
    for i in range(col):
        dic_x = {}
        for j in range(row):
            index = value_index_dic[type_name[i]]#找到下标对应的特征值下标
            if X[j][index] not in dic_x:
                dic_x[X[j][index]] = [j, ]
            else:
                dic_x[X[j][index]].append(j)
        dic_all.append(dic_x)#将每个属性的分布情况丢到总字典，后续划分比较容易
        temp = 0
        for one in dic_x:
            dic_xx = {}
            for ones in dic_x[one]:
                if Y[ones] not in dic_xx:
                    dic_xx[Y[ones]] = 1
                else:
                    dic_xx[Y[ones]] += 1#统计在该特征下 T和F各自的个数
            count = 0
            for elem in dic_xx:
                count += dic_xx[elem]
                print(count)
            for elem in dic_xx:
                temp -= dic_xx[elem] / row * m.log(dic_xx[elem] / count, 2)
        print("%s的信息增益为%.4f" % (type_name[i], p - temp))
        if increase < p - temp:
            increase = p - temp
            key_pos = i
    print("优先特征为%s,信息增益为%.4f\n" % (type_name[key_pos], increase))
    keypos_list.append(value_index_dic[type_name[key_pos]])#填入优先特征的下标
    type_name = type_name[0: key_pos] + type_name[key_pos + 1:]#去除该特征
    NEW_X = []#将X按照最优特征进行划分
    NEW_Y = []#将Y按照最优特征进行划分
    for x in dic_all[key_pos]:
        print("x=",x)
        tempx = []
        tempy = []
        for one in dic_all[key_pos][x]:
            tempx.append(X[one])
            tempy.append(Y[one])
        NEW_X.append(tempx)
        NEW_Y.append(tempy)
    print(dic_all[key_pos])
    LEN = len(NEW_X)
    for i in range(LEN):
        if p - increase > 0.0001:#信息增益>0.0001才进行递归子序列划分
            decision_tree(NEW_X[i], NEW_Y[i], type_name)
        else:#直接中断划分
            temp = []
            for x in keypos_list:
                temp.append(x)
            all_route.append(temp)
    keypos_list.pop()#BFS常用模板 与74
    # 行配对使用 弹走末尾的数，腾出新的为止给其他路径

if __name__ == "__main__":
    type_name, X, Y = getdata("data.xls")
    for i in range(len(type_name)):
        value_index_dic[type_name[i]] = i#构建值映射下标的字典
        index_value_dic[i] = type_name[i]#构建下标映射值的字典
    decision_tree(X , Y, type_name)
    print("\n最终特征排序为:")
    for x in all_route:#打印出过程中的所有路径，根据路径人工构建一棵查询树（可能会有相同的路径）
        for i in x:
            print("%s" % index_value_dic[i], end = " ")
        print("")