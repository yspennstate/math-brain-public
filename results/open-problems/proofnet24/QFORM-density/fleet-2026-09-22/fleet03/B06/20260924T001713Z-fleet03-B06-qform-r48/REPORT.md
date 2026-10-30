SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-24T00:17:13Z.
attacking: QFORM-SHEARFLAT-HEAVYHUB-PIVOT-COMPILER-v1; keep the complete curved/shear geometry through one heavy original-coordinate pivot, aggregate the post-pivot pair area before inversion, and isolate the exact rank-one resonance that can be paid by a product-Fresnel receiver.

# fleet03/B06 r48 — heavy-hub pivot compiler inside the shear-flat normal form

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** `2026-09-22.15`; programme revision `2026-09-22.5`  
**Assignment:** curved fiber integration / quantitative inequalities and rigorous computations  
**Status:** `NEW TARGET-LEVEL CONDITIONAL COMPILER + RANK-ONE RESONANCE PAYMENT + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN. No Gaussian, log-concavity, moment, bounded-support, connected-support, iid, diagonal-basis, or post-rotation-independence assumption is added. Every conditioning/pivot below uses literal original coordinates. The main branch below proves absolute continuity and an `L^infinity` bound; it does not prove continuity. The rank-one resonance branch does give a continuous `C_0` density through an existing mixed-Fresnel theorem.

## 1. Fresh source boundary and live correction boundary


- law-uniform pointwise Fresnel decay for arbitrary cap-one fragmented laws;
- independence after spectral rotation;
- arbitrary-joint quadratic coarea;
- positive moments of worst conditional projection-density heights;
- unrestricted integration of curved-fiber suprema;
- deletion of a nonzero quadratic tail;
- the refuted critical rank-one same-bank half-Riesz endpoint.

The immediate B06 predecessor is

`yspennstate/math-open-problems@fcd44d39858e562272e44a586a458f38776fea2e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T232257Z-fleet03-B06-qform-r47/REPORT.md`.

That run proved the exact shear-flat normal form described next.

## 2. Starting point: exact two-hub shear-flat normal form

Split the literal original coordinates into two physical hub coordinates and an environment bank `L`:

`A = [[H,E],[E^T,C]]`,                                             (2.1)

where `H` is real symmetric `2 x 2`, invertible, `E` is `2 x m`, and `C` is `m x m`. Put

`delta = det H != 0`,                                               (2.2)

and assume the r47 shear-flat conclusion

`S := C-E^T H^(-1)E = D+E^T T E`,                                  (2.3)

where `D` is diagonal and `T` is symmetric `2 x 2`. This is an exact identity in original coordinates, not a rotation of the random input.

Write

`G=E E^T`, `W=det G`.                                               (2.4)

The branch of interest has `rank E=2`, so `W>0`.

For one environment coordinate `h`, write its column of `E` as `e=e_h in R^2`, its diagonal entry in `D` as `d0=D_hh`, and define the physical two-frame leverage

`alpha=e^T G^(-1)e`.                                                (2.5)

The r47 low-disjointness obstruction produces a literal heavy coordinate with `alpha>3/5`; the algebra below is valid for every `alpha<1` and is then applied to that heavy branch.

Define the scalar Schur pivot of the residual at `h` by

`s = S_hh = d0+e^T T e`.                                           (2.6)

The first essential missing implication is to keep the complete nonzero tail after pivoting this physical coordinate and then aggregate the remaining rank-two shear area before invoking any reciprocal minor.

## 3. Exact heavy-hub pivot identities

Delete column `h` from `E` and write

`E0=E[:,L\{h}]`, `G0=E0 E0^T=G-ee^T`.                             (3.1)

Assume `alpha<1` so `G0` stays invertible. The matrix determinant lemma gives the exact frame-area identity

`boxed: det G0 = det G (1-alpha).`                                 (3.2)

Now assume `s!=0` and perform the literal scalar Schur pivot at the original coordinate `h` inside the residual `S`. Since `D` is diagonal, the off-diagonal row of `h` is entirely `E0^T T e`. The exact post-pivot residual is therefore

`S0 = D0 + E0^T T0 E0`,                                            (3.3)

where `D0` is `D` with the `h` entry deleted and

`T0 = T - T e e^T T / s`.                                         (3.4)

A second determinant-lemma calculation gives

`boxed: det T0 = det T * d0/s.`                                   (3.5)

Equation (3.5) remains correct at singular `T` by polynomial continuity; in particular if `det T=0`, then `det T0=0` as expected.

Multiplying (3.2) and (3.5) yields the exact post-pivot two-volume currency

`boxed:
 |det T0| det G0
 = |det T| det G * |d0/s| * (1-alpha).`                            (3.6)

This is the first new invariant of the run. It says precisely what is lost by paying one heavy physical shear coordinate: only the diagonal/pivot ratio and the removed frame-area fraction occur. No individual coordinate minor has been selected.

## 4. Aggregate post-pivot cut before inversion

On the remaining physical columns of `E0`, define the squared pair-area law

`mu0({p,q}) = det(e_p,e_q)^2 / det G0`.                            (4.1)

Let `P,Q` be iid with law `mu0` and put

`Omega0 = Pr(P cap Q = empty)`.                                    (4.2)

The r47 random-cut identity applies verbatim to `E0`: if every remaining original coordinate is independently sent to `I` or `J` with probability `1/2`, then

`E[det(E_I E_I^T) det(E_J E_J^T)]
 = (det G0)^2 Omega0/16`.                                          (4.3)

Hence, if

`Omega0 >= 1/256`,                                                 (4.4)

there exists a deterministic physical cut `I | J` for which

`sqrt(det(E_I E_I^T) det(E_J E_J^T)) >= det G0/64`.                (4.5)

For this cut the cross block of the exact terminal residual `S0` is

`N = E_I^T T0 E_J`.                                                (4.6)

Because it has rank at most two, Cauchy--Binet gives the exact singular-product identity

`sigma1(N) sigma2(N)
 = |det T0| sqrt(det(E_I E_I^T) det(E_J E_J^T)).`                  (4.7)

Thus, whenever `det T0!=0`, the cut in (4.5) has rank exactly two and

`boxed:
 Delta:=sigma1(N)sigma2(N)
 >= |det T0| det G0/64.`                                           (4.8)

Combining with (3.6),

`boxed:
 Delta >=
 [|det T| det G |d0| (1-alpha)]/[64 |s|].`                        (4.9)

This is the requested weighted replacement for a curved-fiber maximum in the heavy-hub branch: the entire post-pivot pair-area law is spent before any rank-two reciprocal singular factor appears.

## 5. Target-level theorem: three physical pivots plus aggregate rank-two tail

Two analytic inputs are now used at their completed scopes.

### 5.1 Rank-two cross-block half-Riesz + scalar pivot

The completed `QFORM-CROSSBLOCK-RANK2-HALFRIESZ-v1` / `QFORM-RANK2-CROSS-SCALAR-PIVOT-v1` theorem says: if one literal original scalar pivot has coefficient `c!=0` and the exact residual admits a physical bipartition with rank-two cross block singular product `Delta`, then arbitrary same-side residual curvature is allowed and

`||p||_infinity <= 8 |c|^(-1/2) Delta^(-1/4).`                    (5.1)

The random completion shift may depend arbitrarily on the residual bank.

### 5.2 Dependence-safe square smoothing

The completed `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` theorem says: if a base random variable has density cap `M`, then adding `b(X+h(environment))^2` with one fresh original cap-one coordinate `X` gives density cap at most

`2 sqrt(M/|b|)`,                                                   (5.2)

without assuming independence between the numerical base and the translated square.

These two theorems can therefore be nested through successive physical Schur pivots.

### Theorem 5.1 — `QFORM-SHEARFLAT-HEAVYHUB-THREEPIVOT-v1`

Assume the setup (2.1)-(2.6), `rank E=2`, and order the two outer hub coordinates so

`a:=H_11 != 0`.                                                     (5.3)

Put `delta=det H`, so the second scalar pivot after completing the first outer hub is exactly

`b=delta/a != 0`.                                                   (5.4)

Assume further

`det T !=0`, `d0!=0`, `s!=0`, `alpha<1`, `Omega0>=1/256`.          (5.5)

Then the complete ambient quadratic form, with every original coordinate and every same-bank term retained, has an absolutely continuous law satisfying

`boxed:
 ||p_Q||_infinity
 <= 4*2^(1/4)
    |a delta|^(-1/4)
    |s|^(-1/8)
    Delta^(-1/16),`                                                (5.6)

where `Delta` is the terminal physical cross singular product from (4.8).

Using only aggregate currencies,

`boxed:
 ||p_Q||_infinity
 <= 4*2^(5/8)
    |a delta|^(-1/4)
    [|det T| det G |d0| |s| (1-alpha)]^(-1/16).`                  (5.7)

The numerical prefactor in (5.7) is

`4*2^(5/8)=6.168843301631763...`.                                  (5.8)

#### Proof

Complete the first outer physical coordinate. The next literal outer coordinate has pivot coefficient `b=delta/a`; completing it leaves exactly the Schur residual `S` in (2.3). Complete the environment coordinate `h`; its pivot is `s` and its terminal residual is exactly `S0` from (3.3).

Under (5.5), Section 4 supplies a physical cut of that terminal residual with rank-two cross singular product `Delta`. Apply (5.1) to the innermost pivot `h`:

`M3 <= 8 |s|^(-1/2) Delta^(-1/4).`                                (5.9)

Now reinsert the second outer translated square using (5.2):

`M2 <= 2 sqrt(M3/|b|)
    = 4 sqrt(2) |b|^(-1/2)|s|^(-1/4)Delta^(-1/8).`                (5.10)

Reinsert the first outer translated square once more:

`M1 <= 2 sqrt(M2/|a|)
    = 4*2^(1/4)|a|^(-1/2)|b|^(-1/4)
      |s|^(-1/8)Delta^(-1/16).`                                   (5.11)

Because `b=delta/a`,

`|a|^(-1/2)|b|^(-1/4)=|a delta|^(-1/4)`,                          (5.12)

which proves (5.6). Finally insert (4.9); the factor `|s|` in its denominator contributes `|s|^(1/16)` after taking `Delta^(-1/16)`, leaving net `|s|^(-1/16)`. Since `64^(1/16)=2^(3/8)`, the prefactor becomes `4*2^(1/4+3/8)=4*2^(5/8)`, proving (5.7). QED.

### What (5.7) accomplishes

This is a true target-level conditional implication. It retains:

- the full original product law;
- both outer physical hub coordinates;
- the heavy environment pivot;
- arbitrary diagonal same-bank curvature `D0`;
- arbitrary same-side pieces of the terminal rank-two factor;
- all nonzero tail directions encoded in the exact branch.

The remaining obstruction is now quantitatively explicit: failure of this branch requires at least one of

`|a delta|`, `|det T|det G`, `|d0|`, `|s|`, `1-alpha`, or `Omega0`

to be small/degenerate. The proof does not call any such quantity zero unless it actually is zero.

Continuity is not claimed for (5.6)-(5.7), because the nested dependence-safe square transducer supplies absolute continuity and an essential bound but not a `C_0` conclusion.

## 6. Low post-pivot disjointness forces a second literal physical hub

If (4.4) fails, the already completed pair-law theorem applies to `mu0`. It gives some remaining physical coordinate `k` with deleted-frame leverage

`beta_k := e_k^T G0^(-1)e_k > 3/5`.                                (6.1)

The relationship to the original frame is exact. Sherman--Morrison yields

`boxed:
 beta_k
 = e_k^T G^(-1)e_k
   + [e_k^T G^(-1)e]^2/(1-alpha).`                                (6.2)

Thus the second heavy coordinate may be heavy because of its own original leverage or because it aligns strongly with the first heavy direction; no information is discarded.

Deleting `k` as well gives

`det(G0-e_k e_k^T)=det G0(1-beta_k).`                              (6.3)

In the live r47 branch `alpha>3/5`; if the post-pivot pair law is also low-disjoint, then `beta_k>3/5`, and therefore

`boxed:
 det(G-e e^T-e_k e_k^T)
 < (2/5)^2 det G = 4 det G/25.`                                   (6.4)

So a second failure of aggregate disjointness produces a literal **two-hub near-coloop certificate** and shrinks the surviving two-frame area by a factor below `4/25`. This is a sharper geometric description than merely saying that an individual minor is small.

## 7. Exact rank-one resonance inside the singular-T endpoint

The main compiler above needs `det T!=0`. The r47 debt also contains the exact singular endpoint `det T=0`. Write the nonzero case as

`T=lambda v v^T`, `||v||=1`, `lambda!=0`.                          (7.1)

The ORIGINAL environment principal block is not `S`; it is

`C=D+E^T U E`, `U:=H^(-1)+T`.                                     (7.2)

The matrix determinant lemma gives the exact resonance scalar

`boxed:
 det U
 = [1+lambda v^T H v]/det H.`                                    (7.3)

Hence the codimension-one resonance

`1+lambda v^T H v=0`                                               (7.4)

is exactly the case in which the **original** environment block becomes diagonal plus rank one.

Assume (7.4). Then `U` has rank exactly one; write

`U=rho w w^T`, `||w||=1`, `rho!=0`.                                (7.5)

Thus

`C=D+rho z z^T`, `z=E^T w`.                                       (7.6)

Choose one of the two original outer hubs, say `s in {1,2}`, and condition on the other outer hub. Its leaf-slope vector is

`b_s=E^T e_s`,                                                     (7.7)

where `e_1,e_2` are the standard basis of the two-dimensional hub coefficient space.

At least one choice of `s` satisfies

`|det[e_s,w]|^2 >= 1/2`.                                           (7.8)

For that choice, let `R=[b_s,z]` and `Gamma=R^T R`. Since

`R=E^T [e_s,w]`,                                                   (7.9)

we have the exact determinant identity

`boxed:
 det Gamma
 = det G * |det[e_s,w]|^2
 >= det G/2.`                                                      (7.10)

More importantly, the normalized row leverages of the augmented hub-slope/rank-one-square frame are exactly the original shear-frame leverages:

`boxed:
 r_i^T Gamma^(-1) r_i
 = e_i^T G^(-1)e_i.`                                               (7.11)

Indeed `[e_s,w]` is invertible, and right multiplication of a full rank two frame by an invertible `2 x 2` matrix does not change its leverage scores.

Therefore, if the shear frame is diffuse in the strong sense

`max_i e_i^T G^(-1)e_i <= 1/2`,                                   (7.12)

the completed `QFORM-W1-HUB-RANK1-LEAF-FRESNEL-v1` theorem applies after conditioning the unused outer hub. It gives a continuous `C_0` density for the FULL ambient form and

`||p_Q||_infinity
 <= 3*2^(4/3) [|rho| det Gamma]^(-1/3)`                            (7.13)

and hence, by (7.10),

`boxed:
 ||p_Q||_infinity
 <= 3*2^(5/3) [|rho| det G]^(-1/3)
 = 9.524406311809198... [|rho|det G]^(-1/3).`                     (7.14)

This proves `QFORM-SHEARFLAT-RANK1-RESONANCE-FRESNEL-v1`.

If (7.12) fails, the obstruction is again finite and physical: since the leverage scores sum to two, at most three original environment coordinates can have leverage above `1/2`. The theorem therefore pays the diffuse exact-resonance branch and leaves only finitely many heavy original hubs there.

Equation (7.14) does **not** claim a universal numerical constant unless the currency `|rho|det G` is itself bounded below by a universal constant in the surrounding structural branch. It is a quantitative supporting theorem, not a completion of the conjecture.

## 8. Designated partner fleet04/B06 applied to an actual curved-section inequality

The designated partner theorem is

`QFORM-FRESH-TRANSVERSE-CURVED-SECTION-v1`,

`yspennstate/math-open-problems@769800c0ab0851828772adabfb6874aa813e423d`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B06/20260923T231442Z-fleet04-B06-QFORM-r2/REPORT.md`.

It proves that for an orthonormal two-frame `(w,v)` on one original-coordinate bank with coordinate leverage `w_i^2+v_i^2<=1/2`, the off-fold pushforward

`(L+a, lambda(V-v0)^2+beta B+c)`, `|V-v0|>r`,                     (8.1)

has continuous joint density at most `4/(|lambda|r)` whenever `B` comes from a disjoint fresh bank. The statement explicitly includes `beta=0`.

Apply this to the actual post-pivot frame `E0`. Let

`F=G0^(-1/2)E0`;                                                   (8.2)

its two rows are orthonormal coefficient vectors. Suppose the deleted frame satisfies the genuine partner gate

`max_{j!=h} e_j^T G0^(-1)e_j <= 1/2`.                             (8.3)

Diagonalize the **whitened** post-pivot shear coefficient

`B0=G0^(1/2) T0 G0^(1/2)`                                         (8.4)

inside this two-dimensional coefficient space only. Let its eigenvalues be `mu1,mu2`, ordered so `|mu2|>=|mu1|`, and rotate the two rows of `F` accordingly. This preserves orthonormality and every coordinate leverage in (8.3). Denote the resulting physical linear forms by `(L,V)`.

Use the partner theorem with `beta=0`, `lambda=mu2`, and `r=1/64`. It gives

`||g_off||_infinity <= 256/|mu2|`.                                (8.5)

Adding `mu1 L^2` to the second output is a triangular map

`(l,y) -> (l,y+mu1 l^2)`                                          (8.6)

with Jacobian one, so the same joint-density bound holds for the complete **rank-two low-rank curved factor**

`(L, mu1 L^2+mu2(V-v0)^2)`                                        (8.7)

on `|V-v0|>1/64`.

Since

`|mu1 mu2| = |det B0| = |det T0| det G0`,                         (8.8)

and `|mu2|>=sqrt(|mu1 mu2|)`, we obtain the actual matrix-specific partner inequality

`boxed:
 ||g_off||_infinity
 <= 256 [|det T0| det G0]^(-1/2).`                                (8.9)

This is a genuine application of the designated fleet04/B06 theorem to the r48 post-pivot geometry. It is deliberately scoped: the diagonal same-bank term `D0` is not absorbed into (8.7), so (8.9) by itself is **not** promoted to a scalar density bound for the full terminal residual. The full scalar branch is instead paid by Theorem 5.1, which keeps `D0` through the cross-block half-Riesz route.

## 9. Finite algebra/check evidence

The exact identities were independently checked numerically on 10,000 random real instances with `2 x 8` frames and symmetric `2 x 2` coefficient matrices. The normalized discrepancy in

`det(T0) det(G0)
 = det(T) det(G) (d0/s)(1-alpha)`                                  (9.1)

was below `1.7e-11` in the finite-precision run. Symbolic algebra also verifies

`det(H^(-1)+lambda v v^T)
 = [1+lambda v^T H v]/det H`.                                     (9.2)

These computations are sanity checks only; Sections 3-8 contain the proofs.

Constants checked exactly/numerically:

`4*2^(5/8)=6.168843301631763...`,                                  (9.3)

`3*2^(5/3)=9.524406311809198...`.                                  (9.4)

## 10. What remains

The full conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**.

The heavy-hub shear-flat survivor is now reduced further:

1. if `det T!=0`, the heavy scalar pivot is nonzero, its diagonal companion is nonzero, the deleted frame is not a coloop, and the post-pivot pair law has disjointness at least `1/256`, Theorem 5.1 pays the complete ambient form by the explicit aggregate bound (5.7);
2. if the post-pivot pair law is low-disjoint, Section 6 forces a second literal heavy physical hub and a `<4/25` two-frame area collapse after two deletions;
3. if `det T=0` and the exact resonance `1+lambda v^T H v=0` holds, the original environment block is diagonal plus rank one, and the diffuse shear-frame branch is paid continuously by (7.14);
4. the designated partner theorem controls the deleted-frame low-rank off-fold geometry by (8.9) whenever its actual leverage gate holds.

The first precise B06 debt after this run is therefore

`QFORM-SHEARFLAT-NONRESONANT-RANK1T-OR-TWOFOLD-HEAVYHUB-v1`:

retain the complete original product structure in the two remaining hard modes:

- `det T=0` but `1+lambda v^T H v !=0`, where the original environment curvature is diagonal plus rank two but its hub slope lies in the same two-frame; and
- repeated low-disjointness after one or two heavy deletions, where the surviving two-frame area collapses but must not simply be discarded.

A successful next receiver should spend either the nonresonance scalar and retained frame area jointly, or the two-heavy-hub area-collapse certificate, before taking any curved-fiber supremum.

**Continuity:** proved only in the exact rank-one resonance Fresnel branch and in the separately scoped partner two-output branch. The main three-pivot aggregate theorem establishes absolute continuity plus essential boundedness, not continuity.

**Native brain:** not verified. Repository read/write and source consumption occurred, but no authenticated native brain receiver/ingestion event was established, so the run remains `WITHOUT_VERIFIED_BRAIN`.
