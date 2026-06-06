class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        lis = []
        
        dih = {}
        # list of list[str]
        for idx, i in enumerate(strs):
            for ch in i:
                dih[ch] = dih.get(ch, 0) + 1
            lis.append(dih)
            dih = {}
            
        retx = []
        ret = []
        for idx, i in enumerate(lis):
            flag = False
            for jdx, j in enumerate(retx):
                if i == j[0]:
                    ret[jdx].append(strs[idx])
                    retx[jdx].append(i)
                    flag = True
                    break
            if flag:
                continue
            ret.append([strs[idx]])
            retx.append([i])
        return ret
            
            
        
