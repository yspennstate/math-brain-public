# fleet02/B10 full audit — constants, arithmetic, adversarial finite examples

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Fresh master observed before publication: `dab87716858e08fcf071327812f6091525cb590b`. Mathematical baseline audited byte-identically to the pinned source: initial commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, `manuscript.tex` git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, owner-recorded SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes / 790 lines. I read the complete manuscript and the complete package README, DELIVERY_STATUS, SOURCE_MANIFEST, AUDIT, proof_map, verify.py and checks.json. This report is my own reconstruction; peer PASS reports were not used as substitutes for the baseline audit.

## Verdict

**PASS** for the pinned seventeen-direction theorem. I found no fatal mathematical gap in the 790-line argument. The theorem proved by this baseline is the stated arbitrary-product-law result under `s_17(A)>=s>0`; it does **not** prove the unrestricted three-eigenvalue conjecture.

Two nonfatal improvements/issues were found:

1. **PASS / constant sharpening.** The pivot calculation gives an exact smaller final constant. The scalar-pivot truncated half-potential is `200+120 log 16`, so the full half-potential is at most `201+120 log 16`; hence the scalar branch is `2010+1200 log 16 = 5337.106466687737... < 5338`, not merely `6010`. All other branches are smaller. This changes no hypothesis.
2. **GAP (presentation only, repaired in the separate nine-direction replacement).** In the newer grouped-Hoelder threshold-nine compiler, indices with inclusion marginal `alpha_i=0` must be dropped before writing powers `1/alpha_i`; their Fourier factors are at most one. With this explicit convention the proof is valid. This gap is not in the pinned 17-direction manuscript itself.

## Package / reproducibility audit

- `README.md`: **PASS**. It identifies the exact 790-line self-contained source and correctly separates source delivery, compiled PDF delivery and review status.
- `SOURCE_MANIFEST.json`: **PASS**. It pins blob `183ccd...`, SHA-256 `9f3b...`, source size/lines, support-file hashes and build limitations.
- `AUDIT.md`: **PASS as historical self-report only**. Its historical finite-check counts are explicitly not asserted to be reproduced by the newer checker.
- `proof_map.csv`: **PASS**. Every listed statement/proof range agrees with the manuscript ranges used below.
- `verify.py`: **PASS as finite diagnostics, not proof**. It pins the source SHA, checks the exact `297/2800` diagonal-dominance slack, exact interpolation support/rank identities, and independent numerical Schur/graph diagnostics. I found no code-level assertion that overclaims mathematical universality.
- `checks.json`: **PASS** against the supplied checker result: 534 exact interpolation seeds, 18 exact volume-sampling cases, 9 strict cases, 240 Schur threshold cases and 30 graph-weight cases. The difference from historical self-audit counts is documented and is not an inconsistency.

## End-to-end source audit

Statuses below cover the entire mathematical source by contiguous section/range; no mathematical range is left UNCHECKED.

### Lines 35--83: theorem, quantifiers, architecture

**PASS.** The singular-value convention is correct for symmetric matrices. The theorem keeps arbitrary independent real coordinate densities bounded by `K`, arbitrary symmetric `A`, all signatures, arbitrary affine `b,c`, and makes only an essential-density claim. The normalized parameters are exactly `eta=1/100`, `kappa=1/80^2`. The scaling at the end correctly produces `K^2/s`.

### Lines 91--160: Fourier identities, power envelope, negative half moments

**PASS.** With `hat f(t)=int e^{itx}f(x)dx`, Plancherel has factor `2pi`, inversion `1/(2pi)`, and the Gaussian identity is normalized correctly. The Riesz calculation uses

`int_0^infty v^(-5/4) exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4)|t|^(-1/2)`,

so the prefactor `1/sqrt(2pi)` is correct. For the `3/4` envelope the weighted integral is exactly `12 sqrt(u)`, yielding the stated half-potential bound.

### Lines 169--217: perturbation, Schur count, diagonal dominance

**PASS.** The singular-value approximation formula justifies both nonsymmetric perturbation statements. In the invertible Schur argument, inverse eigenvalues with modulus `>1/t` correspond exactly to original eigenvalues with modulus `<t`; taking complements gives `N_S(t)>=N_A(t)-k`. The singular-matrix epsilon limiting argument preserves the non-strict threshold. Strict diagonal dominance is valid without symmetry.

### Lines 221--301: geometric BL, projection density, scalar Fourier powers

**PASS.** The heat-flow derivative is

`partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`

by the frame contraction. The large-time Gaussian normalization and small-time Lebesgue-point/Fatou limit are correct. In the product-projection lemma the complement-row weights `b_i=1-|U^Te_i|^2` form the needed frame; `-b log b<=1-b` gives the dimension-free cap `e^(d/2)`. No rotated-coordinate independence is asserted. For scalar Fourier powers, `m=floor(p/2)>=p/4` and the projection bound at the origin gives exactly `2pi sqrt(2e)/sqrt(p)`.

### Lines 310--400: decoupling, regularized determinant, crossing volumes

**PASS.** The second and fourth-power decouplings use only independent original coordinates and copies. In the determinant proof, with `a=2t`, `alpha=(2pi e)^2`, the BL weights satisfy the exact frame and the `d_i` powers cancel. The theta factor is exactly neutralized by the chosen regularizer, leaving

`|phi_Z(t)| <= det(I+t^2 M^TM/(pi^2 e^2))^(-1/8)`.

Cauchy--Binet gives the stated `Z_k`. Retaining one order gives `u_k=pi e Z_k^(-1/(2k))`; `k=5` yields `5e Z_5^(-1/10)` for density and `k=3` yields `12 sqrt((e/2) Z_3^(-1/6))` for the negative half moment.

### Lines 404--482: square, definite pair, hyperbolic pair

**PASS.** The square profile has the correct two inverse branches and interval-preimage length. The definite-pair `(delta,theta)` Jacobian is `1/(2 sqrt(det B))`, hence the density cap `pi M/sqrt(|det B|)`. The hyperbolic parametrization has Jacobian `1/(2 sqrt D)` per branch. The tail change of variables is legitimate with rough cap-one laws; the worst half-line mass-one integral gives `3 log 2`. The middle interval and `Lambda>=2/sqrt D` produce the final `6+log_+(16 sqrt D/|z-v|)` envelope. A tail may select a different original coordinate after swapping `u,w`; this is harmless and no post-rotation independence is used.

### Lines 485--525: quarter-power concentration and logarithmic potential

**PASS.** In the diagonal case the conditional small-ball bound is `4 sqrt(rho/L)`. In the off-diagonal case the sign cut produces a literal crossing block of norm at least `L/4`, and the determinant theorem gives the `|t|^(-1/4)` envelope. At `v=1/8` the exact coefficient is

`2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)<16`.

Layer cake gives exactly `L_0=4+4 log 16` and excludes atoms.

### Lines 528--645: pivot-volume definition, sampling, completion, no-pivot spectral-to-volume, cut

**PASS.** The no-pivot entry estimate is valid because `eta^2+eta=0.0101<1/49`, hence every off-diagonal entry is `<1/7`. In volume sampling, the bordered determinant identity is exact for nonsingular seeds; singular seeds may have nonsingular extensions, so the manuscript correctly uses an inequality rather than equality. The nonsymmetric interpolation has rank at most `r`, agrees on rows `S` and columns `T`, and the completion satisfies

`rank R<=3r`, `R_LL=P_LL`, `rank R_LL<=r`, `D=0` on the seed, `diag E=0`.

The support decomposition proving `rank R<=3r` is valid. In the bad-ratio branch, `epsilon<=(r+1)/80<=1/16`, `m=4k-3>=4r+1`, so at least `r+1` large diagonal entries of `D` lie in `L`. The exact row-dominance arithmetic is

`371/400 - 4(1/7+1/16) = 371/400-23/28 = 297/2800 >0`.

Therefore the `(r+1)x(r+1)` restricted block is invertible, contradicting `rank R_LL<=r`. The fair cut contributes exactly probability `4^(-k)` for each ordered disjoint pair. Consequently `Z_k^(-1/(2k))<=160`; the resulting `k=3` half potential is `<200` and `k=5` density is `<2400`.

### Exact adversarial finite stress test for the interpolation ranks

**PASS / route-sharpness witness.** The following symmetric integer matrix with seed `S={1,2}`, `T={3,4}` (one-based) makes the completion's two rank bounds simultaneously sharp:

```
A =
[-1 -1 -1 -1  0 -1]
[-1 -1  1 -1  1  0]
[-1  1  1  1 -1  1]
[-1 -1  1  0  0  1]
[ 0  1 -1  0  0 -1]
[-1  0  1  1 -1 -1]
```

Here `B=A[S,T]=[[-1,-1],[1,-1]]`, `det B=2`. With the manuscript definitions `P=A[:,T]B^{-1}A[S,:]`, `E=off(A_LL-P_LL)`, `D=diag(A-P)` on `L={5,6}`, `R=A-D-E`, exact rational arithmetic gives

`rank P=2`, `rank R=6=3r`, `rank R_LL=2=r`,

`D_55=1/2`, `D_66=-2`, and

`R_LL=[[-1/2,-1/2],[0,1]]`, which is invertible.

Thus neither the global `3r` nor restricted `r` rank bound can be lowered merely by re-reading the support argument. This is an adversarial witness for the proof interface, not a counterexample to any fixed-multiplicity theorem (it is not asserted to satisfy the full no-pivot / spectral hypotheses).

### Lines 654--724: singular kernels, pivot half-potential, nine-direction half-potential

**PASS.** The kernel inequalities are correctly normalized; the logarithmic-kernel worst overlap occurs at coincident centers and integrates to `8`. Scalar pivot gives the exact sharper value

`H(Q)<=10(20+12 log 16)=200+120 log 16=532.7106466687...`.

Definite pair gives `<160`; indefinite pair gives

`10(32+4 log 16)+4/e=432.3750666542...<444`.

Hence Proposition 6.3's `H<=600` is valid but deliberately coarse. The full half-potential is at most `201+120 log16` in the pivot case and `<200` in the no-pivot case.

### Lines 726--790: main theorem, scaling, threshold accounting, limitations

**PASS.** No-pivot `s_17` gives `<2400`. A scalar pivot leaves at least sixteen Schur directions and therefore enough for the nine-direction half-potential result; with the exact constant above it gives

`||p_Q||_infinity <= 2010+1200 log16 = 5337.1064666877... <5338`,

which improves the printed `6010`. A definite pair gives `10pi<32` (and certainly `<40`). The indefinite pair gives

`10(10+5 log16)+1/e=238.9973155531...<251`.

The scaling `Y=KX` and `Q=(s/K^2)Qtilde` is exact. The limitation statements correctly do not claim threshold optimality or the three-eigenvalue conjecture.

## Baseline dependency map

`BL heat flow -> projection cap -> scalar Fourier powers -> decoupling -> crossing determinant -> volume envelopes`;

`sampling + nonsymmetric completion + rank perturbation + diagonal dominance -> no-pivot V_3/V_5`;

`random physical cut -> no-pivot half-potential/density`;

`square / definite / hyperbolic coordinate pivots + Schur spectral count + quarter-power logarithmic control -> pivot branches`;

`these four exhaustive branches + scaling -> Theorem 1.1`.

Every conditioning step is on original independent coordinates. Deterministic rotations are used only for Jacobians/projection geometry.

## Threshold-lowering obligation after this audit

The baseline is sound. A complete threshold-nine replacement is written separately in this run. The current order-three structural route has a real bookkeeping endpoint at eight directions: at the worst bad-ratio seed `r=2`, `rank R<=6` and `rank R_LL<=2`; `s_8` can force only two large diagonal residual coordinates, compatible with an invertible rank-two restricted block. Nine forces three and closes the contradiction. This is a route obstruction, not a counterexample to an eight-direction theorem. Also, an order-two crossing bound alone cannot be a bounded-density endpoint: if `U,V` are independent Uniform[-1,1], the density of `U^2-V^2` has a logarithmic singularity at zero. Any proof below nine must exploit additional structure before reducing to a generic rank-two indefinite quadratic.
