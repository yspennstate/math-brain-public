"""Finite regression tests for the proved balanced-block Bcan identity."""
import json
from pathlib import Path
import numpy as np
from cancellation_composition import walsh_state, variable, and_state, validate


def tests(seed=610219, trials=100):
    rng=np.random.default_rng(seed)
    maxima=np.zeros(3)
    for rep in range(trials):
        outer=rng.choice([-1,1],8).astype(np.int64)
        inner=np.ones(8,dtype=np.int64)
        inner[rng.choice(8,4,replace=False)]=-1
        # Nine independent input bits: three disjoint three-bit copies.
        x=np.arange(512,dtype=np.int64)
        outer_index=np.zeros(512,dtype=np.int64)
        for i in range(3):
            outer_index |= ((inner[(x>>(3*i))&7]==-1).astype(np.int64)<<i)
        result=outer[outer_index]
        o,g,r=map(walsh_state,[outer,inner,result])
        pred=np.array([o.entropy+o.influence*g.entropy,
                       o.cancellation+o.influence*g.cancellation,
                       o.influence*g.influence])
        actual=np.array([r.entropy,r.cancellation,r.influence])
        maxima=np.maximum(maxima,np.abs(pred-actual))
        assert np.max(np.abs(pred-actual)) < 1e-11
    return {'balanced_block_identity_trials':trials,'seed':seed,
            'outer_functions':'arbitrary Boolean functions on three bits',
            'inner_functions':'balanced Boolean functions on three bits, disjoint copies',
            'composition_dimension':9,
            'max_errors_H_Bcan_I':maxima.tolist(),
            'scope':'finite regression; complete algebraic proof is in REPORT.md'}

if __name__=='__main__':
    out={'and_or_composition':validate(), 'balanced_block_composition':tests()}
    (Path(__file__).resolve().parent/'composition_test_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
