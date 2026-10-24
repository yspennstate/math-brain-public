SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B13, 2026-09-23T00:05:55Z.
attacking: counterexample normal form for the no-pivot finite-grid extreme-product class using D'/D5 cross-volume certificates and exact low cross-rank completion.

# account02/B13 handoff — QFORM r15

Status: **PROVED TARGET-LEVEL COUNTEREXAMPLE NORMAL FORM + EXACT SUPPORTING LINEAR-ALGEBRA LEMMA / FULL QFORM OPEN / CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

Fresh control was resolved before the run and refreshed before publication; OWNER CONTROL revision remained `2026-09-22.15`, QFORM-only, with no account02/B13 stop observed. The live correction inbox was reread and no refuted conditional-density/coarea/rotation/localization premise was used.

Canonical mathematics bundle: `yspennstate/math-open-problems@d59fc91cdb6c772a0b3c73ba5b90fb62e10e3bf`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T000555Z-account02-B13-productset-r15-482fba/`. The report and checker output were read back. Checker terminates `QFORM_B13_R15_CHECK_PASS`.

## New target-level normal form

Apply designated partner account03/B13 r19, `math-open-problems@d21000e145ff5e4756c0abc8727a7c7aa1a02e4d`, which proves exact equality between the no-pivot arbitrary-law slab supremum and a rational finite-grid extreme-product supremum, using finite-mixture approximation rather than an attained global bathtub optimizer.

Then apply the required Claude-attributed `D'` and `D_5` theorems from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md`. Let

`C3=9 sqrt(3e)=25.701021075349...`, `C5=5 sqrt(2e)=11.658219907985...`.

Subject to the current supplied full-to-no-pivot reduction (`math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `GEOMETRIC_SYNTHESIS.md`), if full QFORM is false then for every integer `m>=2` there is a rational finite-grid product-indicator witness with slab ratio `>C3 m`, `s_3(A_m)>1`, and strict no-`m^-4`-pivot inequalities. Hence

`max_ij |A_{m,ij}| < sqrt(2) m^-2`,

and because three singular values exceed one,

`n_m > sqrt(3/2) m^2`.

For every disjoint original-coordinate cut `M=A_m[I,J]`, `D_5` forces

`s_5(M) < (C5/C3)/m < 1/m`.

Thus every physical cross block is asymptotically rank at most four in operator norm. Moreover, if `s_3(M)>=1/m`, then `D'` at `h=2/3`, applied to `M` and `M^T`, forces a row volume marginal `alpha_i>2/3` and a column volume marginal `beta_j>2/3`. Therefore the volume-sampling law on squared `3x3` minors puts mass `>1/3` on minors containing the same physical row and column. At most four rows and four columns can be heavy because the marginals each sum to three.

This is a real inequality-level application of `D'`/`D_5`, with original-coordinate product provenance preserved and no support/fragment bound.

## Exact endpoint theorem

New lemma `QFORM-DISJOINT-CROSSRANK-COMPLETION-v1`: if a finite symmetric matrix satisfies `rank A[I,J]<=r` for every disjoint coordinate pair `I,J`, then

`A=D+R`, with `D` diagonal, `R` symmetric, and `rank R<=4r`.

Proof: choose a maximal invertible disjoint `r x r` pivot `B=A[P,Q]`; vanishing `(r+1)x(r+1)` disjoint cross minors give the exact off-diagonal Schur identities on the remaining coordinates. The symmetric block `H=[[0,2B],[2B^T,0]]` produces a rank-`2r` Nyström completion matching every off-core off-diagonal entry; a second symmetric correction supported on the `2r`-coordinate core has rank at most `2r`. Their sum matches all off-diagonal entries, leaving a diagonal remainder.

The deterministic checker ran 240 seeded diagonal-plus-rank test systems; maximum reconstruction error was `7.194e-14`, and all reconstructed ranks obeyed `rank R<=4r`.

## First unpaid implication

`QFORM-NOPIVOT-CROSSRANK4-STABILITY-v1`: upgrade the exact completion theorem to a dimension-free quantitative/product-compatible statement strong enough for the finite-grid no-pivot witnesses, or construct a diverging finite-grid sequence satisfying the normal form. Raw small-matrix perturbation is not a valid substitute because supports may be arbitrarily remote and fragmented.

Full QFORM remains **OPEN**. Continuity remains **OPEN**.
