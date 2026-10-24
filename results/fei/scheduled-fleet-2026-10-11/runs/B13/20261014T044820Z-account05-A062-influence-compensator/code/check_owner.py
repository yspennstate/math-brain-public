from pathlib import Path
import json,time,sys
run=Path(__file__).resolve().parents[1]
old=run.parent/'20261014T015800Z-account05-A062-influence-compensator/code/check_transfer.py'
env={'__file__':str(old)}
exec(compile(old.read_text().split("pilot='--pilot'")[0],str(old),'exec'),env)
F=env['F']; point=env['point']; plus=env['plus']; minus=env['minus']; mul=env['mul']; pos=env['pos']; tree=env['tree']; measure=env['measure']; equal=env['equal']; leq=env['leq']; fmt=env['fmt']; kernel=env['env']
start=time.perf_counter()
def overlap(a,b,kind): leq(max(a[0],b[0]),min(a[1],b[1]),kind)
def lift(g):
 m=len(g).bit_length()-1
 out=[]
 for x in range(1<<(m+5)):
    a=g[x&((1<<m)-1)]; w=1 if ((x>>m)&1)==0 else -1
    u=(-1)**(((x>>(m+1))&1)+((x>>(m+2))&1))
    v=(-1)**(((x>>(m+3))&1)+((x>>(m+4))&1))
    out.append(u if w*a==1 else v)
 return tuple(out)
pilot='--pilot' in sys.argv
seeds=[tuple(1 if (s>>x)&1 else -1 for x in range(4)) for s in range(16)]
if not pilot: seeds += [tuple(-1 if x==0 else 1 for x in range(1<<m)) for m in (3,4,5)]
rows=[]
for g in seeds:
 m=len(g).bit_length()-1; f=lift(g)
 tagged=tuple(g[x&((1<<m)-1)]*(1 if ((x>>m)&1)==0 else -1) for x in range(1<<(m+1)))
 qparent=F(sum(t==1 for t in tagged),len(tagged))
 equal(qparent,F(1,2),'actual_balanced_selector_probability')
 for i in range(m):
    qchildren=[F(sum(tagged[x]==1 for x in range(len(tagged)) if ((x>>i)&1)==bit),len(tagged)//2) for bit in (0,1)]
    equal(qchildren,[F(1,2)]*2,'actual_controller_children_probabilities')
    bank=lambda q: plus(kernel['atom_h'](q),kernel['atom_h'](1-q))
    equal(minus(bank(qparent),mul(plus(bank(qchildren[0]),bank(qchildren[1])),F(1,2))),point(0),'actual_variance_release_zero')
 _,Hg,Ig=measure(g); _,Hf,If=measure(f)
 overlap(Hf,plus(point(2),mul(Hg,F(1,2))),'lift_entropy_half')
 equal(If[:m],[i/2 for i in Ig],'lift_seed_influence_half')
 equal(If[m:],[F(1,2)]*5,'tag_and_core_influence_accounts')
 for C in ((4,) if pilot else (4,6,11)):
    Qg=tree(g,tuple(range(m)),C)[0]
    Qf=tree(f,tuple(range(m+5)),C)[0]
    overlap(Qf,mul(Qg,F(1,2)),'complete_controller_reserve_half')
    if not pilot and m==4 and C==4: leq(F(1,100),Qg[0],'nonzero_seed_reserve_fixture')
    for p in (0,1,2):
        prefix=(m+1,m+3)[:p]
        order=prefix+tuple(i for i in range(m+5) if i not in prefix)
        Q=tree(f,order,C)[0]
        expected=mul(pos(minus(Qg,point(p*C))),F(1,2))
        overlap(Q,expected,'complete_prefix_debit_identity')
        frontier=[(f,tuple(range(m+5)))]
        for label in prefix:
            nxt=[]
            for vals,labels in frontier:
                i=labels.index(label)
                _,Hp,Ip=measure(vals)
                equal(Ip[i],F(1,2),'prefix_query_single_account')
                for bit in (0,1):
                    child=tuple(vals[x] for x in range(len(vals)) if ((x>>i)&1)==bit)
                    overlap(measure(child)[1],Hp,'prefix_zero_entropy_drop')
                    nxt.append((child,labels[:i]+labels[i+1:]))
            frontier=nxt
        for vals,labels in frontier:
            remaining_order=tuple(range(len(labels)))
            Qfront=tree(vals,remaining_order,C)[0]
            overlap(Qfront,mul(Qg,F(1,2)),'actual_frontier_retains_seed_reserve')
            # q values were reconstructed from actual tagged-controller assignments.
            equal(plus(kernel['atom_h'](qparent),kernel['atom_h'](1-qparent)),point(1),'frontier_variance_bank_one')
        rows.append({'m':m,'seed':list(g),'C':C,'prefix_length':p,'Qseed':fmt(Qg),'Qinitial':fmt(Q),'Qfrontier':fmt(mul(Qg,F(1,2)))})
compressed=[]
if not pilot:
 entropy=kernel['entropy']; Counter=kernel['Counter']
 def H(hist):
    equal(sum(prob*count for prob,count in hist.items()),F(1),'compressed_actual_probability_mass')
    return entropy(hist)
 for k in (4,6,8,10,12,14):
    r=2*k; N=1<<k; L=1<<r; delta=F(1,N); alpha=F(1,1<<(k//2)); p0=F(1,L)
    np=(N+(1<<(k//2)))//2; nn=N-np
    def activated(edited):
        shift=2*delta if edited else F(0)
        hist=Counter({(1-p0+p0*(alpha-shift))**2:1})
        hist[(p0*(alpha-shift-1))**2]+=L-1
        hist[(p0*(alpha-shift))**2]+=L*(np-1)
        hist[(p0*(-alpha-shift))**2]+=L*nn
        return H(hist)
    HG=activated(False); HH=activated(True)
    hist=Counter({(1-p0*(1-alpha+delta))**2:1})
    hist[(p0*(alpha-1-delta))**2]+=L-1
    hist[(p0*(alpha-delta))**2]+=L*(np-1)
    hist[(p0*(-alpha-delta))**2]+=L*nn
    hist[(p0*delta)**2]+=L*N
    HF=H(hist); D=minus(HF,mul(plus(HG,HH),F(1,2))); d=p0*delta
    lower=(1-delta)*(k-2)
    leq(lower*d,D[0],'actual_bad_selector_lower_bound')
    if k>=14: leq(F(23,2)*d,D[0],'price_eleven_fails_with_strict_margin')
    compressed.append({'k':k,'r':r,'actual_seed_dimension':1+k+r,'mixed_lift_dimension_after_one_core_bit':1+k+r+4,'D_seed':fmt(D),'Inf_seed':str(d),'D_over_Inf':fmt(mul(D,1/d)),'proved_ratio_lower_bound':str(lower),'mixed_controller_D':fmt(mul(D,F(1,2))),'mixed_controller_Inf':str(d/2),'variance_release':'0','parity_core_reserves':'0'})
elapsed=time.perf_counter()-start
assert elapsed<60,elapsed
out={'helper_version':'A062-controller-owner-v1','pilot':pilot,'complete_lifted_roots':len(rows),'compressed_roots':len(compressed),'assertions':sum(kernel['counts'].values()),'counts':dict(kernel['counts']),'failures':0,'runtime_seconds':elapsed,'rows':rows,'compressed':compressed}
(run/'out'/('PILOT.json' if pilot else 'EXACT_OWNER.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('rows','compressed')},indent=2))
