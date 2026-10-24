from fractions import Fraction as R
import json,pathlib,time
root=pathlib.Path(__file__).resolve().parent;start=time.monotonic();records=[]
for n in [3,4,5]:
 for q in [R(1,3),R(2,3)]:
  p=1-q;S=list(range(1,1<<n));idx={a:i for i,a in enumerate(S)};d=len(S)
  F=[[R(0) for _ in S] for _ in S];Q=[[R(0) for _ in S] for _ in S]
  def add(M,a,b,rate):
   if a!=b:M[idx[a]][idx[b]]+=rate;M[idx[a]][idx[a]]-=rate
  for a in S:
   for x in range(n):
    l=(x-1)%n;r=(x+1)%n
    if (a>>l&1) or (a>>r&1):add(F,a,a^(1<<x),p if a>>x&1 else q)
    if a>>x&1:
     base=a&~((1<<l)|(1<<r))
     for b in [0,1]:
      for c in [0,1]:add(Q,a,base|(b<<l)|(c<<r),(q if b else p)*(q if c else p))
  K=[[(-p/q)**((a&b).bit_count())-1 for b in S] for a in S]
  for i in range(d):
   for j in range(d):
    assert sum(K[i][k]*F[j][k] for k in range(d))==sum(Q[i][k]*K[k][j] for k in range(d))
  G=[row[:] for row in K];rank=0
  for col in range(d):
   pivot=next((i for i in range(rank,d) if G[i][col]),None)
   if pivot is None:continue
   G[rank],G[pivot]=G[pivot],G[rank]
   v=G[rank][col];G[rank]=[a/v for a in G[rank]]
   for i in range(rank+1,d):
    v=G[i][col]
    if v:G[i]=[a-v*b for a,b in zip(G[i],G[rank])]
   rank+=1
  assert rank==d
  records.append({'n':n,'q':str(q),'nonempty_dimension':d,'schur_rank':rank,
                  'intertwining':'K F^T = Q K exact rational PASS'})
result={'checks':records,'seconds':time.monotonic()-start,
        'scope':'Small finite algebra certificates; all-size invertibility/intertwining are proved separately in FRESH_ATTEMPT.md.'}
(root/'similarity_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('PASS:',len(records),'exact similarity/rank cases; seconds',result['seconds'])
