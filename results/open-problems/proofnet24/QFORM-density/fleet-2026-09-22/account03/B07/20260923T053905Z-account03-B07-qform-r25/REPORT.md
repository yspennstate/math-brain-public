SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T05:39:05Z.
attacking: the high-tail nested-third-volume survivor — compile a fixed two-row/one-column determinant nest into disjoint physical edge-star-core or three-linear-bank currency before any reciprocal minor payment.

# account03/B07 QFORM r25 — nested third-volume to disjoint physical links

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Run:** `20260923T053905Z-account03-B07-qform-r25`  
**Start control:** `yspennstate/math-research-brain@2b6b3e540229f8189a2210ae3dd07b4e42130ae6`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Classification:** `NEW SUPPORTING PHYSICAL-BANK COMPILER / FULL TARGET OPEN`.

## 1. Exact scope and correction boundary

The target is the unrestricted conjecture: for every dimension, independent real ORIGINAL coordinates whose one-dimensional probability densities are bounded by one, and every real symmetric ambient matrix with at least three eigenvalues of modulus at least one, prove one universal finite bound on the essential supremum of the density of `Q=X^TAX`, or give a valid counterexample. Continuity is an additional conclusion and is tracked separately.

No Gaussianity, moments, compact support, connected support, log-concavity, iid hypothesis, spectral-coordinate independence, law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea estimate, positive conditional projection-height moment, naive fiber supremum, coefficient-small tail deletion, or one-good-minor assertion is used.

The first early checkpoint of this run explored the `q=4/3` volume-marginal anchor and a raw Laplace expansion. Fresh source comparison then showed that the heavy double-anchor step was already supplied by account03/B08 r26 and the general exterior degree-drop identity by account01/B20. Those steps are therefore dependencies, not claimed as new results here. The new result below begins **after a fixed one-sided nested third-volume packet is already present** and converts it into disjoint physical-coordinate resources with explicit constants.

The designated `account04/B07` current-QFORM handoff/canonical directory was checked fresh at startup and remained absent. No theorem is fabricated or attributed to that slot. A compatible completed account04/B18 product-projection result is applied to an actual inequality in Section 7.

## 2. Sources actually consumed

### 2.1 Fractional third-volume theorem

The newest required volume-stability source is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For an ORIGINAL-coordinate cross block `M`, let

`Z=E_3(M)=sum_{|S|=|T|=3} det M[S,T]^2`.

Under the normalized squared-minor law let `alpha_i` be a row inclusion marginal. If every `alpha_i<=q/2`, `1<=q<3/2`, then the FULL ambient quadratic-plus-affine form has a continuous `C_0` density with

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`.            (2.1)

The same statement holds after transposing the cross block. At `q=4/3`, the gate is `2/3` and the constant is

`(9 sqrt(3)e/2) Z^(-1/6)`.                                      (2.2)

All same-side quadratic terms, outside couplings and affine terms remain present.

### 2.2 Anchored self-matched third-volume theorem

Account03/B08 r27 is

`yspennstate/math-open-problems@e875d54d4a946d399466cb6afa1fc37da12a11d2`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T042303Z-account03-B08-qform-diffuse-r27/REPORT.md`.

For a physical row anchor `i` and column anchor `a`, let `W_ia` be the complete third-minor mass containing both anchors. Under its normalized law, if all residual row inclusion marginals are at most `1/2`, then, writing `R_i` for the anchor-row norm,

`||p_Q||_infinity <=10 sqrt(e) (2W_ia/R_i)^(-1/5)`.             (2.3)

The density is continuous; the transposed statement holds for residual column marginals. Failure of the row gate produces a fixed residual row carrying more than half of `W_ia`.

### 2.3 Existing degree drop, used only as a novelty boundary

Account01/B20 already proved the general exterior identity

`T_k=b Lambda^k(D)-(c wedge)Lambda^(k-1)(D)iota_r`

and its norm descent at

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260923T001711Z-account01-B20-QFORM-auto11/REPORT.md`

(source observed in the current repository snapshot). The present theorem does not rename that identity. It resolves the more specific **two-row/one-column nested packet** into disjoint physical links by a second physical coloring and a two-dimensional Gram argument.

## 3. A fixed nested packet

Let `B` be an ORIGINAL-coordinate cross block between disjoint row and column banks. Fix two distinct physical row coordinates `i,k` and one physical column coordinate `a`. After physical permutations only, write

```
B = [ x   u^T ]
    [ y   v^T ]
    [ c    N  ],                                             (3.1)
```

where `x=B_ia`, `y=B_ka`, `u,v` are coefficient rows on the residual column set `C`, `c` is a coefficient column on the residual row set `R`, and `N=B[R,C]`.

Define the complete one-sided nested third-volume mass

`P=sum_(r in R) sum_(b<d in C)
     det B[{i,k,r},{a,b,d}]^2`.                                (3.2)

For each residual row `r`, Laplace expansion along column `a` gives the exact physical-coordinate identity

`det B[{i,k,r},{a,b,d}]`
` = x(v_b N_rd-v_d N_rb)`
`   -y(u_b N_rd-u_d N_rb)`
`   +c_r(u_b v_d-u_d v_b)`.                                  (3.3)

Put

`A_v=sum_r ||v wedge N_r||_2^2
    =||v||_2^2||N||_F^2-||Nv||_2^2`,                         (3.4)

`A_u=sum_r ||u wedge N_r||_2^2
    =||u||_2^2||N||_F^2-||Nu||_2^2`,                         (3.5)

`Delta^2=||u wedge v||_2^2
       =||u||_2^2||v||_2^2-<u,v>^2`.                         (3.6)

Treating the three terms in (3.3) as vectors in the Hilbert space indexed by `(r,{b,d})`, the triangle inequality yields

`boxed:
 sqrt(P) <= |x| sqrt(A_v)+|y| sqrt(A_u)+||c||_2 Delta.`        (3.7)

Thus at least one of the three displayed summands is at least `sqrt(P)/3`.

## 4. Two physical splitting lemmas

### Lemma 4.1 — star-core wedge splitting

For every real vector `v` on a physical coordinate set `C` and every real matrix `N` with columns indexed by `C`, there is a bipartition

`C=C_1 disjoint_union C_2`                                    (4.1)

such that one of

`||v_{C_1}||_2 ||N[:,C_2]||_F`,
`||v_{C_2}||_2 ||N[:,C_1]||_F`                               (4.2)

is at least

`boxed: sqrt(A_v)/(2sqrt(2)).`                                 (4.3)

#### Proof

Color each coordinate of `C` independently red/blue. Let `S` be the squared wedge mass with the two wedge coordinates in different colors:

`S=sum_r sum_(b in C_1,d in C_2)
       (v_bN_rd-v_dN_rb)^2`.                                  (4.4)

Every unordered pair is separated with probability `1/2`, so `E S=A_v/2`; some coloring has `S>=A_v/2`. For that coloring the cross tensor is

`v_{C_1} tensor N[:,C_2]-N[:,C_1] tensor v_{C_2}`

(up to the harmless indexing order). Hence

`sqrt(S)<=||v_{C_1}|| ||N[:,C_2]||_F
          +||v_{C_2}|| ||N[:,C_1]||_F`.                       (4.5)

One term is at least `sqrt(S)/2>=sqrt(A_v)/(2sqrt(2))`. QED.

The same statement holds with `u` in place of `v`.

### Lemma 4.2 — two-vector area to two disjoint scalar banks

For every two real coefficient vectors `u,v` on `C`, there is a bipartition `C=C_1 disjoint_union C_2` and unit vectors `e,f in R^2` with `f=J^T e`,

`J=[[0,1],[-1,0]]`,                                             (4.6)

such that the physical coefficient vectors

`w_1=e_1 u_{C_1}+e_2 v_{C_1}`,
`w_2=f_1 u_{C_2}+f_2 v_{C_2}`                                 (4.7)

obey

`boxed: ||w_1||_2 ||w_2||_2 >= Delta/2.`                       (4.8)

#### Proof

Under an independent two-coloring, the separated wedge mass

`S=sum_(b in C_1,d in C_2)(u_bv_d-v_bu_d)^2`                   (4.9)

has expectation `Delta^2/2`, so choose a partition with `S>=Delta^2/2`.

Let `G_1,G_2` be the `2x2` Gram matrices of `(u_{C_1},v_{C_1})` and `(u_{C_2},v_{C_2})`. Direct expansion gives

`S=tr(G_1 J G_2 J^T)`.                                        (4.10)

Diagonalize the positive semidefinite matrix `G_1` with orthonormal eigenvectors `e_1,e_2`. Since

`S=sum_(j=1)^2 lambda_j e_j^T(JG_2J^T)e_j`,                   (4.11)

one term is at least `S/2`. Choose its eigenvector `e`. Then

`||w_1||^2=e^TG_1e`,
`||w_2||^2=(J^Te)^TG_2(J^Te)=e^TJG_2J^Te`,                    (4.12)

so

`||w_1||^2||w_2||^2>=S/2>=Delta^2/4`.                         (4.13)

Taking square roots proves (4.8). QED.

The important point is that `w_1,w_2` are linear forms in **disjoint original-coordinate subbanks**, not spectral coordinates.

## 5. Main new compiler

### Theorem 5.1 — `QFORM-NESTED-THIRDVOLUME-TO-DISJOINT-LINKS-v1`

For the fixed nested packet (3.2), at least one of the following occurs.

**E — edge-star-core physical packet.** There is a choice of one anchor edge (`x` with star `v`, or `y` with star `u`) and a physical bipartition `C=C_1 disjoint_union C_2` such that, after possibly swapping the two colors,

`boxed:
 |edge| * ||star_{C_1}||_2 * ||N[:,C_2]||_F
 >= sqrt(P)/(6sqrt(2)).`                                      (5.1)

The scalar edge, star support and core row/column supports are mutually disjoint physical-coordinate objects.

**S — three disjoint linear banks.** There is a physical bipartition `C=C_1 disjoint_union C_2` and coefficient vectors `w_1,w_2` as in Lemma 4.2 such that

`boxed:
 ||c||_2 ||w_1||_2 ||w_2||_2 >= sqrt(P)/6.`                   (5.2)

The three random scalar projections `c^T X_R`, `w_1^T X_{C_1}`, `w_2^T X_{C_2}` are genuinely independent because their ORIGINAL-coordinate supports are disjoint.

#### Proof

By (3.7), one of

`|x|sqrt(A_v)`, `|y|sqrt(A_u)`, `||c||Delta`                  (5.3)

is at least `sqrt(P)/3`.

If the first term wins, apply Lemma 4.1 to `(v,N)` and multiply (4.3) by `|x|`; this gives (5.1). The second term is identical with `(u,y)`.

If the third term wins, apply Lemma 4.2 and multiply (4.8) by `||c||`; this gives (5.2). QED.

This compiler is dimension-free, involves no reciprocal local determinant, and retains an aggregate packet until it has been converted into disjoint physical banks.

## 6. Application to the current high-tail route

Let `M` be the current B07 cross block and `Z=E_3(M)>0`. Use the `q=4/3` theorem (2.2).

If all row third-volume marginals are at most `2/3`, or all column marginals are at most `2/3`, the full ambient density is already continuously paid by (2.2).

Otherwise choose a physical row `i` and column `a` with marginal probabilities both greater than `2/3`. Their double-incident packet obeys

`W_ia/Z=P(i in S,a in T)>1/3`,

so

`W_ia>Z/3`.                                                     (6.1)

If the anchored residual row marginals are all at most `1/2`, apply account03/B08 r27 (2.3); if the anchored residual column marginals are all at most `1/2`, apply its transposed theorem. Hence every state escaping both paid branches has a residual row `k` included with conditional probability `>1/2`. The fixed one-sided nested packet containing rows `i,k` and column `a` then has

`boxed: P>W_ia/2>Z/6.`                                        (6.2)

Apply Theorem 5.1 to this literal physical packet. It yields either

`boxed:
 |edge| * ||star|| * ||core||_F > sqrt(Z)/(12sqrt(3))`         (6.3)

or

`boxed:
 ||c|| ||w_1|| ||w_2|| > sqrt(Z)/(6sqrt(6)).`                 (6.4)

These are physical aggregate alternatives; no single 3x3 or 2x2 determinant is chosen.

### High-tail scale

The completed B07 r22 scale lemma states that if

`T=sum_(j>=3)s_j(M)^2 >= theta ||M||_F^2`, `0<theta<=1/2`,     (6.5)

then, writing `F=||M||_F`,

`Z=E_3(M)>=theta^2 F^6/6`.                                    (6.6)

Therefore (6.3)-(6.4) sharpen to

`boxed:
 |edge| * ||star|| * ||core||_F > theta F^3/(36sqrt(2))`       (6.7)

or

`boxed:
 ||c|| ||w_1|| ||w_2|| > theta F^3/36.`                       (6.8)

If this high-tail state also comes from the r22 four-bank packet `CRF>kappa` and the large-star exit `CR>Lambda` has failed, then `F>kappa/Lambda`, hence

`|edge| ||star|| ||core||_F
 > theta kappa^3/(36sqrt(2)Lambda^3)`,                         (6.9)

or

`||c|| ||w_1|| ||w_2||
 > theta kappa^3/(36 Lambda^3)`.                               (6.10)

For the concrete r22 values

`theta=1/16`, `Lambda=1`, `kappa=1/(256sqrt(3))`,              (6.11)

the two lower bounds are respectively

`1.40818832947e-11`, `1.99147903391e-11`.                      (6.12)

The constants are intentionally not optimized; the point is a universal physical-bank floor after aggregate selection.

### Paid anchored branch on the same scale

For completeness, if the B08 anchored theorem fires, use `R_i<=F`, `W_ia>Z/3` and (6.6):

`2W_ia/R_i > theta^2 F^5/9`.

Thus that branch has the explicit continuous-density bound

`boxed:
 ||p_Q||_infinity
 <10sqrt(e) 9^(1/5) theta^(-2/5) F^(-1).`                    (6.13)

The global fractional-volume branch similarly has

`||p_Q||_infinity
 <=(9sqrt(3)e/2)(6/theta^2)^(1/6)F^(-1)`.                    (6.14)

## 7. Completed account04 mathematics applied to a new actual inequality

The designated `account04/B07` source remains absent, so no result is invented. Use the compatible completed account04/B18 sharp product-projection consequence from

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`:

for every coefficient vector `q` on an original-coordinate cap-one product bank,

`||p_(q^T X)||_infinity <=sqrt(2)/||q||_2`.                   (7.1)

On Theorem 5.1(S), the three supports `R,C_1,C_2` are disjoint, so the three scalar projections are genuinely independent. Multiplying their one-dimensional caps and using (6.8) gives the ACTUAL three-dimensional coefficient-plane estimate

`boxed:
 ||p_(c^T X_R, w_1^T X_C1, w_2^T X_C2)||_infinity
 <72sqrt(2)/(theta F^3).`                                     (7.2)

If `F>kappa/Lambda`,

`boxed:
 ||p_(c^T X_R, w_1^T X_C1, w_2^T X_C2)||_infinity
 <72sqrt(2)Lambda^3/(theta kappa^3).`                          (7.3)

At (6.11), the numerical cap is

`1.420264575514062e11`.                                       (7.4)

This very large number is still dimension-free. More importantly, (7.2) is **only product-linear provenance**. It is not promoted to a density estimate for an arbitrary indefinite curved quadratic pushforward; the correction ledger explicitly forbids that shortcut.

## 8. What changed and what remains

This run does not prove the full conjecture. It does close one structural step left by the high-tail/double-nested route: a fixed two-row/one-column third-volume nest can no longer remain an undifferentiated determinant packet. It must descend to one of two explicit product-preserving physical geometries:

1. a scalar edge times a disjoint star times a disjoint physical Frobenius core, (5.1); or
2. three genuinely independent original-coordinate scalar banks with product norm bounded below, (5.2).

The first unpaid implication is now

`QFORM-NESTED-LINK-CURVATURE-RECEIVER-v1`:

> consume (6.7) or (6.8) in the **full ambient form**, retaining arbitrary same-bank curvature, the unused anchor couplings, and all additional spectrum; or route them into an already-paid physical-pair, mixed-hub, grouped-square, gapped scalar-compression, ridge, or second-volume endpoint.

A bounded joint density of the three scalar projections by itself is not enough. The edge-star-core branch still needs a curved receiver, and the three-scalar branch needs an actual gapped compression or another dependence-safe kernel.

The low-tail genuine rank-one tube from B07 r23 remains a separate debt; account01/B08's robust recoloring theorem gives important conditional exits but does not remove all of its child-window hypotheses.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Full-target continuity remains OPEN.** Continuity is proved only on the fractional-volume and anchored self-matched branches invoked above.

## 9. Checks

`CHECKS.py` and captured `CHECKS.txt` beside this report test 200 deterministic random finite instances of:

- the exact nested determinant expansion and inequality (3.7);
- the physical separated-wedge lower bound used in Lemma 4.1;
- the two-dimensional Gram product lower bound in Lemma 4.2;
- the concrete collar constants (6.12) and partner cap (7.4).

The captured output ends `QFORM_B07_R25_CHECK_PASS`. These checks verify algebra/constants only; the proof is Sections 3-7.

## 10. Review status

`QFORM-NESTED-THIRDVOLUME-TO-DISJOINT-LINKS-v1`: proved in this run, not independently reviewed.  
Fractional-volume theorem: consumed at stated scope; its source labels independent review pending.  
Account03/B08 r27 anchored theorem: consumed at stated scope; no review status upgraded here.  
Full theorem: OPEN; no end-to-end review requested or claimed by this report.
