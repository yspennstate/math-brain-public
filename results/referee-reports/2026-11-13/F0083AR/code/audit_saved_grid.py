"""Verify saved numerical allocations without importing or calling either solver."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import json
import pathlib
import numpy as np

root = pathlib.Path(__file__).resolve().parents[1]
metadata = json.loads((root/'data/independent_grid_results.json').read_text())
results = []
cores = {}
for record in metadata['records']:
    name, d = record['name'], record['dimension']
    raw = np.loadtxt(root/'data'/(name+'_sites.csv'), delimiter=',', skiprows=1, ndmin=2)
    centres = np.loadtxt(root/'data'/(name+'_centres.csv'), delimiter=',', skiprows=1, ndmin=2)
    sites = raw[:, :d]
    assignments = raw[:, d:].astype(int)
    assert len(sites) == record['sites']
    assert len(centres) == 1 + 2*d*record['layers']*(record['layers']+1)*(2*record['layers']+1)//6
    quota = round(record['alpha']/record['h']**d)
    for assignment in assignments.T:
        valid = assignment >= 0
        allocated_distance = np.full(len(sites), np.inf)
        allocated_distance[valid] = np.sum((sites[valid] - centres[assignment[valid]])**2, axis=1)
        for j, centre in enumerate(centres):
            held = assignment == j
            count = int(np.sum(held))
            assert count <= quota
            maximum = np.max(allocated_distance[held]) if count == quota else np.inf
            candidate_distance = np.sum((sites-centre)**2, axis=1)
            assert not np.any((candidate_distance < allocated_distance) & (candidate_distance < maximum))
    disagreement = int(np.count_nonzero(assignments[:,0] != assignments[:,1]))
    assert disagreement == record['disagreement'] == 0
    core = np.all(np.abs(sites)<1, axis=1)
    ncore = round(2/record['h'])
    cores[(d, record['layers'], record['h'])] = assignments[core,0].reshape([ncore]*d)
    results.append(dict(name=name, capacity_pass=True, blocking_pairs=0, disagreement=disagreement))
refinements = []
for d, largest, steps in [(1,12,[1/16,1/32,1/64]), (2,7,[.5,.25,.125])]:
    for coarse_h, fine_h in zip(steps,steps[1:]):
        coarse = cores[(d,largest,coarse_h)]
        for axis in range(d):
            coarse = np.repeat(coarse, 2, axis=axis)
        fine = cores[(d,largest,fine_h)]
        refinements.append(dict(dimension=d, layers=largest, coarse_h=coarse_h, fine_h=fine_h, core_disagreement_volume=float(np.count_nonzero(coarse != fine)*fine_h**d)))
output = dict(audits=results, refinement_comparisons=refinements)
(root/'data/independent_saved_audit.json').write_text(json.dumps(output,indent=2)+'\n')
print('Saved allocation audits passed:', len(results))
print(json.dumps(refinements,indent=2))
