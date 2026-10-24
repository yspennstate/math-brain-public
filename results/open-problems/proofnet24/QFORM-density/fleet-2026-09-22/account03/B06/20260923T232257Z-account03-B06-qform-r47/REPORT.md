SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T23:22:57Z.
attacking: QFORM-ANCHORED-K-RANKONE-SHEARFLAT-BANK-RECEIVER-v1; aggregate projected transverse anchored-K curvature across the original-product bank and force either a paid three-hub/rank-two branch or a finite heavy-shear-hub certificate.

# account03/B06 r47 — exact shear-flat normal form and disjoint pair-area payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`; programme revision `2026-09-22.5`  
**Assignment:** Curved fiber integration / quantitative inequalities and rigorous computations  
**Status:** `NEW SUPPORTING THEOREMS + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted owner conjecture remains OPEN. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis or post-rotation-independence hypothesis is added. Every probabilistic bank below consists of literal original coordinates. The main paid branch establishes absolute continuity and an essential `L^infinity` bound; continuity is not claimed for that branch. The separately scoped designated-partner branch gives a continuous two-dimensional pushforward density.

## 1. Fresh source boundary and immediate predecessor

Fresh `math-research-brain/main` at startup was

`4f02efd0c35bb09e6fc4a2faa82db9e5d58df285`,

with OWNER CONTROL revision `2026-09-22.15` and QFORM as the sole research target.

The live corrections retained include:

- no law-uniform pointwise quadratic-phase decay for arbitrary cap-one fragmented laws;
- no post-rotation independence;
- no dimension-free argument obtained by integrating unrestricted fiber suprema;
- no arbitrary-joint coarea cap or positive moment of worst conditional projection-density heights;
- no deletion of a small nonzero quadratic tail on arbitrary unbounded inputs;
- the critical rank-one same-bank half-Riesz endpoint is not used.

The immediate B06 predecessor is

`yspennstate/math-open-problems@8920450d29abb30e626d446497942ba3591146f0`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T222115Z-account03-B06-qform-r46/REPORT.md`.

It fixes a literal physical two-hub block

`A = [[H,E],[E^T,C]]`,                                               (1.1)

where `H` is an invertible `2 x 2` physical principal block,

`delta = det H != 0`,                                                (1.2)

and defines the anchored Schur-curvature matrix

`K = delta C - E^T adj(H) E`.                                        (1.3)

Thus the exact Schur residual is

`S = C-E^T H^(-1)E = K/delta`.                                      (1.4)

For an environment coordinate `j`, with `J=[m]\{j}`, r46 proved the exact three-hub volume identity

`Pi_3(B_j)
 = |delta|^(-1) sqrt(det(E_J E_J^T))
   ||P_(ker E_J) K[j,J]||_2`.                                       (1.5)

Consequently a nonzero projected anchored-`K` row is already paid by the completed three-original-hub receiver. The precise debt was the branch in which the projected rows are all zero or very small: the rank-one/shear-flat endpoint.

Two completed analytic inputs are used below at their proved scopes.

### 1.1 Bilateral rank-two half-Riesz receiver

Source used through the completed account02/B01 chain: for an exact residual quadratic polynomial on two disjoint ORIGINAL-coordinate banks whose cross block `N` has nonzero singular values `sigma_1,sigma_2`, arbitrary same-bank quadratic curvature and affine terms are allowed and

`H_(1/2)(R):=sup_t E|R-t|^(-1/2)
 <= 8 (sigma_1 sigma_2)^(-1/4).`                                    (1.6)

### 1.2 Hyperbolic physical-pair smoothing

For an invertible indefinite physical pair `H`, put

`D=|det H|`, `kappa=sigma_min(H)`.                                  (1.7)

If its exact residual obeys

`sup_t P(|R-t|<rho) <= H0 sqrt(rho)`,                               (1.8)

then the complete pair-plus-residual quadratic form satisfies

`||p_Q||_infinity <= 4 sqrt(2 H0) (D kappa)^(-1/4).`               (1.9)

This is the completed pair-log receiver. It is a dependence-safe curved-hyperbola smoothing estimate; it does not assume the numerical residual is independent of a rotated spectral variable.

## 2. Exact theorem: vanishing projected anchored-K rows force diagonal plus rank two

Write the columns of `E` as

`E=[e_1 ... e_m]`, `e_j in R^2`.                                  (2.1)

Assume throughout this section

`rank E=2`,                                                        (2.2)

and first take the no-coloop case

`rank E_J=2` for every `j`.                                        (2.3)

### Theorem 2.1 — `QFORM-SHEARFLAT-NORMAL-FORM-v1`

Under (2.2)-(2.3), the following are equivalent.

1. Every off-diagonal anchored-curvature row is shear-flat:

`P_(ker E_J) K[j,J]=0` for every `j`.                              (2.4)

2. There exist a symmetric `2 x 2` matrix `M` and a diagonal matrix `D0` such that

`boxed: K = E^T M E + D0.`                                        (2.5)

Equivalently the exact Schur residual has the original-coordinate normal form

`boxed: S = D + E^T T E`,                                         (2.6)

where `D=D0/delta` is diagonal and `T=M/delta` is symmetric.

Thus the simultaneous failure of all r46 projected-row receivers is not an arbitrary high-dimensional residual. It is exactly **diagonal plus rank at most two**, and all of the rank-two part factors through the same two-dimensional physical shear frame `E`.

### Proof

Assume (2.4). Because `E_J` has row rank two, for every `j` there is a unique vector `a_j in R^2` such that

`K[j,J] = a_j^T E_J`.                                              (2.7)

Choose `p,q` for which `e_p,e_q` are linearly independent. Define the linear map `M:R^2->R^2` by

`M e_p=a_p`, `M e_q=a_q`.                                         (2.8)

Symmetry of `K` gives

`a_p^T e_q=K_pq=K_qp=a_q^T e_p`.                                 (2.9)

For a linear map on a two-dimensional space, equality of the two cross matrix elements on one basis says its antisymmetric part vanishes; hence `M=M^T`.

For `j` different from `p,q`, symmetry again gives

`a_j^T e_p=K_jp=K_pj=a_p^T e_j
           =(M e_p)^T e_j=(M e_j)^T e_p`,                         (2.10)

where the last equality uses `M=M^T`. The same argument with `q` yields

`a_j^T e_q=(M e_j)^T e_q`.                                       (2.11)

Since `e_p,e_q` span `R^2`, (2.10)-(2.11) imply

`a_j=M e_j`.                                                       (2.12)

The same relation is true by definition for `j=p,q`. Hence for every `j!=k`,

`K_jk=a_j^T e_k=e_j^T M e_k`.                                    (2.13)

Defining

`(D0)_jj=K_jj-e_j^T M e_j`                                       (2.14)

proves (2.5). Conversely, if (2.5) holds, then for `k!=j`,

`K_jk=e_j^T M e_k`,                                               (2.15)

so `K[j,J]` lies in `rowspan(E_J)` and (2.4) follows. QED.

### Coloop endpoint

If (2.3) fails for some `h`, then deleting column `h` drops the two-frame rank. Every nonzero two-area minor of `E` must then contain `h`; in the normalized pair-area law introduced below, the physical coordinate `h` has inclusion marginal exactly one. Thus a shear coloop is already a literal one-coordinate heavy-hub certificate and is routed to the heavy branch rather than divided out.

## 3. Exact weighted cut factorization for the shear-flat normal form

Assume (2.6), and partition the environment ORIGINAL coordinates into two disjoint sets `I,J`. Since `D` is diagonal, it contributes no cross entries, so the exact physical cross block of the Schur residual is

`N=S[I,J]=E_I^T T E_J`.                                           (3.1)

Define the physical two-area currencies

`W_I=det(E_I E_I^T)`, `W_J=det(E_J E_J^T)`.                       (3.2)

### Theorem 3.1 — `QFORM-SHEARFLAT-CUT-FACTOR-v1`

If `det T!=0` and `W_I W_J>0`, then `N` has rank two and its two nonzero singular values obey

`boxed:
 sigma_1(N) sigma_2(N)
 = |det T| sqrt(W_I W_J).`                                        (3.3)

### Proof

For every two-set `P subset I` and two-set `Q subset J`,

`det N[P,Q]
 =det(E_P^T) det(T) det(E_Q)`.                                    (3.4)

Cauchy--Binet therefore gives

`e_2(N^T N)
 =sum_(P,Q) det N[P,Q]^2
 =(det T)^2
   [sum_P det(E_P)^2]
   [sum_Q det(E_Q)^2]`.                                           (3.5)

A second Cauchy--Binet identity gives

`sum_P det(E_P)^2=W_I`, `sum_Q det(E_Q)^2=W_J`.                   (3.6)

Since `rank N<=2`, its second exterior energy is exactly

`e_2(N^T N)=[sigma_1(N)sigma_2(N)]^2`.                            (3.7)

Equations (3.5)-(3.7) prove (3.3). QED.

This identity keeps the entire original-product bank. No individual minor is selected or inverted.

## 4. Product-weighted random cut: either rank-two payment or one heavy physical shear hub

Set

`G=EE^T`, `W=det G>0`,                                             (4.1)

and for physical two-sets `P={p,q}` let

`w_P=det(e_p,e_q)^2`.                                             (4.2)

Cauchy--Binet gives

`sum_P w_P=W`.                                                     (4.3)

Thus

`mu(P)=w_P/W`                                                      (4.4)

defines a probability law on physical pairs. For independent `P,Q~mu`, write

`Omega=P(P cap Q=empty)`.                                         (4.5)

### Lemma 4.1 — disjoint pair area produces a balanced physical cut

Randomly assign every physical environment coordinate independently to `I` or `J` with probability `1/2`. Then

`boxed:
 E[W_I W_J]=W^2 Omega/16.`                                        (4.6)

Consequently some deterministic partition obeys

`W_I W_J>=W^2 Omega/16`.                                          (4.7)

#### Proof

Expand `W_I` and `W_J` using (4.3). A term `w_P w_Q` contributes exactly when `P subset I` and `Q subset J`. This is impossible unless `P cap Q=empty`; for disjoint two-sets it has probability `2^-4=1/16`. Summing all ordered disjoint pairs gives (4.6), and (4.7) follows by averaging. QED.

### Corollary 4.2 — paid disjoint-shear branch

If

`Omega>=1/256`,                                                   (4.8)

then Lemma 4.1 gives a cut for which

`sqrt(W_IW_J)>=W/64`.                                             (4.9)

Theorem 3.1 therefore yields

`Delta:=sigma_1(N)sigma_2(N)
 >= |det T| W/64`.                                                 (4.10)

Apply the completed bilateral rank-two half-Riesz theorem (1.6) to the **exact** Schur residual. It permits the diagonal same-bank curvature in (2.6), so

`H_(1/2)(R)<=8 Delta^(-1/4)`.                                    (4.11)

Hence

`P(|R-t|<rho)
 <= sqrt(rho) E|R-t|^(-1/2)
 <= 8 Delta^(-1/4) sqrt(rho)`.                                   (4.12)

Now assume the physical outer hub `H` is indefinite, as in the live near-null hyperbolic debt, and put

`kappa=sigma_min(H)`.                                             (4.13)

Substitution of `H0=8 Delta^(-1/4)` into the complete physical-pair smoothing theorem (1.9) gives

`||p_Q||_infinity
 <=16 Delta^(-1/8) (|delta| kappa)^(-1/4)`.                       (4.14)

Using (4.10),

`boxed:
 ||p_Q||_infinity
 <=16 [64/(|det T| W)]^(1/8)
       (|delta| kappa)^(-1/4).`                                   (4.15)

The numerical prefactor is

`16*64^(1/8)=26.9086852881...`.                                  (4.16)

This is a target-level bound for the complete ambient form in the stated shear-flat/disjoint branch. All diagonal same-bank curvature, outside coefficients, affine terms created by conditioning, and the nonzero rank-two tail are retained. The bound proves absolute continuity and essential boundedness; continuity is not asserted by this proof.

### Corollary 4.3 — low disjointness forces a literal heavy shear hub

If instead

`Omega<1/256`,                                                    (4.17)

then the already proved pair-law lemma `PAIRLAW-DISJOINTNESS-SINGLE-HUB-v1` gives a physical coordinate `h` with pair inclusion marginal

`alpha_h:=mu(P:h in P)>3/5`.                                     (4.18)

The marginal has the exact frame formula

`boxed:
 alpha_h=e_h^T (EE^T)^(-1)e_h.`                                  (4.19)

Indeed

`sum_(j!=h) det(e_h,e_j)^2
 = e_h^T adj(G)e_h
 = W e_h^T G^(-1)e_h`.                                           (4.20)

Thus failure of the aggregate disjoint-shear payment forces one **literal original coordinate** to carry more than 60% of the whitened two-frame leverage. Since

`sum_h alpha_h=tr(G^(-1)G)=2`,                                   (4.21)

there can be at most three coordinates with `alpha_h>3/5`.

This gives the dimension-free trichotomy for the exact shear-flat endpoint:

1. a shear coloop, hence one literal leverage-one hub;
2. `Omega>=1/256`, hence the full density bound (4.15);
3. `Omega<1/256`, hence at most three literal heavy shear hubs carry every possible obstruction.

No unrestricted curved-fiber maximum appears anywhere in this reduction.

### Singular `T` endpoint

If `det T=0`, the non-diagonal part `E^T T E` has rank at most one. I do **not** apply a critical rank-one same-bank half-Riesz estimate here; that interface is invalid in the current correction ledger. The endpoint is recorded honestly as diagonal plus rank one, with the literal heavy-hub certificates above still available when its shear pair law is concentrated.

## 5. Designated account04/B06 result applied to the actual r47 frame

The newest designated partner result is

`yspennstate/math-open-problems@<commit-containing-r2>`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B06/20260923T231442Z-account04-B06-QFORM-r2/REPORT.md`,

`QFORM-FRESH-TRANSVERSE-CURVED-SECTION-v1`.

Its theorem starts with a two-row Parseval frame `(w,v)` on one original-coordinate bank satisfying

`w_i^2+v_i^2<=1/2`.                                                (5.1)

The r47 shear frame produces exactly such a frame after whitening:

`F=G^(-1/2)E`, `F F^T=I_2`.                                      (5.2)

If the rows of `F` are `w,v`, then for every physical environment coordinate `i`,

`w_i^2+v_i^2
 =e_i^T G^(-1)e_i
 =alpha_i`.                                                        (5.3)

Therefore on the actual diffuse r47 subbranch

`max_i alpha_i<=1/2`,                                             (5.4)

the partner theorem applies with the environment coordinates as its `(S)` bank and the outer physical hub variables as a fresh disjoint `(R)` bank. For

`L=<w,X_S>`, `V=<v,X_S>`,                                        (5.5)

any hub-measurable random variable `B`, any `lambda!=0`, any `beta`, and the off-fold event

`|V-v0|>r`,                                                       (5.6)

the exact two-dimensional curved-section pushforward

`(L+a, lambda(V-v0)^2+beta B+c)`                                  (5.7)

has a continuous density `g_r` satisfying

`boxed:
 ||g_r||_infinity <=4/(|lambda| r).`                              (5.8)

At the live numerical gate

`|lambda|>=1`, `r=1/64`,                                         (5.9)

this gives the actual inequality

`boxed: ||g_(1/64)||_infinity<=256.`                              (5.10)

This is a genuine use of the designated partner theorem on the r47 whitened shear frame. Its scope is deliberately separate from (4.15): it closes the **fresh-hub transverse curved-section** receiver, including arbitrarily small `beta`, but does not by itself absorb a second remainder depending on the same environment bank as `(L,V)`.

## 6. What this resolves and what remains

The r46 vague shear-flat failure has become an exact algebraic/probabilistic packet.

If all projected anchored-`K` rows vanish and the two-frame has no coloop, then the complete Schur residual is precisely

`S=D+E^T T E`.                                                     (6.1)

If `det T!=0`, aggregate the **whole physical pair-area law before choosing a cut**. Either its disjointness is at least `1/256`, in which case (4.15) pays the full ambient form, or one original coordinate has whitened leverage `>3/5`; at most three such coordinates exist. A shear coloop is an even stronger one-coordinate certificate. If `det T=0`, the remaining non-diagonal curvature is rank at most one and is retained rather than passed through a false critical half-Riesz bound.

Thus the next precise B06 debt is

`QFORM-SHEARFLAT-HEAVYHUB-OR-DIAGRANK1-RECEIVER-v1`:

> consume the at-most-three physical heavy-shear hubs, or the `det T=0` diagonal-plus-rank-one endpoint, with a product-preserving physical-pivot / grouped-square / fresh-transverse compiler while retaining the complete diagonal Schur curvature and the nonzero outer hyperbolic hub. The desired output is a universal numerical bound or a further finite physical-hub packet, not a worst conditional fiber supremum.

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains OPEN. The main r47 paid branch proves essential boundedness; the designated partner subbranch (5.8) has a continuous `C_0` two-dimensional density.

## 7. Computation

`check_r47.py` and `CHECKS.md` accompany this report. They verify the exact algebraic identities and constants on random finite matrices, including the normal-form projection identity, singular-product factorization, Cauchy--Binet area identity, exhaustive random-cut expectation, and leverage/marginal identity. These are sanity checks only and are not used as proofs.
