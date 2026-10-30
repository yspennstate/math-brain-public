from pathlib import Path
from fractions import Fraction as F
from math import comb
import time,json
R=Path(__file__).resolve().parents[1];N=0
def ck(x):
 global N
 N+=1
 if not x:raise AssertionError(N)
def main():
 start=time.perf_counter();rows=[]
 # P(M,L) polynomial coefficients in M; each entry is constant + L*coefficient.
 p=[(34,9),(23,5),(7,1),(1,0)]
 shifted=[tuple(sum(p[j][k]*comb(j,i)*(-1)**(j-i) for j in range(i,4)) for k in range(2)) for i in range(4)]
 difference=[tuple(2*shifted[i][k]-p[i][k] for k in range(2)) for i in range(4)]
 ck(difference==[(0,1),(1,1),(1,1),(1,0)])
 # P is positive at every M>=0,L>=1; exponential beats this cubic.
 ck(all(x>=0 for row in p for x in row));ck(p[0][0]>0)
 for L in range(1,33):
  partial=F(0)
  for m in range(1,65):
   partial+=F((1+m*(m+1))*(L+m),1<<m)
   tail=m**3+(L+7)*m*m+(5*L+23)*m+9*L+34
   ck(partial==9*L+34-F(tail,1<<m));ck(tail>0)
 for b in range(12,41):
  ck(F(9*b+43,1<<(b+1))<=F(151,8192));ck(F(b+3,1<<b)<=F(15,4096))
  for k in range(65):
   c=F(k,8);K=4*c+15
   margin=K*F(4081,4096)-F(11,4)*c-201*F(151,8192)-(c+F(37,8))
   ck(margin==F(241,1024)*c+F(54191,8192));ck(margin>0)
 # Exact all-C0 coefficients; samples above are secondary corroboration.
 ck(4*F(4081,4096)-F(11,4)-1==F(241,1024))
 ck(15*F(4081,4096)-201*F(151,8192)-F(37,8)==F(54191,8192))
 ck(F(24,23)*F(23,16)==F(3,2));ck(F(24,23)*F(15,8)==F(45,23))
 for n in range(2,9):
  g=[-1 if x&1 else 1 for x in range(1<<n)]
  f=[-1 if x.bit_count()%2 else 1 for x in range(1<<n)]
  diff=[x for x in range(1<<n) if f[x]!=g[x]];M=len(diff);ck(M==1<<(n-1))
  direct=sum(1+j*(j+1) for j in range(1,M+1));ck(direct==M+M*(M+1)*(M+2)//3)
  S=F(n*direct,1<<n);ck(S>=F(n,3)*(1<<(2*n-3)))
  influence=lambda h:F(sum(sum(h[x]!=h[x^(1<<j)] for x in range(1<<n)) for j in range(n)),1<<n)
  ck(influence(g)==1);ck(influence(f)==n)
  # Direct Fourier certificate that target entropy is0: one squared coefficient1.
  amps=[sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(f)) for s in range(1<<n)]
  ck(amps[-1]==1<<n);ck(all(v==0 for v in amps[:-1]))
  rows.append({'N':n,'minimum_required_point_flips':M,'I_source':1,'I_target':n,'H_target_bits':0,'positive_majorant':str(S),'majorant_over_target_influence':str(S/n)})
 # Fresh-control union support bound with variable allowed widths; every finite
 # M is handled analytically by D_j>=L+j and the finite geometric identity.
 for L in range(1,33):
  for m in range(1,65):
   ck(sum((F(1,1<<(L+j)) for j in range(1,m+1)),F(0))==F(1,1<<L)*(1-F(1,1<<m)))
 ck(time.perf_counter()-start<55)
 out={'status':'PASS','assertions':N,'seconds':time.perf_counter()-start,'parity_cases':7,'tail_identity_cases':2048,'coefficient_cases':1885,'symbolic_tail_difference':difference,'positive_old_booking_margin_coefficients':['241/1024','54191/8192'],'parity':rows,'N1_excluded':'dictator equals parity at N1, so the obstruction requires N>=2','all_M_rung':'symbolic polynomial telescoping plus positive tail; finite replay is corroboration','full_v4_physical_review':'NOT_PERFORMED','FEI':'OPEN'}
 (R/'out/EXACT_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='parity'}))
if __name__=='__main__':main()
