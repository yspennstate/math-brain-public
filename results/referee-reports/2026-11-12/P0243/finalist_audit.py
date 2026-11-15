"""Reconstruct search finalists, verify at 85 digits, and check a raw DT example."""
import json, signal, time
import mpmath as mp
from precision_audit import Spectrum, row_distance, bd, fmt
signal.alarm(240)
mp.mp.dps=85
start=time.monotonic()
data=json.load(open('ratio_search_results.json'))
# A known exact family is preferable to treating floating-point pi as exact input.
s=Spectrum(4,mp.mpf('1e-10')); t=s.tau1()
birth={'n':5,'down_rate':'1','up_rate':'1e-10','tau0':fmt(s.tau0),
       'tau1':fmt(t),'ratio':fmt(t/s.tau0),
       'expm_root_residual':fmt(row_distance(mp.expm(t*s.q))[0]-mp.exp(-1))}
b=data['best']['general'];n=b['n']
x=[mp.mpf(str(v)) for v in b['meta']['parameters']]
pi=[mp.mpf(1)]+[mp.exp(v) for v in x[:n-1]]
total=sum(pi);pi=[p/total for p in pi]
q=mp.matrix(n);pos=n-1
for i in range(n):
    for j in range(i+1,n):
        c=mp.exp(x[pos]);pos+=1
        q[i,j]=c/pi[i];q[j,i]=c/pi[j]
for i in range(n):q[i,i]=-sum(q[i,j] for j in range(n) if j!=i)
scale=max(-q[i,i] for i in range(n));q=q/scale
proj=mp.matrix([pi for _ in range(n)])
z=(proj-q)**-1-proj
tau0=sum(z[i,i] for i in range(n))
# Independent root evaluation directly by matrix exponential, rather than eigendecomposition.
lo=mp.mpf(0);hi=2*tau0
for _ in range(190):
    mid=(lo+hi)/2
    if row_distance(mp.expm(mid*q))[0]>mp.exp(-1):lo=mid
    else:hi=mid
root=(lo+hi)/2
general={'n':n,'tau0':fmt(tau0),'tau1':fmt(root),'ratio':fmt(root/tau0),
         'root_residual':fmt(row_distance(mp.expm(root*q))[0]-mp.exp(-1)),
         'Q':[[fmt(q[i,j]) for j in range(n)] for i in range(n)],'pi':[fmt(v) for v in pi]}
q,pi=bd(2,mp.mpf('.01'));c=mp.mpf('.001');p=mp.eye(3)+c*q
lo=0;hi=4000
while hi-lo>1:
    mid=(hi+lo)//2
    if row_distance(p**mid)[0]>mp.exp(-1):lo=mid
    else:hi=mid
raw={'eps':'.01','c':'.001','tau0_discrete':fmt(2*(1+mp.mpf('.01'))/(1+mp.mpf('.01')+mp.mpf('.01')**2)/c),
     'tau1_raw':hi,'dbar_previous':fmt(row_distance(p**lo)[0]),'dbar_at_threshold':fmt(row_distance(p**hi)[0]),
     'sufficient_norm_bound':fmt(c*mp.mpf('2.02')**2*mp.exp(c*mp.mpf('2.02')))}
out={'birth_death':birth,'general':general,'raw_discrete':raw,'seconds':time.monotonic()-start}
with open('finalist_results.json','w') as f:json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
