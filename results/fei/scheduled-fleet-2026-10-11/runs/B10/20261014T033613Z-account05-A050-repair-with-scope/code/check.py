from pathlib import Path
import json,sys,time
SCRIPT=Path(__file__).resolve()
# Reuse own exact log primitives only; never execute an earlier search.
# Resolve explicitly from the A050 runs directory.
OLD=SCRIPT.parents[2]/'20261014T004109Z-account05-A050-repair-with-scope'/'code'/'check.py'
src=OLD.read_text(encoding='utf-8').split('@lru_cache(None)\ndef stats')[0]
exec(compile(src,str(OLD),'exec'),globals())
LIMIT=60 if PILOT else 180
CASES=0;NODES=0;FIXTURES=[]
def logvec(x):
    out={}
    for n,sgn in [(x.numerator,1),(x.denominator,-1)]:
        for p,k in factor(n).items():out[p]=out.get(p,F(0))+sgn*k
    return {p:v for p,v in out.items() if v}
def kl(p,q):
    out={}
    for s,w in p.items():
        if w:
            ck(q.get(s,F(0))>0)
            out=add(out,scale(logvec(w/q[s]),w))
    return out
def marginal(p,mask):
    out={}
    for s,w in p.items():out[s&mask]=out.get(s&mask,F(0))+w
    return out
def spec(t,coords):
    a=list(t);step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):x,y=a[k],a[k+step];a[k],a[k+step]=x+y,x-y
        step*=2
    p={sum(1<<i for j,i in enumerate(coords) if s>>j&1):F(v*v,len(a)**2) for s,v in enumerate(a) if v}
    ck(sum(p.values())==1)
    inf={i:sum((w for s,w in p.items() if s>>i&1),F(0)) for i in coords}
    for j,i in enumerate(coords):
        flips=sum(t[x]!=t[x|(1<<j)] for x in range(len(t)) if not(x>>j&1))
        ck(inf[i]==F(flips,len(t)//2))
    return p,inf
def restrict(t,j,b):
    return tuple(t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(t)//2))
def productref(p,coords):
    q={0:F(1)}
    for i in coords:
        theta=(1+sum((w for s,w in p.items() if s>>i&1),F(0)))/4
        q={s|(b<<i):v*(theta if b else 1-theta) for s,v in q.items() for b in (0,1)}
    ck(sum(q.values())==1)
    return q
def expand(q,kappa,umask):
    qf={s|z:w*v for s,w in q.items() for z,v in kappa[s&umask].items() if w*v}
    ck(sum(qf.values())==1)
    return qf
def latent(p,kappa,umask):
    return add(*(scale(ent(kappa[s&umask].values()),w) for s,w in p.items()))
def admitted(t,controllers,uc,zc,kappa,policy,name=None):
    global CASES,NODES
    umask=sum(1<<i for i in uc);zmask=sum(1<<i for i in zc)
    def walk(t,coords,depth=0):
        global NODES
        pf,inf=spec(t,coords);remaining=sum(1<<i for i in coords)
        p=marginal(pf,remaining&~zmask)
        ck(pf==expand(p,kappa,umask))
        qc=[i for i in coords if i not in zc];q=productref(p,qc);qf=expand(q,kappa,umask)
        df=kl(pf,qf);dq=kl(p,q);ck(df==dq)
        L=latent(p,kappa,umask)
        ck(ent(pf.values())==add(ent(p.values()),L))
        choices=[i for i in coords if i in controllers and inf[i]]
        if policy=='prefix' and depth>=1:choices=[]
        if not choices:
            return {'Hf':ent(pf.values()),'Hq':ent(p.values()),'Lf':L,'CEf':add(ent(pf.values()),df),
                    'CEq':add(ent(p.values()),dq),'removed':F(0),'leafI':sum(inf.values()),
                    'terminalH':ent(pf.values()),'E':{},'O':{},'rho':{},'leafKL':df,'KL':df,
                    'p':p,'pf':pf,'q':q,'qf':qf,'inf':inf,'coords':coords}
        i=choices[0];j=coords.index(i);children=[walk(restrict(t,j,b),coords[:j]+coords[j+1:],depth+1) for b in (0,1)]
        NODES+=1
        pm=marginal(p,remaining&~zmask&~(1<<i));qm=marginal(q,remaining&~zmask&~(1<<i))
        pfm=marginal(pf,remaining&~(1<<i));qfm=marginal(qf,remaining&~(1<<i))
        ck(pfm==expand(pm,kappa,umask));ck(qfm==expand(qm,kappa,umask))
        eq=add(dq,scale(kl(pm,qm),-1));ef=add(df,scale(kl(pfm,qfm),-1));ck(ef==eq)
        qb=[];bayes=[];bf=[]
        for c in children:
            pred={s:qm[s]*(c['p'].get(s,F(0))/(2*pm[s]) if pm.get(s,F(0)) else F(1,2)) for s in qm}
            outcome=sum(pred.values());ck(outcome>0)
            qb.append(outcome);qchild={s:v/outcome for s,v in pred.items() if v}
            qfc=expand(qchild,kappa,umask)
            # Independently transport the FULL erased reference.
            pred_full={s:qfm[s]*(c['pf'].get(s,F(0))/(2*pfm[s]) if pfm.get(s,F(0)) else F(1,2)) for s in qfm}
            ck(sum(pred_full.values())==outcome)
            ck({s:v/outcome for s,v in pred_full.items() if v}==qfc)
            bd=kl(c['p'],qchild);bdf=kl(c['pf'],qfc);ck(bd==bdf)
            bayes.append(bd);bf.append(bdf)
            # Rational likelihood factorization proves the KL chain exactly.
            for s,w in c['p'].items():
                ck((w/qchild[s])*F(1,2)/outcome==pm[s]/qm[s])
            for s in pm:ck((children[0]['p'].get(s,F(0))+children[1]['p'].get(s,F(0)))/2==pm[s])
        ck(sum(qb)==1)
        O=kl({0:F(1,2),1:F(1,2)},{0:qb[0],1:qb[1]})
        rho=scale(add(*(add(c['KL'],scale(b,-1)) for c,b in zip(children,bayes))),F(1,2))
        rhof=scale(add(*(add(c['KL'],scale(b,-1)) for c,b in zip(children,bf))),F(1,2));ck(rho==rhof)
        av=lambda key:scale(add(*(c[key] for c in children)),F(1,2))
        ck(L==av('Lf'))
        Df=add(ent(pf.values()),scale(av('Hf'),-1));Dq=add(ent(p.values()),scale(av('Hq'),-1));ck(Df==Dq)
        Mfull=add(ent(pf.values()),scale(ent(pfm.values()),-1));Mq=add(ent(p.values()),scale(ent(pm.values()),-1));ck(Mfull==Mq)
        Jfull=add(ent(pfm.values()),scale(av('Hf'),-1));Jq=add(ent(pm.values()),scale(av('Hq'),-1));ck(Jfull==Jq)
        CEf=add(ent(pf.values()),df);CEq=add(ent(p.values()),dq)
        ck(add(CEf,scale(av('CEf'),-1))==add(CEq,scale(av('CEq'),-1)))
        removed=inf[i]+sum((c['removed'] for c in children),F(0))/2
        leafI=sum((c['leafI'] for c in children),F(0))/2
        ck(sum(inf.values())==removed+leafI)
        return {'Hf':ent(pf.values()),'Hq':ent(p.values()),'Lf':L,'CEf':CEf,'CEq':CEq,'removed':removed,
                'leafI':leafI,'terminalH':av('terminalH'),'E':add(ef,av('E')),'O':add(O,av('O')),
                'rho':add(rho,av('rho')),'leafKL':av('leafKL'),'KL':df,'p':p,'pf':pf,'q':q,'qf':qf,'inf':inf,'coords':coords}
    r=walk(t,tuple(range(len(t).bit_length()-1)))
    CASES+=1
    if CASES%50==0:(ROOT/'out'/'CHECKPOINT.json').write_text(json.dumps({'cases':CASES,'seconds':time.perf_counter()-START}),encoding='utf-8')
    if name:
        FIXTURES.append({'name':name,'removed_I':str(r['removed']),'terminal_I':str(r['leafI']),
                         'root_H':serial(r['Hf']),'terminal_H':serial(r['terminalH']),'spectator_entropy_once':serial(r['Lf']),
                         'source_KL':serial(r['KL']),'terminal_KL':serial(r['leafKL']),
                         'signed_reset_sum':serial(r['rho']),'erasure_KL_sum':serial(r['E']),'outcome_KL_sum':serial(r['O']),
                         'exact_full_quotient_cost_match':True})
    return r
for g in ((1,) if PILOT else range(4)):
 for h in ((2,) if PILOT else range(4)):
  for v in range(16):
   if PILOT and CASES>=16:break
   sv=tuple(1-2*(v>>x&1) for x in range(4));pv,_=spec(sv,(5,6))
   kap={u:pv for u in (0,8,16,24)}
   t=[]
   for x in range(128):
    s,a,b=x&1,x>>1&1,x>>2&1
    core=1 if not s else 1-2*(g>>(x>>3&1)&1) if a else 1-2*(h>>(x>>4&1)&1) if b else 1
    t.append(core*sv[x>>5])
   for policy in ('complete','prefix'):
    admitted(tuple(t),range(3),(3,4),(5,6),kap,policy)
if not PILOT:
 for m in range(1,4):
  for n in range(1,6):
   for sp in ('character','ANDsign'):
    k=1 if sp=='character' else 2;coords=tuple(range(m+n,m+n+k))
    vv=(1,-1) if sp=='character' else (1,1,1,-1);pv,_=spec(vv,coords)
    kap={u<<m:pv for u in range(1<<n)};t=[]
    for x in range(1<<(m+n+k)):
     z=(x&((1<<m)-1))==((1<<m)-1);a=((x>>m)&((1<<n)-1))==((1<<n)-1)
     t.append((1-2*(not z and a))*vv[x>>(m+n)])
    admitted(tuple(t),range(m),range(m,m+n),coords,kap,'complete',f'A048-m{m}-n{n}-{sp}' if m==1 and n==5 else None)
 # Conditional spectator that is not independent of retained U-frequency.
 t=tuple((1-2*(x&1))*(1-2*((x>>1)==7)) for x in range(16))
 kap={0:{0:F(3,4),4:F(1,12),8:F(1,12),12:F(1,12)},2:{0:F(1,4),4:F(1,4),8:F(1,4),12:F(1,4)}}
 admitted(t,(0,),(1,),(2,3),kap,'complete','correlated-spectator-point-defect')
 # Row-collinear shared cores; quotient is not asserted Boolean.
 t=[]
 for x in range(32):
  s,a,b=x&1,x>>1&1,x>>2&1;u,z=x>>3&1,x>>4&1
  hv=1-2*(u and z);gv=(1-2*z)*hv
  t.append(hv if not s else gv if a else -hv if b else hv)
 kap={0:{0:F(1,2),16:F(1,2)},8:{0:F(1,2),16:F(1,2)}}
 admitted(tuple(t),(0,1,2),(3,),(4,),kap,'complete','shared-row-collinear-no-Boolean-quotient')
 # Excluded A092 cores have inconsistent conditional spectator laws.
 a,_=spec((1,1,1,1),(0,1));b,_=spec((1,1,1,-1),(0,1));c,_=spec((1,-1,-1,1),(0,1))
 ck(marginal(b,1)[0]==F(1,2));ck(a.get(2,F(0))/a[0]==0)
 ck(b[2]/marginal(b,1)[0]==F(1,2));ck(c[3]/marginal(c,1)[1]==1)
 FIXTURES.append({'name':'A092-excluded-shared-data-cores','fallback_Z_one_given_U_zero':'0','AND_Z_one_given_U_zero':'1/2','parity_Z_one_given_U_one':'1','common_kernel_possible':False});CASES+=1
 # Actual first data exposure violates the martingale spectator correction.
 t=tuple((1-2*(x&1))*(1-2*((x>>1)==7)) for x in range(16))
 p,_=spec(t,(0,1,2,3));pq=marginal(p,3)
 L=add(ent(p.values()),scale(ent(pq.values()),-1))
 childL=[]
 for b in (0,1):
  pt,_=spec(restrict(t,1,b),(0,2,3));qt=marginal(pt,1)
  childL.append(add(ent(pt.values()),scale(ent(qt.values()),-1)))
 correction=add(L,scale(add(*childL),F(-1,2)))
 ck(correction=={2:F(1),3:F(-3,8)});ck(3**3<2**8);nonneg(correction)
 FIXTURES.append({'name':'first-data-query-boundary','root_spectator_entropy':serial(L),'mean_terminal_spectator_entropy':serial(scale(add(*childL),F(1,2))),'missing_correction':serial(correction),'strict_positive_integer_certificate':'3^3<2^8'});CASES+=1
 ck(CASES==546)
out={'status':'PASS','cases':CASES,'nodes':NODES,'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,
     'helper_version':'A050-common-conditional-kernel-v1.1','mode':'pilot' if PILOT else 'main',
     'arithmetic':'Fraction normalized complete references and coherent kernels; integer Walsh and physical edges; integer-log identity vectors',
     'exact_chain_certificate':'pointwise rational likelihood factorization; no floating equality or log-atom independence needed'}
(ROOT/'out'/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
if not PILOT:(ROOT/'out'/'FIXTURES.json').write_text(json.dumps(FIXTURES,indent=2),encoding='utf-8')
print(json.dumps(out))
