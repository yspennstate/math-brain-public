#!/usr/bin/env python3
"""C065 exact adaptive-reveal certificate. Only Fraction/integer sign tests prove signs.

Sympy is used for rational matrix inverses. Floating point appears only in
diagnostic displays after the exact assertions have succeeded.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import sympy as sp

HERE=Path(__file__).resolve().parent
n=4
edges=list(combinations(range(n),2))
bits=[[s>>i&1 for i in range(n)] for s in range(16)]
real_basis=[[(i,i,1)] for i in range(n)] + [[(i,j,1),(j,i,1)] for i,j in edges]
imag_basis=[[(i,j,1),(j,i,-1)] for i,j in edges]  # actual entries are i times these signs
metric=[1]*4+[2]*6

def frac(x):
 return F(int(sp.numer(x)),int(sp.denom(x)))

def matzero(d):return [[F(0) for j in range(d)] for i in range(d)]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def quad(M,a):return sum((a[i]*M[i][j]*a[j] for i in range(len(a)) for j in range(len(a))),F(0))
def add_outer(M,a,scale):
 for i in range(len(a)):
  for j in range(len(a)):M[i][j]+=scale*a[i]*a[j]

def log_interval(v,prec=100):
 """Positive atanh series after exact power-of-two range reduction."""
 assert v>0
 k=0;r=v
 while r<1:r*=2;k-=1
 while r>=2:r/=2;k+=1
 def basic(r):
  t=(r-1)/(r+1);s=F(0);z=t
  # Forty-eight terms: t <= 1/3; tail < 3^-97 up to harmless factors.
  N=48
  for j in range(N):s+=2*z/(2*j+1);z*=t*t
  tail=2*z/((2*N+1)*(1-t*t))
  return s,s+tail
 lo,hi=basic(r);a,b=basic(F(2))
 if k>=0:lo+=k*a;hi+=k*b
 else:lo+=k*b;hi+=k*a
 unit=1<<prec
 lo=F((lo.numerator*unit)//lo.denominator,unit)
 hi=F(-((-hi.numerator*unit)//hi.denominator),unit)
 assert hi-lo<F(1,1<<95)
 return lo,hi

def round_to_grid(v,grid):
 return F((2*v.numerator*grid+v.denominator)//(2*v.denominator),grid)

def exact_psd_coarse(M,logs_error,gamma,diagmetric,label):
 """Round entries to a common dyadic grid and pay a certified row error."""
 d=len(M);grid=1<<24
 C=[[round_to_grid(M[i][j],grid) for j in range(d)] for i in range(d)]
 assert all(C[i][j]==C[j][i] for i in range(d) for j in range(d))
 radius=max(sum(abs(M[i][j]-C[i][j])+logs_error[i][j] for j in range(d)) for i in range(d))
 # A common rational error budget is independently verified, then used in LDL.
 allowance=F(1,100000)
 assert radius<allowance
 S=sp.Matrix([[sp.Rational(C[i][j].numerator,C[i][j].denominator) for j in range(d)] for i in range(d)])
 for i in range(d):S[i,i]-=sp.Rational((gamma*diagmetric[i]+allowance).numerator,(gamma*diagmetric[i]+allowance).denominator)
 # Supply the actual exact LDL factors, in addition to positive pivots.
 target=[[frac(S[i,j]) for j in range(d)] for i in range(d)]
 lower=matzero(d);pivots=[]
 for i in range(d):
  lower[i][i]=F(1)
  pivot=target[i][i]-sum(lower[i][k]**2*pivots[k] for k in range(i))
  assert pivot>0
  pivots.append(pivot)
  for j in range(i+1,d):
   lower[j][i]=(target[j][i]-sum(lower[j][k]*lower[i][k]*pivots[k] for k in range(i)))/pivot
 assert all(target[i][j]==sum(lower[i][k]*pivots[k]*lower[j][k] for k in range(d))
            for i in range(d) for j in range(d))
 row_cap=F(2 if d==10 else 1,10000000)
 pivot_floor=F(17 if d==10 else 3,100)
 assert radius<row_cap and min(pivots)>pivot_floor
 return dict(label=label,dimension=d,gamma=str(gamma),entry_grid=grid,
             row_error_allowance=str(allowance),actual_row_error_upper=str(radius),
             simple_row_error_upper=str(row_cap),minimum_pivot_lower_bound=str(pivot_floor),
             coarse_matrix=[[str(x) for x in row] for row in C],
             exact_unit_lower_factor=[[str(x) for x in row] for row in lower],
             exact_positive_ldl_pivots=[str(x) for x in pivots],
             pivot_displays=[float(x) for x in pivots])

def main():
 B=sp.Matrix([[-1,6,-4,0],[0,0,2,-5],[3,0,-4,-8],[3,0,-6,-3]])
 delta=sp.Rational(1,1000000);d=61
 L=(B*B.T+delta*sp.eye(4))/d
 K=sp.eye(4)-(sp.eye(4)+L).inv()
 assert B.rank()==3
 assert B.T*sp.Matrix([0,1,-1,1])==sp.zeros(4,1)
 # L is strictly positive by its displayed Gram-plus-positive-diagonal form.
 weights=[];p=[];Z=(sp.eye(4)+L).det()
 for s in range(16):
  inds=[i for i in range(4) if s>>i&1]
  w=L.extract(inds,inds).det() if inds else sp.Integer(1)
  assert w>0
  weights.append(frac(w));p.append(frac(w/Z))
 assert sum(p)==1
 derivatives=[];hreal=[];himag=[]
 for s in range(16):
  N=K-sp.diag(*[1-b for b in bits[s]])
  assert frac((-1)**(4-s.bit_count())*N.det())==p[s]
  inv=N.inv();R=[[frac(inv[i,j]) for j in range(4)] for i in range(4)]
  score=[sum(v*R[j][i] for i,j,v in E) for E in real_basis]
  derivatives.append([p[s]*v for v in score])
  Hr=matzero(10);Hi=matzero(6)
  for a,E in enumerate(real_basis):
   for b,Fb in enumerate(real_basis):
    trace=sum(ve*vf*R[l][i]*R[j][k] for i,j,ve in E for k,l,vf in Fb)
    Hr[a][b]=p[s]*(score[a]*score[b]-trace)
  for a,E in enumerate(imag_basis):
   for b,Fb in enumerate(imag_basis):
    trace_sign=sum(ve*vf*R[l][i]*R[j][k] for i,j,ve in E for k,l,vf in Fb)
    Hi[a][b]=p[s]*trace_sign
  hreal.append(Hr);himag.append(Hi)
 assert all(sum(q[i] for q in derivatives)==0 for i in range(10))
 assert all(sum(H[i][j] for H in hreal)==0 for i in range(10) for j in range(10))
 assert all(sum(H[i][j] for H in himag)==0 for i in range(6) for j in range(6))
 # Affineness in each diagonal coordinate makes every diagonal-only self acceleration zero.
 assert all(H[i][i]==0 for H in hreal for i in range(4))
 print('exact atoms and full real/imaginary acceleration coefficients: PASS',flush=True)

 intervals=[log_interval(w) for w in weights]
 ell=[(lo+hi)/2 for lo,hi in intervals]
 err=[(hi-lo)/2 for lo,hi in intervals]
 def frozen(Hs):
  d=len(Hs[0]);M=matzero(d);E=matzero(d)
  for i in range(d):
   for j in range(d):
    M[i][j]=sum(ell[s]*Hs[s][i][j] for s in range(16))
    E[i][j]=sum(err[s]*abs(Hs[s][i][j]) for s in range(16))
  return M,E
 Rlog,Er=frozen(hreal);Ilog,Ei=frozen(himag)
 # Tree 1 and Tree 2 partitions, mask bits correspond to sites 1,...,4.
 tree1=[[0,8],[2,10],[1,9],[3,11],[4,6],[5,7],[12,13],[14,15]]
 tree2=[[0,2],[4,6],[1,3],[5,7],[8,12],[9,13],[10,11],[14,15]]
 def tree_leaves(root,second,third):
  leaves=[]
  for a in range(2):
   for b in range(2):
    observed=[root-1,second[a]-1,third[2*a+b]-1]
    assert len(set(observed))==3
    for c in range(2):
     leaves.append([s for s in range(16) if [bits[s][i] for i in observed]==[a,b,c]])
  return leaves
 assert tree_leaves(3,[1,4],[2,2,1,2])==tree1
 assert tree_leaves(4,[1,2],[3,3,1,3])==tree2
 # Tree 2: root 4; if 0 reveal 1 then 3; if 1 reveal 2,
 # then reveal 1 on outcome 0 and reveal 3 on outcome 1.
 def partition_fisher(leaves):
  assert sorted(s for leaf in leaves for s in leaf)==list(range(16))
  Fm=matzero(10)
  for leaf in leaves:
   pm=sum(p[s] for s in leaf)
   q=[sum(derivatives[s][j] for s in leaf) for j in range(10)]
   add_outer(Fm,q,1/pm)
  return Fm
 F1=partition_fisher(tree1);F2tree=partition_fisher(tree2)
 Fmix=[[(F1[i][j]+F2tree[i][j])/2 for j in range(10)] for i in range(10)]
 # For two-atom leaves, the information loss is an explicit sum of squares.
 full_fisher=matzero(10);residual=matzero(10)
 for s in range(16):add_outer(full_fisher,derivatives[s],1/p[s])
 for leaves in [tree1,tree2]:
  for a,b in leaves:
   score_difference=[derivatives[a][j]/p[a]-derivatives[b][j]/p[b] for j in range(10)]
   add_outer(residual,score_difference,p[a]*p[b]/(2*(p[a]+p[b])))
 assert all(full_fisher[i][j]-Fmix[i][j]==residual[i][j] for i in range(10) for j in range(10))
 # On A = E_44, the unobserved fourth bit in tree 1's leaf {0,8}
 # alone loses more than 2/5 Fisher information after the coin weight.
 leafmass=p[0]+p[8]
 assert derivatives[0][3]==-leafmass and derivatives[8][3]==leafmass
 one_leaf_residual=leafmass**3/(2*p[0]*p[8])
 assert residual[3][3]>=one_leaf_residual>F(2,5)
 print('exact residual sum of squares; strict unrevealed information loss: PASS',flush=True)
 Mreal=[[Fmix[i][j]+Rlog[i][j] for j in range(10)] for i in range(10)]
 gamma=F(1,20)
 proof_real=exact_psd_coarse(Mreal,Er,gamma,metric,'randomized partial-reveal real block')
 proof_imag=exact_psd_coarse(Ilog,Ei,gamma,[2]*6,'complete imaginary acceleration block')
 print('all sixteen Hermitian directions, gap 1/20: PASS',flush=True)

 # Full degree <= 2 score projection, without assuming pairwise frozen logs.
 monomials=[0]+[1<<i for i in range(4)]+[(1<<i)|(1<<j) for i,j in edges]
 G=sp.Matrix([[sp.Rational(sum(p[s] for s in range(16) if s&(a|b)==(a|b))) for b in monomials] for a in monomials])
 deg_witness=[F(x) for x in [4,-641,-480,-577,11,-3,-9,77,60,123]]
 qdir=[dot(q,deg_witness) for q in derivatives]
 m=sp.Matrix([sp.Rational(sum(qdir[s] for s in range(16) if s&a==a)) for a in monomials])
 I2=frac((m.T*G.inv()*m)[0])
 dr=quad(Rlog,deg_witness)
 de=sum(err[s]*abs(quad(hreal[s],deg_witness)) for s in range(16))
 normdeg=sum(metric[i]*deg_witness[i]**2 for i in range(10))
 assert I2+dr+de < -3*normdeg
 print('complete degree-two score certificate fails by more than 3 ||A||F^2: PASS',flush=True)

 # Count-only witness: impose exact zero derivative of the rare full atom,
 # avoiding any ill-conditioned floating-point eigenvector argument.
 count_witness=[F(x,10000) for x in [-7907,3231,3079,2596,-315,-1870,-461,1685,-1796,972]]
 qfull=derivatives[-1]
 count_witness[1]=-sum(qfull[i]*count_witness[i] for i in range(10) if i!=1)/qfull[1]
 assert dot(qfull,count_witness)==0
 Ic=F(0)
 for k in range(5):
  masks=[s for s in range(16) if s.bit_count()==k]
  pk=sum(p[s] for s in masks);qk=sum(dot(derivatives[s],count_witness) for s in masks)
  Ic+=qk*qk/pk
 cr=quad(Rlog,count_witness)
 ce=sum(err[s]*abs(quad(hreal[s],count_witness)) for s in range(16))
 normcount=sum(metric[i]*count_witness[i]**2 for i in range(10))
 assert Ic+cr+ce < -F(1,100)*normcount
 print('complete particle-count certificate fails by more than ||A||F^2/100: PASS',flush=True)

 # All fixed depth-three orders fail: the unrevealed diagonal row has zero
 # Fisher/self-curvature, but a strictly nonzero acceleration mixed entry.
 fixed_obstructions=[]
 for excluded in range(4):
  other=next(j for j in range(4) if j!=excluded)
  lo=Rlog[excluded][other]-Er[excluded][other]
  hi=Rlog[excluded][other]+Er[excluded][other]
  assert hi<0
  fixed_obstructions.append(dict(unrevealed_site=excluded+1,mixed_site=other+1,acceleration_upper=str(hi)))
 print('every fixed-order proper truncation fails: PASS',flush=True)

 # The rare triple is precisely the new cubic observation common to both trees.
 rare=p[14]+p[15]
 assert rare==frac(K.extract([1,2,3],[1,2,3]).det())
 # Confirm genuinely higher-order frozen interactions (C045's pairwise premise fails).
 interaction234=weights[14]*weights[2]*weights[4]*weights[8]/(weights[6]*weights[10]*weights[12])
 assert 0<interaction234<F(1,1000000)

 cert=dict(status='PASS: exact rational certificates',B=[list(map(int,B.row(i))) for i in range(4)],
           delta=str(delta),odds_divisor=d,K=[[str(K[i,j]) for j in range(4)] for i in range(4)],
           atom_probabilities=[str(x) for x in p],odds_weights=[str(x) for x in weights],
           logarithm_intervals=[[str(a),str(b)] for a,b in intervals],
           tree1=tree1,tree2=tree2,mixture_weights=['1/2','1/2'],
           tree1_root=3,tree1_second_sites=[1,4],tree1_third_sites=[2,2,1,2],
           tree2_root=4,tree2_second_sites=[1,2],tree2_third_sites=[3,3,1,3],
           residual_witness='A = E_44',residual_witness_value=str(residual[3][3]),
           residual_one_leaf_lower_bound=str(one_leaf_residual),residual_rational_lower_bound='2/5',
           real_certificate=proof_real,imaginary_certificate=proof_imag,
           degree2_witness=[str(x) for x in deg_witness],
           degree2_upper_ratio=str((I2+dr+de)/normdeg),
           count_witness=[str(x) for x in count_witness],
           count_upper_ratio=str((Ic+cr+ce)/normcount),
           fixed_order_obstructions=fixed_obstructions,
           rare_triple_probability=str(rare),triple_frozen_interaction_ratio=str(interaction234))
 (HERE/'exact_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
 print(json.dumps(dict(degree2_ratio=float((I2+dr+de)/normdeg),
                       count_ratio=float((Ic+cr+ce)/normcount),rare_triple_probability=float(rare),
                       real_pivots=proof_real['pivot_displays'],imaginary_pivots=proof_imag['pivot_displays']),indent=2))

if __name__=='__main__':main()
