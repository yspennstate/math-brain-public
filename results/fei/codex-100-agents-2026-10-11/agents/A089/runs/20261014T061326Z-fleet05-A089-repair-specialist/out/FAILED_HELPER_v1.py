from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
from arithmetic import fwht,log2,scale,plus,Q,ceildiv
ROOT=Path(__file__).resolve().parents[1]
H=tuple(-1 if x in {0,1,2,4,8,16,32,6,17,40} else 1 for x in range(64))
G=tuple(-1 if x<3 else 1 for x in range(64))
K=4;tests=0
def ck(b):
    global tests
    assert b;tests+=1
def signed(iv,r):
    if r>=0:return scale(iv,r)
    lo,hi=scale(iv,-r);return -hi,-lo
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def const(x):return signed((Q,Q),F(x))
def ent(masses):
    iv=(0,0)
    for z in masses:
        if z:iv=plus(iv,scale(log2(1/z),z))
    return iv
def child(truth,i,b):
    n=(len(truth)-1).bit_length()
    return tuple(truth[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(1<<(n-1)))
@lru_cache(None)
def core(truth):
    n=(len(truth)-1).bit_length();co=fwht(list(truth));di=[]
    ck(sum(x*x for x in co)==1)
    for i in range(n):
        d=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(len(truth))),len(truth))
        ck(sum(z*z for T,z in enumerate(co) if T>>i&1)==d);di.append(d)
    hg=ent([x*x for x in co]);I=sum(di);s=sub(const(4*I),hg)
    ck(s[0]>=0)
    return {'p':F(sum(x==-1 for x in truth),len(truth)),'H':hg,'I':I,'d':di,'S':s}
@lru_cache(None)
def outer(tag,ps):
    truth=H if tag=='h' else tuple(-H[x^1] for x in range(64))
    co=fwht(list(truth));ms=[1-2*p for p in ps];vs=[1-m*m for m in ms]
    raw=[];masses=[]
    for T in range(64):
        c=F(0)
        for U in range(64):
            if U&T!=T:continue
            term=co[U]
            for j in range(6):
                if (U^T)>>j&1:term*=ms[j]
            c+=term
        w=F(1)
        for j in range(6):
            if T>>j&1:w*=vs[j]
        raw.append(c);masses.append(w*c*c)
    ck(sum(masses)==1)
    # Taylor coefficients reconstruct even unsupported truth points at endpoint biases.
    for x in range(64):
        val=F(0)
        for T,c in enumerate(raw):
            term=c
            for j in range(6):
                if T>>j&1:term*=1-2*(x>>j&1)-ms[j]
            val+=term
        ck(val==truth[x])
    qs=[]
    for j in range(6):
        q=F(0)
        for x in range(64):
            if x>>j&1 or truth[x]==truth[x|1<<j]:continue
            prob=F(1)
            for k in range(6):
                if k!=j:prob*=ps[k] if x>>k&1 else 1-ps[k]
            q+=prob
        ck(sum(masses[T] for T in range(64) if T>>j&1)==vs[j]*q)
        qs.append(q)
    C=ent(masses)
    for q,v in zip(qs,vs):C=sub(C,scale(ent([v,1-v]),q))
    return {'q':qs,'C':C,'masses':masses}
def composed(profile,cores):
    hf=profile['C'];I=F(0)
    for q,g in zip(profile['q'],cores):hf=plus(hf,scale(g['H'],q));I+=q*g['I']
    return hf,I
def main():
    start=time.perf_counter();cg=core(G);records=[]
    cases=[('J',0,0),('J',0,2)] if '--pilot' in sys.argv else [(tag,j,i) for tag in ['h','J'] for j in [0,1] for i in [0,2]]
    for tag,j,i in cases:
        parent=outer(tag,(cg['p'],)*6);parents=[cg]*6;hf,I=composed(parent,parents)
        q=parent['q'][j];ck(q>0)
        children=[];avail=[];corrects=[];cores=[];hs=[];infs=[];other_margins=[]
        for b in [0,1]:
            gc=core(child(G,i,b));cs=parents.copy();cs[j]=gc
            ps=tuple(x['p'] for x in cs);op=outer(tag,ps);hh,ii=composed(op,cs)
            ck(op['q'][j]==q)
            other=(0,0)
            for l in range(6):
                if l!=j:other=plus(other,scale(cg['S'],op['q'][l]))
            margin=sub(other,op['C'])
            ck(margin[0]>0) # The selected child core slack has not paid outer costs.
            ck(sub(const(4*ii),hh)[0]>=0)
            children.append({'p':str(gc['p']),'H_core':gc['H'],'I_core':str(gc['I']),'S4_core':gc['S'],'q':[str(x) for x in op['q']],'C':op['C'],'other_bank':other,'other_bank_minus_C':margin,'H_full':hh,'I_full':str(ii)})
            cores.append(gc);avail.append(scale(gc['S'],q));corrects.append(op['C']);hs.append(hh);infs.append(ii);other_margins.append(margin)
        for l in range(6):ck((F(children[0]['q'][l])+F(children[1]['q'][l]))/2==parent['q'][l])
        ck(I-(infs[0]+infs[1])/2==q*cg['d'][i])
        avgH=scale(plus(hs[0],hs[1]),F(1,2));DH=sub(hf,avgH)
        e=sub(DH,const(4*q*cg['d'][i]));ck(e[0]>0)
        DC=sub(parent['C'],scale(plus(corrects[0],corrects[1]),F(1,2)))
        dhg=sub(cg['H'],scale(plus(cores[0]['H'],cores[1]['H']),F(1,2)))
        formula=plus(scale(sub(dhg,const(4*cg['d'][i])),q),DC)
        ck(e[0]<=formula[1] and formula[0]<=e[1])
        bank=scale(plus(avail[0],avail[1]),F(1,2))
        margin=sub(scale(bank,F(2,5)),e);ck(margin[0]>0)
        remain=sub(bank,e);ck(remain[0]>0)
        ck(sub(const(4*I),hf)[0]>0)
        frac=(e[0]*Q//bank[1],ceildiv(e[1]*Q,bank[0]))
        records.append({'gate':tag,'block':j,'coordinate':i,'parent_S4_core':cg['S'],'q':str(q),'physical_influence':str(q*cg['d'][i]),'delta_C':DC,'full_query_excess_K4':e,'available_queried_child_bank':bank,'fraction_of_bank_spent_interval':frac,'cap_2_over_5_payment_margin':margin,'remaining_bank':remain,'children':children,'H_parent':hf,'I_parent':str(I)})
        (ROOT/'out'/('PILOT_CASES.json' if '--pilot' in sys.argv else 'CASES.json')).write_text(json.dumps(records,indent=2)+'\n')
        assert time.perf_counter()-start<55
    out={'version':'physical-child-bank-v1','scale_bits':192,'cases':len(records),'exact_assertions_passed':tests,'failed':0,'runtime_seconds':time.perf_counter()-start,'bank_fraction_upper':'2/5','minimum_payment_margin_interval_units':min(r['cap_2_over_5_payment_margin'][0] for r in records),'largest_spent_fraction_interval_units':max(r['fraction_of_bank_spent_interval'][1] for r in records)}
    (ROOT/'out'/('PILOT.json' if '--pilot' in sys.argv else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
