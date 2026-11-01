"""Actual majority-three auxiliary replacement, integer Walsh verification."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as F
import json,time
from check import walsh,parity
ROOT=Path(__file__).resolve().parents[1]
def factor(n):
    out={};d=2
    while d*d<=n:
        k=0
        while n%d==0:n//=d;k+=1
        if k:out[d]=k
        d+=1
    if n>1:out[n]=1
    return out
def entropy_vector(w,size):
    out=defaultdict(F)
    for a in w:
        if not a:continue
        mass=F(a*a,size*size)
        for k,e in factor(mass.denominator).items():out[k]+=mass*e
        for k,e in factor(mass.numerator).items():out[k]-=mass*e
    return {k:v for k,v in out.items() if v}
def main():
    start=time.perf_counter();rows=[];checks=0
    for m in [2,3,4]:
        for masks in [(1,),((1<<m)-1,),(1,2),(1,1)]:
            r=len(masks);N=m+3*r;table=[]
            for z in range(1<<N):
                x=z&((1<<m)-1)
                for j,v in enumerate(masks):
                    block=(z>>(m+3*j))&7
                    if block.bit_count()>=2:x^=v
                table.append(-1 if x==0 else 1)
            a=walsh(table);size=1<<N
            I=sum(F(sum(table[x]!=table[x^(1<<j)] for x in range(size)),size) for j in range(N))
            assert I==F(2*m+3*r,1<<m);checks+=1
            base=entropy_vector(walsh([-1]+[1]*((1<<m)-1)),1<<m)
            base[2]=base.get(2,F(0))+F(4*r,1<<m)
            actual=entropy_vector(a,size)
            assert actual=={k:v for k,v in base.items() if v};checks+=1
            assert sum(a[s]**2*s.bit_count() for s in range(size))==I*size*size;checks+=1
            rows.append({'m':m,'auxiliary_masks':masks,'dimension':N,'I':str(I),'entropy_added_bits':str(F(4*r,1<<m))})
    out={'status':'PASS','helper':'A078-majority-padding-v1','cases':len(rows),'assertions':checks,'seconds':time.perf_counter()-start,'arithmetic':'actual truth tables, integer FWHT, rational prime-log vectors','rows':rows}
    (ROOT/'out'/'padding.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
