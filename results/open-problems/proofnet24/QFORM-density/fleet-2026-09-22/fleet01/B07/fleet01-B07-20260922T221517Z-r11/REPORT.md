SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-22T22:15:17Z.
attacking: coordinate-minor selection by an exact determinant-weighted row/column inclusion law, followed by conditioning on the two high-leverage physical anchors.

# fleet01/B07 — determinant-conditioned anchor selection

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `fleet01-B07-20260922T221517Z-r11`  
**Assignment:** coordinate minor selection / GEOMETRY  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING STRUCTURAL THEOREM / FULL TARGET OPEN`.

The target remains the full arbitrary-product-law statement: independent original coordinates with one-dimensional densities bounded by one, arbitrary real symmetric `A`, and only the hypothesis that at least three eigenvalues have modulus at least one. Nothing below uses post-rotation independence, arbitrary-joint coarea, a pointwise oscillatory decay estimate, a moment/support/log-concavity hypothesis, or reciprocal extraction of one tiny physical minor.

## 1. Conditional end-to-end map and designated partner application

The current O0 coordinate-minor route supplies a physical cross block `B` with

`E_3(B):=e_3(BB^T)>=1/256`.

The previous fleet01/B07 compound-order theorem gives

`E_2(B)^3 >= (9/2) E_3(B)^2`,

hence

`E_2(B)>=c_2:=(9/2^17)^(1/3)=0.0409490842845... >1/25`.

At the unique effective-dimension-two ridge scale `z>0`,

`tr K_L(z)=tr K_R(z)=2`,

where

`K_L=zBB^T(I+zBB^T)^(-1)`,
`K_R=zB^TB(I+zB^TB)^(-1)`.

The completed fleet03/B07 ridge-collar theorem says that if either side has maximum leverage at most `23/24`, the half-Riesz branch is paid. Thus the hard branch has physical anchors `i,j` satisfying

`ell_i:=(K_L)_(ii)>23/24`, `ell_j:=(K_R)_(jj)>23/24`.

The designated partner fleet02/B07 r18 result `QFORM-TWOSTAR-CHECKERBOARD-WEDGE-v1` is source-pinned at

`yspennstate/math-open-problems@d4afa77929c3a9b5322f451c6d470fcfe519f01b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T213439Z-fleet02-B07-QFORM-e7b269/REPORT.md`.

Writing the old physical cross block around those anchors as

`B=[[b,r^T],[c,C]]`

and the same-side anchor couplings as `u,v`, that theorem puts the two anchors on one side of a new physical cut and obtains

`D=[[u^T,r^T],[c^T,v^T]]`,

`E_2(D)=||u wedge c||^2+||r wedge v||^2+||uv^T-cr^T||_F^2`.

In the two-star branch `P=||r||^2||c||^2>1/200`, if

`E_2(D)>=P/16`,

then the completed two-cross theorem gives the actual inequality

`H_(1/2) < 8*3200^(1/8)=21.9398540541...`.

I therefore apply the partner theorem and work only in its surviving near-leaf branch

`E_2(D)<P/16`,

where there is a scalar `alpha` such that

`||u-alpha c||^2+||r-alpha v||^2 < ||r||^2/16`,

with the symmetric companion estimate. The new mathematics below tracks the *same physical anchors* through the entire determinant bank instead of selecting one local minor.

## 2. Determinant-weighted minor measure

Let `B` be any real `m x n` matrix. For `z>0` define

`D_B(z):=det(I_m+zBB^T)`.

Cauchy--Binet gives the exact expansion

`D_B(z)=sum_(k>=0) z^k E_k(B)`,

where

`E_k(B)=sum_(|I|=|J|=k) det B[I,J]^2`.

Thus

`mu_z(I,J):=z^|I| det B[I,J]^2 / D_B(z)`, `|I|=|J|`,

is a probability measure on pairs of equal-size physical row/column sets. Put `N=|I|=|J|`.

If the nonzero singular values of `B` are `sigma_nu`, then

`E[s^N]=D_B(sz)/D_B(z)=prod_nu[(1-lambda_nu)+lambda_nu s]`,

with

`lambda_nu=z sigma_nu^2/(1+z sigma_nu^2)`.

Consequently `N` is Poisson-binomial and

`E N=sum_nu lambda_nu=tr K_L=tr K_R`.

At the effective-dimension-two scale used above, `E N=2` exactly.

## 3. New theorem: exact joint row/column anchor inclusion

Define

`H(z):=sqrt(z) B(I_n+zB^TB)^(-1)`.

### Theorem 3.1 — `QFORM-GRAPH-DPP-JOINT-ANCHOR-v1`

For every physical row `i` and physical column `j`,

`mu_z(i in I)=ell_i=(K_L)_(ii)`,

`mu_z(j in J)=ell_j=(K_R)_(jj)`,

and, crucially,

`boxed( mu_z(i in I, j in J)=ell_i ell_j + H_ij^2. )`            (3.1)

This is stronger than the elementary union lower bound `ell_i+ell_j-1` and is exact.

### Proof

Form the `(m+n) x n` graph matrix

`G=[sqrt(z)B ; I_n]`.

The orthogonal projection onto its column space is

`Pi=G(G^TG)^(-1)G^T`

with block form

`Pi=[[K_L,H],[H^T,I-K_R]]`.

The fixed-size projection determinantal measure on `n` selected elements satisfies

`P(S)=det Pi[S,S]`.

Write a selected set uniquely as

`S=I union (J^c)`,

where `I` is a row set and `J^c` denotes graph-column elements. Necessarily `|I|=|J|`. Since

`det Pi[S,S]=det(G_S)^2/det(G^TG)=z^|I| det B[I,J]^2/D_B(z)`,

this projection-DPP is exactly `mu_z` under the correspondence above.

Row element `i` is selected iff `i in I`, whereas graph-column element `j` is *not* selected iff `j in J`. The two-point determinantal identity gives

`P(i selected, graph-j selected)=ell_i(1-ell_j)-H_ij^2`.

Subtracting from `P(i selected)=ell_i` proves (3.1). QED.

Equivalently, if

`M_k(i,j):=sum_(|I|=|J|=k, i in I, j in J) det B[I,J]^2`,

then

`F_ij(z):=sum_(k>=1) z^k M_k(i,j)`

satisfies

`F_ij(z)/D_B(z)=ell_i ell_j+H_ij^2`.                              (3.2)

The same identity follows by inclusion--exclusion from row/column-deleted regularized determinants, but (3.1) exposes its probabilistic meaning.

## 4. High-leverage anchors force a low-order determinant bank

Return to the hard effective-dimension-two branch

`ell_i,ell_j>23/24`.

By (3.1), for the event `A={i in I,j in J}`,

`p_A:=P(A)> (23/24)^2=529/576`.                                  (4.1)

Let

`q_k=P(A,N=k)=z^k M_k(i,j)/D_B(z)`.

Because `A` forces `N>=1`,

`p_A=sum_(k>=1)q_k`.

Moreover

`2=E N >= E[N 1_A]>=q_1+2q_2+3 sum_(k>=3)q_k`

`=3p_A-2q_1-q_2`.

Therefore

`boxed( 2q_1+q_2 >=3p_A-2 >145/192. )`                          (4.2)

Since `M_1(i,j)=b^2`, (4.2) is the exact determinant-weighted physical-anchor inequality

`boxed(
 2 z b^2/D_B(z) + z^2 M_2(i,j)/D_B(z) >145/192.
)`                                                               (4.3)

In particular at least one of

`z b^2/D_B(z)>145/768`,                                          (4.4)

`z^2 M_2(i,j)/D_B(z)>145/384`                                    (4.5)

holds. This is an *aggregate-before-inversion* selection statement: the second alternative keeps the complete anchored two-by-two determinant bank.

The absolute constants inherited from O0 are also explicit. Since

`E_1(B)^3>=6E_3(B)>=3/128`

and the previous compound transfer gives `E_2(B)>=c_2`, while

`D_B(z)>=zE_1(B)`, `D_B(z)>=z^2E_2(B)`,

(4.4) implies

`b^2 > (145/768)(3/128)^(1/3)=0.05403110845...`,

hence

`|b|>0.2324459258...`;                                           (4.6)

whereas (4.5) implies

`M_2(i,j)>(145/384)c_2=0.01546254485...`.                        (4.7)

The existing ridge-collar theorem already gives the stronger unweighted `M_2(i,j)>E_2/2>1/50`; the new information in (4.3)--(4.5) is the *regularized determinant share* at the same ridge scale.

### Zero direct edge

If `b=0`, then `q_1=0`, so (4.2) sharpens to

`boxed(
 z^2 M_2(i,j)/D_B(z)>145/192=0.7552083333... .
)`                                                               (4.8)

Here

`M_2(i,j)=||c r^T||_F^2=||c||^2||r||^2=P`.

Thus in the genuine zero-edge two-star obstruction, more than 75.5 percent of the *entire regularized determinant* is carried by the single aggregate two-star determinant bank. Higher-order/core minors cannot dominate this ridge-scale bookkeeping. This is substantially stronger than merely knowing `P>1/200`.

## 5. Nonzero direct edge: exact conditional Schur law and dimension drop

Assume now `b!=0`, and put

`C^sharp:=C-c r^T/b`.

### Theorem 5.1 — `QFORM-ANCHOR-CONDITIONED-SCHUR-DROP-v1`

For every `s>=0`,

`boxed( M_(s+1)(i,j)=b^2 E_s(C^sharp). )`                        (5.1)

Consequently

`boxed( F_ij(z)=z b^2 det(I+z C^sharp(C^sharp)^T). )`            (5.2)

Conditioned on `A={i in I,j in J}`, the remaining row/column sets have exactly the determinant-weighted law of `C^sharp` at the same parameter `z`. In particular,

`N-1 | A`

is Poisson-binomial with mean

`tau_sharp(z):=tr[z C^sharp(C^sharp)^T(I+z C^sharp(C^sharp)^T)^(-1)]`.

In the hard effective-dimension-two branch,

`boxed( tau_sharp(z)<623/529=1.1776937618... . )`                (5.3)

### Proof

Every anchored `(s+1)x(s+1)` minor has block form

`[[b,r_J],[c_I,C_(I,J)]]`.

Its determinant is exactly

`b det(C_(I,J)-c_I r_J^T/b)=b det C^sharp[I,J]`.

Squaring and summing proves (5.1), and summing over `s` proves (5.2). Division by (5.2) shows that the conditional residual sets have the determinant measure of `C^sharp`.

Therefore

`1+tau_sharp=E[N|A]`.

But

`E[N 1_A]<=E N=2`,

so, using (4.1),

`1+tau_sharp <=2/p_A <2/(529/576)=1152/529`,

which is (5.3). QED.

Thus a nonzero high-leverage row/column anchor does not merely identify a large local coefficient. **After exact determinant-weighted conditioning on that physical anchor pair, the residual cross Schur matrix drops from effective dimension two to less than 1.178 at the same ridge scale.** This is a dimension-free conditioning identity. It is only a structural statement: `C^sharp` is a rank-one-updated cross matrix, not automatically an admissible independent-coordinate block to which a product-law density theorem can be applied without an additional conditioning argument.

## 6. Zero-edge core retained exactly: screened-star / through-core bridge identity

The partner's exact stress example shows that `b=0` is a real survivor, so it is useful to keep the arbitrary cross core `C` instead of deleting it.

For

`B=[[0,r^T],[c,C]]`,

set

`D_C=det(I+zCC^T)`,
`A_C=(I+zCC^T)^(-1)`,
`R_C=(I+zC^TC)^(-1)`,

`alpha=z c^T A_C c`,
`beta =z r^T R_C r`,
`gamma=z^(3/2) c^T A_C C r`.

### Theorem 6.1 — `QFORM-ZEROEDGE-SCREENED-STAR-OR-BRIDGE-v1`

One has the exact identities

`boxed(
 D_B=D_C[(1+alpha)(1+beta)+gamma^2],
 F_ij=D_C[alpha beta+gamma^2].
)`                                                               (6.1)

Hence

`p_A=(alpha beta+gamma^2)/[(1+alpha)(1+beta)+gamma^2]`.           (6.2)

Under the same high-leverage hypothesis (4.1),

`boxed(
 alpha beta+gamma^2 > (529/47)(1+alpha+beta).
)`                                                               (6.3)

Therefore either

`alpha beta >=(529/94)(1+alpha+beta)`,                            (6.4)

in which case necessarily

`alpha>529/94` and `beta>529/94`,                                (6.5)

or

`gamma^2 >=(529/94)(1+alpha+beta)`.                              (6.6)

So the zero-edge two-star survivor has an exact alternative: **both star arms remain large even after screening by the arbitrary cross core**, or a quantitatively large resolvent-mediated bridge passes through that core.

### Proof

Write

`I+zBB^T = [[1+z||r||^2, z r^T C^T], [zCr, I+zCC^T+zcc^T]]`.

The lower-right determinant is `D_C(1+alpha)`. Sherman--Morrison gives its inverse. Using

`I-zC^T(I+zCC^T)^(-1)C=(I+zC^TC)^(-1)=R_C`,

the Schur complement of the lower-right block equals

`1+beta+gamma^2/(1+alpha)`.

This proves the first identity in (6.1). Deleting the anchor row gives `D_C(1+alpha)`, deleting the anchor column gives `D_C(1+beta)`, and deleting both gives `D_C`; inclusion--exclusion yields the second identity. Equation (6.3) is (6.2) together with `p_A>529/576`; (6.4)--(6.6) are the elementary two-term split. QED.

The screened quantities retain the arbitrary core exactly. No coordinate rotation is being used.

## 7. What the designated partner result plus the new identities now reduce

Applying fleet02/B07 r18 first gives the following exhaustive local map for the O0 two-star survivor.

1. If the partner checkerboard wedge satisfies `E_2(D)>=P/16`, then the existing two-cross theorem pays the residual by `H_(1/2)<21.940`.
2. Otherwise the anchor outside-coupling rows are quantitatively near proportional (the partner's near-leaf branch).
3. For those same physical high-leverage anchors, the new graph-DPP identity forces (4.3). If the direct edge vanishes, the aggregate two-star bank alone carries `>145/192` of the complete regularized determinant.
4. If the direct edge is nonzero, conditioning the determinant bank on the two anchors is *exactly* the Schur determinant law (5.1)--(5.2), and its residual effective dimension is `<623/529`.
5. In the zero-edge case, arbitrary core curvature is reduced exactly to the screened-star / through-core alternative (6.4)--(6.6), instead of being thrown away by a triangle inequality.

This is a stricter structural reduction than the previous generic `near-leaf or edge-bank` description.

## 8. First unpaid implication

The first unpaid implication is now

**`QFORM-NEARLEAF-CONDITIONED-RANKONE-TRANSDUCER-v1`.**

In the partner near-leaf branch, convert one of the following exact determinant-weighted states into a product-preserving half-Riesz/density estimate while retaining arbitrary same-bank quadratic curvature:

- `b=0` and the physical two-star anchored bank contributes more than `145/192` of `D_B(z)`; equivalently use the screened-star / through-core split (6.4)--(6.6); or
- `b!=0` and the exact conditioned cross Schur matrix has effective dimension `<623/529` at the same ridge scale.

A valid transducer must keep the original anchor variables and outside product coordinates independent under conditioning. One may not simply rotate to the near-leaf linear combination, and one may not treat `C^sharp` as a fresh physical product block without justifying that passage.

The current result does **not** prove the full QFORM conjecture and does not prove global continuity. It is an exact determinant-weighted selection/conditioning theorem aimed at the remaining coordinate-minor bottleneck.

## 9. Exact regression checks

A separate exact checker verifies on rational matrices:

- Cauchy--Binet `F_ij=sum z^k M_k`;
- the graph-projection joint inclusion identity (3.1);
- the anchored Schur identities `M_(s+1)=b^2E_s(C^sharp)` and (5.2);
- the zero-edge determinant identities (6.1);
- the exact fractions `529/576`, `145/192`, `145/768`, `145/384`, and `623/529`.

These finite checks are regression evidence only; the proofs are the algebra above.
