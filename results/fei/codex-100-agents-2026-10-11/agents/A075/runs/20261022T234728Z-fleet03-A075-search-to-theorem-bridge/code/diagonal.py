from bridge import *

def fixed_u_polys(u):
    ms=[[1-2*u]]+[[Q(1),Q(-2)] for _ in range(5)]
    vs=[[4*u*(1-u)]]+[[Q(0),Q(4),Q(-4)] for _ in range(5)]
    masses=[];qs=[]
    for T in range(64):
        c=[Q(0)];v=[Q(1)]
        for U,w in enumerate(W):
            if U&T!=T:continue
            term=[Q(w,64)]
            for k in range(6):
                if (U^T)>>k&1:term=times(term,ms[k])
            c=plus(c,term)
        for k in range(6):
            if T>>k&1:v=times(v,vs[k])
        masses.append(times(v,times(c,c)))
    total=[Q(0)]
    for m in masses:total=plus(total,m)
    ar.ck(total==[Q(1)])
    for j in range(6):
        q=[Q(0)]
        for x in range(64):
            if x>>j&1 or J[x]==J[x^(1<<j)]:continue
            term=[Q(1)]
            for k in range(6):
                if k!=j:term=times(term,([u] if x>>k&1 else [1-u]) if k==0 else ([Q(0),Q(1)] if x>>k&1 else [Q(1),Q(-1)]))
            q=plus(q,term)
        qs.append(q)
    C=entseries(masses)
    for j in range(6):
        h=entseries([vs[j],plus([Q(1)],mul(vs[j],Q(-1)))])
        for i in range(3):
            for k in range(min(i,len(qs[j])-1)+1):C[i]=aadd(C[i],h[i-k],-qs[j][k])
    return C,qs,masses

def analytic():
    b,z=series('b'),series('z')
    a=({3:Q(6),2:Q(-8,3)},Q(0),Q(-4))
    A=ascale(a,Q(4));lam=({2:Q(1024,9),3:Q(-64)},Q(0),Q(0))
    delta=aadd(aadd(b['S'][2],z['S'][2],Q(-1)),lam,Q(-1))
    expected=({2:Q(-256,3)},Q(0),Q(-128,3))
    ar.ck(delta==expected and b['S'][1]==z['S'][1]==A)
    out={'A':boundtriple(A),'lambda':boundtriple(lam),'Delta':boundtriple(delta),'dimensions':{}}
    for d in [4,5]:
        K=aadd(A,ascale(delta,Q(3,1<<(d+2))))
        u=Q(2,1<<d);C,q,ms=fixed_u_polys(u)
        ar.ck(C[0]==zero() and C[1][1]==0 and q[0][0]==0 and q[0][1]==4)
        ar.ck(sum(t[0] for t in q[1:])==4*(1-u))
        cS=sparse(d,0,(0,1))[3]
        lead=aadd(aadd((ar.scale(cS,Q(4)),Q(0),Q(0)),ascale(a,4*(1-u))),C[1],Q(-1))
        # Independent closed first-order packet calculation, with all log(e) terms canceled.
        c1closed=ar.add(ar.add({2:32*u*(1-u)},logq(1-u),-32*(1-u)**2),logq(1-2*u),8*(1-2*u)**2)
        ar.ck(C[1]==(c1closed,Q(0),Q(0)))
        gclosed=aadd(ascale(A,1-u),(ar.add(ar.scale(logq(1-u),32*(1-u)**2),logq(u),-32*u*u),Q(0),Q(0)))
        ar.ck(lead==gclosed)
        D=aadd(lead,K,Q(-1));donor=aadd(A,K)
        row={'u':str(u),'K':boundtriple(K),'S_over_p':boundtriple(lead),'D_over_p':boundtriple(D),'sibling_after_subsidy_over_p':boundtriple(donor),'C1':boundtriple(C[1]),'masses':[[str(c) for c in m] for m in ms]}
        ar.ck(Q(row['S_over_p']['lower'])>0 and Q(row['D_over_p']['lower'])>0)
        ar.ck(Q(row['K']['upper'])<0 if d==4 else Q(row['K']['lower'])>0)
        if d==4:
            ar.ck(Q(row['sibling_after_subsidy_over_p']['lower'])>0)
            gamma=ascale(K,Q(-16,3));row['root_subsidy_over_p2']=boundtriple(gamma)
        for p in [Q(3,64),Q(1,1000)]:
            _,qq,mm=outer([u]+[p]*5)
            ar.ck(qq==[ev(x,p) for x in q] and mm==[ev(x,p) for x in ms])
        out['dimensions'][str(d)]=row
    out['checks']=ar.checks
    (ROOT/'out/DIAGONAL_ANALYTIC.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'analytic':{d:{k:v['display'] for k,v in row.items() if isinstance(v,dict) and 'display' in v} for d,row in out['dimensions'].items()},'checks':ar.checks}),flush=True)

def finite(n,whole):
    start=time.perf_counter();p=Q(3,1<<n)
    z={k:profile(n,k) for k in ['r','a','b','c','z']}
    e1=excess(z['r'],z['a'],z['z']);e2=excess(z['a'],z['b'],z['c'])
    T=iv(ar.add(ar.scale(e1,Q(2)),e2));B=iv(ar.scale(ar.add(z['b']['U'],z['c']['U']),Q(1,2)))
    D0=imul(idiv(T,B),iv(z['b']['U']));sz=iv(z['z']['S']);sb=iv(z['b']['S'])
    delta=isub(isub(sb,sz),D0)
    ar.ck(delta[1]<0 and sz[0]>0 and D0[0]>0)
    js=list(range(n-5)) if whole else [n-7,n-6]
    rows=[];previous=z['b'];directD=D0
    for j in js:
        if j==0:cur=z['b']
        else:
            key='n'+str(n)+'j'+str(j);SHAPES[key]=(j+2,(0,1));cur=profile(n,key)
        R=iadd(sz,imul(icon(1<<j),delta));D=isub(iv(cur['S']),R)
        if whole:
            if j:
                e=iv(excess(previous,cur,z['z']));directD=imul(icon(2),iadd(directD,e))
            ar.ck(max(D[0],directD[0])<=min(D[1],directD[1]))
        # No sign is assumed at small n: a bounded pattern is recorded honestly.
        row={'j':j,'remaining_dimension':n-j-2,'S':saveiv(iv(cur['S'])),'D':saveiv(D),'R':saveiv(R),'R_over_p':saveiv(imul(R,icon(1/p))),'D_nonnegative':D[0]>=0,'full_eligible':R[0]>=0,'M':saveiv(iv(cur['M']))}
        if n-j-2==4:
            deficit=ineg(R);donor=iadd(sz,R)
            row.update({'deficit':saveiv(deficit),'last_sibling_after_transfer':saveiv(donor),'local_repair_feasible':deficit[0]>0 and donor[0]>=0,'root_reach':str(Q(1,1<<(j+2))),'root_subsidy_over_p2':saveiv(imul(deficit,icon(Q(1,1<<(j+2))/p**2)))})
            fullB=mean(iv(cur['S']),sz);netT=imul(D,icon(Q(1,2)))
            rebooking_slack=isub(fullB,netT)
            row['zero_flow_if_new_descendant_labels_reassigned']=bool(iv(cur['S'])[0]>0 and netT[0]>0 and rebooking_slack[0]>0)
            row['rebooking_slack']=saveiv(rebooking_slack)
            ar.ck(row['zero_flow_if_new_descendant_labels_reassigned'])
        rows.append(row);previous=cur
        (ROOT/'out'/f'DIAGONAL_n{n}.json').write_text(json.dumps({'n':n,'p':str(p),'whole_chain':whole,'D0':saveiv(D0),'S_Z':saveiv(sz),'Delta':saveiv(delta),'states':rows},indent=2)+'\n',encoding='utf-8')
    out={'n':n,'whole_chain':whole,'states':len(rows),'all_preterminal_D_nonnegative':all(r['D_nonnegative'] for r in rows[:-1]),'all_preterminal_full_eligible':all(r['full_eligible'] for r in rows[:-1]),'endpoint_R_over_p':rows[-1]['R_over_p']['display'],'local_repair_feasible':rows[-1]['local_repair_feasible'],'seconds':time.perf_counter()-start,'checks_so_far':ar.checks}
    print(json.dumps(out),flush=True);return out

if __name__=='__main__':
    start=time.perf_counter()
    spec=json.loads((ROOT/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
    if '--analytic' in sys.argv:analytic()
    else:
        pilot='--pilot' in sys.argv
        domain=spec['domain']['pilot'] if pilot else spec['domain']['whole_zero_chain']+spec['domain']['endpoints_only']
        rows=[finite(n,n in spec['domain']['whole_zero_chain']) for n in domain]
        (ROOT/'out'/('DIAGONAL_PILOT.json' if pilot else 'DIAGONAL_FINITE.json')).write_text(json.dumps({'rows':rows,'checks':ar.checks,'seconds':time.perf_counter()-start},indent=2)+'\n',encoding='utf-8')
    assert time.perf_counter()-start<(55 if '--pilot' in sys.argv else 180)
