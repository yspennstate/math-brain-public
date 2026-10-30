from exact import *
import exact as arithmetic

def kl(mu,r):
    ck(sum(mu.values())==sum(r.values())==1,'complete KL normalizers')
    return combine(*[(1,lg(v/r[t],v)) for t,v in mu.items() if v])

def quotient(row,project):
    mu={};r={}
    for t,v in row['r'].items():
        c=project(t);r[c]=r.get(c,F(0))+v
    for t,v in row['mu'].items():
        c=project(t);mu[c]=mu.get(c,F(0))+v
    return mu,r,kl(mu,r)

def data(table,direct=False):
    p,e,W=spectrum(table,direct);n=len(e);a=edge_forms(p,n,e)
    H=combine(*[(1,lg(1/v,v)) for v in p.values()])
    return p,e,a,H,W

def duplicate(table,J):
    n=len(table).bit_length()-1;pos=[];k=0
    for i in range(n):
        q=[k,k+1] if i in J else [k];pos.append(q);k+=len(q)
    t=[]
    for x in range(1<<k):
        old=sum((sum((x>>j)&1 for j in js)%2)<<i for i,js in enumerate(pos))
        t.append(table[old])
    return t,pos

def duplication_case(name,table,J):
    p,e,a,H,W=data(table);t,pos=duplicate(table,J);pp,ee,aa,HH,WW=data(t)
    embedding={sum(sum(1<<j for j in pos[i]) for i in range(len(e)) if s>>i&1):v for s,v in p.items()}
    ck(pp==embedding and HH==H,'exact embedded spectrum and entropy')
    ck(sum(ee)==sum(e)+sum(e[i] for i in J),'single physical budget')
    subtract=combine(*[(1,a['rows'][i]['M']) for i in J])
    ck(aa['M']==combine((1,a['M']),(-1,subtract)),'partial duplication M')
    losses={}
    for i,js in enumerate(pos):
        for j in js:
            ck(ee[j]==e[i])
            if i not in J:
                ck(aa['rows'][j]['M']==a['rows'][i]['M'])
                ck(aa['rows'][j]['D']==a['rows'][i]['D']);continue
            row=aa['rows'][j];ck(row['M']=={})
            ck(all(not(pp.get(s,F(0)) and pp.get(s^(1<<j),F(0))) for s in pp),'zero erasure')
            if not e[i]:continue
            other=next(k for k in js if k!=j)
            mu,r,D=quotient(row,lambda s:s&~(1<<other))
            ck(D==a['rows'][i]['D'],'drop only partner')
            loss=combine((e[i],row['D']),(-e[i],D))
            ck(loss==a['rows'][i]['M']);losses=combine((1,losses),(1,loss))
            mu,r,D=quotient(row,lambda s:(s>>other)&1)
            ck(mu=={1:F(1)} and r.get(1)==e[i] and r.get(0,F(0))==1-e[i])
            ck(D==row['D']==lg(1/e[i]),'retain partner sufficiency')
    ck(losses==combine((2,subtract)))
    if len(J)==len(e):ck(aa['M']=={} and sum(ee)==2*sum(e))
    return {'name':name,'J':sorted(J),'n':len(e),'N':len(ee),'status':'PASS'},(p,e,a,H)

def bent(y,d):return -1 if sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(d//2))%2 else 1

def bent_selector(d):
    t=[]
    for x in range(1<<(d+1)):
        s=x&1;y=x>>1;t.append(-1 if y==0 and s else bent(y,d))
    record,(p,e,a,H)=duplication_case('bent_selector_'+str(d),t,{0})
    delta=F(1,1<<d);small=F(1,1<<(d//2));ck(e[0]==delta)
    ck(all(x==F(1,2)+delta for x in e[1:]))
    ratios=set()
    for y in range(1<<d):
        A=p.get(2*y,F(0));B=p.get(2*y+1,F(0));ck(B==delta*delta)
        ck(A+B>=delta/2);ratios.add(B/(A+B))
    ck(len(ratios)==2)
    M=combine((1/delta,a['rows'][0]['M']));lo,hi=bounds(M,12)
    ck(lo>d-1 and hi<d,'strict local loss margins')
    record.update({'loss_over_pair_coordinate_influence':decimal_interval((lo,hi),9),
                   'analytic_bounds':[d-1,d],'I_after_duplication':F(d,2)+(d+2)*delta})
    return record

def and_gate(d):
    delta=F(1,1<<d);t=F(1,1<<(d//2));e0=delta/2
    table=[(-1 if (x&3)==3 else 1) if (x>>2)==0 else bent(x>>2,d) for x in range(1<<(d+2))]
    p,e,a,H,W=data(table,False);ck(e[:2]==[e0,e0])
    ck(all(x==F(1,2)+delta/2 for x in e[2:]))
    ck(sum(e)==F(d,2)+(F(d,2)+1)*delta)
    nplus=(2**d+2**(d//2))//2;nminus=2**d-nplus
    D0={};count={1:0,-1:0}
    for y in range(1<<d):
        # Walsh of the core quadratic is a signed flat spectrum; derive its sign directly.
        sigma=-1 if sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(d//2))%2 else 1
        count[sigma]+=1
        for u in [0,1]:
            for v in [0,1]:
                amp=sigma*t-delta/2 if u==v==0 else (delta/2 if (u,v)!=(1,1) else -delta/2)
                ck(p.get((y<<2)|u|(v<<1),F(0))==amp*amp,'actual AND-gate squared amplitudes')
    ck(count=={1:nplus,-1:nminus})
    for sigma,count_sigma in [(1,nplus),(-1,nminus)]:
        c=1-sigma*t+delta/2
        D0=combine((1,D0),(1,lg((1-delta/2)/c,delta*count_sigma)))
        ck(F(5)*(1-delta/2)<=F(7)*c,'likelihood at most 7/5')
    expected_binary=combine((F(1,2),lg(F(1,2)/(1-e0))),(F(1,2),lg(F(1,2)/e0)))
    full=[]
    for i,other in [(0,1),(1,0)]:
        row=a['rows'][i];mu,r,D=quotient(row,lambda s:(s>>other)&1)
        ck(mu=={0:F(1,2),1:F(1,2)} and r=={0:1-e0,1:e0})
        ck(D==expected_binary)
        ck(row['D']==combine((1,D),(F(1,2),D0)),'conditional KL remainder')
        loss=combine((e0,row['D']),(-e0,D))
        ck(loss==combine((e0/2,D0)))
        # Explicitly recompute both conditional laws, keeping the complete reference.
        conditional={}
        for v in [0,1]:
            cm={s&~(1<<other):m/mu[v] for s,m in row['mu'].items() if (s>>other)&1==v}
            cr={s&~(1<<other):m/r[v] for s,m in row['r'].items() if (s>>other)&1==v}
            conditional[v]=kl(cm,cr)
        ck(conditional[0]==D0 and conditional[1]=={})
        ck(sum(p.get(s,F(0))>0 and p.get(s^(1<<i),F(0))>0 for s in p)>0,'nonzero erasure')
        coarseM=combine((1,lg(1/e0,e0)),(-e0,D))
        ck(row['M']==combine((1,coarseM),(-1,loss)))
        dl,dh=bounds(combine((F(1,2),D0)),12)
        ck(dl>0 and dh<F(1,4),'strict retained-binary remainder bounds')
        ml,mh=bounds(combine((1/e0,row['M'])),12)
        ck(ml>F(d,2)+F(3,4),'nonzero-erasure local M cost grows')
        full.append({'coordinate':i,'e':e0,'mu_binary':mu,'r_binary':r,'D_full':row['D'],'D_binary':D,
                     'D_core_given_partner0':D0,'loss_prime_log':loss,
                     'loss_over_e_interval':decimal_interval((dl,dh),9),
                     'M_over_e_interval':decimal_interval((ml,mh),9),
                     'complete_mu':row['mu'],'complete_reference':row['r']})
    result={'family':'bent_AND_point_gate','d':d,'physical_n':d+2,'I':sum(e),'rows':full,
            'H_over_I_analytic_upper_bound':F(2)+F(4,d),'status':'PASS'}
    save('AND_d'+str(d)+'.json',result)
    return {'name':'bent_AND_'+str(d),'d':d,'status':'PASS','loss_over_e':full[0]['loss_over_e_interval'],'M_over_e':full[0]['M_over_e_interval']}

def run(pilot):
    records=[]
    tasks=[]
    for n in [1,2]:
        for mask in range(1<<(1<<n)):
            table=[1-2*((mask>>x)&1) for x in range(1<<n)]
            for Jbits in range(1<<n):tasks.append((str((n,mask,Jbits)),table,{i for i in range(n) if Jbits>>i&1}))
    named=[('majority',[1 if x.bit_count()<=1 else -1 for x in range(8)]),
           ('parity',[(-1)**x.bit_count() for x in range(8)]),('point',[-1]+[1]*7),('AND',[1]*7+[-1])]
    for name,table in named:
        for Jbits in range(8):tasks.append((name,table,{i for i in range(3) if Jbits>>i&1}))
    ck(len(tasks)==104)
    if pilot:tasks=[tasks[i] for i in [0,7,31,103]]
    with (ROOT/'out'/('pilot.jsonl' if pilot else 'cases.jsonl')).open('w',encoding='utf-8') as f:
        for name,table,J in tasks:
            result,_=duplication_case(name,table,J);records.append(result)
            f.write(json.dumps(serial(result))+'\n');f.flush()
        for d in ([2] if pilot else [2,4,6]):
            for result in [bent_selector(d),and_gate(d)]:
                records.append(result);f.write(json.dumps(serial(result))+'\n');f.flush()
    ck(len(records)==(6 if pilot else 110))
    result={'status':'PASS','cases':len(records),'checks':arithmetic.CHECKS,'runtime_seconds':time.perf_counter()-START,
            'precision_terms':12,'precision_refinements':0,'maximum_dimension':4 if pilot else 8,
            'family_summaries':[r for r in records if 'loss_over_e' in r or 'analytic_bounds' in r]}
    save('PILOT.json' if pilot else 'SUMMARY.json',result);print(json.dumps(serial(result),indent=2))

if __name__=='__main__':run('--pilot' in sys.argv)
