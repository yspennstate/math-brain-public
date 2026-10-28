import importlib.util,json,sys,time
from pathlib import Path
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('event_exact',R/'code/check_events.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
Q,ck,add,lf=c.Q,c.ck,c.add,c.lf
def eta(x):return c.scale(-x,lf(x)) if x else {}
def sub(a,b):return add((1,a),(-1,b))
def compressed(k,m):
 rho=Q(1,2**k);mu=Q(3,4)**m;beta=(1-mu)/2;p=rho*beta
 H0=add((1,c.const(4)),(-Q(9,8),lf(Q(3))))
 HB=add((1,eta(beta*beta)),(Q(m,4),H0),(-Q(1,4),eta(mu*mu)),(1,c.const((1-mu*mu)/2)))
 H1=add((1,eta((1-p)**2)),(-1,eta(p*p)),(2*rho,HB),(1,c.const(4*k*p)))
 corecost=add((1,H1),(1,c.const(1)),(-p*p,lf((1+p*p)/(p*p))))
 J=rho*Q(3*m,4)+2*k*p
 bank=add((1,c.const(Q(7,4)-p+J/2)),(-Q(1,4),corecost))
 delta=add((1,eta((1-p/2)**2)),(-Q(1,2),eta((1-p)**2)),(Q(1,4),eta(p*p)),(1,c.const(2*p-p*p/2)))
 Hp=add((Q(1,2),H1),(1,delta))
 klparent=add((1,c.const(1)),(-p*p/2,lf((2+p*p)/(p*p))))
 cp=add((1,c.const(1)),(Q(1,2),Hp),(Q(1,2),klparent),(1,c.psi(p/4)),(-1,c.afun(p*p/16,(2+p*p)/32)))
 ca=add((1,c.const(1)),(Q(1,2),corecost),(1,c.psi(p/2)),(-1,c.afun(p*p/4,(1+p*p)/8)))
 c0=add((1,c.const(Q(7,2))),(-1,c.afun(Q(0),Q(1,8))))
 tq=add((1,cp),(-Q(1,2),ca),(-Q(1,2),c0),(-1,c.const(p)))
 r0,ru=(1+p)/2,(1-p)/2
 cu=add((1,c.const(3)),(-Q(1,2),lf(ru)),(-1,c.afun(Q(0),r0/4)))
 cc=add((1,c.const(1)),(-Q(1,2),lf(r0)),(1,c.psi(Q(1,2))),(-1,c.afun(Q(1,4),r0/4)))
 leaf=add((1-p,cu),(p,cc));bill=c.scale(Q(1,2),sub(ca,leaf))
 remain=add((1,bank),(-1,c.const(Q(1,8))),(-1,c.pos(tq)),(-1,bill))
 ck(c.positive(sub(H0,c.const(2))));ck(c.positive(sub(c.const(3),H0)))
 ck(c.positive(sub(bank,c.const(Q(3,4)))));ck(c.nonneg(bill))
 if k==8:
  root_margin=add((1,c.const(6+J/2-p/2)),(-1,cp))
  ck(c.positive(add((1,root_margin),(-1,bank),(-1,c.const(Q(5,8))))))
  ck(c.positive(add((1,c.const(4*(1-p+J/2))),(-1,corecost))))
 return {'p':p,'H1':H1,'Hp':Hp,'J':J,'corecost':corecost,'bank':bank,'cp':cp,'bill':bill,'remaining':remain}
def literal(k,m,z):
 n=k+3*m;mask=(1<<k)-1
 A=tuple(int((i&mask)==0 and sum(((i>>(k+3*j))&7)==0 for j in range(m))%2==1) for i in range(1<<n))
 tt=c.core(A);p=c.spectrum(tt);r=c.contam(p)
 ck(Q(sum(A),len(A))==z['p']);ck(c.entropy(p)==z['H1']);ck(c.ce(p,r)==z['corecost'])
 ck(sum(v*i.bit_count() for i,v in enumerate(p))==1-z['p']+z['J']/2)
 t0=tuple(1-2*(i%2) for i in range(len(tt)));parent,qr=c.lift(t0,tt,c.contam(c.spectrum(t0)),r)
 ck(c.entropy(c.spectrum(parent))==z['Hp']);ck(c.actcost(parent,qr)==z['cp'])
 # Fully marginalize ALL event coordinates; all physical outcomes retained by total probability.
 for j in range(n):r=c.fold(r,1)
 pA=z['p'];ck(r==((1+pA)/2,(1-pA)/2))
 leaf=add((1-pA,c.actcost((1,-1),r)),(pA,c.actcost((1,1),r)))
 ck(c.scale(Q(1,2),sub(c.actcost(tt,c.contam(p)),leaf))==z['bill'])
def run():
 start=time.perf_counter();pilot='--pilot' in sys.argv;rows=[]
 for k,m in ([(8,1),(2,1)] if pilot else [(8,m) for m in (1,2,4,8)]+[(2,1),(2,2)]):
  z=compressed(k,m)
  if k==2:literal(k,m,z)
  rows.append({'k':k,'m':m,'bank':c.pack(z['bank']),'bill':c.pack(z['bill']),'remaining_interval':c.summary(z['remaining'])})
  assert time.perf_counter()-start<60
 ck(3**9<2**16);ck(3**9>2**8)
 rho=Q(1,256);m=16384;ck(6-rho*m/8==-2)
 out={'status':'PASS','cases':len(rows),'assertions':c.ns['checks'],'seconds':time.perf_counter()-start,'details':rows,'explicit_witness':{'k':8,'m':16384,'event_bits':49160,'bank_gt':'3/4','remaining_lt':'-2','allocation':'no truth table allocated; analytic inequalities and integer certificate'},'full_fei':'OPEN','refuted_scope':'arbitrary-event same-bank all-query payment when every later physical influence credit is left unspent'}
 (R/'out'/('OBSTRUCTION_PILOT.json' if pilot else 'OBSTRUCTION_CHECKS.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k!='details'}))
if __name__=='__main__':run()
