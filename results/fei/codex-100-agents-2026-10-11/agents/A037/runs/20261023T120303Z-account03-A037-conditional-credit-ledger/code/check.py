from pathlib import Path
from fractions import Fraction as F
import time,json,sys
import exact as E
import validate as V
R=Path(__file__).resolve().parents[1];start=time.perf_counter();C=0
def ck(x,msg=''):
 global C
 C+=1;assert x,(C,msg);assert time.perf_counter()-start<55
def KL(p,q):return V.KL(p,q)
def factor(r):return [-1 if w==0 or (j and w==3) else 1 for w in range(1<<r) for j in [0,1]]
def core(k,r):
 t=[1,-1]
 for _ in range(k):t=V.tensor(t,factor(r))
 return t
def qcore(g,alpha):
 p=E.law(g);ck(p[0]==0 and p[-1]>0);q=[(1-alpha)*x for x in p];q[-1]+=alpha;ck(sum(q)==1);return q
def root(k,r):
 g=core(k,r);t=[(-1)**((z>>1)&1) if not z&1 else (g[z>>3] if z&4 else 1) for z in range(8*len(g))];p=E.law(t);q=[F(0)]*len(p);q[:8]=p[:8];qq=qcore(g,F(1,8))
 for s in range(1,len(qq)):
  for c in [0,1,4,5]:q[8*s+c]=qq[s]/16
 ck(sum(q)==1);return t,q
def fresh(t):
 p=E.law(t);g=t[1::2];qq=qcore(g,F(1,6));q=[F(0)]*len(p);q[:2]=p[:2]
 for s in range(1,len(qq)):q[2*s]=q[2*s+1]=qq[s]/4
 ck(sum(q)==1);ck(all((x==0)==(y==0) for x,y in zip(p,q)));return q
def f(m,alpha=F(1,6)):
 return KL([m,1-m],[alpha+(1-alpha)*m,(1-alpha)*(1-m)])
def run(k,r):
 t,q=root(k,r);p,ii,H,_=E.facts(t);I=sum(ii);A=KL(p,q);M=E.sub(E.iv(4*I),E.add(H,A));d=F(1,1<<r);pg=E.law(core(k,r));Hg=E.entropy(pg)
 ck(pg[-1]==d**(2*k));ck(I==F(3,2)+k*(3*r+1)*d/4);ck(E.overlaps(H,E.add(E.iv(3),E.scale(F(1,4),Hg))));ck(E.overlaps(A,E.scale(F(1,4),f(pg[-1],F(1,8)))))
 bs,bp,bq,bo,be,bout=V.step(t,q,2);release=E.add(be,bout);aa,ap,aq,ao,ae,aout=V.step(bs[1],bq[1],1);release=E.add(release,E.scale(F(1,2),E.add(ae,aout)))
 s1=E.iv(0);later=E.iv(0);kap=E.scale(F(1,2),E.logpoint(F(400,399)));leaves=[(F(1,2),bs[0],bq[0])];transactions=[];generation_reaches=[F(0)]*k
 for a in [0,1]:
  rn=fresh(aa[a]);s1=E.add(s1,E.scale(F(1,4),E.sub(KL(ap[a],rn),KL(ap[a],aq[a]))));coords=[i for i in range(len(t).bit_length()-1) if i not in [1,2]];active=[(F(1,4),aa[a],rn,coords,[])]
  for gen in range(k):
   nxt=[]
   for weight,tab,ref,coords,hist in active:
    generation_reaches[gen]+=weight;idx=coords.index(4+gen*(r+1));kids,ps,old,outs,loss,out=V.step(tab,ref,idx);release=E.add(release,E.scale(weight,E.add(loss,out)));ck(outs==[F(19,40),F(21,40)]);m=E.law(tab[1::2])[-1];local=E.iv(0)
    for y in [0,1]:
     qq=fresh(kids[y]);mm=E.law(kids[y][1::2])[-1];ck(mm==[4*m,16*m][y]);inc=E.sub(KL(ps[y],qq),KL(ps[y],old[y]));local=E.add(local,E.scale(F(1,2),inc));nxt.append((weight/2,kids[y],qq,[c for c in coords if c!=4+gen*(r+1)],hist+[y]))
    formula=E.add(kap,E.scale(F(1,4),E.sub(E.add(f(4*m),f(16*m)),E.scale(2,f(10*m)))));ck(E.overlaps(local,formula));ck(local[0]>kap[1]);later=E.add(later,E.scale(weight,local));transactions.append({'a':a,'history':hist,'generation':gen,'reach':str(weight),'full_mass':str(m),'outcomes':list(map(str,outs)),'sigma':E.enc(local)})
   active=nxt
  leaves.extend((w,tt,qq) for w,tt,qq,_,_ in active)
 ck(generation_reaches==[F(1,2)]*k);ck(s1[0]>0);ck(later[0]>E.scale(F(k,2),kap)[1]);HH=E.iv(0);II=F(0);K=E.iv(0);terms=[]
 for w,tt,qq in leaves:
  pp,iii,hh,_=E.facts(tt);II+=w*sum(iii);HH=E.add(HH,E.scale(w,hh));kk=KL(pp,qq);K=E.add(K,E.scale(w,kk));terms.append({'reach':str(w),'H':E.enc(hh),'I':str(sum(iii)),'KL':E.enc(kk),'reference':list(map(str,qq))})
 ck(sum(w for w,_,_ in leaves)==1);ck(E.overlaps(E.add(A,E.add(s1,later)),E.add(release,K)));S=E.sub(E.iv(4*II),HH);e=E.add(E.sub(H,HH),E.iv(-4*(I-II)));net=E.add(E.add(A,e),E.add(s1,later));J=(max(F(0),net[0]),max(F(0),net[1]));rem=E.sub(E.sub(S,J),E.iv(F(1,4)));ck(E.overlaps(E.sub(S,net),E.sub(M,E.add(s1,later))))
 return {'k':k,'r':r,'bits':len(t).bit_length()-1,'A0':E.enc(A),'M0':E.enc(M),'sigma1':E.enc(s1),'sigma_later':E.enc(later),'kappa':E.enc(kap),'generation_reaches':list(map(str,generation_reaches)),'all_erasure_outcome_KL':E.enc(release),'full_terminal_KL':E.enc(K),'full_S':E.enc(S),'same_owner_after_old_quarter':E.enc(rem),'transactions':transactions,'terminals':terms}
if __name__=='__main__':
 rows=[run(k,r) for k,r in ([(1,3)] if '--pilot' in sys.argv else [(1,3),(1,4),(2,3)])];cert=[];ck(400**300>2*399**300)
 for s in range(12,21):
  k=2**s;r=2*s+8;d=F(1,2**r);over=k*(3*r+1)*d;entropy=16*k*(r+1)*d;terminal=16*k*r*d;deficit=F(k,1200)-F(49,16)
  ck(over<F(1,16));ck(entropy<F(1,1024));ck(terminal<=F(1,2048));ck(deficit>0);cert.append({'s':s,'k':k,'r':r,'actual_Boolean_bits':1+k*(r+1)+3,'source_influence_overhead':str(over),'parent_entropy_upper':str(entropy),'terminal_core_entropy_upper':str(terminal),'unpaid_before_old_quarter_lower':str(deficit)})
 ck(cert[0]['unpaid_before_old_quarter_lower']=='421/1200')
 o={'status':'PASS','raw_cases':len(rows),'symbolic_certificates':len(cert),'own_assertions':C,'transport_assertions':V.checks,'primitive_assertions':E.checks,'seconds':time.perf_counter()-start,'raw_rows':rows,'symbolic_rows':cert};(R/'out'/('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json')).write_text(json.dumps(o,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in o.items() if k not in ['raw_rows','symbolic_rows']}))
