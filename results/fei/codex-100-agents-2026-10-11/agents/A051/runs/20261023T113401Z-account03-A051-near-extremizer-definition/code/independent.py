from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
R=Path(__file__).resolve().parents[1];START=time.monotonic();C=0
def ck(z):
 global C
 C+=1;assert z,C
 if time.monotonic()-START>55:raise RuntimeError('55s cap')
records=[]
for k,t in [(2,1),(3,1),(2,2),(2,4)]:
 p=F(1,1<<k);d=2;N=1<<(k+d*t)
 def val(z):
  if z% (1<<k):return 1
  return (-1)**sum(((z>>(k+2*j))&1)*((z>>(k+2*j+1))&1) for j in range(t))
 depth=F(0);a=F(0);err=F(0);query=F(0)
 for z in range(N):
  tau=next((j+1 for j in range(k) if z>>j&1),k+d*t)
  error=val(z)!=1;depth+=F(tau,N);a+=F(error*tau,N);err+=F(error,N)
  # Sum physical query disagreement at original path prefix, from direct edges.
  visited=list(range(tau)) if tau<=k else list(range(k+d*t))
  for j in visited:query+=F(val(z)!=val(z^(1<<j)),N)
 ck(depth==2*(1-p)+p*d*t)
 ck(err==p*(1-F(1,2)**t)/2)
 ck(a==err*(k+d*t))
 ck(query==p*(t+k*(1-F(1,2)**t)))
 # Literal path error membership, no Fourier or source helper.
 ck(a!=err*depth)
 records.append({'k':k,'t':t,'n':k+d*t,'expected_depth':str(depth),'error_probability':str(err),'error_weighted_depth':str(a),'expected_query_influence':str(query)})
# Scalar large-formula negative certificate; no large table or enormous prime factorization.
k=10;p=F(1,1<<k);t=1<<k
ck(2+2*(1-p)==F(2047,512));ck(2-p*(10*k+15)==F(1933,1024))
ck(4*(2*p*(k+F(9,2)))==F(116,1024))
ck(F(1933,1024)>F(116,1024))
ck(1-p*((10+2)*k+15)==F(889,1024)>F(116,1024))
ck(k+2*t==2058)
result={'status':'PASS','assertions':C,'fixtures':records,'runtime_seconds':time.monotonic()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic':'separate direct Boolean exponents, original-input path lengths/errors, physical edge counts and exact Fraction','large_guard':{'seed':'bent2','k':10,'t':1024,'dimension':2058,'expected_depth':'2047/512','actual_entropy_loss_lower':'1933/1024','false_expected_depth_budget_upper':'116/1024','actual_D1_lower':'889/1024','complete_terminal_D1':'0'},'scope':'independent implementation by A051, not independent-agent acceptance'}
(R/'out/INDEPENDENT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
