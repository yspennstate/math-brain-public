from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time,hashlib
R=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('primitive',R/'code/pilot.py');V=importlib.util.module_from_spec(sp);sp.loader.exec_module(V)
L=V.L; COUNT=0
def check(x):
    global COUNT
    COUNT+=1
    assert x,COUNT
def exact(x):return x,x
def add(*xs):return V.sumiv(xs)
def scale(x,k):return V.mul(x,exact(k))
def sub(a,b):return V.sub(a,b)
def overlap(a,b):check(a[0]<=b[1] and b[0]<=a[1])
def encoded(x):return [str(a) for a in x]
def rounded(x):
    d=10**12
    return {'lower':str(F((x[0]*d).__floor__(),d)),'upper':str(F((x[1]*d).__ceil__(),d))}
def fw(tab):
    w=list(tab);h=1
    while h<len(w):
        for i in range(0,len(w),2*h):
            for j in range(i,i+h):w[j],w[j+h]=w[j]+w[j+h],w[j]-w[j+h]
        h*=2
    return [F(x*x,len(w)**2) for x in w]
def inf(tab,i):return F(sum(v!=tab[t^(1<<i)] for t,v in enumerate(tab)),len(tab))
def ent(p):return add(*(scale(V.log(exact(x)),-x) for x in p if x))
def TC(tab):
    p=fw(tab);n=len(tab).bit_length()-1
    return sub(add(*(ent([inf(tab,i),1-inf(tab,i)]) for i in range(n))),ent(p))
def product(tab):
    n=len(tab).bit_length()-1; ds=[inf(tab,j) for j in range(n)];out=[]
    for s in range(1<<n):
        z=F(1)
        for j,d in enumerate(ds):z*=d if s>>j&1 else 1-d
        out.append(exact(z))
    return out
def release(p,Q,i):
    q=V.fuse(p,i);qr=[add(Q[x],Q[x|(1<<i)]) for x in range(len(p)) if not (x>>i)&1]
    terms=[]
    for x in range(len(p)):
        if (x>>i)&1:continue
        pt=p[x]+p[x|(1<<i)];qt=add(Q[x],Q[x|(1<<i)])
        if not pt:continue
        for t in [x,x|(1<<i)]:
            if p[t]:terms.append(scale(V.log(V.div(exact(p[t]/pt),V.div(Q[t],qt))),p[t]))
    E=add(*terms);check(E[0]>=0)
    overlap(V.kl(p,Q),add(E,V.kl(q,qr)))
    return E,q,qr
def step(tab,Q,i):
    p=fw(tab);c=[V.child(tab,i,y) for y in [0,1]];pc=[fw(t) for t in c]
    E,q,qr=release(p,Q,i);k=[[pc[y][t]/(2*q[t]) if q[t] else F(1,2) for t in range(len(q))] for y in [0,1]]
    check(all(q[t]*k[y][t]==pc[y][t]/2 for y in [0,1] for t in range(len(q))))
    qy=[add(*(scale(qr[t],k[y][t]) for t in range(len(q)))) for y in [0,1]]
    check(all(a[0]>0 for a in qy));overlap(add(*qy),exact(F(1)))
    qc=[[V.div(scale(qr[t],k[y][t]),qy[y]) for t in range(len(q))] for y in [0,1]]
    O=V.kl([F(1,2)]*2,qy);K=[V.kl(pc[y],qc[y]) for y in [0,1]]
    overlap(V.kl(p,Q),add(E,O,scale(add(*K),F(1,2))))
    DH=sub(ent(p),scale(add(*(ent(z) for z in pc)),F(1,2)))
    B=F(0);Biv=sub(ent(p),ent(q));JS=sub(ent(q),scale(add(*(ent(z) for z in pc)),F(1,2)))
    overlap(DH,add(Biv,JS));check(inf(tab,i)+sum(sum(inf(t,j) for j in range(len(t).bit_length()-1)) for t in c)/2==sum(inf(tab,j) for j in range(len(tab).bit_length()-1)))
    return {'tab':tab,'children':c,'child_refs':qc,'E':E,'O':O,'K':K,'QY':qy,'DH':DH,'B':Biv,'JS':JS,'d':inf(tab,i),'root_K':V.kl(p,Q)}
def profile(tab,names,assignments):
    # Original exclusive labels survive all physical restrictions; constants have zero variance.
    control_names=[x for x in ['x','a','b'] if x in names]
    data_names=[x for x in ['v0','v1'] if x in names]
    vcore=[]
    for s in range(1<<len(data_names)):
        a=dict(assignments);a.update({name:(s>>i)&1 for i,name in enumerate(data_names)})
        vcore.append(-1 if a['v0']==a['v1']==0 else 1)
    label_counts={0:0,1:0,2:0}
    for s in range(1<<len(control_names)):
        a=dict(assignments);a.update({name:(s>>i)&1 for i,name in enumerate(control_names)})
        label_counts[1 if a['x']==0 and a['a']==1 else 2 if a['x']==1 and a['b']==1 else 0]+=1
    q=F(label_counts[2],1<<len(control_names));m=F(sum(vcore),len(vcore));variance=1-m*m
    Uf=L.add((q,L.ent(fw(vcore))),(-q,L.ent([m*m]) if m else {}))
    Rf=L.add((variance,L.ent([q]))) if q else {}
    Hf=L.ent(fw(tab));pf=L.add((1,Hf),(-1,Uf),(-1,Rf))
    U,reserve,H,phi=map(L.evalformal,[Uf,Rf,Hf,pf])
    check(not pf or phi[0]>=0)
    return {'H':rounded(H),'U':rounded(U),'R':rounded(reserve),'H_minus_U_minus_R':rounded(phi),'remaining_influence':str(sum(inf(tab,i) for i in range(len(names)))),'q_v':str(q),'actual_v_core':vcore,'raw':(H,U,reserve,phi)}
def review_fixture(tab):
    ancestor=[];u=(-1,-1,-1,1);v=(-1,1,1,1)
    for t in range(128):
        x,a,b,u0,u1,v0,v1=[(t>>i)&1 for i in range(7)]
        ancestor.append(u[u0+2*u1] if x==0 and a else v[v0+2*v1] if x==1 and b else 1)
    check(inf(ancestor,3)==F(1,8))
    reached=V.child(ancestor,3,0);check(V.child(reached,3,0)==V.child(reached,3,1)==tab)
    check(fw(tab)==V.spectrum(tab));p=fw(tab)
    check(sorted(x for x in p if x)==[F(1,64)]*14+[F(9,64)]*2+[F(1,4)]*2)
    check(all(p[t]==0 for t in range(32) if t&2 and t&28))
    check(2**1428*7**525<5**1250<2**1432*7**525);check(7**245<2**688)
    check(4*31**2*49**3<55**5)
    M0=F(1559232,9150625);credit=F(55,64)*F(10,7)*(M0+M0*M0/2)
    check(credit>F(43,200));check(sum(inf(tab,i) for i in range(5))==F(11,8))
    return {'actual_essential_ancestor_reconstructed':True,'source_integer_certificates_reconstructed':True,'weighted_excluded_event_lower_bound':str(credit),'source_claim_scope':'Full scalar arbitrary-v continuum statement independently re-derived in REVIEW_A038.md; quantitative fixture and occupancy lower certificate independently verified here'}
def main():
    start=time.perf_counter();lo,hi=F(3,4),F(1)
    g=lambda c:1-c-(1-F(32,55)*c)**2*(1-F(8,55)*c)**3
    check(g(lo)>0 and g(hi)<0)
    for _ in range(48):
        mid=(lo+hi)/2
        if g(mid)>0:lo=mid
        else:hi=mid
    check(g(lo)>0 and g(hi)<0);Q=V.reference((lo,hi));overlap(add(*Q),exact(F(1)))
    tab=[]
    for t in range(32):
        x,a,b,v0,v1=[(t>>i)&1 for i in range(5)]
        tab.append(-1 if x==0 and a else (-1 if x==1 and b and v0==v1==0 else 1))
    reviewed=review_fixture(tab);first=step(tab,Q,1)
    rho=add(exact(F(2)),scale(V.log(exact(F(7))),F(21,32)),scale(V.log(exact(F(5))),F(-25,16)))
    check(sub(first['E'],rho)[0]>F(1,40))
    # Original product reset, reconstructed with its own product reference and same kernel.
    residual_product=product(first['children'][0]);ds=[]
    for j in range(4):ds.append(sum(inf(t,j) for t in first['children'])/2)
    original=[]
    for t in range(16):
        z=F(1)
        for j,d in enumerate(ds):z*=d if t>>j&1 else 1-d
        original.append(exact(z))
    q=V.fuse(fw(tab),1);pcs=[fw(t) for t in first['children']]
    origY=[add(*(scale(original[t],pcs[y][t]/(2*q[t]) if q[t] else F(1,2)) for t in range(16))) for y in [0,1]]
    check(origY==[exact(F(1,2))]*2)
    tc=scale(add(*(TC(t) for t in first['children'])),F(1,2))
    sigma=sub(tc,scale(add(*first['K']),F(1,2)))
    joint_gap=sub(first['E'],sigma)
    check(joint_gap[0]>F(1,25))
    overlap(sub(first['root_K'],add(first['O'],tc)),joint_gap)
    names=['x','b','v0','v1'];second={};leaf_profiles={}
    for y in [0,1]:
        for j,name in enumerate(names):
            t=step(first['children'][y],first['child_refs'][y],j);second[y,j]=t
            ps=[]
            for z in [0,1]:
                p=profile(t['children'][z],[s for s in names if s!=name],{'a':y,name:z});p.pop('raw');ps.append(p)
            leaf_profiles[y,j]=ps
    trees=[]
    for j in range(4):
        for k in range(4):
            t0,t1=second[0,j],second[1,k]
            released=add(first['E'],first['O'],scale(add(t0['E'],t0['O'],t1['E'],t1['O']),F(1,2)))
            terminal=scale(add(*t0['K'],*t1['K']),F(1,4))
            overlap(first['root_K'],add(released,terminal))
            spent=add(rho,sub(first['E'],rho),first['O'],scale(add(t0['E'],t0['O'],t1['E'],t1['O']),F(1,2)),terminal)
            overlap(first['root_K'],spent)
            trees.append({'second_query_by_a_branch':[names[j],names[k]],'spent_reset_once':rounded(rho),'unspent_first_erasure_margin':rounded(sub(first['E'],rho)),'cumulative_erasure_and_outcome_KL':rounded(released),'terminal_inherited_reference_KL':rounded(terminal),'leaf_profiles':[leaf_profiles[0,j],leaf_profiles[1,k]]})
    p0=profile(tab,['x','a','b','v0','v1'],{});p0.pop('raw');childprofiles=[]
    for y in [0,1]:
        p=profile(first['children'][y],names,{'a':y});p.pop('raw');childprofiles.append(p)
    result={'status':'PASS','assertions':COUNT,'c_bracket':encoded((lo,hi)),'root_occupancy_KL':rounded(first['root_K']),
    'first_erasure_release':rounded(first['E']),'occupancy_reference_outcome_KL':rounded(first['O']),'reference_outcomes':list(map(rounded,first['QY'])),
    'original_product_reset_rho':rounded(rho),'release_minus_rho':rounded(sub(first['E'],rho)),'strict_release_margin_lower':'1/40',
    'mean_child_inherited_reference_KL':rounded(scale(add(*first['K']),F(1,2))),'mean_child_product_KL':rounded(tc),
    'actual_occupancy_Bayes_to_product_reset':rounded(sigma),'release_minus_actual_conversion_reset':rounded(joint_gap),'strict_actual_conversion_margin_lower':'1/25',
    'retained_root_profile':p0,'retained_child_profiles':childprofiles,'two_level_stopping_trees':trees,'source_review':reviewed,
    'arithmetic':'rigorous rational intervals; all sign comparisons exact; same inherited reference through all second queries',
    'runtime_seconds':time.perf_counter()-start,'log_helper_sha256':hashlib.sha256(V.P.read_bytes()).hexdigest()}
    check(result['runtime_seconds']<120)
    (R/'out/TRANSPORT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','assertions','first_erasure_release','release_minus_rho','actual_occupancy_Bayes_to_product_reset','release_minus_actual_conversion_reset','runtime_seconds']}))
if __name__=='__main__':main()
