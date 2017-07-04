Str1 = "aaabbcgfhh"
SubStrs = []
SubStrd_Dict = {}
for i in range(1,len(Str1)):
    #SubStrs.append(i)
    SubStrs = []
    for j in range(0,len(Str1)-i):
        SubStrs.append(Str1[j:j+i])
        #print SubStrs
    SubStrd_Dict[i] = SubStrs
    #print SubStrd_Dict
        
        
print SubStrd_Dict[3]
