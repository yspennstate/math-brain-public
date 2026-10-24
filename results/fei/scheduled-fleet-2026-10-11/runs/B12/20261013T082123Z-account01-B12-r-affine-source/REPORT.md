# B12 / A057 — a fixed-piece affine-source theorem

Run: `20261013T082123Z-account01-B12-r-affine-source`  
Primary packet: A057 (Coherent restriction remainder)  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v14`  
Status: contributor-PROVED proper-class theorem; independent A090/A091 review pending; full FEI OPEN.

## Exact delta

The preceding run proved the asymptotically sharp payment `Omega <= 8 ln(2) I(d)` when the physical defect source is the union of at most two disjoint affine cosets. This run proves a dimension-independent theorem for every fixed number of pieces.

Let `E_1,...,E_r` be pairwise disjoint nonempty affine cosets in a physical Boolean cube, write `s_j=1_{E_j}`, `s=sum_j s_j`, and put

`d(x,z)=1_{x=-1}s(z)`.

For the genuine Boolean branches `g_-=x`, `g_+=x+2d`, with `a=x+d`, `h=-x`, and `F=a+d`, the signed associator satisfies, for `r>=3`,

`Omega = E_raw(F)-E_raw(a)-E_raw(d) <= C_r I(d)`,

where

`C_r = 8 r ln(r) + 4/e`.                                  (1)

Thus

`C_3 = 24 ln(3)+4/e = 27.838212692720404...` nats

(equivalently `40.16205139899993...` in bit-normalized units). The result has no dependence on ambient dimension, affine codimensions, physical adjacency graph, spectral overlap, hierarchy depth, or changing activation weights. For `r<=2`, the sharper preceding constant `8 ln 2` applies.

For an adaptive nonreusing physical hierarchy whose reached local sources are restrictions of one global source and remain unions of at most `r` disjoint affine cosets,

`sum_v w_v Omega_v <= C_r I(b)`.

Restrictions preserve the class (a restricted affine coset is empty or affine), and the final inequality is the exact nonreuse derivative ledger.

## Proof

Put `p_j=2^{-k_j}` and `p=sum_j p_j`. For a Fourier coordinate `T`, set `a_j=hat{s_j}(T)`, `u=sum_j a_j^2`, and `z=(sum_j a_j)^2`. Physical disjointness gives `sum_T u=p<=1`; hence `u<=1`, while Cauchy and Boolean boundedness give `z<=min(r u,1)`.

For `Phi(t)=t ln(1/t)`, the scalar envelope

`Phi(z) <= r Phi(u)+u/e`                                  (2)

holds whenever `0<=u<=1` and `0<=z<=min(ru,1)`. If `u<=1/(re)`, monotonicity on `[0,1/e]` gives `Phi(z)<=Phi(ru)<=rPhi(u)`. If `u>=1/(re)`, use `Phi(z)<=1/e`; the concave function `rPhi(u)+u/e` is at least `1/e` at both endpoints of `[1/(re),1]`.

Also `sum_j Phi(a_j^2)>=Phi(u)`. Summing (2) over Fourier coordinates yields

`E_raw(s) <= r sum_j E_raw(s_j)+p/e`
`         = 2 r ln(2) sum_j p_j k_j +p/e`.                 (3)

The density/codimension sum has an exact information interpretation. With `lambda_j=p_j/p`,

`K:=sum_j p_j k_j = p log_2(1/p)+p H_2(lambda)`
`                    <= p log_2(1/p)+p log_2 r`.            (4)

The cube edge-isoperimetric inequality, applied to `s` or its complement, gives

`p log_2(1/p) <= 2 I(s)`                                   (5)

for every `0<=p<=1`; on the majority side use
`(1-p)log_2(1/(1-p)) >= p log_2(1/p)`. Therefore

`K <= 2I(s)+p log_2 r`.                                    (6)

Combining (3) and (6),

`E_raw(s) <= 4r ln(2) I(s) + (2r ln r+1/e)p`.              (7)

The exact selector-pair identity remains

`Omega=E_raw(s)+C(p)`, with `C(p)<=0`, and
`I(d)=I(s)/2+p/4`.

For `r>=3`, (7) is bounded by `(8r ln r+4/e)I(d)`, proving (1).

## Verification

`check_three_piece.py` uses exact rational Walsh coefficients and exhausts every triple of disjoint affine cosets through four source variables. It separately checks the density/isoperimetry budget for the largest-`K` decomposition of each union.

- 629,590 disjoint triple decompositions;
- 57,991 distinct unions across dimensions two through four;
- zero violations of the proved `C_3` bound;
- zero violations of the stronger conjectural `8 ln 2` bound at this finite scope;
- 999,999 deterministic scalar-envelope grid points;
- no random seed.

The largest observed ratio was `2.950791780762193`, far below both constants, on the three-point source `{0,1,2}` in four source variables.

## What remains unpaid

The theorem is dimension-independent for every fixed `r`, but `C_r` grows as `r ln r`; therefore it does not settle FEI. The loss has two explicit origins:

1. the worst-case scalar coherent-sum factor `r` in (2); and
2. the piece-label entropy `p log_2 r` in (4).

The first factor is necessary for arbitrary unconstrained coefficient tuples, but the two-piece theorem shows that disjoint affine phases create a much stronger balanced-character refund. Exhaustive triples through four variables also survive the sharp `8 ln 2` constant. The next step is to express the common-annihilator spectra as a finite character table and prove a multiway phase-refund inequality that pays the label entropy and internal physical edges together. Arbitrary Boolean sources and full FEI remain OPEN.

Independent review: pending A090/A091. No native adoption or packet completion is claimed.
