def check_query(t,i,zmask,q,fallback,name=None):
 global CASES
 n=len(t).bit_length()-1;coords=tuple(range(n));p,inf=spec(t,coords)
 rem=((1<<n)-1)&~(1<<i);tm=rem&~zmask
 pe=marginal(p,rem);qe=marginal(q,rem);ck(sum(q.values())==1)
 child=[spec(restrict(t,i,b),tuple(j for j in coords if j!=i)) for b in (0,1)]
 for s in qe:ck(sum(c[0].get(s,F(0)) for c in child)/2==pe.get(s,F(0)))
 C={};B={};Vcap={};Acap={};rows=[];matched=True
 Pjoint={};Qjoint={}
 for b in (0,1):
  for s,w in qe.items():
   k=child[b][0].get(s,F(0))/(2*pe[s]) if pe.get(s,F(0)) else (F(1,2) if fallback==2 else F(b==fallback))
   Pjoint[b,s]=pe.get(s,F(0))*k;Qjoint[b,s]=w*k
 ck(sum(Qjoint.values())==sum(Pjoint.values())==1)
 for b in (0,1):
  for tv in {s&tm for s in qe}:
   atoms=[s for s in qe if s&tm==tv and Qjoint[b,s]>0]
   pp=sum((Pjoint[b,s] for s in atoms),F(0));qq=sum((Qjoint[b,s] for s in atoms),F(0))
   if not pp:continue
   m=pp/qq;r={s:pe.get(s,F(0))/qe[s] for s in atoms}
   ell={s:r[s]/m for s in atoms}
   A=max(ell.values());V=sum((Qjoint[b,s]/qq*ell[s]**2 for s in atoms),F(0))
   ck(A>=V>=1);ck(sum(Qjoint[b,s]/qq*ell[s] for s in atoms)==1)
   pc={s:Pjoint[b,s]/pp for s in atoms if Pjoint[b,s]};qc={s:Qjoint[b,s]/qq for s in atoms}
   for s in atoms:ck(pc.get(s,F(0))==qc[s]*ell[s])
   c=kl(pc,qc);a=logvec(A);v=logvec(V);cap=logvec(min(A,V))
   # Strict signs use rigorous rational intervals; equality uses exact laws.
   if A==1:ck(not c and V==1)
   else:
    matched=False;ck(bounds(c)[0]>=0)
    for upper in (a,v):
     diff=add(upper,scale(c,-1));ck(not diff or bounds(diff)[0]>=0)
   ck((pc==qc)==(A==V==1))
   C=add(C,scale(c,pp));B=add(B,scale(cap,pp));Acap=add(Acap,scale(a,pp));Vcap=add(Vcap,scale(v,pp))
   if name:rows.append({'branch':b,'T':tv,'P_weight':str(pp),'A':str(A),'V':str(V),'ghost_mass':str(sum((qc[s] for s in atoms if not pc.get(s,F(0))),F(0)))})
 # Full source identity, including all reference-only rows under fixed fallback.
 qb={b:sum((Qjoint[b,s] for s in qe),F(0)) for b in (0,1)}
 terminalKL={};terminalH={};terminalI=F(0)
 for b in (0,1):
  pbc,ic=child[b];qbc={s:Qjoint[b,s]/qb[b] for s in qe if Qjoint[b,s]}
  terminalKL=add(terminalKL,scale(kl(pbc,qbc),F(1,2)))
  terminalH=add(terminalH,scale(ent(pbc.values()),F(1,2)));terminalI+=sum(ic.values())/2
 out=kl({0:F(1,2),1:F(1,2)},qb)
 # Multiplicative likelihood certificates avoid reliance on log atom independence.
 for b in (0,1):
  for s,w in child[b][0].items():ck((w/(Qjoint[b,s]/qb[b]))*F(1,2)/qb[b]==pe[s]/qe[s])
 ck(sum(inf.values())==inf[i]+terminalI)
 ck((not B)==matched)
 CASES+=1
 result={'name':name,'query_influence':str(inf[i]),'C_child':serial(C),'envelope':serial(B),'max_envelope':serial(Acap),'moment_envelope':serial(Vcap),'terminal_H':serial(terminalH),'terminal_I':str(terminalI),'source_KL':serial(kl(p,q)),'erasure_KL':serial(add(kl(p,q),scale(kl(pe,qe),-1))),'outcome_KL':serial(out),'terminal_KL':serial(terminalKL),'rows':rows}
 if name:(ROOT/'out'/f'{name}.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 return result

CENSUS=0
for n in (2,3):
 for mask in range(1<<(1<<n)):
  if PILOT and CENSUS>=24:break
  t=tuple(1-2*(mask>>x&1) for x in range(1<<n))
  for i in range(n):
   for theta in (F(1,2),F(1,4)):
    q={s:theta**s.bit_count()*(1-theta)**(n-s.bit_count()) for s in range(1<<n)}
    for fallback in (0,1,2):
     if PILOT and CENSUS>=24:break
     check_query(t,i,((1<<n)-1)&~(1<<i),q,fallback);CENSUS+=1

for rdim in range(2,9):
 mu=F(1,1<<(rdim-1));a=mu*mu
 h=tuple((1 if x==1 else 1-2*(x.bit_count()%2)) for x in range(1<<rdim))
 t=tuple(1 if not(x&1) else h[x>>1] for x in range(1<<(rdim+1)))
 p,inf=spec(t,tuple(range(rdim+1)));pe=marginal(p,((1<<(rdim+1))-1)&~1)
 ck(pe[0]==(1+a)/2);ck(inf[0]==(1-mu)/2)
 for label,alpha in (('regular',F(1,4)),('extreme',1-a*a)):
  qe={s:alpha if s==0 else (1-alpha)*w/(1-pe[0]) for s,w in pe.items()}
  q={s:w*qe[s&~1]/pe[s&~1] for s,w in p.items()}
  res=check_query(t,0,((1<<(rdim+1))-1)&~1,q,2,f'parity_{label}_r{rdim}')
  beta=alpha*a/(1+a-alpha)
  expected=scale(kl({0:a,1:1-a},{0:beta,1:1-beta}),F(1,2))
  ck(res['C_child']==serial(expected))
  V=a*a/beta+(1-a)**2/(1-beta)
  ck(res['moment_envelope']==serial(scale(logvec(V),F(1,2))))
  if label=='regular':
   ck(V==1+4*a*(1+2*a)**2/(3*(1+a)));ck(V<=1+F(12,5)*a)
   ck(LN2[0]>F(3,5));ck(bounds(expected)[1]<2*a);ck(2*a<=2*inf[0])
  else:
   ck(beta==1-a)
   if rdim==6:ck(1023>512 and F(4599,1024)>8*inf[0])

# Direct truth table of actual exposed gate; c-samples normalized explicitly.
t=tuple(1-2*((x>>1)&1) if not(x&1) else 2*((x>>3)&1)-1 if ((x>>2)&1) else 1 for x in range(16))
p,inf=spec(t,tuple(range(4)));ck(ent(p.values())=={2:F(3)});ck(sum(inf.values())==F(3,2));ck(inf[2]==F(1,4))
def poly(c):return (1-F(8,15)*c)**2*(1-F(4,15)*c)**2-(1-c)
lo,hi=F(3,4),F(13,16);ck(poly(lo)<0<poly(hi))
for c in (lo,F(25,32),hi):
 theta=(F(8,15)*c,F(8,15)*c,F(4,15)*c,F(4,15)*c)
 raw={s:__import__('functools').reduce(lambda a,b:a*b,(theta[j] if s>>j&1 else 1-theta[j] for j in range(4)),F(1)) for s in range(16)}
 norm=1-raw[0];q={s:F(1,16) if not s else F(15,16)*w/norm for s,w in raw.items()}
 res=check_query(t,2,8,q,2,f'priority_c_{c.numerator}_{c.denominator}')
 expected=scale(logvec(1/(1-F(4,15)*c)),F(1,2))
 ck(res['C_child']==res['envelope']==serial(expected))
 ck(res['terminal_H']=={str(2):str(F(2))});ck(res['terminal_I']==str(F(5,4)))
for _ in range(48):
 mid=(lo+hi)/2
 if poly(mid)<0:lo=mid
 else:hi=mid
ck(poly(lo)<0<poly(hi));ck(60**8<8*47**8)
(ROOT/'out/CANONICAL_CERTIFICATE.json').write_text(json.dumps({'c_bracket':[str(lo),str(hi)],'polynomial_signs':[str(poly(lo)),str(poly(hi))],'conditional_envelope_exact':'-1/2 log2(1-4c/15)','influence':'1/4','price_constant':'3/4','unused_mean_child_S4':'3','fraction_spent':'<1/16','integer_sign':'60^8 < 8*47^8','full_terminals_retained':True},indent=2),encoding='utf-8')
ck(CASES==(41 if PILOT else 4817))
result={'status':'PASS','census_cases':CENSUS,'target_cases':17,'total_cases':CASES,'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'mode':'pilot' if PILOT else 'main'}
(ROOT/'out'/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
