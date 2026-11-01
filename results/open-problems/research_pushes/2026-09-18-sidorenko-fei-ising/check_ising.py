#!/usr/bin/env python3
"""Exact moment-body checks and a limited replay of stored Ising geometry.
No Gaussian integral, Arb program, or full capacity certificate is replayed here.
The four stored matrix packets below are explicit source inputs, not recomputed
integral enclosures. All decisions after those inputs use rational arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import json

PACKETS=[[
 ('15726546543925992355521575107569733082849178097274777675981631552','27070961538716772307762322957715961017555354873793347585',-65),
 ('-10794019565378131765674958047277661149424337842753178072670305898','270709615295823870744441797189429308130785860009437691905',-66)],
 [('12551630857350653458167949036679641732571955492636465413975373900','20116541346230865463077529200610583103045373316669898753',-65),
 ('10841467619893356289200725875848591017475214629163391750381675859','201165413599324433130547440587701284097605266259442663425',-66)]]

def interval(p):
 m,r,e=p;scale=F(10)**e
 return ((int(m)-int(r))*scale,(int(m)+int(r))*scale)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def sub(a,b):return (a[0]-b[1],a[1]-b[0])
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def square(a):
 lo,hi=a
 return (F(0) if lo<=0<=hi else min(lo*lo,hi*hi),max(lo*lo,hi*hi))
def sqrt_bounds(x):
 assert x>=0
 scale=10**60;N=x.numerator*x.denominator*scale*scale;r=isqrt(N)
 return F(r,x.denominator*scale),F(r+(r*r<N),x.denominator*scale)
def sqrtiv(a):return sqrt_bounds(a[0])[0],sqrt_bounds(a[1])[1]
def fmt(iv):return [str(x) for x in iv]
def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
 points=sorted(set(points));out=[]
 for seq in [points,list(reversed(points))]:
  chain=[]
  for p in seq:
   while len(chain)>=2 and cross(chain[-2],chain[-1],p)<=0:chain.pop()
   chain.append(p)
  out.extend(chain[:-1])
 return set(out)
def main():
 # Finite analogue of the continuous monotone-ratio frontier theorem.
 xs=[F(1,2),F(1),F(2),F(3)];ms=[F(2,5),F(3,4),F(9,10),F(99,100)]
 ps=[F(1,8),F(3,8),F(1,4),F(1,4)]
 assert all(ms[i]/xs[i]>ms[i+1]/xs[i+1] for i in range(3))
 def moment(signs):return (sum(p*x*s for p,x,s in zip(ps,xs,signs)),sum(p*y*s for p,y,s in zip(ps,ms,signs)))
 vertices=[moment(s) for s in product([-1,1],repeat=4)]
 lower=[moment([-1]*j+[1]*(4-j)) for j in range(5)]
 frontier=set(lower+ [(-a,-b) for a,b in lower])
 assert frontier==hull(vertices)
 n_support=0
 for u,v in product(range(-8,9),repeat=2):
  if u==v==0:continue
  exact=sum(p*abs(u*x+v*m) for p,x,m in zip(ps,xs,ms))
  assert exact==max(u*a+v*b for a,b in frontier)
  n_support+=1
 # Analytic D > 1/15 guard, all rational ancillary comparisons.
 assert 2*F(22,7)*F(13,5)<F(41,10)**2
 assert 2*F(2,3)>F(5,4)
 e3_lower=sum(F(3**j,__import__('math').factorial(j)) for j in range(7))
 assert e3_lower>19
 pA=F(19,82);pB=F(5,41);var_lower=pA*pB*F(2,5)**2
 assert var_lower==F(38,8405)>F(1,225)
 # Uniform half-body collar: s=1024, c_+ <= 1/230400.
 s=1024; epsilon=F(1,230400)
 assert s>=62 and 1+F(s,2)>2**9
 assert 15*s*epsilon==F(1,15)
 assert F(1)-F(4,5)*F(9,6)==F(-1,5)
 assert F(-1,5)*F(2,3)+15*s*epsilon==F(-1,15)
 assert F(15)*(F(3,2)+F(8,15))==F(61,2)<31
 # Stored-packet geometry replay: does not recompute defining integrals.
 a=[[interval(p) for p in row] for row in PACKETS]
 det=sub(mul(a[0][0],a[1][1]),mul(a[0][1],a[1][0]))
 em=sqrtiv(add(square(sub(a[0][0],a[0][1])),square(sub(a[1][0],a[1][1]))))
 ep=sqrtiv(add(square(add(a[0][0],a[0][1])),square(add(a[1][0],a[1][1]))))
 longest=(max(em[0],ep[0]),max(em[1],ep[1]))
 assert det[0]>0 and longest[0]>0
 radius=(det[0]/longest[1],det[1]/longest[0])
 angle=F(2,125)+2*F(1,10**8)+F(1,10**10)
 siniv=(angle-angle**3/6,angle)
 norm=sqrtiv(add((F(1),F(1)),siniv))
 base=F(3458764513820541,288230376151711744)+F(1,10**12)
 required=add(mul((base,base),norm),mul((F(2,10**7),F(2,10**7)),sqrtiv((F(2),F(2)))))
 floor=F(150391982,10**10)
 assert radius[0]>floor and radius[0]>required[1]
 out={'status':'ALL_EXACT_CHECKS_PASS','finite_moment_body_vertices_enumerated':16,
 'frontier_vertices':len(frontier),'exact_support_directions':n_support,
 'variance_lower_bound':str(var_lower),'D_lower_bound':'1/15 (strict)',
 'half_body_collar':{'tilt':1024,'c_upper_bound':'1/230400','objective_upper_bound':'-1/15 (strict)','integrals_needed_in_collar':0},
 'stored_packet_replay':{'source':'yspennstate/ising-perceptron-capacity/verification/results/huang_star_interior.json',
 'source_payload_certificate_sha256':'e03fa07e2ea959ceb035313d28f222e193fd4d78427b389796746f3c69ae790a',
 'input_matrix_packets':PACKETS,'determinant_positive':True,
 'inradius_interval':fmt(radius),'required_radius_interval':fmt(required),
 'inradius_exceeds_floor':True,'inradius_exceeds_required':True,
 'Gaussian_integral_enclosures_recomputed':False,'full_capacity_certificate_chain_replayed':False},
 'scope':'Analytic moment-body ancillary results and conditional stored-packet arithmetic only.'}
 Path(__file__).with_name('ising_checks.json').write_text(json.dumps(out,indent=2)+'\n')
 print('ALL_EXACT_CHECKS_PASS')
 print('finite support directions:',n_support)
 print('analytic variance lower bound:',var_lower,'> 1/225')
 print('stored geometric packets: exact clearance positive; defining integrals NOT recomputed')
if __name__=='__main__':main()
