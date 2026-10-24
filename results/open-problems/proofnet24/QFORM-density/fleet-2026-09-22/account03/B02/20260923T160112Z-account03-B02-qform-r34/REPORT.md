SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T16:01:12Z.
attacking: pay the remaining one-sided strip and low-rank double-anchor packets by a product-preserving integrated-Fourier receiver, then apply one account04/B02 result to a new inequality.

# account03/B02 r34 — strong-cut low-tail stable rank compiles to Fourier L1 or a fixed-scale heavy anchor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Control refreshed before publication:** owner revision `2026-09-22.15`, QFORM only  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository retrieval/write occurred, but no native learned-memory ingestion was verified  
**Full QFORM target:** **OPEN**  
**Target-wide universal unweighted Fourier L1 criterion:** **OPEN / not refuted**  
**Continuity:** proved on the L1 branches below; full-target continuity remains open.

## 1. Exact source-pinned inputs

The newest completed designated-partner result actually applied in this run is account04/B02,

`yspennstate/math-open-problems@782125ea5050ded274e68cae768cde540fbaa3c7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260923T151038Z-account04-B02-QFORM-r1/REPORT.md`.

Its theorem `QFORM-N3-STRONGCUT-D5-OR-HY-v1` works on the fleet's `N3(1/64)` strong-cut branch. It produces an ORIGINAL-coordinate physical cross block `M=A[J,K]` with

`E:=||M||_F^2 > c0:=11907/16384`,                                      (1.1)

and, after its already-paid D5 and optimized-HY exits, leaves only four structural alternatives. In the specific **low tail stable-rank** alternative treated here, if `x1>=x2>=...` are the squared singular values of the same literal block `M`, then

`S4:=x1+x2+x3+x4 > (63/64)E`,                                          (1.2)

`x2 >= E/64`,                                                           (1.3)

`T2:=sum_(r>=3) x_r >= E/64`,                                          (1.4)

and

`R_tail:=T2/x3 < 225`.                                                  (1.5)

No singular-vector coordinates are declared independent; (1.1)-(1.5) are deterministic facts about one physical cross block.

The integrated-Fourier compiler used next is my completed `QFORM-E3-MARGINAL-OVERLOAD-ANCHOR-COMPILER-v1`,

`yspennstate/math-open-problems@cb55a355bc5c623eb5a98c1db8a0ebaa58ff1027`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T125927Z-account03-B02-qform-r30/REPORT.md`.

For every physical cross block `B` with `Z=E3(B)>0` and every `1<q<3/2`, it gives either

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`                    (1.6)

with `phi_Q in L1`, or an actual physical row/column anchor whose joint incident third-volume `J` satisfies

`J>(q-1)Z`.                                                             (1.7)

For a nonzero anchor edge `a`, the exact identity is `J=a^2 E2(S)` for the algebraic cross-Schur residual `S`; for a zero edge, (1.7) is converted directly to the inverse-free two-star/transverse packet. The proof of (1.6) is the reviewed original-coordinate sharp Hausdorff--Young / Brascamp--Lieb argument and retains arbitrary same-bank terms and outside couplings.

For the nonzero-edge rank-at-least-three descent I also use my r32 theorem

`yspennstate/math-open-problems@3cc1145d1fb015deed33085d536db7156d918225`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T142846Z-account03-B02-qform-r32/REPORT.md`,

and the r33 H2-to-H3-or-strips compiler

`yspennstate/math-open-problems@604b3273a6db312558088b7ed2a9d9735c546e7a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T150032Z-account03-B02-qform-r33/REPORT.md`.

## 2. New deterministic bridge: low tail stable rank forces third exterior volume

Define

`Z:=E3(M)=e3(x1,x2,...)`.                                             (2.1)

The partner's survivor inequalities imply three explicit lower bounds. From (1.2),

`x1 >= S4/4 > 63E/256`.                                               (2.2)

From (1.3),

`x2 >= E/64`.                                                         (2.3)

Finally, (1.4)-(1.5) give

`x3=T2/R_tail > T2/225 >= E/14400`.                                  (2.4)

Since every term in `e3(x)` is nonnegative,

`Z >= x1 x2 x3
   > [63/(256*64*14400)]E^3
   = [7/26214400]E^3`.                                                (2.5)

Thus the allegedly difficult low-tail-stable-rank survivor is not third-volume-poor. It carries the universal physical third-volume floor

`boxed: Z > zeta E^3,  zeta=7/26214400.`                              (2.6)

Using `E>c0`,

`Z > Z0 := (7/26214400)c0^3
          = 1.0249563279271686e-7.`                                  (2.7)

This implication is purely spectral algebra on the actual source-coordinate cross block. No perturbation, minor inversion, or rotated product law is used.

## 3. Main theorem — `QFORM-STRONGCUT-LOWTAILSTABLERANK-TO-L1-OR-HEAVYANCHOR-v1`

Apply the r30 compiler (1.6)-(1.7) to this exact `M` with the convenient rational choice

`q=10/7`.                                                             (3.1)

Then `q-1=3/7`, `3-2q=1/7`, and exactly one of the following holds.

### (F) Continuous-density integrated-Fourier exit

The characteristic function belongs to `L1(R)` and

`||p_Q||_infinity
 <=21 e sqrt(7/10) Z^(-1/6)`.                                        (3.2)

Using (2.6),

`||p_Q||_infinity
 <21 e sqrt(7/10)(26214400/7)^(1/6) E^(-1/2)`.                       (3.3)

Using (1.1),

`boxed: ||p_Q||_infinity < 698.144365.`                               (3.4)

The underlying Fourier proof gives the explicit unweighted integral estimate

`boxed: integral_R |phi_Q(t)| dt < 4386.570412.`                      (3.5)

Therefore this branch has a continuous density vanishing at infinity.

### (H) Fixed-scale physical heavy anchor

There are an actual original-coordinate row and column for which

`J > (3/7)Z
   > [3/26214400]E^3`.                                                (3.6)

Numerically, using (1.1),

`boxed: J > 4.3926699768307224e-8.`                                  (3.7)

This is a new scale transfer from the designated partner's low-tail-stable-rank branch into the previously developed heavy-anchor machinery. It does not choose a reciprocal tiny minor.

### Proof

Equation (2.6) establishes `Z>0`. The r30 theorem is therefore applicable to the same physical block. Substitute `q=10/7` in its exhaustive alternatives. In the Fourier alternative, simplify

`3e/[(3-20/7)sqrt(10/7)] = 21e sqrt(7/10)`.

Then insert (2.6) and (1.1), proving (3.2)-(3.4). The r30 source is an actual `L1` characteristic-function theorem; its inversion computation has `integral|phi|` equal to at most `2pi` times the right-hand side in (3.2), which yields (3.5). In the complementary alternative, insert `q-1=3/7` and (2.6), proving (3.6)-(3.7). QED.

## 4. What the heavy branch already buys

Write the heavy anchor block as

`M=[[a,r^T],[c,N]]`.                                                  (4.1)

### 4.1 Zero anchor edge

If `a=0`, the exact r30 joint-star compiler gives directly

`||c||^2||r||^2
 ||P_(c^perp) N P_(r^perp)||_F^2
 >= J
 > [3/26214400]E^3`.                                                 (4.2)

Thus the low-tail branch reaches a fixed-scale inverse-free two-star packet.

### 4.2 Nonzero anchor, exact rank-two Schur residual

If `a!=0`, set

`S=N-c r^T/a`; then `J=a^2E2(S)`.                                     (4.3)

If `rank(S)=2`, the completed grouped Schur L1 theorem gives

`||p_Q||_infinity <=3e^(2/3)J^(-1/6)`.                              (4.4)

Together with (3.6) and (1.1),

`boxed: ||p_Q||_infinity < 98.370033.`                                (4.5)

Again `phi_Q in L1`, so this subbranch is continuous.

### 4.3 Nonzero anchor, rank at least three

For `rank(S)>=3`, apply r32. Its mixed-volume Fourier alternative gives

`||p_Q||_infinity
 <=25.628206855 |a|^(1/5)J^(-1/5)`.                                 (4.6)

Because `a` is an entry of the same physical block `M`, `|a|^2<=E`. Combining this with (3.6) gives

`||p_Q||_infinity
 <25.628206855(26214400/3)^(1/5)E^(-1/2)`,                         (4.7)

hence, by (1.1),

`boxed: ||p_Q||_infinity < 735.039617.`                               (4.8)

This is another genuine L1 branch.

If the r32 Fourier gate fails, it yields one of the following fixed-scale packets:

`two-star/transverse >= J/4 > [3/(4*26214400)]E^3`,                   (4.9)

`double-anchor G3 > J/8 > [3/(8*26214400)]E^3`,                      (4.10)

or the residual H2 packet. The r33 exact algebra then compiles H2 into a double-anchor/strip trichotomy

`max{G3,U,V} > J/288
            > E^3/2516582400`.                                        (4.11)

Using (1.1), every packet in (4.11) is in fact greater than

`1.525232630844001e-10`.                                             (4.12)

Whenever the r33 invertible double-anchor residual has stable rank at least `5/2`, its determinant-cancelling pair/D5 estimate pays (4.10) by

`||p_Q||_infinity < 372.968286`,                                     (4.13)

and pays a `G3` alternative from (4.11) by

`||p_Q||_infinity < 677.728352`.                                     (4.14)

Both are L1/continuous branches. The remaining pieces are exactly the low-stable-rank double-anchor collar and the one-sided strip/two-star packets; importantly, on the partner's low-tail branch these now occur at a fixed absolute packet scale rather than at an arbitrarily small inherited scale.

## 5. Designated partner result applied at an actual inequality

The account04/B02 theorem is not merely cited. Its low-tail survivor data (1.1)-(1.5) are inserted directly into (2.2)-(2.5):

`S4>63E/64`, `x2>=E/64`, `T2>=E/64`, `T2/x3<225`

`=> x1>63E/256`, `x3>E/14400`

`=> E3(M)>7E^3/26214400`.                                           (5.1)

Equation (5.1) is the new receiver inequality. Feeding it into the r30 integrated-Fourier theorem yields the universal branch (3.4)-(3.5) and, on failure, the fixed-scale physical packet (3.6). Thus one complete account04/B02 result was applied to an actual quantitative inequality exactly as required.

## 6. Finite computation check

A seeded diagnostic sampled 200,000 random nonnegative singular-value spectra of dimensions 5 through 12, normalized to `E=1`. Among them, 41,476 satisfied the partner survivor conditions (1.2)-(1.5). The smallest observed ratio `E3/E^3` was

`0.0002523055788836741`,

whereas the proved floor (2.6) is

`7/26214400 = 0.00000026702880859375`.

So the numerical regression had zero violations and minimum observed slack factor about `944.8628`. This computation is only corroboration; the proof is the three-line deterministic argument (2.2)-(2.5).

## 7. Correction boundary and exact remaining obligation

This run does **not** prove that every target matrix lies in the partner's low-tail-stable-rank subbranch, and it does not claim the full theorem. The partner's other surviving strong-cut geometries (near rank one, near rank two, and double physical hub) remain for their assigned workers/receivers.

Within the low-tail-stable-rank subbranch, the formerly vague case is now reduced to:

1. a universal continuous-density Fourier exit (3.4), or
2. an exact-rank-two universal continuous-density exit (4.5), or
3. the rank-at-least-three mixed Fourier exit (4.8), or
4. a fixed-scale inverse-free two-star/strip packet, or
5. a fixed-scale low-stable-rank double-anchor packet.

The next B02 implication is therefore `QFORM-FIXEDSCALE-STRIP-OR-LOWRANK-DOUBLEANCHOR-RECEIVER-v1`: spend the packets in (4.2), (4.9), and (4.11) by a product-preserving grouped-strip/fractional-Fourier mechanism without deleting small singular directions, choosing a reciprocal tiny minor, or assuming independence after a Schur shear.

The live source corrections are respected: no law-uniform pointwise van der Corput decay, no post-rotation independence, no arbitrary-joint coarea theorem, no fiberwise supremum dimension-free step, no worst conditional density cap, and no deletion of a small matrix tail on unbounded inputs.

**New result:** `QFORM-STRONGCUT-LOWTAILSTABLERANK-TO-L1-OR-HEAVYANCHOR-v1`.  
**Full target:** OPEN.  
**Target-wide universal unweighted Fourier L1:** OPEN / not refuted.  
**Full-target continuity:** OPEN.