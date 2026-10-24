SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T11:14:45Z.
attacking: the strict-N3 high-star two-channel residue; choose the partner's star partition simultaneously with quantitative leaf cross energy, then spend diffuse fifth-volume before any local-minor extraction.

# account01/B19 r31 — balanced STAR leaf-cross compiler and D5 diffuse exit

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Fresh owner control:** brain `dd316d19fde1d24308143bcc59abd7be9d5ebac6`, revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED`; full QFORM remains OPEN; continuity is tracked separately and is not asserted here.

## 1. Exact sources consumed

The designated partner result is account02/B19 r32, read at

`yspennstate/math-open-problems@4d1f394498f795b72de7694748aab2b3bd3030f1`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T103645Z-account02-B19-QFORM-r32/REPORT.md`.

Its strict-N3 STAR hypotheses are

`tau0 = 1/256`,

`|A_ii| < tau0` for every original coordinate,

`|A_ii A_jj - A_ij^2| < tau0` for every physical pair,

and for one physical hub row `h`,

`S_h := sum_(j != h) A_hj^2 > S0 := 123/4096`.                    (1.1)

It proves that the leaf block `B=A[h^c,h^c]` has at least one eigenvalue of modulus at least one and that one can split the leaves into two original-coordinate banks with star energies at least

`beta0 = 1711/131072`.                                              (1.2)

The completed unrestricted fifth-volume theorem is source-pinned at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

and summarized in `RESULTS.md`. For every genuine physical cross block `N=A[I,J]` between disjoint original-coordinate banks,

`||p_(X^T A X)||_infinity <= 5 sqrt(2e) e_5(N^T N)^(-1/10)`.       (1.3)

There is no marginal condition in this D5 theorem; self blocks, outside couplings, affine shifts, signs and extra spectrum are arbitrary.

For the global proof graph I also use account02/B19 r22, which source-pins the owner synthesis reduction of the full target to `N3(tau)` after the already-paid scalar/pair exits. No claim below upgrades an incomplete N3 route to a full proof.

## 2. New simultaneous partition theorem

Put

`w_i=A_hi^2`, `i != h`,

`M0=tau0+tau0^2=257/65536`.                                         (2.1)

The strict physical-pair determinant hypothesis gives

`w_i <= |A_hh A_ii| + |A_hh A_ii-A_hi^2| < M0`.                    (2.2)

Let `D=diag(B)` and `O=B-D`. Since the partner proves that `B` has an eigenvalue of modulus at least one while `||D||_op<tau0`,

`||O||_op > 1-tau0 = 255/256`,                                     (2.3)

hence

`||O||_F^2 > (255/256)^2`.                                         (2.4)

### Theorem 2.1 — `QFORM-N3-STAR-BALANCED-LEAFCROSS-COMPILER-v1`

Under (1.1) and the strict-N3 hypotheses, there is a partition of the complete leaf set into disjoint ORIGINAL-coordinate banks

`h^c = J disjoint_union K`                                         (2.5)

such that simultaneously

`sum_(j in J) A_hj^2 > beta0`,

`sum_(k in K) A_hk^2 > beta0`,                                     (2.6)

and

`||B[J,K]||_F^2 > c0 := (255/256)^2/4
                        =65025/262144
                        =0.248050689697265625`.                     (2.7)

Thus the partner's two independent star channels can be chosen without sacrificing a universal amount of genuine leaf cross energy.

### Proof

Order the star weights decreasingly,

`w_1 >= w_2 >= ... >= w_m >=0`,

and append one dummy zero if `m` is odd. Pair consecutive weights

`(w_1,w_2),(w_3,w_4),...`.                                         (2.8)

For each pair, put one coordinate in `J` and the other in `K`. Orient the pairs independently and uniformly for the moment.

For **every** orientation,

`|sum_J w_i - sum_K w_i|
 <= sum_r (w_(2r-1)-w_(2r))
 <= w_1
 < M0`.                                                            (2.9)

The last inequality is the alternating-series identity

`w_1-w_2+w_3-w_4+... <= w_1`

for a nonincreasing nonnegative sequence. Therefore every orientation satisfies

`min(sum_J w_i,sum_K w_i)
 > (S0-M0)/2
 =1711/131072
 =beta0`,                                                           (2.10)

which proves (2.6).

Now consider the undirected leaf edge energy

`E_leaf=sum_(i<j, i,j !=h) B_ij^2 = ||O||_F^2/2`.                  (2.11)

An edge whose endpoints form one of the pairs in (2.8) is always cut. An edge joining two different pairs is cut with probability exactly `1/2`, because the two pair orientations are independent. Hence

`E ||B[J,K]||_F^2 >= (1/2) E_leaf = ||O||_F^2/4
                  > (255/256)^2/4=c0`.                             (2.12)

Some orientation therefore has the cross-energy bound (2.7), and every orientation already has (2.6). QED.

No spectral rotation has been declared independent. The partition acts only on original coordinates.

## 3. A fifth-volume lemma from effective-rank failure

For a matrix `N`, write its singular values `s_1>=s_2>=...>=0`, set

`x_i=s_i^2`,

`E1=sum_i x_i=||N||_F^2`,

and `E5=e_5(N^T N)=e_5(x_1,x_2,...)`.

### Lemma 3.1 — elementary-symmetric diffuse-mass lower bound

For every `eta in (0,1)`, if

`sum_(i=1)^4 x_i <= (1-eta) E1`,                                   (3.1)

then

`E5 >= eta^4 E1^5 / 120`.                                         (3.2)

### Proof

Assume `E1>0` and set `p_i=x_i/E1`. Let `I_1,...,I_5` be iid draws from the probability vector `(p_i)`. Then

`P(I_1,...,I_5 all distinct)=5! e_5(p)`.                           (3.3)

Condition on the event that the first `r<=4` draws are distinct. Their total probability mass is at most the sum of the four largest `p_i`, which by (3.1) is at most `1-eta`. Therefore the next draw is new with conditional probability at least `eta`. Multiplying the four conditional lower bounds after the first draw gives

`5! e_5(p) >= eta^4`.                                              (3.4)

Since `e_5(x)=E1^5 e_5(p)`, (3.2) follows. QED.

This elementary lemma is useful here because D5 pays fifth volume directly; no individual `5x5` minor needs to be selected.

## 4. Actual D5 payment of the partner STAR branch

Apply Theorem 2.1 and put

`N=B[J,K]=A[J,K]`.                                                  (4.1)

This is an actual physical cross block of the original matrix, with

`E1=||N||_F^2 > c0`.                                               (4.2)

Fix any `eta in (0,1)`. There is now an exhaustive alternative.

### Diffuse-cross alternative

If

`sum_(i=1)^4 s_i(N)^2 <= (1-eta)||N||_F^2`,                       (4.3)

then Lemma 3.1 gives

`e_5(N^T N)
 >= eta^4 c0^5/120`.                                               (4.4)

Putting this into the completed unrestricted D5 theorem (1.3),

`boxed:
 ||p_(X^T A X)||_infinity
 <= 5 sqrt(2e) [120/(eta^4 c0^5)]^(1/10)
 = 5 sqrt(2e) 120^(1/10) eta^(-2/5) c0^(-1/2).`                   (4.5)

This is a full target-level `L^infinity` estimate on the diffuse-cross STAR alternative. It retains all self curvature, all outside couplings, all signs, all degeneracies outside the paid volume, arbitrary additional spectrum, and arbitrary independent one-dimensional laws with density cap one.

### Concentrated-cross alternative

If (4.3) fails, then

`boxed:
 sum_(i=1)^4 s_i(N)^2 > (1-eta)||N||_F^2
                      > (1-eta)c0.`                               (4.6)

Thus the unpaid STAR state is forced into a quantitatively low-effective-cross-rank chamber; this is an aggregate singular-subspace statement, not a local minor selector.

### Fixed useful numerical choice

Take

`eta=1/64`.                                                        (4.7)

Then the diffuse alternative gives

`e_5(N^T N)
 > 4.66445655725171848979e-13`,                                   (4.8)

and therefore

`boxed: ||p_(X^T A X)||_infinity < 199.413.`                       (4.9)

If this exit fails, the same simultaneously star-balanced physical cut satisfies

`boxed:
 sum_(i=1)^4 s_i(N)^2 > (63/64)||N||_F^2
                      >0.244174897670745849609375.`                (4.10)

Equivalently, less than `1/64` of this cut's Frobenius energy lies beyond its first four singular directions.

This does **not** authorize deleting that tail: bounded matrix norm/Frobenius norm is not a law-uniform random perturbation for unbounded product inputs. The statement is only a structural localization for the next exact argument.

## 5. Additional exact consequences of the same cut

The strict pair condition also gives for every leaf cross entry

`B_jk^2 < M0=257/65536`.                                           (5.1)

Together with (2.7),

`||B[J,K]||_F^2/M0 >65025/1028 =63.253891...`.                     (5.2)

Hence at least 64 physical cross entries of this chosen cut are nonzero. This is only a support-size fact; it does not by itself produce a constant local edge, row, minor, or determinant, and I do not use it as such.

## 6. Compact conditional proof assembly

The source-pinned owner synthesis used in account02/B19 r22 reduces the full theorem to one fixed strict no-pivot class `N3(tau)` after paid scalar and physical-pair branches. The current rank-three/rank-two-cross compiler then divides the difficult geometry into paid exits plus STAR and TRIANGLE residues. Account03/B19 pays TRIANGLE down to a two-gradient packet but still lacks the third-source `L^infinity` coupling. Account02/B19 r32 pays STAR structurally down to two independent original-coordinate star channels plus a leaf spectral source.

This run replaces the qualitative STAR leaf source by the stronger simultaneous packet

`two star channels >= beta0`

**and**

`one genuine leaf cut with ||B[J,K]||_F^2 > c0`.                  (6.1)

On that exact packet, every diffuse fifth-volume configuration satisfying (4.3) is now completely paid by (4.5). At `eta=1/64`, every still-unpaid STAR state can therefore be assumed to have a chosen physical leaf cut carrying more than `63/64` of its cross Frobenius energy in four singular directions while preserving both star channels.

Accordingly the first essential STAR inequality is sharpened to

`QFORM-STAR-FOURDIR-TAIL-COUPLED-LINFINITY-v1`:

> In the strict-N3 high-star state, with the original-coordinate partition supplied by Theorem 2.1, prove a universal density bound when `sum_{r<=4}s_r(B[J,K])^2 > (63/64)||B[J,K]||_F^2`, both star banks have energy at least `beta0`, and the full matrix still has three eigenvalues of modulus at least one. The proof must retain the cross tail exactly (or route it to another paid branch), and must preserve original-product provenance.

The parallel TRIANGLE third-source coupling and the arbitrary-extra-spectrum/global N3 descent remain separate debts. Therefore the unrestricted theorem is not marked proved.

## 7. Corrections and degeneracies audit

1. No post-rotation independence is used; all cuts are original-coordinate cuts.
2. No arbitrary-joint coarea estimate is used.
3. No small coefficient, small tail, or small matrix perturbation is dropped.
4. No local cross minor is inferred from aggregate cross energy.
5. D5 is applied to the actual full quadratic form through the genuine physical block `A[J,K]`; arbitrary self blocks and outside couplings stay present.
6. All signs of `A` and `B` are allowed. The argument uses singular values and squares only.
7. Repeated eigenvalues, singular leaf cross blocks, and rank `<=4` cross blocks are included in the concentrated alternative.
8. The result establishes essential boundedness only on the diffuse alternative. It does not independently prove continuity there; global continuity remains OPEN.

## 8. Numerical values checked

`tau0 = 1/256 = 0.00390625`

`M0 = tau0+tau0^2 =257/65536 =0.0039215087890625`

`S0 =123/4096 =0.030029296875`

`beta0=(S0-M0)/2=1711/131072=0.01305389404296875`

`c0=(1-tau0)^2/4=65025/262144=0.248050689697265625`

For `eta=1/64`,

`delta5=eta^4 c0^5/120=4.66445655725171848979367959315e-13`,

`5 sqrt(2e) delta5^(-1/10)=199.412389643181257323685783065`,

and

`(63/64)c0=0.244174897670745849609375`.

These values are reproduced by `CHECK.py` in this immutable run directory.
