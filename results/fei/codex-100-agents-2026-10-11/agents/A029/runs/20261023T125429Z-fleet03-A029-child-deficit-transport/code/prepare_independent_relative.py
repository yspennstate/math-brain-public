from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
s=(R/'code/independent.py').read_text(encoding='utf-8')
start=s.index('CAP=Q(1,8)');end=s.index('rows=[]',start)
s=s[:start]+'''def const(q):return {2:Q(q)} if q else {}
def eta(args):
 a,g,h,rg,rh=args
 return (1-P(a)[0])*Q(sum(x!=y for x,y in zip(g,h)),len(g))
def aug(args,s):return add(s['T'],const(eta(args)/2))
def target(args,s,factor):
 a,g,h,rg,rh=args;pf=P(mux(a,g,h));na=len(a);out=[];cost={}
 for t,qt in enumerate(s['q']):
  old=s['Q'][t*na:(t+1)*na];pr=pf[t*na:(t+1)*na]
  if not qt:out.extend(old);continue
  k=sum(pr[1:])/qt
  if factor=='legacy':
   ell=Q(15,16)*k+Q(1,32)
   ck(k not in (0,1));ck(Q(1,2)<=ell*(1-k)/(k*(1-ell))<=2)
  else:ell=factor*k/(1+(factor-1)*k)
  non=sum(old[1:]);mass=sum(old);out.append(mass*(1-ell))
  out.extend(mass*ell*v/non if non else Q(0) for v in old[1:])
  cost=add(cost,scale(KL((1-k,k),(1-ell,ell)),qt))
 out=tuple(out);eq(sub(KL(pf,out),s['D']),cost);nn(cost);nn(sub(const(eta(args)/2),cost))
 return out,cost,add(s['S'],const(eta(args)/2),scale(cost,-1))
for k in (Q(0),Q(1,8),Q(1,2),Q(7,8),Q(1)):
 for lam in (Q(1,2),Q(1),Q(2)):
  ell=lam*k/(1+(lam-1)*k);C=KL((1-k,k),(1-ell,ell))
  nn(C);nn(sub(const(k/2),C))
ck(LN2[0]>Q(2,3));ck(LN2[1]<1);ck(9**8>2*8**8)
rows=[]
'''+s[end+len('rows=[]\n'):]
s=s.replace("target(controls[0],cs[0],Q(1,16)),target(controls[1],cs[1],Q(0))", "target(controls[0],cs[0],'legacy'),target(controls[1],cs[1],Q(1))")
s=s.replace("Ac=sub(first['T'],avg(*(x['T'] for x in cs)))", "Ac=sub(aug(data[1],first),avg(*(aug(controls[k],cs[k]) for k in (0,1))))")
s=s.replace('(Q(1,64),Q(1,16))[k]','(Q(2),Q(1,2))[k]')
s=s.replace("Ad=sub(cs[0]['T'],avg(*(x['T'] for x in ns)))", "Ad=sub(aug(controls[0],cs[0]),avg(*(aug(nextargs[k],ns[k]) for k in (0,1))))")
s=s.replace("add(first['H'],first['T'],const(CAP))", "add(first['H'],aug(data[1],first))")
s=s.replace('const(CAP/2)','const(eta(data[1])/4)').replace('3*m-Q(497,256)','3*m-Q(263,128)')
start=s.index('# Actual Boolean dummy-control witness')
s=s[:start]+'''# Actual relative-odds guard outside A028@9 no-liability Markov image.
a=tuple(1 if y%2==0 else -1 for y in range(32));g=(1,-1,1,-1);h=(1,1,-1,-1)
args=(a,g,h,P(g),P(h));ra=P(a);s=canonical(*args,ra)
eq(s['T'],{});eq(s['S'],{});ck(eta(args)==Q(1,2))
q,C,S=target(args,s,Q(2));eq(C,scale(lg(Q(9,8)),Q(1,2)));ck(interval(C)[0]>0)
nn(sub(scale(C,4),const(Q(1,4))))
inh,rho,E,O=channel(mux(*args[:3]),q,1);rra,_,_,_=channel(a,ra,1)
for k in (0,1):
 ar=(child(a,1,k),g,h,P(g),P(h));ss=canonical(*ar,rra[k]);tar=target(ar,ss,Q(2));ck(inh[k]==tar[0]);eq(tar[1],C)
eq(add(E,O),{})
# All-n obstruction is proved symbolically; these are exact compressed witnesses.
rare=[]
for n in (4,8,12,16,20):
 delta=Q(1,1<<n);q0=1-2*delta+2*delta*delta;k0=delta*delta/q0
 ell=Q(15,16)*k0+Q(1,32);C=scale(KL((1-k0,k0),(1-ell,ell)),q0)
 ck(q0>=Q(7,8) and k0<=Q(1,224));nn(sub(C,const(Q(1,1024))))
 I=(n+1)*delta;atom=(1-delta)**2;small=delta**2;mult=(1<<(n+1))-1
 ck(atom+mult*small==1)
 entropy=add(scale(lg(atom),-atom),scale(lg(small),-mult*small));nn(sub(const(4*I),entropy))
 if n>=12:nn(sub(C,const(4*I)))
 rare.append(dict(n=n,influence=str(I),q0=str(q0),k0=str(k0),cost=enc(C),entropy=enc(entropy),cost_exceeds_4I=n>=12))
for n in (1,2,3,4):
 aa=(1,-1);gg=(1,)*(1<<n);hh=(-1,)+(1,)*((1<<n)-1);f=mux(aa,gg,hh);pf=P(f)
 delta=Q(1,1<<n);ck(pf[0]==(1-delta)**2);ck(all(v==delta**2 for v in pf[1:]))
 measured=sum(Q(sum(v!=f[x^(1<<i)] for x,v in enumerate(f)),len(f)) for i in range(n+1))
 ck(measured==(n+1)*delta)
ck(Q(27783,16777216)>Q(1,1024))
out=dict(status='PASS',cases=3,dummy_control_witness=1,scalar_cases=15,compressed_rare_cases=5,truth_table_rare_cases=4,assertions=checks,seconds=round(time.monotonic()-START,6),rows=rows,rare=rare,representation='direct characters and separate KL/pair-channel algebra; no main/helper imports',clipping_certificate='9^8 > 2*8^8')
(RUN/'out/relative_independent.json').write_text(json.dumps(out,indent=2)+'\\n',encoding='utf-8',newline='\\n');print(json.dumps({k:v for k,v in out.items() if k not in ('rows','rare')}))
'''
(R/'code/relative_independent.py').write_text(s,encoding='utf-8',newline='\n')
spec=dict(helper_version='relative_independent.py',domain='3 literal m1..3 NEXT DATA prefixes; 15 scalar odds cases; dummy-control guard; compressed rare n4,8,12,16,20 and full truth rare n1..4',arithmetic='Fractions, direct character sums, exact prime-log identities with rational atanh intervals',symmetry='none',memory_mb=180,max_runtime_seconds=55,parallel_jobs=1,automatic_domain_increase=False,sha256=hashlib.sha256(s.encode()).hexdigest())
(R/'out/VERIFY_RELATIVE_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8',newline='\n')
print('RELATIVE_INDEPENDENT_PREPARED')
