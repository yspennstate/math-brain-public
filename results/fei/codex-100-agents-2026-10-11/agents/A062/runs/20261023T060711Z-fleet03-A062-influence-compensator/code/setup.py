from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1];a=r.parents[1]
assert a.name=='A062'
(r/'out').mkdir(exist_ok=True)
old=a/'runs/20261023T015047Z-fleet03-A062-influence-compensator'
for name in ['kernel.py','check.py']:(r/'code'/name).write_bytes((old/'code'/name).read_bytes())
spec={'helper':'A062-block-reference-v1 plus byte-copied A062-sparse-reference-v2 interval helper','family':'disjoint products of point defects; separately one-point perturbations create actual coupled Boolean laws','block_families':[[2,2],[2,3],[2,4],[3,3],[3,4],[4,4],[2,3,4]],'original_reference_choices':'each block independently uses product empty tilt or actual-source empty tilt, delta=d_original','block_root_count':32,'profile_state_count':868,'symmetry':'within-block coordinate permutation and signs; inactive blocks have actual/reference point mass at empty; all active coordinate choices physically checked on root and first-child profiles','arithmetic':'integer Walsh, direct Boolean edges, Fraction normalized actual physical kernels; outward 70-bit log bounds with 28-term atanh tail and 64-bit mantissa bracketing; no float sign tests','coupled_families':[[2,3],[3,3],[3,4]],'coupled_flip_points':'0,1,2^firstwidth,1+2^firstwidth; all four distinct','coupled_original_references':['actual coordinate-product reference','product of actual block references with actual-source empty mass and lambda=1'],'coupled_root_count':24,'coupled_child_rows':296,'coupled_scope':'every root coordinate, both physical outcomes; actual inherited R retained; product of reference block marginals used only as analytic comparison, never a reset','pilot':'block widths2,3 with all four empty-tilt choices; coupled widths2,3 flip1 both references and all query outcomes','memory_estimate_MB':100,'max_runtime_seconds_per_job':55,'no_automatic_escalation':True,'adversarial_checks':['global common-attenuation failure at first active query in width3 block of widths3,4 product root','reference nonfactorization and signed coupling tax after a physical query of perturbed products','generic affine theorem guard F=(-1)^(v*y0*y1*y2), core1, Q=pF; zero core reserve fails']}
# 4 references for each two-block family, 8 for the three-block family.
assert 6*4+8==32
assert 4*(9+12+15+16+20+25)+8*60==868
# Every coupled family has four flips, two references and 2*n query rows.
assert sum(4*2*2*sum(w) for w in spec['coupled_families'])==288
spec['coupled_child_rows']=288
(r/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
(r/'out/INHERITED_HELPERS.json').write_text(json.dumps({'source_run':str(old),'copied':{name:hashlib.sha256((r/'code'/name).read_bytes()).hexdigest() for name in ['kernel.py','check.py']}},indent=2)+'\n',encoding='utf-8')
(a/'STATUS.md').write_text('STATE: A062 stage19 IN_PROGRESS: testing blockwise sharp signed projection and exact coupling tax after an unequal-row query; prior stage18 locally checked; full FEI OPEN.\nNEXT: Verify all-interleaving original-reference block invariant; break it with actual one-point-coupled Boolean controls; save exact unpaid signed tax.\n',encoding='utf-8')
print('Frozen32 product roots/868 profiles and24 coupled roots/288 child rows; helpers pinned.')
