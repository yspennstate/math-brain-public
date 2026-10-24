import argparse,json,time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];ASSERT=0
def ck(b):
    global ASSERT
    ASSERT+=1
    if not b:raise AssertionError(ASSERT)
def comp(n):
    if n==0:yield ();return
    for j in range(1,n+1):
        for rest in comp(n-j):yield (j,)+rest
@lru_cache(None)
def core(mask):return tuple(1 if mask>>x&1 else -1 for x in range(4))
@lru_cache(None)
def actual_edges(mask,t):
    g=core(mask);n=t+2;N=2**n
    tab=[g[x%4] if x//4==0 else 1 for x in range(N)]
    return tuple(F(2*sum(tab[x]!=tab[x+(1<<i)] for x in range(N) if not(x>>i&1)),N) for i in range(n))
def main(pilot):
    start=time.monotonic();cases=0;witnesses=[]
    for n in range(1,4 if pilot else 9):
        for widths in comp(n):
            for mask in range(16):
                g=core(mask);edge=actual_edges(mask,0);Ig=sum(edge);e=1-F(sum(g),4);p=F(1,2**n)
                root=actual_edges(mask,n)
                ck(root[:2]==tuple(p*d for d in edge));ck(all(z==p*e for z in root[2:]))
                ck(sum(root)==p*Ig+n*p*e)
                reach=F(1);data=ctrl=F(0);remaining=n
                for t in widths:
                    remaining-=t;a=F(1,2**t);child=actual_edges(mask,remaining)
                    mark=reach*2*a*(1-a)
                    data+=mark*sum(child[:2]);ctrl+=mark*sum(child[2:]);reach*=a
                aa=[F(1,2**t) for t in widths]
                ck(reach==p)
                expected_data=2*p*Ig*sum(1-a for a in aa)
                expected_ctrl=2*p*e*sum((1-a)*sum(widths[j+1:]) for j,a in enumerate(aa))
                ck(data==expected_data);ck(ctrl==expected_ctrl)
                folded=2*p*(1-p)*Ig;ck(data>=folded)
                if all(t==1 for t in widths):
                    ck(data==n*p*Ig);ck(ctrl==p*e*n*(n-1)/2)
                    if mask==10:witnesses.append({'n':n,'terminal_I':str(p*Ig),'split_data':str(data),'split_controls':str(ctrl),'folded_R':str(folded),'refund':str(data+ctrl-folded),'actual_removed_I':str(n*p*e),'actual_total_I':str(sum(root))})
                cases+=1
    out={'status':'PASS','pilot':pilot,'cases':cases,'assertions':ASSERT,'seconds':time.monotonic()-start,'arithmetic':'Independent undirected Boolean boundary enumeration and exact Fraction grouping identities','maximum_dimension':10,'fair_chain_dictator_witnesses':witnesses}
    (BASE/'out'/('grouping_pilot.json' if pilot else 'grouping.json')).write_text(json.dumps(out,indent=2));print(json.dumps(out),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');main(p.parse_args().pilot)
