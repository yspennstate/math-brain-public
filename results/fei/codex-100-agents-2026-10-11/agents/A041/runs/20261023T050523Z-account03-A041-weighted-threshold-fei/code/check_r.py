from pathlib import Path
from fractions import Fraction as Q
import ast,json,time,hashlib
R=Path(__file__).resolve().parents[1];O=R/'out';src=R/'code/check.py'
spec={'helper':'A041-nonzero-inherited-R-v1','family':'AND2(atomic AND3(X1,X2,X3),X4)','domain':'all1/3 and (1/4,1/2,3/4,1/3)','case_count':2,'symmetry':'none','arithmetic':'exact Fraction/direct physical transform/rational log intervals','memory_estimate_MB':100,'maximum_runtime_seconds':60,'purpose':'exercise nonzero inherited gate R, absent from all-binary controls','helper_source_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
(O/'FROZEN_R.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8',newline='\n')
tree=ast.parse(src.read_text(encoding='utf-8'));defs=ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef))],type_ignores=[])
ns={'__file__':str(src),'assertions':0,'formula_count':0,'start':time.monotonic()};exec(compile(defs,str(src),'exec'),ns);ns['L2'],ns['U2']=ns['series'](Q(2))
rows=[]
for ps in [(Q(1,3),)*4,(Q(1,4),Q(1,2),Q(3,4),Q(1,3))]:
 f=ns['build'](8,ns['gate'](128,ps[:3]),ns['literal'](ps[3]));ns['check_formula'](f);assert f['Rt']>0
 rows.append({'biases':list(map(str,ps)),'Delta':str(f['D']),'R_flat':str(f['R']),'R_tree':str(f['Rt']),'TV':str(ns['tv'](f['Q'],f['T']))})
out={'status':'PASS','cases':2,'assertions':ns['assertions']+2,'runtime_seconds':time.monotonic()-ns['start'],'rows':rows};assert out['runtime_seconds']<60
(O/'R_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
