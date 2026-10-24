"""Direct finite three-core refund check; only pinned own arithmetic primitives."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,itertools,json,time
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
HELPER=ROOT/'runs/20261014T022245Z-account05-A023-amortized-rarity-budget/code/check_block.py'
spec=importlib.util.spec_from_file_location('own_exact',HELPER);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
START=time.perf_counter();COUNT=0
def ck(x):
    global COUNT
    assert x;COUNT+=1
    if time.perf_counter()-START>60:raise RuntimeError('Frozen sixty-second pilot cap')
def vec(v):return {str(p):str(c) for p,c in v.items()}
def save(n,x):(RUN/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def disagreement(g,k):return Q(sum(a!=b for a,b in zip(g,k)),len(g))
def product_inf(g,k):return h.inf(tuple(a*b for a,b in zip(g,k)))
def case(ids,cores,r,s):
    g0,g1,g2=cores;a,b=Q(1,1<<r),Q(1,1<<s);pi=[1-a,a*(1-b),a*b]
    child=h.point(g1,g2,s)
    # g0 replication must put each data value across low B-control slots.
    baseline=tuple(x for x in g0 for _ in range(1<<s));f=h.point(baseline,child,r)
    D01,D02,D12=(disagreement(cores[i],cores[j]) for i,j in [(0,1),(0,2),(1,2)])
    I01,I02,I12=(product_inf(cores[i],cores[j]) for i,j in [(0,1),(0,2),(1,2)])
    IA=2*r*a*((1-b)*D01+b*D02);IB=2*s*b*D12;IC=IA+a*IB
    IT=sum(p*h.inf(g) for p,g in zip(pi,cores));HT=h.add(*[(p,h.ent(g)) for p,g in zip(pi,cores)])
    ck(h.inf(f)==IC+IT)
    Rdata=2*a*(1-a)*((1-b)*I01+b*I02)+2*a*b*(1-b)*I12
    Rcontrol=2*a*(1-a)*IB
    Rstar=2*(pi[0]*pi[1]*I01+pi[0]*pi[2]*I02+pi[1]*pi[2]*I12)
    surcharge=2*a*(1-a)*b*(1-b)*I12
    ck(Rdata==Rstar+surcharge);ck(Rstar<=2*IT)
    # Physical outer product influence, including untouched inner controls.
    outerprod=tuple(x*y for x,y in zip(baseline,child))
    ck(h.inf(outerprod)==(1-b)*I01+b*I02+IB)
    ck(2*a*(1-a)*h.inf(outerprod)+2*a*b*(1-b)*I12==Rdata+Rcontrol)
    rates=[2*a,2*(1-a+b),2*(2-a-b)]
    ck(Rdata<=sum(p*rate*h.inf(g) for p,rate,g in zip(pi,rates,cores)))
    # Every core coordinate owns these capacities; no fresh branch copies.
    for i in range(2):
        ii=[Q(sum(g[x]!=g[x^(1<<i)] for x in range(4)),4) for g in cores]
        pp=[Q(sum((cores[j][x]*cores[k][x])!=(cores[j][x^(1<<i)]*cores[k][x^(1<<i)]) for x in range(4)),4) for j,k in [(0,1),(0,2),(1,2)]]
        data=2*a*(1-a)*((1-b)*pp[0]+b*pp[1])+2*a*b*(1-b)*pp[2]
        ck(data<=sum(p*rate*t for p,rate,t in zip(pi,rates,ii)))
    overhead=h.add((1,h.ent(f)),(-1,HT))
    sourcegap=h.add((1,overhead),(-1,h.rational(Q(11,2)*IC+Rdata+Rcontrol)))
    ck(h.sign(sourcegap)<=0)
    refundgap=h.add((1,overhead),(-1,h.rational(Q(11,2)*IC+Rstar)))
    sign=h.sign(refundgap)
    if sign>0:
        save('COUNTEREXAMPLE.json',{'ids':ids,'cores':cores,'r':r,'s':s,'gap':vec(refundgap),'certificate':h.SIGNS[tuple(sorted(refundgap.items()))]})
        raise RuntimeError('Actual Boolean refund counterexample saved')
    ck(sign<=0)
    return {'ids':ids,'r':r,'s':s,'pi':[str(p) for p in pi],'control_I':str(IC),'terminal_I':str(IT),
        'I01':str(I01),'I02':str(I02),'I12':str(I12),'R_star':str(Rstar),'R_data':str(Rdata),
        'control_reserve':str(Rcontrol),'grouping_surcharge':str(surcharge),
        'terminal_H':vec(HT),'actual_entropy_increment':vec(overhead),'refund_gap':vec(refundgap),'gap_sign':sign}
def main():
    tables=list(itertools.product([-1,1],repeat=4));nonconst=[i for i,g in enumerate(tables) if abs(sum(g))!=4]
    domain=[(ids,1,1) for ids in itertools.product(range(16),repeat=3)]
    domain +=[(ids,r,s) for ids in itertools.permutations(nonconst,3) for r,s in [(1,2),(2,1),(2,2)]]
    ck(len(domain)==10648);rows=[]
    with (RUN/'out/rows.jsonl').open('w',encoding='utf-8') as instant:
        for ids,r,s in domain:
            row=case(ids,[tables[i] for i in ids],r,s);rows.append(row);instant.write(json.dumps(row)+'\n');instant.flush()
    save('results.json',rows);save('sign_certificates.json',list(h.SIGNS.values()))
    out={'status':'PASS','cases':len(rows),'checks':COUNT,'unique_sign_certificates':len(h.SIGNS),
        'elapsed_seconds':time.perf_counter()-START,'zero_refund_gaps':sum(x['gap_sign']==0 for x in rows),
        'scope':'Finite declared two-bit-core/point-width domain only; no arbitrary-dimensional refund theorem'}
    save('validation.json',out);print(json.dumps(out))
if __name__=='__main__':main()
