import json,sys,time
from pathlib import Path
from fractions import Fraction as F
import cumulative as c
import interval_primitives as m
import baseline as b
import postreset as p
R=Path(__file__).resolve().parents[1];V=m.V;start=time.monotonic();count=0
def ck(x,label):
 global count
 count+=1
 assert x,label
 if time.monotonic()-start>55:raise RuntimeError('55-second frozen watchdog')
def scalar():
 rows=[]
 for k in range(1,17):
  e=F(1,2**k);p0=(1-2*e)**2
  H=-(p0*m.lg(p0) if p0 else V(0))-(2**k-1)*4*e*e*m.lg(4*e*e)
  T=k*m.h(2*e)-H
  if k<=2:ck(T.a==T.b==0,'forced boundary reset KL zero')
  else:ck(T.b<F(5,8),'strict actual reset price')
  if k>=6:
   tail=2*e*(k*k-F(7,2)*k+4)
   ck(T.b<tail<=F(19,32),'analytic decreasing tail certificate')
  if k>=3:
   E=2*m.h(F(1,4))+k*m.h(e/2)-1-2*(k-1)*e
   ck(E.b<F(37,32),'sharper cumulative package envelope')
  rows.append({'k':k,'H':H.out(),'T':T.out()})
 for k in range(6,33):ck(k*k-F(11,2)*k+F(13,2)>0,'reset tail rational monotonicity')
 ck(3**12>2**19,'exact center entropy bound')
 ck(F(123,128)<F(37,32) and F(131,128)<F(37,32),'all-width envelope cases')
 ck(2-F(37,32)-3*F(5,32)-F(11,32)==F(1,32),'final account exact arithmetic')
 return rows
def main():
 N,q,A,rootc=p.root(5);names=['x','a','b','y0','y1','y2','y3','y4','z']
 bc,r,_,_=c.split((N,q,names,F(1)),'b');old=[bc[0]]
 core,r2,_,_=c.split(bc[1],'x');S0=c.stats(old+core)
 original_terminal=sum((m.kl(n['p'],c.norm(qq))*w for n,qq,nn,w in old+core),V(0))
 c.overlap(A,r+r2+original_terminal,'whole original source owned')
 L0=A+m.positive(S0-(4*N['I']-N['H']));c.overlap(L0,A,'neutral b/x prefix')
 previous=S0;U=[];B=[];rows=[]
 for j,label in enumerate(['y0','y1','y2']):
  core,bill=c.reset(core);B.append(bill)
  ck(bill.a>0 and bill.b<=F(5,32),'positive FULL actual reset bill '+str(j))
  core,ledger=c.data(core,label);S=c.stats(old+core);u=m.positive(S-previous);U.append(u)
  ck(u.a>0,'positive physical query debit including AFTER third reset')
  ck(sum(w for n,qq,nn,w in old+core)==1,'every complementary physical terminal retained')
  rows.append({'reset_index':j,'full_reset_bill':bill.out(),'query':label,'new_U_retained':u.out(),'complete_surplus':S.out(),'current_reference_ledger':ledger,'complete_terminal_count':len(old+core)})
  previous=S
 package=L0+sum(U,V(0));remaining=previous-package-sum(B,V(0))-F(11,32)
 ck(package.b<F(37,32),'unchanged actual source and ALL positive query bills')
 ck(previous.a>=2,'complete terminal surplus floor')
 ck(remaining.a>F(1,32),'third reset and later query paid by SAME original owner')
 for n,qq,nn,w in old+core:ck(n['H'].b<=4*n['I'],'physical hereditary terminal certificate')
 return {'m':5,'n':9,'A':A.out(),'L0':L0.out(),'S0':S0.out(),'history':rows,'cumulative_query_debit':sum(U,V(0)).out(),'cumulative_source_query_package':package.out(),'all_three_full_reset_bills':sum(B,V(0)).out(),'omega':'11/32','remaining':remaining.out(),'original_reference_terminal':original_terminal.out()}
if __name__=='__main__':
 rows=scalar();pilot='--pilot' in sys.argv
 physical=None if pilot else main()
 counts={'new':count,'cumulative':c.count,'baseline':b.COUNT,'primitive':m.COUNT,'postreset':p.count}
 out={'status':'PASS','counts':counts,'total_assertions':sum(counts.values()),'runtime_seconds':time.monotonic()-start,'scalar_rows':rows,'physical':physical,'identity_rung':'chain/sector identities proved analytically; interval overlaps are diagnostics only'}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
 print(json.dumps({k:out[k] for k in ['status','total_assertions','runtime_seconds']}))
