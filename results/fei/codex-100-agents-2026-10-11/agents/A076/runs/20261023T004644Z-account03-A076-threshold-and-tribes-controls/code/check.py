"""Frozen A076 stage8 census and complete-sibling mixed histories."""
from pathlib import Path
import sys, json, time, hashlib, itertools
ROOT=Path(__file__).resolve().parents[1]
old=ROOT.parent/'20261021T201341Z-account03-A076-threshold-and-tribes-controls'/'code'/'arithmetic.py'
raw=old.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='af2c8fdd2ff2063cc60d12fd5256f6bcaec59c1a27213c39eff444a07c0be865'
(ROOT/'code'/'arithmetic.py').write_bytes(raw)
exec(compile(raw.decode('utf-8'),str(ROOT/'code'/'arithmetic.py'),'exec'))
pilot='--pilot' in sys.argv
limit=55 if pilot else 600
counts={'two_point_roots':0,'one_point_roots':0,'root_queries':0,'mixed_nodes':0,'mixed_leaves':0,'direct_reproductions':0}
def guard():
    if time.perf_counter()-start>limit:raise RuntimeError('Frozen time limit reached; no escalation')
def mean(t):return F(sum(t),len(t))
def delt(t,i):return plus((H(t),F(1)),(H(child(t,i,0)),F(-1,2)),(H(child(t,i,1)),F(-1,2)))
def tabs(n):return itertools.product((-1,1),repeat=1<<n)
def two(v,w,d):return tuple(v[x] if s==0 else w[x] if s==1 else 1 for s in range(1<<d) for x in range(len(v)))
def one(v,r):return tuple(v[x] if s==0 else 1 for s in range(1<<r) for x in range(len(v)))
def xi(v,w,d):
    e=F(1,1<<d)
    return plus(*[(plus((phi((a+b)**2),F(1,2)),(phi((a-b)**2),F(1,2)),(phi(a*a),F(-1)),(phi(b*b),F(-1))),e) for a,b in zip(coeff(v)[1:],coeff(w)[1:])])
def variance(v):return 1-mean(v)**2
def private_check(t,v,w,d,i):
    e=F(1,1<<d)
    dx=plus((xi(v,w,d),F(1)),(xi(child(v,i,0),child(w,i,0),d),F(-1,2)),(xi(child(v,i,1),child(w,i,1),d),F(-1,2)))
    release=d*e*(coeff(v)[1<<i]**2+coeff(w)[1<<i]**2)
    leq(plus((delt(t,i),F(1)),(delt(v,i),-e),(delt(w,i),-e),(dx,F(-1))),release+12*inf(t,i))
    eq(inf(t,i),e*(inf(v,i)+inf(w,i)))
def direct(t):
    c=tuple(F(sum(a*(-1 if (s&z).bit_count()%2 else 1) for z,a in enumerate(t)),len(t)) for s in range(len(t)))
    eq(c,coeff(t))
    for i in range(len(t).bit_length()-1):eq(inf(t,i),F(sum(t[z]!=t[z^(1<<i)] for z in range(len(t))),len(t)))
    counts['direct_reproductions']+=1
for n in range(2 if pilot else 3):
  for v0 in tabs(n):
    for w0 in tabs(n):
      v,w=tuple(v0),tuple(w0)
      for d in range(1,3 if pilot else 4):
        guard();e=F(1,1<<d);t=two(v,w,d);cv,cw=coeff(v),coeff(w)
        leq(xi(v,w,d),0);leq(plus((xi(v,w,d),F(-1))),4*e)
        if n<=1 and d<=2:direct(t)
        for i in range(n):private_check(t,v,w,d,i)
        # Separator erasure: independently aggregate the empty-private rows.
        q=2-mean(v)-mean(w);c=mean(v)-mean(w)
        b0=plus((Phi((1-e*q)**2,e*e*c*c),F(1)),(Phi(e*e*q*q,e*e*c*c),1/(2*e)-1))
        mu_erasure=plus(*[(Phi(coeff(t)[s]**2,coeff(t)[s|(1<<n)]**2),F(1)) for s in range(len(t)) if not s>>n&1 and s%len(v)==0])
        equal_expr(plus((b0,F(1)),(mu_erasure,F(-1))))
        j=2*e*F(sum(a!=b for a,b in zip(v,w)),len(v));eq(inf(t,n),j)
        release=e*(variance(v)+variance(w))
        leq(plus((B(t,n),F(1)),(b0,F(-1))),release)
        leq(b0,6*j)
        leq(delt(t,n),release+9*j)
        for k in range(1,d):
            i=n+k;j=e*(2-mean(v)-mean(w));eq(inf(t,i),j)
            leq(delt(t,i),6*j)
            # Surviving gate doubles both Xi and the constant-density account.
            equal_expr(plus((xi(v,w,d),F(1)),(xi(v,w,d-1),F(-1,2))))
        counts['two_point_roots']+=1;counts['root_queries']+=n+d
        coeff.cache_clear()
for n in range(2 if pilot else 3):
  for vv in tabs(n):
    v=tuple(vv)
    for r in range(2 if pilot else 3):
      guard();p=F(1,1<<r);t=one(v,r)
      for i in range(n):
        release=r*p*coeff(v)[1<<i]**2
        leq(plus((delt(t,i),F(1)),(delt(v,i),-p)),release+11*inf(t,i))
      for k in range(r):
        i=n+k;w=p*(1-mean(v));eq(inf(t,i),w)
        exact=plus((Phi((1-w)**2,w*w),F(1)),({F(2):2*w*(1-w)},F(1)))
        equal_expr(plus((B(t,i),F(1)),(exact,F(-1))))
        leq(delt(t,i),6*w)
      counts['one_point_roots']+=1;counts['root_queries']+=n+r;coeff.cache_clear()

# Truth tables use z1,z2,z3,z4,x1,x2,y as private low-order bits.
names0=('z1','z2','z3','z4','x1','x2','y')
v=tuple((-1 if z>>6&1 else 1)*(-1 if ((z&1)*((z>>1)&1)+((z>>2)&1)*((z>>3)&1))%2 else 1) for z in range(128))
w=tuple((-1 if z>>6&1 else 1)*(-1 if z%64==0 else 1) for z in range(128))
eq(I(v),F(3));equal_expr(plus((H(v),F(1)),({F(2):4},F(-1))))
e0=F(1,8);S=11*e0;old_debit=4*e0;bank=S-old_debit
policies=[('s2','x2','s1','z1','y'),('z1','s3','z2','s1','x2'),('x2','s2','z1','s3','z2','s1','y')]
def core(st):
    if st['mode']=='dead':return {}
    p=F(1,1<<len(st['shared']))
    return plus((H(st['v']),p),*([(H(st['w']),p)] if st['mode']=='two' else []))
def pot(st):
    if st['mode']=='dead':return F(0)
    r=len(st['shared']);p=F(1,1<<r)
    return r*p*(variance(st['v'])+(variance(st['w']) if st['mode']=='two' else 0))
def account(st):
    if st['mode']=='two':
        p=F(1,1<<len(st['shared']))
        return plus(({F(2):p*(st['beta'])},F(1)),(st['xio'],-p),(xi(st['v'],st['w'],len(st['shared'])),F(1)))
    return st['frozen']
def table(st):
    if st['mode']=='dead':return (1,)*(1<<(len(st['private'])+len(st['shared'])))
    # s1, the separator, stays first while present.
    return two(st['v'],st['w'],len(st['shared'])) if st['mode']=='two' else one(st['v'],len(st['shared']))
def branch(st,name,bit):
    out=dict(st);pr=list(st['private']);sh=list(st['shared'])
    if name in pr:
        idx=pr.index(name);pr.remove(name)
        if st['mode']!='dead':
            out['v']=child(st['v'],idx,bit)
            if st['mode']=='two':out['w']=child(st['w'],idx,bit)
    else:
        idx=sh.index(name);sh.remove(name)
        if st['mode']=='two' and name=='s1':
            out['mode']='one';out['v']=st['v'] if bit==0 else st['w'];out['frozen']=account(st)
        elif st['mode']!='dead' and bit==1:
            out['mode']='dead';out['frozen']={} if st['mode']=='two' else st['frozen']
    out['private']=tuple(pr);out['shared']=tuple(sh)
    return out
mixed=[];ledger=[]
for policy in policies[:1 if pilot else 3]:
  branch_results=[]
  for firstbit in (0,1):
    vv=child(v,4,firstbit);ww=child(w,4,firstbit);pn=tuple(a for a in names0 if a!='x1')
    xio=plus((xi(vv,ww,3),1/e0))
    root={'mode':'two','v':vv,'w':ww,'private':pn,'shared':('s1','s2','s3'),'beta':bank/e0,'xio':xio,'frozen':None}
    equal_expr(plus((account(root),F(1)),({F(2):bank},F(-1))))
    totals={'H':{},'T':{},'R':F(0),'K':{},'private':F(0),'gate':F(0),'separator':F(0),'mass':F(0)}
    def walk(st,depth,weight,path=''):
        guard();tt=table(st);kk=account(st);leq(plus((kk,F(-1))),0)
        entry={'policy':list(policy),'first_x1_bit':firstbit,'path':path,'reach_probability':str(weight),'mode':st['mode'],'remaining_private':list(st['private']),'remaining_shared':list(st['shared']),'H_interval':[str(a) for a in bounds(H(tt))],'I':str(I(tt)),'R':str(pot(st)),'K_interval':[str(a) for a in bounds(kk)],'inherited_H_interval':[str(a) for a in bounds(core(st))]}
        ledger.append(entry)
        if depth==len(policy) or st['mode']=='dead':
            entry['terminal']=True
            totals['H']=plus((totals['H'],F(1)),(H(tt),weight));totals['T']=plus((totals['T'],F(1)),(core(st),weight));totals['R']+=weight*pot(st)
            totals['K']=plus((totals['K'],F(1)),(kk,weight));totals['mass']+=weight;counts['mixed_leaves']+=1;return
        name=policy[depth];allnames=st['private']+st['shared'];idx=allnames.index(name)
        kids=[branch(st,name,b) for b in (0,1)]
        for b,kid in enumerate(kids):eq(child(tt,idx,b),table(kid))
        delta=plus((H(tt),F(1)),(H(table(kids[0])),F(-1,2)),(H(table(kids[1])),F(-1,2)))
        dc=plus((core(st),F(1)),(core(kids[0]),F(-1,2)),(core(kids[1]),F(-1,2)))
        dr=pot(st)-(pot(kids[0])+pot(kids[1]))/2
        dk=plus((kk,F(1)),(account(kids[0]),F(-1,2)),(account(kids[1]),F(-1,2)))
        kind='private' if name in st['private'] else ('separator' if name=='s1' and st['mode']=='two' else 'gate')
        price={'private':12,'separator':9,'gate':6}[kind];actual=inf(tt,idx)
        entry.update({'terminal':False,'query':name,'query_kind':kind,'actual_query_influence':str(actual),'entropy_decrement_interval':[str(a) for a in bounds(delta)],'reserve_release':str(dr),'account_decrement_interval':[str(a) for a in bounds(dk)]})
        if kind=='private':
            p=F(1,1<<len(st['shared']))
            inherited_B=plus((B(st['v'],idx),p),*([(B(st['w'],idx),p)] if st['mode']=='two' else []))
            entry['full_inherited_core_erasure_interval']=[str(a) for a in bounds(inherited_B)]
            # Quarter-scaled erasures are retained as data, never substituted for full inputs.
            entry['quarter_inherited_core_erasure_interval']=[str(a/4) for a in bounds(inherited_B)]
        leq(plus((delta,F(1)),(dc,F(-1)),(dk,F(-1))),dr+price*actual)
        if kind!='private' or st['mode']!='two':equal_expr(dk)
        if kind=='separator':
            for kid in kids:equal_expr(plus((account(kid),F(1)),(kk,F(-1))))
        totals[kind]+=weight*actual;counts['mixed_nodes']+=1
        for bit,kid in enumerate(kids):walk(kid,depth+1,weight/2,path+str(bit))
    walk(root,0,F(1));eq(totals['mass'],F(1))
    lhs=plus((H(table(root)),F(1)),(totals['H'],F(-1)),(totals['K'],F(1)),({F(2):totals['R']},F(1)),(core(root),F(-1)),(totals['T'],F(1)))
    rhs=pot(root)+bank+12*totals['private']+6*totals['gate']+9*totals['separator']
    leq(lhs,rhs);leq(plus((totals['K'],F(-1))),-(S-8*e0))
    branch_results.append({'first_x1_bit':firstbit,'expected_remaining_bank_interval':[str(a) for a in bounds(totals['K'])],'guaranteed_remaining_bank':str(S-8*e0),'old_debit':str(old_debit),'input_bank':str(bank),'expected_terminal_H_interval':[str(a) for a in bounds(totals['H'])],'private_query_influence':str(totals['private']),'gate_query_influence':str(totals['gate']),'separator_query_influence':str(totals['separator'])})
    coeff.cache_clear()
  mixed.append({'policy':list(policy),'all_first_query_children':branch_results})
result={'status':'PASS','pilot':pilot,'assertions':checks,'counts':counts,'elapsed_seconds':time.perf_counter()-start,'arithmetic_helper_sha256':hashlib.sha256(raw).hexdigest(),'mixed_histories':mixed,'first_unproved_line':'Extension to a nonconstant outside carrier, or an unrestricted original donor certificate, is not proved.'}
(ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
if not pilot:(ROOT/'out'/'MIXED_LEDGER.json').write_text(json.dumps(ledger,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'pilot':pilot,'assertions':checks,'counts':counts,'elapsed_seconds':result['elapsed_seconds']}),flush=True)
