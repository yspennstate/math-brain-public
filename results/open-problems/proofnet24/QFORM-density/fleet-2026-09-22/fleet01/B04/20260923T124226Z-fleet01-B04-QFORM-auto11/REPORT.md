SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T12:42:26Z.
attacking: product Fourier rearrangement by downshifting canonical fourth exterior volume to an entropy-efficient third-volume weight, then paying the exact fourth-volume-coloop endpoint with the completed fleet02/B04 exact-rank theorem.

# fleet01/B04 — fourth-volume face downshift and an explicit rotated indefinite estimate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATE / FULL_TARGET_OPEN`  
Continuity in the new branch: **proved (`C_0`)**.  
Full unrestricted QFORM theorem: **OPEN**.  
Independent end-to-end review of the new theorem: **not yet recorded**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.


## 1. The first missing implication and the mechanism change

The newest designated-partner report

- `yspennstate/math-open-problems@907d4092f2d22b6c02146cb8165efa0b7416ffa5`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260923T111930Z-qform/REPORT.md`

proves `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`: exact *support infeasibility* for a strict third-volume marginal gate is already paid by exact-rank-three product Plancherel, with at most a factor `4^(1/6)` loss. Thus there is no reason to spend this run on another support classification. The genuinely unpaid B04 issue is quantitative: a strict third-volume weight may exist, but every obvious such weight can have poor determinant/entropy currency.

The useful observation here is that a robust fourth exterior volume contains, by an exact face identity, a canonical *third-volume probability law*. One should not choose a single three-row minor. Instead, sample a four-row volume packet and delete one row. This gives exact row marginals and an exact entropy currency, and it remains stable when an additional singular direction is arbitrarily small.

The analytic compiler used below is the already-completed theorem from this slot,

`QFORM-ENTROPY-WEIGHTED-THREE-VOLUME-v1`,

read from the pinned snapshot

- `yspennstate/math-open-problems@1d2dd52680ec729f28b7289e74a6f3752a379127`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T021315Z-fleet01-B04-QFORM-auto11/REPORT.md`.

For a physical cross block `M=A[I,J]`, any probability law `w` on supported physical `3 x 3` minors, row marginals `alpha_i`, and determinant/entropy currency

`G(w)=exp(sum_(S,T) w_(S,T) log(det(M[S,T])^2/w_(S,T)))`,

it says that if

`1<=q<3/2`,  `max_i alpha_i<=q/2`,

then the full original-coordinate quadratic form, retaining arbitrary same-bank curvature, outside couplings and induced affine terms, has a continuous density vanishing at infinity and

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] G(w)^(-1/6)`.          (1.1)

This is the only Fourier theorem used in the new downshift branch.

## 2. Exact exterior-volume face identity

Let `M` be an `m x d` real matrix with

`E4(M):=e4(M^T M)>0`.

Write its physical row vectors as `m_1,...,m_m in R^d`. For each physical three-row set `S`, define

`a_S = det(M[S,:] M[S,:]^T)
     = sum_(|T|=3) det(M[S,T])^2`.                              (2.1)

For each physical four-row set `R`, define

`d_R = det(M[R,:] M[R,:]^T)
     = sum_(|U|=4) det(M[R,U])^2`.                              (2.2)

Cauchy--Binet gives

`sum_(|R|=4) d_R = E4(M)`.                                     (2.3)

If `a_S>0`, let `V_S` be the three-dimensional span of the rows in `S`, let `P_S` be the orthogonal projection onto `V_S`, and put

`tau_S = sum_j dist(m_j,V_S)^2
       = ||M(I-P_S)||_F^2`.                                    (2.4)

### Lemma 2.1 — Gram height identity

For every `j notin S`,

`d_(S union {j}) = a_S dist(m_j,V_S)^2`.                       (2.5)

Hence

`b_S:=sum_(j notin S) d_(S union {j}) = a_S tau_S`.            (2.6)

If `a_S=0`, then every four-set containing `S` also has zero four-volume, so `b_S=0`.

**Proof.** Gram--Schmidt the fourth row against the span of the first three rows. Squared Euclidean volume is multiplied by the squared orthogonal height, which is exactly (2.5). If the three-row volume vanishes, their row rank is at most two, so adjoining one row has rank at most three and every corresponding four-row Gram determinant vanishes. QED.

Every positive four-row volume has four three-row faces. Summing (2.6) therefore gives the exact identity

`boxed: sum_S a_S tau_S = 4 E4(M).`                            (2.7)

This is the structural identity that drives the run.

## 3. Canonical fourth-volume deletion law

Let

`pi(R)=d_R/E4(M)`                                               (3.1)

be the canonical squared fourth-volume law on physical four-row sets, and write

`rho_i=P_pi(i in R)`,  `rho_*=max_i rho_i`.                    (3.2)

Now sample `R~pi` and, conditional on `R`, delete one of its four rows uniformly. Let `S` be the remaining triple. By (2.6)--(2.7), its law is

`mu(S)=a_S tau_S/[4E4(M)]`.                                    (3.3)

This law has an exact row-marginal formula. Given a four-set containing row `i`, the uniform deletion retains `i` with probability `3/4`. Therefore

`boxed: alpha_i(mu)=(3/4)rho_i.`                               (3.4)

This is not an estimate and does not select a physical pivot.

Lift `mu` to a probability law on full physical `3 x 3` minors by retaining the canonical conditional column-volume law:

`w_(S,T)=mu(S) det(M[S,T])^2/a_S`                              (3.5)

when `a_S>0`; triples with `a_S=0` have `mu(S)=0` and need no definition. Cauchy--Binet in (2.1) shows that (3.5) is normalized and has the same row marginals (3.4).

## 4. Exact entropy currency

The determinant factors in (3.5) cancel inside the entropy currency:

`det(M[S,T])^2 / w_(S,T) = a_S/mu(S) = 4E4(M)/tau_S`.

Therefore

`log G(w)
 = sum_(S,T) w_(S,T) log(det(M[S,T])^2/w_(S,T))`
` = log(4E4(M)) - sum_S mu(S) log tau_S`.                       (4.1)

Define the `mu`-weighted geometric mean

`tau_geo = exp(sum_S mu(S) log tau_S)`.                        (4.2)

Then the currency is exactly

`boxed: G(w)=4E4(M)/tau_geo.`                                  (4.3)

Since `tau_S<=||M||_F^2` for every supported `S`,

`boxed: G(w)>=4E4(M)/||M||_F^2.`                              (4.4)

A slightly sharper rank-sensitive but still elementary bound is available: if `r=rank(M)`, then the orthogonal complement of `V_S` inside the row space has dimension `r-3`, so

`tau_S <= sum_(j=1)^(r-3) sigma_j(M)^2`                        (4.5)

when the singular values are arranged decreasingly. The exact geometric mean (4.2), however, is the right currency and can be much smaller than either coarse upper bound.

Equation (4.3) is the main new analytic identity. It converts fourth exterior volume to precisely the determinant/entropy quantity needed by the third-volume Fourier compiler. No reciprocal local minor appears.

## 5. New theorem — fourth-volume downshift

### Theorem 5.1 — `QFORM-FOURTHVOLUME-DOWNSHIFT-v1`

Let `I,J` be disjoint original-coordinate banks in the full quadratic form, let `M=A[I,J]`, and suppose `E4(M)>0`. Define `rho_*`, `mu` and `tau_geo` by (3.1)--(4.2).

If

`rho_*<1`,                                                     (5.1)

put

`q4=max{1,(3/2)rho_*}`.                                       (5.2)

Then `q4<3/2`, the full ambient quadratic form has a continuous density vanishing at infinity, and

`boxed:
 ||p_Q||_infinity
 <= [3e/((3-2q4)sqrt(q4))]
    [4E4(M)/tau_geo]^(-1/6).`                                 (5.3)

In particular,

`boxed:
 ||p_Q||_infinity
 <= [3e/((3-2q4)sqrt(q4))]
    [4E4(M)/||M||_F^2]^(-1/6).`                               (5.4)

All same-bank quadratic terms, all outside couplings, and all affine terms created by conditioning are retained.

**Proof.** By (3.4),

`alpha_*=(3/4)rho_*<=q4/2`.

Condition (5.1) gives `q4<3/2`. Apply the completed entropy-weighted third-volume theorem (1.1) to the minor law (3.5). Equation (4.3) gives (5.3), and (4.4) gives (5.4). Integrability of the resulting characteristic-function bound supplies the `C_0` representative. QED.

A useful explicit form of the marginal coefficient is

- if `rho_*<=2/3`, then `q4=1` and the prefactor is `3e`;
- if `2/3<rho_*<1`, then `q4=3rho_*/2` and

`3e/[(3-2q4)sqrt(q4)]
 = e/[(1-rho_*) sqrt(3rho_*/2)]`.                              (5.5)

Thus the only marginal singularity in this one-step compiler is a genuine near-coloop of the *fourth-volume* law.

## 6. Exact fourth-volume coloop endpoint is paid by fleet02/B04

The endpoint `rho_*=1` is not silently discarded. Suppose `rho_i=1` for some physical row `i`. Then every positive four-row volume includes row `i`. If `rank(M_{-i,*})>=4`, four independent rows avoiding `i` would have a positive Gram determinant, contradiction. Hence

`rank(M_{-i,*})<=3`.

Since `E4(M)>0`, `rank(M)>=4`, while adding a single row can increase rank by at most one. Therefore

`boxed: rho_*=1  => rank(M)=4.`                                (6.1)

Now apply the completed designated-partner theorem

`QFORM-RANKR-TWOSIDED-CONTAMINATION-FOURIER-v1`,

- `yspennstate/math-open-problems@8f8913581643a7e7bcbe7d8c178a2255194dfc3d`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T233213Z-r22/REPORT.md`.

For an exact-rank `r>=3` physical cross block with nonzero singular values `sigma_1,...,sigma_r`, arbitrary measurable same-bank contamination on both product banks is allowed and

`||p_Q||_infinity <= e r/(r-2) (prod_j sigma_j)^(-1/r)`.       (6.2)

At the endpoint (6.1), `r=4` and

`E4(M)=prod_(j=1)^4 sigma_j^2`.

Thus the partner theorem gives the actual endpoint inequality

`boxed: ||p_Q||_infinity <= 2e E4(M)^(-1/8).`                 (6.3)

Its characteristic function is integrable at rank four, so this endpoint also has a continuous `C_0` density.

Therefore the fourth-volume downshift has no **exact** coloop hole: the non-coloop case is handled by (5.3), and the exact coloop case collapses to exact rank four and is paid by the designated partner. The remaining difficulty is quantitative near-coloop/low-currency routing, not the exact endpoint.

## 7. A genuinely rotated indefinite target family

Let `H_8` be the real `8 x 8` Sylvester Hadamard matrix, so `H_8 H_8^T=8I`. Let `U` be its first five columns divided by `sqrt(8)`. Thus `U^T U=I_5` and every entry of `U` is `+/-1/sqrt(8)`.

For `epsilon>0`, set

`Sigma_epsilon=diag(2,2,2,2,epsilon)`,
`M_epsilon=U Sigma_epsilon`,                                  (7.1)

and define the physical symmetric matrix

`A_epsilon=[[0,M_epsilon],[M_epsilon^T,0]]`.                   (7.2)

Every one of the forty physical cross coefficients of `M_epsilon` is nonzero. The singular values of `M_epsilon` are exactly

`2,2,2,2,epsilon`,

so the exact spectrum of `A_epsilon` is

`boxed: {+2 (x4), -2 (x4), +epsilon, -epsilon, 0 (x3)}.`       (7.3)

Hence for every `epsilon>0` this is a genuinely non-diagonal, rotated, indefinite instance of the owner's target; in particular it always has eight eigenvalues of modulus two.

### 7.1 Fourth-volume marginals are exactly flat

Index Hadamard rows by the group `(Z/2Z)^3`. Translating the row index multiplies each selected character column by a sign. Hence it maps every physical row packet to another packet by a right orthogonal diagonal sign matrix, preserving every Gram determinant `d_R`. The canonical fourth-volume law is therefore transitive on the eight physical rows.

Its row marginals sum to four, so

`boxed: rho_i=1/2 for all i.`                                  (7.4)

The downshifted third-volume law consequently has

`alpha_i=3/8`,                                                  (7.5)

and the strongest Fourier choice `q4=1` is available.

Also, with `t=epsilon^2`,

`E4(M_epsilon)=e4(4,4,4,4,t)=256(1+t)`.                       (7.6)

### 7.2 Exact face calculation

There are fifty-six physical row triples. Direct symbolic Gram evaluation, using only the Hadamard identities, splits them into two translation/symmetry types:

Type A, count `32`:

`a_A=(16+3t)/2`,
`b_A=4(8+5t)`,
`tau_A=8(8+5t)/(16+3t)`.                                      (7.7)

Type B, count `24`:

`a_B=2t`,
`b_B=16t`,
`tau_B=8`.                                                     (7.8)

Since `4E4=1024(1+t)`, their total `mu`-masses are

`m_A=(8+5t)/[8(1+t)]`,
`m_B=3t/[8(1+t)]`.                                             (7.9)

Thus

`tau_geo=tau_A^(m_A) 8^(m_B)`.                                (7.10)

Weighted AM--GM gives `tau_geo<=m_A tau_A+8m_B`, and the latter is exactly

`2(17t^2+64t+32)/[(1+t)(3t+16)]`.                              (7.11)

A direct subtraction gives

`4(1+t)-[m_A tau_A+8m_B]
 = 6t(2t^2+9t+2)/[(1+t)(3t+16)] >=0`.                          (7.12)

Therefore

`tau_geo<=4(1+t)`

and the exact entropy currency satisfies the epsilon-uniform lower bound

`boxed:
 G(w)=1024(1+t)/tau_geo >=256.`                                (7.13)

Combining `q4=1` with (1.1) gives, for **every** admissible independent cap-one product law,

`boxed:
 ||p_(X^T A_epsilon X)||_infinity
 <= 3e * 256^(-1/6)
 = 3e/2^(4/3)
 = 3.236252575531447... .`                                    (7.14)

The density has a continuous representative vanishing at infinity. The estimate is uniform as the fifth nonzero singular value `epsilon` tends to zero, while that fifth direction remains fully present in the physical quadratic form.

The coarser general inequality (5.4) would only give `G>=4E4/||M||_F^2=1024(1+t)/(16+t)`, tending to `64`. The exact face calculation improves the limiting currency by a factor four and the density certificate by `4^(1/6)`.

## 8. Same-matrix designated-partner comparison

Apply the completed fleet02/B04 theorem (6.2) to the **same** `M_epsilon`. Here the exact cross rank is five and

`Delta=prod sigma_j=16 epsilon`.

Therefore

`boxed:
 ||p_(X^T A_epsilon X)||_infinity
 <= (5e/3)(16 epsilon)^(-1/5).`                                (8.1)

At `epsilon=10^(-6)`, (8.1) is

`41.24005492190681...`,                                       (8.2)

whereas the new downshift theorem gives the epsilon-uniform

`3.236252575531447...`.                                       (8.3)

The ratio is about

`12.743150900431344`.                                         (8.4)

Thus the new mechanism is not a rephrasing of the exact-rank theorem. The partner estimate necessarily pays the product of all five nonzero singular values and diverges as the fifth one vanishes; the fourth-to-third face downshift aggregates exterior volume before Fourier inversion and is insensitive to that weak fifth singular direction on this family.

This is the required actual designated-partner application to a concrete inequality.

## 9. Why the theorem matters for the live proof map

The newest fleet02/B04 report shows that exact strict-third-volume support defects are already paid. The harder survivor is a support-feasible higher-rank packet whose entropy-balanced third-volume currency is small. Theorem 5.1 gives a new route in precisely that regime:

- if fourth-volume mass is quantitatively spread over physical rows, delete one row from a canonical four-volume packet;
- the resulting third-volume marginal gate is exact, not estimated;
- its determinant/entropy currency is the global quantity `4E4/tau_geo`, not a selected small minor;
- an arbitrarily weak fifth or later singular direction need not be multiplied into the price;
- the exact fourth-volume-coloop endpoint collapses to rank four and is paid by fleet02/B04.

A convenient scale is

`kappa_down(M)=[4E4(M)/tau_geo]^(1/6)`.                        (9.1)

Whenever `rho_*<=2/3`, the theorem reads simply

`||p_Q||_infinity <= 3e/kappa_down(M)`.                        (9.2)

For `2/3<rho_*<1`, the only additional loss is the explicit near-coloop factor in (5.5).

## 10. The remaining implication

The full three-large-eigenvalue theorem is not closed. The new exact gap is

`QFORM-FOURTHVOLUME-DOWNSHIFT-OR-COMPOUND-HUB-v1`:

> Starting from only the full symmetric-matrix hypothesis that three eigenvalues have modulus at least one, after the already-paid exact-rank-three/support-defect exits, either find an original-coordinate cross cut with target-scale `kappa_down(M)` and fourth-volume row marginal bounded away from one, or show that simultaneous failure of those conditions forces one of the completed compound-hub, ridge, pair-log, aggregate-square, grouped-bank, or exact-rank mechanisms without paying an arbitrarily small extra singular direction.

The exact `rho_*=1` endpoint is now paid, but `rho_*` arbitrarily close to one and `kappa_down` arbitrarily small remain quantitative structural debts. Also, the bare three-eigenvalue hypothesis does not itself guarantee that a useful cut has `E4>0`; exact-rank-three and lower-cross-rank routes remain necessary in the global synthesis.

No claim of a full solution or literature novelty is made. Two independent end-to-end reviews would still be required for any full candidate proof.
