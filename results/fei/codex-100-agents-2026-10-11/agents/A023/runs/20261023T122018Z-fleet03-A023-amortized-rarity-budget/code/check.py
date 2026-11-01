"""Frozen exact actual-reference continuation; no implicit domain escalation."""
import sys,time,json,itertools,importlib.util
from pathlib import Path
from fractions import Fraction as Q
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
old=ROOT/'runs/20261023T063426Z-fleet03-A023-amortized-rarity-budget/code/check.py'
sp=importlib.util.spec_from_file_location('paid_v8',old);p=importlib.util.module_from_spec(sp);sp.loader.exec_module(p);h=p.h
START=time.perf_counter();CHECKS=0;ROWS=[];CACHE={};PILOT='--pilot' in sys.argv
LIMIT=60 if PILOT else 180
def ck(ok):
 global CHECKS
 assert ok
 CHECKS+=1
 assert time.perf_counter()-START<LIMIT
def save(n,o):(RUN/'out'/n).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def vec(x):return {str(k):str(v) for k,v in sorted(x.items()) if v}
def ce(P,q):
 c={}
 for i,a in P.items():h.lg(c,q[i],-a)
 return h.add((1,c))
def profile(m,fix):
 key=(m,tuple(sorted(fix.items())))
 if key in CACHE:return CACHE[key]
 # The imported helper's cap remains the same as this explicitly frozen job.
 p.START=time.perf_counter()
 s=p.state(m,1,(1<<m)-1,fix,0);active=[i for i in range(m) if i not in fix]
 base=[];actual=[];A=fix[m+1];B=fix[m+2];marked=A==1 and B==0
 for x in range(1<<len(active)):
  y=p.scatter(x,active,{i:v for i,v in fix.items() if i<m});b=p.seed(y,m,(1<<m)-1)
  base.append(b);actual.append(b*(-1 if A and y==(1 if B else 0) else 1))
 pb=p.law(base);P=p.law(actual);u=Q(1,len(base))
 qo={i:(pb.get(i,Q(0))+u)/2 for i in range(len(base))}
 qn={i:(P.get(i,Q(0))+u)/2 for i in range(len(base))} if marked else qo
 ck(sum(qn.values())==1 and min(qn.values())>0)
 C=ce(P,qn);K=h.add((1,C),(-1,s['H']));D=h.add((1,C),(-1,s['C']));bn=h.add((1,s['B']),(-1,D))
 ck(ce(P,qo)==s['C']);ck(h.sign(K)>=0);ck(K==h.add((1,C),(-1,s['H'])))
 ck(D==h.add((1,K),(-1,s['K'])));ck(s['R']==0 and s['IC']==0)
 if marked:ck(h.sign(h.add((1,h.rational(1)),(-1,K)))>=0);ck(h.sign(h.add((1,h.rational(1)),(-1,D)))>=0)
 else:ck(not D and C==s['C'])
 out=dict(s=s,C=C,K=K,D=D,Bnew=bn,marked=marked)
 row={'m':m,'fix':{str(i):v for i,v in fix.items()},'marked':marked,'k':len(active),'ID':str(s['ID']),'M':str(s['M']),'Z':str(s['Z']),'R':str(s['R'])}
 for name,v in [('H',s['H']),('Cold',s['C']),('Kold',s['K']),('Bold',s['B']),('Cnew',C),('Knew',K),('D',D),('Bnew',bn)]:row[name]=vec(v)
 out['row']=len(ROWS);ROWS.append(row);CACHE[key]=out;return out
def combine(rows,field):return h.add(*[(q,z[field]) for q,z in rows])
def main():
 results=[];queries=[];terminal=[];resets=[]
 for m in ([6] if PILOT else [6,8]):
  EB={};ED={};EZ=EM=N=DEPTH=MASS=NEG=EXTRA=Q(0);count=parents=nodes=0;reset_mass=Q(0)
  opts=[[{a:0},{a:1,a+1:0},{a:1,a+1:1}] for a in range(0,m,2)]
  for pieces in itertools.product(*opts):
   cf={i:v for z in pieces for i,v in z.items()};free=[i for i in range(m) if i not in cf]
   for A,B in itertools.product([0,1],repeat=2):
    ctrl={m+1:A,m+2:B};marked=A==1 and B==0;negative=A==B==0
    if marked:
     par=profile(m,cf|ctrl);parents+=1;reset_mass+=Q(1,1<<(len(cf)+2));resets.append(par['row'])
     if free:
      j=free[0];ch=[profile(m,cf|ctrl|{j:v}) for v in [0,1]];s=par['s'];a,b=[z['s'] for z in ch]
      ck(s['M']==(a['M']+b['M'])/2);ck(s['Z']-(a['Z']+b['Z'])/2==4)
      pivot=s['ii'][j];ck(s['ID']-(a['ID']+b['ID'])/2==pivot)
      dc=h.add((1,par['C']),(-Q(1,2),ch[0]['C']),(-Q(1,2),ch[1]['C']))
      ck(h.add((1,par['Bnew']),(-Q(1,2),ch[0]['Bnew']),(-Q(1,2),ch[1]['Bnew']))==h.add((1,h.rational(4*pivot)),(-1,dc)))
      signed_increment=h.add((Q(1,2),ch[0]['D']),(Q(1,2),ch[1]['D']),(-1,par['D']))
      ck(h.add((1,par['D']),(1,signed_increment))==h.add((Q(1,2),ch[0]['D']),(Q(1,2),ch[1]['D'])))
      queries.append({'m':m,'parent':par['row'],'coordinate':j,'children':[z['row'] for z in ch],'signed_conversion_increment':vec(signed_increment)});nodes+=1
    assignments=itertools.product([0,1],repeat=len(free)) if negative else [(0,),(1,)] if marked and free else [()]
    for bits in assignments:
     extra=1 if marked and free else 0;cf2=cf|dict(zip(free if negative else free[:extra],bits));fix=cf2|ctrl
     z=profile(m,fix);s=z['s'];reach=Q(1,1<<(len(cf2)+2));consumed=len(free) if negative else extra
     MASS+=reach;DEPTH+=reach*len(cf2);N+=reach*consumed;EXTRA+=reach*extra;EZ+=reach*s['Z'];EM+=reach*s['M'];EB=h.add((1,EB),(reach,z['Bnew']));ED=h.add((1,ED),(reach,z['D']))
     if negative:ck(z['Bnew']==h.rational(-Q(m,8)));NEG+=reach
     terminal.append({'row':z['row'],'reach':str(reach),'consumed_live':consumed,'extra':extra,'negative':negative});count+=1
  ck(count==(164 if m==6 else 564));ck(parents==3**(m//2));ck(nodes==3**(m//2)-2**(m//2));ck(reset_mass==Q(1,4));ck(MASS==1 and NEG==Q(1,4))
  ck(EXTRA==Q(1,4)*(1-Q(1,1<<(m//2))));ck(N==Q(m,16)+EXTRA);ck(DEPTH==Q(13*m,16)+EXTRA);ck(EZ==m-4*N and EM==Q(1,1<<(m+1)))
  bound=Q(5*m,8)-Q(9,4)-(9*m+Q(15,4))*Q(1,1<<m)
  ck(bound>=Q(153,256));ck(h.sign(h.add((1,EB),(-1,h.rational(bound))))>0);ck(h.sign(h.add((1,h.rational(Q(1,4))),(-1,ED)))>=0)
  results.append({'m':m,'terminal_states':count,'reset_parents':parents,'query_nodes':nodes,'expected_core_depth':str(DEPTH),'expected_consumed_live':str(N),'extra_consumed_live':str(EXTRA),'expected_Z':str(EZ),'expected_original_M':str(EM),'negative_branch_mass':str(NEG),'expected_new_bank':vec(EB),'expected_signed_conversion':vec(ED),'strict_lower_bound':str(bound)})
 # Positive first reset, negative surviving edited child, zero unedited child.
 m=6;f={0:0,2:0,4:0,7:1,8:0};g=profile(m,f);a,b=[profile(m,f|{1:v}) for v in [0,1]]
 ck(not g['s']['K'] and h.sign(g['D'])>0);ck(h.sign(a['D'])<0 and not b['D']);ck(g['s']['k']==3 and a['s']['k']==2)
 guards={'parent':g['row'],'surviving_child':a['row'],'unedited_child':b['row'],'free_reset_refuted':True}
 for m in range(6,65):
  lower=Q(5*m,8)-Q(9,4)-(9*m+Q(15,4))*Q(1,1<<m);ck(lower>=Q(153,256));ck(lower>Q(1,2))
 suffix='pilot_' if PILOT else ''
 save(suffix+'rows.json',ROWS);save(suffix+'frontiers.json',{'results':results,'terminal':terminal,'resets':resets,'queries':queries,'guards':guards});save(suffix+'sign_certificates.json',list(h.SIGNS.values()))
 result={'status':'PASS','pilot':PILOT,'profiles':len(ROWS),'terminal_states':sum(x['terminal_states'] for x in results),'reset_parents':len(resets),'query_nodes':len(queries),'checks':CHECKS,'inherited_profile_checks':p.CHECKS,'elapsed_seconds':time.perf_counter()-START,'all_dimensional_scope':'Analytic proof PROOF.md; finite cases are not extrapolated','independent_person_review':'PENDING'}
 save(suffix+'validation.json',result);print(json.dumps(result))
if __name__=='__main__':main()
