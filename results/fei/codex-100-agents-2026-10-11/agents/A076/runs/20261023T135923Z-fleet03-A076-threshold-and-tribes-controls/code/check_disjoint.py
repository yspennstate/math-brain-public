from pathlib import Path
import json,sys,itertools,hashlib,time
ROOT=Path(__file__).resolve().parents[1]
raw=(ROOT/'code/arithmetic.py').read_bytes();assert hashlib.sha256(raw).hexdigest()=='af2c8fdd2ff2063cc60d12fd5256f6bcaec59c1a27213c39eff444a07c0be865'
exec(compile(raw.decode('utf-8'),str(ROOT/'code/arithmetic.py'),'exec'))
pilot='--pilot' in sys.argv;limit=55 if pilot else 600
counts={'roots':0,'root_queries':0,'mixed_nodes':0,'mixed_leaves':0,'mask_cofactors':0}
def guard():
    if time.perf_counter()-start>limit:raise RuntimeError('Frozen runtime limit')
def mean(t):return F(sum(t),len(t))
def make(h,label,v,w):return {'h':tuple(h),'label':tuple(label),'v':tuple(v),'w':tuple(w),'pr':tuple('x'+str(i) for i in range(len(v).bit_length()-1)),'sh':tuple('s'+str(i) for i in range(len(h).bit_length()-1))}
def branch(st,name,bit):
    out=dict(st)
    if name in st['pr']:
        i=st['pr'].index(name);out['v']=child(st['v'],i,bit);out['w']=child(st['w'],i,bit);out['pr']=tuple(x for x in st['pr'] if x!=name)
    else:
        i=st['sh'].index(name);out['h']=child(st['h'],i,bit);out['label']=child(st['label'],i,bit);out['sh']=tuple(x for x in st['sh'] if x!=name)
    return out
def TT(st):return tuple(h if k==0 else st['v'][x] if k==1 else st['w'][x] for h,k in zip(st['h'],st['label']) for x in range(len(st['v'])))
def vals(st):
    guard();p=[F(st['label'].count(i),len(st['h'])) for i in range(3)]
    masks=[tuple(h if k==0 else 0 for h,k in zip(st['h'],st['label'])),tuple(int(k==1) for k in st['label']),tuple(int(k==2) for k in st['label'])]
    js=[H(b) for b in masks];hp=plus(*[(phi(pi),F(1)) for pi in p]);u=plus((H(st['v']),p[1]),(H(st['w']),p[2]));hh=H(TT(st));n=plus((hh,F(1)),(u,F(-1)))
    return {'p':p,'J':js,'Hp':hp,'U':u,'H':hh,'N':n}
def verify(st):
    v=vals(st);p=v['p'];npr=len(st['pr']);cf=coeff(TT(st));cv=coeff(st['v']);cw=coeff(st['w']);marg=[]
    for t in range(len(cv)):
        q=sum((cf[(s<<npr)|t]**2 for s in range(len(st['h']))),F(0));eq(q,p[0]*int(t==0)+p[1]*cv[t]**2+p[2]*cw[t]**2);marg.append(q)
    privateH=plus(*[(phi(q),F(1)) for q in marg]);leq(plus((v['U'],F(1)),(privateH,F(-1))),0);leq(plus((v['N'],F(-1))),0)
    bound=plus((v['Hp'],F(1)),*[(j,F(3)) for j in v['J']]);leq(plus((v['N'],F(1)),(bound,F(-1))),1)
    for i in range(npr):eq(inf(TT(st),i),p[1]*inf(st['v'],i)+p[2]*inf(st['w'],i))
    return v
def local(st,name):
    v=vals(st);kids=[branch(st,name,b) for b in (0,1)];vk=[vals(k) for k in kids];i=(st['pr']+st['sh']).index(name)
    for bit,k in enumerate(kids):eq(child(TT(st),i,bit),TT(k))
    expr={}
    for key,sign in [('H',1),('U',-1),('N',-1)]:expr=plus((expr,F(1)),(v[key],F(sign)),(vk[0][key],F(-sign,2)),(vk[1][key],F(-sign,2)))
    equal_expr(expr);return kids
profiles=list(itertools.product((-1,1),repeat=2))
parts=list(itertools.product((0,1,2),repeat=4))
for labels in parts[:9 if pilot else 81]:
  for h in [(1,1,1,1)] if pilot else [(1,1,1,1),(1,-1,-1,1)]:
    for v in profiles:
      for w in profiles:
        st=make(h,labels,v,w);verify(st)
        for name in st['pr']+st['sh']:local(st,name);counts['root_queries']+=1
        counts['roots']+=1;coeff.cache_clear()

d=7;m=3;h=tuple(1 if s.bit_count()<=m else -1 for s in range(1<<d));label=tuple(1 if s.bit_count()<=m-2 else 2 if s.bit_count()==m-1 else 0 for s in range(1<<d));i0=I(h);quota=240*i0
vv=tuple((-1 if z>>2&1 else 1)*(-1 if (z&1)*((z>>1)&1) else 1) for z in range(8));ww=tuple(-1 if z==0 else 1 for z in range(8))
root=make(h,label,vv,ww);vr=verify(root);eq(I(TT(root))>=i0,True);leq(plus((vr['H'],F(1)),(vr['U'],F(-1))),177*i0)
oldL=F(58);oldK=F(3,16);oldR=F(1,8);lam=plus(({F(2):quota-oldL},F(1)),(vr['N'],F(-1)));leq(plus((lam,F(-1))),-5*i0)
policies=[('x2','s1','x0','s3','s0','s5','s2'),('s4','x0','s0','x2','s1','s2','s3')];ledger=[];histories=[]
for policy in policies[:1 if pilot else 2]:
    totals={key:{} for key in ('H','U','N')};mass=F(0);spent=F(0);terminalI=F(0)
    def walk(st,depth,reach,path=''):
        global mass,spent,terminalI
        v=verify(st);leq(v['N'],177*i0)
        row={'policy':list(policy),'path':path,'reach':str(reach),'old_L':str(oldL),'old_K_frozen':str(oldK),'old_R_frozen':str(oldR),'Q_new':str(quota),'Q_old':str(96*i0),'explicit_original_enlargement':str(144*i0),'Lambda_interval':[str(a) for a in bounds(lam)],'I':str(I(TT(st))),'terminal':depth==len(policy)}
        for key in ('H','U','N'):row[key+'_interval']=[str(a) for a in bounds(v[key])]
        ledger.append(row)
        if depth==len(policy):
            counts['mixed_leaves']+=1;mass+=reach;terminalI+=reach*I(TT(st))
            for key in totals:totals[key]=plus((totals[key],F(1)),(v[key],reach))
            return
        name=policy[depth];i=(st['pr']+st['sh']).index(name);ij=inf(TT(st),i);spent+=reach*ij;row['query']=name;row['query_influence']=str(ij);kids=local(st,name);counts['mixed_nodes']+=1
        for bit,k in enumerate(kids):walk(k,depth+1,reach/2,path+str(bit))
    walk(root,0,F(1));eq(mass,1);eq(I(TT(root))-terminalI,spent)
    equal_expr(plus((vr['H'],F(1)),(totals['H'],F(-1)),(totals['N'],F(1)),(vr['U'],F(-1)),(totals['U'],F(1)),(vr['N'],F(-1))))
    equal_expr(plus((vr['N'],F(1)),(lam,F(1)),({F(2):oldL-quota},F(1))))
    histories.append({'policy':list(policy),'root_I':str(I(TT(root))),'expected_terminal_I':str(terminalI),'consumed_I':str(spent),'terminal_H_interval':[str(a) for a in bounds(totals['H'])],'guaranteed_Lambda':str(5*i0)})
    coeff.cache_clear()
for assign in ([(-1,)*7] if pilot else itertools.product((-1,0,1),repeat=7)):
    st=root
    for name,bit in zip(root['sh'],assign):
        if bit!=-1:st=branch(st,name,bit)
    v=vals(st);leq(v['J'][0],36*i0+6);leq(v['J'][1],F(9,4)*i0+F(3,2));leq(v['J'][2],9*i0+3);leq(v['N'],177*i0);counts['mask_cofactors']+=1
    coeff.cache_clear()
out={'status':'PASS','pilot':pilot,'assertions':checks,'counts':counts,'elapsed_seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(raw).hexdigest(),'histories':histories,'first_unsupported_line':'General same-original-influence admission of H(p)+r sum mask entropy, or sharper mask/profile-count interference control, remains unpaid.'}
(ROOT/'out'/('pilot_disjoint.json' if pilot else 'validation_disjoint.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
if not pilot:(ROOT/'out/DISJOINT_LEDGER.json').write_text(json.dumps(ledger,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ('status','pilot','assertions','counts','elapsed_seconds')}),flush=True)
