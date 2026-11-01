SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-23T22:53:26Z.
attacking: the first unresolved finite-collar step after fleet02/B20's exact common-Gram third-mode escape; convert the six relative Schur relations into an absolute rank-two off-diagonal collar on a quantitatively nondegenerate moderate-scale branch, then localize the forced third mode to non-arm physical banks.

# Finite-collar absolute bridge for the r37 canonical common-Gram chamber

Status: **PROVED SUPPORTING IMPLICATION / ESSENTIAL STEP APPLIED / FULL QFORM OPEN**. Global continuity remains OPEN; only branches explicitly paid through the physical E3 receiver below obtain a continuous C0 density.

Run: `20260923T225326Z-fleet01-B20-QFORM-auto11b`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-pinned completed partner and live setup

The newest completed designated fleet02/B20 package at the dependency refresh is

`yspennstate/math-open-problems@edefefbd4d25c1c870330eb976e47a9356f7f4a0`,
run `20260923T200300Z-fleet02-B20-QFORM-auto11`, whose theorem
`QFORM-R37-EXACT-COMMONGRAM-THIRDMODE-ESCAPE-v1` proves the following scale-sigma statement.

Let the five disjoint physical two-frames be the canonical frames on
`D_1,K_1,K_2,K_3,D_2`, let `P` be their orthogonal sum and `Q=I-P`, and suppose the off-diagonal compressed P-network is exactly a rank-at-most-two symmetric common-Gram kernel. If `s_3(A)>=sigma`, while the five compressed self blocks may be arbitrary, then

`max{ ||PAQ||_op, max_i ||Delta_i||_op, ||QAQ||_op } >= sigma/2`.   (1.1)

The later fleet02/B20 commit `e6fb033da9284737b71b90dfd2cb2f7f6277d9e1` is explicitly an EARLY calculation from an unfinished newer run, so it is not substituted for the completed designated partner.

The canonical r37 diffuse packet uses, for `b=1,2,3`,

`A_b = U_1^T A[D_1,K_b] W_b`,
`B_b = W_b^T A[K_b,D_2] U_2`,
`C   = U_1^T A[D_1,D_2] U_2`,
`D_ab= W_a^T A[K_a,K_b] W_b`,  `a!=b`,

with exact physical symmetry `D_ba=D_ab^T` and

`s_2(A_b), s_2(B_b) > a`,
`a:=a_D=0.002408434254376076... .`                                (1.2)

For ordered `a!=b` put

`S_ab := B_a-D_ab A_b^{-1} C`.                                  (1.3)

The completed mixed-fan Schur identity gives on the literal physical cut
`M_ab=A[D_1 union K_a, K_b union D_2]`

`e_3(M_ab M_ab^T) >= det(A_b)^2 ||S_ab||_F^2
                  > a^4 ||S_ab||_F^2`.                           (1.4)

The completed marginal-free physical E3 theorem gives, for every literal physical cross block with `Z_3=e_3(MM^T)>0`,

`||p_Q||_infinity <= C_3 Z_3^{-1/6}`,
`C_3=3*2^(4/3)*exp(1/3)=10.5501688311...`,                        (1.5)

with a continuous C0 density and with arbitrary same-bank curvature, outside coordinates and exterior couplings retained.

## 2. Main robustification theorem

### Theorem `QFORM-R37-FINITE-COLLAR-ABSOLUTE-BRIDGE-v1`

Assume the canonical diffuse packet above. Fix numbers `c,M>0` and suppose

`s_2(C)>=c`,
`max_b ||A_b||_op <= M`,
`||C||_op <= M`.                                                   (2.1)

No upper bound on `B_b` or `D_ab` is assumed.

Define

`delta_*(a,c,M)
 := c / [ 8(21 M^2/a + 2M) ].`                                   (2.2)

Then one of the following holds.

**(D3 payment)** For some ordered `a!=b`, `||S_ab||_F>=delta_*`, and the full ambient law is paid by

`||p_Q||_infinity
 <= C_3 a^{-2/3} delta_*^{-1/3}`.                                (2.3)

This branch has a continuous C0 density.

**(Absolute common-Gram escape)** There is a symmetric rank-at-most-two common-Gram model for the five canonical frames whose off-diagonal P-block differs from the actual compressed P-block by operator norm strictly smaller than `1/4`. Consequently the completed fleet02/B20 theorem applies after this perturbation and yields

`max{ ||PAQ||_op, max_i ||Delta_i||_op, ||QAQ||_op } > 3/8`.      (2.4)

Here the self defects `Delta_i` are relative to the constructed exact common-Gram model. All projections are used only for deterministic coefficient geometry; no projected random coordinates are declared independent.

### Proof

Assume the D3-payment alternative fails, so

`||S_ab||_F < delta_*` for all ordered `a!=b`.                    (2.5)

Because `s_2(A_b)>a` and `s_2(C)>=c`, all `A_b,C` are invertible. Define

`F_b := A_b^{-T} B_b C^{-1}`.                                    (2.6)

The six Schur relations and exact symmetry produce a quantitative transpose cocycle with no upper-norm loss. Indeed, from (1.3),

`D_ab=(B_a-S_ab) C^{-1} A_b`.                                    (2.7)

Transpose (2.7), use `D_ba=D_ab^T`, and compare with the equation for `S_ba`. After multiplying on the left by `A_b^{-T}` and on the right by `C^{-1}`, one gets the exact identity

`F_b-F_a^T
 = A_b^{-T} S_ba C^{-1}
   -(A_a^{-T} S_ab C^{-1})^T`.                                  (2.8)

Hence

`||F_b-F_a^T||_op < kappa,
 kappa:=2 delta_*/(ac).`                                          (2.9)

With three K-banks, the odd three-cycle forces approximate symmetry. Put

`F := (F_1+F_1^T)/2`.                                             (2.10)

Using the three estimates `F_2~F_1^T`, `F_3~F_2^T`, `F_1~F_3^T`,

`||F_1-F_1^T|| < 3 kappa`,                                       (2.11)

and therefore

`||F_1-F|| < (3/2)kappa`,
`||F_2-F|| < (5/2)kappa`,
`||F_3-F|| < (7/2)kappa`.                                        (2.12)

In particular

`max_b ||F_b-F|| < tau,
 tau:=7 delta_*/(ac).`                                            (2.13)

If `F` is singular, choose a symmetric invertible `F'` arbitrarily close to `F`; if it is already invertible take `F'=F`. Choose it so that

`nu:=||F'-F||_op < 1/(24 M^2)`.                                  (2.14)

Let `E':=(F')^{-1}` and define five invertible node maps

`G_(D_1)=I_2`,
`G_(K_b)=F' A_b`,
`G_(D_2)=F' C`.                                                   (2.15)

The block matrix

`S^P_(ij):=G_i^T E' G_j`                                         (2.16)

is symmetric and has rank at most two. Its off-diagonal blocks satisfy exactly

`S^P_(D_1,K_b)=A_b`,
`S^P_(D_1,D_2)=C`,
`S^P_(K_b,D_2)=A_b^T F' C`,
`S^P_(K_a,K_b)=A_a^T F' A_b`.                                   (2.17)

Thus the first four source edges are matched exactly, and the remaining errors can be bounded without any `B_b` or `D_ab` upper norm. Since

`B_b=A_b^T F_b C`,                                                (2.18)

we have

`||B_b-A_b^T F' C||
 <= M^2(tau+nu).`                                                  (2.19)

Likewise (2.7) gives

`D_ab=A_a^T F_a A_b-S_ab C^{-1}A_b`,                              (2.20)

and therefore

`||D_ab-A_a^T F' A_b||
 <= M^2(tau+nu)+delta_* M/c.`                                    (2.21)

Let `T` be the zero-diagonal five-node block matrix consisting of these off-diagonal errors. A K-row has one error of type (2.19) and two of type (2.21); the D_2 row has three errors of type (2.19); the D_1 row has none. The block row-sum estimate therefore gives

`||T||_op
 <= 3M^2(tau+nu)+2 delta_* M/c
 = delta_*/c (21M^2/a+2M)+3M^2 nu.`                              (2.22)

By (2.2), the first term is at most `1/8`; by (2.14), the second is strictly smaller than `1/8`. Hence

`boxed: ||T||_op<1/4.`                                            (2.23)

Now form a new deterministic symmetric coefficient matrix `A'` from `A` by replacing only the off-diagonal compressed blocks among the five P-frames by (2.16), while leaving every compressed self block, every P-Q block and the entire Q-Q block unchanged. Then

`||A-A'||_op=||T||_op<1/4`,                                      (2.24)

so Weyl gives

`s_3(A') >= s_3(A)-||A-A'|| > 3/4`.                              (2.25)

The P-network of `A'` is now an exact common-Gram endpoint, with arbitrary self defects retained. Apply the completed fleet02/B20 theorem (1.1) to this actual inequality at scale `sigma=s_3(A')>3/4`. Because the P-Q and Q-Q blocks and the self blocks were not changed,

`max{ ||PAQ||_op, max_i ||Delta_i||_op, ||QAQ||_op }
 =max{ ||PA'Q||_op, max_i ||Delta_i(A')||_op, ||QA'Q||_op }
 >3/8.`                                                          (2.26)

This proves the absolute-escape alternative. QED.

## 3. Spend the completed source-tail information: the escape is non-arm

The source packet preceding the common-Gram compiler has

`epsilon=0.0023595307563857772`

and its off-plane Frobenius tail implies that every plane/complement and complement/complement block on the six strong arms

`D_1-K_b`, `K_b-D_2`, `b=1,2,3`

has operator norm `<epsilon`. This was written out in the previous fleet01/B20 run.

There are 12 oriented strong-arm blocks inside either `PAQ` or `QAQ`. Their aggregate operator norm is at most `sqrt(12) epsilon`. Therefore the robust threshold (2.26) sharpens exactly as follows.

If `||PAQ||>3/8`, the non-arm part has norm greater than

`3/8-sqrt(12)epsilon`,

spread over at most 18 plane/complement blocks. Hence one non-arm physical plane/complement interaction satisfies

`||P_i A Q_r||_op
 > delta_PQ^(rob)
 :=(3/8-sqrt(12)epsilon)/sqrt(18)
 =0.0864617988531... .`                                          (3.1)

If `||QAQ||>3/8`, the non-arm part is spread over at most 24 complement/complement blocks, so one satisfies

`||Q_r A Q_s||_op
 > delta_QQ^(rob)
 :=(3/8-sqrt(12)epsilon)/sqrt(24)
 =0.0748781142637... .`                                          (3.2)

Thus the moderate-scale quantitatively nondegenerate finite collar is reduced to the exhaustive physical alternative

1. a paid E3 Schur defect;
2. a compressed same-node Gram self defect `>3/8`;
3. a NON-ARM physical plane/complement interaction `>0.08646`; or
4. a NON-ARM physical complement/complement interaction `>0.07487`.

The mandatory third mode cannot remain hidden on the six already-controlled source arms.

## 4. Concrete universal subcompiler

Take the fixed thresholds

`c=a`, `M=1`.                                                     (4.1)

Then

`delta_* = a^2/[8(21+2a)]
          =3.45191985840904e-8.`                                 (4.2)

If one Schur defect reaches this value, (1.4)-(1.5) give the explicit full-law payment

`||p_Q||_infinity
 < C_3 a^(-2/3) delta_*^(-1/3)
 =180336.0881... <180337,`                                       (4.3)

with continuous C0 density.

Consequently every unpaid state satisfying

`s_2(C)>=a`, `||C||<=1`, `max_b||A_b||<=1`                       (4.4)

must lie in one of the three non-paid escape resources in Section 3. Therefore the former undifferentiated finite-collar debt has been replaced by the explicit residual compiler

`QFORM-R37-C-SMALL-OR-HIGHSCALE-OR-NONARM-THIRDMODE-PAYMENT-v1`:

- `s_2(C)<a` (quantitative near-rank-one D_1-D_2 edge), or
- `||C||>1` or some `||A_b||>1` (high-scale canonical edge), or
- a same-node Gram self defect `>3/8`, or
- a non-arm plane/complement physical interaction `>0.08646`, or
- a non-arm complement/complement physical interaction `>0.07487`.

This is a genuine finite-collar robustification of the completed fleet02/B20 exact endpoint. It does not claim that these final non-arm/self/high-scale packets are already paid.

## 5. Scope / correction audit

- Full unrestricted QFORM remains OPEN.
- Global continuity remains OPEN; continuity is asserted only on the E3-paid branch.
- No uniform pointwise quadratic oscillatory decay is used.
- No post-rotation independence is used; all frames serve only deterministic coefficient geometry.
- No arbitrary-joint coarea or worst-fibre supremum is used.
- No conditional bounded-density cap is substituted for independence.
- No small nonzero random quadratic tail is deleted; the source tail is retained and used quantitatively.
- No aggregate volume is converted into a single large physical minor.
- Same-bank curvature, affine terms, exterior coordinates, exterior couplings and all extra spectrum remain in the full-law E3 receiver.
