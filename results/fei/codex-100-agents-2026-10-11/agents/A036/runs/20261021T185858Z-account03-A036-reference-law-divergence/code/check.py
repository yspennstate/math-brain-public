from pathlib import Path
from fractions import Fraction as F
import exact as E
import json,sys,time
r=Path(__file__).resolve().parents[1];start=time.perf_counter()
k=int(sys.argv[1]);assert k in [1,2,3]
def ck(b):
 E.ck(b);assert time.perf_counter()-start<55
n=k+9
# coordinates x,a,b; six point-defect bits; k parity bits
core=[(-1 if (z&7)==7 else 1)*(-1 if ((z>>3)&7)==7 else 1)*(-1 if (z>>6).bit_count()%2 else 1) for z in range(1<<(k+6))]
tab=[-1 if not (u&1) and u&2 else core[u>>3] if u&1 and u&4 else 1 for u in range(1<<n)]
p,d,H,TC=E.facts(tab);ck(d==[F(1,2),F(1,2),F(1,4)]+[F(1,16)]*6+[F(1,4)]*k);ck(p[0]==F(1,16));ck(sum(d)==F(13,8)+F(k,4))
q,c,HM=E.rootref(p,d);A=E.sub(HM,H);ck(E.overlaps(A,E.kl(p,q)))
margin=E.sub(E.iv(4*sum(d)-1),HM);ck(margin[0]>F(k+3,8))
# exact integer entropy sign certificates and boundary normalizer control
ck(3**6>2**9);ck(15**15>2**58);ck(F(13,15)**5<F(1,2))
# Both data children nonconstant and have unequal absolute means (parity kept
# makes means zero, so compare their non-flat spectra/entropy instead).
l0=E.restrict(core,0,0);l1=E.restrict(core,0,1);ck(len(set(l0))==len(set(l1))==2);ck(sorted(E.law(l0))!=sorted(E.law(l1)))
kids,qs,ob,out,zero,eb=E.step(tab,q,2);rows=[]
for physical in [3,9]:
 # local coordinate removes b at index2, hence original i becomes i-1
 grand,rs,oz,oznorm,zz,ez=E.step(kids[1],qs[1],physical-1)
 leaves=[kids[0],*grand];refs=[qs[0],*rs];weights=[F(1,2),F(1,4),F(1,4)]
 fs=[E.facts(t) for t in leaves]
 Hf=E.total(E.scale(w,f[2]) for w,f in zip(weights,fs));If=sum(w*sum(f[1]) for w,f in zip(weights,fs))
 Kf=E.total(E.scale(w,E.kl(f[0],qq)) for w,f,qq in zip(weights,fs,refs))
 O=E.add(ob,E.scale(F(1,2),oz));Er=E.add(eb,E.scale(F(1,2),ez));ledger=E.add(Er,E.add(O,Kf));ck(E.overlaps(A,ledger))
 D=E.sub(H,Hf);R=sum(d)-If;S=E.sub(E.iv(4*If),Hf)
 signed=E.add(E.add(A,D),E.iv(1-4*R));ck(E.overlaps(E.sub(S,signed),margin))
 ck(S[0]>=2);ck(E.sub(S,signed)[0]>F(k+3,8))
 # exact Boolean coherent kernel conditions at both queried nodes
 for tt,ii in [(tab,2),(kids[1],physical-1)]:
  pp=E.law(tt);ps=[E.law(E.restrict(tt,ii,b)) for b in [0,1]]
  fused=[pp[u]+pp[u|(1<<ii)] for u in range(len(pp)) if not u>>ii&1]
  for a,b,v in zip(ps[0],ps[1],fused):
   ck(a+b==2*v)
   if v:ck(a/(2*v)+b/(2*v)==1)
 rows.append({'second_query_original_coordinate':physical,'source_zero_rows':[zero,zz],'outcome_normalizers_b':[E.enc(a) for a in out],'outcome_normalizers_second':[E.enc(a) for a in oznorm],'full_terminal_KL':E.enc(Kf),'source_erasure_KL':E.enc(Er),'source_outcome_KL':E.enc(O),'full_terminal_H':E.enc(Hf),'full_terminal_I':str(If),'terminal_S':E.enc(S),'signed_required_withdrawal_before_positive_part_including_debit_one':E.enc(signed),'source_recovery_margin':E.enc(margin)})
result={'status':'PASS','k':k,'physical_dimension':n,'assertions':E.checks,'runtime_seconds':time.perf_counter()-start,'canonical_c':E.enc(c),'canonical_source_KL':E.enc(A),'canonical_CE':E.enc(HM),'incoming_debit':'1','recovery_margin':E.enc(margin),'policies':rows,'rung':'analytic proof with exact interval checks; not Lean checked'}
(r/'out'/('CHECK_k%d.json'%k)).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({a:result[a] for a in ['status','k','assertions','runtime_seconds','recovery_margin']}))
