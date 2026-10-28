from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import ast,json,time,hashlib
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(b):
 global checks
 assert b
 checks+=1
def product_q(xs):
 out=F(1)
 for x in xs:out*=x
 return out
def lift(r,kap):return [r[z]*kap[z][i] for z in [0,1] for i in [0,1]]
def intpower(x,w):ck(w.denominator==1);return x**w.numerator
def valid(q0,rs,qs):
 return all(sum(qs[u])==1 and all(v>=0 for v in qs[u]) and [sum(qs[u][2*z:2*z+2]) for z in [0,1]]==rs[u] for u in [0,1]) and all((qs[0][s]+qs[1][s])/2==q0[s] for s in range(4))
records=[]
for a in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
 for k in range(1,8):
  for j in range(1,16):
   if not 0<4*k-j<16:continue
   pz=[a,1-a];r0=[F(k,8),1-F(k,8)];rs=[[F(j,16),1-F(j,16)]];rs.append([2*r0[z]-rs[0][z] for z in [0,1]])
   kap=[[F(1,3),F(2,3)],[F(2,5),F(3,5)]];p=lift(pz,kap);q0=lift(r0,kap);opt=[lift(r,kap) for r in rs];ck(valid(q0,rs,opt))
   direct=product_q(intpower(q0[s]/opt[u][s],60*p[s]) for u in [0,1] for s in range(4))
   formula=product_q(intpower(r0[z]**2/(rs[0][z]*rs[1][z]),60*pz[z]) for z in [0,1]);ck(direct==formula);ck(formula>=1)
   for sg in [-1,1]:
    comp=[list(q) for q in opt]
    for z in [0,1]:
     eps=min(comp[u][2*z+i] for u in [0,1] for i in [0,1])/4
     for u in [0,1]:comp[u][2*z]+=sg*(-1)**u*eps;comp[u][2*z+1]-=sg*(-1)**u*eps
    ck(valid(q0,rs,comp));ratio=product_q(intpower(opt[u][s]/comp[u][s],60*p[s]) for u in [0,1] for s in range(4));ck(ratio>1)
    broken=[list(q) for q in comp];broken[1]=list(opt[1]);ck(not valid(q0,rs,broken))
   inheritedkap=[[F(1,4),F(3,4)],[F(3,7),F(4,7)]];old=lift(r0,inheritedkap);cal=lift(pz,inheritedkap)
   change=product_q(intpower(old[s]/cal[s],60*p[s]) for s in range(4) if p[s])
   coarse=product_q(intpower(r0[z]/pz[z],60*pz[z]) for z in [0,1] if pz[z]);ck(change==coarse);ck(coarse<=1)
   records.append({'a':str(a),'k':k,'j':j,'exact_power_identity':True,'all_tested_compatible_perturbations_cost_more':True})
ck(len(records)==285)
# Definitions-only extraction of the independently written truth-table implementation.
# Importing/executing its module would rewrite an old run, so no top-level statements execute.
source=R.parents[0]/'20261023T045953Z-account03-A031-convolution-identity/code/reproduce.py'
needed={'lg','logs','add','scale','sub','av','zero','overlap','marg','fair','ce','H','B','Mrow','cmi','normalize_h','spectrum','child'}
tree=ast.parse(source.read_text(encoding='utf-8'));defs=[node for node in tree.body if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)) and node.name in needed]
ns={'F':F,'ck':ck,'cache':{},'lru_cache':lru_cache,'start':start,'time':time}
exec(compile(ast.Module(body=defs,type_ignores=[]),str(source),'exec'),ns)
S=ns['spectrum'];child=ns['child'];H=ns['H'];B=ns['B'];ce=ns['ce'];fair=ns['fair'];add=ns['add'];av=ns['av'];sub=ns['sub'];norm=ns['normalize_h']
@lru_cache(None)
def bell(L,h):
 ck(time.monotonic()-start<55)
 p=S(L,h)[1];values=[ce(p,fair(p,4))]
 for i in [0,2]+[i for i in range(5,2*L+4)]:
  if i in dict(h):continue
  values.append(add(B(p,i),av([bell(L,norm(h+((i,u),))) for u in [0,1]])))
 return tuple(max(v[j] for v in values) for j in [0,1])
reviewrows=[]
for L in [1,2]:
 p=S(L,())[1];M=add(*(ns['Mrow'](p,i) for i in range(2*L+4)));I=sum(v for mask,v in p.items() for i in [3]+list(range(4,2*L+4)) if mask>>i&1)
 bb=[B(child(L,(),3,s)[1],1) for s in [0,1]];D=add(M,B(p,3),av(bb));env=[bell(L,norm(((3,s),(1,t)))) for s in [0,1] for t in [0,1]];bill=add(D,av(env));spare=17*I-bill[1];ck(spare>F(1,8));reviewrows.append({'L':L,'all_policy_spare_lower':str(spare)})
ck(bell.cache_info().currsize==1080);ck(F(32,31)**16<2)
q=F(1,1<<64);I=(2-2*q+q*q)/8+128*q*(3-q)/8;ck(17*I<5)
# Fixed parity witness: exact powers prove cost>1 at m4, with no logarithm error.
eps=F(1,16);ck(F(1,4)/(eps*(1-eps))>4)
ck([F(1,16),F(15,16)]!=[F(0),F(1)])
out={'checks':checks,'seconds':time.monotonic()-start,'profile_cases':len(records),'all_policy_states':bell.cache_info().currsize,'all_profile_formulae_exact':True,'actual_five_bit_obstruction_exact':True,'free_calibration_wrong_for_forced_class_rejected':True,'helper_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'review_rows':reviewrows}
(R/'out/REPRODUCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
review={'claim_id':'A035-ALL-QUERY-TERMINAL-KL-ENVELOPE','version':1,'verdict':'HOLDS_AT_STATED_SUPPLIED_SOURCE_SCOPE_NO_REPAIR','analytic_reconstruction':'DERIVATION section1; exact endpoint identity and original C2 comparison reproduce all-L/all-tree full-KL cap and reserve; source >7/8 is an inherited A031 author dependency, not relabeled full-chain independent review','independent_validation':'All adaptive query/stop policies retaining j at triangle L1,2:1080 states; exact mixture scalar; actual Boolean L64 five-bit uniform-reference obstruction','limits':'Does not pay arbitrary full terminal KL, positive-part turnover, or arbitrary-core initial source'}
(R/'out/REVIEW_A035.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='review_rows'}))
