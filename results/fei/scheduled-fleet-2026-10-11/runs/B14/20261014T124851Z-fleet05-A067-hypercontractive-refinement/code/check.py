import argparse,hashlib,itertools,json,time
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
PRIOR=ROOT.parent/'20261013T222025Z-fleet05-A067-hypercontractive-refinement/code/check.py'
ns={'__file__':str(Path(__file__).resolve())};exec(PRIOR.read_text().split('def masks(')[0],ns)
START=time.perf_counter();COUNT=0;LIMIT=600
def ck(b):
    global COUNT
    COUNT+=1;assert b;assert time.perf_counter()-START<LIMIT
ns['check']=ck
fwht=ns['fwht'];physical=ns['physical'];combine=ns['combine']
@lru_cache(None)
def ent(weights,den):return ns['entropy'](weights,den)
def H(a,den=None):return ent(tuple(sorted(c*c for c in a)),len(a)**2 if den is None else den)
@lru_cache(None)
def endpoints(items):return ns['interval'](dict(items))
def interval(p):return endpoints(tuple(sorted(p.items())))
def lower(p):return interval(p)[0]
def upper(p):return interval(p)[1]
def pos(p):ck(not p or lower(p)>=0)
def linear(x):return {2:Q(x)} if x else {}
def rank(rows):
    rows=list(rows);r=0
    for j in range(len(rows)):
        pivot=next((k for k in range(r,len(rows)) if rows[k]>>j&1),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        for k in range(len(rows)):
            if k!=r and rows[k]>>j&1:rows[k]^=rows[r]
        r+=1
    return r
def phases(n):
    pairs=list(itertools.combinations(range(n),2))
    for edges in range(1<<len(pairs)):
        rows=[0]*n;quadratic=[0]*(1<<n)
        for j,(a,b) in enumerate(pairs):
            if edges>>j&1:
                rows[a]|=1<<b;rows[b]|=1<<a
                for x in range(1<<n):quadratic[x]^=((x>>a)&1)*((x>>b)&1)
        R=rank(rows)
        for lin in range(1<<n):
            for const in [0,1]:
                yield R,edges,lin,const,[(-1)**(quadratic[x]+((x&lin).bit_count()%2)+const) for x in range(1<<n)]
def selector(b,R):
    n=len(b).bit_length()-1;N=n+1;e=Q(1,len(b));s=b[0]
    edited=list(b);edited[0]=-s;v=edited+b
    a=fwht(v);den=len(v)**2;dcore=fwht(b);child=fwht(edited)
    ck(sum(c*c for c in a)==den)
    ck(sum(bool(c) for c in dcore)==1<<R);ck(all(c*c==(len(b)**2>>R) for c in dcore if c))
    ck(a==[2*c-2*s for c in dcore]+[-2*s]*len(b))
    ephys=physical(v,[n]);IX=physical(v,range(n));ck(ephys==e)
    marg=[a[t]**2+a[t+len(b)]**2 for t in range(len(b))]
    hr=ent(tuple(sorted(marg)),den);hroot=H(a);hc=combine((H(dcore),Q(1,2)),(H(child),Q(1,2)))
    B=combine((hroot,Q(1)),(hr,Q(-1)));J=combine((hr,Q(1)),(hc,Q(-1)))
    bank=combine((linear(4*IX),Q(1)),(hr,Q(-1)))
    pos(J)
    if R:
        pos(bank)
        margin=combine((linear(4*e),Q(1)),(bank,Q(1,2)),(B,Q(-1)));pos(margin)
        if n>=5:pos(combine((bank,Q(1)),(linear(R*(1-6*e)-3*e),Q(-1))))
    else:
        margin=combine((linear(3*e),Q(1)),(B,Q(-1)));pos(margin)
    pos(combine((linear(4*(IX+e)),Q(1)),(hroot,Q(-1))))
    return {'rank':R,'n':n,'I_X':str(IX),'I_z':str(e),'bank_lower':str(lower(bank)),'paid_margin_lower':str(lower(margin))}
def obstruction(m):
    n=2*m+1;size=1<<n;delta=Q(1,size)
    b=[(-1)**sum(((x>>(2*j+1))&1)*((x>>(2*j+2))&1) for j in range(m)) for x in range(size)]
    # x bit0 is informative dummy w, z is the fresh bit.
    row=selector(b,2*m)
    edited=b[:];edited[0]=-b[0];v=edited+b;a=fwht(v);den=len(v)**2
    B=combine((H(a),Q(1)),(ent(tuple(sorted(a[t]**2+a[t+size]**2 for t in range(size))),den),Q(-1)))
    pos(combine((B,Q(1)),(linear((m+Q(3,2))*delta),Q(-1))))
    ck(physical(v,range(n+1))==m+(2*m+2)*delta)
    ck(upper(H(a))<=3*physical(v,range(n+1)))
    # Build actual coupled parent and its c=0 restriction without author code.
    parent=[]
    for z in range(2):
        for x in range(1<<(n+1)):
            c=x&1;w=(x>>1)&1;Y=x>>2
            sign=(-1)**(c*w+sum(((Y>>(2*j))&1)*((Y>>(2*j+1))&1) for j in range(m)))
            if z==0 and x==0:sign=-sign
            parent.append(sign)
    ck([parent[(x<<1)+(z<<(n+1))] for z in range(2) for x in range(size)]==v)
    return {'m':m,'conditional_flag_rate_lower':str(lower(B)/delta),**row}
def main():
    global LIMIT
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=['pilot','full'],required=True);mode=p.parse_args().mode;LIMIT=60 if mode=='pilot' else 600
    cases=0;minimum=None;rankcounts=Counter();fixtures=[]
    for n in range(4 if mode=='pilot' else 6):
        for R,edges,lin,const,b in phases(n):
            row=selector(b,R);cases+=1;rankcounts[(n,R)]+=1
            if len(fixtures)<5:fixtures.append(row)
            value=Q(row['paid_margin_lower']);minimum=value if minimum is None else min(minimum,value)
    obs=[obstruction(m) for m in ([2] if mode=='pilot' else [2,3,4,5])]
    affine=[selector([1]*(1<<n),0) for n in (range(1,4) if mode=='pilot' else range(1,9))]
    if mode=='full':ck(Q(affine[-1]['bank_lower'])<0)
    result={'mode':mode,'helper_version':2,'quadratic_selector_cases':cases,'A088_reconstruction_cases':len(obs),'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'rank_counts':{str(k):v for k,v in rankcounts.items()},'min_margin_lower':str(minimum),'fixtures':fixtures,'post_exposure':obs,'affine_guards':affine,'prior_helper_sha256':hashlib.sha256(PRIOR.read_bytes()).hexdigest()}
    (ROOT/'out'/('CHECK_'+mode.upper()+'.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['fixtures','post_exposure','rank_counts']}))
if __name__=='__main__':main()
