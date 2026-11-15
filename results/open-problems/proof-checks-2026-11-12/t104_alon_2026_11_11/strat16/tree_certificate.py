"""Exact coefficient certificates for all three five-vertex tree types."""
import itertools
import json
import time
from pathlib import Path
from sympy.polys.rings import ring
from sympy.polys.domains import QQ

TREES={'star':[(0,1),(0,2),(0,3),(0,4)],
       'path':[(0,1),(1,2),(2,3),(3,4)],
       'fork':[(0,1),(0,2),(0,3),(3,4)],
       'four_star_and_isolate':[(0,1),(0,2),(0,3)],
       'four_path_and_isolate':[(0,1),(1,2),(2,3)],
       'three_path_and_two_isolates':[(0,1),(1,2)]}


def construct(edges):
    rr,a,b,c,d,h=ring('a,b,c,d,h',QQ);ts=(a,b,c,d)[:len(edges)];k=5+h
    sizes=[sum(t for e,t in zip(edges,ts)if i in e)for i in range(5)]
    signs=[None if any(i in e for e in edges)else 0 for i in range(5)];signs[0]=1
    while any(a is None for a in signs):
        for i,j in edges:
            if signs[i] is not None:signs[j]=-signs[i]
            elif signs[j] is not None:signs[i]=-signs[j]
    U=[sg*v for sg,v in zip(signs,sizes)];R=sum(v*v for v in U)
    denominators=[sizes[i]+sizes[j]for i,j in edges]
    D=rr.one
    for v in denominators:D*=v
    L=[[rr.zero for j in range(5)]for i in range(5)]
    for e,(i,j),t in zip(range(len(edges)),edges,ts):
        w=t
        for f in range(len(edges)):
            if e!=f:w*=denominators[f]
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    assert sum(U)==0
    assert all(sum(L[i][j]*U[j]for j in range(5))==D*U[i]for i in range(5))
    tr=sum(L[i][i]for i in range(5));tr2=sum(L[i][j]**2 for i in range(5)for j in range(5))
    B=sum(U[i]*U[j]*(int(i==j)*D-L[i][j])**2 for i in range(5)for j in range(5))
    hn=sum(U[i]**2*L[i][i]for i in range(5))+R*D/2
    Y=-2*sum(L[i][j]*(U[i]-U[j])**2*(2*D-L[i][i]-L[j][j]+2*L[i][j])for i in range(5)for j in range(i+1,5))
    num=2*R*k*k*(D*tr-tr2)+2*k*(k+2)*B-k*k*Y
    num+=(tr-D)/2*(2*(k+1)*(k-2)*R*D-2*k*R*(tr+D)+2*(k+2)*hn)
    return rr,U,D,num


def main():
    tick=time.monotonic();records=[]
    for name,edges in TREES.items():
        rr,U,D,num=construct(edges)
        bad=[(m,c)for m,c in num.items()if c<0]
        print(name,len(num),'negative',len(bad),flush=True)
        rec=dict(tree=name,terms=len(num),negative=len(bad),strict_witness=None)
        if not bad:
            # For positive four fluxes a monomial with h exponent zero
            # proves strict positivity, including k=5.
            witness=next((m for m,c in num.items()if c>0 and not m[4]),None)
            assert witness is not None;rec['strict_witness']=witness
            infinity=next((m for m,c in num.items()if c>0 and m[4]==2),None)
            assert infinity is not None;rec['infinity_strict_witness']=infinity
        else:
            for perm in itertools.permutations(range(4)):
                dest,*gs=ring('w,x,y,z,h',QQ);repl=[None]*5;repl[4]=gs[4]
                for j,i in enumerate(perm):repl[i]=sum(gs[j:4])
                out=dest.zero
                for m,c in num.items():
                    term=dest(c)
                    for v,e in zip(repl,m):term*=v**e
                    out+=term
                fails=sum(c<0 for c in out.values())
                print(name,perm,'negative',fails,flush=True)
                assert not fails
        records.append(rec)
    Path('tree_checks.json').write_text(json.dumps(dict(checks=records,seconds_NUMERICAL=time.monotonic()-tick),indent=2)+'\n')
    print('PROVED (tree_certificate.py): every connected five-vertex tree with a tied edge has T>0, k>=5 and infinity.')

if __name__=='__main__':main()
