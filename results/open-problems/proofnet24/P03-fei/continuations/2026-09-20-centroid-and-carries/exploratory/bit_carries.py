import numpy as np,json
out=[]
for n in (7,9,11,13):
 N=1<<n;wt=np.array([i.bit_count() for i in range(N)],dtype=np.int64)
 # f=-1 on Hamming-weight-one inputs, +1 elsewhere.
 W=np.where(np.arange(N)==0,N,0)-2*(n-2*wt)
 r=min((int(abs(z))&-int(abs(z))).bit_length()-1 for z in W if z)
 A=W//(1<<r)
 def degree(v):
  v=np.array(v,dtype=np.uint8)
  for j in range(n):
   x=v.reshape(-1,2<<j);x[:,1<<j:]^=x[:,:1<<j]
  return int(max(wt[v!=0],default=-1))
 rec={'n':n,'r':r,'amplitude_digits':[degree((A>>l)&1) for l in range(1,min(n,8))],
      'square_base4_digits':[degree(((A*A)>>(2*l))&1) for l in range(1,min(n,8))]}
 out.append(rec);print(rec)
open('/mnt/data/fei_active/exploratory/bit_carries.json','w').write(json.dumps(out,indent=2))
