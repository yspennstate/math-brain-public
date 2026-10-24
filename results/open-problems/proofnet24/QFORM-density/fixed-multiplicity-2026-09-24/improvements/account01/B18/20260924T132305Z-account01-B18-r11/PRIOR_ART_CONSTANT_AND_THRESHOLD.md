# B18 improvements — primary-source scope, constant tightening, and the 17→16 literature gate

Pinned baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **proved constant improvement + publication-scope citation patch + exact negative scope result for the current 16-direction endpoint. No multiplicity below 17 is claimed.**

## 1. Rigorous constant replacement

The baseline normalizes `K=s=1`, `eta=1/100`. In Proposition `prop:pivot-H`, the scalar-pivot branch actually gives

\[
H(Q)\le \eta^{-1/2}(8+3L_0)
=10\bigl(8+3(4+4\log16)\bigr)
=200+120\log16.
\]

The no-pivot nine-direction full half-potential is

\[
12\sqrt{80e}=176.959336\ldots<200,
\]

the definite-pair truncated potential is `<160`, and the indefinite-pair bound is

\[
10(32+4\log16)+4/e=432.375066\ldots.
\]

Hence the worst truncated half-potential is the scalar branch, and Proposition `prop:nine` may be sharpened from `H<=600`, full half-potential `<=601`, to

\[
H(Q)\le200+120\log16,
\qquad
\sup_a E|Q-a|^{-1/2}\le201+120\log16.
\]

The main scalar-pivot density therefore satisfies

\[
\|p_Q\|_\infty
\le10(201+120\log16)
=2010+1200\log16
=5337.106466687737\ldots.
\]

All other main branches are `<2400`, `<40`, and `<251`. Scaling exactly as in the baseline proves the stronger theorem

\[
\boxed{\|p_Q\|_\infty\le(2010+1200\log16)\,K^2/s<5338\,K^2/s.}
\]

No hypothesis changes. This tightening was already identified in the preceding B18 artifact and is reverified here; it is not asserted novel relative to that artifact.

## 2. Exact primary-source bibliography/scope patch recommended for publication

The baseline proof is self-contained, so these citations are provenance/scope rather than proof dependencies.

### BCCT published version

Replace or supplement the preprint-only entry with:

J. Bennett, A. Carbery, M. Christ, T. Tao, *The Brascamp–Lieb inequalities: finiteness, structure and extremals*, Geom. Funct. Anal. **17** (2008), no. 5, 1343–1415. DOI `10.1007/s00039-007-0619-6`.

The published source explicitly uses heat-flow monotonicity and is appropriate provenance for the self-contained geometric rank-one argument.

### Rudelson–Vershynin published version

M. Rudelson, R. Vershynin, *Small ball probabilities for linear images of high-dimensional distributions*, Int. Math. Res. Not. IMRN **2015** (2015), no. 19, 9594–9617. DOI `10.1093/imrn/rnu243`.

This is the primary projection/small-ball source. Its sharp scalar theorem is stronger than the manuscript's self-contained `sqrt(e)` constant.

### Add Livshyts–Paouris–Pivovarov

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. **216** (2016), no. 2, 877–889. DOI `10.1007/s11856-016-1431-5`.

Their cap-one product-marginal estimate is `2^{d/2}`, sharper than the manuscript's self-contained `e^{d/2}` estimate. The manuscript should acknowledge this direct projection prior art rather than leaving BCCT/RV as the only antecedents.

### Add Banks–Garza Vargas–Kulkarni–Srivastava

J. Banks, J. Garza-Vargas, A. Kulkarni, N. Srivastava, *Overlaps, eigenvalue gaps, and pseudospectrum under real Ginibre and absolutely continuous perturbations*, Ann. Inst. H. Poincare Probab. Statist. **60** (2024), no. 4, 2736–2766. DOI `10.1214/23-AIHP1400`.

Section 2 contains Theorem 2.1, explicitly titled “Density of Quadratic Forms,” for bilinear-affine forms `X^T ZY+X^T U+V^T Y+W` under independent bounded-density entries. Corollary 2.4 gives a scalar singular-value geometric-mean refinement. This is the closest primary prior art found in the targeted search and should be named explicitly.

A suitable scope sentence is:

> Related bounded-density anticoncentration results for bilinear-affine quadratic expressions were proved by Banks, Garza-Vargas, Kulkarni and Srivastava. Their theorem does not directly cover the arbitrary same-bank phases `F(X_I)+G(X_J)` retained by the crossing determinant argument here. Sharp product-marginal density constants were obtained by Livshyts, Paouris and Pivovarov. We prove the specialized estimates needed below self-containedly.

This sentence avoids any novelty claim from search absence.

## 3. Why the strongest located quadratic-form prior art does not close 17→16

The fresh B20 endpoint reduction shows that the unpaid `s_16` no-pivot chamber can contain a physical cut with quantitative order-four crossing volume, very small tail beyond rank four, and a second large crossing residing in a same-bank block. The tempting literature transfer is Banks et al. Corollary 2.4, because their scalar theorem can pay a bilinear form using only two leading cross singular values.

However, its exact scalar object is of the form

\[
X^T ZY+X^T U+V^TY+W,
\]

where the same-bank dependence is affine. In a physical cut of a general quadratic form, one instead has

\[
F(X)+2X^TMY+G(Y),
\]

with both `F` and `G` arbitrary quadratic polynomials inherited from the two principal blocks. The baseline determinant theorem was designed precisely to tolerate these phases by decoupling them away, at the price of exponent `-1/8`. Therefore one cannot substitute the Banks theorem for the order-four endpoint without first removing or separately paying at least one arbitrary same-bank quadratic phase. Conditioning cannot simply remove such a phase while retaining a two-bank cross matrix of the required rank, and no unconditional projected-density statement creates independence after rotation.

Consequently the targeted primary-literature search yields **no source-valid 16-direction closure** of the B20 endpoint geometry. This is a positive scope determination, not a novelty claim.

## 4. Exact current-method barrier

For the baseline determinant receiver, order `k` yields large-frequency power `k/4`. Absolute Fourier inversion requires `k>=5`. At `k=4`, the envelope is the endpoint `C/|t|` and does not prove a bounded density.

For order five, the sampled-interpolation algebra can encounter `r=4`. With global correction rank `<=3r` and restricted rank `<=r`, the diagonal-dominance contradiction needs

\[
m-3r\ge r+1,
\]

hence `m>=17`. This is why neither a literature citation nor a constant optimization lowers the certified threshold. A genuine `16` theorem needs a new self-contained endpoint receiver for arbitrary same-bank phases or a deterministic transversality/paving lemma that converts the B20 endpoint resources into fifth crossing volume.

## 5. Correction to the prior B18 Schur note

The earlier B18 report labeled the singular Schur moving-threshold passage a GAP. That label is withdrawn. If `m=N_A(t)-k>0`, the invertible regularizations give

\[
s_m(S_\epsilon)\ge t-|\epsilon|,
\]

and `S_epsilon->S`, so singular-value continuity gives `s_m(S)>=t`. The baseline paragraph is valid as written. The previously supplied fixed-threshold proof remains an alternative but is not a necessary repair.

No baseline file was overwritten in this run.