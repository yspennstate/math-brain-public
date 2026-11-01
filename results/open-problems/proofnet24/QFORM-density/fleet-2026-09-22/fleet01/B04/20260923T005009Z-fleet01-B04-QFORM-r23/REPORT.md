SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T00:50:09Z.
attacking: N3 high-volume-marginal obstruction via an aggregate heavy-row/heavy-column Schur-volume identity, then route its exact currencies into product-Fourier branches.

# fleet01/B04 r23 — double-heavy volume sampling forces exact Schur 2-volume or a zero-edge mixed hub

Programme: `QFORM-DENSITY-3EIG-20260922`. Owner control observed fresh at revision `2026-09-22.15`. Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_LEMMA_PROVED / FULL_TARGET_OPEN`. Execution: `WITHOUT_VERIFIED_BRAIN`.

The full conjecture is NOT proved here. Full-target continuity is NOT proved here. This run works directly on the latest N3 no-pivot reduction and preserves the live corrections: no law-uniform one-dimensional pointwise quadratic-phase decay; no independence after spectral rotation; no arbitrary-joint coarea; no worst conditional-density moment; no inference from aggregate E2 alone to two uniformly large singular values; and no local-packet selection before aggregation.

## 1. Conditional end-to-end route

Fix the N3 threshold `tau in (0,1]`. Thus all physical diagonals obey `|A_ii|<tau`, all physical two-coordinate principal determinants obey

`|A_ii A_jj - A_ij^2|<tau`,

and the global matrix has at least three eigenvalues of modulus at least one.

For any disjoint original-coordinate cut `I sqcup J`, put `M=A_IJ` and

`Z_3(M)=e_3(M M^T)=sum_{|S|=|T|=3} det(M_ST)^2`,
`Z_5(M)=e_5(M M^T)`.

The newest Claude Fourier report supplies two already-paid exits:

1. if `Z_5(M)` is quantitatively positive, D5 gives a density bound with no marginal restriction;
2. if `Z_3(M)` is quantitatively positive and the volume-sampling row marginals on one orientation are uniformly `<3/4`, D' gives a density bound.

Therefore, on a cut carrying useful third-volume but escaping D' in BOTH orientations, one has a row `i` and a column `j` whose third-volume marginals are both at least `3/4`. The first unpaid structural step is to identify what that simultaneous concentration forces without selecting a single local 3x3 minor. The theorem below does exactly that, and is stronger than the preliminary cofactor triangle inequality: when the heavy-heavy edge is nonzero, the relevant aggregate is exactly the second volume of its Schur cross bank.

If the aggregate currency below can be paid directly by an averaged-frequency/mixed-Fresnel estimate, or routed to D5/ridge/grouped-coordinate branches, then the N3 class closes. The latest Claude Gaussian-padding reduction then upgrades N3 to the full theorem. This final aggregate smoothing/routing implication remains open.

## 2. Double-heavy Schur-volume theorem

Let `M=(m_ij)` be any real matrix with `Z=Z_3(M)>0`. Put the canonical third-volume sampling law

`w_ST = det(M_ST)^2/Z`,  `|S|=|T|=3`.

Define its row and column marginals

`alpha_i = sum_{S contains i,T} w_ST`,
`beta_j  = sum_{S,T contains j} w_ST`.

For fixed `i,j`, define the joint third-volume mass

`Z_ij = sum_{S contains i,T contains j} det(M_ST)^2`.

### Theorem 2.1 — `QFORM-D3-DOUBLE-HEAVY-SCHUR-VOLUME-v1`

If `alpha_i >= h` and `beta_j >= h` for some `h>1/2`, then

`Z_ij >= (2h-1) Z`.                                                (2.1)

Write the full cut around the distinguished row and column as

`M = [[a,r^T],[c,N]]`, `a=m_ij`,                                  (2.2)

where `N=M_{I\{i},J\{j}}`.

If `a != 0`, define the cross Schur bank

`S = N - c r^T/a`.                                                (2.3)

Then the following exact identity holds:

`Z_ij = a^2 e_2(S S^T)`.                                         (2.4)

Consequently

`a^2 e_2(S S^T) >= (2h-1) Z`.                                   (2.5)

At the D' obstruction threshold `h=3/4`,

`a^2 e_2(S S^T) >= Z/2`.                                         (2.6)

If instead `a=0`, write for every `|P|=|Q|=2`

`H_ij = sum_{P,Q} [r_Q^T adj(N_PQ)c_P]^2`.                        (2.7)

Then in this zero-edge case

`H_ij = Z_ij >= (2h-1)Z`,                                        (2.8)

and at `h=3/4`, `H_ij>=Z/2`.

#### Proof

Under the probability law `w`, the events `R={i in S}` and `C={j in T}` have probabilities `alpha_i` and `beta_j`. Hence

`P(R intersect C) >= P(R)+P(C)-1 >= 2h-1`,

which after multiplying by `Z` proves (2.1).

Every contributing minor has the form

`M_{iP,jQ} = [[a,r_Q^T],[c_P,N_PQ]]`, `|P|=|Q|=2`.                (2.9)

If `a!=0`, the scalar Schur determinant identity gives

`det(M_{iP,jQ}) = a det(N_PQ-c_P r_Q^T/a) = a det(S_PQ)`.         (2.10)

Squaring and summing over every `P,Q` gives

`Z_ij = a^2 sum_{P,Q} det(S_PQ)^2
      = a^2 e_2(S S^T)`,                                         (2.11)

by Cauchy--Binet, proving (2.4)-(2.6).

If `a=0`, Laplace expansion gives

`det(M_{iP,jQ}) = - r_Q^T adj(N_PQ)c_P`.                          (2.12)

Squaring and summing proves (2.8). QED.

### N3 specialization

In N3(tau), for every physical pair `(i,j)`,

`A_ij^2 <= |A_ii A_jj| + |A_ii A_jj-A_ij^2|
          < tau^2+tau = tau(1+tau) <= 2tau`.                       (2.13)

Thus simultaneous D' failure on both orientations gives a heavy row/column pair `(i,j)` with the following exact alternatives.

If `a=A_ij !=0`,

`e_2(S S^T) >= Z/[2 a^2]
             > Z/[2 tau(1+tau)]
             >= Z/(4tau)`.                                      (2.14)

If `a=0`,

`H_ij >= Z/2`.                                                    (2.15)

This is an aggregate statement. Equation (2.14) is NOT promoted to two individually robust singular values, and (2.15) is NOT promoted to one individually robust `(P,Q)` packet. Those stronger local-selection moves are explicitly blocked by current correction evidence. The useful conclusion is sharper: simultaneous D' failure transfers at least half of the original third-volume exactly into a heavy-edge Schur second-volume (when `a!=0`), or into the zero-edge mixed-hub cofactor currency (when `a=0`).

## 3. Product-space interpretation

For `a!=0`, the bilinear part admits the exact original-coordinate completion

`a x_i y_j + x_i r^T y + y_j c^T x + x^T N y
 = a (x_i+c^Tx/a)(y_j+r^Ty/a) + x^T S y`.                        (3.1)

No spectral rotation of the random inputs occurs. Conditional on the residual original coordinates `(x,y)`, the translated distinguished variables retain density cap one and remain independent. Therefore (2.14) is precisely the aggregate rank-two currency left after completing the heavy hyperbolic edge.

For `a=0`, the cofactor term in (2.12) records the two-arm mixed hub from the distinguished row and column through the residual bank. The aggregate `H_ij` is the squared compound norm of those hub cofactors. This is the algebraic object that a mixed-Fresnel or averaged-frequency estimate must consume directly.

The remaining debt is analytic, not algebraic: derive a density/fractional-potential estimate from the Schur `e_2` or zero-edge cofactor aggregate BEFORE selecting a local packet. The live correction `local collision before aggregation is false` is therefore respected.

## 4. Named OTHER-account result applied to an actual N3 inequality

I apply the completed fleet02/B04 r22 theorem `QFORM-RANKR-TWOSIDED-CONTAMINATION-FOURIER-v1` at its exact scope. It states that for an exact-rank `r>=3` physical cross packet with nonzero singular values `sigma_1,...,sigma_r`, arbitrary within-bank contamination on both original-coordinate banks is allowed, and

`||p_H||_infinity <= e r/(r-2) Delta^(-1/r)`,
`Delta=product sigma_k`.                                         (4.1)

Take the dense Householder reflection

`M = I_3-(2/3)11^T
   = [[ 1/3,-2/3,-2/3],
      [-2/3, 1/3,-2/3],
      [-2/3,-2/3, 1/3]]`.                                       (4.2)

It is orthogonal with determinant `-1`, hence all three singular values equal one. Let

`A=[[0,M],[M,0]]`.                                                (4.3)

Then `A` has eigenvalues `+1` and `-1`, each with multiplicity three, so it satisfies the original target with six eigenvalues of modulus one. It is genuinely rotated/indefinite and every cross entry is nonzero.

Moreover it lies in `N3(1/2)`: all physical diagonals are zero; same-bank two-coordinate principal determinants vanish; cross-bank two-coordinate principal determinants equal `-m_ij^2`, of absolute value `1/9` or `4/9`, all strictly below `1/2`.

Equation (4.1), with `r=3` and `Delta=1`, gives for EVERY admissible independent cap-one product law

`||p_(X^T A X)||_infinity <= 3e = 8.154845485377136...`.          (4.4)

Because the partner's `r>=3` proof has an integrable characteristic function, this particular example has a continuous density. This is an actual N3 application, not a diagonal or post-rotation argument.

The example also illustrates Theorem 2.1 in its exact Schur form. There is exactly one 3x3 volume minor, so all row and column marginals equal one. With `i=j=1`,

`a=1/3`,
`N=[[1/3,-2/3],[-2/3,1/3]]`,
`r=c=(-2/3,-2/3)^T`,
`S=N-c r^T/a=[[-1,-2],[-2,-1]]`.                                (4.5)

Here `det S=-3`, so

`a^2 e_2(S S^T)=a^2 det(S)^2=(1/9)*9=1=Z_ij=Z`.                 (4.6)

This maximally double-heavy D' failure therefore becomes a large Schur rank-two aggregate after the heavy edge is completed. It is closed here because the original full cross packet has exact rank three, allowing the partner theorem directly.

## 5. What is and is not paid

Paid in this run:

- exact joint-volume lower bound for simultaneous heavy row/column third-volume marginals;
- exact identity `Z_ij=a^2 e_2(SS^T)` for every nonzero distinguished heavy edge;
- exact zero-edge identity `Z_ij=H_ij`;
- at the D' threshold, transfer of at least `Z/2` into the corresponding aggregate currency;
- in N3, `e_2(SS^T)>=Z/[2tau(1+tau)]>=Z/(4tau)` whenever the heavy edge is nonzero;
- an actual application of the designated OTHER-account fleet02/B04 exact-rank-three Fourier theorem to a genuinely rotated indefinite N3 matrix, with explicit constant `3e` and continuity for that branch.

Not paid:

- a dimension-free lower bound on `Z_3` for some cut from `s_3(A)>=1` alone;
- a direct density estimate from large aggregate Schur `e_2` when the Schur bank has extra tiny singular directions;
- a direct density estimate from large aggregate zero-edge `H_ij`;
- the full N3 theorem;
- the full QFORM conjecture;
- full-target continuity.

## 6. First unpaid implication

`QFORM-N3-SCHUR-E2-OR-ZEROEDGE-HUB-SMOOTHING-v1`:

Given an N3 cut with useful `Z_3` and simultaneous row/column D' obstruction, consume one of the exact alternatives

`a != 0:  a^2 e_2(SS^T) >= Z/2`,

or

`a = 0:  H_ij >= Z/2`,

by an averaged-frequency/product-space inequality WITHOUT selecting a single residual minor or asserting two individually large residual singular values. In the nonzero-edge branch the form already has the exact completed-hyperbolic decomposition (3.1); in the zero-edge branch the aggregate is the two-arm hub compound norm. A successful proof may combine these with the newest mixed-Fresnel theorem, D5, or the regularized ridge determinant on the same matrix.

This is strictly narrower than the preceding generic `packet extraction` gap: the exact post-completion aggregate is now identified.

Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_LEMMA_PROVED / FULL_TARGET_OPEN`.
