import ast,json,time
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];START=time.perf_counter();N=0
old=R.parent/'20261023T070855Z-account03-A088-booleanity-referee'/'code'/'real_scope.py'
tree=ast.parse(old.read_text(encoding='utf-8'));names={'ck','chars','transform','cut','energy'}
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[]),str(old),'exec'),globals())
v=[F((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(3)))-2*((x&127)==0 and bool(x&128)) for x in range(256)]
labels=list(range(8));tv=transform(v,labels);paths=[[],[(7,0)],[(7,1)],[(7,1),(6,0)],[(7,1),(6,1)]]
prefix=[(7,1),(6,0)];paths.extend([prefix+[(0,0)],prefix+[(0,1)],prefix+[(0,0),(1,0)],prefix+[(0,0),(1,1)]])
rows=[]
for path in paths:
 p=v;q=tv;lab=labels
 for i,b in path:
  oldlab=lab;p,lab=cut(p,oldlab,i,b);q,_=cut(q,oldlab,i,b)
 a,b=chars(p),chars(q)
 ck(q==transform(p,lab),'commutation through actual early w')
 ck([x*x for x in a]==[x*x for x in b],'all restricted spectra unchanged')
 ck(sum(x*x for x in q)==len(q),'actual real node norm1')
 ck(any(x not in (-1,1) for x in q),'actual nonBoolean node')
 for j in range(len(lab)):ck(energy(p,j)==energy(q,j),'all Dirichlet influences unchanged')
 rows.append({'path':path,'value_set':sorted(set(map(str,q))),'norm_squared':'1'})
c=chars(tv);conv=sum((c[s]*c[s^16] for s in range(256)),F());ck(conv!=0,'nonempty Boolean convolution fails')
out={'status':'PASS','checks':N,'runtime_seconds':time.perf_counter()-START,'nodes':rows,'nonempty_convolution':{'shift':16,'value':str(conv)},'scope':'Untouched-pair prefix only; includes actual early w and its following edited block'}
(R/'out'/'REAL_SCOPE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({'status':'PASS','checks':N,'nodes':len(rows),'runtime_seconds':out['runtime_seconds'],'convolution':str(conv)}))
