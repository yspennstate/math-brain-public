# Addendum — quantitative tetrad stability in the strong-triangle / row-bounded chamber

Run `20260924T044522Z-account01-B19-QFORM-auto11-r12`.

This addendum attacks the first quantitative gap left by `QFORM-DISJOINT-TETRAD-RIGIDITY-v1`. It does not solve the no-strong-triangle branch.

Let `S=S^T` be a real symmetric matrix and define

`W_dis(S)=sum det S[I,J]^2`,

where the sum is over ordered disjoint two-subsets `I,J`. Put

`omega=sqrt(W_dis(S))`.

## Theorem — `QFORM-TETRAD-STRONGTRIANGLE-STABILITY-v1`

Assume there are three distinct physical anchors `a,b,c` such that

`|S_ab|, |S_ac|, |S_bc| >= mu >0`.                               (1)

Let

`U=V\{a,b,c}`

and assume only the row-size bound

`||(S_ai)_(i in U)||_2 <= R`.                                    (2)

Then there are a diagonal matrix `Delta` and a symmetric rank-one matrix `K` such that

`boxed: ||S-Delta-K||_F`
` <= omega*(4/mu + R/mu^2).`                                     (3)

All signs are allowed. No dimension enters the bound.

### Proof

Set

`gamma=S_bc/(S_ab S_ac)`.                                        (4)

Define `v` by

`v_a=1/gamma`,
`v_i=S_ai` for every `i!=a`,                                     (5)

and put

`K=gamma v v^T`.                                                  (6)

Then `K` is symmetric rank one and it matches the three anchor edges and every edge out of `a` exactly:

`K_ai=S_ai`, `K_ab=S_ab`, `K_ac=S_ac`, `K_bc=S_bc`.              (7)

Write, on `U`,

`x_i=S_ai`, `y_i=S_bi`, `z_i=S_ci`.                              (8)

The tetrad minors with rows `{a,b}` and columns `{c,i}` give

`S_ac y_i-S_bc x_i`.                                              (9)

Their squared sum over `i in U` is a sub-sum of `W_dis(S)`. Hence

`|| y-(S_bc/S_ac)x ||_2 <= omega/|S_ac| <= omega/mu`.             (10)

Likewise, from rows `{a,c}` and columns `{b,i}`,

`|| z-(S_bc/S_ab)x ||_2 <= omega/mu`.                             (11)

Thus the `b-U` and `c-U` rows of `S-K` each have Euclidean norm at most `omega/mu`.

For distinct `i,j in U`, use the tetrad with rows `{a,i}` and columns `{b,j}`:

`d_ij=S_ab S_ij-S_aj S_ib`.                                      (12)

The squared sum of these `d_ij` is again at most `W_dis(S)`. Since

`gamma S_ab=S_bc/S_ac`,                                          (13)

we have

`S_ab (S_ij-gamma x_i x_j)`
` = d_ij + x_j [y_i-(S_bc/S_ac)x_i]`.                            (14)

Therefore the off-diagonal `U x U` block obeys

`||offdiag((S-K)[U,U])||_F`
` <= omega/|S_ab|`
`    + ||x||_2 ||y-(S_bc/S_ac)x||_2/|S_ab|`
` <= omega/mu + R omega/mu^2.                                    (15)

Now choose

`Delta=diag(S-K)`.                                                (16)

The matrix `E=S-Delta-K` has zero diagonal. Its only nonzero blocks are the symmetric copies of the `b-U`, `c-U` errors and the off-diagonal `U x U` block. By the triangle inequality in Frobenius norm,

`||E||_F`
` <= sqrt(2) omega/mu + sqrt(2) omega/mu`
`    + omega/mu + R omega/mu^2`
` = (1+2sqrt(2)) omega/mu + R omega/mu^2`
` < 4 omega/mu + R omega/mu^2`.                                  (17)

This is (3). QED.

## Corollary in the physical-pair Schur setting

For the exact physical pair `T` of the main report,

`W_T=D^2 W_dis(S)`,                                               (18)

so

`omega=sqrt(W_T)/D`.                                              (19)

Thus, if the Schur remainder has a physical anchor triangle satisfying (1) and the anchor row bound (2),

`boxed: dist_F(S,{diagonal + rank<=1})`
` <= (sqrt(W_T)/D)*(4/mu+R/mu^2).`                               (20)

This is a dimension-free quantitative stability theorem through small nonzero incident four-volume in the nondegenerate triangle chamber. It uses the full aggregate `W_T`; it does not select or reciprocate one tiny tetrad minor.

Consequently the first missing coverage statement narrows again. A small-`W_T` survivor must now enter at least one of:

1. no physical Schur triangle has all three edges at a fixed scale `mu`;
2. an anchor row is large (a physical star resource);
3. the Schur matrix is quantitatively close to physical diagonal plus rank one, hence must be coupled to the retained third target resource rather than discarded as a perturbation.

The newest account02/B19 exact rank-three stress lies in branch 3 with `W_T=0` exactly; its full law is correctly paid only after the third square is retained jointly.

## Regression check

On 1000 random `8 x 8` signed rank-one-plus-diagonal matrices perturbed by small symmetric off-diagonal noise, with anchors `{0,1,2}` satisfying the strong-triangle hypothesis, the exact constructed `K` above obeyed (3) in every sample; the largest observed ratio `lhs/rhs` was `0.1189238542`. This is only a numerical regression check; the proof is (4)-(17).

Status: **PROVED SUPPORTING DETERMINISTIC LEMMA / FULL QFORM STILL OPEN**.
