SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-24T05:06:26Z.
attacking: the exact-singular low-pivot overlap-two survivor — renormalize its determinant packet into a balanced two-column Pluecker frame, then force either finitely many physical determinant hubs or one literal cut balancing both determinant directions.

# fleet01/B07 r42 — tau-cancelled Pluecker frame and hub-or-balanced-cut selection

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / exact structural identities  
Run: `20260924T050626Z-fleet01-B07-qform-auto11-r42`  
Status: **NEW SUPPORTING LEMMA PROVED / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; repository retrieval/write/readback is not native receiver-memory ingestion.

No Gaussianity, moments, compact support, connected support, log-concavity, post-rotation independence, or diagonal-basis hypothesis is introduced. The two-dimensional rotation below is used only as deterministic coefficient algebra inside the fixed physical pair; every selected row index and every determinant weight is an ORIGINAL coordinate object.

## 1. Incoming exact-singular carrier

The preceding B07 reduction leaves an exact-singular physical pair `H={h1,h2}` on its hard overlap-two branch. Write

`B=A[H,H]=tau ell ell^T`,

where `tau!=0`, `||ell||_2=1`; let `k` be a unit vector orthogonal to `ell`, let `O=H^c`, and put

`U=A[O,H]`, `p=U ell`, `q=U k`.

The completed r40/r41 identities give

`D_H=-tau q q^T`,                                                   (1.1)

where `D_H(i,j)=det A[(H,i),(H,j)]`, together with

`|tau| ||q||_2^2 >= 7/96`,                                         (1.2)

`|tau| q_i^2 < 1/96` for every `i in O`,                            (1.3)

and, on the forced pair-to-outside third-resource branch,

`s_2(U)>31/64`.                                                     (1.4)

The previous run also proved `|tau| E_2(U)>6727/393216`, but the point here is to recover that currency as the determinant of a quantitatively balanced two-column frame and to expose its exact ORIGINAL-coordinate Pluecker marginals.

Define

`alpha=<p,q>/||q||_2^2`,

`z=p-alpha q`,

`r=sqrt(|tau|) q`,

and the `|O| x 2` coefficient matrix

`K=[r,z]`.                                                         (1.5)

By construction `r perpendicular z`.

## 2. The tau-cancelled balanced frame

### Theorem 2.1 — `QFORM-EXACTSINGULAR-RENORMALIZED-PLUCKER-FRAME-v1`

Under (1.1)--(1.4), the matrix `K` in (1.5) obeys

`||r||_2^2 >= 7/96`,                                               (2.1)

`||z||_2 > 31/64`,                                                 (2.2)

and therefore

`s_2(K) > sqrt(7/96)=0.2700308624...`.                             (2.3)

Moreover

`Omega:=E_2(K)=||r||_2^2 ||z||_2^2
      =|tau| E_2(U)
      >6727/393216
      =0.01710764567...`.                                          (2.4)

For every pair of ORIGINAL outside coordinates `i<j`,

`det K[{i,j},:]^2=|tau| det U[{i,j},:]^2`.                         (2.5)

Thus the normalized squared-minor law of `K` is exactly the normalized squared-`2x2`-minor law of the physical cross block `U`; no spectral-coordinate independence is asserted or needed.

#### Proof

The `2x2` Gram determinant of `U` is basis invariant. In the deterministic column basis `(ell,k)`,

`E_2(U)=det(U^T U)
       =||q||_2^2 ||p-alpha q||_2^2
       =||q||_2^2 ||z||_2^2`.                                     (2.6)

Also `s_1(U)>=||q||_2`, while `s_1(U)s_2(U)=sqrt(E_2(U))=||q||_2||z||_2`; hence `s_2(U)<=||z||_2`. Equation (1.4) proves (2.2), and (1.2) proves (2.1). Since the columns of `K` are orthogonal, its singular values are their norms, yielding (2.3), and (2.4) follows from (2.6).

For (2.5), let `U'=U[ell,k]=[p,q]`. Right multiplication by this orthogonal `2x2` matrix changes every physical `2x2` determinant only by `det[ell,k]=+/-1`. Replacing the first column `p` by `p-alpha q=z` leaves every `2x2` determinant unchanged, and scaling the second column `q` by `sqrt(|tau|)` multiplies its determinant square by `|tau|`. QED.

The important point is that the exact-singular small scale `tau` has disappeared from the conditioning of the determinant frame: although the physical `U` can become arbitrarily ill-conditioned as `tau->0`, the determinant-equivalent frame `K` always has two quantitative singular directions.

## 3. Exact physical determinant-marginal identity

Write

`R2=||r||_2^2`, `Z2=||z||_2^2`,

and

`kappa_ij=r_i z_j-r_j z_i`.

For an outside coordinate `i`, let

`m_i=sum_{j!=i} kappa_ij^2`.

Since `r perpendicular z`, direct expansion gives the exact identity

`boxed: m_i=Z2 r_i^2+R2 z_i^2.`                                  (3.1)

After normalization by `Omega=R2 Z2`,

`boxed:
 mu_i:=m_i/Omega
      =r_i^2/R2+z_i^2/Z2.
}`                                                                  (3.2)

By (2.5), this is not an artificial spectral marginal:

`mu_i = [sum_{j!=i} det U[{i,j},:]^2]/E_2(U)`.                    (3.3)

It is exactly the ORIGINAL-coordinate inclusion marginal of the complete physical squared-minor law of `U`.

The low-principal-triple condition (1.3) and (2.1) imply

`boxed: r_i^2/R2 < 1/7` for every `i`.                             (3.4)

Thus any large physical determinant marginal is forced by the transverse `z` direction rather than by the already-controlled bordered-minor star.

## 4. Hub or simultaneously balanced physical cut

### Theorem 4.1 — `QFORM-PLUCKER-3HUB-OR-BALANCED-2BANK-v1`

Under the same hypotheses, exactly one of the following two usable alternatives occurs.

### (H) Finite determinant-hub alternative

There is an ORIGINAL outside coordinate `i` with

`mu_i >= 2/5`.                                                     (4.1)

Every such hub satisfies

`z_i^2/Z2 > 9/35`,                                                 (4.2)

so there are at most three such coordinates. Each hub carries the physical minor-star currency

`boxed:
 |tau| sum_{j!=i} det U[{i,j},:]^2
   =m_i
   >=(2/5)Omega
   >6727/983040
   =0.006843058268... .
}`                                                                  (4.3)

### (B) Balanced two-bank alternative

If no `mu_i` is at least `2/5`, there is a literal ORIGINAL-coordinate partition

`O=R disjoint_union S`

such that both determinant directions are simultaneously balanced:

`1/8 < ||r_R||_2^2/R2 < 7/8`,
`1/8 < ||z_R||_2^2/Z2 < 7/8`,                                     (4.4)

and hence the complementary bank has the same bounds. On this SAME cut,

`boxed:
 |tau| sum_{i in R,j in S} det U[{i,j},:]^2
   =sum_{i in R,j in S} kappa_ij^2
   >=Omega/32
   >6727/12582912
   =0.0005346139272... .
}`                                                                  (4.5)

The exact bordered-minor rank-one star is also retained on that same cut:

`boxed:
 ||D_H[R,S]||_op
 =||r_R||_2 ||r_S||_2
 >= (sqrt(7)/8) R2
 >= 7sqrt(7)/768
 =0.02411492080... .
}`                                                                  (4.6)

Thus the hard exact-singular branch now has either at most three explicit physical determinant hubs or one physical cut that carries BOTH a constant determinant packet and a constant bordered-minor star while giving each of the two tau-cancelled determinant directions positive energy on both sides.

#### Proof

If (4.1) holds, (3.2) and (3.4) give

`z_i^2/Z2 = mu_i-r_i^2/R2 >2/5-1/7=9/35`,

proving (4.2). Since the normalized `z` energies sum to one, there can be at most three such indices. Equation (4.3) is (3.3), (2.5), and (2.4).

Assume now `mu_i<2/5` for every `i`. Put

`a_i=r_i^2/R2`, `b_i=z_i^2/Z2`.

Then `max a_i<1/7` by (3.4), while `max b_i<2/5` because `b_i<=mu_i`. Color each outside coordinate independently into `R` with probability `1/2`. For

`A_R=sum_i a_i 1_{i in R}` and `B_R=sum_i b_i 1_{i in R}`,

`E A_R=E B_R=1/2`, and

`Var(A_R)=1/4 sum_i a_i^2 <1/28`,

`Var(B_R)=1/4 sum_i b_i^2 <1/10`.                                 (4.7)

Chebyshev plus a union bound gives

`P(|A_R-1/2|>=3/8 or |B_R-1/2|>=3/8)
 <= (1/28+1/10)/(3/8)^2
 =304/315 <1`.                                                     (4.8)

Hence one deterministic cut satisfies (4.4).

Let `c_R=<r_R,z_R>`. Since `<r,z>=0`, `<r_S,z_S>=-c_R`. Expanding the cross Pluecker mass gives the exact identity

`sum_{i in R,j in S} kappa_ij^2
 =||r_R||^2||z_S||^2+||z_R||^2||r_S||^2+2c_R^2`.                 (4.9)

Each of the first two terms is at least `Omega/64` under (4.4), proving (4.5).

Finally (1.1) gives, after absorbing the sign of `tau`,

`D_H[R,S]=-sign(tau) r_R r_S^T`,

so its operator norm is `||r_R||||r_S||`. If `x=||r_R||^2/R2` lies in `[1/8,7/8]`, then `sqrt(x(1-x))>=sqrt(7)/8`, proving (4.6). QED.

## 5. Designated partner result applied at an actual inequality

The latest completed designated fleet02/B07 result consumed in this run is

`yspennstate/math-open-problems@ec29bb4321feffe020e5cb0185d148f2f6de847e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260924T013622Z-fleet02-B07-qform-auto11/REPORT.md`.

Its theorem `QFORM-E2-BOUNDED-SUPPORT-BALANCE-v1` states for a rank-`r>=2` matrix `M`

`E_2(M) <= (r-1)s_2(M)^2 ||M||_F^2`.                              (5.1)

Applying (5.1) to the actual tau-cancelled matrix `K` (rank two) and using (2.4) gives

`boxed:
 s_2(K)||K||_F
   >=sqrt(Omega)
   >sqrt(6727/393216)
   =0.13079619899... .
}`                                                                  (5.2)

Here the exact branch identities improve the partner's generic product estimate to the individual bound (2.3). This is precisely where the partner's accompanying stress matters: aggregate `E_2` alone does NOT force a balanced rank-two carrier on diffuse support, but the exact-singular bordered-star scale (2.1) and the independently forced third resource (1.4) do force balance after the determinant-preserving tau renormalization.

A reusable bounded-core corollary is immediate. If a set `C subset O` of `m` physical coordinates carries at least an `eta` fraction of the INTERNAL Pluecker mass of `K`, and

`L_C=max_{i in C} max(|r_i|,|z_i|)`,

then the same partner theorem applied to `K[C,:]` gives

`boxed:
 s_2(K[C,:])
 >0.09248687926 * sqrt(eta/m)/L_C.
}`                                                                  (5.3)

This is conditional on genuine bounded physical support; no bounded-core conclusion is inferred in the diffuse case, in agreement with the partner's exact counterexample.

## 6. What this closes and what remains

This run does NOT prove a universal density bound for the full target and does not prove full-target continuity. It removes one structural ambiguity from the exact-singular low-pivot overlap-two branch:

* the `tau->0` degeneracy can be cancelled at the COMPLETE determinant-law level;
* the resulting physical squared-minor law is generated by a quantitatively balanced two-column frame;
* its coordinate marginals are exactly the sum of two normalized energy laws;
* therefore it cannot remain an amorphous diffuse packet: it has at most three transverse determinant hubs, or there is a literal cut balancing both determinant directions and retaining both a constant Pluecker packet and a constant bordered-minor star.

The first unpaid analytic implication is now

`QFORM-3HUB-OR-BALANCED-TAUCANCELLED-PAIR-RECEIVER-v1`:

1. spend the at-most-three outside determinant hubs in (4.3), OR
2. spend the same-cut resources (4.4)--(4.6),

while retaining arbitrary same-bank curvature and all nonzero residual spectral directions. One may not condition away the transverse `z` direction and then reuse the old rank-one-pair half-Riesz bound, because that deliberately recreates the `|tau|^{-1/4}` loss that the present determinant renormalization removed.

The near-singular but invertible pair collar and the anchored-`E_4` branch from r39 remain separate obligations. Existing phase-aligned-support, arbitrary-joint-coarea, fiber-supremum, and post-rotation-independence corrections remain in force.

Full QFORM: **OPEN / not proved / not disproved**.  
Continuous representative for the full target: **OPEN**.
