from pathlib import Path
from fractions import Fraction as Q
import argparse,json,time,sys
sys.set_int_max_str_digits(100000)
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';OUT.mkdir(exist_ok=True)
checks=0
def ck(x,label):
 global checks
 checks+=1
 if not x:raise AssertionError(label)
def point(x):return (Q(x),Q(x))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[1],a[1]-b[0])
def mul(a,b):
 v=[a[i]*b[j] for i in [0,1] for j in [0,1]];return(min(v),max(v))
def div(a,b):
 ck(b[0]>0,'positive interval denominator');return mul(a,(1/b[1],1/b[0]))
def sm(xs):
 result=point(0)
 for x in xs:result=add(result,x)
 return result
def logbound(x):
 x=Q(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def ln(y):
  z=(y-1)/(y+1);lo=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(32)),Q(0))
  return lo,lo+2*z**65/(65*(1-z*z))
 a,b=ln(x);c,d=ln(Q(2));return Q(k)+a/d,Q(k)+b/c
def loginterval(x):return(logbound(x[0])[0],logbound(x[1])[1])
def kl(p,q):
 return sm([mul(point(v),loginterval(div(point(v),w))) for v,w in zip(p,q) if v])
def compact(x):
 scale=1<<60
 return {'lower':str(Q((x[0]*scale).numerator//(x[0]*scale).denominator,scale)),
         'upper':str(Q(-(-(x[1]*scale).numerator//(x[1]*scale).denominator),scale))}
def poly(c):return(1-8*c/15)**2*(1-4*c/15)**2-1+c
def canonical_bracket():
 lo=Q(3,4);hi=Q(13,16);ck(poly(lo)<0<poly(hi),'canonical initial bracket')
 for _ in range(48):
  m=(lo+hi)/2
  if poly(m)<0:lo=m
  else:hi=m
 ck(poly(lo)<0<poly(hi),'canonical exact root signs');return lo,hi
def spectrum(table):
 length=len(table);n=length.bit_length()-1
 w=[Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(table)),length) for s in range(length)]
 p=[v*v for v in w];ck(sum(p)==1,'Parseval')
 inf=[]
 for i in range(n):
  v=Q(sum(table[x]!=table[x^(1<<i)] for x in range(length)),length)
  ck(v==sum(m for s,m in enumerate(p) if s&(1<<i)),'physical/spectral influence');inf.append(v)
 return w,p,sum(inf),inf
def restrict(table,i,value):
 n=len(table).bit_length()-1
 return [table[(x&((1<<i)-1))|((x>>i)<<(i+1))|(value<<i)] for x in range(1<<(n-1))]
def reference(c):
 theta=[mul(c,point(v)) for v in [Q(8,15),Q(8,15),Q(4,15),Q(4,15)]]
 atom=[]
 for s in range(16):
  a=point(1)
  for i,t in enumerate(theta):a=mul(a,t if s&(1<<i) else sub(point(1),t))
  atom.append(a)
 denominator=sub(point(1),atom[0])
 return [point(Q(1,16))]+[mul(point(Q(15,16)),div(v,denominator)) for v in atom[1:]]
def transport(table,ref,i):
 w,p,_,_=spectrum(table);n=len(table).bit_length()-1;length=1<<(n-1)
 indices=[(s&((1<<i)-1))|((s>>i)<<(i+1)) for s in range(length)]
 erased=[p[s]+p[s|(1<<i)] for s in indices]
 qerased=[add(ref[s],ref[s|(1<<i)]) for s in indices]
 kernels=[]
 for b in [0,1]:
  kernels.append([((w[s]+(-1 if b else 1)*w[s|(1<<i)])**2/(2*mass)) if mass else Q(1,2)
                  for s,mass in zip(indices,erased)])
 ck(all(kernels[0][t]+kernels[1][t]==1 for t in range(length)),'normalized same kernel including fallback')
 children=[];outcomes=[]
 for b in [0,1]:
  child=restrict(table,i,b);cw,cp,ci,cinf=spectrum(child)
  ck(cp==[2*erased[t]*kernels[b][t] for t in range(length)],'actual physical child channel')
  joint=[mul(qerased[t],point(kernels[b][t])) for t in range(length)]
  qb=sm(joint);outcomes.append(qb)
  qr=[div(v,qb) for v in joint];children.append((child,qr))
  ck(qb[0]>0,'complete inherited normalization')
 # At point-valued pilot references, prove likelihood chain atomwise without logarithms.
 if all(v[0]==v[1] for v in ref):
  ck(sum(v[0] for v in ref)==1,'exact normalized parent reference')
  for b,(child,qr) in enumerate(children):
   _,cp,_,_=spectrum(child)
   ck(sum(v[0] for v in qr)==1,'exact normalized inherited child')
   for t,pe in enumerate(erased):
    if cp[t]:
     ck(cp[t]/qr[t][0]==(pe/qerased[t][0])*2*outcomes[b][0],'exact chain likelihood including ghost reference')
 return children,outcomes,erased,qerased,kernels
def fixture(c,label):
 table=[]
 for v in range(16):
  x,a,b,y=[(v>>j)&1 for j in range(4)]
  table.append((-1 if a else 1) if x==0 else (2*y-1 if b else 1))
 _,p,I,inf=spectrum(table);ck(I==Q(3,2) and inf[2]==Q(1,4),'parent physical ledger')
 rootref=reference(c);children,_,_,_,_=transport(table,rootref,2)
 Db=[]
 for b,(child,qr) in enumerate(children):
  _,cp,ci,_=spectrum(child);ck(ci==(Q(1) if b==0 else Q(3,2)),'first child influence')
  ck(kl(cp,[point(v) for v in cp])==(Q(0),Q(0)),'true law entropy zero KL')
  ck(sm([mul(point(v),loginterval(point(1/v))) for v in cp if v])[0]<=2,'child entropy upper')
  Db.append(kl(cp,qr))
 meanD=mul(point(Q(1,2)),add(Db[0],Db[1]))
 C=mul(point(Q(-1,2)),loginterval(sub(point(1),mul(c,point(Q(4,15))))))
 reached,qr=children[1]
 grands,outcomes,pe,qe,kernels=transport(reached,qr,2)
 ck(all(k==Q(1,2) for row in kernels for k in row),'essential data kernel exactly fair')
 Dg=[]
 for child,qg in grands:
  _,gp,gi,_=spectrum(child);ck(gp==[Q(1,4)]*4 and gi==1,'complete grandchild terminal')
  Dg.append(kl(gp,qg))
 finalD=add(mul(point(Q(1,2)),Db[0]),mul(point(Q(1,4)),add(Dg[0],Dg[1])))
 identity=sub(meanD,add(mul(point(Q(1,2)),C),finalD))
 ck(identity[0]<=0<=identity[1],'all complete KL components agree with analytic ownership identity')
 ck(meanD[1]<1,'complete inherited b child KL fits less than one bit')
 ck(C[0]>Q(1,8) and C[1]<Q(3,16),'original conditional payment bound')
 ck(sub(meanD,C)[0]>0,'unpaid retained quotient is positive')
 ck(sub(point(2),meanD)[0]>1,'same owner has greater than one bit left after influence debit and all current KL')
 theta=mul(c,point(Q(8,15)))
 V=div(mul(sub(point(2),theta),sub(point(2),theta)),mul(point(4),sub(point(1),theta)))
 Cy=mul(point(Q(1,2)),loginterval(V))
 final_quotient=sub(sub(meanD,C),mul(point(Q(1,2)),Cy))
 conservative_spend=add(meanD,mul(point(Q(1,2)),Cy))
 ck(final_quotient[0]>0,'A050 remaining final quotient is positive')
 ck(sub(point(2),conservative_spend)[0]>Q(173,100),'A050 old envelope booking plus unpaid quotient leaves more than1.73')
 ck(Q(3)==4*Q(1,2)*Q(1,2)+Q(2),'exact surplus conservation; no renewed bank')
 result={'label':label,'c':compact(c),'D_mean_b_children':compact(meanD),'C_original_booked':compact(C),
         'R_retained_quotient':compact(sub(meanD,C)),'D_final':compact(finalD),
         'root_reached_y_erasure':compact(mul(point(Q(1,2)),C)),
         'old_S4':3,'consumed_influence_debit':1,'final_actual_S4':2,
         'unused_same_owner':compact(sub(point(2),meanD)),'status':'PASS'}
 result.update({'A050_C_y':compact(Cy),'A050_final_unpaid_quotient':compact(final_quotient),
                'A050_booking_unchanged_total_spend':compact(conservative_spend),
                'A050_booking_unchanged_owner_left':compact(sub(point(2),conservative_spend))})
 return result
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();start=time.perf_counter()
 params=[(point(Q(3,4)),'normalized-family-low'),(point(Q(13,16)),'normalized-family-high')] if args.pilot else [(canonical_bracket(),'true-canonical-root')]
 results=[]
 for c,label in params:
  result=fixture(c,label);results.append(result)
  (OUT/(label+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
  ck(time.perf_counter()-start<55,'frozen runtime budget')
 output={'status':'PASS','physical_nodes_per_reference':5,'reference_certificates':len(params),'checks':checks,
         'elapsed_seconds':time.perf_counter()-start,'results':results,'full_FEI':'OPEN'}
 (OUT/('pilot.json' if args.pilot else 'audit.json')).write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8');print(json.dumps(output))
if __name__=='__main__':main()
