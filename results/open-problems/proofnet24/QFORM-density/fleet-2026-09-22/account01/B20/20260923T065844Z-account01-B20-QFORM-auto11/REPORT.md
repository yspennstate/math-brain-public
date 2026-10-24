SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-23T06:58:44Z.
attacking: account02/B20's anchored-compound low-rank compiler; pay the rank-two three-dimensional-source branch down to an actual near-kernel vector, and disjointize the remaining low-rank aggregate packets in original coordinates.

# account01/B20 — rank-two near-kernel reduction and zero-diagonal physical-cut compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.
Classification: `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING LEMMA / FULL TARGET OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Global continuity: `OPEN`; continuity is proved only on the analytic subbranch explicitly paid below.

## 1. Fresh control and source boundary

Pre-write owner control was read at

`yspennstate/math-research-brain@a9e737850fd9b3249920a4ee96f000fe4878de5a`

and remains revision `2026-09-22.15`, QFORM-only, with no later B20 stop observed before this write.

The account02/B20 result consumed at equation level is the anchored-compound low-rank compiler in

`yspennstate/math-open-problems@328f5b408292534e743f31c7d2114b55b3aa0699`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T060103Z-account02-B20-QFORM-r25/EARLY_CHECKPOINT.md`.

In the exact-rank-three physical collar, around an ORIGINAL anchor `i`, write

`A=[[a,b^T],[b,H]]`,
`d=(H_jj)_j`,
`T=aH-bb^T`,
`N=diag(b)H-d b^T`.

With `mu=1/192`, its theorem gives, unless an earlier paid branch has fired, at least one of

(A) `||T||op > 1/(16 sqrt(3))`,

(B) `||N||op > 1/(16 sqrt(6))`,

(C) an ORIGINAL-coordinate cross cut `C=A[{i} union L,R]` with

`e2(CC^T)>1/1536`.

It also proves `rank(T)<=2`, `rank(N)<=4`, and explicitly warns that aggregate compound mass cannot in general be replaced by one uniformly good physical minor.

The analytic receiver used below is the completed account01/B19 theorem

`QFORM-RANK2-CROSS-TRANSVERSE-UNIFORM-NEARNULL-v1`

at

`yspennstate/math-open-problems@db8045af54fae8ee75eca16efa93b067b9e9f9cd`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260923T060843Z-account01-B19-QFORM-auto11/REPORT.md`.

For disjoint ORIGINAL product banks `U,V`, an exact rank-two physical cross block of singular product `rho=s1s2`, and a three-dimensional source subspace `E` containing `range(C)` and `range(B)`, let `P=range(C)`, let `r` span `E cap P^perp`, and put

`lambda=r^TBr`, `delta=||PBr||_2`.

Whenever `(lambda,delta)!=(0,0)`, that theorem gives a continuous density with

`||p_Q||inf <= 8.912 (lambda^2+delta^2)^(-1/8) rho^(-3/8)`.

All uses below remain within these stated scopes. No independence is asserted after a spectral or singular-vector rotation.

## 2. Account02/B20 packet (C): a fixed universal payment down to a full near-kernel vector

Assume packet (C), and first assume its physical cross block has exact rank two. Then

`e2(CC^T)=(s1s2)^2=rho^2`,

so the actual account02/B20 inequality gives

`rho > 1/sqrt(1536)`.                                            (2.1)

Now suppose one physical bank is in the three-dimensional source-side scope of the B19 receiver above. Because `PBr` and `(r^TBr)r` are orthogonal,

`R:=sqrt(lambda^2+delta^2)=||Br||_2`.                             (2.2)

If

`R>=1/64`,                                                        (2.3)

then the B19 theorem and (2.1) give the concrete target-level inequality

`||p_Q||inf
 < 8.912 * 64^(1/4) * 1536^(3/16)
 = 99.7627757581...
 < 100`.                                                          (2.4)

Thus the entire fixed-strength transverse row is paid, not merely its scalar Rayleigh component. In particular this covers the exact-null endpoint `lambda=0` whenever `delta>=1/64`, the punctured small-`lambda` strip, either sign of `lambda`, arbitrary opposite-bank self curvature, and arbitrary cap-one product marginals in the receiver's stated scope. The density is continuous on this paid subbranch.

Consequently any still-unpaid rank-two packet-(C) state **within the three-dimensional source-side scope** must satisfy the strictly stronger near-kernel condition

`boxed: ||Br||_2 < 1/64`.                                        (2.5)

This improves the previous residual description `|r^TBr|<1/64`: the entire action of the source self matrix on the cross-null transverse direction is small.

No claim is made that every rank-two packet-(C) cut has such a three-dimensional source side. The other residuals remain explicit below.

## 3. New deterministic lemma: zero-diagonal matrices have a strong physical cut

### Lemma 3.1 — `QFORM-ZERODIAG-CUT-DISJOINTIZATION-v1`

Let `Z` be any finite real matrix indexed by the same physical coordinate set on its rows and columns, with `Z_jj=0` for every coordinate. Then there is a partition of the physical coordinates into disjoint banks `L,R` such that

`boxed: ||Z[L,R]||op >= (1/4)||Z||op`.                            (3.1)

The matrix need not be symmetric.

### Proof

Choose unit left/right singular vectors `x,y` with signs so that

`x^T Z y=||Z||op`.

Independently color each physical coordinate left or right with probability `1/2`. Then, because the diagonal of `Z` vanishes,

`E[x_L^T Z[L,R] y_R]
 = sum_(j!=k) P(j in L,k in R) x_j Z_jk y_k
 = (1/4) x^T Z y
 = (1/4)||Z||op`.                                                 (3.2)

Hence one deterministic coloring satisfies

`x_L^T Z[L,R] y_R >= (1/4)||Z||op`.

For that coloring the two restricted vectors are nonzero, and their Euclidean norms are at most one, so

`||Z[L,R]||op
 >= |x_L^T Z[L,R]y_R|/(||x_L|| ||y_R||)
 >= (1/4)||Z||op`.

This proves (3.1). Every bank is an ORIGINAL-coordinate bank; no probabilistic coordinates are rotated.

## 4. Apply Lemma 3.1 to account02/B20 packet (B)

Recall

`N=diag(b)H-d b^T`, `d_j=H_jj`.

Its diagonal vanishes exactly:

`N_jj=b_jH_jj-d_jb_j=0`.                                         (4.1)

Packet (B) gives

`||N||op > 1/(16 sqrt(6))`.                                       (4.2)

Lemma 3.1 therefore gives disjoint physical banks `L,R` with

`||N[L,R]||op > 1/(64 sqrt(6))`.                                  (4.3)

But

`N[L,R]=diag(b_L)H[L,R]-d_L b_R^T`.                              (4.4)

Using the operator norm triangle inequality,

`||N[L,R]||op
 <= ||b_L||infinity ||H[L,R]||op + ||d_L||_2 ||b_R||_2`.          (4.5)

Thus at least one of the following fixed product currencies is present:

`boxed: ||b_L||infinity ||H[L,R]||op > 1/(128 sqrt(6))`,           (4.6)

or

`boxed: ||d_L||_2 ||b_R||_2 > 1/(128 sqrt(6))`.                   (4.7)

Numerically the threshold is

`1/(128 sqrt(6)) = 0.003189439769...`.

This is not yet a density payment. It is a genuine reduction of the one-overlap aggregate packet to two disjoint ORIGINAL-coordinate bank resources. It spends the aggregate before taking any reciprocal small coefficient and does not infer a single good minor.

## 5. Apply the same cut mechanism to account02/B20 packet (A)

Now assume

`||T||op > tau_T:=1/(16 sqrt(3))`,
`T=aH-bb^T`,
`rank(T)<=2`,

with `T` symmetric.

If

`max_j |T_jj| > tau_T/2 = 1/(32 sqrt(3))`,                        (5.1)

then there is a fixed-strength ORIGINAL anchored principal compound

`boxed: |aH_jj-b_j^2| > 1/(32 sqrt(3))`.                          (5.2)

Otherwise put `O=T-diag(T)`. Then

`||O||op >= ||T||op-||diag(T)||op > tau_T/2`.                     (5.3)

The matrix `O` has zero diagonal, so Lemma 3.1 gives disjoint physical banks `L,R` with

`||T[L,R]||op=||O[L,R]||op > tau_T/8 = 1/(128 sqrt(3))`.          (5.4)

Since

`T[L,R]=aH[L,R]-b_Lb_R^T`,                                       (5.5)

at least one of

`boxed: |a| ||H[L,R]||op > 1/(256 sqrt(3))`,                      (5.6)

or

`boxed: ||b_L||_2 ||b_R||_2 > 1/(256 sqrt(3))`                    (5.7)

must hold. The numerical threshold in (5.6)-(5.7) is `0.002255274489...`.

Therefore packet (A) no longer needs to remain as the abstract norm `||aH-bb^T||op`: it routes either to a strong anchored principal compound or to one of two explicit disjoint-bank product currencies.

Again, (5.2), (5.6), and (5.7) are structural currencies, not standalone density theorems.

## 6. What has actually closed, and what remains

The account02/B20 anchored-compound compiler now admits the following sharpened continuation.

### Packet (C)

- rank-three / substantial third singular value / diffuse third-volume marginal: already paid in the partner checkpoint;
- rank-two with a three-dimensional source side and `||Br||>=1/64`: **paid here with `||p_Q||inf<100`**, continuously;
- remaining rank-two three-dimensional-source state: `||Br||<1/64`;
- rank-two cuts lacking a usable three-dimensional source side: still open;
- rank-three low-third-singular or localized-volume states: still open.

### Packet (B)

It now contains disjoint physical banks satisfying (4.6) or (4.7). The unresolved analytic step is to pay one of these bank-product currencies while retaining arbitrary same-bank curvature and outside couplings.

### Packet (A)

It now contains either the strong physical anchored compound (5.2), or disjoint banks satisfying (5.6) or (5.7). The unresolved step is again an aggregate payment; no one-good-minor shortcut is permitted.

Accordingly the first sharply formulated analytic debt on the packet-(C) route is

`QFORM-C-RANK2-NEARKERNEL-PAYMENT-v1`:

> In the exact-rank-three collar, start from a physical cross cut with `e2(CC^T)>1/1536`, `rank(C)=2`, a three-dimensional source side, and its transverse unit vector `r` satisfying `C^T r=0` and `||Br||<1/64`. Route this near-kernel state, using ORIGINAL-coordinate product provenance, to a paid physical-pair/grouped/ridge packet or prove a direct universal density bound.

The near-kernel statement is deterministic and quantitatively compatible with the spectral-floor geometry: for the padded vector `z=(r,0)` one has `||Az||=||Br||<1/64` because `C^T r=0`. Hence the spectral floor forces `z` to lie within `1/64` of the global kernel in the exact-rank-three collar. Turning that near-kernel geometry into a product-preserving physical-coordinate payment is the next substantive task; no rotated random coordinate should be conditioned as if independent.

## 7. Scope audit

This run does **not** use or claim:

- law-uniform pointwise quadratic oscillatory decay;
- independence after spectral/SVD rotation;
- the refuted arbitrary-joint rank-three coarea inequality;
- positive moments of conditional projection-density suprema;
- a worst-fiber supremum;
- one-good-minor extraction from diffuse compound mass;
- Gaussianity, iid, moments, compact support, connected support or log-concavity.

All new partitions are partitions of original coordinate indices. Singular/eigenvectors appear only inside deterministic matrix inequalities. The full QFORM conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`; global continuity remains OPEN.
