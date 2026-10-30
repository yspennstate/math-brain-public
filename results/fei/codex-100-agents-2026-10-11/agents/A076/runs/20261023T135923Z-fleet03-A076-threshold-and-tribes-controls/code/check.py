from pathlib import Path
import sys,json,hashlib,itertools,math,time
ROOT=Path(__file__).resolve().parents[1]
raw=(ROOT.parent/'20261023T114019Z-fleet03-A076-threshold-and-tribes-controls/code/arithmetic.py').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='af2c8fdd2ff2063cc60d12fd5256f6bcaec59c1a27213c39eff444a07c0be865'
(ROOT/'code/arithmetic.py').write_bytes(raw)
exec(compile(raw.decode('utf-8'),str(ROOT/'code/arithmetic.py'),'exec'))
pilot='--pilot' in sys.argv;limit=55 if pilot else 600
counts={'roots':0,'root_queries':0,'partial_states':0,'partial_queries':0,'mixed_nodes':0,'mixed_leaves':0,'majority_dimensions':0,'event_dimensions':0,'growth_parameters':0}
def guard():
    if time.perf_counter()-start>limit:raise RuntimeError('Frozen runtime limit reached')
def mean(t):return F(sum(t),len(t))
def make(v,d,k):return {'h':tuple(1 if s.bit_count()<=d//2 else -1 for s in range(1<<d)),'a':tuple(1 if s.bit_count()<=k else 0 for s in range(1<<d)),'v':tuple(v),'pr':tuple('x'+str(i) for i in range(len(v).bit_length()-1)),'sh':tuple('s'+str(i) for i in range(d))}
def branch(st,name,bit):
    out=dict(st)
    if name in st['pr']:
        i=st['pr'].index(name);out['v']=child(st['v'],i,bit);out['pr']=tuple(x for x in st['pr'] if x!=name)
    else:
        i=st['sh'].index(name);out['h']=child(st['h'],i,bit);out['a']=child(st['a'],i,bit);out['sh']=tuple(x for x in st['sh'] if x!=name)
    return out
def TT(st):return tuple(v if a else h for h,a in zip(st['h'],st['a']) for v in st['v'])
def values(st):
    p=mean(st['a']);mu=mean(st['v']);m=tuple(F(h)+(mu-1)*a for h,a in zip(st['h'],st['a']));a_sign=tuple(2*a-1 for a in st['a']);e=H(m);j=H(st['a']);u=plus((H(st['v']),p));r=plus((j,(1-mu*mu)/2));z=plus((e,F(1)),(r,F(1)),(phi(mu*mu),-p),({F(2):1},F(1)))
    return {'p':p,'mu':mu,'m':m,'a_sign':a_sign,'E':e,'J':j,'U':u,'R':r,'Z':z,'H':H(TT(st))}
def subtract(a,b):return plus((a,F(1)),(b,F(-1)))
def verify(st,i0):
    guard();v=values(st);p=v['p'];mu=v['mu'];aa=v['a_sign'];hh=H(st['h']);ha=H(aa)
    equal_expr(plus((v['H'],F(1)),(v['U'],F(-1)),(v['R'],F(-1)),(v['Z'],F(-1)),({F(2):1},F(1))))
    equal_expr(plus((v['J'],F(1)),(phi(p*p),F(-1)),(ha,F(-1,4)),(phi(mean(aa)**2),F(1,4)),({F(2):2*p*(1-p)},F(-1))))
    leq(subtract(v['E'],plus((hh,F(2)),(ha,F(2)))),6)
    leq(plus((v['Z'],F(-1))),0);leq(v['Z'],45*i0);leq(v['Z'],96*i0-58-20*i0)
    leq(hh,9*i0);leq(ha,9*i0);eq(I(st['h'])<=i0,True);eq(I(aa)<=i0,True)
    ct=coeff(st['h']);ca=coeff(aa);cm=coeff(v['m']);q=(1-mu)/2
    for s in range(1,len(ct)):
        eq(cm[s],ct[s]-q*ca[s]);eq(cm[s]**2<=2*(ct[s]**2+ca[s]**2),True)
    actual=TT(st);np=len(st['pr']);shared=sum((inf(actual,np+i) for i in range(len(st['sh']))),F(0));priv=sum((inf(actual,i) for i in range(np)),F(0))
    eq(shared,I(st['h'])+q*I(aa));eq(priv,p*I(st['v']))
    return v
def local(st,name,i0):
    v=values(st);kids=[branch(st,name,b) for b in (0,1)];vk=[values(k) for k in kids]
    i=(st['pr']+st['sh']).index(name)
    for bit,k in enumerate(kids):eq(child(TT(st),i,bit),TT(k))
    delta={key:plus((v[key],F(1)),(vk[0][key],F(-1,2)),(vk[1][key],F(-1,2))) for key in ('H','U','R','Z')}
    equal_expr(plus((delta['H'],F(1)),(delta['U'],F(-1)),(delta['R'],F(-1)),(delta['Z'],F(-1))))
    if name in st['pr']:equal_expr(plus((delta['R'],F(1)),(v['J'],-coeff(st['v'])[1<<i]**2/2)))
    return kids

if not pilot:
  for d,nmax in ((5,2),(7,1),(9,0)):
    for n in range(nmax+1):
      for vv in itertools.product((-1,1),repeat=1<<n):
        for k in range((d-1)//2):
          st=make(vv,d,k);i0=I(st['h']);v=verify(st,i0)
          shared=I(TT(st))-v['p']*I(st['v'])
          leq(subtract(v['H'],v['U']),46*shared)
          for name in st['pr']+st['sh']:local(st,name,i0);counts['root_queries']+=1
          counts['roots']+=1;coeff.cache_clear()

profiles=[(-1,)] if pilot else list(itertools.product((-1,1),repeat=2))
for vv in profiles:
    root=make(vv,5,1);i0=I(root['h']);names=root['pr']+root['sh']
    for assign in itertools.product((-1,0,1),repeat=len(names)):
        st=root
        for name,bit in zip(names,assign):
            if bit!=-1:st=branch(st,name,bit)
        verify(st,i0);counts['partial_states']+=1
        for name in st['pr']+st['sh']:local(st,name,i0);counts['partial_queries']+=1
    coeff.cache_clear()

vv=tuple((-1 if z>>4&1 else 1)*(-1 if ((z&1)*((z>>1)&1)+((z>>2)&1)*((z>>3)&1))%2 else 1) for z in range(32))
policies=[('x4','s1','x0','s2','s3','x1','s4','s0'),('s3','x0','s0','s4','x4','s1','x1','s2')]
ledger=[];histories=[]
for policy in policies[:1 if pilot else 2]:
    root=make(vv,5,1);i0=I(root['h']);quota=96*i0;oldL=F(58);frozenK=F(3,16);rv=values(root);lam=plus(({F(2):quota-oldL},F(1)),(rv['Z'],F(-1)));leq(plus((lam,F(-1))),-20*i0)
    totals={key:{} for key in ('H','U','R','Z')};mass=F(0);spent=F(0);terminalI=F(0)
    def walk(st,depth,reach,path=''):
        global mass,spent,terminalI
        guard();v=verify(st,i0)
        row={'policy':list(policy),'path':path,'reach':str(reach),'profile_mean':str(v['mu']),'event_mass':str(v['p']),'original_Q':str(quota),'supplied_old_L':str(oldL),'already_frozen_K':str(frozenK),'Lambda_interval':[str(x) for x in bounds(lam)],'I':str(I(TT(st))),'terminal':depth==len(policy)}
        for key in ('H','U','R','Z'):row[key+'_interval']=[str(x) for x in bounds(v[key])]
        ledger.append(row)
        if depth==len(policy):
            counts['mixed_leaves']+=1;mass+=reach;terminalI+=reach*I(TT(st))
            for key in totals:totals[key]=plus((totals[key],F(1)),(v[key],reach))
            return
        name=policy[depth];i=(st['pr']+st['sh']).index(name);ij=inf(TT(st),i);row['query']=name;row['actual_query_influence']=str(ij);spent+=reach*ij
        kids=local(st,name,i0);counts['mixed_nodes']+=1
        for bit,kid in enumerate(kids):walk(kid,depth+1,reach/2,path+str(bit))
    walk(root,0,F(1));eq(mass,1);eq(I(TT(root))-terminalI,spent)
    equal_expr(plus((rv['H'],F(1)),(totals['H'],F(-1)),(totals['R'],F(1)),(totals['Z'],F(1)),(rv['U'],F(-1)),(totals['U'],F(1)),(rv['R'],F(-1)),(rv['Z'],F(-1))))
    equal_expr(plus((rv['Z'],F(1)),(lam,F(1)),({F(2):oldL-quota},F(1))))
    histories.append({'policy':list(policy),'Q':str(quota),'old_L':str(oldL),'frozen_K':str(frozenK),'guaranteed_Lambda':str(20*i0),'root_I':str(I(TT(root))),'expected_terminal_I':str(terminalI),'consumed_I':str(spent),'expected_terminal_H_interval':[str(x) for x in bounds(totals['H'])]})
    coeff.cache_clear()

for n in ((3,) if pilot else (3,5,7,9,11)):
    l=n//2;maj=tuple(1 if z.bit_count()<=l else -1 for z in range(1<<n));cc=coeff(maj);alpha=F(math.comb(2*l,l),1<<(2*l))
    for s,c in enumerate(cc):
        k=s.bit_count();expected=F(0) if k%2==0 else (-1)**((k-1)//2)*alpha*F(math.comb(l,(k-1)//2),math.comb(2*l,k-1));eq(c,expected)
    norm=sum(map(abs,cc),F(0));eq(norm>=alpha*2**l,True);counts['majority_dimensions']+=1;coeff.cache_clear()
    d=n+2;m=d//2;a=tuple(1 if z.bit_count()<=m-1 else 0 for z in range(1<<d));aa=child(child(a,0,0),0,0);eq(aa,tuple((v+1)//2 for v in maj));eq(sum(map(abs,coeff(a)),F(0))>=sum(map(abs,coeff(aa)),F(0)),True);counts['event_dimensions']+=1;coeff.cache_clear()
for m in (range(2,3) if pilot else range(2,33)):
    guard();alpha=F(math.comb(2*m-2,m-1),1<<(2*m-2));norm=alpha*sum((F(2*m-1,2*j+1)*math.comb(m-1,j) for j in range(m)),F(0));eq((1+norm)/2>=F(2**m,4*(2*m-1)),True);counts['growth_parameters']+=1
out={'status':'PASS','pilot':pilot,'assertions':checks,'counts':counts,'elapsed_seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(raw).hexdigest(),'histories':histories,'first_unsupported_line':'Two active nonsubcube masks do not have the point/parallel-face Xi/K identity; arbitrary event admission still needs hereditary spectral entropy, not influence proved here.'}
(ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
if not pilot:(ROOT/'out/MIXED_LEDGER.json').write_text(json.dumps(ledger,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ('status','pilot','assertions','counts','elapsed_seconds')}),flush=True)
