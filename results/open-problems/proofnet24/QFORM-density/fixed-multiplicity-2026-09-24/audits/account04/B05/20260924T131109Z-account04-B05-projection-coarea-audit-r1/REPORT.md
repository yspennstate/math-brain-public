SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B05, 2026-09-24T13:11:09Z.

# account04/B05 independent audit — projection densities and exceptional slices

Run: `20260924T131109Z-account04-B05-projection-coarea-audit-r1`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Owner-supplied SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

## Verdict

**PASS for the mathematical 17-eigenvalue theorem.** The product-projection lemma and all scalar/definite/hyperbolic changes of variables are valid for arbitrary rough input densities. No exceptional-slice atom or illicit pointwise trace is used downstream.

There is one nonfatal wording gap in the projection proof, repaired explicitly below. Four reproducibility files advertised by the README were absent at the inspected root; this remains a package gap, not a mathematical defect.

## Product-projection reconstruction

Source lines 256–283, Lemma `projection`.

Choose Borel representatives (0le f_ile1) everywhere. Complete (U) to an orthogonal matrix ((U,W)). For (d<n), define

[
p(y)=int_{mathbb R^{n-d}}prod_i f_i((Uy+Wz)_i),dz.
]

The orthogonal change of variables and Tonelli show directly that (p(y),dy) is the law of (U^TX); no trace on a lower-dimensional set is being prescribed.

Let (w_i^T) be row (i) of (W) and (b_i=|w_i|^2=1-|U^Te_i|^2). Rows with (b_i=0) contribute factors at most one. For (b_i>0), the vectors (v_i=w_i/sqrt{b_i}) satisfy

[
sum_{b_i>0}b_iv_iv_i^T=W^TW=I_{n-d}.
]

With

[
h_i(t)=f_i((Uy)_i+sqrt{b_i}t)^{1/b_i},
]

geometric Brascamp--Lieb and (f_i^{1/b_i}le f_i) give

[
p(y)leprod_{b_i>0}b_i^{-b_i/2}.
]

The final entropy step should be written

[
log p(y)
lerac12sum_{b_i>0}(-b_ilog b_i)
lerac12sum_{b_i>0}(1-b_i)
lerac12sum_i(1-b_i)
=rac d2.
]

The baseline sentence writes equality immediately after zero-(b_i) rows have been omitted. Under a restricted-index reading, that equality should be (le). Under an all-index reading it is already correct. This is a wording repair only; the lemma and constant (e^{d/2}) are unchanged.

When (d=n), (U) is orthogonal and the transformed joint density is (prod_i f_i((Uy)_i)), bounded by one. Scaling gives the scalar projection bound (sqrt e/|a|).

Status: **PASS WITH LOCAL WORDING REPAIR.**

## Definite-pair coarea

Source lines 422–436, Lemma `definite`.

After deterministic translation and diagonalization, the map

[
(delta,	heta)mapsto
w_0+sqrt{delta/mu_1}cos	heta,e_1+
sqrt{delta/mu_2}sin	heta,e_2
]

has absolute Jacobian (1/(2sqrt{det B})). Integrating a joint density bounded by (M) over (0le	heta<2pi) gives (pi M/sqrt{|det B|}).

The critical fiber (delta=0) is one point, hence has zero probability under an absolutely continuous planar law. The formula therefore gives the whole output law, not merely its restriction away from a possible atom.

Status: **PASS.**

## Indefinite-pair coarea and exceptional critical level

Source lines 437–493, Lemma `hyperbola`.

For each sign of (delta=z-v), the two hyperbolic charts cover the corresponding noncritical part of the plane. Direct differentiation gives Jacobian

[
left|detrac{partial w}{partial(delta,t)}ight|
=rac1{2sqrt D}.
]

The critical fiber (q^{-1}(v)) is a union of two affine lines, hence has planar Lebesgue measure zero. Therefore the pushforward has no atom at (v).

For any nonnegative Borel output test (psi), apply the two-dimensional change of variables to

[
int_{mathbb R^2}psi(q(w))f_1(w_1)f_2(w_2),dw.
]

This produces the displayed hyperbolic integral for almost every (delta). A change of either (f_i) on a one-dimensional null set changes the planar product density only on a planar null set, and therefore does not alter the test-function identity. The later one-coordinate tail substitution is an ordinary one-dimensional integral inequality using (0le f_ile1) and total mass one. Thus no arbitrary pointwise trace of a density version on a fixed hyperbola is assumed.

After conditioning on the complementary original coordinates, the translations are measurable functions of the conditioning variable. The preceding domination holds fiberwise with a uniform constant; applying it to nonnegative tests and then Tonelli yields the global measure domination. Condition-dependent exceptional output levels cause no problem.

Status: **PASS.**

## Remaining end-to-end ledger

- Lines 1–160, theorem, scaling, Fourier inversion, Riesz potential — **PASS**.
- Lines 162–255, singular values, Schur count, heat-flow BL — **PASS**.
- Lines 284–400, scalar Fourier powers, decoupling, graph determinant, crossing volumes — **PASS**.
- Lines 494–651, concentration, sampled interpolation, both rank bounds, spectral-to-volume and random cuts — **PASS**.
- Lines 652–725, singular kernels, truncated/full half potentials, pivot receivers — **PASS**.
- Lines 726–790, branch exhaustion, constants, rescaling, limitations — **PASS**.
- `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json` — **UNCHECKED/ABSENT (404)**.

## Downstream impact

The wording repair does not alter any theorem statement or constant. The rough-law projection and coarea steps are already mathematically valid when read as nonnegative test-function identities. The 17-eigenvalue theorem remains at PASS, not independently validated by this report alone. No lower (L^infty) multiplicity is certified here.
