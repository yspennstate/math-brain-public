# Addendum — independent B19 review of the concurrent multiplicity-eight candidate

Run: `20260924T150253Z-account03-B19-QFORM-fixed-multiplicity-audit-auto11`

This addendum corrects two items in `REPORT.md` after refreshing concurrent worker output.

1. The two-high-leverage contradiction was independently found slightly earlier by account03/B07 and account03/B01. Therefore B19 does **not** claim priority for that short closing observation.
2. The complete multiplicity-eight constant can be taken as **2400**, not merely the `<2510` bound assembled in the first B19 write.

## Source reviewed

I read the complete concurrent candidate of account03/B07:

- repository: `yspennstate/math-open-problems`
- commit containing the report: `07099b280095527eff5059c591a8ea4a86629bdf`
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B07/20260924T150837Z-account03-B07-fixedmult-r2/REPORT.md`

I also read the independently assembled account03/B01 candidate at the same repository state:

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B01/20260924T151315Z-account03-B01-fixedmult-collision-r03/REPORT.md`.

The B19 review verdict for the B07 `QFORM-FIXED-MULTIPLICITY-8-v1` chain is **PASS**.

This is one genuinely separate end-to-end review. I do not self-award the owner's two-review validation gate; a second independent end-to-end review of the complete `s_8` chain is still required unless another existing worker records one.

## Reviewed chain

### 1. Pivot branches under `s_8` — PASS

Use the old collar threshold `eta=1/100`.

- Scalar pivot: one Schur loss from `s_8>=1` leaves at least seven unit-scale singular directions. The completed five-direction full half-potential theorem therefore applies to the Schur remainder. With the active manuscript constants `d=3/40`, `p=1/400`, its bound is `<115`; the outer square profile contributes `eta^{-1/2}=10`, hence `<1150`.
- Definite two-coordinate pivot: direct coarea gives `<pi/sqrt(eta)<40`.
- Indefinite two-coordinate pivot: the Schur remainder retains at least six unit-scale directions, while the hyperbolic/logarithmic-potential argument needs only one. The displayed bound is `<197`.

Thus every pivot branch is `<2400` already at multiplicity eight. Arbitrary affine terms are retained through Schur completion.

### 2. No pivot, `V_3>=kappa^3` — PASS

Here `kappa=80^-2=1/6400`. A fair literal physical cut gives

`Z_3>=V_3/64>=kappa^3/64`.

The marginal-free order-three receiver has `C_3<15`, so

`||p_Q||_infinity < 15 (kappa^3/64)^(-1/6) = 2400`.

This branch has a continuous `C_0` density.

### 3. No pivot, `V_3<kappa^3`: robust anchor extraction — PASS

The source-pinned account03/B17 theorem supplies a literal original-coordinate pair `H`, complement `L`, and `C=A[H,L]` satisfying

`g=det(CC^T)>=delta_*^2/2`,

with

`delta_*=97/100-(297 sqrt(2)+3 sqrt(202))/4000`.

The elementary bounds `sqrt(2)<3/2`, `sqrt(202)<15` imply `delta_*>4/5`, hence `g>8/25`.

### 4. Zero or one high leverage — PASS

The leverage-corrected completion is valid also with one exceptional high row. Let

`Q_C=C^T(CC^T)^(-1)C`, `P=I-Q_C`, `q_i=(Q_C)_ii`, and `J={i:q_i>2/3}`.

For light rows, the exact identity

`W_i=g(p_i||r_i||^2-r_ii^2)`, `p_i=1-q_i>=1/3`,

produces a zero-diagonal error `E` with

`||E||_F^2 <= 3 sum_{light i} W_i/g`.

If the disjoint incident volume is at most `g/48`, then `||E||_F<=1/4`. With `h=|J|<=1`, the residual matrix has global rank at most `4+h<=5` and light-light rank at most two. Rank perturbation from `s_8(A)>=1` forces at least three light diagonal completion entries of magnitude at least `3/4`; the no-pivot entry cap then makes the corresponding `3 x 3` light compression strictly diagonally dominant, contradicting rank at most two. Hence the incident volume is `>g/48`, and the completed product-safe incident-volume receiver gives `<23.48` with continuous density.

B19 also independently checked the stronger terminal version used in `REPORT.md`, where `V_3<kappa^3` makes `||E||_F<10^-3`; this is consistent and strictly stronger than the `1/4` contradiction threshold.

### 5. Two high leverages — PASS / impossible

Because `Q_C` has rank two, `sum_i q_i=2`, so there are at most two coordinates above `2/3`. Suppose there are exactly two, `i,j`.

The determinantal weights

`w_ab=det(C_{ab})^2/g`

form a probability measure on two-subsets and have marginals `q_i`. Therefore

`w_ij >= q_i+q_j-1 > 1/3`,

so

`det(C_{ij})^2 > g/3 > 8/75`.

But no `eta`-pivot implies every off-diagonal physical coefficient satisfies

`|A_uv|^2 < eta+eta^2 = 101/10000`.

All four entries of the literal cross matrix `C_{ij}` are off diagonal, hence

`|det C_{ij}| < 2(101/10000)=101/5000`,

and therefore

`det(C_{ij})^2 < 10201/25000000 < 8/75`,

a contradiction.

Thus the robust terminal collar has no unpaid state.

## Reviewed theorem

After normalization and scaling back exactly as in the active manuscript:

\[
\boxed{
 s_8(A)\ge s>0
 \Longrightarrow
 \|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
 <2400\,{K^2\over s}.
}
\]

Scope: arbitrary dimension; arbitrary real symmetric `A`; arbitrary signs and remaining spectrum; arbitrary affine `b,c`; independent real coordinate densities bounded only by `K`. No Gaussianity, moments, support assumptions, log-concavity, diagonal-basis assumption, post-rotation independence, arbitrary-joint coarea, or pointwise rough quadratic-phase decay is used.

Regularity: the no-pivot branches are continuous `C_0`; the assembled theorem is presently recorded only as an essentially bounded density theorem because global pivot-branch continuity has not been independently established.

## Review status

- `s_8 => 2400 K^2/s`: **B19 INDEPENDENT END-TO-END REVIEW PASS (review 1)**.
- owner two-review gate: **NOT YET SELF-DECLARED COMPLETE**.
- unrestricted `s_3` theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
