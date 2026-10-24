SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B07, 2026-09-22T18:36:53Z.
attacking: the surviving O0 one-heavy exclusion branch; turn a second exclusion-heavy physical row into either a bounded-cardinality determinant bank or a quantified two-coordinate replacement/near-coloop.

# account03/B07 — exclusion-heavy pair dichotomy and bounded-cardinality regularized minor bank

**Run:** `20260922T183653Z-account03-B07-qform-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection  
**Fresh owner control:** revision `2026-09-22.11`; programme remains exclusively QFORM.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING STRUCTURAL THEOREM / FULL TARGET OPEN`.

## 1. Exact target and incoming state

The owner target is unchanged: for every finite `n`, every independent real `X_i` with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has an essentially bounded density with one universal finite constant, or give a target-valid counterexample. Continuity is a separate strengthening.

This proof uses only original-coordinate cross blocks and determinant-weighted laws. It does not use post-rotation independence, law-uniform pointwise van der Corput decay, unrestricted fiber suprema, the refuted arbitrary-joint rank-three coarea lemma, the refuted worst scalar-conditioned core supremum, or selection followed by reciprocal payment of one tiny physical minor.

The incoming B07 theorem is `QFORM-O0-ONE-HEAVY-EXCLUSION-COLLAR-v1`, canonical source

`yspennstate/math-open-problems@54e57957ed371362e28d0699ccb9a7b8e55e9238`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T180507Z-account03-B07-qform-r14/REPORT_FINAL.md`.

In the O0 branch there is an original-coordinate cross block `B` with effective-dimension-three ridge kernel

`L=gamma^(-2) B B^T`, `K=L(I+L)^(-1)`, `tr K=3`,                   (1.1)

or the rank-three limiting interpretation. The diffuse branch `max diag K<3/4` is already paid. The preceding one-row deletion theorem pays every heavy row `i` with

`3/4 <= ell:=K_ii <=7/8`                                       (1.2)

unless, after excluding `i`, a second physical row is conditionally heavy. More precisely, on `C={i}^c` the exclusion kernel is

`K^(-i)=K_CC+K_Ci K_iC/(1-ell)`,                              (1.3)

and an unpaid survivor has some `j in C` with

`m:=(K^(-i))_jj >=1/2`.                                       (1.4)

The branch `ell>7/8` is already isolated as a one-row near-coloop. The purpose of this run is to classify (1.2)-(1.4) without throwing away determinant weight.

The designated `account04/B07` still has no completed current-QFORM canonical directory or shared handoff at the fresh source check. No result is fabricated for it. A compatible completed account04 result is applied below at its exact scope: account04/B16, `QFORM-NESTED-HEAVY-ZERODIAG-ATOM-v1`, source

`yspennstate/math-open-problems@54e57957ed371362e28d0699ccb9a7b8e55e9238`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`.

## 2. Exact two-row determinant identities

Fix `i,j` as above and write

`d=K_jj`, `s=K_ij`,
`g=det K[{i,j},{i,j}]=ell*d-s^2`.                              (2.1)

Because `0<=K<=I`, one has `0<=g` and the two-point DPP identities below are valid. From (1.3),

`m=d+s^2/(1-ell)`.                                            (2.2)

Eliminating `s^2` between (2.1)-(2.2) gives the first key identity

`boxed(d=(1-ell)m+g.)`                                        (2.3)

Likewise

`det(I-K[{i,j},{i,j}])
 =1-ell-d+g
 =(1-ell)(1-m).`                                              (2.4)

Now let `nu` be the `L`-ensemble on row subsets,

`nu(S)=det L[S,S]/det(I+L)`.                                  (2.5)

Its marginal kernel is `K`. Therefore

`P_nu(i in S)=ell`,
`P_nu(j in S | i notin S)=m`,
`P_nu(i,j in S)=g`,                                           (2.6)

and (2.3)-(2.4) are equivalently the exact occupancy formulas

`P_nu(i notin S, j notin S)=(1-ell)(1-m)`,                    (2.7)
`P_nu(i in S, j notin S)=ell-g`,                              (2.8)
`P_nu(i notin S, j in S)=(1-ell)m`,                           (2.9)
`P_nu(exactly one of i,j is in S)=1-g-(1-ell)(1-m).`          (2.10)

These formulas expose the actual determinant currency carried by the pair. No physical minor has yet been inverted.

## 3. Main theorem — area bank or replacement pair

### Theorem 3.1 — `QFORM-O0-EXCLUSION-PAIR-DICHOTOMY-v1`

Assume (1.1)-(1.4). Put `J={i,j}` and `g=det K_J`.

Then one of the following alternatives holds.

### (A) Regularized-area bank: `g>=1/16`

The determinant-weighted law places a universal amount of mass on bounded-cardinality row packets containing both physical rows:

`boxed(
 nu(J subset S, 3<=|S|<=5)
 >= c_* := (31/64-e^(-1))/16
 =0.007280972426... .
)`                                                               (3.1)

Equivalently, with `D=det(I+L)`,

`boxed(
 sum_{S superset J, 3<=|S|<=5} det L[S,S]
 >= c_* D.
)`                                                               (3.2)

Since `L=gamma^(-2)BB^T`, this is the original-coordinate aggregate minor inequality

`sum_{S superset J, 3<=|S|<=5}
 gamma^(-2|S|) det(B_S B_S^T)
 >= c_* det(I+gamma^(-2)BB^T).`                                (3.3)

Thus a constant amount of the full regularized determinant is carried by row packets of size at most five. The conclusion is aggregate: it does not assert that any one packet has a universally large unregularized determinant.

### (B) Replacement/near-coloop pair: `g<=1/16`

The pair is selected by the determinant law almost always as one replacement for the other:

`boxed(P_nu(exactly one of i,j is in S)>=13/16.)`              (3.4)

More sharply,

`P_nu(i in S,j notin S)>=11/16`,                              (3.5)
`P_nu(i notin S,j in S)>=1/16`,                               (3.6)
`P_nu(i,j notin S)<=1/8`,                                    (3.7)
`P_nu(i,j in S)<=1/16`.                                      (3.8)

The two eigenvalues `mu_+>=mu_-` of the physical pair kernel `K_J` satisfy

`boxed(
 mu_+ >= (7+sqrt(33))/16 =0.796535...,
 mu_- <= (7-sqrt(33))/16 =0.0784649... .
)`                                                               (3.9)

Writing the regularized feature matrix

`U=B(gamma^2 I+B^T B)^(-1/2)`, so `K=UU^T`,                    (3.10)

the second physical feature row is quantitatively close to the line of the first:

`boxed(
 dist(u_j,span{u_i})^2=g/ell <=1/12.
)`                                                               (3.11)

Finally, if `j` is excluded instead, the conditional leverage of `i` obeys

`boxed(
 P_nu(i in S | j notin S)
 = (ell-g)/(1-d)
 >=11/13.
)`                                                               (3.12)

Hence this is not merely another heavy pair: it is a genuine two-coordinate replacement geometry in the determinant law, with one nearly rank-one regularized direction and both original coordinates carrying nontrivial exclusive occupancy.

### Proof of (A)

Condition the DPP on inclusion of `J`. Its kernel on `J^c` is

`K^J=K_CC-K_CJ K_J^(-1)K_JC`.                                (3.13)

Let `N=|S\J|` under this conditional law and `mu=E N=tr K^J`.

First, inclusion of one physical row reduces expected cardinality by at most one. For the pair this gives

`mu>=tr K-2=1`.                                               (3.14)

For completeness, the block inequality `K^2<=K` gives

`K_JC K_CJ <= K_J-K_J^2`.

After multiplying by `K_J^(-1)` and taking traces,

`tr(K_CJ K_J^(-1)K_JC)<=2-tr K_J`.

Substituting in (3.13) yields (3.14).

Second, `K^J<=K_CC`, so

`mu<=tr K_CC=3-tr K_J`.                                      (3.15)

By the two-by-two identity

`tr K_J=1+det K_J-det(I-K_J)=1+g-(1-ell)(1-m)`.               (3.16)

Under `g>=1/16`, `ell>=3/4`, `m>=1/2`,

`tr K_J>=1+1/16-1/8=15/16`,                                  (3.17)

hence

`1<=mu<=33/16`.                                               (3.18)

The cardinality of a DPP is a sum of independent Bernoulli variables with parameters equal to the eigenvalues of its kernel. Thus

`P(N=0)=det(I-K^J)<=exp(-tr K^J)<=e^(-1)`.                    (3.19)

Markov's inequality and (3.18) give

`P(N>=4)<=mu/4<=33/64`.                                      (3.20)

Therefore

`P(1<=N<=3)>=1-e^(-1)-33/64=31/64-e^(-1)`.                   (3.21)

Multiplying by the inclusion probability

`P(J subset S)=det K_J=g>=1/16`                               (3.22)

proves (3.1). Equations (3.2)-(3.3) are just the definition of the `L`-ensemble. QED.

### Proof of (B)

From (2.7),

`delta_0:=P(i,j notin S)=(1-ell)(1-m)<=1/8`.                 (3.23)

Then (2.10) and `g<=1/16` give

`P(exactly one)>=1-1/16-1/8=13/16`,                           (3.24)

while (2.8)-(2.9) and `3/4<=ell<=7/8`, `m>=1/2` give (3.5)-(3.8).

For (3.9), the eigenvalues of `K_J` satisfy

`mu_++mu_-=tr K_J=1+g-delta_0>=7/8`,
`mu_+mu_-=g<=1/16`.                                          (3.25)

Since `mu_+>=mu_-`, one has `mu_+>=7/16`. If `mu_+<(7+sqrt(33))/16`, then

`mu_->7/8-mu_+`

and therefore

`mu_+mu_->mu_+(7/8-mu_+)>=1/16`,

because the roots of `x(7/8-x)=1/16` are `(7+-sqrt(33))/16`. This contradicts (3.25), proving the lower bound on `mu_+`; the upper bound on `mu_-` follows from `mu_-=g/mu_+` and the product of the two displayed roots being `1/16`.

For (3.11), the squared distance of `u_j` from the span of `u_i` is the Gram determinant divided by `||u_i||^2`:

`dist(u_j,span{u_i})^2
 = [ell*d-s^2]/ell
 =g/ell
 <=(1/16)/(3/4)=1/12.`                                     (3.26)

Finally, DPP exclusion gives

`P(i in S | j notin S)=(ell-g)/(1-d)`.                       (3.27)

Using (2.3), this is

`F(ell,m,g)=(ell-g)/[1-(1-ell)m-g]`.                         (3.28)

For fixed `ell,m`, `F` is decreasing in `g`; for fixed `ell,g`, it is increasing in `m`. At `g=1/16`, `m=1/2`, it is increasing in `ell` on `[3/4,7/8]`. Hence its minimum is attained at `(ell,m,g)=(3/4,1/2,1/16)` and equals

`(3/4-1/16)/(1-(1/4)(1/2)-1/16)=11/13`.                      (3.29)

This proves (3.12). QED.

## 4. Rank-three endpoint is sharper

When `rank B=3` and `gamma downarrow0`, `K` is a rank-three orthogonal projection and the limiting determinant law is exactly size-three volume sampling. In the area branch,

`P(J subset S)=g`

then already implies

`P(J subset S, |S|=3)=g>=1/16`;                               (4.1)

there is no size-four/five leakage. Equivalently, if `B=U Sigma V^T` with `U^TU=I_3`,

`sum_{k notin J} det(B_{J union {k}}B_{J union {k}}^T)
 =det(Sigma^2) det(U_JU_J^T)
 =E*g`.                                                       (4.2)

Thus the finite-gamma theorem genuinely extends the endpoint third-volume bank rather than replacing it by a single coordinate minor.

## 5. Actual application of compatible account04 mathematics

In the exact-rank-three target specialization

`A=R Lambda R^T`, `R^TR=I_3`, `min |lambda_r|>=1`,             (5.1)

take the same physical pair `i,j` and put `K=RR^T`. Let `c=K_ii=ell` and let the **inclusion** residual leverage of row `j` after removing the direction of row `i` be

`h=det K_J/c=g/ell`.                                         (5.2)

If the stronger subbranch

`g>ell/2`                                                     (5.3)

occurs, then `c>1/2` and `h>1/2`, exactly the nested-heavy hypotheses of the completed account04/B16 result. Applying its exact fixed-pair identity gives the actual inequality

`boxed(
 sum_{k !=i,j} |det A[{i,j,k},{i,j,k}]|
 =|det Lambda| g
 >3/8.
)`                                                               (5.4)

This uses `ell>=3/4` and `|det Lambda|>=1`.

Moreover, if one normalized atom in that account04 determinant bank has weight at least `1/8` and its three physical diagonal entries vanish, account04/B16's target-level theorem gives

`||p_Q||_infinity <15.277`                                    (5.5)

with arbitrary outside original-coordinate quadratic terms and couplings. This is a direct quantitative application of completed account04 mathematics, not an attribution to the absent designated B07 partner.

The remaining area branch `1/16<=g<=ell/2` is not claimed paid by (5.5); its source-valid output is the bounded-cardinality aggregate bank (3.3).

## 6. Updated smallest conditional deduction

Combining the preceding B07 deletion collar with Theorem 3.1, every unpaid O0 one-heavy state is now forced into one of only three geometries:

1. **single near-coloop:** `ell>7/8`;
2. **replacement pair:** `3/4<=ell<=7/8`, the exclusion row has `m>=1/2`, and `det K_{ij}<=1/16`; then (3.4)-(3.12) hold;
3. **bounded-cardinality area bank:** the same nested exclusion state but `det K_{ij}>=1/16`; then at least `c_*>0.00728` of the full regularized determinant lies on original-coordinate row packets containing `{i,j}` and of total size three through five.

This is strictly more structured than the previous statement “a second row is heavy after deletion.” The determinant resource is now either concentrated into a finite row packet before inversion, or the two bad coordinates are quantitatively a single regularized direction with a replacement relation.

The first unpaid O0 implication becomes

**`QFORM-O0-REPLACEMENT-PAIR-OR-SIZE5-BANK-PAYMENT-v1` (OPEN):** pay either the two-coordinate replacement geometry (3.4)-(3.12), or the size-three-to-five regularized row bank (3.3), using a product-preserving grouped-square/rank-two/pair-log mechanism that retains arbitrary self blocks and additional spectral components. The current corrections forbid replacing this with one reciprocal local minor or a worst scalar-conditioned fiber supremum.

The separate O1/O2/O3 overlap classes remain debts in the complete synthesis.

## 7. Status

Proved in this source:

- `QFORM-O0-EXCLUSION-PAIR-DICHOTOMY-v1`;
- `QFORM-O0-BOUNDED-CARDINALITY-REGULARIZED-BANK-v1`, inequality (3.3);
- `QFORM-O0-REPLACEMENT-PAIR-v1`, inequalities (3.4)-(3.12);
- the rank-three endpoint sharpening (4.1)-(4.2).

Applied from account04/B16 at exact scope: (5.4), and the zero-diagonal heavy-atom payment (5.5) on its stated subbranch.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** The new structural theorem does not itself prove continuity; continuity remains available only on previously paid ridge branches or other theorems that explicitly establish it.

No scheduler, task identity, cadence, enabled/paused state, quiet-delivery setting, email, public-release workflow, paid model/API/Codex call, credential, permission, or cross-account native state was changed. `full_brain_connected=false`.
