import json,time,random,math
from pathlib import Path
import mpmath as mp
from symmetric import evaluate,integer_data
mp.mp.dps=100
start=time.monotonic();records=[];maxerr=0.
for n in [25,64,256,1024,2000]:
 row=json.loads(Path(f'thresholds_{n:04d}.json').read_text())
 for name in ['B/I','Gamma/I']:
  r=row['maxima'][name]['threshold'];f=[1 if t<r else -1 for t in range(n+1)]
  v=evaluate(f,90);v2=evaluate(f,130)
  error=abs(float(v[name])-row['maxima'][name]['value']);maxerr=max(maxerr,error)
  assert error<1e-10
  assert abs(v[name]-v2[name])<mp.mpf('1e-75')
  assert abs(v['Gamma']-(v['H']/2+(1-mp.mpf(integer_data(f)[0][0])**2/mp.mpf(2)**(2*n))*mp.log(v['I']/n,2)))<mp.mpf('1e-75')
  records.append({'n':n,'family':'threshold','threshold':r,'objective':name,'value':mp.nstr(v[name],70),'binary64_error':error})
  print('threshold',n,name,error,flush=True)
for n in [25,128,512,2000]:
 row=json.loads(Path(f'parity_thresholds_v3_{n:04d}.json').read_text())
 for name in ['B/I','Gamma/I']:
  r=row['maxima'][name]['threshold'];f=[(1 if t<r else -1)*(-1)**t for t in range(n+1)]
  v=evaluate(f,100);error=abs(float(v[name])-row['maxima'][name]['value']);maxerr=max(maxerr,error)
  assert error<1e-10,(n,name,error)
  records.append({'n':n,'family':'parity times threshold','threshold':r,'objective':name,'value':mp.nstr(v[name],70),'binary64_error':error})
  print('parity threshold',n,name,error,flush=True)
for n in [24,64,256,1024,2000]:
 row=json.loads(Path(f'hill_{n:04d}.json').read_text())
 for s in row['searches']:
  f=[1 if t=='+' else -1 for t in s['value_vector']];v=evaluate(f,100)
  for name in ['A/I','B/I','Gamma/I']:
   error=abs(float(v[name])-s['final'][name]);maxerr=max(maxerr,error);assert error<1e-10,(n,name,error)
  records.append({'n':n,'family':'bounded hill climbing','objective':s['objective'],'value':mp.nstr(v[s['objective']],70),'I':mp.nstr(v['I'],50)})
  print('hill',n,s['objective'],flush=True)
# Attempt to break the new analytic steps on structured and random symmetric functions.
rng=random.Random(8601);tested=0
for n in [5,16,24,32,64,128,256]:
 for rep in range(12):
  f=[rng.choice([-1,1]) for _ in range(n+1)];v=evaluate(f,45)
  rows=integer_data(f)
  D=sum(mp.mpf(math.comb(n,k))*F*F/mp.mpf(2)**(2*n)*mp.log(math.comb(n,k),2) for k,(F,L,Q,N) in enumerate(rows) if F)
  assert D<=3*v['I']+mp.mpf('1e-35')
  assert v['B']<=mp.mpf('3.463')*v['I']+mp.mpf('1e-35')
  assert v['Gamma']<=v['B']/2+mp.mpf('1e-35')
  tested+=1
Path('large_high_precision.json').write_text(json.dumps(records,indent=2)+'\n')
print('random_symmetric_functions_analytic_checks',tested)
print('maximum_float_error',maxerr)
print('wall_seconds',time.monotonic()-start)
