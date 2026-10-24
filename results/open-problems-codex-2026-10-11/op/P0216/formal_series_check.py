import json,pathlib,math
R=pathlib.Path(__file__).resolve().parent;N=16
def invert(f):
 h=[0]*(N+1);h[1]=1
 for n in range(2,N+1):
  power=[1]+[0]*n;s=0
  for k in range(1,n+1):
   nxt=[0]*(n+1)
   for a in range(n+1):
    for b in range(1,n-a+1):nxt[a+b]+=power[a]*h[b]
   power=nxt
   if k>=2:s+=f[k]*power[n]
  h[n]=-s
 return h
f=[0]+[math.factorial(i) for i in range(1,N+1)];v=invert(f)
g=[0,1]+[3*v[i]+3*(-1)**i for i in range(2,N+1)];h=invert(g)
js=json.loads((R/'formal_series_diagnostic.json').read_text())
assert [str(x) for x in h]==js['H_coefficients']
for x in json.loads((R/'balanced_counts.json').read_text()):assert x['H']==h[x['n']]
out={'python_javascript_coefficients_agree_through':N,'direct_balanced_counts_agree_through':8,'H_9':h[9],'H_16':h[16],'scope':'Exact finite formal coefficient computation; no conjectured optimal-mean constant.'}
(R/'formal_series_check.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out))
