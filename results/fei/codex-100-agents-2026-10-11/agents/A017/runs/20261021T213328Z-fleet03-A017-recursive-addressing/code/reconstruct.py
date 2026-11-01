"""Second representation: direct characters, actual Boolean words and GL(3,2)."""
from pathlib import Path
from itertools import product
from fractions import Fraction
from collections import Counter
import json,time,hashlib
R=Path(__file__).resolve().parents[1]
def transform(a):
    return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(a)) for s in range(len(a))]
def cost(v):
    p=q=1
    for t,u in v:
        if t+u:p*=(t+u)**(t+u)
        if t:q*=t**t
        if u:q*=u**u
    return p,q
def phase(word):
    q,l,c=word
    return [(-1)**((q*(t==3)+(l&t).bit_count()+c)%2) for t in range(4)]
def ledger(f):
    W=transform(f);assert all(w%4==0 for w in W)
    return cost([(W[j]**2//16,W[j+1]**2//16) for j in range(0,64,2)])
def main():
    start=time.perf_counter();checks=cases=0;digest=hashlib.sha256()
    # Recheck ALL 192 one-intrusion scalar rows using direct character sums.
    results={}
    for c in [0,2,-2]:
        best=None
        for tail in product([-1,1],repeat=6):
            H=[1,c]+list(tail); A=[w-1 for w in transform(H)];p,q=cost([(v*v,1) for v in A])
            if best is None or p*best[1]>best[0]*q:best=(p,q,Counter(v*v for v in A))
            cases+=1;checks+=1
        assert best[2]==({0:2,4:4,16:2} if c==0 else {4:4,16:4});checks+=1;results[str(c)]={'P':str(best[0]),'Q':str(best[1])}
    sigma=[1,1,1,-1];covered={0,1,2,3,5,6};count_by_k={}
    for k in range(8):
        count_by_k[k]=0
        for seed in range(64):
            slices=[phase((1,0,0))]
            for z in range(1,8):slices.append(phase((int(z>k),(seed+z*3)&3,((seed>>(z%6))^z)&1)))
            child=[slices[z][t] for z in range(8) for t in range(4)]
            f=[child[u]*(-1 if s and u//4==0 else 1) for u in range(32) for s in range(2)]
            p,q=ledger(f); pp=qq=1
            Hrows=[]
            for row in range(4):
                H=[sigma[row]*transform(slices[z])[row]//2 for z in range(8)]
                assert H[0]==1;Hrows.append(H)
                A=[w-1 for w in transform(H)];a,b=cost([(v*v,1) for v in A]);pp*=a;qq*=b
            assert p*qq==pp*q;checks+=5
            assert sum(f[x]!=f[x^1] for x in range(64))==8;checks+=1
            if k in covered:assert p<=q<<128;checks+=1
            count_by_k[k]+=1;cases+=1;digest.update(bytes(int(v<0) for v in f))
    witness=json.loads((R/'out/boolean_counterexample.json').read_text(encoding='utf-8'))['truth_table'];p,q=ledger(witness)
    for a,b,c in product(range(1,8),repeat=3):
        L=[(a if z&1 else 0)^(b if z&2 else 0)^(c if z&4 else 0) for z in range(8)]
        if len(set(L))!=8:continue
        f=[witness[(x&7)|(L[x>>3]<<3)] for x in range(64)]
        pp,qq=ledger(f);assert p*qq==pp*q;checks+=1;cases+=1
    out={'status':'PASS','total_cases':cases,'assertions':checks,'scalar_rows':192,'actual_parent_cases_by_intrusion_count':count_by_k,'invertible_z_maps':168,'covered_intrusion_counts':sorted(covered),'one_intrusion_row_maxima':results,'coverage_sha256':digest.hexdigest(),'elapsed_seconds':time.perf_counter()-start}
    assert cases==872
    (R/'out/reconstruction.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
if __name__=='__main__':main()
