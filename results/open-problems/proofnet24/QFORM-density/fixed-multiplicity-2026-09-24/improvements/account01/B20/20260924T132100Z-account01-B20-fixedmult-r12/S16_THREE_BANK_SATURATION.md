# account01/B20 r12 — `s_16` saturation forces a quantitative three-bank rank-four collar

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T132100Z-account01-B20-fixedmult-r12`  
Pinned manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

## Scope

Normalize to coordinate density caps `<=1` and spectral scale one. Put

\[
\eta=\frac1{100},\qquad \kappa=\frac1{80^2}=\frac1{6400}.
\]

Assume throughout this note that `A=A^T` has **no** `eta`-pivot in the manuscript's sense and

\[
s_{16}(A)\ge1.
\]

This note does **not** prove the `s_16` bounded-density theorem. It isolates the only branch not already paid by the manuscript's order-five Fourier argument and forces that branch into an exact original-coordinate three-bank geometry.

## Theorem — order-five payment or three-bank saturation

Under the assumptions above, either

\[
V_5(A)\ge \kappa^5,
\]

in which case the manuscript's random-cut and order-five determinant argument gives

\[
\|p_Q\|_\infty\le 800e<2400,
\]

or there exist three pairwise disjoint original-coordinate four-sets `S,T,H` with the following properties.

1. `B=A[S,T]` is invertible.
2. With
   \[
   P=A_{\cdot,T}B^{-1}A_{S,\cdot},\qquad L=[n]\setminus(S\cup T),
   \]
   there is a decomposition `A=D+R+E` from the manuscript's completion lemma satisfying
   \[
   \|E\|_F<\frac1{16},\qquad \operatorname{rank}R\le12,
   \qquad R_{L,L}=P_{L,L},\qquad \operatorname{rank}P_{L,L}\le4,
   \]
   and `D` is diagonal and vanishes on `S union T`.
3. Exactly four indices in `L` can have `|D_ii|>=15/16`; choosing these as `H`,
   \[
   s_4(P_{H,H})>\frac{109}{700}.
   \]
   In particular `P_{H,H}` is invertible and `rank(P_{L,L})=4`.
4. The rank-four restriction has the exact skeleton factorization
   \[
   P_{L,L}=P_{L,H}P_{H,H}^{-1}P_{H,L}.
   \]
5. Both physical four-by-four crossing blocks `A[H,T]` and `A[S,H]` are invertible, and
   \[
   |\det A[H,T]|\,|\det A[S,H]|
   \ge
   \left(\frac{109}{700}\right)^4 |\det A[S,T]|.
   \]

Thus every unpaid normalized `s_16` no-pivot state contains three disjoint four-coordinate banks `S,T,H`, with all three pairwise physical crossings nonsingular (the third orientation follows from symmetry), and with a quantitative determinant transfer through the middle bank.

## Proof

Assume `V_5(A)<kappa^5`. Consider the successive ratios `V_{r+1}/V_r` in the manuscript's telescoping argument. For `r=0,1,2,3`, the proof of Proposition `prop:volume` still closes under `s_16(A)>=1`, because at those indices

\[
16\ge4r+1.
\]

Indeed, if `V_{r+1}<kappa V_r` for such an `r`, the manuscript's sampled completion has `rank R<=3r` and `||E||_F<=(r+1)sqrt(kappa)<=1/20`, while the rank-perturbation argument forces at least `r+1` large entries of the diagonal matrix `D` on the seed complement. The same strict-diagonal-dominance contradiction with `rank R_{L,L}<=r` applies verbatim. The `r=0` case is also unchanged.

Therefore the first ratio below `kappa` can only occur at `r=4`. In particular,

\[
V_4(A)\ge\kappa^4,
\qquad
\frac{V_5(A)}{V_4(A)}<\kappa.
\]

Apply the manuscript's volume-sampled interpolation lemma with `r=4`. We obtain disjoint four-sets `S,T`, an invertible

\[
B=A[S,T],
\]

and the completion

\[
A=D+R+E
\]

with

\[
\|E\|_F
\le5\sqrt{V_5/V_4}
<5\sqrt\kappa
=\frac1{16},
\]

\[
\operatorname{rank}R\le12,\qquad
R_{L,L}=P_{L,L},\qquad
\operatorname{rank}P_{L,L}\le4,
\]

where `L=[n]\setminus(S\cup T)` and `D` vanishes on `S union T`.

Since `s_16(A)>=1` and `||E||<=||E||_F<1/16`, Weyl gives

\[
s_{16}(D+R)=s_{16}(A-E)>\frac{15}{16}.
\]

The rank bound `rank R<=12` and the manuscript's rank-perturbation inequality imply

\[
s_4(D)>\frac{15}{16}.
\]

Because `D` is diagonal, at least four diagonal entries satisfy `|D_ii|>15/16`. They all lie in `L` because `D` vanishes on the seed `S union T`.

There cannot be five such entries. If `H' subset L`, `|H'|=5`, consisted of five of them, then for every `i in H'`, using the no-pivot bound `|A_ii|<1/100` and the zero diagonal of `E`,

\[
|R_{ii}|=|A_{ii}-D_{ii}|
>\frac{15}{16}-\frac1{100}
=\frac{371}{400}.
\]

For `i neq j` in `H'`,

\[
|R_{ij}|
\le |A_{ij}|+|E_{ij}|
<\frac17+\frac1{16}
=\frac{23}{112}.
\]

Hence each off-diagonal row sum on `H'` is strictly less than

\[
4\cdot\frac{23}{112}=\frac{23}{28}<\frac{371}{400}.
\]

Strict diagonal dominance would make `R[H',H']` invertible of rank five, contradicting `rank R_{L,L}<=4`. Thus exactly four entries of `D` can be above the `15/16` level. Let `H` be four such indices.

On `H`, the same estimates give diagonal lower bound `371/400`, now with only three off-diagonal terms. Therefore the diagonal-dominance margin is

\[
\frac{371}{400}-3\frac{23}{112}
=
\frac{371}{400}-\frac{69}{112}
=
\frac{109}{350}.
\]

Since `R_{H,H}=P_{H,H}`, for every `x in R^4` and an index `i` with `|x_i|=||x||_infty`,

\[
|(P_{H,H}x)_i|
>
\frac{109}{350}\,||x||_\infty
\ge
\frac{109}{700}\,||x||_2.
\]

Thus

\[
s_4(P_{H,H})>\frac{109}{700},
\]

so `P_{H,H}` is invertible. Since `rank P_{L,L}<=4`, the invertible four-by-four principal block forces `rank P_{L,L}=4`. Standard rank factorization through an invertible full-rank principal block gives the exact identity

\[
P_{L,L}=P_{L,H}P_{H,H}^{-1}P_{H,L}.
\]

Finally, by the definition of `P`,

\[
P_{H,H}=A[H,T]B^{-1}A[S,H].
\]

All factors are four-by-four. Since `P_{H,H}` and `B` are invertible, both `A[H,T]` and `A[S,H]` are invertible. Taking determinants,

\[
\det P_{H,H}
=
\frac{\det A[H,T]\det A[S,H]}{\det B}.
\]

Moreover

\[
|\det P_{H,H}|
\ge s_4(P_{H,H})^4
>
\left(\frac{109}{700}\right)^4.
\]

Therefore

\[
|\det A[H,T]|\,|\det A[S,H]|
>
\left(\frac{109}{700}\right)^4 |\det A[S,T]|.
\]

This proves the theorem.

## What this does and does not close

The result is stronger than merely saying that `s_16` saturates the manuscript's rank count. It produces an exact physical three-bank skeleton in the only unpaid order-five branch and quantifies the transfer of four-dimensional volume through the middle bank.

It does **not** by itself produce an `L^infinity` bound at multiplicity sixteen. The present determinant envelope at crossing order four is still the critical `|t|^{-1}` endpoint. A valid `17 -> 16` theorem now reduces to a genuinely new analytic/geometric implication for this three-bank collar: for example, prove that the two additional physical crossings force a leverage gap/transverse fifth direction on some product-preserving cut, or prove a direct three-bank endpoint estimate. No rotated coordinate is treated as independent, no coefficient tail is deleted, and all affine terms remain arbitrary.

Status: **PROVED STRUCTURAL REDUCTION; NOT A 16-EIGENVALUE DENSITY THEOREM.**
