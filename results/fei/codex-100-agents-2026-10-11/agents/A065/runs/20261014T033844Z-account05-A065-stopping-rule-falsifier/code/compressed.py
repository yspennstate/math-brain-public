from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import kernel as c
import hashlib,json,time,sys

ROOT=Path(__file__).resolve().parents[1]
S=c.SCALE
PRICES=c.PRICES
RULES=c.RULES

@lru_cache(None)
def coefficients(t,s):
    N=len(t); L=N*(1<<s); w=c.walsh(t)
    counts=Counter()
    for z in w[1:]:
        if z:counts[abs(z)]+=1<<s
    z=w[0]-N
    if z and s:counts[abs(z)]+=(1<<s)-1
    z=L+w[0]-N
    if z:counts[abs(z)]+=1
    c.check(sum(v*v*num for v,num in counts.items())==L*L)
    return L,tuple(sorted(counts.items())),w[0]

@lru_cache(None)
def activation(t,s):
    N=len(t); n=N.bit_length()-1+s
    L,counts,w0=coefficients(t,s); lo=hi=0
    for v,num in counts:
        a,b=c.log_bounds(v);lo+=num*v*v*a;hi+=num*v*v*b
    h=(2*n*S-c.ceil(F(2*hi,L*L)),2*n*S-c.floor(F(2*lo,L*L)))
    base=c.stats(t)[1]
    ds=tuple(F(2*x,L) for x in base)
    dc=F(N-w0,L) if s else F(0)
    c.check(h[0]>=0 and h[1]<=n*S)
    return h,ds,dc

@lru_cache(None)
def symbolic(t,s):
    L,counts,w0=coefficients(t,s);n=L.bit_length()-1; d={2:F(2*n)}
    for v,num in counts:
        for p,e in c.factors(v).items():d[p]=d.get(p,F(0))-F(2*num*v*v*e,L*L)
    return tuple(sorted((p,z) for p,z in d.items() if z))

def ratio_symbolic(t,s,i,d):
    out=dict(symbolic(t,s))
    if i is None:
        pairs=[(bytes([0]),0),(t,s-1)]
    else:pairs=[(x,s) for x in c.children(t,i)]
    for x,r in pairs:
        for p,z in symbolic(x,r):out[p]=out.get(p,F(0))-z/2
    return {p:z/d for p,z in out.items() if z}

def raw_activation(t,s):
    return t+bytes(len(t)*((1<<s)-1))

def interval_ratio(q,d):
    return [c.floor(F(q[0],S)/d*10**10)/10**10,c.ceil(F(q[1],S)/d*10**10)/10**10]

def reserve(t,s,labels,controls,groups,rule):
    nodes=0;ties=0;root=None;max_ratio=(F(0),F(0));all_nodes=[]
    @lru_cache(None)
    def visit(t,s,labels,controls):
        nonlocal nodes,ties,root,max_ratio
        nodes+=1;h,ds,dc=activation(t,s)
        candidates=[(i,labels[i],d) for i,d in enumerate(ds) if d]
        if dc:candidates.append((None,controls[0],dc))
        if not candidates:return tuple((0,0) for _ in PRICES)
        def children(i):
            if i is None:return [(bytes([0]),0,(),()),(t,s-1,labels,controls[1:])]
            new=labels[:i]+labels[i+1:]
            return [(x,s,new,controls) for x in c.children(t,i)]
        def delta(i):
            pair=children(i)
            hh=[activation(x,r)[0] for x,r,_,_ in pair]
            return c.sub(h,c.half(c.add(*hh)))
        if rule=='min-influence':i,lab,d=min(candidates,key=lambda x:(x[2],x[1]))
        elif rule=='max-influence':i,lab,d=min(candidates,key=lambda x:(-x[2],x[1]))
        elif rule=='greedy-min-D-over-d':
            winner=None;best=None
            for cand in candidates:
                j,jlab,jd=cand;de=delta(j); rr=(F(de[0],S)/jd,F(de[1],S)/jd)
                if best is None or rr[1]<best[0]:winner=cand;best=rr
                elif rr[0]<=best[1]:
                    old,oldlab,oldd=winner
                    c.check(ratio_symbolic(t,s,j,jd)==ratio_symbolic(t,s,old,oldd));ties+=1
                    if jlab<oldlab:winner=cand;best=rr
            i,lab,d=winner
        else:
            order=['control','core','selector'] if rule=='control-first' else ['selector','control','core']
            i,lab,d=min(candidates,key=lambda x:(order.index(groups[x[1]]),x[1]))
        pair=children(i);qa,qb=[visit(*z) for z in pair]
        de=delta(i); I=sum(ds)+s*dc
        child_I=[]
        for x,r,_,_ in pair:
            _,di,ci=activation(x,r);child_I.append(sum(di)+r*ci)
        c.check(I==d+sum(child_I)/2)
        qs=tuple(c.pos(c.add(c.sub(de,c.exact(C*d)),c.half(c.add(a,b)))) for C,a,b in zip(PRICES,qa,qb))
        c.check(all(q[0]>=0 and q[1]<=h[1]+2*(len(labels)+s) for q in qs))
        rr=(F(de[0],S)/d,F(de[1],S)/d)
        if rr[1]>max_ratio[1]:max_ratio=rr
        rec={'core_hash':hashlib.sha256(t).hexdigest(),'s':s,'core_labels':labels,'controls':controls,'chosen':lab,'chosen_group':groups[lab],'d':str(d),'D_scaled':de,'Q_scaled':qs,'H_scaled':h,'I':str(I)}
        all_nodes.append(rec)
        if t==initial_t and s==initial_s and labels==initial_labels and controls==initial_controls:root=rec
        return qs
    initial_t=t;initial_s=s;initial_labels=tuple(labels);initial_controls=tuple(controls)
    qs=visit(t,s,initial_labels,initial_controls)
    h,ds,dc=activation(t,s);I=sum(ds)+s*dc
    return {'rule':rule,'dimension':len(labels)+s,'I_exact':str(I),'H_scaled':h,'Q_scaled':qs,'Q_over_I': [interval_ratio(q,I) for q in qs],'H_over_I':interval_ratio(h,I),'root':root,'maximum_node_D_over_d':[float(v) for v in max_ratio],'unique_nodes':nodes,'greedy_exact_ties':ties,'certificate_nodes':all_nodes}

def core_splice(k):return c.bent_defect(k,0)[0]
def and_splices(k,l,shared):
    a=core_splice(k);b=core_splice(l)
    if not shared:
        n=k+l+2
        t=bytes(a[v&((1<<(k+1))-1)] & b[v>>(k+1)] for v in range(1<<n))
        groups=['core']*k+['selector']+['core']*l+['selector']
    else:
        n=k+l+1
        t=bytes(a[(v&((1<<k)-1))|(((v>>(k+l))&1)<<k)] & b[((v>>k)&((1<<l)-1))|(((v>>(k+l))&1)<<l)] for v in range(1<<n))
        groups=['core']*(k+l)+['selector']
    return t,groups

def labels_for(groups,s):
    # Restore B05 original labels: core variables, controls, selector.
    first_selector=groups.index('selector')
    labels=[i if i<first_selector else i+s for i in range(len(groups))]
    controls=list(range(first_selector,first_selector+s))
    full={lab:groups[i] for i,lab in enumerate(labels)}
    full.update({lab:'control' for lab in controls})
    return labels,controls,full

def pilot():
    start=time.monotonic();tested=0
    for word in range(256):
        t=bytes((word>>i)&1 for i in range(8))
        for s in (0,1,2):
            h,ds,dc=activation(t,s); raw=raw_activation(t,s); rh,ri=c.stats(raw)
            c.check(h[0]<=rh[1] and rh[0]<=h[1])
            c.check(dict(symbolic(t,s))==c.symbolic_H(raw))
            c.check(ds==tuple(F(2*z,len(raw)) for z in ri[:3]))
            c.check(all(F(2*z,len(raw))==dc for z in ri[3:]));tested+=1
    old=json.loads((ROOT.parent/'20261011T230426Z-account05-A065-stopping-rule-falsifier'/'out'/'validation.json').read_text())
    comparisons=[]
    for k in (2,4):
        t=core_splice(k);groups=['core']*k+['selector'];s=2*k
        labels,controls,full=labels_for(groups,s)
        for rule in RULES:
            row=reserve(t,s,labels,controls,full,rule)
            ref=next(x for x in old['cases'] if x['family']==f'B05-k{k}' and x['rule']==rule)
            c.check(row['I_exact']==ref['I_exact'])
            for q,r in zip(row['Q_scaled'],ref['Q_scaled']):c.check(q[0]<=r[1] and r[0]<=q[1])
            c.check(row['root']['chosen']==ref['root_query'][0]['coordinate'])
            comparisons.append({'family':f'B05-k{k}','rule':rule,'Q_over_I':row['Q_over_I'],'nodes':row['unique_nodes']})
    out={'helper':'A065 compressed v2','raw_calibration_cases':tested,'saved_certificate_comparisons':comparisons,'assertions':c.ASSERTIONS,'elapsed_seconds':time.monotonic()-start}
    c.check(out['elapsed_seconds']<60)
    (ROOT/'out'/'PILOT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

def main():
    if '--pilot' in sys.argv:return pilot()
    start=time.monotonic();families=[]
    for k in (2,4,6):families.append((f'B05-k{k}',core_splice(k),['core']*k+['selector'],2*k))
    for k,l in ((2,2),(2,4),(4,4)):
        for shared in (False,True):
            t,g=and_splices(k,l,shared)
            for s in (0,2):families.append((f'AND-{k}-{l}-shared{int(shared)}-r{s}',t,g,s))
    out={'helper':'A065 compressed v2','scale':str(S),'prices':[str(x) for x in PRICES],'cases':[]}
    for name,t,g,s in families:
        labels,controls,groups=labels_for(g,s)
        for rule in RULES:
            row={'family':name,**reserve(t,s,labels,controls,groups,rule)}
            out['cases'].append(row);out['assertions']=c.ASSERTIONS;out['elapsed_seconds']=time.monotonic()-start
            (ROOT/'out'/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n')
            print(name,rule,row['Q_over_I'],row['unique_nodes'],flush=True)
        activation.cache_clear();coefficients.cache_clear();symbolic.cache_clear();c.stats.cache_clear();c.children.cache_clear();c.symbolic_H.cache_clear()
        c.check(time.monotonic()-start<1500)
    out['assertions']=c.ASSERTIONS;out['elapsed_seconds']=time.monotonic()-start
    out['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/'out'/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',out['assertions'],'seconds',out['elapsed_seconds'])

if __name__=='__main__':main()
