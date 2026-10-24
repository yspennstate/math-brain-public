from pathlib import Path
import json
p=Path('ATTEMPT.md')
s=p.read_text(encoding='utf8')
x=json.loads(Path('experiment_results.json').read_text())
s+='''
## 6. Reproducible finite computations

`experiment.py` uses a full red-blue distance matrix and processes edges in increasing order, accepting an edge if both endpoints are still unused. On a finite balanced configuration this produces a perfect stable matching: an omitted edge had an endpoint already matched via a no-longer edge; with strict preferences this rules out blocking. For the continuous torus samples ties occur with probability zero. Independently, after construction all red-blue pairs were checked for the two strict blocking inequalities.

Integer chain tests used n=2,3,5,10,30, asserting the complete predicted partner array, final edge length 8n-3, and zero blocking pairs.

The random tests used n=2048 red and 2048 blue independent uniform points on a flat torus of volume n, in dimensions 2 and 3, seeds 8100+100*d+seed with seed=0,1,2,3. This is a pair of balanced binomial processes, not independent Poisson counts and not infinite Euclidean space. For partitions into k^d cubes, k=4,8,16, the residual threshold was r=sqrt(d)*L/k. Every cube was checked for no coexistence of residual colours, and the global exact sum identity sum|D|=2*number of long red edges was checked. All assertions passed. Finite-size effects are particularly severe for k=4, where r is a substantial fraction of the torus diameter.

Average descriptive results over four replicates:

| d | k | r | tail | E D^2 / cube volume | E D^4 / volume squared |
|---|---|---|---|---|---|
'''
for d in [2,3]:
 for k in [4,8,16]:
  rows=[a for a in x['results'] if a['kind']=='torus' and a['dimension']==d and a['k']==k]
  avg=lambda key:sum(a[key] for a in rows)/len(rows)
  s+=f"| {d} | {k} | {rows[0]['r']:.6f} | {avg('tail'):.8f} | {avg('second_moment_per_volume'):.8f} | {avg('fourth_moment_per_volume_squared'):.8f} |\n"
s+=f'''
Runtime: {x['elapsed']:.2f} seconds. Raw results: experiment_results.json. Distance matrices have 2048^2 double entries (32 MiB); sorting indices and auxiliary arrays keep this job's planned array allocation comfortably below 1 GB. No empirical exponent is estimated from these six scales, and no uniform moment bound is inferred.

## 7. Lean scope

ResidualChecks.lean formalizes five finite arithmetic lemmas: residual one-colour count addition, the internal chain distance, both competing-distance lower bounds, and the endpoint length. It does not formalize Campbell's theorem, Hölder, stability of the whole finite matching, or the infinite Poisson conjecture. The handwritten proofs above are the source for those claims. Only the narrow imports Mathlib.Data.Int.Basic and Lean.Elab.Tactic.Omega are used; no sorry or native_decide. The final compile result is recorded in lean_check.log.

The initial compile attempts exposed missing Mathlib.Tactic.Omega and shell encoding/BOM issues, all local to the input/imports. The final check uses the core Omega module and a UTF-8 file without BOM. The wrapper gives a 3600-second subprocess timeout, as requested for shared Lean checking, and runs only one Lean process at a time. All actual invocations completed well below ten minutes.
'''
p.write_text(s,encoding='utf8')
q=Path('CLAIMS.jsonl')
with q.open('a',encoding='utf8') as f:f.write(json.dumps(dict(problem_id='F0081',claim='Eight balanced finite-torus samples in dimensions 2 and 3 pass exhaustive stability checks and residual monochromatic/count identities at three thresholds each.',status='numerical_evidence',proof_location='ATTEMPT.md §6; experiment.py; experiment_results.json',remaining_gap='Balanced finite binomial torus samples do not establish the infinite Poisson tail or uniform growing-window moment bounds.',checks='All assertions passed; chain checks n=2,3,5,10,30 also passed.'))+'\n')
print('Appended experimental record')
