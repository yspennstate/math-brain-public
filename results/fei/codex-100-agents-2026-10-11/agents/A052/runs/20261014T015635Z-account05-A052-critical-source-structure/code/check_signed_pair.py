import ast,json,itertools,time
from fractions import Fraction as F
from pathlib import Path
import phase_library as p
import exact_library as e
ROOT=Path(__file__).resolve().parents[1]; count=0
def ck(v):
    global count
    count+=1
    if not v:raise AssertionError(count)
def div(x,y):return x/y if y else F(0)
def quartet(a,b,c,d):
    q=a*a+b*b+c*c+d*d
    if not q:return {k:F(0) for k in ['Q','ci','cj','P','Mi','Mj','o','v']}
    ci=4*(div(a*a*b*b,a*a+b*b)+div(c*c*d*d,c*c+d*d))
    cj=4*(div(a*a*c*c,a*a+c*c)+div(b*b*d*d,b*b+d*d))
    P=4*(a*d+b*c)**2/q
    Q=4*((a*b+c*d)**2+(a*c+b*d)**2+(a*d+b*c)**2)/q
    Mi=ci-4*(a*b+c*d)**2/q;Mj=cj-4*(a*c+b*d)**2/q
    o=sum(max(F(0),x-y) for x,y in [(b*b,a*a),(d*d,c*c),(c*c,a*a),(d*d,b*b)])
    minority=min(a*a,b*b)+min(c*c,d*d)+min(a*a,c*c)+min(b*b,d*d)
    v=b*b+c*c+2*d*d
    ck(Mi>=0);ck(Mj>=0);ck(Q==ci+cj+P-Mi-Mj);ck(v==minority+o)
    ck(P<=2*v);ck(ci+cj>=2*minority);ck(Q<=2*(ci+cj)+2*o)
    ck(Mi==div(4*(a*b*(c*c+d*d)-c*d*(a*a+b*b))**2,q*(a*a+b*b)*(c*c+d*d)))
    ck(Mj==div(4*(a*c*(b*b+d*d)-b*d*(a*a+c*c))**2,q*(a*a+c*c)*(b*b+d*d)))
    return dict(Q=Q,ci=ci,cj=cj,P=P,Mi=Mi,Mj=Mj,o=o,v=v)
def one(v,i):
    r=p.block(v,1<<i);N=len(v);w=e.direct(v);beta=F(0);C=F(0)
    for s in range(N):
        if s>>i&1:continue
        a,b=F(w[s],N),F(w[s|(1<<i)],N);q=a*a+b*b
        if q:beta+=min(a*a,b*b);C+=4*a*a*b*b/q
    O=r['IA']-beta
    ck(C==r['C']);ck(2*beta<=C<=4*beta)
    upper=p.add(p.entropy([C/2,1-C/2]),{2:C})
    ck(p.sg(p.add(upper,r['L'],-1))>=0)
    reserves={}
    for K in (2,4,8):
        D=p.add(r['H'],{2:K*r['I']},-1);S={}
        for hc,ic,_ in r['children']:S=p.add(S,p.add(hc,{2:K*ic},-1),-F(1,2))
        left=p.add(p.add(D,S),{2:K*O})
        right=p.add(r['L'],{2:K*beta},-1)
        ck(left==right)
        rk=p.lograt(1+F(2)**(3-K))
        ck(p.sg(p.add(rk,left,-1))>=0)
        reserves[K]=(D,S,rk)
    return r,C,O,reserves
def pairs(v,name):
    n=len(v).bit_length()-1;N=len(v);w=[F(x,N) for x in e.direct(v)]
    single=[one(v,i) for i in range(n)];records=[]
    for i,j in itertools.combinations(range(n),2):
        A=(1<<i)|(1<<j);r=p.block(v,A);tot={k:F(0) for k in ['Q','ci','cj','P','Mi','Mj','o','v']}
        for t in range(N):
            if t&A:continue
            row=quartet(w[t],w[t|(1<<i)],w[t|(1<<j)],w[t|A])
            for k in tot:tot[k]+=row[k]
        ck(tot['Q']==r['C']);ck(tot['ci']==single[i][1]);ck(tot['cj']==single[j][1])
        ck(tot['o']==single[i][2]+single[j][2]);ck(tot['v']==r['IA'])
        ck(r['C']<=6*r['IA'])
        W0=Wg=Wb=F(0)
        for row in r['rows']:
            mass=F(row['q']);cr=F(row['collision_ratio'])-1;phase=row['phase_truth']
            if len(set(phase))==1:W0+=mass
            elif cr<=F(1,16):Wg+=mass
            else:Wb+=mass
        ck(W0+Wg+Wb==1);ck(Wb<=16*r['C'])
        for K in (4,8):
            left=p.add(r['L'],{2:K*r['IA']},-1);left=p.add(left,{2:(F(K,2)-2)*Wg})
            rhs=p.add(r['G'],p.lograt(1+3*F(2)**(-K)),W0);rhs=p.add(rhs,{2:2*Wb})
            ck(p.sg(p.add(rhs,left,-1))>=0)
        # Guarded comparison with rationally weaker r_K, checking actual S signs.
        D,Si,rk=single[i][3][2];_,Sj,_=single[j][3][2]
        critical=n==3 and p.sg(D)>0
        if critical:
            ck(p.sg(Si)>=0);ck(p.sg(Sj)>=0)
            slack=p.scale(rk,F(4,2));slack=p.add(slack,D,-F(4,2));slack=p.add(slack,Si,-F(2,2));slack=p.add(slack,Sj,-F(2,2))
            slack=p.add(slack,{2:2*(tot['ci']+tot['cj'])-r['C']})
            ck(p.sg(slack)>=0)
        records.append({'pair':[i,j],'critical_K2':critical,**{k:str(x) for k,x in tot.items()}})
    return records
def main():
    start=time.perf_counter()
    for row in itertools.product(range(-2,3),repeat=4):quartet(*map(F,row))
    ck(count>0);tablecount=paircount=criticalcuts=0
    for n in (1,2,3):
        for code in range(1<<(1<<n)):
            v=[1 if code>>x&1 else -1 for x in range(1<<n)]
            rr=pairs(v,f'n{n}:{code}');tablecount+=1;paircount+=len(rr);criticalcuts+=sum(x['critical_K2'] for x in rr)
    tree=ast.literal_eval('(((((), ()), (), ()), ()), ())')
    controls={'NAND6':[2*x-1 for x in e.table(tree)],'parity_guard':[-1 if (((x&1)^((x>>1)&1)) and (x&4)) else 1 for x in range(8)]}
    named={}
    for name,v in controls.items():named[name]=pairs(v,name)
    guard=named['parity_guard'][0]
    ck(guard['ci']==guard['cj']=='0');ck(guard['Q']=='1');ck(guard['o']=='1');ck(guard['P']=='1')
    # Reproduce the orientation coefficient limit on exact rational real rows.
    tails=[]
    for k in range(1,9):
        eps=F(1,2**k);r=quartet(F(1),F(0),F(0),eps)
        ck(r['Q']/r['o']==2/(1+eps*eps));tails.append({'epsilon':str(eps),'Q_over_o':str(r['Q']/r['o'])})
    result={'status':'PASS','small_tables':tablecount,'small_pair_cuts_including_full_n2':paircount,'K2_critical_pair_cuts':criticalcuts,
            'real_row_grid_cases':625,'named_controls':named,'real_orientation_limit':tails,
            'assertions_new_checker':count,'assertions_phase_library':p.checks,'assertions_log_library':e.ASSERTIONS,
            'runtime_seconds':time.perf_counter()-start}
    (ROOT/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('named_controls','real_orientation_limit')}))
if __name__=='__main__':main()
