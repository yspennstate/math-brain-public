SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T11:12:27Z.
attacking: the strict-N3 STAR two-channel gap — test whether the two quantitative star channels plus the surviving leaf eigenvalue force any quantitative physical rank-three cross volume, and identify the exact grouped replacement when they do not.

# account02/B19 — STAR+leaf-source does not force rank-three cross volume

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS / complementary constructions and source-valid counterexamples  
**Fresh owner control read:** `yspennstate/math-research-brain@8c376e8113908b0bc1d610da2844d1680bfb9c96`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_STRUCTURAL_IMPLICATION_REFUTED`; full QFORM remains OPEN.

The full target remains: arbitrary finite dimension, arbitrary independent real input densities bounded by one, and arbitrary real symmetric `A` with at least three actual eigenvalues of modulus at least one. No moment, support, log-concavity, Gaussianity, diagonal-coordinate, or post-rotation-independence assumption is introduced. Continuity is separate.

## 1. Incoming first gap and source pins

The immediately preceding account02/B19 theorem is

`yspennstate/math-open-problems@f13d13f2dd1d240c98505a03afebe80f64d4bf10`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T103645Z-account02-B19-QFORM-r32/REPORT.md`.

Its strict-`N3(1/256)` STAR compiler says that after the current partner supplies a physical hub `h` with

`|A_hh|<1/64`,  `sum_(j!=h) A_hj^2 > 123/4096`,

strict no-pivot control splits the leaves into two disjoint ORIGINAL-coordinate banks with star energies at least

`beta0=1711/131072`,

and the leaf principal block has at least one eigenvalue of modulus at least one. Its first unpaid analytic implication is the coupled use of those two star channels and the surviving leaf spectral source.

The current completed designated partner used here is account03/B19 r29,

`yspennstate/math-open-problems@f13d13f2dd1d240c98505a03afebe80f64d4bf10`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T090443Z-account03-B19-QFORM-r29/REPORT.md`.

It reduces its exact-rank-three residue to a hub satisfying

`|A_hh|<1/64`,  `sum_(j!=h) A_hj^2>123/4096`,

unless an earlier branch is already paid. It also records the product-safe hub small-ball estimate

`P(|Q-z|<=r) <= 4*2^(1/4) ||A[h,-h]||_2^(-1/2) r^(1/2)`.

The required Claude package is read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I use its proved ruled-surface Theorem C below, and I explicitly compute why its D/D'/D5 physical-cross-volume mechanisms cannot be forced in the family constructed here.

## 2. A target-valid strict-N3 near-coloop family

Fix `0<epsilon<=1/4` and an even integer `m>=2`. Let `R` have three orthonormal columns and rows supported on three pairwise disjoint sets of ORIGINAL coordinates as follows.

* `E1`: `m` rows `(1/sqrt(m)) e1`;
* `E2`: one hub row `sqrt(1-epsilon) e2`, plus `m` residual rows `sqrt(epsilon/m) e2`;
* `E3`: `m` rows `(1/sqrt(m)) e3`.

Thus `R^T R=I_3`. Put

`M=[[1,0,0],[0,0,1],[0,1,0]]`

and

`A=R M R^T`.

Since `R` is an isometry, the nonzero spectrum of `A` is exactly the spectrum of `M`:

`boxed: spec_nonzero(A)={1,1,-1}.`                                  (2.1)

Hence every member of the family is inside the exact QFORM target.

The only nonzero physical diagonal entries are on `E1`, and each equals `1/m`. Every physical principal-pair determinant is zero except an `E2`/`E3` pair; for such a pair with row coefficients `b,c` it is `-(bc)^2`. Therefore

`max_i |A_ii|=1/m`,

`max_(i!=j) |det A_{\{i,j\},\{i,j\}}|=(1-epsilon)/m <1/m`.          (2.2)

Consequently, for every fixed `tau>0`, every sufficiently large even `m` lies in strict `N3(tau)`.

Let `h` be the hub. Its physical diagonal is zero, while its star energy is

`boxed: sum_(j!=h) A_hj^2 = 1-epsilon >=3/4.`                      (2.3)

All this star energy goes to the `E3` bank. Split `E3` into two equal halves and put the other leaves arbitrarily between the two banks. Each bank then carries star energy

`(1-epsilon)/2 >=3/8 > beta0=1711/131072`.                         (2.4)

Thus this family satisfies the exact two-channel conclusion of the preceding B19 compiler by a wide margin.

After deleting the hub, the leaf block consists of an `E1` rank-one square of eigenvalue `1` and an `E2_res`/`E3` hyperbolic block whose nonzero eigenvalues are `+sqrt(epsilon),-sqrt(epsilon)`. Hence

`boxed: spec_nonzero(A_{-h,-h})={1,+sqrt(epsilon),-sqrt(epsilon)}.` (2.5)

In particular the promised leaf eigenvalue of modulus at least one is present exactly.

## 3. Every physical rank-three cross volume nevertheless collapses

Take **arbitrary disjoint ORIGINAL-coordinate banks** `I,J`; they need not form a full partition. Define their spectral-axis masses

`a_I=sum_(i in I cap E1)||r_i||^2`, `b_I=sum_(i in I cap E2)||r_i||^2`, `c_I=sum_(i in I cap E3)||r_i||^2`,

and analogously `a_J,b_J,c_J`.

Because the three physical ray supports are disjoint and `M` contains only the `e1-e1`, `e2-e3`, and `e3-e2` couplings, the cross block is exactly

`A[I,J]=p1 q1^T + p2 q3^T + p3 q2^T`,                              (3.1)

where the three left vectors have pairwise disjoint supports and the three right vectors have pairwise disjoint supports. Therefore its nonzero singular values are exactly

`sqrt(a_I a_J)`, `sqrt(b_I c_J)`, `sqrt(c_I b_J)`,                (3.2)

with zeros inserted when a factor vanishes. In particular

`Pi3(A[I,J]) := s1 s2 s3
 = sqrt(a_I a_J b_I b_J c_I c_J)`.                                (3.3)

For any two disjoint subbanks of a unit-mass ray,

`a_I a_J<=1/4`, `c_I c_J<=1/4`.                                  (3.4)

The `E2` ray contains one hub atom of mass `1-epsilon`; all remaining `E2` mass is only `epsilon`. Whichever of `I,J` does **not** contain the hub has `E2` mass at most `epsilon`; if neither contains it then both do. Thus

`b_I b_J<=epsilon`.                                                (3.5)

Combining (3.3)-(3.5), for every disjoint physical pair of banks,

`boxed: Pi3(A[I,J]) <= sqrt(epsilon)/4,`                           (3.6)

and, because the global rank is three,

`boxed: e_3(A[I,J]^T A[I,J]) <= epsilon/16,   e_5(...)=0.`         (3.7)

This gives the structural refutation:

### `QFORM-STAR-LEAFSOURCE-RANK3-CROSSVOLUME-FORCING-FALSE-v1`

For every `tau>0` and every `eta>0`, choose an even `m>1/tau` and

`0<epsilon<min(1/4,16 eta^2)`.

Then `A` is an exact-rank-three QFORM target in strict `N3(tau)`, it has a zero-diagonal hub with star energy at least `3/4`, two disjoint original-coordinate star channels each of energy at least `3/8`, and its leaf block has an eigenvalue exactly `1`; nevertheless

`Pi3(A[I,J])<eta`

for **every** pair of disjoint physical banks `I,J`.

So the r32 packet

`two quantitative star channels + one large leaf eigenvalue`

does **not** force a quantitative Theorem-D/D' rank-three physical cross-volume exit. Since every cross block has rank at most three, D5 is identically unavailable as well. This is a refutation of a proof mechanism, not of QFORM.

## 4. The same family is uniformly paid by the grouped product mechanism

Let

`Y1=sum_(i in E1) r_i(1) X_i`,

`Y2=sqrt(1-epsilon) X_h + sum_(i in E2_res) r_i(2) X_i`,

`Y3=sum_(i in E3) r_i(3) X_i`.

The three variables use pairwise disjoint sets of ORIGINAL independent coordinates, so they are genuinely independent. Their coefficient vectors all have Euclidean norm one. The source-valid scalar product-projection theorem gives

`||p_Yk||_infinity <= sqrt(e)`, `k=1,2,3`.                        (4.1)

The exact form is

`boxed: Q=Y1^2+2Y2Y3.`                                            (4.2)

Apply the completed account02/B06 theorem `QFORM-THIRD-SQUARE-HYPERBOLIC-ABSORPTION-v1`, canonical source

`yspennstate/math-open-problems@168ac7725f62401408f20ce18cbf8ff7055e9013`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T234200Z-e4c1068b3e5d/REPORT.md`.

Its scalar-cap form is

`||p_(aZ^2+2dUV)||_infinity <= 4 sqrt(2) L_Z sqrt(L_U L_V)/sqrt(|ad|)`.

Using `a=d=1` and (4.1),

`boxed: ||p_Q||_infinity <= 4 sqrt(2) e = 15.3769241126... .`       (4.3)

Thus the degeneration in (3.6) is entirely a degeneration of rank-three cross-volume currency. The law remains uniformly bounded because the correct payment is the whole original-product grouped packet: one independent square plus one independent hyperbolic product.

## 5. Current named partner and required Claude result applied at equations

For this family, the named partner r29 hub estimate applies with

`||A[h,-h]||_2^2=1-epsilon>=3/4`.

Hence for every `z,r>0`,

`P(|Q-z|<=r)
 <=4*2^(1/4)(1-epsilon)^(-1/4) r^(1/2)
 <=4(8/3)^(1/4) r^(1/2)
 <5.112 r^(1/2).`                                                  (5.1)

This is real partner currency, but it is not an `L^infinity` conclusion; (4.3) supplies the missing third-source payment in this model.

The required Claude `COUNTEREXAMPLE_SEARCH.md` Theorem C applies because (2.1) has signature `(2,1)` with all three nonzero eigenvalue magnitudes equal to one. On its proved one-sheet side,

`boxed: sup_(s>=0) p_Q(s) <= pi sqrt(2) = 4.4428829382... .`        (5.2)

This is an equation-level application at the exact source scope. Separately, (3.7) shows why the Claude D/D'/D5 cross-volume tools cannot be forced uniformly here: the entire three-volume is at most `epsilon/16` and the five-volume is zero.

## 6. Updated proof graph and first unpaid implication

The source-pinned assembly now says:

1. completed scalar/pair, ridge/window, D/D'/D5, diffuse F/H, semidefinite, ruled-side, rank-two-cross and grouped-coordinate exits remain paid at their exact hypotheses;
2. account03/B19 r29 reduces the current exact-rank-three residue to a quantitative small-pivot star unless an earlier exit applies;
3. account02/B19 r32 compiles a deep strict-N3 star into two disjoint quantitative original-product star channels plus at least one large leaf spectral source;
4. the theorem above proves that these three resources do **not** automatically combine into a nondegenerate rank-three physical cross block: an arbitrarily strong physical coloop can make every `Pi3` tend to zero;
5. in the model obstruction, exact original-coordinate support separation exposes the right replacement — a grouped square-plus-hyperbola packet — and pays the whole law uniformly.

Therefore the first unpaid implication is sharpened to

### `QFORM-STAR-TWOCHANNEL-LEAFSOURCE-GROUPED-DESCENT-v2`

Uniformly over the strict-N3 STAR packet

`|A_hh|<1/256`,

`||A[h,J]||_2^2, ||A[h,K]||_2^2 >=1711/131072`,

with `J,K` disjoint original-coordinate banks and `A_{-h,-h}` possessing an eigenvalue of modulus at least one, prove either

* a universal `L^infinity` bound by spending the hub and leaf curvature jointly while preserving original-product provenance, **or**
* an exact product-preserving descent to a grouped square/hyperbola, ridge/window, pair, or other already-paid packet.

One may not insert as an intermediate claim that the packet forces a fixed positive rank-three physical cross volume; Section 3 disproves that implication with all target quantifiers intact. The unrestricted higher-rank/full-N3 descent remains a separate global debt. No full-proof or continuity claim is made, and the required two independent end-to-end reviews do not exist.
