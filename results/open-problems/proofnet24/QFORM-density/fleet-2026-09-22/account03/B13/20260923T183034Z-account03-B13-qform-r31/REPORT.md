SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T18:30:34Z.
attacking: sharpen the high-concentration algebraic reduction by retaining a real physical pivot as a finite hub set, rather than absorbing it into the low-rank skeleton; prove an exact weighted bordered-completion theorem and apply it to the aggregate third-volume slab inequality.

# account03/B13 r31 — weighted physical-pivot completion and finite-hub low-rank reduction

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: extremal product laws. Execution context: `WITHOUT_VERIFIED_BRAIN`.

Status: **NEW PROVED DETERMINISTIC COMPLETION LEMMA + NEW HIGH-SLAB STRUCTURAL CONSEQUENCE / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

No Gaussian, moment, compact-support, connected-support, post-rotation independence, interval-extremality, or perturbative deletion assumption is used. The new lemma is purely an original-coordinate determinant identity. Its slab application uses the current reviewed projected-crossing source and the designated account04/B13 exact product purification.

## 1. Source refresh and premises

Fresh owner control remained QFORM-only, revision `2026-09-22.15`. The current release still states that unrestricted rough-law QFORM is OPEN.

The designated partner result is account04/B13's nonattained bathtub purification:

`yspennstate/math-open-problems` current source path
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260923T121154Z-account04-B13-nonattained-bathtub-r1/REPORT.md`.

For every nonnegative measurable kernel `K`,

    sup_{0<=f_i<=1, int f_i=1} int K(x) prod_i f_i(x_i) dx
      = sup_{|E_i|=1} int_{prod_i E_i} K(x) dx,                    (1.1)

with no optimizer asserted. Thus a strict slab inequality proved for unit product indicators transfers with zero limiting constant loss to every admissible product law. No single interval, common diameter, or fixed fragment count is introduced.

The previous B13 run r30 proved, from the physical third-volume cascade, that for slab ratio

    rho = P{X^T A X in J}/|J|,

one has

    V_3(A) <= 64 C_3^6 rho^(-6),
    C_3 = 9 sqrt(3e),                                             (1.2)

where

    V_r(A) = sum_{|S|=|T|=r, S cap T = empty} det A[S,T]^2.      (1.3)

At r30 publication the grouped projected-crossing receiver was still marked pending independent review. The current source checkpoint `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`, retained in the final release, supplies the full weighted-subset/grouped-hub proof; the owner continuation records the projected-crossing extension as independently checked. No later correction found in the refreshed control invalidates (1.2). The skeleton addendum corrects an equality to an upper bound, but explicitly preserves the robust consequence. Accordingly (1.2) can now be used without r30's former `pending receiver review` qualifier, while the full QFORM theorem remains open.

For the high-ratio exhaustion below I also use the already-proved localized physical-triple compiler from r24: if a physical 3x3 principal block has smallest singular value at least `s`, then

    ||p_Q||_infinity <= C_0/s,
    C_0 = 128*2^(1/4).                                           (1.4)

All outside couplings and induced affine terms are retained in that theorem.

## 2. New deterministic theorem: weighted physical-pivot complement completion

### Theorem 2.1 — `QFORM-WEIGHTED-PIVOT-COMPLEMENT-v1`

Let `A` be real symmetric. Fix an integer `r>=1` with `V_r(A)>0`. For every ordered pair of disjoint `r`-sets `(S,T)` with `det A[S,T] != 0`, let

    H = S union T,
    K = [n] \ H,
    B = A[S,T],
    P^{S,T} = A[K,T] B^(-1) A[S,K].                              (2.1)

Then `rank P^{S,T} <= r`. Put

    L^{S,T} = (P^{S,T} + (P^{S,T})^T)/2,                         (2.2)

so `L^{S,T}` is symmetric of rank at most `2r`. There is a diagonal matrix `D^{S,T}` on `K` and a symmetric zero-diagonal matrix `E^{S,T}` such that

    A[K,K] = D^{S,T} + L^{S,T} + E^{S,T},                       (2.3)

and, under the determinant-squared probability law

    w_{S,T} = det(A[S,T])^2 / V_r(A),                            (2.4)

one has the average bound

    E_w ||E^{S,T}||_F^2
       <= (r+1)^2 V_{r+1}(A)/V_r(A).                             (2.5)

Consequently some nonsingular physical pivot satisfies

    ||E^{S,T}||_F
       <= (r+1) sqrt(V_{r+1}(A)/V_r(A)).                         (2.6)

If `V_{r+1}(A)=0`, then for every nonsingular seed `(S,T)` the completion is exact and may be chosen with a **symmetric rank-at-most-r** matrix:

    A[K,K] = D^{S,T} + P^{S,T},
    P^{S,T}=(P^{S,T})^T,
    rank P^{S,T} <= r.                                           (2.7)

#### Proof

Fix a nonsingular seed `(S,T)`. For distinct `k,l in K`, append `k` to the seed rows and `l` to the seed columns. The bordered determinant formula gives, up to the harmless sign coming from a chosen ordering,

    Delta_{kl}^{S,T}
      := det A[S union {k}, T union {l}]
       = det(B) [a_{kl} - A[k,T] B^(-1) A[S,l]].                (2.8)

Thus, with

    R_{kl}=a_{kl}-P^{S,T}_{kl},

we have

    |R_{kl}|^2 = |Delta_{kl}^{S,T}|^2 / |det B|^2,  k!=l.       (2.9)

Choose the diagonal in (2.3) by

    D_{kk}^{S,T}=a_{kk}-L_{kk}^{S,T}.

For `k!=l`, symmetry of `A` gives

    E_{kl}^{S,T}
      = a_{kl} - (P_{kl}^{S,T}+P_{lk}^{S,T})/2
      = (R_{kl}+R_{lk})/2.                                      (2.10)

Therefore

    |E_{kl}^{S,T}|^2
      <= (|R_{kl}|^2+|R_{lk}|^2)/2,

and summing over ordered distinct pairs yields

    ||E^{S,T}||_F^2
      <= sum_{k!=l in K}|R_{kl}|^2
      = |det B|^(-2) sum_{k!=l in K}|Delta_{kl}^{S,T}|^2.       (2.11)

Multiply by `det(B)^2` and sum over all nonsingular disjoint seeds. A fixed ordered disjoint pair of `(r+1)`-sets `(S',T')` can arise from at most `(r+1)^2` seed/deleted-row/deleted-column choices. Seeds left singular by a deletion simply do not occur in the left side. Hence

    sum_{S,T:det B!=0} det(B)^2 ||E^{S,T}||_F^2
      <= (r+1)^2 V_{r+1}(A).                                    (2.12)

Divide by `V_r(A)` to obtain (2.5), and (2.6) follows by averaging.

If `V_{r+1}=0`, then every bordered determinant in (2.8) vanishes, so `R_{kl}=0` for all distinct `k,l`. Therefore the off-diagonal entries of `P^{S,T}` equal those of the symmetric matrix `A[K,K]`, and hence `P^{S,T}` itself is symmetric. (Diagonal entries do not affect symmetry.) Then `A[K,K]-P^{S,T}` is diagonal and (2.7) follows. QED.

### Why this formulation matters

The robust global skeleton theorem absorbs the seed coordinates into a larger low-rank matrix. Theorem 2.1 instead **retains the actual original-coordinate seed as a finite hub set** and only compresses the complementary self-curvature. That is the useful format for the grouped-hub Fourier/crossing receivers: arbitrary hub functions and hub-to-light couplings can remain visible rather than being hidden in an abstract rank factorization.

## 3. Exact algebraic classification when the third disjoint volume vanishes

### Corollary 3.1 — `QFORM-V3-ZERO-FINITE-HUB-CLASSIFICATION-v1`

If `V_3(A)=0`, exactly one of the following structural cases applies.

1. `V_2(A)>0`: choose any nonsingular disjoint physical 2x2 pivot. After deleting its at most four original coordinates,

       A[K,K] = D_K + R_K,
       rank R_K <= 2,                                            (3.1)

   with `D_K` diagonal and `R_K` symmetric.

2. `V_2(A)=0` but `V_1(A)>0`: choose any nonzero off-diagonal entry `a_ij` as a disjoint 1x1 pivot. After deleting the two physical coordinates `{i,j}` one has

       A[K,K] = D_K + R_K,
       rank R_K <= 1.                                            (3.2)

3. `V_1(A)=0`: `A` is diagonal.                                  (3.3)

This is an exact classification of the **complementary self block**, not a claim that the full matrix is diagonal plus rank two. The hub block and hub-to-complement couplings remain arbitrary, exactly as required by the original-coordinate product geometry.

#### Proof

If `V_2>0`, apply Theorem 2.1 with `r=2` and `V_3=0`, obtaining (3.1). If `V_2=0<V_1`, apply it with `r=1`, giving (3.2). Finally `V_1=sum_{i!=j}a_ij^2`; thus `V_1=0` means every off-diagonal entry vanishes. QED.

This exact endpoint is stronger than merely saying `A` is close to a bounded-rank matrix: it identifies the finite physical hubs and preserves arbitrary translations/couplings through them.

## 4. New high-slab finite-hub reduction

### Theorem 4.1 — `QFORM-HIGHRATIO-FINITE-HUB-RANK4-COMPLEMENT-v1`

Assume `A` has at least three eigenvalues of absolute value at least one and let a slab have ratio `rho`. Suppose

    rho > C_0+2 = 128*2^(1/4)+2.                                 (4.1)

Then there exists a set `H` of at most four original coordinates, with complement `K`, for which

    A[K,K] = D_K + R_K + E_K,                                   (4.2)

where `D_K` is diagonal, `R_K` is symmetric of rank at most four, `E_K` is symmetric zero-diagonal, and

    ||E_K||_F <= K_hub/rho,
    K_hub = 24 C_3^3
          = 24 (9 sqrt(3e))^3
          = 407438.791453379... .                                (4.3)

There is a sharper two-hub branch with rank at most two and residual `<2/rho`.

#### Proof

Split according to the same aggregate currencies as r30.

**Case A: `V_2(A)>=rho^(-4)`.** By (1.2),

    V_3/V_2 <= 64 C_3^6 rho^(-2).                               (4.4)

Apply Theorem 2.1 with `r=2`. A nonsingular disjoint 2x2 pivot exists, its union is a physical hub set of size four, and on the complement

    rank R_K <= 4,
    ||E_K||_F
       <= 3 sqrt(V_3/V_2)
       <= 24 C_3^3/rho.                                         (4.5)

**Case B: `V_2(A)<rho^(-4)` but `V_1(A)>=rho^(-2)`.** Apply Theorem 2.1 with `r=1`:

    ||E_K||_F
       <= 2 sqrt(V_2/V_1)
       < 2/rho,                                                  (4.6)

and `rank R_K<=2` after retaining only two physical hub coordinates.

**Case C: `V_1(A)<rho^(-2)`.** This is impossible under (4.1). Let `D_0=diag(A)`, `O=A-D_0`. Then `||O||_op<=||O||_F<1/rho`. Since `s_3(A)>=1`, the third singular value of `D_0` is `>1-1/rho`; hence three physical diagonal entries have modulus `>1-1/rho`. The corresponding physical 3x3 block has smallest singular value `>1-2/rho`. By (1.4),

    rho <= C_0/(1-2/rho),

so `rho-2<C_0`, contradicting (4.1). This exhausts the cases and proves the theorem. QED.

### Comparison with r30

r30 gave a global

    A = diagonal + rank<=8 + E,  ||E||_F <= 72 C_3^3/rho.

Theorem 4.1 gives a different and, for hub methods, sharper object:

* at most four **named original coordinates** are retained as hubs;
* the complementary self block is diagonal plus rank at most four;
* the Frobenius residual constant improves by a factor three, from `72 C_3^3` to `24 C_3^3`;
* in the low-`V_2` branch only two hubs, rank two, and `<2/rho` remain.

No small quadratic residual is discarded. Equation (4.2) is only a coefficient decomposition.

## 5. Pivotwise scale-free tradeoff

For every nonsingular disjoint physical 2x2 pivot `B=A[I,J]`, with `K` its complement, Theorem 2.1 before averaging gives

    |det B| * dist_F(A[K,K], Diag + SymRank<=4)
       <= sqrt(V_3(A)).                                          (5.1)

Combining with (1.2),

    |det B| * dist_F(A[K,K], Diag + SymRank<=4)
       <= 8 C_3^3 rho^(-3)
       = 135812.930484459... rho^(-3).                           (5.2)

Thus a bad slab cannot simultaneously carry a moderately large physical two-pivot and substantial complementary non-diagonal/non-rank-four self-curvature. For example, if

    |det B| >= eta rho^(-2),

then

    dist_F(A[K,K], Diag + SymRank<=4)
       <= (8 C_3^3/eta) rho^(-1).                                (5.3)

This statement avoids the false inference that one uniformly good minor must exist: it is a quantitative tradeoff valid for **every** nonsingular physical pivot.

## 6. Actual use of the designated account04/B13 purification theorem

The new high-slab statements are first read as assertions about a unit-product-set slab witness. In that setting the aggregate third-volume inequality (1.2), and therefore (4.4), feed directly into Theorem 2.1.

Now suppose arbitrary admissible densities `f_i` gave a strict violation of either (4.2)-(4.3) or the pivotwise tradeoff (5.2) at slab ratio `rho_0`. The matrix `A`, all determinant currencies, and the candidate pivot/complement distances are deterministic and unchanged under purification. Choose `epsilon>0` so small that the same strict violation persists with `rho_0-epsilon` in the right side. The account04/B13 no-attainment theorem (1.1) supplies a unit-product indicator witness for the same `A,J` with slab ratio at least `rho_0-epsilon`. Applying the indicator inequality gives the contradiction. Letting `epsilon downarrow 0` transfers the new inequalities to the entire cap-one product class with zero constant loss.

This is an application of the completed partner result to the **actual finite-hub/pivot-distance inequality**, not an appeal to interval extremality or to an attained optimizer.

## 7. Exact checks

A fractions-only diagnostic on a fixed 7x7 symmetric integer matrix gave

    V_2 = 5980,
    V_3 = 34868,
    weighted mean unsymmetrized residual^2 = 47.3806020066...,
    weighted mean symmetrized residual^2   = 31.5996655518...,
    9 V_3/V_2                              = 52.4769230769...,

with 184 nonsingular disjoint 2x2 seeds. Both required inequalities held exactly before decimal conversion. The diagnostic checks the bordered determinant/counting implementation only; the proof is the algebra above.

Constants:

    C_3 = 25.70102107534928...,
    C_0 = 152.2185107203483...,
    C_0+2 = 154.2185107203483...,
    8 C_3^3  = 135812.93048445976...,
    24 C_3^3 = 407438.7914533793....

## 8. Remaining implication

**Full unrestricted QFORM remains OPEN. Full continuity remains OPEN.**

The first B13 obligation is now sharper:

`QFORM-FINITE-HUB-DIAG-RANK4-ROUGH-GLUE-v1`.

For a high-ratio witness, Theorem 4.1 reduces the complementary **self-curvature** to diagonal plus rank at most four plus an `O(1/rho)` Frobenius twist after at most four physical hubs. What remains is to combine this with the reviewed grouped-hub/projected-crossing theorem without deleting the small residual on unbounded fragmented laws. Concretely, one must show that either:

1. the hub-to-light cross block plus the rank-four complement supplies a paid `k+ell>2` grouped-crossing certificate with its volume marginals satisfied; or
2. the slab-conditioned core mechanism converts the residual into positive slab-scale geometric spread that itself forces such a certificate.

The exact endpoint `V_3=0` is now reduced to at most four physical hubs plus an exact diagonal+rank-two complementary self block; that is the cleanest algebraic test case for the next analytic glue theorem.

No target-level solution is claimed here.
