# Strong-pivot Schur wedge routing

This addendum applies the new B19 wedge/star lemma directly inside a genuine physical Schur pivot, so the ridge-ready alternative becomes immediately payable by the completed account03/B09 pivot-ridge theorem.

## Source-pinned input actually applied

`QFORM-PIVOT-RIDGE-BILINEAR-v1`, account03/B09, canonical `yspennstate/math-open-problems@62bdcf30669c1037a3c7d87aee1fcb2bdcccd251`, proves: for an original physical pivot `a=A_kk!=0` with scalar Schur complement `S`, a residual physical cross block `N=S[I,J]`, ridge scale `gamma`, `q=1`, `max diag K_gamma<=1/2`, and ridge trace `theta>=3/2`, one has the safe bound

`||p_Q||_inf <= 9.2544320556 / sqrt(|a| gamma).`

All coordinates in the cross bank remain original, and arbitrary self blocks/additional directions are retained.

## Theorem — `QFORM-STRONG-PIVOT-SCHUR-WEDGE-v1`

Let `A` satisfy the exact target hypotheses and suppose an original physical pivot `k` has

`|a|=|A_kk| >= c_* := 2/(3+sqrt(5)).`

Let

`S=A_{-k,-k}-A_{-k,k}A_{k,-k}/a`,
`H_S=S-diag(S)`.

Assume

`s_2(H_S) >= 1/8,       sr(H_S) <= 24.`

Then at least one of the following holds:

1. `Q=X^TAX` already has an essentially bounded density with

`||p_Q||_inf <316`; or

2. some residual original coordinate `i` has a Schur offdiagonal row satisfying

`||H_S[i,i^c]||_2 >= 1/(256 sqrt(6)).`

### Proof

Apply `QFORM-WEDGE-STAR-RIDGE-DICHOTOMY-v1` from the primary B19 report to `H_S`, with `delta=1/8` and `R=24`.

If its heavy-row alternative occurs, then

`||H_S[i,i^c]||_2
 >= delta/sqrt(256R)
 = 1/(256 sqrt(6)),`

which is conclusion 2.

Otherwise there is a residual original-coordinate bipartition `I disjoint_union J`, a cross block

`N=H_S[I,J]=S[I,J]`,

and a ridge scale

`gamma >= delta/sqrt(128R)
        = 1/(256 sqrt(3)),`

such that

`theta=tr[N N^T(gamma^2I+N N^T)^(-1)] >=8/5>3/2`

and

`max diag K_gamma<=1/2`.

The scalar pivot `X_k` is automatically disjoint from all residual coordinates, so there is no resource-reservation issue in this application. The account03/B09 pivot-ridge theorem therefore applies with `q=1` and gives

`||p_Q||_inf
 <=9.2544320556/sqrt(|a|gamma)
 <=9.2544320556/sqrt(c_*/(256sqrt(3)))
 <315.31<316.`

This is conclusion 1. QED.

## Synthesis consequence

Combine this theorem with the dimension-descent addendum and account02/B09's high-Schur-stable-rank theorem. In the diagonal-dominant heavy-coordinate branch, a minimal counterexample to a global induction bound `C>=20122` must now satisfy all of:

- `|a|>=c_*=2/(3+sqrt(5))` (otherwise dimension descent pays it);
- `sr(H_S)<24` (otherwise account02/B09 pays it);
- and either `s_2(H_S)<1/8`, or a residual Schur offdiagonal row has norm at least `1/(256sqrt(6))`.

Thus the diagonal-heavy structural debt has collapsed to a **one-effective Schur / heavy-Schur-row** state under a strong physical pivot. The remaining offdiagonal-heavy original-coordinate branch is separate.

The live first unpaid implication is correspondingly sharpened to `QFORM-STRONG-PIVOT-ONEEFFECTIVE-OR-HEAVYROW-v1`: under the strong pivot above, pay either `s_2(H_S)<1/8` or the forced heavy Schur row while retaining a genuinely independent third smoothing resource; and separately route the window-heavy offdiagonal-coordinate case. The same-square and half-negative-moment corrections forbid collapsing that third resource into the heavy row itself.

Full QFORM remains OPEN.
