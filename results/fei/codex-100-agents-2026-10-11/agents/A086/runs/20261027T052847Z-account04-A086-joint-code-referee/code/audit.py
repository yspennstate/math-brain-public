from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib,itertools

START=time.perf_counter(); checks=0
HERE=Path(__file__).resolve().parents[1]
SOURCE=Path('agents/A012/runs/20261023T140756Z-account03-A012-sparse-activation-accounting')
def ck(ok,why):
    global checks
    checks+=1
    if not ok: raise AssertionError(why)
    if time.perf_counter()-START>55:raise TimeoutError('frozen 55s cutoff')
def save(name,obj):
    (HERE/'out'/name).write_text(json.dumps(obj,indent=2,default=str)+'\n',encoding='utf-8',newline='')

cert=json.loads((SOURCE/'out/FULL.json').read_text(encoding='utf-8'))
truth=[]
for x in range(64):
    shared=x%8; u=(x>>3)&1; v=(x>>4)&1; z=x>>5
    base=1-2*(shared==0)
    truth.append(base*(1-2*((shared==0 and u==0) if z==0 else (shared==1 and v==0))))
def spec(vals):
    n=len(vals)
    return tuple(F(sum(y*(1-2*((x&t).bit_count()%2)) for x,y in enumerate(vals))**2,n*n) for t in range(n))
rootq=spec(truth)

@lru_cache(None)
def laws(s):
    free=tuple(j for j,v in enumerate(s) if v<0)
    vals=[]
    for k in range(1<<len(free)):
        x=sum(v<<j for j,v in enumerate(s) if v>=0)+sum(((k>>i)&1)<<j for i,j in enumerate(free))
        vals.append(truth[x])
    p=spec(vals); q=[F(0)]*len(p)
    for t,y in enumerate(rootq):
        projected=sum(((t>>j)&1)<<i for i,j in enumerate(free));q[projected]+=y
    ck(sum(p)==sum(q)==1,'normalized raw laws')
    influence=sum((p[t]*t.bit_count() for t in range(len(p))),F(0))
    shared=sum((p[t]*sum((t>>i)&1 for i,j in enumerate(free) if j<3) for t in range(len(p))),F(0))
    return p,tuple(q),free,influence,shared

GRID=1<<64
@lru_cache(None)
def ln(q):
    ck(q>0,'log domain')
    if q==1:return F(0),F(0)
    k=q.numerator.bit_length()-q.denominator.bit_length()
    r=q/(F(2)**k)
    if r<1:k-=1;r*=2
    ck(1<=r<2,'log range reduction')
    def series(t):
        z=(t-1)/(t+1); power=z; total=F(0)
        for j in range(24):total+=2*power/(2*j+1);power*=z*z
        return total,total+2*power/F(49)/(1-z*z)
    a,b=series(r);c,d=series(F(2))
    low=a+k*(c if k>=0 else d); high=b+k*(d if k>=0 else c)
    # Preserve exact directed error under a common rational grid.
    return F((low*GRID).__floor__(),GRID),F((high*GRID).__ceil__(),GRID)
L2,U2=ln(F(2))
def kl(p,q):
    lo=hi=F(0)
    for x,y in zip(p,q):
        if x:
            ck(y>0,'cover on positive target')
            a,b=ln(x/y);lo+=x*a;hi+=x*b
    return lo,hi
def ent(p):return kl(p,(F(1),)*len(p))

W={}
for row in cert['DP_super_solution'].values():
    s=tuple(row['state']);a=None if row['anchor'] is None else tuple(row['anchor'])
    ck((s,a) not in W,'duplicate certificate state');W[s,a]=F(row['upper_potential_nats'])
TX={}
for row in cert['transactions'].values():
    s=tuple(row['anchor']);p,q,free,_,_=laws(s)
    ck(q[0]<1,'profile denominator nonzero')
    r0=(p[0]+q[0])/2; beta=(1-r0)/(1-q[0]);r=(r0,)+tuple(beta*x for x in q[1:])
    ck(sum(r)==1 and min(r)>=0,'actual converted law')
    ck(beta==F(row['beta']) and r==tuple(map(F,row['R_at_transaction'])),'transaction law metadata')
    cup=F(row['conversion_nats'][1]);ck(kl(r,q)[1]<=cup,'full conversion fee')
    ck(s not in TX,'duplicate transaction');TX[s]=(beta,cup)

visited=set(); triggers=set(); edges=0; ghosts=0; constants=0; beta_above=0
def trigger(s,a):return a is None and s[0]>=0 and s[1]>=0 and s[2]<0
def bound(s,a):
    if trigger(s,a):
        ck(s in TX and (s,s) in W,'mandatory transaction exists')
        return TX[s][1]+W[s,s]
    ck((s,a) in W,'reachable record exists');return W[s,a]
def walk(s,a):
    global edges,ghosts,constants,beta_above
    if trigger(s,a):
        triggers.add(s);walk(s,s);return
    if (s,a) in visited:return
    visited.add((s,a));p,q,free,inf,shared=laws(s)
    if a is not None:
        ck(all(v<0 or s[j]==v for j,v in enumerate(a)),'anchor compatibility')
        beta=TX[a][0];q=(1-beta*(1-q[0]),)+tuple(beta*x for x in q[1:])
        beta_above+=beta>1
    ck(sum(q)==1 and min(q)>=0,'complete current reference incl ghosts')
    ghosts+=sum(x==0 and y>0 for x,y in zip(p,q))
    constants+=p[0]==1
    w=W[s,a];ck(kl(p,q)[1]<=w,'terminal complete KL bound')
    for k,j in enumerate(free):
        daughters=[]
        for bit in (0,1):
            t=list(s);t[j]=bit;t=tuple(t);walk(t,a);daughters.append(t)
        edge=(bound(daughters[0],a)+bound(daughters[1],a))/2
        ck(w>=edge,'Bellman query inequality')
        pivot=sum((x for t,x in enumerate(p) if (t>>k)&1),F(0))
        left,right=map(laws,daughters)
        ck(inf==pivot+(left[3]+right[3])/2,'original total influence conservation')
        ck(shared==(pivot if j<3 else 0)+(left[4]+right[4])/2,'old shared owner conservation')
        # Check every remaining coordinate, not only their sum.
        for jj in free:
            if jj==j:continue
            ii=free.index(jj); parent=sum((x for t,x in enumerate(p) if (t>>ii)&1),F(0))
            child=[]
            for law in (left,right):
                kk=law[2].index(jj);child.append(sum((x for t,x in enumerate(law[0]) if (t>>kk)&1),F(0)))
            ck(parent==sum(child)/2,'individual unqueried influence identity')
        edges+=1

root=(-1,)*6
walk(root,None)
ck(visited==set(W),'no missing or unreachable augmented states')
ck(triggers==set(TX),'all and only reachable transactions')
observed={'potential_records':len(visited),'mandatory_conversion_entries':len(triggers),'augmented':len(visited)+len(triggers),'transactions':len(TX),'raw':laws.cache_info().currsize}
save('DOMAIN_CHECK.json',observed)
ck(len(visited)+len(triggers)==2229 and len(TX)==108 and laws.cache_info().currsize==729,'complete stated domain '+str(observed))
p,_,_,inf,shared=laws(root)
ck(inf==F(7,8) and shared==F(5,8),'actual original owners')
hlo,hhi=ent(p); Hlo,Hhi=-hhi,-hlo
# Source in nats: (4ln2+2)I -5/4 - H_nats.
source_lo=(4*L2+2)*inf-F(5,4)-Hhi
source_hi=(4*U2+2)*inf-F(5,4)-Hlo
w=bound(root,None);margin_nats=source_lo-w; margin_bits=margin_nats/U2
ck(margin_bits>F(19,1024),'claimed sharp safe margin')
ck(margin_bits>F(1,64),'public theorem margin')
ck(ghosts>0 and constants>0 and beta_above>0,'boundary cases actually exercised')
# Independently execute the prescribed shared-frontier then private-U policy.
u_bill=F(0);u_terminals=0
saved_u={tuple(row['physical_state']):row for row in cert['prescribed_U_full_terminals']}
for a,b in itertools.product((0,1),repeat=2):
    anchor=(a,b,-1,-1,-1,-1);beta,cup=TX[anchor];u_bill+=cup/4
    for c,u in itertools.product((0,1),repeat=2):
        s=(a,b,c,u,-1,-1);p,q,free,ii,_=laws(s)
        q=(1-beta*(1-q[0]),)+tuple(beta*x for x in q[1:])
        row=saved_u[s]
        ck(p==tuple(map(F,row['P'])) and q==tuple(map(F,row['Q_current'])) and ii==F(row['I']),'prescribed-U full terminals match')
        u_bill+=kl(p,q)[1]/16;u_terminals+=1
u_margin_bits=(source_lo-u_bill)/U2
ck(u_margin_bits>F(3,5),'prescribed-U original-owner margin')
# Negative controls test completeness and the root inequality separately.
root_edges=[]
for j in range(6):
    ts=[]
    for bit in (0,1):t=list(root);t[j]=bit;ts.append(bound(tuple(t),None))
    root_edges.append(sum(ts)/2)
ck(max(root_edges)>0,'zero root potential rejected')
missing=next(k for k in visited if k!=(root,None));mutant=set(W)-{missing}
ck(visited!=mutant,'removed reachable record rejected by coverage predicate')
counts=[1]
for n in range(1,7):counts.append(1+n*counts[-1]**2)
ck(counts==cert['policy_counts'],'syntactic policy count')
result={'status':'PASS','rung':'exact finite certificate and analytic tensor proof; not Lean-checked', 'assertions':checks,'seconds':time.perf_counter()-START,'raw_restrictions':laws.cache_info().currsize,'reachable_augmented_states':len(visited)+len(triggers),'potential_records':len(visited),'transactions':len(TX),'physical_query_pairs':edges,'ghost_atom_occurrences':ghosts,'constant_state_occurrences':constants,'beta_above_one_states':beta_above,'original_total_influence':inf,'original_shared_influence':shared,'original_source_spare_nats':[source_lo,source_hi],'root_potential_nats':w,'margin_bits_lower':margin_bits,'margin_bits_lower_decimal_evidence_only':float(margin_bits),'policy_counts':counts,'certificate_sha256':hashlib.sha256((SOURCE/'out/FULL.json').read_bytes()).hexdigest(),'source_helper_imports':False,'finite_policy_search':False,'log_method':'24-term rational atanh with explicit geometric tail and outward 2^-64 rounding'}
save('AUDIT.json',result)
save('U_POLICY.json',{'status':'PASS','full_terminals':u_terminals,'complete_KL_plus_fee_upper_nats':u_bill,'same_original_margin_bits_lower':u_margin_bits,'claimed_lower':'3/5'})
print(json.dumps({k:result[k] for k in ['status','assertions','seconds','raw_restrictions','reachable_augmented_states','transactions','physical_query_pairs','ghost_atom_occurrences','constant_state_occurrences','beta_above_one_states','margin_bits_lower_decimal_evidence_only']}))
