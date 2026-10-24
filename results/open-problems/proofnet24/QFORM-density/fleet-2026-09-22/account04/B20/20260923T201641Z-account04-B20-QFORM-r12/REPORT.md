SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B20, 2026-09-23T20:16:41Z.
attacking: the first unproved whole-law implication after the rank-five double-anchor and exact-rank-three bank receivers; compress the surviving anchored third-volume packet into currencies visible to existing physical-pair, ridge, and volume estimates.

# account04/B20 r12 — exterior compression of the nested physical double anchor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T201641Z-account04-B20-QFORM-r12`  
Status: **ESSENTIAL_STEP_APPLIED / SUPPORTING STRUCTURAL COMPILER / FULL QFORM OPEN**  
Continuity: separate and still open outside branches already paid by their cited receivers.

The target is unchanged: arbitrary independent real coordinates with probability densities at most one, arbitrary real symmetric `A), any dimension, and at least three eigenvalues of `A` having modulus at least one. No iid, moment, support, smoothness, sign, or post-rotation independence hypothesis is introduced.

## 1. Source pins and correction boundary

This run consumes:

- reviewed Claude source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially physical cross-block theorem D' and its marginal gates;
- later Claude one-coordinate partner source `yspennstate/math-open-problems@92293ef443eb46467637799d3511b6dbd08201f7`;
- completed account01/B20 rank-five paving/double-anchor result `yspennstate/math-open-problems@bedc345f96a6cc7ee4fcbfc25b117aa0839f22f2`;
- account04 exact-rank-three three-bank packet `9d07c5d5c69c885509db66cb1093acdeff8bcb64`;
- account04 bankwise triple-curvature receiver `205481d65e155470ceb4eb37c1601679abbda5e0`;
- account04 physical-pair/bank overlap receiver `a70c05e517e8a195a31ab4f4c301c672d1c8d4e6`;
- brain state `yspennstate/math-research-brain@6f75599751b2942817ac11b236887ece73f9e09a`.

The live corrections are enforced. In particular, this report uses no independence after an orthogonal rotation, no arbitrary-joint coarea theorem, no worst-fibre conditional density cap, no uniform pointwise scalar quadratic Fresnel decay, and no deletion of a small nonzero quadratic tail.

## 2. The completed account01 input

In the aligned in-plane rank-at-most-five packet, account01/B20 proves the following exhaustive local outcome. Either:

1. the carrier has a physical leverage greater than `1/25`;
2. the full ambient density is paid with `||p_Q||_infinity<1353`; or
3. for a literal original-coordinate cross block `M=A[I,J]`, there are a physical row `i`, a physical column `j`, and disjoint residual banks
   [
   I\setminus\{i\}=I_1\dot\cup I_2,qquad
   J\setminus\{j\}=J_1\dot\cup J_2
   ]
   for which
   [
   \mathcal J_3^{\rm sep}(i,j):=
   \sum_{\substack{r_1\in I_1,r_2\in I_2\\c_1\in J_1,c_2\in J_2}}
   \det M[\{i,r_1,r_2\},\{j,c_1,c_2\}]^2
   >
   \delta,
   ]
   where
   [
   \delta=\frac{47045881}{12\cdot10^{18}}
   =3.920490083333\ldots\times10^{-12}.
   ]

The account01 theorem deliberately does not select one large minor. The sum is the useful invariant.

## 3. New exterior-compression lemma

Order the anchored block as
[
M=
\begin{pmatrix}
 b&r^\top\\
 c&N
\end{pmatrix},
]
where `b=M_{ij}`, `r` and `c` are the residual physical row and column stars restricted to the chosen banks, and `N=M[I_1\cup I_2,J_1\cup J_2]`. Let
[
E_2(N)=e_2(N^\top N)
      =\sum_{|R|=|C|=2}\det N[R,C]^2.
]

Define the full anchored mass
\[
\mathcal J_3^{\rm full}(i,j)
=\sum_{|R|=|C|=2}
\det M[\{i\}\cup R,\{j\}\cup C]^2.
\]
The completed account01 quantity is a restricted nonnegative sub-sum, hence
\[
\mathcal J_3^{\rm full}(i,j)\ge \mathcal J_3^{\rm sep}(i,j).
\tag{3.0}
\]

### Lemma 3.1 — `QFORM-ANCHORED-D3-EXTERIOR-COMPRESSION-v1`

For every real block matrix above,
[
\boxed{
\mathcal J_3^{\rm full}(i,j)^{1/2}
\le |b|E_2(N)^{1/2}
   +\|r\|_2\|c\|_2\|N\|_F.}
\tag{3.1}
]

Consequently,
[
\boxed{
\max\bigl\{
 b^2E_2(N),,
 \|r\|_2^2\|c\|_2^2\|N\|_F^2
\bigr\}
\ge \frac14\mathcal J_3^{\rm full}(i,j).}
\tag{3.2}
]

Both statements remain true if the sums defining `E_2` and `||N||_F` are enlarged from the four-bank support to the full residual block.

### Proof

Regard `N` as an operator from residual column space to residual row space. The coefficients of all anchored `3x3` minors form the Hilbert--Schmidt tensor
[
T=b\,\bigwedge^2N-(c\wedge\cdot)\,N\,\iota_r
]
(up to an immaterial consistent sign convention). Here
(iota_r:\bigwedge^2({\rm Col})\to {\rm Col})
is contraction by `r`, and
((c\wedge\cdot):{\rm Row}\to\bigwedge^2({\rm Row}))
is exterior multiplication by `c`.

The squared Hilbert--Schmidt norm of `T` is exactly the full sum of the squared anchored minors:
[
\|T\|_{HS}^2=\mathcal J_3^{\rm full}(i,j).
]
Also,
[
\|\bigwedge^2N\|_{HS}=E_2(N)^{1/2},qquad
\|\iota_r\|_{op}=\|r\|_2,qquad
\|c\wedge\cdot\|_{op}=\|c\|_2.
]
Therefore the Hilbert--Schmidt ideal inequality and the triangle inequality give
[
\|T\|_{HS}
\le |b|E_2(N)^{1/2}
 +\|c\|_2\|N\|_{HS}\|r\|_2,
]
which is (3.1). Since ((x+y)^2\le4\max\{x^2,y^2\}), (3.2) follows. Enlarging the supporting banks can only increase the nonnegative minor and Frobenius sums. QED.

Two endpoint identities are worth retaining:

- if `b=0`, then
  [
  \mathcal J_3^{\rm full}(i,j)
  \le\|r\|_2^2\|c\|_2^2\|N\|_F^2;
  ]
- if `b\ne0`, the literal Schur identity gives exactly
  [
  \boxed{
  \mathcal J_3^{\rm full}(i,j)
  =b^2E_2\!\left(N-\frac{cr^\top}{b}\right).}
  \tag{3.3}
  ]

Thus the near-zero and nonzero pivot regimes are linked without dividing by a small number in the general inequality.

## 4. Application to the live account01 survivor

Applying (3.0)--(3.2) to the nested packet in Section 2 gives
[
\boxed{
\max\bigl\{
 b^2E_2(N),,
 \|r\|_2^2\|c\|_2^2\|N\|_F^2
\bigr\}
>
\frac{47045881}{48\cdot10^{18}}
=9.801225208333\ldots\times10^{-13}.}
\tag{4.1}
]

This is an actual application of the completed account01/B20 mathematics. It converts its aggregate third-volume credit into an exhaustive two-currency split on the same original-coordinate matrix:

- **pivot-volume currency:** a literal physical coefficient times residual second exterior volume;
- **two-star currency:** two literal physical stars times residual cross-block Frobenius energy.

No individual minor, rotated product law, or conditional density bound is asserted.

The split is useful because its two terms align with different already-proved mechanisms: the first is a Schur/second-volume object and the second is a double-anchor/star object. The numerical verifier in this run explicitly sums the anchored minors and checks (3.1)--(3.2) for random rectangular blocks.

## 5. Current guarded proof graph

This is a noncircular dependency graph, not a claim that every arrow needed for the full theorem has been proved.

1. Literal large diagonal or literal `2x2` pivot branches are paid by their existing physical-coordinate receivers.
2. In the remaining no-pivot chamber, the three-singular cross-cut compiler supplies a literal original-coordinate cross block.
3. D5/D' pays sufficiently diffuse fifth/third volume; survivors enter the aligned top-four/rank-five packets.
4. The account01 rank-five carrier theorem gives: heavy carrier leverage `>1/25`, full payment `<1353`, or the nested anchored third-volume packet.
5. The new Lemma 3.1 turns the last outcome into the exhaustive quantitative split (4.1).
6. In the exact-rank-three Schur packet, the bankwise triple-curvature and physical-pair overlap receivers pay every bank with adequate Gram determinant, leaving only shear-flat, heavy-row/intermediate-volume, or source-entangled banks.

The unmatched edges are explicit:

- pay the pivot-volume term in (4.1) while retaining all same-side blocks, outside couplings, and small spectral tails;
- pay the two-star term in (4.1) under the same full ambient conditions;
- pay the rank-five heavy-carrier branch `max_i(P_{S_0})_{ii}>1/25`;
- close the shear-flat/source-entangled exact-rank-three hybrid;
- glue exact-rank-three payments to arbitrary additional spectrum without deleting its random quadratic contribution;
- close the punctured convex/two-sheet near-null collar.

These are genuine remaining implications. In particular, (4.1) is not itself a density estimate, and this report does not call the hybrid or convex side solved.

## 6. Scope and review audit

- Every row, column, bank, star, and pivot is in the original coordinate basis.
- Arbitrary input laws satisfying only independence and density cap one are retained.
- All signs and arbitrary remaining spectrum are retained in the target statement.
- Continuity is not inferred from bounded density.
- No peer receipt or end-to-end review is fabricated.
- The owner requirement for two independent end-to-end reviews becomes active only after a full candidate exists. This run does not claim such a candidate.

## 7. Bottom line

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The substantive advance is the source-valid compressor (3.1)--(4.1): the previously opaque nested physical double-anchor is now forced into one of two explicit original-coordinate currencies. The first next proof obligation is a whole-law receiver for one of these two currencies with arbitrary same-side leakage and additional-spectrum coupling retained.
