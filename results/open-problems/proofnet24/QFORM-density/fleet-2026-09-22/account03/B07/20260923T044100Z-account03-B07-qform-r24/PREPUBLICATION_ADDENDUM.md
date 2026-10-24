# r24 prepublication correction and genuine advance

Fresh correction refresh after the first `REPORT.md` write found the new account03/B02 correction handoff at brain commit `475842ad3094381bb411c7b4cac008ed3207032c` and canonical mathematics

`yspennstate/math-open-problems@648ea277fc2cfcc8ce11a7093c61951a9e15baa8`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T043653Z-account03-B02-qform-r20/ADDENDUM_COMPOUND_HUB_COMPILER.md`.

That correction states that B02's r19 structural corollary already contains the six-coordinate compound-hub incidence statement from which `REPORT.md` Theorem 3.1 follows. Therefore the double-anchor theorem in the first r24 report is **mathematically valid but not counted as new progress**. This addendum changes mechanism immediately and records the principal new B07 advance after consuming B02's genuinely new compound-hub compiler.

The full QFORM conjecture remains open throughout.

## 1. New input: compound hub to two explicit physical resources

Let `M` be the current B07 original-coordinate cross block and

`Z=E3(M)>0`.

Let `delta_r,delta_c` be the determinant-weighted row/column triple disjointness probabilities. The corrected B02 theorem says that if

`delta_r,delta_c<eta<1/2`,

then there is a physical row/column anchor pair `(i,a)` such that, after writing

`M=[[b,r^T],[c,N]]`,

and

`F_perp=||P_(c^perp) N P_(r^perp)||_F`,

one has

`boxed:
 max{ b^2 E2(N), ||c||^2 ||r||^2 F_perp^2 }
 >= ((1-2eta)/36) Z.
`                                                                  (1.1)

This is an aggregate physical-block identity. It selects no local minor and takes no reciprocal determinant.

## 2. New B07 theorem: high-tail compound hub gives E2 matching banks or a transverse two-star reserve

The current B07 high-tail state has

`F=||M||_F`,

and, from r22,

`Z=E3(M) >= (theta^2/6) F^6`,                                  (2.1)

for `0<theta<=1/2`.

Define

`rho=((1-2eta) theta^2)/216`.                                  (2.2)

Combining (1.1) and (2.1) gives

`max{ b^2 E2(N), ||c||^2 ||r||^2 F_perp^2 } >= rho F^6`.       (2.3)

### Theorem — `QFORM-HIGHTAIL-COMPOUND-HUB-E2-OR-TRANSVERSE-v1`

Under the high-tail hypothesis (2.1) and `delta_r,delta_c<eta`, at least one of the following holds.

**E. Residual aggregate-E2 branch.**

`boxed: E2(N) >= rho F^4.`                                     (2.4)

Moreover there are two disjoint original-coordinate row banks `L1,L2`, two disjoint original-coordinate column banks `R1,R2`, and a matching `sigma in S2` such that

`boxed:
 ||N[L1,R_sigma(1)]||_F^2
 ||N[L2,R_sigma(2)]||_F^2
 >= (rho/16) F^4.
`                                                                  (2.5)

**T. Transverse two-star branch.**

`boxed: ||c|| ||r|| F_perp >= sqrt(rho) F^3`,                  (2.6)

and hence, because `F_perp<=||N||_F<=F`,

`boxed: ||c|| ||r|| >= sqrt(rho) F^2.`                         (2.7)

#### Proof

If the first term in (2.3) is at least `rho F^6`, then `b^2<=F^2`, so

`E2(N)>=rho F^4`,

which is (2.4). The completed B07 two-coloring argument for aggregate second minors says that every matrix with second-compound mass `E2(N)` admits disjoint two-color row and column banks with matching product at least `E2(N)/16`; this gives (2.5).

If the second term in (2.3) is at least `rho F^6`, taking square roots gives (2.6), and `F_perp<=F` gives (2.7). QED.

This is the principal new result of r24 after the duplicate discovery. It converts the determinant-weighted third-compound concentration into one of two lower-order original-coordinate bank resources with universal scale, without ever asserting that one physical determinant is large.

## 3. Concrete collar

Take the same convenient constants

`theta=1/16`, `eta=1/64`.

Then

`rho=(31/32)*(1/256)/216=31/1769472`.                           (3.1)

Thus every high-tail, small-disjointness state has either

`boxed: E2(N) >= (31/1769472)F^4`,                             (3.2)

and a two-color matching-bank product

`boxed:
 ||N[L1,R_sigma(1)]||_F^2
 ||N[L2,R_sigma(2)]||_F^2
 >= (31/28311552)F^4,
`                                                                  (3.3)

or

`boxed:
 ||c|| ||r||
 >= sqrt(31/1769472) F^2
 =0.00418561230945... F^2.
`                                                                  (3.4)

These constants are dimension-free.

## 4. Completed account04 result applied to the new inequality

The designated `account04/B07` current-QFORM artifact remains absent. The compatible completed account04/B18 product-projection theorem is the same source pinned in `REPORT.md`:

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`.

The star vectors `c` and `r` in (3.4) live on disjoint original-coordinate banks. Therefore their scalar projections are genuinely independent and the account04 theorem gives

`||p_(c^T X, r^T Y)||_infinity
 <=2/(||c||||r||)
 <2 rho^(-1/2) F^(-2).`                                      (4.1)

At (3.1),

`boxed:
 ||p_(c^T X,r^T Y)||_infinity
 <477.827341 F^(-2).
`                                                                  (4.2)

If the outer large-star alternative `CR>Lambda` has failed, the inherited B07 packet `CRF>kappa`, `kappa=1/(256sqrt(3))`, implies `F>kappa/Lambda`. Therefore (4.2) becomes the dimension-free coefficient-plane cap

`||p_(c^T X,r^T Y)||_infinity
 < 477.827341 Lambda^2/kappa^2`.                               (4.3)

At `Lambda=1`, the right side is `<93,944,677.846`.

This is an actual application of completed account04 mathematics to the **new** transverse-star inequality. It is deliberately retained only as product-linear currency; a bounded projected joint density alone is not a generic curved-pushforward theorem.

## 5. Updated proof map

The correct r24 high-tail route is now:

1. if one determinant-weighted row/column disjointness is large, the already-completed balanced-crossminor Fourier theorem pays a continuous density;
2. if both are small, use the corrected B02 compound-hub compiler, not the duplicate selector as the claimed novelty;
3. Theorem (2.4)-(2.7) converts the compound hub into either an aggregate residual `E2` matching-bank packet or a transverse two-star packet;
4. the B08 anchored mixed-order theorem remains an additional analytic exit when the chosen incident third-volume law is diffuse, but it is not needed for the algebraic compiler above.

The next B07 implication is now

`QFORM-HIGHTAIL-E2-OR-TRANSVERSE-RECEIVER-v1`:

> Pay either the residual `E2` matching-bank packet (2.5) or the transverse product `||c||||r||F_perp` from (2.6) while retaining arbitrary same-bank curvature and the true full Schur remainder; or route them to a paid mixed-hub, rank-two affine, grouped-square, physical-three-scalar, or second global-disjointness endpoint.

The low-tail rank-one tube remains a separate debt.

## 6. Status

`REPORT.md` remains a valid record of the double-anchor derivation and its analytic consequences, but its Theorem 3.1 is now explicitly classified as **subsumed / duplicate**, not principal new progress. This addendum is the authoritative novelty/status correction for r24.

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. Global continuity remains open. Execution remains `WITHOUT_VERIFIED_BRAIN`; no scheduler, notification, email, public-release, paid-model/API/Codex, permission, or cross-account native state was changed.
