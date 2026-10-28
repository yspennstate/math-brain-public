from pathlib import Path
import ast,json,time,hashlib
from fractions import Fraction as Q
R=Path(__file__).resolve().parents[1];O=R/'out';src=R/'code/check.py'
spec={'helper':'A041-nested-adversarial-v1','family':'depth-three disjoint AND4 and OR(AND(OR(X1,X2),X3),X4), plus physical repeated-wire countercontrol','domain':'both shapes at all1/3 and (1/4,1/2,3/4,1/3)','case_count':5,'symmetry':'none','arithmetic':'exact Fraction and proved log intervals; direct physical spectrum versus recursively inherited reference','memory_estimate_MB':100,'maximum_runtime_seconds':60,'helper_source_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
(O/'FROZEN_NESTED.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
# Load only definitions/imports; never execute or repeat the prior enumeration.
tree=ast.parse(src.read_text(encoding='utf-8'))
defs=ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef))],type_ignores=[])
ns={'__file__':str(src),'R':R,'O':O,'assertions':0,'formula_count':0,'start':time.monotonic()}
exec(compile(defs,str(src),'exec'),ns)
ns['L2'],ns['U2']=ns['series'](Q(2))
rows=[]
for ps in [(Q(1,3),)*4,(Q(1,4),Q(1,2),Q(3,4),Q(1,3))]:
 for tables in [(8,8,8),(14,8,14)]:
  base=ns['gate'](tables[2],ps[:2]);mid=ns['build'](tables[1],base,ns['literal'](ps[2]));f=ns['build'](tables[0],mid,ns['literal'](ps[3]));ns['check_formula'](f)
  rows.append({'tables_outer_to_inner':tables,'biases':list(map(str,ps)),'Delta':str(f['D']),'R_flat':str(f['R']),'R_tree':str(f['Rt']),'TV':str(ns['tv'](f['Q'],f['T']))})
p=Q(1,3)
# Repeated-wire law summed in the physical sample space, separately from the
# fictitious two-independent-input product sum.
wire_mean=sum((prob*(2*x*x-1) for x,prob in [(0,1-p),(1,p)]),Q(0))
ind_mean=sum(((p if x else 1-p)*(p if y else 1-p)*(2*x*y-1) for x in (0,1) for y in (0,1)),Q(0))
assert wire_mean**2==Q(1,9) and ind_mean**2==Q(49,81)
out={'status':'PASS','cases':5,'assertions':ns['assertions']+1,'runtime_seconds':time.monotonic()-ns['start'],'rows':rows,'wire_empty':str(wire_mean**2),'independent_empty':str(ind_mean**2)}
assert out['runtime_seconds']<60
(O/'NESTED_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
