from exact import *
import exact,sys

def h(t):return ent([t,1-t])
def node(tab,Q,coords,w=F(1),fixed=None,kind='root'):
 return {'tab':tab,'q':Q,'coords':coords,'w':w,'fixed':fixed or {},'kind':kind}
def split(N,i):
 ch,E,O,z=step(N['tab'],N['q'],N['coords'],i)
 out=[]
 for y,(t,q,c) in enumerate(ch):
  fixed=dict(N['fixed']);fixed[i]=y
  out.append(node(t,q,c,N['w']/2,fixed,N['kind']))
 return out,scale(E,N['w']),scale(O,N['w']),z
def tensor_reference(N,m,r,beta,changed=None):
 coords=N['coords'];parts=[]
 for j in range(m):
  orig=list(range(3+j*r,3+(j+1)*r));free=[i for i in orig if i in coords]
  off=any(N['fixed'].get(i,0)==1 for i in orig)
  vals=[1 if off or s else -1 for s in range(1<<len(free))]
  p=law(vals);b=F(4,5) if j==changed else beta
  q=list(p)
  if not off and len(free)>=2:
   v=1-p[0];q=[p[0]]+[b*x for x in p[1:]];q[-1]+=(1-b)*v
  ck(sum(q)==1)
  parts.append((j,free,p,q,not off and len(free)>=2))
 out=[];actual=[]
 for s in range(1<<len(coords)):
  if any(s>>k&1 and i<3 for k,i in enumerate(coords)):out.append(F(0));actual.append(F(0));continue
  qq=pp=F(1)
  for j,free,p,q,eligible in parts:
   u=sum((1<<k) for k,i in enumerate(free) if s>>coords.index(i)&1)
   qq*=q[u];pp*=p[u]
  out.append(qq);actual.append(pp)
 ck(actual==law(N['tab']))
 return out,parts
def reset(N,Q):
 P=law(N['tab']);old=kl(P,N['q']);new=kl(P,Q)
 M=dict(N);M['q']=Q
 return M,scale(sub(new,old),N['w'])
def initial(m,r):
 d=m*r
 core=[math.prod(-1 if ((s>>(j*r))&((1<<r)-1))==0 else 1 for j in range(m)) for s in range(1<<d)]
 tab=[(-1 if s&2 else 1) if not s&1 else (core[s>>3] if s&4 else 1) for s in range(1<<(d+3))]
 P=law(tab);dummy=node(core,[],list(range(3,d+3)))
 qcore,parts=tensor_reference(dummy,m,r,F(7,8))
 Q=list(P)
 for s in range(1,1<<d):
  for c in [0,1,4,5]:Q[(s<<3)|c]=qcore[s]/16
 ck(sum(Q)==1);ck(Q[0]==P[0])
 return node(tab,Q,list(range(d+3))),core
def account(leaves,A,H0,I0,sig1,sig2,E,O):
 Hf=If=F(0);Hiv=(0,0);K=(0,0);rows=[]
 for N in leaves:
  P,ds,H,TC,S4=info(N['tab']);w=N['w'];ii=sum(ds)
  Hiv=add(Hiv,scale(H,w));If+=w*ii;K=add(K,scale(kl(P,N['q']),w))
  rows.append({'reach':str(w),'kind':N['kind'],'fixed':N['fixed'],'coords':N['coords'],'H':encode(H),'I':str(ii),'S4':encode(S4),'KL':encode(kl(P,N['q'])),'reference':list(map(str,N['q']))})
 R=I0-If;e=sub(sub(H0,Hiv),iv(4*R));S4=sub(iv(4*If),Hiv)
 J=add(add(add(A,e),sig1),sig2);J=(max(J[0],0),max(J[1],0))
 leftover=sub(sub(S4,J),iv(F(1,4)))
 ck(leftover[0]>F(17,24)*S)
 # Complete source chain with both actually exercised reset amounts.
 chain=sub(sub(add(add(A,sig1),sig2),add(E,O)),K)
 ck(chain[0]<=0<=chain[1])
 ck(S4[0]>=2*S)
 return {'H_terminal':encode(Hiv),'I_terminal':str(If),'S4_terminal':encode(S4),'removed_influence':str(R),'query_signed_edge':encode(e),'liability':encode(J),'remaining_original_owner':encode(leftover),'sigma1':encode(sig1),'sigma2':encode(sig2),'erasure':encode(E),'outcome':encode(O),'KL_terminal':encode(K),'terminals':rows}
def run_case(m,r,policy):
 root,core=initial(m,r);P,ds,H0,TC,S4=info(root['tab']);I0=sum(ds);A=kl(P,root['q'])
 M0=sub(iv(4*I0),add(H0,A));delta=F(1,2**r);t=F(sum(x==-1 for x in core),len(core))
 ck(M0[0]>(1+2*t+F(3,10)*m*delta)*S)
 bs,E,O,z=split(root,2);base=bs[0];base['kind']='b0-retained'
 front,e,o,zz=split(bs[1],3);E=add(E,e);O=add(O,o)
 mixed=[base];sigma1=(0,0)
 for N in front:
  pair,e,o,zz=split(N,0);E=add(E,e);O=add(O,o)
  for x,M in enumerate(pair):
   if x==0:Q=law(M['tab']);M['kind']='x0-character'
   else:Q,_=tensor_reference(M,m,r,F(5,6));M['kind']='x1-paid-core'
   M,s=reset(M,Q);sigma1=add(sigma1,s);mixed.append(M)
 ck(sigma1[1]<F(11,40)*m*delta*S)
 leaves=[];sigma2=(0,0);two_nonconstant=0;reset_details=[]
 for N in mixed:
  if N['kind']!='x1-paid-core' or (policy=='last-data0' and N['fixed'][3]!=0):leaves.append(N);continue
  _,parts=tensor_reference(N,m,r,F(5,6));eligible=[p for p in parts if p[-1]]
  if not eligible:leaves.append(N);continue
  j,free,p,qq,_=eligible[0 if policy=='first' else -1]
  pair,e,o,zz=split(N,free[0]);E=add(E,e);O=add(O,o)
  if all(len(set(M['tab']))>1 for M in pair):two_nonconstant+=1
  local=(0,0)
  for M in pair:
   Q,_=tensor_reference(M,m,r,F(5,6),changed=j)
   M,s=reset(M,Q);sigma2=add(sigma2,s);local=add(local,s);M['kind']='second-reset';leaves.append(M)
  ck(local[1]<=N['w']*F(1,2)*log(F(5,4))[1])
  reset_details.append({'queried_factor':j,'parent_width':len(free),'parent_reach':str(N['w']),'signed_reset':encode(local)})
 ck(sigma2[1]<F(1,24)*S)
 out=account(leaves,A,H0,I0,sigma1,sigma2,E,O)
 out.update({'m':m,'r':r,'policy':policy,'sigma2_display':diag(sigma2),'two_nonconstant_pairs':two_nonconstant,'second_resets':reset_details,'root_source_A':encode(A),'original_source_headroom':encode(M0)})
 if (m,r)==(2,3) and policy in ['last','last-data0']:
  ck(sigma2[0]>0);ck(two_nonconstant>=1)
 return out

pilot='--pilot' in sys.argv
cases=[(1,3)] if pilot else [(1,3),(2,2),(2,3),(3,2)]
results=[run_case(m,r,p) for m,r in cases for p in ['first','last','last-data0']]
ck(5**3<2*4**3)
out={'status':'PASS','ledger_checks':exact.COUNT,'runtime_seconds':time.monotonic()-START,'pilot':pilot,'cases':results,'positive_second_resets':sum(F(x['sigma2'][0])>0 for x in results),'strict_global_bound':'sigma2<1/24; after old quarter remainder>17/24'}
(BASE/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','ledger_checks','runtime_seconds','positive_second_resets','pilot']}))
