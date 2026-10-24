# B15 handoff — current FEI lower bound retires the Hod sharp target

Full FEI remains OPEN. This is a correction and a new arithmetic-remainder transfer, not an FEI proof.

The live public `teorth/optimizationproblems` record (`main` commit `9d57db86c8564cb623ec9f9e41429a34efd819fb`, `constants/71a.md` blob `d5fcdad39105d4cb594176b128119ab6f7dda9e4`) records

`C_FEI > 6.521845710923046575`

from an explicit balanced monotone n=18 seed plus O'Donnell--Tan amplification. Merged PR #94 had already certified an n=14 amplification constant `>6.4901128435` and compared it against a certified upper enclosure of the full Hod `beta(1/2)`, so `beta(1/2)` is no longer a viable conjecture for the universal sharp FEI constant. The n=18 external certificate was not independently replayed by B15 in this run; use the statement as the current curated public record, not as a new B15 certification.

New proved transfer. For any balanced Boolean seed `g` with `H(g)>0`, `I(g)>1`, put

`L(g)=H(g)/(I(g)-1)`.

O'Donnell--Tan amplification gives finite Boolean `f_m` with `H(f_m)/I(f_m) -> L(g)`. Applying the project's already-proved rare-perturbation isolation construction to each `f_m` gives explicit finite Boolean `F_{m,t}` with

`D(F_{m,t})/I(F_{m,t}) -> H(f_m)/(2 I(f_m))` as `t->infinity`.

Therefore

`lim_m lim_t D(F_{m,t})/I(F_{m,t}) = L(g)/2`.

Using the current n=18 record forces, subject to its public certificate,

`C_D > 3.2609228554615232875`.

Hence the previous B15 universal target `D <= beta(1/2) I / 2` is false, and so is the corresponding proposed all-function mesh-band target at `beta/2+epsilon` for sufficiently small epsilon. The mesh-band coarse-graining theorem itself remains valid; only its old sharp-Hod target is retired.

The unequal-magnitude and valuation/carry warnings remain intact. Isolation separates the distinguished old Fourier magnitudes into singleton packets and drives the divisibility contribution to zero; it does not assume a common mesh, tensor subadditivity, or bounded carry depth.

Next B15 target: obtain the packet/free-energy profile of the current n=18 (or merged n=14) seed and study how `2D=log N-KL(p||q)` evolves under balanced disjoint composition, retaining equal-magnitude collision and valuation-mismatch terms. This should identify which mesh-depth bands create the post-Hod excess and may suggest either a stronger lower-bound family or the correct universal payment mechanism.
