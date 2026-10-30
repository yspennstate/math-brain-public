from pathlib import Path
import json,time,sys,hashlib,itertools,math
ROOT=Path(__file__).resolve().parents[1]
raw=(ROOT.parent/'20261023T053636Z-fleet03-A076-threshold-and-tribes-controls'/'code'/'arithmetic.py').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='af2c8fdd2ff2063cc60d12fd5256f6bcaec59c1a27213c39eff444a07c0be865'
(ROOT/'code'/'arithmetic.py').write_bytes(raw)
exec(compile(raw.decode('utf-8'),str(ROOT/'code'/'arithmetic.py'),'exec'))
B_i_original=B
pilot='--pilot' in sys.argv;limit=55 if pilot else 600
counts={'roots':0,'partial_states':0,'queries':0,'mixed_nodes':0,'mixed_leaves':0,'handoffs':0,'future_shared_nodes':0}
def guard():
    if time.perf_counter()-start>limit:raise RuntimeError('Frozen runtime reached')
def mean(t):return F(sum(t),len(t))
def var(t):return 1-mean(t)**2
def maj(d):return tuple(1 if 2*z.bit_count()<d else -1 for z in range(1<<d))
def collision(v,w,p):return plus(*[(plus((phi((a+b)**2),F(1,2)),(phi((a-b)**2),F(1,2)),(phi(a*a),F(-1)),(phi(b*b),F(-1))),p) for a,b in zip(coeff(v)[1:],coeff(w)[1:])])
def TT(st):
    N=1<<len(st['pr']);return tuple(st['v'][s][x] if s in st['v'] else st['h'][s] for s in range(len(st['h'])) for x in range(N))
def U(st):return plus(*[(H(vv),F(1,len(st['h']))) for vv in st['v'].values()])
def Rv(st):return F(len(st['sh']),len(st['h']))*sum((var(vv) for vv in st['v'].values()),F(0))
def X(st):return collision(st['v'][0],st['v'][1],F(1,len(st['h']))) if len(st['v'])==2 else {}
def Z(st):
    mt=tuple(mean(st['v'][s]) if s in st['v'] else F(st['h'][s]) for s in range(len(st['h'])))
    return plus((H(mt),F(1)),({F(2):Rv(st)+1},F(1)),*[(phi(mean(vv)**2),-F(1,len(st['h']))) for vv in st['v'].values()])
def K(st):
    if len(st['v'])==2:
        p=F(1,len(st['h']));return plus(({F(2):p*st['beta']},F(1)),(st['chi'],-p),(X(st),F(1)))
    return st['frozen']
def branch(st,name,bit):
    out=dict(st);pr=list(st['pr']);sh=list(st['sh'])
    if name in pr:
        i=pr.index(name);pr.remove(name);out['v']={a:child(vv,i,bit) for a,vv in st['v'].items()}
    else:
        i=sh.index(name);sh.remove(name);out['h']=child(st['h'],i,bit)
        def remove(a):return (a&((1<<i)-1))+((a>>(i+1))<<i)
        out['v']={remove(a):vv for a,vv in st['v'].items() if ((a>>i)&1)==bit}
        if len(st['v'])==2 and len(out['v'])==1:out['frozen']=K(st)
        elif len(st['v'])==2 and not out['v']:out['frozen']={}
    out['pr']=tuple(pr);out['sh']=tuple(sh);return out
def make(v,w,d,names=None,B=None):
    p=F(1,1<<d)
    return {'h':maj(d),'v':{0:v,1:w},'pr':tuple(names or ('x'+str(i) for i in range(len(v).bit_length()-1))),'sh':tuple('s'+str(i+1) for i in range(d)),'beta':(4*p if B is None else B)/p,'chi':plus((collision(v,w,p),1/p)),'frozen':{}}
def identity(st):
    equal_expr(plus((H(TT(st)),F(1)),(U(st),F(-1)),(X(st),F(-1)),({F(2):Rv(st)},F(-1)),(Z(st),F(-1)),({F(2):1},F(1))))
def diff(fun,st,kids):return plus((fun(st),F(1)),(fun(kids[0]),F(-1,2)),(fun(kids[1]),F(-1,2)))
def local(st,name,kids):
    dh=diff(lambda a:H(TT(a)),st,kids);du=diff(U,st,kids);dr=Rv(st)-(Rv(kids[0])+Rv(kids[1]))/2;dx=diff(X,st,kids);dk=diff(K,st,kids);dz=diff(Z,st,kids)
    equal_expr(plus((dh,F(1)),(du,F(-1)),(dx,F(-1)),({F(2):dr},F(-1)),(dz,F(-1))))
    leq(plus((dx,F(1)),(dk,F(-1))),0)
    leq(plus((dh,F(1)),(du,F(-1)),(dk,F(-1)),(dz,F(-1))),dr)
    return dh,du,dr,dk,dz
domains=[(0,5)] if pilot else [(0,5),(1,5),(0,7)]
for n,d in domains:
  for v in itertools.product((-1,1),repeat=1<<n):
    for w in itertools.product((-1,1),repeat=1<<n):
      root=make(tuple(v),tuple(w),d);i0=I(root['h']);names=root['pr']+root['sh']
      for assignment in itertools.product((-1,0,1),repeat=n+d):
        guard();st=root
        for name,bit in zip(names,assignment):
            if bit!=-1:st=branch(st,name,bit)
        identity(st);z=Z(st);leq(plus((z,F(-1))),0);leq(z,35*i0)
        leq(plus((z,F(1)),(H(st['h']),F(-1))),26)
        eq(Rv(st)<=1,True);eq(I(st['h'])<=i0,True);leq(H(st['h']),9*i0)
        # Worst-case old bill58, never a renewed conditional source.
        leq(z,96*i0-58-3*i0)
        for name in st['pr']+st['sh']:
            kids=[branch(st,name,b) for b in (0,1)];local(st,name,kids);counts['queries']+=1
        counts['partial_states']+=1
      counts['roots']+=1;coeff.cache_clear()

pn=('z1','z2','z3','z4','x1','x2','y')
v=tuple((-1 if z>>6&1 else 1)*(-1 if ((z&1)*((z>>1)&1)+((z>>2)&1)*((z>>3)&1))%2 else 1) for z in range(128))
w=tuple((-1 if z>>6&1 else 1)*(-1 if z%64==0 else 1) for z in range(128))
e0=F(1,32);S=11*e0;FIRST=4*e0;D0=e0;B=S-FIRST-D0
policies=[(('y','s2','z1','s3','s4'),('s5','x2','s1','z2')),(('s3','y','s2','x2','s4'),('z1','s1','z2','s5'))]
ledger=[];results=[]
for prefix,suffix in policies[:1 if pilot else 2]:
  policy=prefix+suffix
  for firstbit in (0,1):
    root=make(child(v,4,firstbit),child(w,4,firstbit),5,tuple(a for a in pn if a!='x1'),B)
    i0=I(root['h']);quota=96*i0
    totals={'H':{},'U':{},'K':{},'Z':{},'Lambda':{},'R':F(0),'I':F(0),'mass':F(0),'old_private':F(0),'old_L':F(0),'spent':F(0)}
    def walk(st,depth,reach,path='',oldL=F(0),shared_before=0,frozen=None):
        guard();tt=TT(st);z=Z(st);k=K(st);identity(st)
        if depth==len(prefix):
            frozen=plus(({F(2):quota-oldL},F(1)),(z,F(-1)))
            leq(plus((frozen,F(-1))),-3*i0);counts['handoffs']+=1
            equal_expr(plus((z,F(1)),(frozen,F(1)),({F(2):oldL-quota},F(1))))
        row={'policy':list(policy),'prefix_length':len(prefix),'first_x1_bit':firstbit,'path':path,'reach':str(reach),'phase':'old' if depth<len(prefix) else 'new','old_shared_L':str(oldL),'original_Q':str(quota),'original_I0':str(i0),'remaining_shared':list(st['sh']),'remaining_private':list(st['pr']),'profile_means':{str(a):str(mean(vv)) for a,vv in st['v'].items()},'H_interval':[str(x) for x in bounds(H(tt))],'I':str(I(tt)),'U_interval':[str(x) for x in bounds(U(st))],'R':str(Rv(st)),'K_interval':[str(x) for x in bounds(k)],'Z_interval':[str(x) for x in bounds(z)],'Lambda_interval':None if frozen is None else [str(x) for x in bounds(frozen)]}
        ledger.append(row)
        if depth==len(policy):
            row['terminal']=True;counts['mixed_leaves']+=1
            for key,expr in [('H',H(tt)),('U',U(st)),('K',k),('Z',z),('Lambda',frozen)]:totals[key]=plus((totals[key],F(1)),(expr,reach))
            totals['R']+=reach*Rv(st);totals['I']+=reach*I(tt);totals['old_L']+=reach*oldL;totals['mass']+=reach;return
        name=policy[depth];idx=(st['pr']+st['sh']).index(name);kids=[branch(st,name,b) for b in (0,1)];is_shared=name in st['sh'];ij=inf(tt,idx)
        for bit,kid in enumerate(kids):eq(child(tt,idx,bit),TT(kid))
        dh,du,dr,dk,dz=local(st,name,kids)
        nextL=oldL
        if depth<len(prefix):
            price=(5,15,38)[shared_before] if is_shared else 12
            leq(plus((dh,F(1)),(du,F(-1)),(dk,F(-1))),dr+price*ij)
            if is_shared:nextL+=price*ij
            else:totals['old_private']+=reach*ij
        elif is_shared:counts['future_shared_nodes']+=1
        row.update({'terminal':False,'query':name,'actual_query_influence':str(ij),'old_charge':str(nextL-oldL),'reserve_release':str(dr),'delta_Z_interval':[str(x) for x in bounds(dz)]})
        if not is_shared:
            inherited=plus(*[(Bexpr(vv,idx),F(1,len(st['h']))) for vv in st['v'].values()]) if st['v'] else {}
            row['inherited_full_core_erasure_interval']=[str(x) for x in bounds(inherited)]
        totals['spent']+=reach*ij;counts['mixed_nodes']+=1
        for bit,kid in enumerate(kids):walk(kid,depth+1,reach/2,path+str(bit),nextL,shared_before+int(is_shared),frozen)
    # Keep the inherited B_i routine distinct from the original collision budget B.
    Bexpr=globals().get('B_i_original')
    if Bexpr is None:raise RuntimeError('erasure helper alias missing')
    walk(root,0,F(1));eq(totals['mass'],1);eq(I(TT(root))-totals['I'],totals['spent'])
    lhs=plus((H(TT(root)),F(1)),(totals['H'],F(-1)),(totals['K'],F(1)),(totals['Z'],F(1)),(totals['Lambda'],F(1)),({F(2):totals['R']},F(1)),(U(root),F(-1)),(totals['U'],F(1)))
    leq(lhs,Rv(root)+B+quota+12*totals['old_private']);leq(plus((totals['K'],F(-1))),-2*e0);leq(plus((totals['Lambda'],F(-1))),-3*i0)
    results.append({'policy':list(policy),'first_x1_bit':firstbit,'old_shared_charge_expectation':str(totals['old_L']),'original_shared_quota':str(quota),'expected_K_interval':[str(x) for x in bounds(totals['K'])],'expected_Lambda_interval':[str(x) for x in bounds(totals['Lambda'])],'guaranteed_collision_remainder':str(2*e0),'guaranteed_carrier_remainder':str(3*i0),'FIRST_collision_debit':str(FIRST),'old_D0':str(D0),'original_collision_B':str(B),'expected_terminal_H_interval':[str(x) for x in bounds(totals['H'])],'expected_terminal_I':str(totals['I'])})
    coeff.cache_clear()
out={'status':'PASS','pilot':pilot,'assertions':checks,'counts':counts,'elapsed_seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(raw).hexdigest(),'histories':results,'first_unsupported_line':'Hereditary carrier entropy/source eligibility and influence-controlled disturbance for a growing edited block remain unpaid; Q is an explicit ORIGINAL allowance, not consumed-influence payment.'}
(ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
if not pilot:(ROOT/'out'/'MIXED_LEDGER.json').write_text(json.dumps(ledger,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','pilot','assertions','counts','elapsed_seconds']}),flush=True)
