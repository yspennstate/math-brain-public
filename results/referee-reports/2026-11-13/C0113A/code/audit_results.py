"""Independently recompute numerical summaries from saved pair observations."""
import csv,json,math,hashlib,datetime
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=[json.loads(s) for s in (ROOT/'data/observations.jsonl').read_text().splitlines()]
bykey={(r['d'],r['replicate'],r['expected_n'],r['boundary']):r for r in rows}
pairs=defaultdict(list)
with (ROOT/'data/pair_observations.csv').open() as f:
 for p in csv.DictReader(f):
  key=(int(p['d']),int(p['replicate']),int(p['expected_n']),p['boundary'])
  row=bykey[key]
  assert float(p['distance'])>=row['side']/3-1e-12
  p['core_connected']=int(p['core_connected'])
  p['wired_core_connected']=int(p['wired_core_connected'])
  p['wired_whole_box_connected']=int(p['wired_whole_box_connected'])
  assert p['wired_core_connected']<=p['core_connected']
  assert p['wired_core_connected']<=p['wired_whole_box_connected']
  pairs[key].append(p)
for key,row in bykey.items():
 ps=pairs[key]
 assert len(ps)==row['far_pair_count']==64
 for field,raw in [('far_core_fraction','core_connected'),('wired_far_core_fraction','wired_core_connected'),('wired_whole_box_far_fraction','wired_whole_box_connected')]:
  assert math.isclose(row[field],sum(p[raw] for p in ps)/len(ps),abs_tol=1e-14)
 assert row['max_mst_edge']<row['radius']
 assert row['full_connected']
 assert math.isclose(row['fixed_root_distance'],math.dist(*row['fixed_root_coordinates']),abs_tol=1e-12)
 assert row['fixed_inner_connected']==(row['fixed_path_radius']<=row['fixed_inner_side']/2)
for d in (3,4,5):
 for rep in range(16):
  seq=[bykey[d,rep,n,'free'] for n in (1024,4096,16384,65536)]
  assert all(a['n']<b['n'] for a,b in zip(seq,seq[1:]))
  assert all(a['fixed_inner_connected']>=b['fixed_inner_connected'] for a,b in zip(seq,seq[1:]))
  assert all(a['wired_fixed_inner_connected']<=b['wired_fixed_inner_connected'] for a,b in zip(seq,seq[1:]))
  assert all(a['wired_whole_box_fixed_connected']<=b['wired_whole_box_fixed_connected'] for a,b in zip(seq,seq[1:]))
  assert all(a['fixed_root_coordinates']==b['fixed_root_coordinates'] for a,b in zip(seq,seq[1:]))
  for n in (1024,4096,16384,65536):
   free=bykey[d,rep,n,'free'];periodic=bykey[d,rep,n,'periodic']
   assert periodic['far_core_fraction']<=free['far_core_fraction']
   for a,b in zip(pairs[d,rep,n,'free'],pairs[d,rep,n,'periodic']):
    assert (a['i'],a['j'],a['distance'])==(b['i'],b['j'],b['distance'])
    assert b['core_connected']<=a['core_connected']
with (ROOT/'data/summary.csv').open() as f:
 summaries=list(csv.DictReader(f))
for s in summaries:
 key=(int(s['d']),int(s['expected_n']),s['boundary'])
 group=[r for r in rows if (r['d'],r['expected_n'],r['boundary'])==key]
 xs=[r['far_core_fraction'] for r in group];mean=sum(xs)/len(xs)
 variance=sum((x-mean)**2 for x in xs)/(len(xs)-1)
 # Tabulated 0.975 Student-t quantile for 15 degrees of freedom.
 half=2.131449545559323*math.sqrt(variance/16)
 assert math.isclose(mean,float(s['mean_far_core_fraction']),abs_tol=1e-14)
 assert math.isclose(max(0,mean-half),float(s['replicate_t95_low']),abs_tol=1e-12)
 assert math.isclose(min(1,mean+half),float(s['replicate_t95_high']),abs_tol=1e-12)
metadata=json.loads((ROOT/'data/run_metadata.json').read_text())
assert metadata['nice']>=10 and metadata['numerical_threads']==1
assert metadata['peak_rss_bytes']<4_000_000_000
result={'status':'PASS','audit_time':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'observations':len(rows),'pair_observations':sum(map(len,pairs.values())),
 'summary_rows':len(summaries),'independent_realizations':48,
 'checks':['raw pair counts reproduce every reported fraction',
 'Student-t intervals independently recalculated with tabulated critical value',
 'paired free/periodic interior inclusion and wired lower bounds',
 'fixed-root identity, path-radius confinement, nested-window monotonicity',
 'finite-metric MST radius certificate on all 384 graphs',
 'recorded nice/thread/RSS bounds'],
 'source_code_sha256':hashlib.sha256((ROOT/'code/poisson_msf.py').read_bytes()).hexdigest()}
(ROOT/'data/audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
