SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-23T21:00:23Z.
attacking: the globally spread V1 overlap-one third-compound mass; compile it, without selecting one shared coordinate, into one actual original-coordinate three-bank packet and isolate the precise grouped Fourier debt.

# account03/B02 r39 — global three-bank compiler for the V1 overlap-one stratum

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** integrated Fourier estimate  
**Status:** `NEW SUPPORTING COMPILER / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/writeback is not native learned-memory ingestion.  
**Full-target continuity:** OPEN.  
**Target-wide universal unweighted Fourier-L1 criterion:** OPEN / not refuted.

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussianity, moments, compact support, connected support, log-concavity, post-rotation independence, or diagonal-basis independence is inserted.


## 1. Inputs actually used

The immediate same-slot predecessor is

`QFORM-LOCAL-COMPOUND-NEWTON-CASCADE-v1`,

`yspennstate/math-open-problems@c5cc2edeeee6426fcbbf73eb00fbd68a176d28cb`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T201213Z-account03-B02-qform-r38/REPORT.md`.

It decomposes

`e3(A^2)=V0+V1+V2+V3 >=1`,

where `Vr` is squared third-minor mass with row/column support intersection size `r`. The disjoint `V0` branch has a genuine Fourier-L1 receiver; this run addresses the globally spread part of `V1` rather than selecting a single shared coordinate.

The local shared-hub identity used below is the already-proved B02 theorem

`QFORM-V1-SHAREDHUB-TRANSVERSE-IDENTITY-v1`,

canonical source

`yspennstate/math-open-problems@343750e0bd888523ca52f424f46de7a25d070930`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T194347Z-account03-B02-qform-r38/REPORT.md`.

For one fixed shared physical coordinate `h`, one residual left/right cut, scalar `a=A_hh`, star vectors `c,r`, and residual cross block `N`, if `D_h` is the oriented overlap-one third-minor mass on that cut then

`sqrt(D_h) <= |a| sqrt(E2(N)) + sqrt(T_h)`,                    (1.1)

where

`T_h=||c||^2 ||r||^2 ||P_(c^perp) N P_(r^perp)||_F^2`.        (1.2)

At `a=0` equality holds: `D_h=T_h`.

The designated account04/B02 input is

`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

Whenever a nonsingular physical zero-diagonal principal triple `H0` is present, it gives

`L:=integral_R |phi_Q(t)|^2 dt
 <= 6 pi 2^(2/3) |det H0|^(-1/3)`.                            (1.3)

Section 5 applies (1.3) at an actual new inequality.

## 2. Global V1 random three-bank compiler

Write the ordered overlap-one mass as

`V1 = sum_{|I|=|J|=3, |I cap J|=1} det A[I,J]^2`.              (2.1)

Each ordered pair `(I,J)` in (2.1) has a unique shared coordinate `h`, a residual row pair `P=I\{h}`, and a residual column pair `Q=J\{h}`; `P` and `Q` are disjoint.

Independently color every physical coordinate into three banks `H,L,R` with probabilities

`P(H)=1/5,   P(L)=P(R)=2/5`.                                   (2.2)

For an actual coloring define

`W(H,L,R)
 = sum_{h in H}
   sum_{P subset L, Q subset R, |P|=|Q|=2}
      det A[{h} union P,{h} union Q]^2`.                        (2.3)

A fixed ordered overlap-one minor survives in (2.3) exactly when its shared coordinate is in `H`, its two row-only coordinates are in `L`, and its two column-only coordinates are in `R`. Therefore

`E W(H,L,R)
 =(1/5)(2/5)^4 V1
 = (16/3125) V1`.                                               (2.4)

Consequently there is an actual ORIGINAL-coordinate partition satisfying

`boxed: W >= (16/3125) V1.`                                    (2.5)

The probabilities in (2.2) are the optimizer among symmetric independent three-colorings: if `p_L=p_R=p` and `p_H=1-2p`, then `(1-2p)p^4` is maximized at `p=2/5`.

This is already a dimension-free aggregation of the shared-coordinate spread. No `max_h Delta_h` and hence no factor depending on the number of physical coordinates appears.

## 3. Exact grouped pivot-versus-two-star split on the same partition

Fix a partition attaining (2.5). Put

`N=A[L,R]`, `E=E2(N)`.

For each `h in H`, define

`a_h=A_hh`,
`c_h=A[L,h]`,
`r_h=A[h,R]`,
`C_h=P_(c_h^perp) N P_(r_h^perp)`,
`T_h=||c_h||^2 ||r_h||^2 ||C_h||_F^2`,                         (3.1)

with the evident conventions if a star vector vanishes. Let `D_h` denote the `h`-summand in (2.3), so `W=sum_h D_h`.

### Theorem 3.1 — `QFORM-V1-GLOBAL-THREEBANK-COMPILER-v1`

For the partition above,

`boxed:
 sqrt(W)
 <= sqrt( E sum_{h in H} a_h^2 )
    + sqrt( sum_{h in H} T_h ).
}`                                                               (3.2)

Hence

`boxed:
 max{ E sum_h a_h^2,  sum_h T_h }
 >= W/4
 >= (4/3125) V1.
}`                                                               (3.3)

In particular, on the target-scale branch `V1>1/4`, one actual physical partition satisfies

`boxed:
 max{ E2(A[L,R]) sum_{h in H} A_hh^2,
      sum_{h in H} ||A[L,h]||^2 ||A[h,R]||^2
      ||P_(A[L,h]^perp) A[L,R] P_(A[h,R]^perp)||_F^2 }
 > 1/3125.
}`                                                               (3.4)

### Proof

For each pair `(P,Q)` of two-subsets of `L,R`, write

`m_(P,Q)=det N[P,Q]`.

Laplace expansion along the shared coordinate gives the coefficient identity

`d_(h,P,Q)=a_h m_(P,Q)-z_(h,P,Q)`,                              (3.5)

where

`z_(h,P,Q)=r_h[Q]^T adj(N[P,Q]) c_h[P]`.                        (3.6)

For fixed `h`, the already-proved exterior identity gives

`sum_(P,Q) z_(h,P,Q)^2 = T_h`.                                 (3.7)

Also Cauchy-Binet gives

`sum_(P,Q) m_(P,Q)^2=E2(N)=E`.                                 (3.8)

Now stack all coefficients `(h,P,Q)` in one Euclidean coefficient space. The first array in (3.5) has squared norm

`sum_h a_h^2 sum_(P,Q)m_(P,Q)^2
 = E sum_h a_h^2`,                                               (3.9)

while the second has squared norm `sum_h T_h` by (3.7). The full difference array has squared norm `W`. Euclidean Minkowski therefore gives (3.2). If both terms inside the maximum in (3.3) were `<W/4`, their square roots would sum to `<sqrt(W)`, contradicting (3.2). Combine with (2.5). QED.

The point of (3.2) is that the local shared-coordinate compiler has now been aggregated **before** selecting any hub. The former `max_h Delta_h` loss is absent.

## 4. Heavy shared hub versus a genuinely diffuse grouped residue

Normalize the actual cut masses by

`omega_h=D_h/W` when `W>0`.                                     (4.1)

Then `omega` is a probability law on the actual physical shared hubs. Exactly one of the following holds:

* **heavy shared hub:** some `h` has `D_h>=W/2`;
* **diffuse shared-hub law:** every `omega_h<=1/2`.

Thus the globally spread `V1` problem is reduced, without a dimensional loss, to either a single target-scale local packet or a grouped determinant law already satisfying the standard `1/2` marginal threshold. The latter is a sharply scoped remaining analytic problem; this report does **not** claim that the abstract weights `omega_h` can simply be inserted into the projected-crossing theorem, because its rows must arise from the actual coefficient map rather than an exterior-feature lift.

On the heavy-hub branch,

`D_h >= W/2 >= (8/3125)V1`.                                     (4.2)

If additionally `A_hh=0`, the exact local identity gives `D_h=T_h`. On the favorable transverse subbranch from the completed one-hub theorem,

`rho_h=sr(C_h)>=2`,
`b_h=min(||c_h||^2,||r_h||^2)/||C_h||_F^2 <=1`,                (4.3)

we have `gamma=(rho_h-1)/(2rho_h)>=1/4` and the physical one-hub projected-E2 resource obeys

`R_hub >= (gamma/b_h) D_h
 >= (2/3125)V1`.                                                  (4.4)

The marginal-free one-hub projected-E2 Fourier theorem then gives

`boxed:
 ||p_Q||_infinity
 <= 3*2^(7/6)*exp(1/3) (3125/2)^(1/6) V1^(-1/6)
 =32.0177700561... V1^(-1/6),
}`                                                               (4.5)

and

`boxed:
 integral_R |phi_Q(t)|dt
 <= 201.173582385... V1^(-1/6).
}`                                                               (4.6)

Therefore this branch has a continuous `C0` density. At the target scale `V1>1/4`, (4.4) gives `R_hub>1/6250`, hence the absolute bounds

`||p_Q||_infinity <40.339862465`,
`integral |phi_Q| <253.462831130`.                               (4.7)

The only heavy exact-zero-pivot cases left by this payment are the transverse near-rank-one collar `rho_h<2` and the two-star-dominated collar `b_h>1`; nonzero shared pivots remain a separate packet. No claim is made that small principal determinant forces a small diagonal pivot.

## 5. Designated account04/B02 theorem applied to a new hybrid inequality

Stay on the exact-zero heavy-hub favorable branch (4.3), and suppose the exact scope of the designated partner theorem is also present: a nonsingular physical zero-diagonal principal triple `H0`.

The one-hub source theorem supplies the high-frequency envelope

`|phi_Q(t)|
 <= K_h R_hub^(-1/4)|t|^(-3/2),
 K_h=2^(7/4) pi^(3/2) exp(1/2).`                                (5.1)

The account04/B02 theorem supplies (1.3). For every `T>0`,

`integral |phi_Q|
 <= sqrt(2LT)+4 K_h R_hub^(-1/4)T^(-1/2)`.                     (5.2)

Optimizing in `T` gives

`integral |phi_Q|
 <=4 K_h^(1/2) R_hub^(-1/8)(2L)^(1/4)`,                       (5.3)

and Fourier inversion yields the actual partner hybrid

`boxed:
 ||p_Q||_infinity
 <=9.83947303316740
 |det H0|^(-1/12) R_hub^(-1/8).
}`                                                               (5.4)

Using the new global compiler (4.4),

`boxed:
 ||p_Q||_infinity
 <=24.6717151983
 |det H0|^(-1/12) V1^(-1/8).
}`                                                               (5.5)

At `V1>1/4`, this gives the absolute overlap bound

`boxed:
 ||p_Q||_infinity
 <29.339779254 |det H0|^(-1/12).
}`                                                               (5.6)

This is an equation-level application of the designated account04/B02 result, not a citation-only use. The continuity on this overlap is already supplied by the one-hub Fourier-L1 branch.

## 6. Finite deterministic regression

A seeded checker (`seed=20260923`) was run on 20 dense random symmetric matrices in dimensions 5,6,7, enumerating all three-colorings for each matrix. It verified:

* weighted-color expectation `(sum_color p(color)W)/(V1)=16/3125` to maximum relative error `1.41e-15`;
* zero violations of the grouped Minkowski consequence `max(A0,T0)>=W/4` on the maximizing cut;
* zero violations of the local coefficient/exterior identities used to form `T_h`;
* minimum observed maximizing ratio `max_color W/V1 =0.0411169729`, comfortably above the rigorous expectation floor `16/3125=0.00512`.

The computation is corroborative only. Equations (2.4) and (3.2) are exact symbolic proofs.

## 7. Scope and next exact debt

The **full universal QFORM conjecture remains OPEN**. Full-target continuity remains OPEN. The unrestricted target-wide assertion `sup integral|phi_Q|<infinity` remains **OPEN / not refuted**.

This run removes the dimension-dependent `max_h Delta_h` bottleneck from the `V1` overlap-one stratum. At `V1>1/4` there is always one actual physical three-bank partition carrying a fixed resource `>1/3125`; the only unpaid grouped mechanisms are now explicit:

1. `E2(N) sum_h A_hh^2` — grouped diagonal-pivot times crossing-two-volume;
2. `sum_h T_h` — grouped two-star/transverse mass;
3. in the latter family, either a heavy local hub (partially paid above) or a diffuse physical shared-hub law `omega_h<=1/2`.

The next B02 mechanism is therefore

`QFORM-V1-DIFFUSE-SHAREDHUB-WEIGHTED-FOURIER-v1`:
prove an actual-coefficient weighted Fourier inequality for the diffuse law `omega_h<=1/2`, or route the grouped pivot/two-star resource into an existing grouped-hub/ridge receiver. The exterior-feature weights must not be substituted for physical coefficient rows without proof.

No task identity, schedule, enabled/paused state, notification, email, Drive, public-release, paid-API, permission, or cross-account-authentication state was changed.
