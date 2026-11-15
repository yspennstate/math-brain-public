"""Full-coordinate reconstruction, disjoint-edge checks and exact word integrals."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import factorial
from datetime import datetime,timezone
from functools import lru_cache
import json,ctypes,hashlib,time,random

ROOT=Path(__file__).resolve().parents[1]
def freeze(x):return tuple(freeze(y) for y in x) if isinstance(x,list) else x
def canon(word):
    labels={}
    return tuple((labels.setdefault(axis,len(labels)),sign) for axis,sign in word)
def positions(word):
    out=[(0,0,0)]
    for axis,sign in word:
        val=list(out[-1]);val[axis]+=sign;out.append(tuple(val))
    return out
def dist(x,y):return sum(abs(a-b) for a,b in zip(x,y))
def edge(x,y):return tuple(sorted((x,y)))

def description(word,selected,p=0):
    n=len(word);pts=positions(word);q=2*((n-3)//2)
    chords=[(i,i+3) for i in range(n-2) if dist(pts[i],pts[i+3])==1]
    cover=[sum(i<=j<k for i,k in chords) for j in range(n)]
    dirty=set();ends=set()
    for i,k in chords:
        v=i if i%2==0 else k;ends.add(v);dirty.update((v-2,v))
    for b in range(0,n-3,2):
        if dist(pts[b],pts[b+4])<=2:dirty.update((b,b+2))
    elig={b:word[b][0]!=word[b+1][0] and b not in dirty for b in range(0,n-1,2)}
    starts=list(range(q,n-1,2));I=q-1 in selected
    state=(n%2,canon(word[-3:]),tuple(cover[q:]),tuple(elig[b] for b in starts),
           (n if n%2==0 else n-1) in ends,
           tuple(b+1 in selected and b+3<=n for b in starts),I,p)
    return state,cover,elig,chords,q

@lru_cache(None)
def block(a,c0,c1,E,O,I,p,q):
    x,y=a+c0+I+E,a+c1+E+O;out=Q(0)
    for left in ((-1,0,1) if E else (-1,)):
        for right in ((-1,1,2) if O else (-1,)):
            if int(right==2)!=q:continue
            u=p+int(left==0);v=int(left==1)+int(right==1)
            out+=Q(factorial(u)*factorial(v),1)/(x**(u+1)*y**(v+1))
    return out

def main():
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(),0x4000)
    started=time.monotonic();graph_path=ROOT/'scripts/height_renewal_graph.json'
    graph=json.loads(graph_path.read_text(encoding='utf-8'))
    states=[freeze(s) for s in graph['states']];index={s:i for i,s in enumerate(states)}
    point_path=ROOT/'logs/height_bridge_tail_certificate.json'
    point=json.loads(point_path.read_text(encoding='utf-8'));a=Q(int(point['s']['n']),int(point['s']['d']))+1
    totals=Counter()

    def check(word,integrate=False):
        pts=positions(word);height=[sum(x) for x in pts];visits=Counter(height)
        selected={i for i in range(3,len(word)-1,2)
                  if visits[height[i+1]]==1 and word[i][1]==word[i+1][1]==1
                  and word[i][0]!=word[i+1][0]}
        if any(pts[k]==pts[k-j] for k in range(1,len(pts)) for j in (2,4) if k>=j):return
        totals['words']+=1
        if len(set(pts))==len(pts):
            _,_,elig,chords,_=description(word,selected)
            actual={edge(pts[i],pts[i+1]) for i in range(len(word))}
            chord_edges={edge(pts[i],pts[j]) for i,j in chords}
            used=set()
            for i in sorted({b for b,val in elig.items() if val}|selected):
                middle=tuple(pts[i][j]+pts[i+2][j]-pts[i+1][j] for j in range(3))
                alt={edge(pts[i],middle),edge(middle,pts[i+2])}
                assert len(alt)==2 and not alt&(actual|chord_edges|used),(word,i)
                used|=alt
            totals['simple_geometry']+=1
        coeff={0:Q(1)}
        for n in range(4,len(word)):
            old=description(word[:n],selected);new=description(word[:n+1],selected)
            mark=int(n-1 in selected);axis,sign=word[n]
            hist_axes={x[0] for x in word[n-3:n]};r=0 if axis in hist_axes else len(hist_axes)
            final=n%2==0;next_coeff={}
            for p in ((0,1) if old[0][6] else (0,)):
                src=old[0][:-1]+(p,);assert src in index
                possible=(0,1) if final and new[0][6] else ((0,) if final else (p,))
                for qp in possible:
                    dst=new[0][:-1]+(qp,);assert dst in index
                    if final:
                        b=old[4];c0,c1=new[1][b:b+2];E=new[2][b];O=b+1 in selected;I=src[6]
                        expected=(index[dst],sign,r,1,c0,c1,int(E),int(O),int(I),p,qp)
                        factor=block(a,c0,c1,E,O,I,p,qp)
                    else:
                        expected=(index[dst],sign,r,0,0,0,0,0,int(src[6]),p,p);factor=Q(1)
                    assert list(expected) in graph['rows'][index[src]][mark],(word,n,expected)
                    totals['transition_branches']+=1
                    if integrate:next_coeff[qp]=next_coeff.get(qp,Q(0))+coeff.get(p,Q(0))*factor
            if integrate:coeff=next_coeff
        if not integrate:return
        state,cover,elig,chords,q=description(word,selected)
        raw=sum(value/(a+state[6])**(p+1)*a**(-(len(word)-q-1)) for p,value in coeff.items())
        windows={b for b,val in elig.items() if val and b<q}|{b for b in selected if b<q}
        v0,v1=Q(1),Q(0)
        for j in range(len(word)):
            rate=a+(cover[j] if j<q else 0)+sum(b<=j<=b+1 for b in windows)
            active=int(j in windows)
            v0,v1=v0*(1/rate+active/rate**2)+v1*(1/rate**2+2*active/rate**3),active*(v0/rate+v1/rate**2)
        assert raw==v0 and v1==0,(word,raw,v0)
        totals['exact_word_integrals']+=1

    directions=((0,1),(0,-1),(1,1),(1,-1))
    for k,word in enumerate(product(directions,repeat=8)):
        check(word,k%997==0)
    for k,axes in enumerate(product((0,1),repeat=12)):
        word=tuple((axis,1) for axis in axes);check(word,k%97==0)
    rng=random.Random(170685)
    for k in range(512):
        word=tuple((rng.randrange(3),1) for _ in range(14));check(word,k%17==0)
    # Explicit long-fold obstruction from C012, under the present eligibility.
    check(((0,1),(1,1),(2,1),(2,1),(2,1),(0,-1),(2,-1),(2,-1),(2,-1),(1,1),(0,1)),True)
    out=dict(at=datetime.now(timezone.utc).isoformat(),counts=dict(totals),
             graph_sha256=hashlib.sha256(graph_path.read_bytes()).hexdigest(),
             point_sha256=hashlib.sha256(point_path.read_bytes()).hexdigest(),
             seconds=time.monotonic()-started,method='actual coordinates, all-prefix state reconstruction, direct alternative-edge intersections, independent per-edge moment integration',
             scope='finite validation, not a substitute for the all-length induction and independent review')
    (ROOT/'logs/height_renewal_word_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS full-coordinate renewal words',dict(totals),'seconds',out['seconds'],flush=True)

if __name__=='__main__':main()
