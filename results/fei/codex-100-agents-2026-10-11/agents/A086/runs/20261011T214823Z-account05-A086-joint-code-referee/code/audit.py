"""Independent A086 reconstruction; no imported author checker."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, permutations
from math import comb, factorial
import json, time, hashlib

RUN=Path(__file__).resolve().parents[1]
OUT=RUN/'out'; OUT.mkdir(exist_ok=True)
checks=0
def ck(b):
    global checks
    checks+=1
    assert b, checks
def walsh(table):
    a=list(table); step=1
    while step<len(a):
        for k in range(0,len(a),2*step):
            for j in range(step):
                u,v=a[k+j],a[k+j+step]
                a[k+j],a[k+j+step]=u+v,u-v
        step*=2
    return {s:F(v,len(a)) for s,v in enumerate(a) if v}

def sunflower():
    nr=0
    for m in range(1,6):
        table=[1 if not (x&1) and any(not(x>>i&1) for i in range(1,m+1)) else -1 for x in range(1<<(m+1))]
        p={s:c*c for s,c in walsh(table).items()}
        ck(sum(p.values())==1)
        ck(sum(s.bit_count()*v for s,v in p.items())==1+F(m-1,2**m))
        for a in [F(2,5),F(1,2)]:
            D=(1+F(1,4*m))**m-1
            masses={}; residual={}; allkeys=set()
            for A in range(1,1<<(m+1)):
                coords=[j for j in range(m+1) if A>>j&1]
                options=[range(1,m+1) if j==0 else [j] for j in coords]
                total=F(0); sb=F(0)
                for owners in product(*options):
                    blocks={g:sum(1<<j for j,o in zip(coords,owners) if o==g) for g in set(owners)}
                    gates=sorted(blocks)
                    edges={(g,h) for g in gates for h in gates if g!=h and blocks[g]&((1<<h)|1)}
                    reach={(g,g) for g in gates}|edges
                    for k in gates:
                        reach|={(g,h) for g in gates for h in gates if (g,k) in reach and (k,h) in reach}
                    components=[]; unseen=set(gates)
                    while unseen:
                        g=min(unseen); c={h for h in gates if (g,h) in reach and (h,g) in reach}; components.append(c); unseen-=c
                    sources=[c for c in components if not any(h in c and g not in c for g,h in edges)]
                    for roots0 in product(*(sorted(c) for c in sources)):
                        roots=tuple(sorted(roots0)); nonroots=[g for g in gates if g not in roots]
                        for pars in product(*[[h for h in gates if (h,g) in edges] for g in nonroots]):
                            parent=dict(zip(nonroots,pars))
                            # Reject cycles rather than assuming a star.
                            valid=True
                            for g in nonroots:
                                seen=set(); h=g
                                while h in parent and h not in seen: seen.add(h); h=parent[h]
                                if h not in roots: valid=False
                            if not valid: continue
                            children={g:[h for h in nonroots if parent[h]==g] for g in gates}
                            for orders in product(*[list(permutations(children[g])) for g in gates]):
                                child=dict(zip(gates,orders)); queue=list(roots); trace=[]; prob=F(1,D)*(F(1,4*m)**len(roots)); bw=F(1,m**len(gates)*4**len(roots))
                                decoded=0
                                while queue:
                                    g=queue.pop(0); B=blocks[g]; s=B.bit_count(); c=len(child[g]); kappa=(A&((1<<g)|1)).bit_count()
                                    ck(s in [1,2]); ck(decoded&B==0); decoded|=B
                                    subset=F(1) if s==2 else (F(1) if B==1 else a)/(1+a)
                                    prob*=F(1,s*(s+1))*subset*F(1,(c+1)*(c+2))*F(1,comb(s+c-1,c))*F(1,m**c)
                                    # The only legal attachment coordinate for any edge is 0.
                                    ck(not c or B&1)
                                    if s==1 and kappa==2: bw*=a
                                    if B>>g&1 and not A&1: bw*=a
                                    trace.append((g,B,child[g])); queue.extend(child[g])
                                ck(decoded==A and len(trace)==len(gates))
                                key=(roots,tuple(trace)); ck(key not in allkeys); allkeys.add(key); nr+=1
                                total+=prob; sb+=bw
                t=(A>>1).bit_count()
                if A==1:
                    expected=F(1,16*(1+a)*D); ebs=F(1,4)
                elif not A&1:
                    expected=F(1,D)*(a/(16*m*(1+a)))**t; ebs=(a/(4*m))**t
                else:
                    win=F(factorial(t),24*D*t*t*(t+1)*m**t)*(a/(4*(1+a)))**(t-1)
                    wout=F((m-t)*factorial(t),8*D*m**(t+1)*(1+a)*(t+1)*(t+2))*(a/(4*(1+a)))**t
                    expected=win+wout
                    ebs=F(factorial(t),4*m**t)*a**(t-1)*(1+(1-F(t,m))*a)
                ck(total==expected); ck(sb==ebs); masses[A]=total; residual[A]=sb
            ck(sum(masses.values())<=1)
    return nr

def trees(depth,j=0):
    if depth==0: return [0,1]
    prev=trees(depth-1,j+1)
    return [0,1]+[(j,l,r) for l in prev for r in prev]

def leaf_spectrum(label,mode):
    if mode=='characters': return {1<<(3+label):F(1)}
    vals=[1 if label>>i&1 else -1 for i in [0,1]]
    return {s<<2:c for s,c in walsh(vals).items()}

def reconstruct(tree,mode):
    if isinstance(tree,int):
        spec=leaf_spectrum(tree,mode)
        # All leaves in these domains have exactly one Fourier atom.
        ck(len(spec)==1); s=next(iter(spec))
        return spec,[((),(),s,F(1))]
    j,left,right=tree
    u,wl=reconstruct(left,mode); v,wr=reconstruct(right,mode)
    spec={}; witness=[]
    for s in set(u)|set(v):
        plus=(u.get(s,0)+v.get(s,0))/2
        minus=(u.get(s,0)-v.get(s,0))/2
        if plus: spec[s]=plus
        if minus: spec[s|(1<<j)]=minus
    for branch,ws in enumerate([wl,wr]):
        for path,bits,s,p in ws:
            q=(u.get(s,0)**2+v.get(s,0)**2)/2
            ck(q>0)
            theta=(u.get(s,0)-v.get(s,0))**2/(4*q)
            ck(0<=theta<=1)
            for bit,r in [(0,1-theta),(1,theta)]:
                if r: witness.append(((branch,)+path,bits+(bit,),s|(bit<<j),p*r/2))
    return spec,witness

def evaltree(tree,x,mode):
    while not isinstance(tree,int):
        j,l,r=tree; tree=r if x>>j&1 else l
    if mode=='characters': return -1 if x>>(3+tree)&1 else 1
    return 1 if tree>>(x>>2&1)&1 else -1

def pathdict(tree,path=(),queries=()):
    if isinstance(tree,int): return [(path,queries,tree)]
    j,l,r=tree
    return pathdict(l,path+(0,),queries+(j,))+pathdict(r,path+(1,),queries+(j,))

def selectors():
    nt=0; nw=0; dup=0
    domains=[('characters',trees(3),5),('onebit',[(0,(1,a,b),(1,c,d)) for a,b,c,d in product(range(4),repeat=4)],3)]
    for mode,ts,n in domains:
        for tree in ts:
            spec,ws=reconstruct(tree,mode)
            table=[evaltree(tree,x,mode) for x in range(1<<n)]
            ck(spec==walsh(table))
            paths=pathdict(tree); dictionary={}; kraft=F(0)
            depth=F(0)
            for path,queries,label in paths:
                d=len(path); depth+=F(d,2**d)
                for bits in product([0,1],repeat=d):
                    word=path+bits
                    ck(word not in dictionary)
                    s=next(iter(leaf_spectrum(label,mode)))
                    for j,bit in zip(reversed(queries),bits): s|=bit<<j
                    dictionary[word]=s; kraft+=F(1,2**len(word))
            ck(kraft==1)
            words=list(dictionary)
            ck(all(not(len(a)<len(b) and b[:len(a)]==a) for a in words for b in words))
            marginal={}; leafmass={}; expected=F(0)
            for path,bits,s,p in ws:
                ck(dictionary[path+bits]==s)
                marginal[s]=marginal.get(s,0)+p
                leafmass[path]=leafmass.get(path,0)+p
                expected+=2*len(path)*p
            ck(marginal=={s:c*c for s,c in spec.items()}); ck(expected==2*depth)
            for path,_,_ in paths: ck(leafmass[path]==F(1,2**len(path)))
            influences=sum(F(sum(table[x]!=table[x^(1<<j)] for x in range(1<<n)),1<<n) for j in range(n))
            ck(influences==sum(s.bit_count()*c*c for s,c in spec.items()))
            nw+=len(ws); dup+=len(ws)-len(marginal); nt+=1
    return {'trees':nt,'positive_witnesses':nw,'duplicate_output_witnesses':dup}

def main():
    start=time.perf_counter()
    result={'sunflower_runs':sunflower(),'selector':selectors()}
    result.update(assertions=checks,seconds=time.perf_counter()-start,failures=0,arithmetic='integer FWHT and Fraction only')
    (OUT/'EXACT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__': main()
