def L1_8_03(s1,s2):
    len_=0
    start=0
    s1=s1*2
    s2=s2*2
    res=[]
    for i_ in range(len(s1)):
        for j_ in range(len(s2)):
            i=i_
            j=j_
            if s1[i]==s2[j]:
                start=i
            while i<len(s1) and j<len(s2) and s1[i]==s2[j]:
                i+=1
                j+=1
                
            else:
                if s1[start:i] in s2:
                    res.append(s1[start:i])
                if 1+i-start>len_:
                    len_=i-start+1
                else:
                    pass
    max_len=max(list(map(len,res)))
    res_=[k for k in res if len(k)==max_len]
    if res_==[]:
        return ""
    return res_[0]
if __name__=="__main__":
    print(L1_8_03("ABCEFAGADEGKABUVKLM","MADJKUVKL"))
    print(L1_8_03("ABC","DEF"))
