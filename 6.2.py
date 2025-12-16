#====dictionary======
def func6201(lst):
    d={i[0]:[] for i in lst}
    for x in lst:
        d[x[0]].append(x)
    return d
def ave(i):
    new=i[1::]
    ave_=sum(new)/len(new)
    return round(ave_,1)
def func6202(lst):
    res=[]
    for i in lst:
        res.append({"name":i[0],"score":ave(i)})
    return res
def func6203(s):
    s_=list(s)
    d={i:0 for i in s}
    for x in s_:
        d[x]+=1
    return d

    pass

def func6204(dict1,dict2):
    res=[]
    for i in dict1:
        if i in dict2:
            res.append(i)

    return sorted(res)

def func6205(dict1,dict2):
    res=[]
    for i in dict1:
        for j in dict2:
            if dict1[i]==dict2[j] and i==j:
                res.append(i)
    return sorted(res)


    pass

def func6206(lst1, lst2):
    lst2=lst2[::-1]
    res={}
    name=[]
    num=18
    for i in range(len(lst1)):
        name.append(str(lst1[i])+" "+str(lst2[i]))
    for j in name:
        res[j]=num
        num+=1
    return res

def func6207(tp1, tp2):
    return dict(zip(tp1,tp2))
    pass

def func6208(prices, quantities):
    if prices=={} or quantities=={}:
        return 0
    cost=0
    for i in quantities:
        cost+=prices[i]*quantities[i]
    return cost

def func6209(employee_dict):
    res=[]
    for i in employee_dict:
        res.append((i,employee_dict[i]))
    res.sort(key=lambda x:x[1])
    return res    
    

#=====set==========
def func6210(set1, set2):
    res1=[]
    res2=[]
    lst=set(list(set1)+list(set2))
    for i in lst :
        if (i in set1 and i not in set2) or (i not in set1 and i in set2):
            res1.append(i)
        if i in set1 and i in set2:
            res2.append(i)
    return (tuple(sorted(res1)),tuple(sorted(res2,reverse=True)))
    pass

def func6211(set1, set2):
    res=[]
    lst=tuple(set(sorted(list(set1)+list(set2))))
    for i in lst:
        if i in set1 and i in set2:
            res.append(i)
    return (lst,tuple(sorted(res,reverse=True)))
    pass

if __name__=="__main__":
    print(func6201(["alpha", "all", "dig", "date", "egg"]))
    
    print(func6203("AABBC"))
    print(func6204({"key1": 100, "key2": 200}, {"key3": 300, "key4": 400}))
    print(func6205({"x": 10, "y": "20", "z": 30}, {"y": 20, "z": 30}))
    print(func6206(["Williams", "Brown", "Jones"], ["Isabella", "Sophia", "Mia"]))
    print(func6207(("Alice", "Bob", "Charlie"), (25, 30, 35)))
    print(func6208({}, {'milk': 1}))
    print(func6209({'Alice': 102, 'Bob': 101, 'Charlie': 103}))
    print(func6210({5, 6, 7}, {5, 6, 7}))
    print(func6211({1, 3, 5}, {2, 4, 6}))
    pass