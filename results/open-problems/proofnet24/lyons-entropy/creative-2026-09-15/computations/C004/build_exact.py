import itertools as it, json, math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
OUT=Path(__file__).resolve().parent
E=tuple(range(6));levels=[list(it.combinations(E,k)) for k in (2,3,4)];sets=sum(levels,[]);ix={s:k for k,s in enumerate(sets)}
AB=[(A,B) for A in levels[0] for B in it.combinations([i for i in E if i not in A],2)]
D=[[0]*90 for _ in range(50)]
for k,(A,B) in enumerate(AB):
 J=tuple(i for i in E if i not in A+B);T=tuple(i for i in E if i not in B)
 for X,sig in [(A,1),(T,1)]+[(tuple(sorted(A+(j,))),-1) for j in J]:D[ix[X]][k]=sig
beta={(2,0,0):1788,(1,1,0):-702,(1,0,1):378,(0,2,0):588,(0,1,1):-222,(0,0,2):228}
gamma={(2,1,0):-1222,(2,0,1):838,(1,2,0):838,(1,1,1):-357,(1,0,2):338,(0,2,1):338,(0,1,2):-122}
R=[]
for A,B in AB:
 J=tuple(i for i in E if i not in A+B);row=[]
 for X in sets:
  cnt=tuple(len(set(X)&set(G)) for G in (A,J,B))
  if len(X)==2:v=beta[cnt]
  elif len(X)==3:v=gamma[cnt]
  else:v=beta[(2-cnt[2],2-cnt[1],2-cnt[0])]
  row.append(v)
 R.append(row)
for i,X in enumerate(sets):
 for j,Y in enumerate(sets):
  prod=sum(D[i][k]*R[k][j] for k in range(90))
  pinum=42+70*(len(X)-3)*(len(Y)-3)+150*len(set(X)&set(Y))-25*len(X)*len(Y)
  assert prod==6*(2100*(i==j)-pinum),(i,j,prod,pinum)
assert set(sum(abs(v) for v in r) for r in R)=={25872}
# Orbit weights, invariant under cyclic/reflection coordinate maps and exchanging A,B.
seeds=[((0,1),(2,3),1),((0,1),(2,4),1),((0,1),(3,4),1),((0,1),(2,5),1),((0,2),(3,5),7),((0,2),(1,3),1),((0,2),(1,4),7),((0,3),(1,4),4)]
weightmap={};orbitrecord=[]
for A,B,w in seeds:
 orb=set()
 for sig in [-1,1]:
  for shift in E:
   a=tuple(sorted((sig*i+shift)%6 for i in A));b=tuple(sorted((sig*i+shift)%6 for i in B))
   orb.add((a,b));orb.add((b,a))
 for ab in orb:
  assert ab not in weightmap
  weightmap[ab]=w
 orbitrecord.append({'A':A,'B':B,'size':len(orb),'numerator':w})
assert len(weightmap)==90
xf=[weightmap[ab] for ab in AB]
def pair_num(A):
 d=abs(A[0]-A[1]);d=min(d,6-d)
 return {1:6,2:18,3:24}[d]
def triple_num(M):
 gaps=sorted([(M[1]-M[0]),(M[2]-M[1]),6+M[0]-M[2]])
 return {(1,1,4):15,(1,2,3):24,(2,2,2):27}[tuple(gaps)]
bf=[pair_num(A) for A in levels[0]]+[-triple_num(M) for M in levels[1]]+[pair_num(tuple(i for i in E if i not in T)) for T in levels[2]]
assert [sum(a*b for a,b in zip(row,xf)) for row in D]==bf
assert sum(xf)==216 and min(xf)==1
# Six-entry triangular exchange flows.
flows=[];flabel=[];abix={ab:k for k,ab in enumerate(AB)}
for h in E:
 for e in E:
  if h==e:continue
  for tri in it.combinations([i for i in E if i not in (h,e)],3):
   f=[0]*90
   for k in range(3):
    a,b=tri[k],tri[(k+1)%3]
    f[abix[(tuple(sorted((h,a))),tuple(sorted((e,b))))]]+=1
    f[abix[(tuple(sorted((h,b))),tuple(sorted((e,a))))]]-=1
   assert all(sum(a*b for a,b in zip(row,f))==0 for row in D)
   flows.append(f);flabel.append((h,e)+tri)
# Rational row elimination certifies independent rows and columns.
FM=[[F(flow[i]) for flow in flows] for i in range(90)];rperm=list(range(90));pcols=[];rk=0
for j in range(120):
 pivot=next((i for i in range(rk,90) if FM[i][j]),None)
 if pivot is None:continue
 FM[rk],FM[pivot]=FM[pivot],FM[rk];rperm[rk],rperm[pivot]=rperm[pivot],rperm[rk]
 v=FM[rk][j];FM[rk]=[x/v for x in FM[rk]]
 for i in range(rk+1,90):
  fac=FM[i][j]
  if fac:FM[i]=[a-fac*b for a,b in zip(FM[i],FM[rk])]
 pcols.append(j);rk+=1
assert rk==47
prows=rperm[:47]
def det(M):
 M=[list(map(F,row)) for row in M];ans=F(1);n=len(M)
 for j in range(n):
  p=next((i for i in range(j,n) if M[i][j]),None)
  if p is None:return F(0)
  if p!=j:M[p],M[j]=M[j],M[p];ans=-ans
  v=M[j][j];ans*=v
  for i in range(j+1,n):
   fac=M[i][j]/v
   for k in range(j+1,n):M[i][k]-=fac*M[j][k]
 return ans
minor=det([[flows[j][i] for j in pcols] for i in prows]);assert minor == -1
knumer=[12600*xf[i]-sum(R[i][j]*bf[j] for j in range(50)) for i in range(90)]
aug=[[F(flows[j][i]) for j in pcols]+[F(knumer[i])] for i in prows]
for j in range(47):
 pp=next(i for i in range(j,47) if aug[i][j]);aug[j],aug[pp]=aug[pp],aug[j]
 vv=aug[j][j];aug[j]=[a/vv for a in aug[j]]
 for i in range(47):
  if i!=j:
   aa=aug[i][j]
   if aa:aug[i]=[a-aa*b for a,b in zip(aug[i],aug[j])]
thetanum=[r[-1] for r in aug]
assert all(t.denominator==1 for t in thetanum)
thetanum=[int(t) for t in thetanum]
assert all(sum(flows[j][i]*v for j,v in zip(pcols,thetanum))==knumer[i] for i in range(90))
common=math.gcd(2721600,*thetanum)
thetaden=2721600//common;thetanum=[a//common for a in thetanum]
# Three orbit-summed local flows give the entire Fourier correction.
sym_labels=[(0,1,2,3,4),(0,1,2,3,5),(0,2,1,3,5)]
symflows=[]
for lab in sym_labels:
 f=flows[flabel.index(lab)];sy=[0]*90
 for sign in (-1,1):
  for sh in E:
   for swap in (False,True):
    for (A,B),v in zip(AB,f):
     aa=tuple(sorted((sign*i+sh)%6 for i in A));bb=tuple(sorted((sign*i+sh)%6 for i in B))
     if swap:aa,bb=bb,aa
     sy[abix[(aa,bb)]]+=v
 symflows.append(sy)
assert all(knumer[i]==1575*(-5*symflows[0][i]+5*symflows[1][i]+symflows[2][i]) for i in range(90))
# Dense real exact flag and LP-discovered weights, now checked without tolerances.
B=[[-5,-80,-50,-20,10,40],[-80,43,-44,-26,-8,10],[-50,-44,67,-32,-26,-20],[-20,-26,-32,67,-44,-50],[10,-8,-26,-44,43,-80],[40,10,-20,-50,-80,-5]]
assert all(sum(B[k][i]*B[k][j] for k in E)==11025*(i==j) for i in E for j in E)
def prob(A,cols):return det([[B[i][j] for j in cols] for i in A])**2/F(105)**(2*len(A))
pr=[prob(A,(0,1)) for A in levels[0]]+[prob(M,(0,1,2))+prob(M,(0,1,3)) for M in levels[1]]+[prob(T,(0,1,2,3)) for T in levels[2]]
br=pr[:15]+[-x for x in pr[15:35]]+pr[35:]
# npz came from numeric search; round only proposes integers, exact assertions certify.
z=np.load(OUT/'real_seed.npz');xreal_orig=[int(round(w*33075)) for w in z['x']]
# Source npz indexes (A,added-pair), while this verifier indexes (A,B=complement-top).
oldorder=[(A,tuple(i for i in E if i not in A+J)) for A in levels[0] for J in it.combinations([i for i in E if i not in A],2)]
xo=dict(zip(oldorder,xreal_orig));xr=[xo[ab] for ab in AB]
assert all(F(sum(a*b for a,b in zip(row,xr)),33075)==t for row,t in zip(D,br))
assert sum(xr)==33075 and min(xr)==2
assert min(pr)>0
record={'ground_set':'0..5','indexing':'AB lexicographic, A and B disjoint 2-subsets; bottom A, top E minus B','AB':AB,'fourier':{'denominator':216,'contrast_numerators':bf,'weight_numerators':xf,'orbits':orbitrecord},'right_inverse':{'denominator':12600,'beta':{','.join(map(str,k)):v for k,v in beta.items()},'gamma':{','.join(map(str,k)):v for k,v in gamma.items()},'row_l1_norm':'154/75','matrix_identity':'D R = I - Pi_modular'},'flows':{'count':120,'rank':rk,'pivot_row_indices':prows,'pivot_column_indices':pcols,'pivot_column_labels':[flabel[j] for j in pcols],'pivot_minor_det':str(minor),'fourier_correction_denominator':thetaden,'fourier_correction_numerators':thetanum,'symmetrized_correction':{'labels':sym_labels,'multipliers':[-5,5,1],'denominator':1728}},'real':{'frame_denominator':105,'frame_numerators':B,'probability_denominator':11025,'probability_numerators':[int(x*11025) for x in pr],'coupling_denominator':33075,'weight_numerators':xr}}
(OUT/'exact_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'all_exact_checks_passed':True,'fourier_min_weight':'1/216','right_inverse_row_norm':'154/75','fourier_law_radius':'25/11088','exchange_flows':120,'exchange_flow_rank':rk,'pivot_minor_det':str(minor),'real_min_weight':'2/33075','real_law_radius':'1/33957','certificate':'exact_certificate.json'},indent=2))
