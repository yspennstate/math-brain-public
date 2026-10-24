import time,json
from fractions import Fraction as Q
import arithmetic as a
a.S=1<<192;a.NAT=1<<256;a.TERMS=96;a.LN2=a.ln_unit(2,1);a.lint.cache_clear()
import search as s
def Hcore(n):
 N=1<<n
 z=a.mul(a.xlog(Q((N-6)**2,N*N)),-1)
 z=a.sub(z,a.mul(a.xlog(Q(36,N*N)),Q(N,4)-1))
 return a.sub(z,a.mul(a.xlog(Q(4,N*N)),Q(3*N,4)))
def main():
 t=time.perf_counter();rows=[]
 for n in [6,7,8,9,10,11,12,16,24,32,48,64]:
  p=Q(3,1<<n);H=Hcore(n);I=Q(6*n-8,1<<n);C,qs=s.outer(p,p);C0,_=s.outer(Q(0),p);C1,q1=s.outer(Q(1),p)
  S=a.sub((4*I,)*2,H);D=a.sub(C,a.add(a.mul(C0,1-p),a.mul(C1,p)))
  e=a.sub(D,a.mul(S,qs[0]));end=a.sub(a.mul(S,sum(q1[1:])),C1);parent=a.sub(a.mul(S,sum(qs)),C)
  a.ck(e[0]>0);a.ck(end[1]<0);a.ck(parent[0]>0)
  rows.append({'n':n,'excess4':e,'negative_endpoint_S4':end,'parent_S4':parent})
  a.save('FINITE_REVIEW_PARTIAL.json',rows)
 # Fixed stopping tree from source: direct physical restriction census, no source data.
 order=[2,0,1,3,4,5];front=[((2,)*6,Q(1))];nodes=[];terminal=[]
 for depth in range(7):
  nxt=[]
  for tag,reach in front:
   node=s.state(tag);slack=a.sub((4*node['I'],)*2,node['H']);nodes.append({'tag':tag,'depth':depth,'reach':reach,'S4':slack})
   if not node['core']['I']:terminal.append((node,reach));continue
   if depth<6:
    for bit in (0,1):
     child=list(tag);child[order[depth]]=bit;nxt.append((tuple(child),reach/2))
  front=nxt
 a.ck(len(nodes)==27);a.ck(min(x['depth'] for x in nodes if x['S4'][1]<0)==6)
 a.ck(sum(r for _,r in terminal)==1)
 root=s.state((2,)*6);endH=(Q(0),Q(0));endI=Q(0)
 for node,r in terminal:endH=a.add(endH,a.mul(node['H'],r));endI+=r*node['I']
 a.ck(root['I']-endI==root['qs'][0]*s.G['I'])
 total=a.sub(a.sub(root['H'],endH),(4*(root['I']-endI),)*2)
 a.ck(total[0]>0)
 # Census intervals certify rational bounds, including dummy-query zeros.
 records=json.loads((a.ROOT/'out/STATES_PARTIAL.json').read_text());edges=json.loads((a.ROOT/'out/EDGES.json').read_text())
 a.ck(len(records)==729);a.ck(len(edges)==1458)
 for r in records:a.ck(Q(r['H'][1])<Q(21,5)*Q(r['I']))
 negative=[r for r in records if Q(r['other_owner9over2'][1])<0]
 a.ck(len(negative)==23)
 witness=next(r for r in negative if r['tag']==[0,0,0,0,0,2])
 # A donor-negative complete state remains fully affordable at9/2.
 a.ck(Q(witness['H'][1])<Q(9,2)*Q(witness['I']))
 a.ck(Q(witness['other_owner9over2'][1])<Q(-1,10))
 result=json.loads((a.ROOT/'out/RESULTS.json').read_text())
 for name,left,right in [('full_terminal_H_over_I',Q(4198,1000),Q(21,5)),('complete_selected_reveal_required_rate',Q(547,100),Q(548,100)),('individual_query_required_rate',Q(629,100),Q(63,10))]:
  l,u=map(Q,result['maxima'][name]['interval']);a.ck(left<l<=u<right)
 # Even the original root complete reveal cannot use selected-only rate9/2.
 p=s.G['p'];D=a.sub(root['C'],a.add(a.mul(s.outer(Q(0))[0],1-p),a.mul(s.outer(Q(1))[0],p)))
 excess45=a.sub(a.add(a.mul(s.G['H'],root['qs'][0]),D),(Q(9,2)*root['qs'][0]*s.G['I'],)*2)
 a.ck(excess45[0]>0)
 out={'source_finite_clauses':rows,'tree_nodes':nodes,'tree_total_excess':total,'negative_donor_witness':witness,'root_complete_excess9over2':excess45,'rational_census_bounds_checked':True,'checks':a.checks,'seconds':time.perf_counter()-t}
 a.save('VERIFICATION.json',out);print('verification checks',a.checks,'seconds',out['seconds'])
if __name__=='__main__':main()
