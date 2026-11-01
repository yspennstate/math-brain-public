SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-23T17:00:11Z.
attacking: a rank-spent stable-rank six-mode carrier theorem that absorbs arbitrary-magnitude added spectrum on the carrier, pays only the residual carrier footprint plus a dense operator-norm tail, and then routes the surviving six-mode resource through an original-coordinate receiver.

# fleet02/B12 auto11 — rank-spent stable-rank carrier and projected-crossing complement

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: separate. The D5 and projected-crossing exits below have integrable characteristic-function bounds; the hybrid theorem also invokes physical-core/pair exits for which only the stated essential density bound is used here.

## 1. First unpaid implication

The full target is still not proved: from the bare assumption `s3(A)>=1`, one must force either a bounded original-coordinate carrier/crossing certificate of the kind below or an already-paid hub/ridge/grouped-bank/physical-core/Schur exit. The theorem proved in this run is a compiler once such a carrier is present; it does not assert that every target matrix supplies one.

The new gain over the preceding six-mode carrier theorem is that one may spend `r` completely arbitrary-magnitude matrix directions first, while an arbitrarily large orthogonal spectral completion is free and a genuinely dense tail is charged only by its matrix operator norm. No step treats a small matrix tail as a uniformly small random quadratic error on unbounded inputs, and no rotated random coordinates are declared independent.

## 2. Rank-spent stable-rank carrier theorem

Let

`A = A0 + R + L + T`

be real symmetric. Assume

`A0 R = 0`, `rank(L)<=r`, `||T||op<=delta`.

Fix an ORIGINAL-coordinate set `H` of size `m>=r+6` and let

`C0 = A0[:,H]`

be the full column restriction of the baseline matrix. Define

`g_r^2 = ( ||C0||F^2 - (r+5)||C0||op^2 )_+ /(m-r-5)`.          (2.1)

Equivalently, when `C0!=0`, writing `sr(C0)=||C0||F^2/||C0||op^2`,

`g_r = ||C0||op * sqrt((sr(C0)-r-5)_+/(m-r-5))`.              (2.2)

### Theorem 2.1 (`QFORM-RANK-SPENT-STABLE-RANK-CARRIER-v1`)

If `g_r>delta`, then the ACTUAL final matrix satisfies

`lambda_6((A^2)[H,H]) >= (g_r-delta)^2`.                       (2.3)

Thus, putting `g=g_r-delta`, the complete six-mode spectral-square carrier theorem from fleet02/B12 r36 applies to the final matrix. In particular, if also `s3(A)>=s>0`, writing

`C=A[H,H]`, `M=A[H,Hc]`, `N=binom(m,2)`,

then for every

`0<a<b/N`, `0<b<g`, `kappa=b/N-a`,

one has

`||p_(X^TAX)||inf <= max {`
`  2 sqrt(6 pi m)/a,`
`  pi/kappa,`
`  3*400^(1/3) kappa^(-5/6) s^(-1/6),`
`  5 sqrt(2e)/sqrt(g^2-b^2)`
`}.`                                                           (2.4)

This holds for every independent cap-one product source. All spectrum outside the hypotheses remains arbitrary.

### Proof

Let the singular values of `C0` be decreasing. Since there are `m-r-5` terms from index `r+6` through `m`,

`sum_{j>=r+6} s_j(C0)^2`
` = ||C0||F^2 - sum_{j<=r+5}s_j(C0)^2`
` >= ||C0||F^2-(r+5)||C0||op^2`.                              (2.5)

On the other hand every term in this tail is at most `s_{r+6}(C0)^2`, hence

`(m-r-5)s_{r+6}(C0)^2 >= sum_{j>=r+6}s_j(C0)^2`.              (2.6)

Equations (2.5)-(2.6) give

`s_{r+6}(C0)>=g_r`.                                            (2.7)

Now put `B=A0+R`. Symmetry plus `A0R=0` also gives `RA0=0`, so

`B^2=A0^2+R^2 >= A0^2`.                                       (2.8)

Compressing to the ORIGINAL coordinate set `H`,

`B[:,H]^T B[:,H]=(B^2)[H,H] >= (A0^2)[H,H]=C0^T C0`.          (2.9)

Therefore

`s_{r+6}(B[:,H]) >= s_{r+6}(C0)>=g_r`.                         (2.10)

This is exactly the spectral-square conservation mechanism in the designated partner fleet03/B12 r37, here used on the full column carrier rather than on only one side of a cut.

Next `rank(L[:,H])<=r`. Rank-r singular-value interlacing gives

`s_6((B+L)[:,H]) >= s_{r+6}(B[:,H]) >= g_r`.                   (2.11)

Finally `||T[:,H]||op<=delta`, so Weyl gives

`s_6(A[:,H]) >= g_r-delta=g`.                                  (2.12)

Because `A` is symmetric,

`A[:,H]^T A[:,H]=(A^2)[H,H]`,                                 (2.13)

and (2.12) proves (2.3).

To obtain (2.4), take `G=A^2` in `QFORM-SIX-MODE-SPECTRAL-SQUARE-CARRIER-v1`, proved at
`yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`.
That theorem exhausts the final self-block regimes: a three-mode physical self block is paid directly; an approximate rank-two self block yields an invertible ORIGINAL-coordinate physical pair; and a nearly rank-one self block exports five directions into the actual cross block. The last branch is paid by the pinned D5 theorem. QED.

## 3. Literal arbitrary eigenvalue replacements

The rank-r packet is genuinely magnitude-free. In the literal replacement specialization, take orthonormal baseline eigenvectors `v_1,...,v_r` and

`L=sum_{j=1}^r tau_j v_j v_j^T`.                               (3.1)

Whenever these are baseline eigendirections, their eigenvalues are replaced by `lambda_j+tau_j`. Every `tau_j` may be positive, negative, cross zero, or tend to either infinity. The theorem depends on `r` but not on the sizes of the `tau_j`.

The orthogonal completion `R` is even less restricted: it can have arbitrary rank, signs, inertia and norm, as long as its spectral support is orthogonal to that of `A0`, i.e. `A0R=0`. It enters (2.8) only through the positive square `R^2`.

The dense tail `T` can have full rank and arbitrary sign pattern. It is used only in the deterministic singular-value inequality (2.12). There is no assertion that `X^T T X` is small; such a statement is false for arbitrary unbounded cap-one sources.

## 4. Required pinned D5 result at a real inequality

Let `g=g_r-delta` and suppose the final physical self block additionally satisfies

`s_2(C)<b<g`.                                                   (4.1)

The six-mode spill step in r36 gives

`s_5(M) >= sqrt(g^2-s_2(C)^2) > sqrt(g^2-b^2)`.                (4.2)

For the actual final ORIGINAL-coordinate cross block `M`, the pinned `e5f71d79...` theorem gives

`||p_Q||inf <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`.                (4.3)

Since

`e_5(M^TM) >= product_{j=1}^5 s_j(M)^2 >= s_5(M)^10`,         (4.4)

(4.2)-(4.4) yield the concrete inequality

`||p_Q||inf <= 5 sqrt(2e)/sqrt(g^2-b^2)`.                     (4.5)

The D5 source has no row-volume marginal gate and retains arbitrary self blocks, outside couplings and affine terms. This is an application to the actual final matrix, not a post-rotation product surrogate.

Pinned source consumed at equations (4.3)-(4.5):
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and its `FOURIER_ROUTE_REPORT.md`.

## 5. Exact target-class stress family and a D5-only obstruction

Fix any integer `r>=0`. Let

`H={h_1,...,h_{r+6}}`

and introduce four further physical coordinates `j_3,...,j_6`. Define `A0` by

`A0 h_1=2 h_1`, `A0 h_2=-2 h_2`,                              (5.1)

and, for `k=3,4,5,6`, put a hyperbolic `2x2` block on `(h_k,j_k)`:

`A0[h_k,j_k]=A0[j_k,h_k]=2`, with zero diagonal on that pair.  (5.2)

For `k=7,...,r+6`, put

`A0 h_k=2 h_k`.                                                 (5.3)

All other baseline entries vanish. Then the `m=r+6` columns indexed by `H` are orthogonal and all have norm two, so

`C0^T C0=4I_m`, `||C0||F^2=4m`, `||C0||op^2=4`.               (5.4)

Consequently (2.1) gives exactly

`g_r^2=[4m-4(r+5)]/[m-r-5]=4`, hence `g_r=2`.                  (5.5)

Now add

`L_tau=sum_{k=7}^{r+6} tau_k h_k h_k^T`,                       (5.6)

with every `tau_k in R` arbitrary. These are literal replacements `2 -> 2+tau_k`. Also append an arbitrary symmetric spectator operator `R` supported on coordinates disjoint from the support of `A0`; then `A0R=0` and `R` may have arbitrary rank, signs and eigenvalue magnitudes. Finally add any globally dense symmetric

`T`, `||T||op<=1/64`.                                          (5.7)

Theorem 2.1 gives the six-mode final carrier floor

`lambda_6((A^2)[H,H]) >= (127/64)^2`.                          (5.8)

Independently, before `T` the untouched baseline already has at least five eigenvalues equal to `-2` (one from `h_2`, and one from each of the four hyperbolic blocks). Therefore Weyl gives

`s_3(A)>=127/64>1`                                             (5.9)

uniformly in all replacement coefficients and the whole spectator spectrum. This is an exact target-class family.

There is also a source-valid obstruction to trying to close it by D5 alone. Set all `tau_k=-2`, take `T=0`, and leave `R` arbitrary on spectators. Across the cut `H|H^c`, the only baseline cross directions are the four pairs (5.2), so

`rank A[H,Hc]=4`, hence `e_5(A[H,Hc]^T A[H,Hc])=0`.            (5.10)

Thus D5 supplies no finite bound on this member. The hybrid theorem is not cosmetic: the ORIGINAL physical pair `{h_1,h_2}` is exactly `diag(2,-2)` when `T=0`, and under every tail in (5.7) it remains indefinite with

`sigma_min(A[{h_1,h_2},{h_1,h_2}])>=127/64`.                  (5.11)

Using the completed arbitrary-rank physical-pair theorem and (5.9)-(5.11),

`||p_Q||inf <= 3*400^(1/3)/(127/64)`
`           = 11.139118862030774...`.                          (5.12)

So this exact family simultaneously has arbitrary signed low-rank eigenvalue replacements, arbitrary additional spectator spectrum, an arbitrary dense small tail, and a uniform density bound, while a five-cross-volume-only strategy provably has no uniform certificate at the zero-tail endpoint.

## 6. Applying the current projected-crossing theorem to an actual target partition

The current owner continuation asks B09-B12 to consume the new grouped projected-crossing theorem at an actual surviving physical partition. Here is a minimal exact target-class instance where it gives a finite bound although D5 is structurally silent.

Use seven ORIGINAL coordinates grouped as two hubs `x_1,x_2`, two first-light coordinates `z_1,z_2`, and three second-light coordinates `y_1,y_2,y_3`. Take all self blocks zero and set the only nonzero cross coefficients to

`A[{x_1,x_2},{y_1,y_2,y_3}] = [[1,0,0],[0,1,0]]`,             (6.1)

`A[{z_1,z_2},{y_1,y_2,y_3}]`
`   = [[0,0,1/sqrt(2)],[0,0,1/sqrt(2)]].`                      (6.2)

Across the left/right bipartition `{x_1,x_2,z_1,z_2}|{y_1,y_2,y_3}`, the rectangular cross block has singular values exactly `1,1,1`; hence the symmetric seven-dimensional matrix has nonzero spectrum

`{1,1,1,-1,-1,-1}`.                                           (6.3)

It is therefore in the exact three-large-eigenvalue target class. But its cross rank is only three, so again `e_5=0` and D5 is silent.

Apply `NEW_PROJECTED_CROSSING.md` with the two original hub coordinates as the hub group. Because the hub projection is just `(X_{x_1},X_{x_2})`, its joint density is at most

`M_H<=1`.                                                       (6.4)

Take `J={y_1,y_2,y_3}` and `I={z_1,z_2}` in the theorem. The hub-to-`J` matrix has rank `k=2` and singular-value product

`S=1`.                                                         (6.5)

Its row-space projection is

`Pi=diag(1,1,0)`.                                              (6.6)

Therefore the projected light crossing is exactly (6.2), and for `ell=1`

`Z_1=||C||F^2=1`.                                              (6.7)

The two one-volume row marginals are

`alpha_{z_1}=alpha_{z_2}=1/2`,                                 (6.8)

so the theorem's marginal gate is met exactly. With `d=k+ell=3` and the `ell=1` exponential factor omitted, its formula gives

`||p_Q||inf <= 3*2^(5/6) M_H^(1/3) S^(-1/3) Z_1^(-1/6)`
`           <= 3*2^(5/6)`
`           = 5.345392308842036...`.                           (6.9)

This is a genuine complementary receiver: a target matrix can have too few cross directions for D5, yet two grouped hub directions plus one diffuse projected crossing direction provide the third smoothing resource. The theorem permits arbitrary internal hub function and arbitrary same-light-bank quadratic terms at its stated scope; no independence of the two hub projections is assumed by that theorem.

Source consumed at (6.9):
`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

## 7. Designated partner result consumed

The proof of (2.8)-(2.10) is the column-carrier form of the completed fleet03/B12 r37 orthogonal spectral-completion theorem:

`yspennstate/math-open-problems@3d6d9699d94146c3d2cbc475936dacd74109f913`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260923T164514Z-qform-eigenvalue-r37/REPORT.md`.

That theorem proves, from `A0R=0`, the exact positive-square mechanism

`(A0+R)^2=A0^2+R^2>=A0^2`,                                    (7.1)

and the resulting self/cross singular-profile conservation. Here (7.1) first protects the whole physical column carrier, after which the finite-rank packet is spent by singular-value interlacing. This use is stronger than an operator-norm stability statement: the norm of `R` is unrestricted.

Its later projected-crossing addendum at
`yspennstate/math-open-problems@5606cbf66c810119c1e7c0ca4908abe0eb753f56`
was also read before publication; its q=1 and q=2 obligations are compatible with, but not needed to prove, Theorem 2.1.

## 8. Corrections retained and precise remaining gap

The live correction refresh included the later `QFORM-E2-HALFRIESZ-ALONE-NOT-LINF-v1`: finite two-direction half-Riesz credit alone cannot imply bounded density; a genuine third smoothing resource is needed. The present theorem uses six-mode carrier conservation and then an already-proved three-resource receiver, so it does not make the corrected inference.

The later partner-bank correction `QFORM-PARTNER-BANK-INDIVIDUAL-BOUND-CORRECTION-v1` changes a separate random-coloring corollary from individual bank lower bounds to a product/larger-bank statement. No step here uses that corollary.

The standard corrections remain active: no law-uniform pointwise quadratic-phase decay, no arbitrary-joint coarea cap, no worst conditional-density cap, no independence after rotation, and no conversion of small `||T||op` into a small random quadratic perturbation.

**Remaining full-target implication.** Starting from only `s3(A)>=1`, force one of:

1. a physical carrier `H` for which the stable-rank excess after spending the hostile rank satisfies `g_r>delta` at universal scale, so Theorem 2.1 applies;
2. an actual grouped projected-crossing/volume certificate satisfying every rank, product and row-marginal gate;
3. an already-paid high-leverage hub, ridge, grouped-bank, physical pair/triple, or dependence-safe Schur exit.

The bare three-eigenvalue hypothesis has not yet been shown to force this exhaustive alternative. Hence the full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

## 9. Source map

- Pinned Claude/Fourier source: `e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`.
- Designated partner fleet03/B12 r37: `3d6d9699d94146c3d2cbc475936dacd74109f913` plus projected-crossing addendum `5606cbf66c810119c1e7c0ca4908abe0eb753f56`.
- Previous fleet02/B12 six-mode compiler: `e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`.
- Current independently checked projected crossing: `829192412f2a2d84e72b4bed91115fc5fab68401`.
- Current owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.

Execution remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval/writeback is not authenticated native learned-memory ingestion.