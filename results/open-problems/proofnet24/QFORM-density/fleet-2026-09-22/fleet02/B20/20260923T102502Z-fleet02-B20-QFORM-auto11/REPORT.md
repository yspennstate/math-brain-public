# fleet02/B20 — N3 high-leverage star reduction and an exact Hall-route stress family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T102502Z-fleet02-B20-QFORM-auto11`  
Status: `ESSENTIAL_STEP_APPLIED / GLOBAL-N3-FIRST-DEBT / EXACT-RANK3-STAR-ENERGY / HALL-ROUTE-STRESS-FAMILY-PAID / FULL-QFORM-OPEN`  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains OPEN. No moment, Gaussian, log-concave, support, diagonal-basis, or post-rotation-independence hypothesis is added. All probabilistic conditioning below is on ORIGINAL coordinates or on independent ORIGINAL-coordinate banks. Continuity is not claimed beyond cited source scopes.

## 1. Strongest source-pinned end-to-end reduction

The current strongest end-to-end compiler is the no-pivot reduction in

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`,
`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`, Theorem 5.1.

Fix any `tau in (0,1]`. Let `N3(tau,C0)` denote the statement that every real symmetric matrix `A` with

1. `s_3(A)>=1`,
2. `|A_ii|<tau` for every ORIGINAL coordinate `i`, and
3. `|det A[{i,j},{i,j}]|<tau` for every ORIGINAL pair `i!=j`,

has, for every independent cap-one product input, a quadratic-form density bounded by `C0`.

That source proves that `N3(tau,C0)` implies the full QFORM theorem, including arbitrary affine terms, with an explicit universal transfer constant depending only on `(tau,C0)`. Hence the first global unpaid implication may be taken to be `N3(1/64,C0)` for some universal finite `C0`.

The newest completed designated partner at the publication-stage refresh is fleet03/B20 r30,

`yspennstate/math-open-problems@2c0131b6830892a77a8faaf3521388d3a51e7514`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T084738Z-fleet03-B20-QFORM-r30/REPORT.md`.

Its exact-rank-three survivor supplies three disjoint ORIGINAL-coordinate packets carrying three orthogonal spectral-direction masses at least `453/4096`, plus an ORIGINAL physical row of leverage `>1/2`; after its exact partitioned endpoint, every unpaid packet survivor also has a genuinely mixed longitudinal/transverse physical row. Its report explicitly warns that packet directional masses alone do not force a cross-packet third volume.

This run changes mechanism: rather than attempt another single-minor or packet-mixed-discriminant extraction, it quantizes the high-leverage row directly in PHYSICAL star energy and then constructs a target-valid N3 family showing why the Hall-volume shortcut can vanish even in the presence of the partner's high-leverage and mixed-row witnesses.

## 2. Exact high-leverage star-energy identity

### Theorem 2.1 — `QFORM-EXACTR3-HIGHLEVERAGE-STAR-ENERGY-v1`

Let

`A=R M R^T`, `R^T R=I_3`, `M=M^T`, `s_min(M)>=1`.

For an ORIGINAL physical coordinate `h`, write `r=r_h` for the corresponding row of `R`,

`c=||r||^2`, `a=A_hh=r^T M r`.

Then the complete ORIGINAL off-diagonal star at `h` satisfies the exact identity

`sum_(j!=h) A_hj^2 = ||M r||^2-a^2`,

and hence

`boxed(sum_(j!=h) A_hj^2 >= c-a^2).`                          (2.1)

In particular, if `c>1/2` and `|a|<1/64`, then

`boxed(sum_(j!=h) A_hj^2 > 2047/4096).`                       (2.2)

#### Proof

Parseval gives

`sum_(j!=h) r_j r_j^T = I_3-r r^T`.

Therefore

`sum_(j!=h) A_hj^2
 =sum_(j!=h) (r^T M r_j)^2
 =(M r)^T (I-r r^T)(M r)
 =||M r||^2-(r^T M r)^2
 =||M r||^2-a^2.`

Since `s_min(M)>=1`, `||M r||>=||r||=sqrt(c)`, proving (2.1). Equation (2.2) follows from `c>1/2`, `a^2<1/4096`. QED.

This identity uses only deterministic spectral bookkeeping. It does NOT rotate the random input law and does NOT infer independence of spectral coordinates.

## 3. A robust-edge exit is already paid

Assume the target scale `s_3(A)>=1`, and suppose `|A_hh|,|A_jj|<1/64` but

`|A_hj|>=1/16`.

For the ORIGINAL physical pair

`B=[[A_hh,A_hj],[A_hj,A_jj]]`

we have

`det B=A_hh A_jj-A_hj^2 <0`,

`|det B|>1/256-1/4096=15/4096`,                               (3.1)

and, since the eigenvalues of a symmetric `2x2` matrix are centered at `(A_hh+A_jj)/2`,

`sigma_min(B) >= |A_hj|-(|A_hh|+|A_jj|)/2 >3/64`.             (3.2)

The arbitrary-rank physical-pair theorem at

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

therefore gives

`||p_Q||_infinity
 <=3*400^(1/3)*(|det B|^2 sigma_min(B) s_3(A))^(-1/6)
 <239.`                                                        (3.3)

Thus after the already-paid physical-pair exit, every high-leverage exact-rank-three N3 survivor with `|A_hh|<1/64` may be assumed to satisfy

`|A_hj|<1/16` for every `j!=h`.                                (3.4)

Combining (2.2) and (3.4), the star has at least 128 nonzero physical leaves. More usefully, greedy accumulation gives three disjoint ORIGINAL-coordinate leaf banks `J1,J2,J3` such that

`boxed(sum_(j in Jk) A_hj^2 >=1/8, k=1,2,3).`                 (3.5)

Indeed each squared edge is `<1/256`. Accumulate `J1` until its energy first reaches `1/8`; its total is `<33/256`. Do the same for `J2`. The remaining energy exceeds

`2047/4096-2*(33/256)=991/4096>1/8`.

So the exact-rank-three high-leverage part of N3 is reduced, after a `<239` pair exit, to a genuinely diffuse three-bank ORIGINAL star. This is a product-preserving structural replacement for the failed local-minor strategy.

## 4. A target-valid stress family inside N3(1/64)

The natural next shortcut would be to combine the partner's three packets, high-leverage row and mixed-row witness and demand a fixed positive cross-packet third-volume. The following exact family shows that this is false even while all scalar and pair pivots lie in the no-pivot class.

Let `(e1,e2,e3)` be orthonormal and define

`u=(e1+e2)/sqrt(2)`, `v=(e1-e2)/sqrt(2)`,
`w=(v+e3)/sqrt(2)`, `z=(v-e3)/sqrt(2)`.

Then `(u,w,z)` is orthonormal. In this basis let

`M=[[1,0,0],[0,0,1],[0,1,0]]`.                                (4.1)

Thus `M` has eigenvalues `{1,1,-1}` and `s_min(M)=1`.

Fix

`c=127/128`, `N>=33`, `L>=32`,
`alpha=sqrt((1-c)/(2L))`, `beta=1/sqrt(2L)`.

Define the rows of `R` by three ORIGINAL-coordinate packets:

- `B1`: `N` copies of `u/sqrt(2N)`;
- `B2`: `N` copies of `u/sqrt(2N)`;
- `B3`: one row `h=sqrt(c) w`, and for `k=1,...,L` two rows
  `p_k=alpha w+beta z`, `q_k=alpha w-beta z`.

Then

`sum_(i in B1) r_i r_i^T=(1/2) u u^T`,
`sum_(i in B2) r_i r_i^T=(1/2) u u^T`,

while

`h h^T+sum_k(p_k p_k^T+q_k q_k^T)
 =c w w^T+(1-c)w w^T+z z^T
 =w w^T+z z^T`.

Hence

`boxed(R^T R=I_3).`                                            (4.2)

Therefore `A=R M R^T` is a target-valid exact-rank-three matrix with nonzero spectrum exactly `{1,1,-1}`.

### 4.1 It has the partner packet masses and a near-coloop

The packet directional masses in the basis `(e1,e2,e3)` are

`sum_(B1)<r_i,e1>^2=1/4`,
`sum_(B2)<r_i,e2>^2=1/4`,
`sum_(B3)<r_i,e3>^2=1`.                                       (4.3)

All exceed the partner threshold `453/4096` and also the later strengthened `1953/16384` threshold.

The singleton core `{h}` has Gram eigenvalues `{c,0,0}` with

`c=127/128>63/64`,                                              (4.4)

so it also realizes the current small-core near-coloop geometry. The row `h` has leverage `c>1/2`.

Relative to the high-leverage direction `w`, every `p_k,q_k` is genuinely mixed: both its longitudinal `w` component and transverse `z` component are nonzero.

### 4.2 Yet the cross-packet mixed third-volume is exactly zero

Define

`V_123=sum_(i in B1,j in B2,k in B3) det(r_i,r_j,r_k)^2`.

Every row of `B1` and every row of `B2` is parallel to `u`, so

`boxed(V_123=0).`                                               (4.5)

Thus even the conjunction

- three fixed packet directional masses,
- a `>1/2` leverage row,
- a `>63/64` one-row near-coloop core,
- and genuinely mixed residual rows

still does NOT force any positive cross-packet third-volume. Any quantitative Hall/mixed-discriminant closure must therefore use more than those invariants, or it must explicitly handle the aligned-packet endpoint rather than claiming it disappears.

### 4.3 The whole family lies in `N3(1/64)`

The ORIGINAL physical diagonal entries are:

- on `B1,B2`: `1/(2N)<1/64`;
- at `h`: `0`;
- at `p_k,q_k`: `+/- 2 alpha beta = +/- sqrt(1-c)/L`, whose magnitude is `<1/64` for `L>=32`.

For physical pair determinants:

- two `u`-rows give determinant zero;
- a `u`-row and a plane row have zero off-diagonal entry, hence determinant magnitude `<1/4096`;
- `(h,p_k)` and `(h,q_k)` have determinant magnitude
  `c beta^2=c/(2L)<=127/8192<1/64`;
- two same-sign `p` rows, or two same-sign `q` rows, give determinant zero;
- a `p` row and a `q` row have zero mutual bilinear entry and determinant magnitude
  `(2 alpha beta)^2=(1-c)/L^2<1/64`.

Hence

`boxed(|A_ii|<1/64 and |det A[{i,j},{i,j}]|<1/64 for every i!=j).` (4.6)

This is a genuine family inside the global first-debt class `N3(1/64)`.

Its high-leverage star is nevertheless macroscopic and diffuse:

`sum_(j!=h) A_hj^2=c=127/128`,                                 (4.7)

while each individual `h`-leaf determinant tends to zero as `L` grows.

## 5. The stress family is paid: grouped square plus rank-two half-Riesz

The family above is NOT a counterexample to QFORM. It is uniformly controlled by a source-valid grouped mechanism that retains ORIGINAL-bank independence.

Let

`U=(1/sqrt(2N)) [sum_(i in B1) X_i+sum_(i in B2) X_i]`.

On `B3` put

`W=sqrt(c) X_h+alpha sum_k(P_k+Q_k)`,
`Z=beta sum_k(P_k-Q_k)`.

Because `(u,w,z)` is the deterministic spectral basis and `M` is (4.1),

`boxed(Q=U^2+2WZ).`                                             (5.1)

The bank `B1 union B2` is disjoint from `B3`, so `U` is genuinely independent of `(W,Z)`.

The coefficient vector of `U` has Euclidean norm one. By the Rogozin--Ball one-dimensional projection bound (also used in the pinned Claude/Fourier source),

`||p_U||_infinity<=sqrt(2)`.                                   (5.2)

The coefficient vectors defining `W` and `Z` on the ORIGINAL `B3` variables are orthonormal:

`c+2L alpha^2=1`, `2L beta^2=1`, and their inner product is zero. Therefore the orientation-free rank-two affine half-Riesz theorem

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

applies to `H=2WZ`, with

`Lambda=[[0,1],[1,0]]`, `|det Lambda|=1`,

and gives

`sup_t E|H-t|^(-1/2)<=128`.                                    (5.3)

From (5.2), the square `U^2` has density kernel bounded by

`p_(U^2)(s)<=sqrt(2) s^(-1/2) 1_(s>0)`.

Using the genuine independence in (5.1),

`p_Q(t)
 <=sqrt(2) E[|t-H|^(-1/2)]
 <=128 sqrt(2)<181.020.`                                       (5.4)

Thus this no-pivot/Hall-degenerate family is uniformly PAID. The correct currency is an aggregated independent square bank plus a rank-two fractional estimate, not a fixed physical minor or cross-packet third-volume.

## 6. Required pinned newest-source application

The pinned Claude/Fourier report at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

proves the unrestricted fifth-volume estimate

`||p_Q||_infinity<=5 sqrt(2e) E_5(T^T T)^(-1/10)`

for any ORIGINAL-coordinate cross block `T`, with no volume-marginal condition. Therefore every global no-pivot state with some physical cross block satisfying

`E_5(T^T T)>=1/1024`

is already paid by

`boxed(||p_Q||_infinity<=10 sqrt(2e)<23.317).`                 (6.1)

The stress family in Section 4 has rank exactly three, hence every cross block has rank at most three and its fifth volume is zero. It therefore genuinely probes the complementary low-volume geometry rather than falling into the D5 exit.

## 7. What changed in the proof graph

The strongest end-to-end reduction remains: prove `N3(1/64,C0)` and the cited Gaussian-padding/no-pivot compiler supplies the full theorem. This run proves two new source-valid facts inside that first global debt:

1. In the exact-rank-three high-leverage branch, a small physical pivot forces a fixed star resource `>2047/4096`; after the existing robust physical-pair exit, this resource can be split into three independent ORIGINAL leaf banks each carrying star energy at least `1/8`.
2. The previous packet-Hall idea cannot close by demanding cross-packet third-volume: an explicit target-valid `N3(1/64)` family has all partner packet/near-coloop/mixed-row witnesses while its cross-packet third-volume is exactly zero. The same family is nevertheless uniformly paid by grouped-square plus rank-two half-Riesz, with cap `<181.020`.

Accordingly the first unpaid exact-rank-three sub-implication is sharpened to

`QFORM-N3-DIFFUSE-THREEBANK-STAR-PAYMENT-v1`:

> Under the full ORIGINAL product-source hypotheses, assume exact rank three `A=RMR^T`, `R^TR=I3`, `s_min(M)>=1`, all `|A_ii|<1/64`, all useful robust physical-pair exits fail, and an ORIGINAL row has leverage `>1/2`. Then the row has three disjoint ORIGINAL leaf banks `J1,J2,J3` with `sum_(j in Jk)A_hj^2>=1/8`. Prove one universal linear small-ball/density bound for this diffuse three-bank star with arbitrary residual same-side curvature, or reduce it source-preservingly to the grouped-square/rank-two, mixed-hub, ridge/volume, or physical-pair classes.

This is strictly stronger and more physical than asking for a good local second singular direction or a positive cross-packet mixed discriminant. It also matches the source corrections: aggregation must occur before reciprocal-minor inversion.

The arbitrary-extra-spectrum part of `N3(1/64)` remains separately unpaid. Therefore full QFORM is OPEN, and no global continuity statement is made.

## 8. Scope and corrections retained

- No uniform pointwise quadratic-phase decay is used.
- No worst spectral-fiber supremum is used.
- No conditional projected-density cap is asserted.
- No rotated spectral coordinate is declared independent.
- Small matrix norm is never treated as a uniformly small random quadratic perturbation.
- Packet/source independence is invoked only for disjoint ORIGINAL coordinate sets.

These preserve the live `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, and `QFORM-NO-INDEPENDENCE-AFTER-ROTATION` corrections.
