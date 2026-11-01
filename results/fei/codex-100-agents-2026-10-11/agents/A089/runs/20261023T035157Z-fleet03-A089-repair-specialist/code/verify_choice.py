"""Rebuild adaptive choice envelope from the separate moment certificates."""
from joint import ROOT,TYPES,truth,canonical,child,Q
from functools import lru_cache
import json,time
def main():
    start=time.perf_counter();db={};checks=0
    def ck(b):
        nonlocal checks
        assert b;checks+=1
    for p in (ROOT/'out').glob('PAIR_*_REPRODUCTION.json'):
        data=json.loads(p.read_text(encoding='utf-8'));pair=tuple(data['pair'])
        for r in data['cases']:db[(pair,tuple(map(tuple,r['types'])))]=r
    def node(j,t,k,u):return db[(tuple(sorted((j,k))),(t,u) if j<k else (u,t))]
    def physical(t):
        table=truth(t);ans=[]
        for i in range((len(table)-1).bit_length()):ans.append(tuple(canonical(child(table,i,b)) for b in (0,1)))
        return ans
    @lru_cache(None)
    def bound(j,t):
        k=next(k for k in range(2,6) if k!=j);s=node(j,t,k,('L',6))['S4'];candidates=[max(0,-s[0])]
        for a,b in physical(t):candidates.append((bound(j,a)[0]+bound(j,b)[0]+1)//2)
        for k in range(2,6):
            if k==j:continue
            for a,b in physical(('L',6)):candidates.append((node(j,t,k,a)['hull'][1]+node(j,t,k,b)['hull'][1]+1)//2)
        return max(candidates),candidates[1:]
    margins=[]
    for j in range(2,6):
        for t in TYPES:bound(j,t)
        k=next(k for k in range(2,6) if k!=j);a=-node(j,('L',6),k,('L',6))['S4'][1]
        for u in bound(j,('L',6))[1]:ck((a-u)*100000>379*Q);margins.append(a-u)
    out={'independent_input_states':len(db),'choice_states':bound.cache_info().currsize,'physical_root_query_actions':len(margins),'checks':checks,'root_margin_rational_lower':'379/100000 bits','minimum_root_margin_units':min(margins),'runtime_seconds':time.perf_counter()-start,'passed':True}
    (ROOT/'out/CHOICE_REPRODUCTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
if __name__=='__main__':main()
