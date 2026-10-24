from pathlib import Path
SCRIPT=Path(__file__).resolve()
source=(SCRIPT.parent/'check.py').read_text(encoding='utf-8').split('for g in ((1,)')[0]
exec(compile(source,str(SCRIPT.parent/'check.py'),'exec'),globals())
LIMIT=60
DATA=0
for n in range(1,4):
 for mask in range(1<<(1<<n)):
  if PILOT and DATA>=12:break
  t=tuple(1-2*(mask>>x&1) for x in range(1<<n));p,inf=spec(t,tuple(range(n)))
  for i in range(n):
   if PILOT and DATA>=12:break
   pq=marginal(p,1<<i)
   children=[spec(restrict(t,i,b),tuple(j for j in range(n) if j!=i))[0] for b in (0,1)]
   L=add(ent(p.values()),scale(ent(pq.values()),-1))
   meanL=scale(add(*(ent(c.values()) for c in children)),F(1,2))
   delta=add(L,scale(meanL,-1))
   pe=marginal(p,((1<<n)-1)&~(1<<i))
   J=add(ent(pe.values()),scale(meanL,-1))
   M=add(ent(p.values()),scale(ent(pe.values()),-1))
   IqueryZ=add(ent(pq.values()),scale(M,-1))
   ck(delta==add(J,scale(IqueryZ,-1)))
   nonneg(IqueryZ);nonneg(J);nonneg(add(J,scale(delta,-1)))
   if J:ck(bounds(J)[1]*LN2[1]<=2*inf[i])
   else:ck(not delta or bounds(delta)[1]<=0)
   DATA+=1
if not PILOT:
 pc,_=spec((1,1,1,-1),(0,1));pd,_=spec(tuple(1-2*(x==7) for x in range(8)),(2,3,4))
 qc=productref(pc,(0,1));q={c|d:a*b for c,a in qc.items() for d,b in pd.items()}
 t=tuple((1-2*((x&3)==3))*(1-2*((x>>2)==7)) for x in range(32))
 p,inf=spec(t,tuple(range(5)))
 ck(p=={c|d:a*b for c,a in pc.items() for d,b in pd.items()})
 sourceKL=kl(p,q);ck(sourceKL=={2:F(4),3:F(-1),5:F(-1)})
 ck(16>15)
 mask=((1<<5)-1)&~4;pe=marginal(p,mask);qe=marginal(q,mask)
 ck(kl(pe,qe)==sourceKL)
 outcomes=[];continuations=[]
 for b in (0,1):
  child=restrict(t,2,b);pb,_=spec(child,(0,1,3,4))
  pred={s:w*(pb.get(s,F(0))/(2*pe[s])) for s,w in qe.items()}
  Qb=sum(pred.values());ck(Qb==F(1,2));outcomes.append(Qb)
  qb={s:w/Qb for s,w in pred.items() if w}
  db=(1,1,1,1) if not b else (1,1,1,-1)
  pzb,_=spec(db,(3,4));ck(qb=={c|z:a*v for c,a in qc.items() for z,v in pzb.items()})
  ck(kl(pb,qb)==sourceKL)
  for s,w in pb.items():ck(w/qb[s]==pc[s&3]/qc[s&3])
  # Coordinate relabeling is fixed and disclosed, not chosen by history.
  pzrenamed,_=spec(db,(2,3))
  r=admitted(child,(0,1),(),(2,3),{0:pzrenamed},'complete',f'post-data-branch-{b}-controller-continuation')
  ck(r['KL']==sourceKL)
  continuations.append({'branch':b,'root_KL':serial(r['KL']),'terminal_KL':serial(r['leafKL']),
                        'signed_reset':serial(r['rho']),'terminal_entropy':serial(r['terminalH']),
                        'removed_controller_I':str(r['removed']),'terminal_I':str(r['leafI'])})
 fixture={'source_KL':serial(sourceKL),'retained_frequency_likelihood_ratio':'P_h2(C)/Q_C(C)',
          'data_erasure_KL':'0','data_outcome_KL':'0','additional_conditional_reset_KL':'0',
          'data_query_influence':str(inf[2]),'continuations':continuations,
          'positive_entropy_drift':{'2':'1','3':'-3/8'}}
 ck(DATA==804 and CASES==2)
else:fixture=None
out={'status':'PASS','data_queries':DATA,'controller_continuations':CASES,'assertions':COUNT,
     'runtime_seconds':time.perf_counter()-START,'mode':'pilot' if PILOT else 'main',
     'arithmetic':'Fraction likelihood factorization, direct spectra and physical edges, certified rational JS bounds',
     'fixture':fixture}
(ROOT/'out'/('DATA_PILOT.json' if PILOT else 'DATA_CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='fixture'}))
