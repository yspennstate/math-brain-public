# MOC4 handoff — account01/B09 simple-complex even-lift no-go

Run: `20260922T024937Z-account01-B09-MOC4-r12`  
Outcome: `CANDIDATE_REFUTED` for `MOC4-SIMPLE-COMPLEX-EVEN-LIFT-v1`; parent MOC4 remains OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Named OTHER-account input applied

Directly applied account02/B07 `MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1` / `MOC4-PAIR-HESSIAN-TRACE-v1`: if any odd-Weyl overlap is tight, the complete exterior-square channel array lies in the convex hull of the 24 even endpoint arrays. The new exact witness below violates an even-endpoint facet, so by contraposition **all odd-overlap inequalities are strict** for this true unitary.

Also consumed the lead account03/B07 `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`, account01/B08 `MOC4-BOGOLIUBOV-EVEN-LIFT-v1`, and the fresh account02/B09 `MOC4-CARTAN-POLARIZATION-v1` collar.

## New exact source-valid adversary

Use the dense rational orthogonal matrix

```text
[  636/1105,  -423/1105,   -12/65,   -772/1105 ]
[ 3576/5525,    332/5525, -144/325,  3411/5525 ]
[   164/425,     348/425,      9/25,    -96/425 ]
[      27/85,       -36/85,       4/5,       24/85 ]
```

and simple nonreal spectra

`a=(-4+4i,-i,-3+2i,-4-4i)`,
`b=(-4-4i,2-i,2-4i,4-i)`.

Exact arithmetic gives

`det(A+B)=(-82603754544-3513801072 i)/763140625`.

All 24 target vertices are distinct. The determinant has the exact positive three-vertex certificate

- `(0,1,2,3)`: `80-240i`, weight `1442439283/4637546875`;
- `(0,1,3,2)`: `64+256i`, weight `57833177464/180864328125`;
- `(0,3,1,2)`: `-416-32i`, weight `66776018624/180864328125`.

The weights sum to one and the doubled triangle area is `242688`, so the determinant is strictly inside this target triangle, hence inside the MOC4 hull.

Yet for the actual exterior-square channel array, the account01/B08 facet has

`Phi(true q)=2403485709/763140625 = 3 + 114063834/763140625`,

while every one of the 24 even endpoint channel arrays satisfies `Phi<=3`. The three target vertices used above are themselves channel-facet-tight (`Phi=3` each). Thus no positive endpoint law reproduces the true channel array, even though the target determinant has an explicit strict hull certificate using facet-tight target vertices.

This is not an MOC4 counterexample. It refutes the stronger universal coefficient/channel representation on a genuine simple-complex normal pair and shows that representation failure can coexist with strict target truth in the same datum.

## Next implication

Do not return to a universal positive even-channel lift. The first surviving obligation is maximizer-local: `MOC4-STATIONARY-FACET-PAYMENT-v1` / `MOC4-STRICT-ORIENTATION-BIRAYLEIGH-v1`. Test whether row/column bi-Rayleigh + Spin(6) stationarity + the Cartan/odd-overlap collars force structured spectral support to pay every outward even-lift facet direction. The present datum is a useful negative control: it is strict-orientation and coefficient-lift-bad, but target-safe, so a valid maximizer argument must use stationarity rather than merely true-unitary realizability.

Scientific report: `proofnet24/collective-MOC4/account01/B09/20260922T024937Z-account01-B09-MOC4-r12/REPORT.md`, creation commit `e26f7f6eef4a68e4645a308a2d1bc07d39ea3cf0`. Exact standard-library verifier and captured output are in the same immutable directory.
