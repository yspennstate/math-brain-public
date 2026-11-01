SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-24T07:20:33Z.
attacking: aggregate many disjoint rank-two cross minors before inversion, then transfer the aggregate currency through an exact scalar Schur pivot to reduce tiny-pivot loss.

# fleet01/B01 — disjoint-tetrad aggregation and pivot-compensated overlap-minor compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T072033Z-fleet01-B01-qform-auto11-r15`  
Role: Oscillatory replacement  
Status: **NEW AGGREGATE HALF-RIESZ / PIVOT-COMPENSATED L-INFINITY COMPILER / EXACT ZERO-CURRENCY CLASSIFICATION / FULL QFORM OPEN**

## 1. Scope and corrections retained

All random coordinates below are literal ORIGINAL independent coordinates with probability densities bounded by one. No Gaussian, iid, moment, compact-support, connected-support, log-concavity, or post-rotation independence assumption is made. The phase-aligned fragmented-support counterexample remains valid: no law-uniform positive power decay for a scalar quadratic characteristic function is asserted or used.

The full owner target remains OPEN. The new density conclusion below is essential boundedness; continuity is not asserted for arbitrary merely measurable input densities. There are not two independent end-to-end reviews of the full conjecture.


Two pinned mathematical inputs are used explicitly:

1. `QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1`, fleet02/B06, canonical report  
   `yspennstate/math-open-problems@c2ce876df8b5483a00802170001d4144bb4cdbfa:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260923T192839Z-auto11/REPORT.md`.  
   If a quadratic polynomial in the original product coordinates has a literal cross block `M=A[I,J]` with
   `Z=e_2(M^T M)>0`, then, retaining all same-bank curvature, other cross directions and affine terms,

   `H_(1/2)(Q):=sup_s E|Q-s|^(-1/2) <= 8 e^(1/4) Z^(-1/8)`.       (1.1)

2. The source-valid scalar-square peel, in the previous B01 synthesis  
   `yspennstate/math-open-problems@0bbbd2e99a4d26b7a4380a9827d92596daeaf2a6:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T200355Z-fleet01-B01-qform-auto11/E2_SQUARE_SYNTHESIS.md`: if exact completion of one literal original coordinate gives

   `Q=a(X_0+h(Y))^2+R(Y)`, `a!=0`,                                (1.2)

   then

   `||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R)`.                  (1.3)

Related prior work, not duplicated here: fleet03/B11 r24 aggregates disjoint `2x2` minors of a **defect matrix** `F=uu^T-A` to obtain a STAR/CROSS structural dichotomy. The theorem below instead aggregates the actual Schur residual and identifies its currency exactly with overlap-one physical `3x3` minors of the original matrix; it then spends that currency in a density estimate.

## 2. Aggregate disjoint-tetrad half-Riesz theorem

For a real symmetric `m x m` matrix `B`, define the ordered disjoint-tetrad energy

`W_2^dis(B)
 := sum_{I,J subset [m], |I|=|J|=2, I cap J=emptyset} det B[I,J]^2`. (2.1)

The sum is ordered in `(I,J)`; symmetry therefore counts the reverse orientation separately.

### Theorem 2.1 — `QFORM-DISJOINT-TETRAD-AGGREGATE-HALFRIESZ-v1`

Let

`R=X^T B X + ell^T X + c`                                         (2.2)

for arbitrary independent cap-one original coordinates. If `W=W_2^dis(B)>0`, then

`boxed: H_(1/2)(R) <= 8 sqrt(2) e^(1/4) W^(-1/8).`                (2.3)

The numerical coefficient is

`8 sqrt(2)e^(1/4)=14.52708926969255...`.                           (2.4)

### Proof

Independently color every physical coordinate `P` or `Q` with probability `1/2`. Put `M=B[P,Q]`. By Cauchy--Binet,

`e_2(M^T M)=sum_{I subset P, J subset Q, |I|=|J|=2} det B[I,J]^2`. (2.5)

For every fixed ordered disjoint pair `(I,J)` in (2.1), the event `I subset P, J subset Q` has probability `2^(-4)=1/16`. Therefore the exact expectation identity is

`E e_2(B[P,Q]^T B[P,Q]) = W/16`.                                  (2.6)

Hence some deterministic original-coordinate cut satisfies

`Z:=e_2(B[P,Q]^T B[P,Q]) >= W/16`.                                (2.7)

Apply the row-gate-free E2 theorem (1.1) to that cut:

`H_(1/2)(R)
 <=8e^(1/4) Z^(-1/8)
 <=8e^(1/4)(W/16)^(-1/8)
 =8sqrt(2)e^(1/4)W^(-1/8)`.                                       (2.8)

No random variable is rotated. The random coloring is only a deterministic-existence argument for a physical cut. QED.

This is the desired aggregate-before-inversion replacement: no individual `2x2` minor is inverted, and many weak disjoint minors contribute quadratically before the `-1/8` power is taken.

## 3. Exact Schur transfer from overlap-one physical 3x3 minors

Let `A` be real symmetric and fix a literal coordinate `k` with

`a=A_kk !=0`.                                                       (3.1)

Write the exact Schur complement after completing `X_k` as

`S=A_(hat k,hat k)-A_(hat k,k) A_(k,hat k)/a`.                     (3.2)

Define the overlap-one `3x3` determinant energy rooted at `k` by

`T_k(A)
 := sum_{I,J subset [n]\{k}, |I|=|J|=2, I cap J=emptyset}
       det A[{k} union I,{k} union J]^2`.                           (3.3)

The row and column triples intersect **exactly** in the pivot `k`.

For every term, block determinant/Schur complement gives the exact identity

`det A[{k} union I,{k} union J] = a det S[I,J]`.                   (3.4)

Consequently

`boxed: T_k(A)=a^2 W_2^dis(S).`                                    (3.5)

### Theorem 3.1 — `QFORM-PIVOT-OVERLAP3-AGGREGATE-LINF-v1`

If `T_k(A)>0`, then for every admissible product law

`boxed:
 ||p_(X^T A X)||_infinity
 <= 8 sqrt(2)e^(1/4) |a|^(-1/4) T_k(A)^(-1/8)`                    (3.6)

or, equivalently,

`boxed:
 ||p_(X^T A X)||_infinity
 <= 8 sqrt(2)e^(1/4) [a^2 T_k(A)]^(-1/8).`                        (3.7)

Proof. Complete the literal coordinate `k`. Equation (1.3) gives the square peel, Theorem 2.1 gives

`H_(1/2)(R)<=8sqrt(2)e^(1/4)W_2^dis(S)^(-1/8)`,                   (3.8)

and (3.5) yields (3.6)-(3.7). QED.

The scaling is exact: under `A -> lambda A`, `a^2 T_k -> lambda^8(a^2 T_k)`, so the right side scales as `|lambda|^-1`, exactly like an output density.

The important change from a one-pivot estimate is the power of the physical pivot. A naive square peel costs `|a|^-1/2`; the overlap-minor currency contains the compensating Schur inflation and leaves only `|a|^-1/4`, or more invariantly the single aggregate currency `a^2 T_k`.

## 4. Exact zero-currency classification

The failure `W_2^dis(B)=0` is not an unstructured event.

Let `G_B` be the graph whose vertices are physical coordinates and whose edges are the nonzero off-diagonal coefficients `B_ij`.

### Theorem 4.1 — `QFORM-DISJOINT-TETRAD-ZERO-CLASSIFICATION-v1`

If `W_2^dis(B)=0`, then at least one of the following holds:

1. `B=D+sigma uu^T` for a diagonal `D`, a real vector `u`, and `sigma in {+1,-1}`; or
2. all nonzero off-diagonal entries of `B` are supported on one physical star; or
3. all nonzero off-diagonal entries are supported on one physical triangle.

The last two cases include smaller supports (one edge, two adjacent edges, etc.).

### Proof

`W_2^dis(B)=0` means every disjoint tetrad vanishes:

`B_ik B_jl = B_il B_jk`                                             (4.1)

whenever `i,j,k,l` are distinct.

If the support graph has no two vertex-disjoint edges, its edge family is pairwise intersecting. Pick two adjacent edges `ab,ac` if possible. Any edge not containing `a` must meet both and is therefore `bc`; any further edge meeting `ab,ac,bc` lies in that triangle. Thus the support is a star or a triangle.

Assume instead that `ab` and `cd` are disjoint nonzero edges. Applying (4.1) to row/column pairings `(a,c)|(b,d)` and `(a,d)|(b,c)` shows that all six edges among `{a,b,c,d}` are nonzero. If a further nonisolated vertex `v` has an edge to the core, (4.1) with a disjoint core edge forces `v` to every core vertex. If `v` initially has only an edge to another outside vertex, applying (4.1) against a core edge first forces a core connection. Finally two nonisolated outside vertices are forced adjacent by (4.1) using two core anchors. Hence the nonisolated support is complete.

Choose three nonisolated anchors `1,2,3` and put

`sigma = sign(B_12 B_13 B_23)`.                                    (4.2)

Define

`u_1=sqrt(|B_12 B_13/B_23|)`,
`u_i=B_1i/(sigma u_1)` for every other nonisolated `i`,             (4.3)

and set `u_i=0` on isolated vertices. Tetrad identity (4.1), first with anchors and then with an arbitrary pair `i,j`, gives

`B_ij = sigma u_i u_j` for every `i!=j`.                            (4.4)

Absorb the diagonal discrepancy `B_ii-sigma u_i^2` into a diagonal matrix `D`. This proves alternative 1. QED.

Therefore `T_k(A)=0` has a concrete meaning after a nonzero pivot: the Schur residual is either diagonal plus signed rank one, or its off-diagonal support is a star/triangle. The aggregate branch and its exact failure are both structurally explicit.

## 5. Diffuse strict-target stress: all local currencies may be tiny while the aggregate stays fixed

Let `m` be even. Choose `m x 2` orthonormal matrices `R,S` whose row norms are at most `sqrt(2/m)` (for example the normalized constant and balanced-sign columns). For `0<epsilon<=1`, define on one scalar coordinate plus two disjoint `m`-coordinate banks

`A_(epsilon,m)
 = [ epsilon      0          0
       0          0     epsilon^(-1) R S^T
       0    epsilon^(-1) S R^T      0 ].`                           (5.1)

Its spectrum is

`{epsilon, +epsilon^(-1),+epsilon^(-1),-epsilon^(-1),-epsilon^(-1),0,...,0}`, (5.2)

so it is a strict owner-target family. Every physical cross entry is at most `2/(epsilon m)`, and every `2x2` minor of `epsilon^(-1)RS^T` is at most `4/(epsilon^2 m^2)`. Thus every rooted overlap-one `3x3` determinant at the scalar pivot is at most

`4/(epsilon m^2)`,                                                   (5.3)

which tends to zero with `m`.

Nevertheless the residual bipartite block has two-volume at least twice the two natural orientations:

`W_2^dis(Schur) >= 2 e_2((epsilon^(-1)RS^T)^T(epsilon^(-1)RS^T))
                     =2 epsilon^(-4)`.                              (5.4)

Hence

`T_0(A)>=2 epsilon^(-2)`,
`epsilon^2 T_0(A)>=2`.                                               (5.5)

Theorem 3.1 therefore gives the scale-free bound

`boxed: ||p_Q||_infinity
 <=8sqrt(2)e^(1/4) 2^(-1/8)
 =13.3213995963033...`                                              (5.6)

uniformly in `epsilon,m` and in every admissible product law. This is exactly the regime where selecting and inverting one physical edge/minor is the wrong mechanism.

For the five-dimensional special case `m=2`, `R=S=I_2`, the exact currency is `epsilon^2 T_0=4`, giving the sharper numerical value `12.2157772909552...`.

## 6. Designated partner fleet02/B01 applied at an actual inequality

The newest completed designated-partner result read in this run is fleet02/B01 r46,

`yspennstate/math-open-problems@fb7b0f71ead32ea608ff9ec45370edc246f7239e:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260924T063552Z-fleet02-B01-qform-auto11-r46/REPORT.md`,

theorem `QFORM-RANK1-TWOHUB-ARROWHEAD-HALFRIESZ-v1`.

Apply it to the strict target

`Q_* = X_0^2 + 2 (w dot H)(c dot Y)`,
`w=c=2^(-1/2)(1,1)`.                                                 (6.1)

The coefficient matrix has spectrum `{1,1,-1,0,0}`. Here `s=||w|| ||c||=1` and both leaf leverages equal `1/2`, so the partner's spread-leaf inequality gives

`boxed: ||p_(Q_*)||_infinity <=2^(13/4)=9.513656920021768...`.      (6.2)

This is an actual equation-level use of the completed partner theorem.

The new disjoint-tetrad compiler also sees this form from a different cut. Its four-variable residual has

`W_2^dis= (||w||^4-sum_i w_i^4)(||c||^4-sum_j c_j^4)=1/4`,         (6.3)

so Theorem 3.1 gives the valid but weaker

`||p_(Q_*)||_infinity <=17.2757179197981...`.                       (6.4)

Equation (6.3) is the general exact identity for a symmetric rank-one bipartite packet `[0,wc^T;cw^T,0]`. It shows the complementarity: the partner theorem only needs dispersion on the leaf side after reducing the hub side to a scalar aggregate; the tetrad theorem pays simultaneous physical dispersion on both sides without choosing a privileged hub.

## 7. What this does and does not close

**Closed in this run:**

- aggregate disjoint `2x2` cross minors now give a direct half-Riesz estimate for the whole quadratic polynomial;
- after one literal nonzero scalar pivot, the corresponding overlap-one physical `3x3` determinants give an L-infinity density bound with exact pivot compensation;
- exact vanishing of the aggregate disjoint-tetrad currency is classified as diagonal+signed-rank-one or star/triangle off-diagonal support.

**Not closed:** the bare spectral hypothesis `s_3(A)>=1` has not yet been shown to force a target-scale lower bound on

`Gamma(A):=max_{k:A_kk!=0} A_kk^2 T_k(A)`                          (7.1)

or to force one of the already-paid low-complexity zero-currency branches with a scale-free receiver when every usable physical pivot is tiny or zero. The exact QFORM conjecture is therefore still OPEN.

The next implication is

`QFORM-OVERLAP3-AGGREGATE-OR-LOWCOMPLEXITY-TINY-PIVOT-ROUTING-v1`:

> Under `s_3(A)>=1`, quantitatively route the case `Gamma(A)<<1`. Either recover a target-scale star/triangle/diagonal+rank-two receiver, or prove a different aggregate currency before taking reciprocal pivot powers. A nonzero low-rank collar must be retained; it may not be discarded as a small random quadratic perturbation.

The phase-aligned scalar counterexample is preserved throughout: every Fourier estimate spent here is the already-proved **joint E2** averaged-frequency estimate, never scalar pointwise quadratic van der Corput.
