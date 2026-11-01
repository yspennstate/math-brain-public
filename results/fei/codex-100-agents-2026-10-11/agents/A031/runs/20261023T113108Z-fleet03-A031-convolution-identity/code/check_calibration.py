from pathlib import Path
from fractions import Fraction as F
import argparse,json,time
R=Path(__file__).resolve().parents[1];N=0;cache={};D=1<<256
def ck(b):
 global N
 assert b
 N+=1
def lg(x):
 if x in cache:return cache[x]
 k=x.numerator.bit_length()-x.denominator.bit_length();z=x/F(2)**k
 if z<1:z*=2;k-=1
 def ln(z):
  t=(z-1)/(z+1);v=t;s=F(0)
  for j in range(28):s+=v/(2*j+1);v*=t*t
  return 2*s,2*s+2*v/(57*(1-t*t))
 a,b=ln(z);c,d=ln(F(2));cache[x]=(k+a/d,k+b/c);return cache[x]
def logs(terms):
 lo=hi=F(0)
 for w,x in terms:
  if not w:continue
  a,b=lg(x)
  if w<0:a,b=b,a
  a,b=w*a,w*b
  lo+=F(a.numerator*D//a.denominator,D);hi+=F(-((-b.numerator*D)//b.denominator),D)
 return lo,hi
def add(*xs):return tuple(sum(x[j] for x in xs) for j in [0,1])
def sc(x,c):return tuple(c*z for z in (x if c>=0 else x[::-1]))
def sub(x,y):return add(x,sc(y,-1))
def zero(x):ck(x[0]<=0<=x[1])
def save(x):return [str(v) for v in x]
def ce(p,q):
 ck(sum(p)==sum(q)==1)
 return logs([(-v,q[i]) for i,v in enumerate(p) if v])
def KL(p,q):return logs([(v,v/q[i]) for i,v in enumerate(p) if v])
def profile(r,kappa):return [r[z]*kappa[z][j] for z in [0,1] for j in [0,1]]
def pair_ce(p,qs):return sc(add(*(ce(p,q) for q in qs)),F(1,2))
def case(a,k,j):
 pz=[a,1-a];r0=[F(k,8),1-F(k,8)];rp=[F(j,16),1-F(j,16)];rm=[2*r0[z]-rp[z] for z in [0,1]]
 kap=[[F(1,3),F(2,3)],[F(2,5),F(3,5)]];p=profile(pz,kap);q=profile(r0,kap);opts=[profile(r,kap) for r in [rp,rm]]
 ck(all(x>0 for x in rp+rm));ck(all((opts[0][t]+opts[1][t])/2==q[t] for t in range(4)))
 cost=sub(pair_ce(p,opts),ce(p,q));E=logs([(pz[z]/2,r0[z]**2/(rp[z]*rm[z])) for z in [0,1]])
 zero(sub(cost,E))
 if rp==r0:zero(E)
 else:ck(E[0]>0)
 for sign in [-1,1]:
  c=[list(x) for x in opts]
  for z in [0,1]:
   eps=min(opts[u][2*z+t] for u in [0,1] for t in [0,1])/4
   for u in [0,1]:
    c[u][2*z]+=sign*(-1)**u*eps;c[u][2*z+1]-=sign*(-1)**u*eps
  ck(all((c[0][t]+c[1][t])/2==q[t] for t in range(4)))
  for u in [0,1]:
   ck(sum(c[u])==1);ck([sum(c[u][2*z:2*z+2]) for z in [0,1]]==([rp,rm][u]))
  gap=sub(pair_ce(p,c),pair_ce(p,opts));ck(gap[0]>0)
 # Current inherited fine profile need not be the actual one for FREE matching calibration.
 oldkap=[[F(1,4),F(3,4)],[F(3,7),F(4,7)]];old=profile(r0,oldkap);cal=profile(pz,oldkap)
 drop=sub(ce(p,cal),ce(p,old));release=KL(pz,r0);zero(add(drop,release));ck(release[1]>=0)
 return {'a':str(a),'k':k,'j':j,'optimum_conversion':save(E),'matching_calibration_CE_change':save(drop)}
def parity():
 vals=[(-1)**x.bit_count() for x in range(16)];amp={s:F(sum(vals[x]*(-1)**((s&x).bit_count()) for x in range(16)),16) for s in range(16)}
 ck(amp[15]==1);ck(sum(v*v for v in amp.values())==1)
 for U in range(16):ck(sum(amp[S]*amp[S^U] for S in range(16))==int(U==0))
 for u in [0,1]:
  ac={S:amp[S]+(-1)**u*amp[S|8] for S in range(8)};ck(ac[7]==(-1)**u);ck(sum(v*v for v in ac.values())==1)
 ck(sum(amp[S]*amp[S|8] for S in range(8))==0)
 qp={9:F(1,2),15:F(1,2)};bar={S:qp.get(S,F(0))+qp.get(S|8,F(0)) for S in range(8)}
 ck(sum(qp.values())==sum(bar.values())==1);ck(qp.get(0,0)==qp.get(8,0)==0)
 ck(bar[1]==bar[7]==F(1,2));ck(bar[0]==0)
 out=[]
 for m in [1,2,3,4,8,16]:
  eps=F(1,1<<m);p=[F(0),F(1)];q=[F(1,2),F(1,2)];qs=[[eps,1-eps],[1-eps,eps]]
  cost=sub(pair_ce(p,qs),ce(p,q));formula=logs([(F(1,2),F(1,4)/(eps*(1-eps)))]);zero(sub(cost,formula))
  ck(sum(qs[0])==sum(qs[1])==1);ck([(qs[0][z]+qs[1][z])/2 for z in [0,1]]==q)
  if m>1:ck(cost[0]>0);ck(cost[0]>F(m-2,2))
  if m==4:ck(cost[0]>1)
  out.append({'m':m,'minimum_full_conversion':save(cost),'actual_JS':0,'actual_B_query':0,'actual_phase_products_all_zero':True,'query_influence':1,'minimum_expected_terminal_KL':save(pair_ce(p,qs))})
 return {'actual_boolean':'parity4; queried bit3; children +/-parity3','parent_complete_reference':{'9':'1/2','15':'1/2','other_labels':'0'},'child_nonempty_profile_labels':[1,7],'true_and_reference_vacuum_masses':0,'profiles':out,'all16_signed_convolutions_checked':True,'singleton_coefficients':0}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();start=time.monotonic()
 aa=[F(0),F(1,2),F(1)] if args.pilot else [F(0),F(1,4),F(1,2),F(3,4),F(1)];kk=[2,4,6] if args.pilot else range(1,8)
 rows=[]
 for a in aa:
  for k in kk:
   for j in range(1,16):
    if 0<4*k-j<16:
     rows.append(case(a,k,j));assert time.monotonic()-start<(55 if args.pilot else 180)
 ck(len(rows)==(87 if args.pilot else 285));w=parity();out={'cases':rows,'parity':w,'checks':N,'seconds':time.monotonic()-start}
 name='PILOT.json' if args.pilot else 'CHECK.json';(R/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'file':name,'cases':len(rows),'checks':N,'seconds':out['seconds']}))
