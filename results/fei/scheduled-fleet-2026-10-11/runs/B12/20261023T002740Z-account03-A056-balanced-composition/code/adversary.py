from reset import *
import reset as model

def direct(f):
 return tuple(Q(sum(a*(-1 if (x&t).bit_count()%2 else 1) for x,a in enumerate(f)),len(f)) for t in range(len(f)))

start=time.perf_counter();records=[]
for d in [2,3,4]:
 phase=tuple(1 if ((x&1)^((x>>1)&1))==0 else -1 for x in range(1<<(d+1)))
 ck(direct(phase)==spectrum(phase))
 s=State(phase,phase,prob(phase),prob(phase),1,1)
 ck(s.I==Q(7,4));ck(edge_inf(s.f,1)==Q(1,2));ck(direct(s.f)==spectrum(s.f))
 ck(sum((edge_inf(s.f,j) for j in range(len(s.f).bit_length()-1)),Q(0))==s.I)
 total={};old=[]
 for t in range(2):
  u=restrict(phase,1,t);ru=prob(u)
  c=State(u,u,ru,ru,1,1)
  ck(c.f==restrict(s.f,1,t))
  for b in range(2):
   e=c.child('B',b);old.append(e)
   ck(e.f==restrict(c.f,c.index('B'),b))
   n=State(e.u,e.v,fresh(e.u),e.rv,e.na,e.nb,e.ea,e.eb,e.z)
   ck(e.I>0);ck(n.I==e.I);ck(e.ru==prob(e.u));ck(n.f==e.f)
   delta=add(n.CE,e.CE,-1)
   expected=scale(log(Q((1<<((1<<d)-1))-1)),Q(1,8))
   ck(delta==expected);total=add(total,delta,Q(1,4))
 ck(total==expected)
 old_spent=Q(1,2)+Q(1,4)
 ck(s.I==old_spent+sum((c.I for c in old),Q(0))/4)
 records.append({'d':d,'root_influence':'7/4','old_spent_influence':str(old_spent),'all_four_prefix_states_nonconstant':True,'fresh_signed_price':ser(total),'expected_price':'(1/8)log2(2^(2^d-1)-1)','root_mean':str(mean(s.f))})
Nd=(1<<127)-1
ck(Nd>(1<<126));ck(Q(126,8)>7*Q(7,4))
# Materialize the actual d7 Boolean witness and every fresh reference mass,
# but represent its log(N7) symbolically to avoid a giant factorization.
d=7
phase=tuple(1 if ((x&1)^((x>>1)&1))==0 else -1 for x in range(1<<(d+1)))
s=State(phase,phase,prob(phase),prob(phase),1,1)
ck(s.I==Q(7,4));ck(sum((edge_inf(s.f,j) for j in range(11)),Q(0))==s.I)
critical=[];old_cost={}
for t in range(2):
 u=restrict(phase,1,t);c=State(u,u,prob(u),prob(u),1,1)
 for bit in range(2):
  e=c.child('B',bit);ck(e.f==restrict(c.f,c.index('B'),bit));ck(e.I>0)
  rr=fresh(e.u);mask=(1<<d)-1
  qnew=tuple(Q(1,16)*rr[j&mask] if (j>>d)&1 and (j&mask) else q for j,q in enumerate(e.Q))
  ck(sum(qnew)==1)
  changed=Q(0);positive_atoms=0
  for j,p in enumerate(e.P):
   if not p:continue
   ck(qnew[j]>0);ratio=e.Q[j]/qnew[j];ck(ratio in [1,Nd])
   if ratio==Nd:changed+=p
   positive_atoms+=1
  ck(changed==Q(1,8));old_cost=add(old_cost,e.CE,Q(1,4))
  critical.append({'shared_outcome':t,'B_outcome':bit,'fresh_reference_sum':'1','coefficient_of_log2_N7':str(changed),'positive_true_atoms_checked':positive_atoms,'nonconstant':True})
import hashlib
out={'status':'PASS','runtime_seconds':time.perf_counter()-start,'assertions':model.N,'direct_small_models':records,'critical_exact_boundary':{'d':7,'root_truth_table_sha256':hashlib.sha256(bytes(x==1 for x in s.f)).hexdigest(),'physical_truth_table_entries':len(s.f),'root_influence':'7/4','old_complete_CE_debit':ser(add(s.CE,old_cost,-1)),'N_d':str(Nd),'all_four_actual_fresh_states':critical,'exact_inequality':'N7>2^126 and126/8>49/4=7*(7/4)','all_d_extension':'N_d>2^(2^d-2), 2^d>=128 for everyd>=7','scope':'refutes unrestricted prescribed geometric-floor payment; Boolean H/I<=20/7 under dummy padding'}}
(R/'out/adversarial.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='direct_small_models'},indent=2))
