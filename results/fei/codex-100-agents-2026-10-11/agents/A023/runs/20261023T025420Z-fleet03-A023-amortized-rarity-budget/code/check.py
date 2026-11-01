"""Actual balancing-sign children with no renewed source; frozen domain."""
import sys,json,time,itertools,importlib.util
from pathlib import Path
from fractions import Fraction as Q
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
source=ROOT/'runs/20261023T022946Z-fleet03-A023-amortized-rarity-budget/code/check.py'
spec=importlib.util.spec_from_file_location('pre_z',source);pre=importlib.util.module_from_spec(spec);spec.loader.exec_module(pre)
h=pre.h;START=time.perf_counter();CHECKS=0;POST={};ROWS=[]
def ck(ok):
 global CHECKS
 assert ok
 CHECKS+=1
 assert time.perf_counter()-START<60
def save(n,x):(RUN/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def key(m,w,fix):return (m,w,tuple(sorted(fix.items())))
def post(s,z):
 k=(key(s['m'],s['w'],s['fixed']),z)
 if k in POST:return POST[k]
 m=s['m'];w=s['w'];fixed=s['fixed'];active=[i for i in range(m+3) if i!=m and i not in fixed];data=[i for i in active if i<m];ctrl=[i for i in active if i>m]
 table=[]
 for x in range(1<<len(active)):
  y=pre.expand(x,active,fixed);core=y% (1<<m);A=(y>>(m+1))&1;B=(y>>(m+2))&1
  table.append(pre.bent(core,m)*(-1 if z else 1)*(-1 if A and core==(w if B else 0) else 1))
 p=pre.law(table);old_projected={}
 for mask,a in s['p'].items():
  ck((mask>>len(data))&1==1);new=(mask% (1<<len(data)))|((mask>>(len(data)+1))<<len(data));old_projected[new]=a
 ck(p==old_projected)
 ref={mask:s['qd'][mask% (1<<len(data))]*s['nu'][mask>>len(data)] for mask in p}
 H=pre.ent(p);C=pre.ce(p,ref);K=h.add((1,C),(-1,H));ck(H==s['H'] and C==s['C'] and K==s['K'])
 ii={i:pre.influence(table,j) for j,i in enumerate(active)};ID=sum((ii[i] for i in data),Q(0));IC=sum((ii[i] for i in ctrl),Q(0));ck(ID==s['ID']-1 and IC==s['IC'])
 R=s['R'];B=h.add((1,h.rational(4*ID-Q(m,8)-R)),(-1,C));ck(B==h.add((1,s['B']),(-1,h.rational(4))))
 out=dict(m=m,w=w,fixed=fixed,z=z,H=H,C=C,K=K,B=B,ID=ID,IC=IC,R=R,ii=ii)
 POST[k]=out;row={'m':m,'w':w,'fixed':{str(i):a for i,a in fixed.items()},'z':z,'ID':str(ID),'IC':str(IC),'R':str(R)}
 for n in ['H','C','K','B']:row[n]=pre.vec(out[n])
 ROWS.append(row);return out
def children(s,i,z):
 a,b=pre.transition(s,i);pa,pb=post(a,z),post(b,z);ps=post(s,z)
 ck(ps['ID']-(pa['ID']+pb['ID'])/2==(ps['ii'][i] if i<s['m'] else 0))
 releaseC=h.add((1,ps['C']),(-Q(1,2),pa['C']),(-Q(1,2),pb['C']));releaseR=ps['R']-(pa['R']+pb['R'])/2
 ck(h.add((1,ps['B']),(-Q(1,2),pa['B']),(-Q(1,2),pb['B']))==h.add((1,h.rational(4*ps['ii'][i] if i<s['m'] else 0)),(-1,releaseC),(-1,h.rational(releaseR))))
 return a,b
def main():
 cases={}
 def add(m,w,fix):cases[key(m,w,fix)]=(m,w,fix)
 for m in [4,6,10]:
  for w in ([1] if m==10 else [1,3]):
   for controls in itertools.product([None,0,1],repeat=2):
    f={m+1+j:a for j,a in enumerate(controls) if a is not None};add(m,w,f)
    for i in ([0] if m==10 else range(m)):
     for a in [0,1]:add(m,w,f|{i:a})
 for m in [8,10]:
  for j in range(m+1):add(m,1,dict.fromkeys(range(j),0))
  for j in range(m):add(m,1,dict.fromkeys(range(j),0)|{j:1})
 ck(len(cases)==458)
 for counter,(m,w,fix) in enumerate(cases.values(),1):
  s=pre.state(m,w,fix)
  for z in [0,1]:post(s,z)
  if counter%25==0:save('checkpoint.json',{'completed_profiles':counter,'z_children':len(POST),'checks':CHECKS})
 save('checkpoint.json',{'profiles':len(cases),'z_children':len(POST),'checks':CHECKS})
 DP={};rootrows=[]
 def worst(s,hasz):
  k=(key(s['m'],s['w'],s['fixed']),hasz)
  if k in DP:return DP[k]
  best=s['B'] if hasz else post(s,0)['B']
  if hasz:
   candidate=worst(s,False)
   if h.sign(h.add((1,candidate),(-1,best)))<0:best=candidate
  allow=[i for i in [s['m']+1,s['m']+2] if i not in s['fixed']]
  if s['d']==0:allow+=([0] if s['m']==10 else list(range(s['m'])))
  for i in allow:
   a,b=children(s,i,0);children(s,i,1);v=h.add((Q(1,2),worst(a,hasz)),(Q(1,2),worst(b,hasz)))
   if h.sign(h.add((1,v),(-1,best)))<0:best=v
  DP[k]=best;return best
 for m in [4,6,10]:
  for w in ([1] if m==10 else [1,3]):
   s=pre.state(m,w,{});a=worst(s,True);b=worst(s,False);ck(a==b)
   if m==10:ck(h.sign(h.add((1,a),(-1,h.rational(Q(729,4096)))))>0)
   rootrows.append({'m':m,'w':w,'worst_all_policy_bank':pre.vec(a),'theorem_admitted':m>=10})
 deep=[]
 for m in [8,10]:
  expected={};D=Q(0)
  leaves=[(Q(1,1<<(j+1)),dict.fromkeys(range(j),0)|{j:1}) for j in range(m)]+[(Q(1,1<<m),dict.fromkeys(range(m),0))]
  for reach,fix in leaves:
   s=pre.state(m,1,fix)
   for z in [0,1]:expected=h.add((1,expected),(reach/2,post(s,z)['B']))
   D+=reach*len(fix)
  last=post(pre.state(m,1,dict.fromkeys(range(m),0)),0);ck(h.sign(last['B'])<0);ck(D==2*(1-Q(1,1<<m)))
  if m==10:ck(h.sign(h.add((1,expected),(-1,h.rational(Q(729,4096)))))>0)
  deep.append({'m':m,'D':str(D),'expected_B_after_z':pre.vec(expected),'negative_leaf_B_after_z':pre.vec(last['B']),'full_leaf_KL':pre.vec(last['K'])})
 scalar=[]
 for m in range(10,65):
  bound=Q(m,8)-1-(7*m+Q(15,4))*Q(1,1<<m);ck(bound>=Q(729,4096));ck(7*m-Q(13,4)>0)
  scalar.append({'m':m,'bound':str(bound)})
 ck(Q(729,4096)>Q(1,8));ck(len(POST)==916)
 save('rows.json',ROWS);save('roots.json',rootrows);save('deep_frontiers.json',deep);save('scalar_certificates.json',scalar);save('sign_certificates.json',list(h.SIGNS.values()))
 result={'status':'PASS','profiles':len(cases),'actual_z_children':len(POST),'roots':5,'checks':CHECKS,'inherited_profile_checks':pre.CHECKS,'scalar_integer_cases':len(scalar),'sign_certificates':len(h.SIGNS),'elapsed_seconds':time.perf_counter()-START,'scope':'Amended finite domain: m10 only w1/first core coordinate0 in shallow policy search. Arbitrary-bent all-m>=10 result is analytic author proof, independent-person review pending.'}
 save('validation.json',result);print(json.dumps(result))
if __name__=='__main__':main()
