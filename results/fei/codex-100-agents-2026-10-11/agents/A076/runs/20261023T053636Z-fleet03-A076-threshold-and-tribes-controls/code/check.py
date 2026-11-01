"""A076 stage9: parity leakage, physical influences, and one shared handoff."""
from pathlib import Path
import json,time,sys,hashlib,itertools,math
ROOT=Path(__file__).resolve().parents[1]
helper=ROOT.parent/'20261023T004644Z-fleet03-A076-threshold-and-tribes-controls'/'code'/'arithmetic.py'
raw=helper.read_bytes();assert hashlib.sha256(raw).hexdigest()=='af2c8fdd2ff2063cc60d12fd5256f6bcaec59c1a27213c39eff444a07c0be865'
(ROOT/'code'/'arithmetic.py').write_bytes(raw)
exec(compile(raw.decode('utf-8'),str(ROOT/'code'/'arithmetic.py'),'exec'))
pilot='--pilot' in sys.argv;limit=55 if pilot else 600
counts={'roots':0,'physical_queries':0,'direct_reproductions':0,'mixed_nodes':0,'mixed_leaves':0,'shared_handoffs':0}
def guard():
    if time.perf_counter()-start>limit:raise RuntimeError('Frozen runtime reached; no enlargement')
def mean(t):return F(sum(t),len(t))
def var(t):return 1-mean(t)**2
def delta(t,i):return plus((H(t),F(1)),(H(child(t,i,0)),F(-1,2)),(H(child(t,i,1)),F(-1,2)))
def majority(d):return tuple(1 if s.bit_count()*2<d else -1 for s in range(1<<d))
def form(h,profiles,N):
    return tuple(profiles[s][x] if s in profiles else h[s] for s in range(len(h)) for x in range(N))
def collision(v,w,e):
    return plus(*[(plus((phi((a+b)**2),F(1,2)),(phi((a-b)**2),F(1,2)),(phi(a*a),F(-1)),(phi(b*b),F(-1))),e) for a,b in zip(coeff(v)[1:],coeff(w)[1:])])
def empty_erasure(t,n,j):
    cc=coeff(t);i=n+j
    return plus(*[(Phi(cc[s]**2,cc[s|(1<<i)]**2),F(1)) for s in range(0,len(t),1<<n) if not s>>i&1])
def direct(t):
    independent=tuple(F(sum(a*(-1 if (s&z).bit_count()%2 else 1) for z,a in enumerate(t)),len(t)) for s in range(len(t)))
    eq(independent,coeff(t))
    for i in range(len(t).bit_length()-1):eq(inf(t,i),F(sum(t[z]!=t[z^(1<<i)] for z in range(len(t))),len(t)))
    counts['direct_reproductions']+=1
for n in range(2 if pilot else 3):
  for vv in itertools.product((-1,1),repeat=1<<n):
    for ww in itertools.product((-1,1),repeat=1<<n):
      v,w=tuple(vv),tuple(ww)
      for d in ((5,) if pilot else (5,7)):
        guard();e=F(1,1<<d);h=majority(d);t=form(h,{0:v,1:w},len(v));cc=coeff(t)
        alpha=F(math.comb(d-1,(d-1)//2),1<<(d-1))
        Q=sum((cc[s<<n]**2 for s in range(1<<d) if s.bit_count()%2==0),F(0))
        eq(Q,e*((1-mean(v))**2+(1-mean(w))**2)/2);eq(Q<=4*e,True)
        totalmean=sum((cc[s<<n]**2 for s in range(1<<d)),F(0));eq(totalmean,1-e*(var(v)+var(w)))
        hb=plus((phi(Q),F(1)),(phi(1-Q),F(1)))
        leq(hb,4*d*e);eq(4*d*e<=2*alpha,True)
        for j in range(d):
            be=empty_erasure(t,n,j);i=n+j;ij=inf(t,i)
            actual=alpha+(2*e*F(sum(a!=b for a,b in zip(v,w)),len(v)) if j==0 else e*(2-mean(v)-mean(w)))
            eq(ij,actual);leq(be,2*ij)
            leq(plus((be,F(1)),(hb,F(-1))),0)
            release=e*(var(v)+var(w))
            leq(plus((B(t,i),F(1)),(be,F(-1))),release)
            leq(delta(t,i),release+5*ij)
            for bit in (0,1):
                c=child(t,i,bit);mu=mean(c)
                eq(mu!=0 and abs(mu)<1,True)
        for i in range(n):
            dx=plus((collision(v,w,e),F(1)),(collision(child(v,i,0),child(w,i,0),e),F(-1,2)),(collision(child(v,i,1),child(w,i,1),e),F(-1,2)))
            release=d*e*(coeff(v)[1<<i]**2+coeff(w)[1<<i]**2)
            leq(plus((delta(t,i),F(1)),(delta(v,i),-e),(delta(w,i),-e),(dx,F(-1))),release+12*inf(t,i))
            eq(inf(t,i),e*(inf(v,i)+inf(w,i)))
        if n==0 and d==5:direct(t)
        counts['roots']+=1;counts['physical_queries']+=n+d;coeff.cache_clear()

names=('z1','z2','z3','z4','x1','x2','y')
v=tuple((-1 if z>>6&1 else 1)*(-1 if ((z&1)*((z>>1)&1)+((z>>2)&1)*((z>>3)&1))%2 else 1) for z in range(128))
w=tuple((-1 if z>>6&1 else 1)*(-1 if z%64==0 else 1) for z in range(128))
eq(I(v),3);equal_expr(plus((H(v),F(1)),({F(2):4},F(-1))))
e0=F(1,32);S=11*e0;first_debit=4*e0;D0=e0;bank=S-first_debit-D0
policies=[('y','s2','z1','x2'),('z1','y','s1','x2'),('x2','z1','y','s3','z2')]
ledger=[];mixed=[]
def TT(st):return form(st['h'],st['profiles'],1<<len(st['pr']))
def core(st):
    p=F(1,len(st['h']));return plus(*[(H(vv),p) for vv in st['profiles'].values()])
def reserve(st):
    r=len(st['sh']);p=F(1,len(st['h']));return r*p*sum((var(vv) for vv in st['profiles'].values()),F(0))
def XI(st):
    if len(st['profiles'])!=2:return {}
    return collision(st['profiles'][0],st['profiles'][1],F(1,len(st['h'])))
def K(st):
    if len(st['profiles'])==2:return plus(({F(2):st['density']/len(st['h'])},F(1)),(XI(st),F(1)))
    return st['frozen']
def branch(st,name,bit):
    out=dict(st);pr=list(st['pr']);sh=list(st['sh'])
    if name in pr:
        i=pr.index(name);pr.remove(name)
        out['profiles']={a:child(vv,i,bit) for a,vv in st['profiles'].items()}
    else:
        i=sh.index(name);sh.remove(name);out['h']=child(st['h'],i,bit)
        def remove(z):return (z&((1<<i)-1))+((z>>(i+1))<<i)
        out['profiles']={remove(a):vv for a,vv in st['profiles'].items() if a>>i&1==bit}
        if len(st['profiles'])==2 and len(out['profiles'])==1:out['frozen']=K(st)
        elif len(st['profiles'])==2 and not out['profiles']:out['frozen']={}
    out['pr']=tuple(pr);out['sh']=tuple(sh);return out
for policy in policies[:1 if pilot else 3]:
  runs=[]
  for initialbit in (0,1):
    vv=child(v,4,initialbit);ww=child(w,4,initialbit)
    xo=collision(vv,ww,e0)
    # Xi is a logarithm expression: encode its scalar density as another expression.
    root={'h':majority(5),'profiles':{0:vv,1:ww},'pr':tuple(x for x in names if x!='x1'),'sh':('s1','s2','s3','s4','s5'),'density':bank/e0,'frozen':{},'xio':plus((xo,1/e0))}
    # The source-normalized -Xi_o is a signed expression, retained at every two-point node.
    oldK=K
    def account(st):
        if len(st['profiles'])==2:
            p=F(1,len(st['h']));return plus(({F(2):p*st['density']},F(1)),(st['xio'],-p),(XI(st),F(1)))
        return st['frozen']
    K=account
    equal_expr(plus((K(root),F(1)),({F(2):bank},F(-1))))
    totals={'H':{},'U':{},'K':{},'R':F(0),'Ileaf':F(0),'mass':F(0),'private':F(0),'shared':F(0)}
    def walk(st,depth,reach,path=''):
        guard();t=TT(st);k=K(st);leq(plus((k,F(-1))),0)
        row={'policy':list(policy),'first_x1_bit':initialbit,'path':path,'reach':str(reach),'remaining_private':list(st['pr']),'remaining_shared':list(st['sh']),'carrier':list(st['h']),'profile_means':{str(a):str(mean(vv)) for a,vv in st['profiles'].items()},'H_interval':[str(x) for x in bounds(H(t))],'I':str(I(t)),'U_interval':[str(x) for x in bounds(core(st))],'R':str(reserve(st)),'K_interval':[str(x) for x in bounds(k)]}
        ledger.append(row)
        if depth==len(policy) or not st['profiles']:
            row['terminal']=True;counts['mixed_leaves']+=1
            for key,expr in [('H',H(t)),('U',core(st)),('K',k)]:totals[key]=plus((totals[key],F(1)),(expr,reach))
            totals['R']+=reach*reserve(st);totals['Ileaf']+=reach*I(t);totals['mass']+=reach;return
        name=policy[depth];idx=(st['pr']+st['sh']).index(name);kids=[branch(st,name,b) for b in (0,1)]
        for bit,kid in enumerate(kids):eq(child(t,idx,bit),TT(kid))
        dh=delta(t,idx);du=plus((core(st),F(1)),(core(kids[0]),F(-1,2)),(core(kids[1]),F(-1,2)))
        dr=reserve(st)-(reserve(kids[0])+reserve(kids[1]))/2
        dk=plus((k,F(1)),(K(kids[0]),F(-1,2)),(K(kids[1]),F(-1,2)))
        kind='private' if name in st['pr'] else 'shared';ij=inf(t,idx);price=12 if kind=='private' else 5
        leq(plus((dh,F(1)),(du,F(-1)),(dk,F(-1))),dr+price*ij)
        row.update({'terminal':False,'query':name,'kind':kind,'actual_influence':str(ij),'delta_H_interval':[str(x) for x in bounds(dh)],'release_R':str(dr),'delta_K_interval':[str(x) for x in bounds(dk)]})
        if kind=='shared':
            eq(len(st['sh']),5);equal_expr(dk);equal_expr(du);counts['shared_handoffs']+=1
            for kid in kids:eq(mean(TT(kid))!=0 and abs(mean(TT(kid)))<1,True)
        else:
            inherited=plus(*[(B(vv,idx),F(1,len(st['h']))) for vv in st['profiles'].values()])
            row['inherited_full_core_B_interval']=[str(x) for x in bounds(inherited)]
            row['inherited_quarter_core_B_interval']=[str(x/4) for x in bounds(inherited)]
        totals[kind]+=reach*ij;counts['mixed_nodes']+=1
        for bit,kid in enumerate(kids):walk(kid,depth+1,reach/2,path+str(bit))
    walk(root,0,F(1));eq(totals['mass'],1)
    lhs=plus((H(TT(root)),F(1)),(totals['H'],F(-1)),(totals['K'],F(1)),({F(2):totals['R']},F(1)),(core(root),F(-1)),(totals['U'],F(1)))
    leq(lhs,reserve(root)+bank+12*totals['private']+5*totals['shared'])
    leq(plus((totals['K'],F(-1))),-2*e0)
    eq(I(TT(root))-totals['Ileaf'],totals['private']+totals['shared'])
    runs.append({'first_x1_bit':initialbit,'expected_terminal_H_interval':[str(x) for x in bounds(totals['H'])],'expected_terminal_I':str(totals['Ileaf']),'expected_K_interval':[str(x) for x in bounds(totals['K'])],'guaranteed_remaining_K':str(2*e0),'original_S':str(S),'FIRST_debit':str(first_debit),'old_D0':str(D0),'continuation_B':str(bank),'spent_private_influence':str(totals['private']),'spent_shared_influence':str(totals['shared'])})
    coeff.cache_clear()
  mixed.append({'policy':list(policy),'both_first_x1_children':runs})
result={'status':'PASS','pilot':pilot,'assertions':checks,'counts':counts,'elapsed_seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(raw).hexdigest(),'mixed_histories':mixed,'first_unsupported_line':'Second shared query on the already paid biased cofactor lacks the parity-zero certificate; unrestricted source admission and input/terminal FEI remain open.'}
(ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
if not pilot:(ROOT/'out'/'MIXED_LEDGER.json').write_text(json.dumps(ledger,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','pilot','assertions','counts','elapsed_seconds']}),flush=True)
