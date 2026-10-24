SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T04:41:00Z.
attacking: the high-tail four-bank survivor — aggregate all third minors through determinant-weighted disjointness, then force a double-incident physical anchor before any reciprocal minor payment.

# account03/B07 QFORM r24 — global E3 disjointness or a double-incident physical anchor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Run:** `20260923T044100Z-account03-B07-qform-r24`  
**Fresh control before write:** `yspennstate/math-research-brain@32a1935ac4f126737f7dd9f50e03634e7f4f4002`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Classification:** `NEW DIMENSION-FREE AGGREGATE MINOR SELECTION THEOREM + PAID CONTINUOUS BRANCHES / FULL TARGET OPEN`.

## 1. Scope and correction boundary

The exact owner target remains unrestricted: independent ORIGINAL real coordinates, each having a probability density bounded by one, and an arbitrary real symmetric ambient matrix with at least three eigenvalues of modulus at least one. The goal is one universal finite essential-density bound for `Q=X^T A X`, or a valid counterexample. The stronger continuous-density conclusion is tracked separately.

No Gaussian, moment, compact-support, connected-support, log-concavity, iid, post-rotation independence, arbitrary-joint coarea bound, positive conditional-projection-height moment, law-uniform pointwise quadratic-phase decay, naive fiber-supremum integration, small-coefficient deletion, or one-good-minor principle is used here. In particular, the argument never chooses a tiny local determinant and then pays its reciprocal. All selection occurs through complete squared-minor mass before any analytic receiver is invoked.

The designated `account04/B07` current-QFORM artifact was searched again and remains absent; no partner result is fabricated. A compatible completed account04/B18 product-projection result is applied to the actual large-star inequality in Section 7.

## 2. Inputs actually used

### 2.1 Global three-volume disjointness theorem

The newest account03/B02 result is

`yspennstate/math-open-problems@aa76b8c1d3d2e6ef6477500d94220c1d54bff4b8`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T043653Z-account03-B02-qform-r20/REPORT.md`.

For an ORIGINAL-coordinate cross block `M=A[I,J]`, put

`Z=E_3(M)=sum_{|S|=|T|=3} det M[S,T]^2>0`.                     (2.1)

Define the canonical squared-minor probability law

`w(S,T)=det M[S,T]^2/Z`.                                      (2.2)

Let `mu_r` be its row-triple marginal, draw two independent row triples from `mu_r`, and let

`delta_r=P(the two row triples are disjoint)`.                 (2.3)

The B02 theorem proves that if `delta_r>0`, then the FULL ambient quadratic form has a continuous density and

`||p_Q||_infinity <= 3 e delta_r^(-1/6) Z^(-1/6)`.             (2.4)

It also proves the exact identity

`delta_r=E_{S~mu_r}[E_3(M[S^c,J])/Z]`.                         (2.5)

Therefore some physical row triple `R0` satisfies

`E_3(M[R0^c,J]) <= delta_r Z`.                                (2.6)

Applying the same theorem to `M^T` defines a column disjointness `delta_c` and gives the analogous physical column triple `C0`.

All same-side curvature, outside couplings and affine terms are retained in (2.4).

### 2.2 Anchored self-matched third-volume theorem

The newest account03/B08 result is

`yspennstate/math-open-problems@e875d54d4a946d399466cb6afa1fc37da12a11d2`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T042303Z-account03-B08-qform-diffuse-r27/REPORT.md`.

For a physical row anchor `i` and column anchor `a`, define the complete double-incident third-volume packet

`W_ia=sum_{|S|=|T|=3, i in S, a in T} det M[S,T]^2`.            (2.7)

Normalize these minors to a probability law. Let `alpha_k` be the inclusion marginal of residual row `k!=i`; each draw contains exactly two residual rows. If

`max_{k!=i} alpha_k <=1/2`,                                    (2.8)

then with `R_i=||row_i(M)||_2`, the full ambient form has a continuous density satisfying

`||p_Q||_infinity <=10 sqrt(e) (2W_ia/R_i)^(-1/5)`.            (2.9)

The transposed theorem uses the anchor column norm and residual column marginals.

If (2.8) fails, then some residual row `k` carries more than half the anchored packet:

`sum_{S contains {i,k}, T contains a} det M[S,T]^2 > W_ia/2`. (2.10)

The column statement is analogous.

## 3. Main new selection theorem

### Theorem 3.1 — `QFORM-E3-DISJOINTNESS-TO-DOUBLE-ANCHOR-v1`

Let `M` be any real ORIGINAL-coordinate cross block with `Z=E_3(M)>0`. Fix

`0<eta<1/2`.                                                    (3.1)

Then at least one of the following occurs.

**A. Globally disjoint third-volume branch.** At least one of

`delta_r >= eta`, `delta_c >= eta`                             (3.2)

holds, and the full ambient quadratic form has a continuous density with

`boxed: ||p_Q||_infinity <=3 e eta^(-1/6) Z^(-1/6).`          (3.3)

**B. Double-incident physical anchor.** There exist a physical row `i` and physical column `a` such that

`boxed: W_ia > ((1-2eta)/9) Z.`                               (3.4)

No individual determinant is selected in either branch.

#### Proof

If (3.2) holds, apply (2.4), to `M` or `M^T`, proving (3.3).

Assume instead

`delta_r<eta`, `delta_c<eta`.                                  (3.5)

By (2.6), choose a physical row triple `R0` satisfying

`E_3(M[R0^c,J])<eta Z`.                                       (3.6)

Under the full joint law (2.2), (3.6) is exactly

`P_w(S cap R0=empty)<eta`.                                    (3.7)

The transposed argument gives a physical column triple `C0` such that

`P_w(T cap C0=empty)<eta`.                                    (3.8)

The union bound gives

`P_w(S cap R0 !=empty AND T cap C0 !=empty)>1-2eta`.          (3.9)

Now sum all double-incident packets over the nine anchor pairs in `R0 x C0`:

`sum_{i in R0,a in C0} W_ia
 = Z E_w[ |S cap R0| |T cap C0| ]`.                           (3.10)

On the event in (3.9), the product in (3.10) is at least one. Hence

`sum_{i in R0,a in C0} W_ia >(1-2eta)Z`.                      (3.11)

There are nine pairs, so one satisfies (3.4). QED.

The key point is that the selector is a **nine-anchor aggregate consequence of the entire third compound**. It does not assert that one `3x3` determinant is large.

## 4. Analytic payment of a diffuse double-anchor

Take the anchor `(i,a)` from Theorem 3.1(B). Put

`F=||M||_F`.                                                    (4.1)

Both the anchor row and anchor column norms are at most `F`. Therefore if the anchored residual row law obeys (2.8), the B08 theorem gives

`||p_Q||_infinity
 <=10 sqrt(e) [2(1-2eta)Z/(9F)]^(-1/5)`.                      (4.2)

The same bound follows if the residual column marginals of the anchored law are all at most `1/2`, by transposing `M`.

Thus the only survivor of the double-anchor branch has **both** a heavy residual row and a heavy residual column. More precisely:

### Corollary 4.1 — `QFORM-DOUBLE-INCIDENT-TO-ONE-SIDED-NESTS-v1`

If neither anchored diffuse theorem applies, there exist `k!=i` and `ell!=a` such that

`boxed:
 sum_{S contains {i,k}, T contains a} det M[S,T]^2
 > ((1-2eta)/18) Z,`                                          (4.3)

and

`boxed:
 sum_{S contains i, T contains {a,ell}} det M[S,T]^2
 > ((1-2eta)/18) Z.`                                         (4.4)

This is again aggregate determinant currency in literal original coordinates.

**Important non-claim.** Equations (4.3)-(4.4) do *not* imply that the intersection packet containing all four anchors `{i,k}` and `{a,ell}` has a universal fraction of `Z`. The two conditional inclusion marginals can each be just above `1/2`, so their intersection lower bound can be arbitrarily small. A next receiver must consume the two one-sided nests jointly or re-randomize; it may not silently intersect them.

## 5. Application to the B07 four-bank high-tail survivor

The immediate B07 predecessor is r22/r23. Its four mutually disjoint ORIGINAL-coordinate banks carry two outer star norms `C,R` and a physical cross block `M` with

`C R F > kappa`,
`F=||M||_F`,
`kappa=1/(256 sqrt(3))`.                                      (5.1)

Let the squared singular values of `M` be `lambda_1>=lambda_2>=...` and

`T=sum_{j>=3} lambda_j`.                                      (5.2)

The completed r22 scale lemma proves that for `0<theta<=1/2`, the high-tail condition

`T>=theta F^2`                                                 (5.3)

forces

`boxed: Z=E_3(M) >= (theta^2/6)F^6.`                          (5.4)

Fix also `Lambda>0`. If the large-star alternative `CR>Lambda` fails, (5.1) gives

`F>kappa/Lambda`.                                              (5.5)

Combining Theorem 3.1 with (5.4), every such high-tail state has one of:

**H1. Global disjointness paid:**

`boxed:
 ||p_Q||_infinity
 <=3e eta^(-1/6)(6/theta^2)^(1/6) F^(-1).`                   (5.6)

**H2. Double-anchor diffuse paid:**

`boxed:
 ||p_Q||_infinity
 <=10sqrt(e)[(1-2eta)theta^2/27]^(-1/5) F^(-1).`             (5.7)

**H3. Double nested third-volume survivor:** there are physical `i,k` on the row side and `a,ell` on the column side for which both one-sided packets satisfy

`boxed:
 P_row-nest > ((1-2eta)theta^2/108)F^6,`                      (5.8)

`boxed:
 P_col-nest > ((1-2eta)theta^2/108)F^6.`                      (5.9)

Equations (5.8)-(5.9) denote the squared-minor sums displayed in (4.3)-(4.4), not probabilities.

This is a strictly more physical reduction than the prior spectral bicore: all surviving anchors are literal original-coordinate indices and the resources are complete incident third-compound packets.

## 6. Concrete collar

Take

`theta=1/16`, `eta=1/64`, `Lambda=1`.                          (6.1)

Then

`Z>=F^6/1536`.                                                 (6.2)

If global row or column disjointness is at least `1/64`, (5.6) gives

`boxed: ||p_Q||_infinity <55.400150 F^(-1)`.                  (6.3)

Because failure of the large-star branch gives `F>kappa`, this implies the dimension-free numerical bound

`||p_Q||_infinity <24564.704`.                                 (6.4)

If both global disjointnesses are below `1/64`, Theorem 3.1 gives an anchor packet

`boxed: W_ia > (31/442368)F^6.`                               (6.5)

If either anchored residual side is diffuse, then

`boxed: ||p_Q||_infinity <97.235678 F^(-1)<43114.787.`        (6.6)

If both anchored residual sides are heavy, the one-sided nests satisfy

`boxed:
 P_row-nest,\ P_col-nest > (31/884736)F^6.`                   (6.7)

Thus, at this concrete collar, the entire non-large-star high-tail branch is either analytically paid with a continuous density or reduced to two fixed, source-valid one-sided third-volume nests of universal relative size.

## 7. Completed account04 result applied to an actual inequality

The designated `account04/B07` current-QFORM source remains absent. The compatible completed account04/B18 source used by r22 is

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

Its scalar product-projection consequence is

`||p_(u^T X)||_infinity <=sqrt(2)/||u||_2`                     (7.1)

for an original-coordinate coefficient bank `u`. The two outer star banks in (5.1) are disjoint original-coordinate sets, so their projections are genuinely independent. Therefore on the complementary large-star branch `CR>Lambda`,

`boxed:
 ||p_(c_L^T X_L, r_R^T X_R)||_infinity
 <=2/(CR)<2/Lambda.`                                          (7.2)

Equation (7.2) is an actual application of completed account04 mathematics. It is retained only as product-linear provenance; a bounded projected joint density is not promoted to a generic indefinite quadratic pushforward theorem.

For comparison, the r23 incident-volume sibling has the actual star product

`||r|| ||c|| > theta F^2/480`,                                (7.3)

so the same theorem yields

`||p_(r^T X,c^T Y)||_infinity <960/(theta F^2)`.               (7.4)

At `theta=1/16` and, when applicable, `F>kappa`, the crude dimension-free cap in (7.4) is `<3,019,898,880`. The magnitude is irrelevant; the point is that this is genuine independent-product currency rather than a false curved receiver.

## 8. What remains

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.** Continuity is proved here on branches H1 and H2, but not on the double-nested survivor or on the large-star resource (7.2) by this report alone.

The first B07 high-tail debt is now

`QFORM-HIGHTAIL-DOUBLE-NESTED-THIRDVOLUME-RECEIVER-v1`:

> Starting from the two one-sided packets (5.8)-(5.9), consume them jointly without assuming a positive four-anchor intersection and without selecting one local determinant; or route them to a physical three-coordinate block, mixed-hub theorem, grouped-square theorem, a second global-disjointness law, or another already-paid aggregate receiver while retaining arbitrary same-bank curvature and additional spectrum.

The low-tail rank-one tube from r23 remains a separate debt. The new scale-sensitive B11 robust recoloring theorem supplies a paid chamber once a controlled pair-PSD packet is extracted, but such extraction is not automatic and is not claimed here.

## 9. Source pins and execution status

- Fresh control before this write: `yspennstate/math-research-brain@32a1935ac4f126737f7dd9f50e03634e7f4f4002`, OWNER CONTROL `2026-09-22.15`.
- Own incoming r22 bundle: `yspennstate/math-open-problems@c6ef0024d2d937df235fa0f8c8d7ad5a416dbba0`.
- Own incoming r23 bundle: `yspennstate/math-open-problems@e24329a6a315b96a87b3efc608473ef0554f3b8d`.
- Global disjointness theorem: `math-open-problems@aa76b8c1d3d2e6ef6477500d94220c1d54bff4b8`.
- Anchored mixed-order theorem: `math-open-problems@e875d54d4a946d399466cb6afa1fc37da12a11d2`.
- Compatible account04 product-projection source: `math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`.

Repository transport is not native learned-memory ingestion. No authenticated native receiver retrieval/use occurred, so this run remains `WITHOUT_VERIFIED_BRAIN` with `full_brain_connected=false`. No task identity, schedule, enabled/paused state, notification setting, email/public workflow, paid model/API/Codex call, or cross-account native state was changed.
