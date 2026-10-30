"""Separate direct-moment spectra and Bellman-bound reconstruction."""
import json,time,sys
from pathlib import Path
from itertools import product
from fractions import Fraction as F
import reproduce as alt
from arithmetic import Q,scale,plus
from joint import truth,canonical,G
ROOT=Path(__file__).resolve().parents[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def main():
    start=time.perf_counter();tag=sys.argv[1];states=json.loads((ROOT/'out'/f'{tag}_STATES.json').read_text(encoding='utf-8'));out=[];known={};checks=0
    def ck(b):
        nonlocal checks
        assert b;checks+=1
    pending=sorted(states,key=lambda r:sum(t[1] for t in r['types']))
    for r in pending:
        pair=tuple(r['pair']);a,b=map(tuple,r['types']);ts=[(-1,),(1,)]+[G]*4;ts[pair[0]]=truth(a);ts[pair[1]]=truth(b)
        h,i,s=alt.full(tuple(ts));ck(i==F(r['I']));ck(h[0]<=r['H'][1] and r['H'][0]<=h[1]);ck(s[0]<=r['S4'][1] and r['S4'][0]<=s[1])
        stop=(max(0,-s[1]),max(0,-s[0]));lo,hi=stop
        # Generate EVERY physical next query from literal tables, not the primary row list.
        for axis,t in enumerate((a,b)):
            n=(len(truth(t))-1).bit_length()
            for coordinate in range(n):
                kids=[]
                for bit in (0,1):
                    table=truth(t);ct=tuple(table[(x&((1<<coordinate)-1))|((x>>coordinate)<<(coordinate+1))|(bit<<coordinate)] for x in range(1<<(n-1)))
                    typ=canonical(ct);key=(a,typ) if axis else (typ,b);kids.append(known[key])
                iv=scale(plus(*kids),F(1,2));lo=max(lo,iv[0]);hi=max(hi,iv[1])
        known[(a,b)]=(lo,hi);ck(lo<=r['hull'][1] and r['hull'][0]<=hi)
        out.append({'types':[a,b],'H':h,'I':str(i),'S4':s,'hull':(lo,hi)})
        ck(time.perf_counter()-start<55)
    root=known[(('L',6),('L',6))];src=next(r for r in states if r['types']==[['L',6],['L',6]])
    margins=[sub(src['hull'],row['mean_child_hull']) for row in src['rows']]
    # Root stopping identity is certified from independently computed child hulls.
    A=(-src['S4'][1],-src['S4'][0]);actual=[]
    for row in src['rows']:
        kids=[known[tuple(map(tuple,k))] for k in row['children']];m=sub(A,scale(plus(*kids),F(1,2)));ck(m[0]>0);actual.append(m)
    result={'pair':pair,'states':len(out),'checks':checks,'moment_checks':alt.checks,'root_margin_lower_units':[m[0] for m in actual],'runtime_seconds':time.perf_counter()-start,'independent_moment_spectra_and_all_physical_rows':True,'cases':out}
    (ROOT/'out'/f'{tag}_REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
if __name__=='__main__':main()
