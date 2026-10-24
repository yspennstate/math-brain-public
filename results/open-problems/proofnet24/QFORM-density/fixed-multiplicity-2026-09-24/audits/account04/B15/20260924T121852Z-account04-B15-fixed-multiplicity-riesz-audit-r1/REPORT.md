SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B15, 2026-09-24T12:18:52Z.

# account04/B15 independent fixed-multiplicity audit

Run: `20260924T121852Z-account04-B15-fixed-multiplicity-riesz-audit-r1`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned SHA-256 supplied by the owner objective: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Current-master readback: the same 790-line source blob.

## Verdict

**PASS for the mathematical 17-eigenvalue baseline, with one nonfatal wording gap and one repository-package gap.**

I read the complete pinned `manuscript.tex` and reconstructed the full dependency chain. I found no fatal mathematical defect in

[
s_{17}(A)ge s>0
quadLongrightarrowquad
|p_{X^TAX+b^TX+c}|_inftyle 10^4 K^2/s
]

for independent arbitrary real coordinate densities bounded by (K), arbitrary real symmetric (A), arbitrary signature and remaining spectrum, and arbitrary affine terms.

This is one independent worker audit, not formal verification or a release certificate. The three-eigenvalue conjecture remains open.

## Findings

### B15 focal chain: Gaussian inversion and Riesz half-potential — PASS

Source lines 91–160.

With (widehat f(t)=int e^{itx}f(x),dx), the manuscript's constants are consistent:

[
mathbb E e^{-v(Z-a)^2}
=
rac{1}{2sqrt{pi v}}
int_{mathbb R}e^{-t^2/(4v)}e^{-ita}phi_Z(t),dt.
]

Using

[
|z|^{-1/2}
=
Gamma(1/4)^{-1}int_0^infty v^{-3/4}e^{-vz^2},dv
]

and

[
int_0^infty v^{-5/4}e^{-t^2/(4v)},dv
=
sqrt2,Gamma(1/4)|t|^{-1/2}
]

gives exactly

[
mathbb E|Z-a|^{-1/2}
le
(2pi)^{-1/2}int |t|^{-1/2}|phi_Z(t)|,dt.
]

For (|phi_Z(t)|lemin(1,(u/|t|)^{3/4})), the weighted integral is

[
2int_0^u t^{-1/2}dt+
2u^{3/4}int_u^infty t^{-5/4}dt
=12sqrt u,
]

hence the displayed (12sqrt{u/(2pi)}). The proof is valid for extended values: first apply Tonelli to the nonnegative Gaussian representation, apply Gaussian inversion for each fixed (v>0), take absolute values, and apply Tonelli to the nonnegative Fourier majorant. No pointwise density representative is used.

### Rough product laws and trace/coarea steps — PASS

Source lines 256–301 and 401–493.

1. The projection lemma selects representatives satisfying (0le f_ile1) everywhere. Its marginal formula is needed only for almost every projected point, and geometric Brascamp--Lieb then gives an essential bound.
2. The scalar-square formula is used as conditional measure domination against nonnegative output tests. Integrating conditional domination with Tonelli prevents condition-dependent exceptional sets from becoming a gap.
3. The definite-pair change of variables is a deterministic two-dimensional integral after conditioning on original coordinates.
4. In the hyperbolic-pair lemma, the ((delta,t,epsilon)) parameterization is applied against nonnegative test functions. Although the displayed coarea density is only defined for almost every output level, the resulting measure domination is version-independent. Modifying an input density on a null set modifies the planar product density only on a planar null set; the change-of-variables identity and Tonelli are therefore unaffected.
5. The tail estimate uses one original coordinate density cap and its mass, never a rotated marginal cap or post-rotation independence.

Consequently the pivot branches are rigorous for arbitrary rough product densities without a smoothing hypothesis.

### Full versus truncated half potentials — PASS

Source lines 652–725.

The manuscript preserves the distinction

[
H(Z)=sup_amathbb Eigl[|Z-a|^{-1/2}mathbf 1_{{|Z-a|le1}}igr]
]

versus the full potential. Proposition `pivot-H` proves only the truncated estimate. Proposition `nine` adds at most one from (|Z-a|>1), where the kernel is at most one, to obtain the full bound (601). The scalar-pivot density receiver uses the full bound, not the truncated one.

### Regularity scope — PASS

Source lines 91–120, 386–400, 726–790.

The no-pivot order-five branch has an (L^1) characteristic function and therefore a canonical continuous (C_0) density. The pivot branches establish domination of the output measure by (C,dx), hence an essentially bounded density, but do not supply a uniform translation modulus. The theorem and final remarks correctly make no global continuity claim. Essential boundedness is not silently promoted to continuity.

### End-to-end ledger

- Lines 1–90, theorem, quantifiers, normalization, and architecture: **PASS**. The scaling (Y=KX), (widetilde Q=(K^2/s)Q) yields (K^2/s).
- Lines 91–160, Fourier inversion, power envelope, Riesz half-potential: **PASS**.
- Lines 162–220, singular-value perturbation, Schur spectral count, diagonal dominance: **PASS**. For the singular Schur limit, the baseline's moving-threshold argument is valid: if (N_{S_arepsilon}(t-|arepsilon|)ge q), convergence of ordered eigenvalues implies the (q)-th limiting modulus is at least (t). A fixed-(delta) rewrite is clearer but not mathematically necessary.
- Lines 221–255, geometric Brascamp--Lieb heat flow and limiting steps: **PASS**.
- Lines 256–283, product projection: **PASS WITH WORDING GAP**. After factors with (b_i=0) are dropped, the text writes (sum_i(1-b_i)=d). If the sum is over retained (b_i>0) indices, it should read (le d). Alternatively keep the sum over all indices. The needed upper bound and all downstream constants remain valid.
- Lines 284–301, integrated scalar Fourier powers: **PASS**.
- Lines 303–400, decoupling, graph weights, regularizer, crossing determinant, and volume exponents: **PASS**. The order-three exponent is used only with the Riesz weight; order five supplies (L^1) inversion.
- Lines 401–536, scalar/definite/hyperbolic pivots and quarter-power concentration: **PASS**.
- Lines 537–621, sampled interpolation, support, global rank (3r), restricted rank (r), and spectral-to-volume conversion: **PASS**.
- Lines 622–651, random cut and no-pivot consequences: **PASS**.
- Lines 652–725, singular kernels and pivot/nine-direction half potentials: **PASS**.
- Lines 726–790, final branch closure, constants, scaling, and limitations: **PASS**.

## Threshold-lowering check

The same structural argument at order four would replace 17 by 13 in the no-pivot algebra, but the determinant theorem then gives only

[
|phi(t)|lesssim |t|^{-1}.
]

That envelope alone cannot imply a bounded density. For independent (U,Vsim{m Unif}[-1,1]),

[
p_{UV}(x)=	frac12log(1/|x|)mathbf 1_{0<|x|<1}
]

is unbounded, while

[
phi_{UV}(t)=operatorname{Si}(t)/t
]

satisfies (|phi_{UV}(t)|lemin(1,4/|t|)). Therefore this run does not certify 13; a genuine reduction must exploit additional quadratic/product structure beyond the scalar Fourier envelope.

## Repository-package gap

At the inspected root, `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` named by the README returned 404. The manuscript, README, and textual audit were present. This is a reproducibility/package delivery gap, not a defect in the symbolic proof.

## Next obligations

1. Replace the projection-lemma equality by the unambiguous restricted-index inequality.
2. Restore the four advertised reproducibility files or amend the README.
3. Keep the 17-eigenvalue theorem at PASS, not independently validated, until the release gate synthesizes genuinely separate full reviews.
4. Any 17-to-13 improvement must close the critical order-four endpoint using structure absent from a bare (1/|t|) characteristic-function envelope.
