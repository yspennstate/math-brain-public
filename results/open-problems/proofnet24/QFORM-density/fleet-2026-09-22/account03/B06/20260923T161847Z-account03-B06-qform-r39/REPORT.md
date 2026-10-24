SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T16:18:47Z.
attacking: change mechanism from the three preceding determinant/cofactor runs: retain the entire nonzero near-rank-two tail inside the one-scale ridge operator and prove a paid-ridge / bounded physical ridge-hub / ultra-thin-rank-two trichotomy.

# account03/B06 r39 — one-scale ridge payment or ultra-thin rank-two physical cross tube

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`, programme revision `2026-09-22.5`  
**Assignment:** Curved fiber integration  
**Status:** `NEW SUPPORTING TRICHOTOMY / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and mechanism change

The unrestricted target remains open: for every dimension, independent ORIGINAL real coordinates with densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `Q=X^TAX`, or give a valid counterexample. No moment, support, iid, Gaussian, log-concavity, sign, finite-rank, compactness or post-rotation independence assumption is introduced. Continuity is tracked separately.

The previous B06 runs r36-r38 all developed determinant/cofactor cascades. The owner protocol asks for a mechanism change after three unchanged substantive runs. This run changes to the **one-scale ridge characteristic-function mechanism** while staying on the same physical near-rank-two cross packet. The small nonzero tail is never deleted as a random perturbation: it remains inside the exact ridge matrix `K`.

Fresh control source at startup: `yspennstate/math-research-brain@e1a13a8fc3898c98d4dff65adf01266c77df70fd`. The live corrections consumed include: no law-uniform pointwise van-der-Corput decay; no independence after spectral rotation; arbitrary-joint rank-three coarea is false; positive moments of worst conditional projection-density caps can diverge; unrestricted fiber suprema lose dimension; a small coefficient tail cannot be thrown away for arbitrary unbounded inputs; and aggregate determinant mass need not contain one universally good physical minor.

The exact designated `account04/B06` current-QFORM handoff directory was absent at startup/source refresh, so no theorem is fabricated there. The compatible completed account04 result actually applied below is the account04/B20 cross-cut theorem:

`yspennstate/math-open-problems@3671f29afb89083947437ffc4ebbb037aba58a4d`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T142031Z-account04-B20-QFORM-r10/REPORT.md`.

It supplies, in the live no-moderate-diagonal branch, a literal ORIGINAL-coordinate partition `[n]=J disjoint_union K` with cross block

`N=A[J,K]`,

`E:=||N||_F^2 > c3:=11907/16384`,                                      (1.1)

and the B06 r37 near-rank-two survivor additionally has squared singular values

`x1>=x2>=...>=0`, `sum_r x_r=E`,

`T:=sum_{r>=3}x_r < E/64`,                                              (1.2)

`x2 >= E/64`.                                                           (1.3)

The source for (1.2)-(1.3) is

`yspennstate/math-open-problems@fa9d5dd3cc78a092484480b536872d332e22c90a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T141825Z-account03-B06-qform-r37/REPORT.md`.

The ridge theorem used below is the source-pinned `QFORM-RIDGE-DENSITY-v1`:

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For any ORIGINAL-coordinate cross block `B`, any `gamma>0`,

`K=B B^T (gamma^2 I+B B^T)^(-1)`,

`theta=tr K`,

if `1<=q<=2`, `max_i K_ii<=q/2` and `theta>2q`, then the FULL ambient quadratic form, with all same-bank terms and outside couplings retained, has a continuous `C_0` density and

`||p_Q||_infinity
 <= sqrt(e)/(sqrt(2q) gamma) * theta/(theta-2q)`.                        (1.4)

The theorem also applies to `B^T`; the two ridge matrices have the same trace `theta`.

## 2. Fix an absolute ridge scale

Set

`gamma=1/64`, `a:=gamma^2=1/4096`.                                      (2.1)

Define

`K_L=N N^T(aI+N N^T)^(-1)`,

`K_R=N^T N(aI+N^T N)^(-1)`,                                            (2.2)

and

`theta=tr K_L=tr K_R=sum_r x_r/(a+x_r)`.                               (2.3)

Both `K_L` and `K_R` are positive contractions, so every diagonal entry lies in `[0,1)`.

From (1.1)-(1.3),

`x2 >= E/64 > c3/64 =11907/1048576`.                                   (2.4)

Therefore each of the first two ridge eigenvalues is strictly larger than

`kappa0 := (11907/1048576)/(11907/1048576+1/4096)
          =11907/12163
          =0.9789525610457946...`.                                     (2.5)

Hence the top two directions alone contribute

`theta_top2 > 2 kappa0 =23814/12163
                         =1.957905122091589...`.                        (2.6)

This absolute lower bound is where the actual account04/B20 energy floor is used.

## 3. High effective ridge dimension is already a full density payment

### Lemma 3.1 — `QFORM-R39-HIGH-RIDGE-PAYMENT-v1`

If

`theta >= 9/2`,                                                         (3.1)

then the FULL ambient law has a continuous density with

`boxed: ||p_Q||_infinity <= 288 sqrt(e) < 474.832.`                     (3.2)

#### Proof

Use (1.4) with `q=2`. Since `K_L` is a positive contraction,

`max_i (K_L)_ii <=1=q/2`,                                               (3.3)

and `theta>=9/2>4=2q`. Also

`theta/(theta-4) <= (9/2)/(1/2)=9`.                                    (3.4)

With `gamma=1/64`, (1.4) gives

`||p_Q||_infinity
 <= sqrt(e)/(2 gamma) * 9
 =288 sqrt(e)`.                                                         (3.5)

No orientation assumption and no tail deletion occurs. QED.

This branch is important because `q=2` makes the leverage gate automatic: once the one-scale effective dimension is large enough, arbitrarily complicated small singular directions pay for themselves.

## 4. Intermediate effective dimension: diffuse ridge pays, otherwise two finite physical hubs

### Lemma 4.1 — `QFORM-R39-MID-RIDGE-OR-8x8-HUB-v1`

Assume

`9/4 <= theta < 9/2`.                                                   (4.1)

If either

`max_i (K_L)_ii <=1/2`                                                  (4.2)

or

`max_j (K_R)_jj <=1/2`,                                                 (4.3)

then the FULL ambient law has a continuous density satisfying

`boxed: ||p_Q||_infinity <=288 sqrt(2e)<671.514.`                       (4.4)

If neither (4.2) nor (4.3) holds, define the physical ridge-heavy sets

`H_L={i in J:(K_L)_ii>1/2}`,

`H_R={j in K:(K_R)_jj>1/2}`.                                           (4.5)

Then both are nonempty and

`boxed: 1<=|H_L|<=8, 1<=|H_R|<=8.`                                     (4.6)

#### Proof

If (4.2) holds, apply (1.4) to `N` with `q=1`. If (4.3) holds, apply it to `N^T`. In either case `theta>=9/4>2`, and

`theta/(theta-2) <= (9/4)/(1/4)=9`.                                    (4.7)

Thus

`||p_Q||_infinity
 <= sqrt(e)/(sqrt(2)gamma)*9
 =288 sqrt(2e)`.                                                        (4.8)

If both gates fail, the sets in (4.5) are nonempty. Since diagonal sums equal the trace,

`|H_L|/2 < sum_{i in H_L}(K_L)_ii <=theta<9/2`,                         (4.9)

so `|H_L|<9` and hence `|H_L|<=8`; identically for `H_R`. QED.

Thus every un-paid intermediate-ridge state is compressed to two literal ORIGINAL-coordinate hubs of cardinality at most eight. This is not a claim that the entire curvature is supported on those hubs; it is an exact certificate that every obstruction to the ridge theorem at this scale is physically localized on both sides.

## 5. Low effective dimension forces an ultra-thin absolute rank-two tube

The genuinely new quantitative implication is that failure of even the low threshold `theta>=9/4` collapses the complete nonzero cross tail by more than two orders of magnitude relative to the old r38 tube.

Let

`eta := sum_{r>=3} x_r/(a+x_r)`                                        (5.1)

be the exact tail contribution to the ridge trace.

### Lemma 5.1 — ridge trace controls total tail energy

For any `a>0` and nonnegative numbers `y_j`,

`sum_j y_j/(a+y_j) >= (sum_j y_j)/(a+sum_j y_j)`.                      (5.2)

#### Proof

For two variables,

`x/(a+x)+y/(a+y)-(x+y)/(a+x+y)
 =xy(2a+x+y)/[(a+x)(a+y)(a+x+y)] >=0`.                                 (5.3)

Induction proves (5.2). QED.

### Theorem 5.2 — `QFORM-R39-ULTRATHIN-RANK2-v1`

If

`theta <9/4`,                                                           (5.4)

then

`boxed:
 T=dist_F(N, rank<=2)^2
 < 14211/141070336
 =0.00010073698272044947...`,                                          (5.5)

and therefore

`boxed:
 dist_F(N,rank<=2)<0.010036782.`                                       (5.6)

#### Proof

By (2.6),

`eta=theta-theta_top2
 < 9/4 - 23814/12163
 =14211/48652
 =:eta0
 =0.29209487790841077...`.                                             (5.7)

Apply Lemma 5.1 to the tail singular energies `x_r`, `r>=3`:

`eta >= T/(a+T)`.                                                       (5.8)

Hence

`T < a eta0/(1-eta0)
   = (1/4096)(14211/48652)/(34441/48652)
   =14211/141070336`,                                                   (5.9)

which is (5.5); (5.6) follows from Eckart-Young. QED.

For comparison, r38's recursive cofactor route only forced a residual-core rank-two distance below `1/(4sqrt2)=0.176777` in its large-core branch. The present statement concerns the original r37 physical cross block `N` and, without deleting any tail, forces its complete singular tail below `0.010037` whenever the ridge receiver cannot even reach effective trace `9/4`.

### Corollary 5.3 — a ridge-heavy coordinate in the low-trace branch is a strong top-two physical anchor

Let `U_2` be the top-two left singular frame of `N`. Under `theta<9/4`, if some physical row satisfies

`(K_L)_ii>1/2`,                                                         (5.10)

then

`boxed: ||U_2(i,:)||_2^2 > 10115/48652
                           =0.207905122091589... .}`                    (5.11)

The transpose statement holds for the top-two right singular frame.

#### Proof

The ridge contribution of every tail direction to one diagonal is at most its contribution to the total tail trace, hence at most `eta<eta0`. Therefore the first two ridge directions contribute more than

`1/2-eta0
 =10115/48652`.                                                        (5.12)

Each first-two ridge eigenvalue is at most one, so the ordinary top-two projector leverage is at least that contribution. QED.

Thus a high-leverage failure in the ultra-thin branch is not a vague ridge obstruction: it forces a literal physical coordinate carrying more than `20.79%` of the dominant two-dimensional singular plane.

## 6. Combined r39 compiler on the live near-rank-two packet

Combining Sections 3-5 gives the following source-valid trichotomy for the actual r37/r38 survivor.

### Theorem 6.1 — `QFORM-NEARRANK2-RIDGE-OR-HUB-OR-ULTRATHIN-v1`

For the account04/B20 physical cut satisfying (1.1), in the B06 near-rank-two chamber (1.2)-(1.3), exactly one of the following source-valid exits is available at scale `gamma=1/64`:

1. **High effective dimension:** `theta>=9/2`, and the full ambient quadratic form has a continuous density `<474.832`.
2. **Intermediate diffuse ridge:** `9/4<=theta<9/2` and at least one orientation has maximum ridge leverage `<=1/2`; the full ambient form has a continuous density `<671.514`.
3. **Intermediate double physical hub:** `9/4<=theta<9/2` and both orientations fail the leverage gate; there are row and column ridge-heavy physical hubs, each of cardinality at most eight.
4. **Low effective dimension:** `theta<9/4`; then the ENTIRE nonzero cross tail satisfies `dist_F(N,rank<=2)<0.010037`. If either ridge orientation is heavy, it additionally supplies a physical top-two singular-plane anchor of leverage `>0.207905`.

The density branches retain arbitrary same-bank curvature, every outside coupling, every sign, and the complete cross tail because they apply the ridge theorem to the literal `N`. The structural branches are coefficient statements only; they do not replace the quadratic form by a low-rank approximation and therefore do not commit the forbidden small-random-tail deletion.

This substantially narrows the r38 debt. The remaining near-rank-two work is no longer an arbitrary `0.1768` Frobenius tube. It is either a bounded-cardinality double physical ridge hub or a literal cross block whose full tail is below `0.010037` while its second singular energy still obeys

`x2 >11907/1048576 =0.0113554...`.                                      (6.1)

In particular the ratio

`T/x2 < (14211/141070336)/(11907/1048576)
       <0.008872`,                                                      (6.2)

so less than `0.8872%` of the guaranteed second-singular energy remains in all singular directions from the third onward.

## 7. What is and is not closed

This run **does not** prove the full conjecture. In the ultra-thin diffuse rank-two survivor, an arbitrarily small but nonzero tail still cannot be erased for unbounded inputs. The next exact B06 implication is:

`QFORM-ULTRATHIN-RANK2-PRODUCT-RECEIVER-v1`:

> Starting from `x2>0.0113554`, `sum_{r>=3}x_r<0.000100737`, retain the whole tail and arbitrary same-bank terms; either combine a second independent product-structured curvature currency with the rank-two half-Riesz mechanism, or show that the `>20.79%` physical top-plane anchor / at-most-eight double-ridge hub necessarily activates an existing grouped-square, pair-log, third-volume, or finite-bank receiver.

A separate useful task is to splice the new `<=8 x <=8` ridge hubs into the finite grouped `2+2+2` product-triangle packet now appearing in account03/B19, without replacing the grouped product provenance by an arbitrary bounded joint law.

`QFORM-R39-HIGH-RIDGE-PAYMENT-v1`: **PROVED supporting density branch**.  
`QFORM-R39-MID-RIDGE-OR-8x8-HUB-v1`: **PROVED supporting dichotomy**.  
`QFORM-R39-ULTRATHIN-RANK2-v1`: **PROVED supporting quantitative reduction**.  
`QFORM-NEARRANK2-RIDGE-OR-HUB-OR-ULTRATHIN-v1`: **PROVED supporting compiler**.  
Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.  
Universal continuity: **OPEN**; continuity is established here only on the two ridge-paid branches.
