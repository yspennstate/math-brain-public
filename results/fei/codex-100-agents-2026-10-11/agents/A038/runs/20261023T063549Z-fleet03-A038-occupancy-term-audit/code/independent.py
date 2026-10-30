"""Separate 32-term log lane, Bellman bound and retained-booking readback."""
import json,time
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];start=time.monotonic();count=0;GRID=2**100
def check(x,label):
 global count
 count+=1
 assert x,label
 if time.monotonic()-start>55:raise RuntimeError('55 second watchdog')
def floor(x):return F((x*GRID).__floor__(),GRID)
def ceil(x):return F((x*GRID).__ceil__(),GRID)
def ln(q):
 t=(q-1)/(q+1);a=2*sum((t**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
 return a,a+2*t**65/(65*(1-t*t))
L2=ln(F(2))
def lg(q):
 shift=0
 while q<1:q*=2;shift-=1
 while q>=2:q/=2;shift+=1
 a,b=ln(q);return floor(shift+a/L2[1]),ceil(shift+b/L2[0])
def read_interval(x):return tuple(map(F,x))
def overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]
C=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
entropies={};DPpd=F(0);DPchar=F(4);states=[]
for k in range(1,17):
 eps=F(1,2**k);p=(1-2*eps)**2;nonempty=8*(k-1)*eps*(1-eps)
 if p:
  l,h=lg(p);H=(nonempty-p*h,nonempty-p*l)
 else:H=(nonempty,nonempty)
 check(H[0]>=8*(k-1)*eps,'independent lower entropy bound')
 entropies[k]=H;I=2*k*eps;stopupper=4*I-H[0]
 pdnew=max(stopupper,DPpd/2)
 chnew=max(4+stopupper,DPchar/2+2,pdnew)
 check(pdnew==8*eps,'Bellman upper attained by data stopping policy')
 check(chnew==4+8*eps,'character-query option accounted in Bellman bound')
 check(overlap(H,read_interval(C['scalar_rows'][k-1]['H'])),'32-term vs24-term entropy agreement')
 DPpd,DPchar=pdnew,chnew;states.append({'k':k,'point_defect_optimum':str(DPpd),'character_optimum':str(DPchar)})
for row in C['histories']:
 k=row['m'];eps=F(1,2**k);H=entropies[k];Sroot=(3+2*k*eps-H[1]/4,3+2*k*eps-H[0]/4)
 S0=read_interval(row['S0']);S1=read_interval(row['S1']);A=read_interval(row['A']);B=read_interval(row['B0']);L=read_interval(row['L0']);U=read_interval(row['new_U'])
 Lre=(A[0]+max(F(0),S0[0]-Sroot[1]),A[1]+max(F(0),S0[1]-Sroot[0]))
 check(overlap(Lre,L),'independent actual old liability reconstruction')
 check(Lre[1]<F(39,32),'old full L, not only source KL, is bounded')
 newU=(max(F(0),S1[0]-S0[1]),max(F(0),S1[1]-S0[0]))
 check(overlap(U,newU),'post-leg extra U independently reconstructed')
 residue=(S1[0]-L[1]-B[1]-F(11,32)-U[1],S1[1]-L[0]-B[0]-F(11,32)-U[0])
 check(residue[0]>F(7,32),'all actual old bookings plus new U retained')
 check(overlap(residue,read_interval(row['remaining'])),'retained-account residue readback')
 releases=read_interval(row['post_releases']);term=read_interval(row['post_terminal_KL'])
 check(overlap(B,(releases[0]+term[0],releases[1]+term[1])),'whole first reset source bill transport diagnostic')
if (R/'out/SECOND.json').exists():
 D=json.loads((R/'out/SECOND.json').read_text(encoding='utf-8'))
 def binary(q):
  lo=hi=F(0)
  for p in [q,1-q]:
   if p:
    a,b=lg(p);lo-=p*b;hi-=p*a
  return lo,hi
 hh4=binary(F(1,8));hh3=binary(F(1,4));H4=entropies[4];H3=entropies[3]
 B0=(hh4[0]-H4[1]/4,hh4[1]-H4[0]/4)
 B1=((3*hh3[0]-H3[1])/8,(3*hh3[1]-H3[0])/8)
 check(B0[0]>0 and B1[0]>0,'independent positive first and second full new bills')
 check(overlap(B0,read_interval(D['B0'])) and overlap(B1,read_interval(D['B1'])),'32-term second-reset bill reconstruction')
 s1=read_interval(D['S1']);aa=read_interval(D['A_and_booked_L0']);u=read_interval(D['U'])
 residue=(s1[0]-aa[1]-B0[1]-B1[1]-F(11,32)-u[1],s1[1]-aa[0]-B0[0]-B1[0]-F(11,32)-u[0])
 check(residue[0]>F(1,128),'all actual old bills plus second canonical reset independently paid')
 check(overlap(residue,read_interval(D['remaining_after_second_reset'])),'second-reset remaining endpoint readback')
 check(2-F(155,128)-2*F(7,32)-F(11,32)==F(1,128),'universal scoped second-reset margin arithmetic')
check(len(C['histories'])==5,'frozen five physical histories present')
check(any(F(h['B0'][0])>0 for h in C['histories'] if h['m']==4),'proper data prefix with positive first reset present')
check(any(h['positive_outcome_nodes']>0 and F(h['B0'][0])>0 for h in C['histories']),'positive-reset nonfair outcome test present')
out={'status':'PASS','assertions':count,'runtime_seconds':time.monotonic()-start,'method':'independent32-term rational entropy, exact Bellman optimum recurrence and original-booking reconstruction; no payment checker imported','states':states}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:out[k] for k in ['status','assertions','runtime_seconds']}))
