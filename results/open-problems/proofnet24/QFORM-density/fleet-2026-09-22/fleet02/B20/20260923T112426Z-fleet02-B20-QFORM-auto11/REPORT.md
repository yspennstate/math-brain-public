SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-23T11:24:26Z.
attacking: the arbitrary-extra-spectrum no-pivot branch by converting high spectral leverage into a literal original-coordinate three-bank star resource, then routing its arbitrary leaf curvature through disjoint volume / low-rank completion.

# fleet02/B20 auto11 — arbitrary-rank high-leverage N3 compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: proof closure / keeper, pathway SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / GLOBAL-N3-ARBITRARYRANK-HIGHLEVERAGE-COMPILED / DISJOINT5-ROUTING / PURESTAR-ENDPOINT-REFUTED / FULL-QFORM-OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. No statement below assumes moments, bounded or connected support, log-concavity, Gaussianity, diagonal-basis independence, or independence after a rotation/projection. Spectral projections are used only as deterministic matrix certificates. Every probabilistic bank is a bank of original independent coordinates. Continuity is separate except on already-completed source theorems which explicitly prove it.

## 1. Source-pinned reduction and first global split

The current no-pivot synthesis proves that, for one fixed universal `tau>0`, a universal density bound on the class

`N3(tau): s3(A)>=1, |A_ii|<tau, |A_ii A_jj-A_ij^2|<tau for all i!=j`

implies the full target. I use `tau=1/64` throughout.

The required interactive source also gives the unrestricted fifth-volume exit: for any ORIGINAL disjoint-coordinate cross block `M`,

`Z5=e5(M^T M),`

`||p_Q||_infinity <= 5 sqrt(2e) Z5^(-1/10).`                  (1.1)

Thus

`Z5>=1/1024  =>  ||p_Q||_infinity <=10 sqrt(2e)<23.317.`      (1.2)

This is a direct density estimate retaining arbitrary self blocks, outside couplings and affine terms.

Let

`P=1_{[1,infinity)}(|A|)`                                     (1.3)

be the deterministic spectral projection onto all eigendirections of `A` with `|lambda|>=1`. Since `A^2-P` is positive semidefinite,

`(A^2)_ii >= P_ii`                                             (1.4)

for every original coordinate `i`.

This produces an exhaustive global N3 split:

* **high spectral leverage:** some original coordinate `h` has `P_hh>=1/2`;
* **low spectral leverage:** every `P_ii<1/2`.

The first branch is compiled quantitatively below for arbitrary rank and arbitrary extra spectrum. The second branch is now the first globally untouched implication.

## 2. New theorem: arbitrary-rank high leverage forces a robust physical three-bank star

### Theorem `QFORM-N3-ARBITRARYRANK-HIGHLEVERAGE-THREEBANK-v1`

Assume `A in N3(1/64)` and let `P` be (1.3). If for some original coordinate `h`,

`P_hh>=1/2`,                                                   (2.1)

then the literal physical star at `h` satisfies

`sum_(j!=h) A_hj^2 > 2047/4096`.                              (2.2)

Every individual star edge satisfies

`A_hj^2 < 65/4096`.                                            (2.3)

Consequently the star has at least 32 nonzero leaves, and there exist three pairwise disjoint ORIGINAL-coordinate leaf banks `J1,J2,J3` such that

`boxed: sum_(j in J_k) A_hj^2 >= 639/4096,  k=1,2,3.`         (2.4)

No rank assumption on `A` appears.

### Proof

By (1.4) and (2.1),

`(A^2)_hh >=1/2.`                                              (2.5)

The `hh` entry of `A^2` is the squared Euclidean norm of the physical row:

`(A^2)_hh=A_hh^2+sum_(j!=h)A_hj^2.`                           (2.6)

Since `|A_hh|<1/64`, (2.2) follows:

`sum_(j!=h) A_hj^2 >1/2-1/4096=2047/4096.`                   (2.7)

For `j!=h`, the no-pivot principal-minor condition gives

`|A_hh A_jj-A_hj^2|<1/64.`                                   (2.8)

Hence, using both diagonal caps,

`A_hj^2 <1/64+1/4096=65/4096,`                               (2.9)

which is (2.3). In particular fewer than 32 nonzero edges would have total square mass strictly below

`32*(65/4096)=2080/4096`;                                    (2.10)

and more sharply `31*(65/4096)=2015/4096<2047/4096`, so at least 32 nonzero leaves are necessary.

Set

`S0=2047/4096,  w=65/4096,  a=(S0-2w)/3=639/4096.`           (2.11)

Greedily take a minimal first bank with square-mass at least `a`. Minimality and the pointwise cap imply its mass is `<a+w`. Repeat on the remaining leaves for a second bank. The leftover mass is then strictly larger than

`S0-2(a+w)=a.`                                                (2.12)

and contains a third bank of mass at least `a`. This proves (2.4). QED.

### Significance

The preceding exact-rank-three star theorem required a factorization `A=RMR^T`. The argument above uses only `A^2>=P` and therefore survives arbitrary additional eigenvalues. The spectral projection is never applied to the random vector. The actual smoothing resource (2.4) is formed solely from original-coordinate coefficients `A_hj` and original independent banks.

## 3. Arbitrary leaf curvature is now routed exactly before any inversion

Let `T={h}^c` be the physical leaf bank and `B=A[T,T]`. I apply the completed fleet02/B09 arbitrary-curvature result to this exact star.

Define the intrinsic disjoint five-volume

`Omega5(B)=sum_{S cap R=empty, |S|=|R|=5} det B[S,R]^2.`      (3.1)

The completed theorem gives

`Omega5(B)>0  =>
 ||p_Q||_infinity <=10 sqrt(2e) Omega5(B)^(-1/10).`           (3.2)

This follows by random ORIGINAL-coordinate bipartition and the source-pinned D5 estimate (1.1). It is already a linear interval estimate; however (3.2) is not a universal closure when `Omega5` may be arbitrarily small.

At the exact-zero endpoint, let `dr(B)` be the largest `k` admitting an invertible disjoint `k x k` minor. Then `Omega5(B)=0` implies

`dr(B)<=4.`                                                    (3.3)

For a maximal disjoint physical pivot `S,R`, `|S|=|R|=k`, conditioning only the at most `2k<=8` literal pivot coordinates leaves a principal block

`B[L,L]=D+C`,                                                  (3.4)

where `D` is diagonal and `C` is symmetric of rank at most `k`. This is exact: for `P0=B[S,R]`, one may take

`C=B[L,R] P0^(-1) B[S,L]`,                                   (3.5)

and maximality makes every off-diagonal Schur remainder vanish.

If `rank(C)=r>=1`, the completed one-hub Pluecker smoother applies whenever the surviving star `c_L=A[L,h]` is quantitatively transverse to `range(C)` and the determinant-weighted coefficient frame has positive disjointness `rho`. In an eigen-expansion of `C`, it gives exactly

`||p_Q||_infinity
 <=((r+2)/r) exp((r+1)/(r+2))
 [rho |pdet(C)| dist(c_L,range(C))^2]^(-1/(r+2)).`             (3.6)

All same-side diagonal curvature and arbitrary outside terms are retained. No projected independence is used.

Thus the high-leverage branch is no longer an undifferentiated arbitrary-curvature star. It is reduced to:

1. small positive `Omega5`, where (3.2) is quantitative but may be large;
2. `Omega5=0`, `1<=dr(B)<=4`, with a bounded literal pivot set of size at most eight, and failure only through low transverse resource / zero Pluecker disjointness / alignment;
3. the apparent `dr(B)=0` pure-star endpoint, which is actually impossible under the three-large-eigenvalue target, as shown next.

## 4. New obstruction theorem: the pure physical star endpoint cannot satisfy the target

### Theorem `QFORM-N3-PURESTAR-IMPOSSIBLE-v1`

Let `0<tau<1`. Assume all physical diagonals satisfy `|A_ii|<tau`. If, for some coordinate `h`, the complementary principal block `A[h^c,h^c]` is diagonal, then `A` has at most two eigenvalues of absolute value greater than `tau`: at most one above `tau` and at most one below `-tau`.

Consequently no matrix in the QFORM target (`>=3` eigenvalues with `|lambda|>=1`) can have `dr(A[h^c,h^c])=0` in `N3(tau)`.

### Proof

Write

`A=D+S`,                                                       (4.1)

where `D` is the diagonal matrix formed by all physical diagonal entries and

`S=[[0,c^T],[c,0]]`                                            (4.2)

after placing `h` first. Thus `||D||_op<tau`. If `c!=0`, `S` has exactly one positive and one negative eigenvalue; if `c=0`, both counts are zero.

Since `D-tau I` is negative definite,

`n_+(A-tau I)=n_+((D-tau I)+S)<=n_+(S)<=1.`                   (4.3)

Likewise `-D-tau I` is negative definite and

`n_+(-A-tau I)=n_+((-D-tau I)-S)<=n_+(-S)<=1.`                (4.4)

Equations (4.3)-(4.4) say respectively that at most one eigenvalue of `A` exceeds `tau` and at most one is below `-tau`. QED.

Therefore, in the exact `Omega5=0` endpoint of the high-leverage target state, the original complement must have

`boxed: 1<=dr(B)<=4.`                                         (4.5)

A genuine bounded original-coordinate pivot packet is unavoidable. This identifies where the third spectral direction must reside when the high-leverage star itself is nearly one-dimensional.

## 5. Designated partner result used at an exact expression

The newest compatible COMPLETED designated result at the final discovery check is fleet03/B20 r30, `QFORM-DOUBLECOLOOP-THREEPACKET-COMPILER-v1`. Its exact-rank-three branch produces three disjoint ORIGINAL-coordinate packets `B1,B2,B3` and an orthonormal spectral basis with

`sum_(i in B_k) <r_i,e_k>^2 >=453/4096,  k=1,2,3.`            (5.1)

It also gives the robust augmented-core payment `<13309` when the heavy row lies outside its bounded core, and records a valid stress frame showing that packet directional masses alone do not force a cross-packet triple determinant.

The present theorem (2.4) is complementary rather than duplicative: it replaces exact-rank-three directional packet masses by an arbitrary-rank physical-row star packet with the larger fixed physical energy

`639/4096`                                                     (5.2)

in each of three disjoint literal leaf banks. In the intersection with exact rank three, (5.1) and (5.2) may both be retained; one must not identify their spectral packet coordinates with independent random variables. The r30 stress warning is therefore respected: the next receiver must aggregate physical bank energy before reciprocal minor selection.

## 6. Strongest conditional proof graph after this run

The source-pinned compiler now has the following form.

**Full target -> fixed `N3(1/64)` debt.** Already completed in the no-pivot synthesis.

Inside `N3(1/64)`:

* any physical cross block with fifth volume `>=1/1024` is paid by `<23.317` via (1.2);
* if `max_i P_ii>=1/2`, Theorem 2 gives three disjoint original leaf banks each carrying star energy `>=639/4096`;
* for that high-leverage star, positive leaf `Omega5` is paid quantitatively by (3.2), while exact `Omega5=0` reduces after at most eight literal leaf conditionings to `diagonal + rank<=4`;
* the original disjoint-rank-zero / pure-star endpoint is impossible by Theorem 4;
* when the completed low-rank curvature is quantitatively transverse to the star and its Pluecker disjointness is positive, (3.6) gives a direct density bound;
* exact-rank-three subcases retain the designated-partner r30 finite-core / three-packet exits and the earlier physical-pair, grouped-square, mixed-hub and volume receivers.

This leaves two explicit universal debts.

### First unpaid universal implication: `QFORM-N3-LOWLEVERAGE-EXTRASPECTRUM-PAYMENT-v1`

Assume the full original product-source hypotheses, `A in N3(1/64)`, and

`max_i [1_{|A|>=1}]_ii <1/2.`                                 (6.1)

Prove one universal linear small-ball / density estimate, or reduce source-preservingly to a paid physical cross-volume, grouped-square, mixed-hub, ridge or finite-core packet. The projection in (6.1) is deterministic only; no claim of independence in its range is allowed.

### High-leverage remainder: `QFORM-N3-HIGHLEVERAGE-BOUNDEDPIVOT-ALIGNED-PAYMENT-v1`

Assume instead a high-leverage hub and the three physical banks (2.4), while all robust volume exits fail. At the exact zero-disjoint-five-volume endpoint, the complementary leaf block necessarily has `1<=dr(B)<=4`; after conditioning at most eight literal pivot coordinates it is `D+C`, `rank(C)<=4`. Pay the states in which the surviving star is aligned with `range(C)` or the determinant-weighted Pluecker disjointness degenerates, without deleting any small quadratic remainder. A natural next receiver is the completed two-zero-core-hub wedge theorem when the bounded pivot packet exposes a second physical hub: if two literal hubs have zero core and complementary row wedge `Delta>0`, then arbitrary residual curvature is paid by

`||p_Q||_infinity <=2 sqrt(2) Delta^(-1/4).`                  (6.2)

The missing structural step is to force such a quantitative second-hub/wedge or another already-paid bounded-core packet from the `1..4` disjoint pivot state.

## 7. Corrections explicitly preserved

1. No law-uniform pointwise quadratic-phase decay is used. The D5 and Pluecker inputs finish with integrated Fourier envelopes.
2. No unrestricted fiber supremum replaces the conditional average.
3. No independence is inferred after diagonalizing `A`, whitening coefficient frames, or projecting onto the high spectral subspace.
4. No tiny matrix coefficient is discarded as a uniformly tiny random quadratic perturbation on arbitrary unbounded inputs.
5. No sum of squared minors is replaced by a single uniformly good reciprocal minor. The three-bank theorem and `Omega5` routing aggregate before inversion.
6. Full-target continuity is not claimed.

## 8. Status

This is an essential structural advance but not a full proof. It removes the previous exact-rank-three restriction from the high-leverage star compiler and shows that, in arbitrary rank, a high spectral-leverage N3 survivor contains three strong original-coordinate star banks. Combined with the arbitrary-curvature disjoint-five-volume theorem, it forces every exact-zero-volume high-leverage survivor to carry a bounded nonempty physical pivot packet of size at most eight. The genuinely first untouched global N3 branch is now the low-leverage extra-spectrum state (6.1). Full QFORM remains OPEN and still lacks two independent end-to-end reviews.
