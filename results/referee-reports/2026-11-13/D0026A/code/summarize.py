#!/usr/bin/env python3
import csv,json,math
from pathlib import Path
records=[]
for path in sorted(Path('data').glob('q*_mode*.csv')):
 rows=list(csv.DictReader(path.open()));last=rows[-1];q=float(last['q']);mode=int(last['mode']);T=float(last['time'])
 record={'q':q,'mode':mode,'T':T}
 for name,eq in [('infect0',q),('infect01',q*q),('healthy3',(1-q)**3)]:
  m=float(last[name]);se=float(last[name+'_se']);record.update({name:m,name+'_eq':eq,name+'_difference':m-eq,name+'_se':se,name+'_z':(m-eq)/se})
 for name in ['right_front','minus_left_front','ever_right','ever_minus_left','diameter']:record[name]=float(last[name]);record[name+'_se']=float(last[name+'_se'])
 if mode==0:
  # Endpoint difference of ensemble means. Times within a trajectory are correlated;
  # no standard error for this difference is claimed.
  prev=max((r for r in rows if float(r['time'])<T*.8),key=lambda r:float(r['time']))
  record['late_right_slope']=(float(last['right_front'])-float(prev['right_front']))/(T-float(prev['time']))
 records.append(record)
with open('data/summary.csv','w') as f:
 fields=list(dict.fromkeys(k for r in records for k in r));w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(records)
lines=['| q | initial law | T | P(zero at 0)-q (SE) | P(zeros at 0,1)-q² (SE) | P(healthy -1,0,1)-p³ (SE) |', '|---|---|---:|---:|---:|---:|']
for r in records:
 lines.append('| '+ ' | '.join([str(r['q']),['single seed','sparse + seed'][r['mode']],str(int(r['T']))]+[f"{r[n+'_difference']:+.4f} ({r[n+'_se']:.4f})" for n in ['infect0','infect01','healthy3']])+' |')
lines+=['','| q | T | E[R(T)] (SE), single seed | E[-L(T)] (SE) | late right slope | E[ever-right], sparse + seed |','|---|---:|---:|---:|---:|---:|']
for a,b in zip(records[::2],records[1::2]):
 lines.append(f"| {a['q']} | {int(a['T'])} | {a['right_front']:.3f} ({a['right_front_se']:.3f}) | {a['minus_left_front']:.3f} ({a['minus_left_front_se']:.3f}) | {a['late_right_slope']:.5f} | {b['ever_right']:.3f} ({b['ever_right_se']:.3f}) |")
Path('data/results_table.txt').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines));print('max final |z|',max(abs(r[n+'_z']) for r in records for n in ['infect0','infect01','healthy3']))
# Bound for influence from the discarded exterior to the local support at |x|<=1.
n=24000;T=4000
print('log clock-path bound',math.log(3)+n*math.log(2*math.e*T/n)-math.log(1-2*T/(n+1)))
