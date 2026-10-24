SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T11:19:16Z.
attacking: integrated Fourier estimate — sharpen the common-anchor incident-(3+2) transport failure into a unique nested near-coloop or an exact-rank-three physical slice, while applying account02/B02's current transport compiler at an actual inequality.

# account01/B02 r28 — star-collision support collapse after the common-anchor transport receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the explicit `phi_Q in L1` exits below; unrestricted continuity remains open.  
**Target-wide universal Fourier-L1:** `OPEN_NOT_REFUTED`.

The target is unchanged: independent ORIGINAL real coordinates with probability densities at most one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moments, compact/connected support, Gaussianity, log-concavity, iid assumption, or independence after a spectral rotation is used.

## 1. Current designated-partner theorem actually used

The newest completed designated partner result I use is account02/B02

`QFORM-INCIDENT32-DISJOINT-TRANSPORT-L1-v1`,

at

`yspennstate/math-open-problems@<partner-report-readback-current-master>`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T100819Z-account02-B02-qform-r11/REPORT.md`.

Its canonical report blob is `aa85a320ce54c90b1929ab1a5fd5b90d89746bbf`. The preceding account02/B02 cross-disjoint run is pinned at commit `94189deb89884b0dd57057041ec04f98a85e6764`.

Let `B=A[I,J]` be an ORIGINAL-coordinate cross block. In the live two-sided D' failure collar, choose outer physical row/column anchors `x,y`. Put

`Z3=E3(B)=e3(B^T B)`

and let `J3` be the incident third-minor mass through `(x,y)`. The partner proves

`J3 > Z3/3`.                                                    (1.1)

Let `N=B[I\{x},J\{y}]`, `E2=e2(N^T N)`. Failure of its first incident-(3+2) disjointness exit at the stated threshold supplies a physical residual row/column anchor `(i,j)` with

`H=H2^(i,j)(N) > 7 E2/32`.                                     (1.2)

The newest partner transport theorem says that, after conditioning the incident residual-row-pair law on avoiding `i`, if the exact weighted Hall conditions for a disjoint coupling with the anchored-H companion-row law hold and the incident anchor marginal obeys `p_i<=3/4`, then

`||p_Q||inf <17.659639 (Z3 E2)^(-1/10)`.                       (1.3)

Tracking its same explicit Fourier envelope gives

`integral_R |phi_Q(t)| dt <110.958781 (Z3 E2)^(-1/10)`.       (1.4)

The density is continuous and vanishes at infinity. The transpose gives the analogous column-side exit.

The same partner theorem also supplies the independent anchored-product disjointness compiler: if

`delta_r^H=P(R3 cap {i,K}=empty)>0`,                            (1.5)

then

`||p_Q||inf <=5e 2^(-1/5) (delta_r^H J3 H)^(-1/10)`,           (1.6)

and the Fourier integral is exactly `2pi` times the right side. This is the partner result applied below at a new concrete threshold.

## 2. Normalize the remaining row-side star

Assume

`p_i=P(i in R3)<=3/4`.                                         (2.1)

Let `bar_mu` be the incident residual-row-pair law conditioned on `i notin R3`. Its total determinant mass is

`Jbar_i=(1-p_i)J3 >= J3/4 > Z3/12`.                            (2.2)

A sample `R` under `bar_mu` is a two-element physical row set. Define

`u_r=P_bar_mu(r in R)`,                                        (2.3)

so

`sum_r u_r=2`.                                                  (2.4)

Under the anchored-H determinant law, every row pair is `{i,K}` for one far physical row `K`. Let

`v_r=P(K=r)`, `sum_r v_r=1`.                                   (2.5)

The conditional independent star-disjointness probability is

`delta_i^* = P_bar_mu x v(K notin R)
           = sum_r v_r(1-u_r)`.                                (2.6)

Because the raw partner event requires both `i notin R3` and `K notin R3`,

`delta_r^H=(1-p_i) delta_i^*`.                                 (2.7)

This is an exact identity, not an inequality.

## 3. New support-collapse lemma

### Lemma 3.1 — `QFORM-STARCOLLISION-UNIQUE-NEARCOLOOP-v1`

Let `u=(u_r)` be inclusion probabilities of a law on two-element subsets, so `sum u_r=2`, and let `v=(v_r)` be a probability law on singleton labels. Suppose

`delta=sum_r v_r(1-u_r)<eta`,                                  (3.1)

where `0<eta<1/9`. Define

`G={r: u_r>1-sqrt(eta)}`.                                      (3.2)

Then:

1. `v(G)>1-sqrt(eta)`;
2. `1<=|G|<=2`;
3. if `G={r1,r2}`, then
   `P(R={r1,r2})>1-2sqrt(eta)`;
4. if `G={r}`, then simultaneously
   `u_r>1-sqrt(eta)` and `v_r>1-sqrt(eta)`.

#### Proof

For every `r notin G`, `1-u_r>=sqrt(eta)`. Therefore

`delta >= sqrt(eta) sum_(r notin G) v_r
       = sqrt(eta) v(G^c)`,                                    (3.3)

and (3.1) gives `v(G^c)<sqrt(eta)`, proving item 1 and nonemptiness.

Since `eta<1/9`, every member of `G` has `u_r>2/3`. Three such members would give `sum u_r>2`, contradicting (2.4). Thus `|G|<=2`.

If `G={r1,r2}`, inclusion--exclusion for the events `{r1 in R}`, `{r2 in R}` gives

`P(r1,r2 in R)>=u_r1+u_r2-1>1-2sqrt(eta)`.                    (3.4)

Because `R` has exactly two elements, `{r1,r2 subset R}` is exactly `{R={r1,r2}}`. This proves item 3. If `G` is a singleton, item 1 says its `v`-mass is `>1-sqrt(eta)`, while membership in `G` gives the same lower bound for `u`; item 4 follows. QED.

This is a purely finite probability statement on determinant-weighted physical subsets. It rotates no random variables and selects no reciprocal minor.

## 4. Concrete `1/64` trichotomy and a new exact-rank-three L1 exit

Apply the partner independent-disjointness theorem at the concrete raw threshold

`delta_r^H >= 1/64`.                                           (4.1)

Using (1.1)--(1.2),

`delta_r^H J3 H
 > (1/64)(Z3/3)(7E2/32)
 = 7 Z3 E2/6144`.                                              (4.2)

Thus the designated partner theorem gives the actual new live bound

`boxed:
 ||p_Q||inf <23.302033 (Z3 E2)^(-1/10),
}`                                                              (4.3)

and

`boxed:
 integral_R |phi_Q(t)|dt <146.410989 (Z3 E2)^(-1/10).
}`                                                              (4.4)

This is a genuine unweighted Fourier-L1 estimate, hence gives a continuous `C_0` density.

Now suppose instead

`delta_r^H<1/64`.                                               (4.5)

By (2.1) and (2.7),

`delta_i^* < (1/64)/(1/4)=1/16`.                               (4.6)

Apply Lemma 3.1 with `eta=1/16`. Then

`G={r:u_r>3/4}`, `v(G)>3/4`, and `1<=|G|<=2`.                  (4.7)

### Case A: `|G|=2`

Write `G={r1,r2}`. Lemma 3.1 gives

`P_bar_mu(R={r1,r2})>1/2`.                                    (4.8)

Consequently the physical three-row block

`C=B[{x,r1,r2},J]`                                             (4.9)

carries third exterior volume

`E3(C) > Jbar_i/2
       >=J3/8
       >Z3/24`.                                                 (4.10)

Use the completed exact-rank-three physical-cross-block theorem

`QFORM-EXACT-RANK3-CROSSBLOCK-FOURIER-v1`,

source

`yspennstate/math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T230126Z-account03-B02-QFORM-r17/REPORT.md`.

Because `C` has exactly three physical rows and `E3(C)>0`, it has exact rank three and the squared product of its three nonzero singular values equals `E3(C)`. Therefore

`boxed:
 integral_R |phi_Q(t)|dt
 <12pi 24^(1/6) Z3^(-1/6)
 <64.028 Z3^(-1/6),
}`                                                              (4.11)

and

`boxed:
 ||p_Q||inf
 <6 24^(1/6) Z3^(-1/6)
 <10.191 Z3^(-1/6).
}`                                                              (4.12)

Again the density is continuous and vanishes at infinity. This is the essential new Fourier implication: a two-row collision in the conditional star is not an unpaid bounded-width obstruction; it is already an exact-rank-three physical slice.

### Case B: `|G|=1`

Let `G={r}`. Then

`u_r>3/4`, `v_r>3/4`.                                          (4.13)

Thus a **unique common nested near-coloop row** survives. It has explicit scale on both determinant packets:

`incident restricted third volume through r
 =u_r Jbar_i
 > (3/4)(J3/4)
 =3J3/16
 >Z3/16`,                                                       (4.14)

and

`H_r=v_r H
 >(3/4)H
 >21E2/128`.                                                    (4.15)

No averaging over an unbounded set of possible companion rows remains.

Combining Sections 1 and 4 proves the row-side trichotomy:

* if the exact Hall transport passes, use (1.3)--(1.4);
* if Hall fails but `delta_r^H>=1/64`, use (4.3)--(4.4);
* if `delta_r^H<1/64`, either the exact-rank-three L1 exit (4.11)--(4.12) applies, or one unique row satisfies (4.13)--(4.15).

The transpose gives the identical column-side trichotomy.

## 5. Double-singleton endpoint

Suppose both row and column sides reach their singleton survivors, say far row `r` and far column `s`. Under the **same anchored-H squared-minor law**,

`P(K=r)>3/4`, `P(L=s)>3/4`.                                    (5.1)

Inclusion--exclusion gives

`P(K=r,L=s)>1/2`.                                               (5.2)

But each anchored-H atom is exactly the squared physical minor

`det N[{i,K},{j,L}]^2/H`.                                      (5.3)

Hence the literal residual physical minor satisfies

`boxed:
 det N[{i,r},{j,s}]^2 > H/2 >7E2/64.
}`                                                              (5.4)

This improves the preceding bounded-width certificate, but I retain it only as **scale currency**. The live correction `QFORM-CROSSMINOR-ALONE-FALSE` forbids the invalid inference that one good cross minor alone solves the full symmetric quadratic problem.

The simultaneous survivor additionally carries the row-side volume currency (4.14) and its transposed column analogue. Thus the unpaid collar is now a genuinely nested, finite physical configuration rather than a two-row/two-column ambiguity.

## 6. What changed relative to the preceding B02 run

The preceding account01/B02 r27 left, after small star-disjointness, “at most two” common companion rows and columns. The new Lemma 3.1 distinguishes those possibilities sharply:

* **two** common rows imply a fixed physical row triple carrying a universal fraction of `Z3`, and are therefore paid by the exact-rank-three Fourier theorem;
* **one** common row is a unique near-coloop simultaneously for the incident third-volume law and the anchored residual second-volume law.

Using the newest account02/B02 transport theorem before this split also pays every low-entropy disjoint-coupling case with the stronger live bound (1.3). Therefore the remaining row-side obstruction is not generic Hall failure or generic two-row concentration: it is either the partner's `p_i>3/4` anchor-heavy state or the unique nested near-coloop (4.13)--(4.15). The same is true on columns.

## 7. Correction audit

The derivation does not use any refuted premise:

* no law-uniform pointwise quadratic-phase decay;
* no independence after spectral rotation;
* no arbitrary-joint coarea density bound;
* no conditional-density cap after a sum/difference transform;
* no deletion of a small coefficient tail on unbounded laws;
* no inference from one physical cross minor to a full theorem;
* no Monte Carlo or interval-extremality claim.

The exact-rank-three step uses a literal ORIGINAL-coordinate three-row cross block and retains all same-bank terms and outside couplings, exactly within its cited scope.

## 8. Remaining implication

The first unpaid interface is now

`QFORM-NESTED-INCIDENT-E2-NEARCOLOOP-RECEIVER-v1`.

In the common-anchor packet, after all Fourier exits above, one must pay configurations in which either

1. the inner incident anchor itself has `p_i>3/4` (and/or its column analogue), or
2. there is a **unique** far row `r` with both `u_r,v_r>3/4`, carrying simultaneously `>Z3/16` incident third-volume scale and `>21E2/128` anchored-H scale, with the analogous column state.

When both singleton states occur, (5.4) gives an actual four-coordinate cross-minor scale `>7E2/64`, but the missing operation is still a product-preserving TRUE pair/scalar-Schur, grouped-star, ridge, or mixed-hub receiver that can use this finite nested structure without pretending cross-only Schur algebra is a full symmetric Schur complement.

I found no source-valid counterexample to the stronger target-wide statement

`integral_R |E exp(it X^T A X)|dt <= C`.

Accordingly universal Fourier-L1 remains `OPEN_NOT_REFUTED`; the unrestricted bounded-density conjecture and unrestricted continuity conclusion also remain OPEN.

## 9. Status

`ESSENTIAL_STEP_APPLIED`. The result is a quantitative structural/Fourier improvement on the live common-anchor collar, not a full solution. It applies the current designated partner account02/B02 result at (1.3)--(1.6) and (4.2)--(4.4), and converts the previous two-support star-collision branch into a genuine exact-rank-three L1 theorem.
