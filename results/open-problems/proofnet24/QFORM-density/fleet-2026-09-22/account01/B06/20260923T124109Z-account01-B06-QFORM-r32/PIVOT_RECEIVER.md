# account01/B06 r32 supplement — fixed-index square peel plus rank-two cross-volume half-Riesz receiver

This supplement continues the same r32 mechanism. It gives an actual density receiver for the subbranch in which the distinguished collision hub has a usable physical diagonal pivot and a fixed amount of its double-incidence packet survives off the diagonal. It is not a full-QFORM proof.

## 1. Rank-two cross-volume controls a half-Riesz potential

Let `S(X)` be an arbitrary real quadratic-affine polynomial in independent original-coordinate variables of density at most one. After conditioning any outside coordinates, choose disjoint original-coordinate banks `I,J`, and let

`M=S_(I,J)`

be the literal quadratic cross block. Put

`Z_2=E_2(M)=sum_(|R|=|T|=2) det(M_(R,T))^2`.

Use squared-minor volume sampling

`w_(R,T)=det(M_(R,T))^2/Z_2`,

and let

`alpha_i=sum_(R contains i,T) w_(R,T)`

be its row marginals. Suppose

`max_i alpha_i <= h <1`.                                           (1.1)

Set

`q=max(1,2h)`, so `1<=q<2` and `alpha_i<=q/2`.

### Theorem 1.1 — `QFORM-CROSS2-HALF-RIESZ-VOLUME-v1`

Uniformly in all affine terms and all conditioning values,

`boxed:
 H_(1/2)(S):=sup_t E|S-t|^(-1/2)
 <= [8 e^(1/4) q^(-1/4)/(2-q)] Z_2^(-1/8).`                        (1.2)

In particular, under the clean marginal gate `max alpha_i<=1/2`,

`boxed: H_(1/2)(S) <=8 e^(1/4) Z_2^(-1/8).`                        (1.3)

### Proof

The proof is the `k=2` fractional-potential specialization of the completed decoupling/Brascamp--Lieb volume argument in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

For completeness, here is the constant calculation. Decoupling and Jensen with exponent `q` give, exactly as in the general `D_k` proof,

`E_W F^q
 <= e^(k/2) (2pi/|t|)^k q^(-k/2) Z_k^(-1/2)`

whenever all row marginals are at most `q/2`. With `k=2`, after taking the `1/(2q)` power required by the decoupling square,

`|phi_S(t)|
 <= B |t|^(-1/q),`                                                  (1.4)

where

`B=e^(1/(2q)) (2pi)^(1/q) q^(-1/(2q)) Z_2^(-1/(4q)).`              (1.5)

The Fourier potential identity from the same source states that for `0<alpha<1`, if

`|phi(t)|<=min(1,B|t|^(-b))`, `b>alpha`,

then

`H_alpha
 <= c_alpha [2b/(alpha(b-alpha))] B^(alpha/b)`,                    (1.6)

with `c_(1/2)=(2pi)^(-1/2)`. Here `alpha=1/2`, `b=1/q`, and `q<2`. Since

`B^(q/2)=e^(1/4)(2pi)^(1/2)q^(-1/4)Z_2^(-1/8)`,                    (1.7)

and

`2b/[alpha(b-alpha)]=8/(2-q)`,                                     (1.8)

(1.2) follows. Conditioning outside `I union J` is harmless because the quadratic cross block is fixed and all generated affine terms are already allowed. QED.

This theorem is deliberately a **fractional-potential** result, not a density theorem: two cross directions give enough Fourier decay for `H_(1/2)` but not necessarily for an `L^1` characteristic function. It therefore matches a subsequent square peel exactly.

## 2. The distinguished physical coordinate as a square pivot

Return to the r30/r32 zero-anchor chamber

`A=[[0,0,a^T],[0,0,b^T],[a,b,C]]`.                                (2.1)

Fix a background physical coordinate `i` and write

`c=C_(ii)`.                                                         (2.2)

Assume `c!=0`. Complete the square in the **original independent scalar** `Z_i`. If `A^(i)` denotes the Schur complement after deleting coordinate `i`, then

`Q=c(Z_i+Psi(X,Y,Z_(-i)))^2+S`,                                    (2.3)

where `S` is the quadratic-affine form with quadratic matrix `A^(i)`. The standard one-dimensional square peel gives

`boxed: ||p_Q||_inf <= |c|^(-1/2) H_(1/2)(S).`                     (2.4)

No support, moment, or conditional-independence hypothesis beyond the original product law is used.

## 3. Double-incidence bordered minors become two-volume after the pivot

Use the r30 bordered minors

`D_(R,T)=det [[0,a_T^T],[b_R,C_(R,T)]],` `|R|=|T|=2`.              (3.1)

For `j,k!=i`, consider the double-incidence terms

`D_({i,j},{i,k})`.                                                  (3.2)

### Proposition 3.1 — `QFORM-SHARED-INDEX-SCHUR-MINOR-v1`

For every `j,k!=i`,

`boxed:
 D_({i,j},{i,k})
 = c det A^(i)[{X,j},{Y,k}]`                                       (3.3)

up to the fixed row/column ordering sign, hence exactly after squaring.

### Proof

The left side is the determinant of the `3 x 3` submatrix of `A` with rows `{X,i,j}` and columns `{Y,i,k}`. Reorder both rows and columns so that the common pivot coordinate `i` is first. The two swaps have cancelling sign. Block determinant elimination at the nonzero pivot `c=A_(ii)` gives `c` times the indicated `2 x 2` minor of the Schur complement. QED.

Define the **off-diagonal double-incidence mass**

`S_i^off=sum_(j!=k; j,k!=i) D_({i,j},{i,k})^2`.                    (3.4)

The exclusion `j=k` is exactly what permits a disjoint physical cut after the pivot.

## 4. Random cut after fixing the pivot

Randomly partition the remaining background coordinates `[m]\{i}` into `L union R`, independently with probability `1/2`, and keep hub `X` permanently on the left and hub `Y` permanently on the right. Let

`M_cut=A^(i)[{X} union L,{Y} union R]`.                             (4.1)

For every ordered `j!=k`, the minor in (3.3) appears in `E_2(M_cut)` exactly when `j in L` and `k in R`, which has probability `1/4`. Since all terms in `E_2` are nonnegative,

`E_cut E_2(M_cut)
 >= S_i^off/(4c^2).`                                                (4.2)

Therefore some literal original-coordinate cut satisfies

`boxed: E_2(M_cut) >= S_i^off/(4c^2).`                             (4.3)

This is a weighted replacement for selecting one curved minor: the whole shared-index packet is first converted through the physical pivot, and only then is its aggregate off-diagonal mass exposed by a cut.

## 5. Actual density receiver

Assume that the cut supplied by (4.3) has row squared-2-volume marginals at most `1/2`. Then Theorem 1.1 gives

`H_(1/2)(S)
 <=8 e^(1/4) [S_i^off/(4c^2)]^(-1/8).`                             (5.1)

Combining with the square peel (2.4),

`boxed:
 ||p_Q||_inf
 <=8 (2e)^(1/4) |c|^(-1/4) (S_i^off)^(-1/8).`                     (5.2)

The numerical front constant is

`8(2e)^(1/4)=12.2157772909...`.                                    (5.3)

The scaling is exactly correct: `c` has quadratic scale one and `S_i^off` is a sum of squared third-order minors, so `|c|^(-1/4)(S_i^off)^(-1/8)` has inverse quadratic scale.

More generally, if the row marginal bound is `h<1`, use `q=max(1,2h)` in (1.2) and obtain

`||p_Q||_inf
 <= [8 e^(1/4) q^(-1/4)/(2-q)] 2^(1/4)
    |c|^(-1/4)(S_i^off)^(-1/8).`                                   (5.4)

## 6. Target-scale corollary

Suppose, in addition to the clean marginal gate,

`|c|>=kappa s`,
`S_i^off>=theta s^6`,                                               (6.1)

where `s=s_3(A)>0`, `kappa,theta>0` are dimension-free. Then

`boxed:
 ||p_Q||_inf
 <=8(2e)^(1/4) kappa^(-1/4) theta^(-1/8) s^(-1).`                 (6.2)

Hence every r32 distinguished hub with a target-scale diagonal pivot and a target-scale off-diagonal double-incidence packet is a completed universal-density branch.

## 7. Remaining local obstruction after this supplement

The r32 incidence theorem gives a fixed fraction of total packet in both `W_i^L` and `W_i^R`, but it does not by itself force `S_i^off` to be large. Therefore the remaining same-index obstruction has an explicit shape:

1. the distinguished pivot is small, `|C_ii|<<s`; or
2. most of the incident packet is not double-incident at `i`; or
3. the double-incidence packet is dominated by the diagonal terms `D_({i,j},{i,j})`; or
4. every cut carrying the off-diagonal double-incidence mass has a heavy rank-two volume-sampling row marginal.

Each failure is a more local hub/ridge configuration than the original high-collision exterior packet. The next receiver should treat these cases directly rather than restore a spectral-fiber supremum.

## 8. Finite check

For random symmetric `C` and random `a,b` in dimensions `m=3,5,8`, the Schur identity (3.3) was checked over all `j,k!=i`; the maximum absolute discrepancy over the tested cases was `1.56e-15`.

Full QFORM remains OPEN. This supplement proves a new conditional density branch and does not claim global continuity.
