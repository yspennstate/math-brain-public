# Commands

Executed from `/workspace/scratch/8c38fde664e1`:

```sh
python3 20261014T111508Z-fleet01-B01-global-augmented-candidate-a004/CHECK_GLOBAL_AUGMENTED.py > 20261014T111508Z-fleet01-B01-global-augmented-candidate-a004/CHECK_GLOBAL_AUGMENTED.out
python3 20261014T111508Z-fleet01-B01-global-augmented-candidate-a004/CHECK_ORBIT_LIFT.py | tee 20261014T111508Z-fleet01-B01-global-augmented-candidate-a004/CHECK_ORBIT_LIFT.out
python3 20261014T111508Z-fleet01-B01-global-augmented-candidate-a004/CERTIFY_ORBIT_LIFT.py | tee 20261014T111508Z-fleet01-B01-global-augmented-candidate-a004/CERTIFY_ORBIT_LIFT.out
```

Random seed: `20261014111508`. The exhaustive search fixes complement
symmetry and enumerates `2^(2^n-1)` truth tables for each `1<=n<=4`.

