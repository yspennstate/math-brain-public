"""A069 exact finite validation v1; standard library only."""
from pathlib import Path
from fractions import Fraction as F
import json, time, hashlib

RUN = Path(__file__).resolve().parents[1]
checks = 0
def ck(test):
    global checks
    assert test
    checks += 1

def fwht(a):
    a = a[:]
    h = 1
    while h < len(a):
        for k in range(0, len(a), 2*h):
            for j in range(k, k+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return a

def maj_tree(start, depth):
    if not depth:
        return start
    width = 3**(depth-1)
    return tuple(maj_tree(start+i*width,depth-1) for i in range(3))

def binary_tree(indices):
    if len(indices)==1:
        return indices[0]
    k = len(indices)//2
    return binary_tree(indices[:k]),binary_tree(indices[k:])

def leaves(t):
    if isinstance(t,int):
        return 1<<t
    return sum(leaves(c) for c in t)

def internals(t):
    if isinstance(t,int):
        return []
    return [(leaves(t),len(t))]+[v for c in t for v in internals(c)]

def encode(t,s):
    if not s:
        return '0'
    def walk(v):
        if isinstance(v,int):
            return ''
        mask = sum((1<<j) for j,c in enumerate(v) if leaves(c)&s)
        return format(mask-1,'0%db'%len(v))+''.join(walk(c) for j,c in enumerate(v) if mask>>j&1)
    return '1'+walk(t)

def decode(t,word):
    at=1
    if word[0]=='0':
        ck(len(word)==1)
        return 0
    def walk(v):
        nonlocal at
        if isinstance(v,int):
            return 1<<v
        b=len(v)
        mask=1+int(word[at:at+b],2)
        at += b
        ck(mask < 1<<b)
        return sum(walk(c) for j,c in enumerate(v) if mask>>j&1)
    s=walk(t)
    ck(at==len(word))
    return s

def value(t,x):
    if isinstance(t,int):
        return 1 if not (x>>t&1) else -1
    vals=[value(c,x) for c in t]
    return 1 if sum(vals)>0 else -1

def direct_influence(table,n):
    return sum(table[x]!=table[x^(1<<i)] for x in range(len(table)) for i in range(n))

def run():
    began=time.perf_counter()
    rows=[]
    cases=0
    for depth,domain in [(1,range(3,9)),(2,range(9,11))]:
        n=3**depth
        main=maj_tree(0,depth)
        for N in domain:
            size=1<<N
            tree=main if N==n else (main,binary_tree(list(range(n,N))))
            nodes=internals(tree)
            words=[encode(tree,s) for s in range(size)]
            lengths=[len(w) for w in words]
            for s,w in enumerate(words):
                ck(decode(tree,w)==s)
                ck(len(w)==1+sum(b for c,b in nodes if c&s))
            ordered=sorted(words)
            ck(all(not b.startswith(a) for a,b in zip(ordered,ordered[1:])))
            ck(sum((F(1,1<<len(w)) for w in words),F())<=1)
            ck(max(lengths)<=3*N-2)
            base=[value(main,x) for x in range(size)]
            a=fwht(base)
            den=size*size
            Ibase_num=sum(s.bit_count()*v*v for s,v in enumerate(a))
            Ig=F(Ibase_num,den)
            ck(Ig==F(3,2)**depth)
            ck(F(direct_influence(base,N),size)==Ig)
            Lg_num=sum(v*v*lengths[s] for s,v in enumerate(a))
            Lg=F(Lg_num,den)
            ck(Lg==1+6*(Ig-1)+(2 if N>n else 0))
            ck(Lg<=6*Ig-3)
            base_occupancy=[sum(v*v for s,v in enumerate(a) if s&c) for c,b in nodes]
            # Recursive-majority occupancy at every main-tree cell is exactly 2^{-level}.
            def level_check(t,level):
                c=leaves(t)
                ck(F(sum(v*v for s,v in enumerate(a) if s&c),den)==F(1,2)**level)
                if not isinstance(t,int):
                    for ch in t:
                        level_check(ch,level+1)
            level_check(main,0)
            for x in range(size):
                changed=base[:]
                changed[x]*=-1
                z=fwht(changed)
                # Rank-one point edit checked independently against the full truth-table transform.
                for s,v in enumerate(z):
                    ck(v==a[s]-2*base[x]*(-1 if (s&x).bit_count()%2 else 1))
                ck(sum(v*v for v in z)==den)
                Ifnum=sum(s.bit_count()*v*v for s,v in enumerate(z))
                If=F(Ifnum,den)
                ck(F(direct_influence(changed,N),size)==If)
                ck(abs(If-Ig)<=F(2*N,size))
                ck(If>=1-F(4,den))
                Lfnum=sum(v*v*lengths[s] for s,v in enumerate(z))
                ck(Lfnum<=2*Lg_num+8*sum(lengths))
                ck(F(Lfnum,den)<=25*If)
                if N>=6:
                    ck(F(Lfnum,den)<=12*If)
                for (c,b),bg in zip(nodes,base_occupancy):
                    fg=sum(v*v for s,v in enumerate(z) if s&c)
                    tail_num=4*(size-(1<<(N-c.bit_count())))
                    ck(fg<=2*bg+2*tail_num)
                cases+=1
            rows.append({'depth':depth,'N':N,'point_edits':size,'I_base':str(Ig),'L_base':str(Lg),'max_code_length':max(lengths)})
    elapsed=time.perf_counter()-began
    result={'helper_version':'A069-exact-v1','arithmetic':'integer Walsh, rational Fraction; no logarithmic numerical claims','cases':cases,'assertions':checks,'seconds':elapsed,'rows':rows,'result':'PASS'}
    (RUN/'out'/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    run()
