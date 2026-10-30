import check as c
import json,time
for n in range(3):
 for tab in range(1<<(1<<n)):
  vals=[1 if tab>>x&1 else -1 for x in range(1<<n)]
  orders=list(dict.fromkeys([tuple(range(n)),tuple(reversed(range(n)))]))
  for s in (-1,1):
   for order in orders:
    R=c.fresh(vals,s)
    R=[v/2+c.F(1,2*len(R)) for v in R]
    c.trees+=1
    c.recurse(vals,s,R,list(order))
result={'status':'PASS','trees':c.trees,'nodes':c.nodes,'assertions':c.checks,'source_zero_kernel_rows':c.zero_rows,'seconds':time.perf_counter()-c.START,'scope':'adversarial changed-vacuum initial references; no sign conclusion'}
(c.ROOT/'out/ADVERSARIAL.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
