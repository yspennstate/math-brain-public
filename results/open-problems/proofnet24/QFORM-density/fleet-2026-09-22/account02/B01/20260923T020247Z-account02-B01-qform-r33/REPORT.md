SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T02:02:47Z.
attacking: the rank-two grouped-slope / one-curvature N3 branch — aggregate the entire two-dimensional slope bank before inversion, then spend one transverse Fresnel direction through the original-product Brascamp–Lieb integral.

# account02/B01 r33 — grouped two-slope plus one-Fresnel smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Oscillatory replacement / complementary constructions and source-valid counterexamples  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING N3 THEOREM / FULL QFORM OPEN`  
**Review status:** no end-to-end independent review of this report; full-candidate requirements are not met.  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred, but no native learned-memory receiver use was established).

## 1. Target and correction boundary

The target remains unchanged: for arbitrary independent real original-coordinate inputs with densities at most one and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one universal essential bound for the density of `X^T A X`, or give a valid target counterexample. No moments, compact/connected support, Gaussianity, log-concavity, diagonal-basis independence, or post-rotation independence are introduced. Continuity is separate.

The phase-aligned obstruction to a law-uniform scalar Fresnel estimate remains active. For every fixed nonzero `s` and every small `delta>0`, a measure-one subset of

`{x: dist(s x^2,2 pi Z)<=delta}`

can be used as an admissible density, giving

`Re E exp(i s X^2)>=cos(delta)`.

Nothing below asserts a law-uniform pointwise `|s|^{-1/2}` estimate. The new decay is obtained only after a **two-dimensional random slope is averaged first** and a separate curvature direction is Fresnel-linearized jointly with it.


`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

and `FOURIER_ROUTE_REPORT.md`, especially the shifted Fresnel–Brascamp–Lieb integral. The later volume-stability report

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`

is also retained: it pays rank-at-least-three cross blocks near a diffuse three-volume certificate, but explicitly leaves low-cross-rank/hub states open.

## 2. Named partner input actually used

The completed assigned partner account03/B01 report

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T235524Z-r21/REPORT.md`

records the following source-valid rank-two slope payment (through its weighted affine-fiber input). If `C` is a real rank-two matrix from one original-coordinate bank to another and `R` is an orthonormal basis of its range, write

`C=R B`, `B in R^(2 x |J|)`.

Then for independent cap-one `X_J`, the two-dimensional grouped slope

`eta=B X_J`

has density cap

`boxed: ||p_eta||_infinity <= e / Delta_2(C),`                  (2.1)

where

`Delta_2(C)=sqrt(pdet(C C^T))=s_1(C)s_2(C)`.

Indeed `B B^T` has the two nonzero eigenvalues of `C C^T`, and the product-projection theorem gives `e/sqrt(det(BB^T))`. Equation (2.1) is inserted below before any fixed physical two-column minor is selected.

## 3. Main theorem — aggregate two slopes plus one transverse Fresnel direction

Let the original coordinates be split into disjoint sets `I,J,K`. Condition on `X_K`; the resulting affine terms are arbitrary and will be kept. Put

`C=A[I,J]`,                                                       (3.1)

and suppose

`rank C=2`.                                                       (3.2)

Assume the physical `I`-block has the form

`A_II = lambda v v^T + D`,                                      (3.3)

where `lambda!=0`, `||v||_2=1`, and `D` is diagonal. Let `R` be an `|I| x 2` matrix with orthonormal columns spanning `range(C)`, and set

`delta=||(I-RR^T)v||_2>0`.                                      (3.4)

Let `P_*` be the orthogonal projector onto the three-dimensional space

`E=span(v,range(C))`.                                            (3.5)

Assume the original-coordinate leverage gate

`max_(i in I) (P_*)_ii <=1/2`.                                  (3.6)

No restriction is imposed on `A_JJ`, on any block touching `K`, on the signs of coefficients, or on conditioning-generated affine terms.

### Theorem 3.1 — `QFORM-GROUPED-TWOSLOPE-ONEFRESNEL-v1`

Under (3.1)-(3.6), `Q=X^TAX+b^T X+c` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= (5/3) 2^(6/5) e^(2/5)
    [ |lambda| delta^2 pdet(C C^T) ]^(-1/5)
 < 5.713 [ |lambda| delta^2 pdet(C C^T) ]^(-1/5).`              (3.7)

This is an aggregate-before-inversion estimate: `pdet(CC^T)` sums the two-dimensional slope-bank resource before any reciprocal physical minor is paid.

### Proof

After conditioning on `X_K`, absorb all terms depending only on `X_J` into a real phase `G(X_J)` and all deterministic linear terms in `X_I` into a vector `b_I`. Factor

`C=R B`.                                                         (3.8)

Set

`eta=B X_J`.                                                     (3.9)

By (2.1), `eta` has a density `rho` with

`||rho||_infinity <= K_2:=e/Delta_2(C)`.                        (3.10)

Disintegrating the `X_J` law over `eta`, the remaining conditional phase contributes a multiplier `m_t(eta)` with `|m_t(eta)|<=1`. Thus, writing `phi(t)=E exp(itQ)`, it suffices to bound

`int rho(eta) |Phi_t(eta)| d eta`,                              (3.11)

where

`Phi_t(eta)=E_(X_I) exp{i t[lambda(v^T X_I)^2 + X_I^T D X_I]
                         +i(2t R eta+t b_I)^T X_I}.`            (3.12)

For `t!=0`, use the damped Fresnel identity from the newest-Claude Theorem F and remove the damping by dominated convergence. With

`g_i(x)=f_i(x) exp(i t D_ii x^2)`

(and the deterministic linear shifts retained in the Fourier arguments),

`|Phi_t(eta)|
 <= (4 pi |t lambda|)^(-1/2)
    int_R prod_(i in I)
      |hat g_i(u v_i+2t(R eta)_i+t(b_I)_i)| du.`                (3.13)

Insert (3.13) into (3.11), use `rho<=K_2`, and make the two-dimensional change of variables

`y=2t eta`, `d eta=(2|t|)^(-2)dy`.                              (3.14)

This gives

`|phi(t)|
 <= (4 pi |t lambda|)^(-1/2) K_2(2|t|)^(-2)
    int_(R^3) prod_i |hat g_i(u v_i+(Ry)_i+t(b_I)_i)| du dy.`   (3.15)

The row vectors of the last three-dimensional integral are

`omega_i=(v_i,R_i) in R^3`.                                     (3.16)

Their Gram matrix is

`G=sum_i omega_i omega_i^T
  =[[1,v^T R],[R^T v,I_2]],`                                    (3.17)

hence by the Schur complement

`det G=1-||R^T v||^2=delta^2`.                                 (3.18)

The normalized row leverages `omega_i^T G^(-1)omega_i` are exactly the diagonal entries of the projector onto `E`, so (3.6) is precisely the `<=1/2` gate in the shifted geometric Brascamp–Lieb argument of newest-Claude Theorem F. Its scalar Fourier `L^p` lemma is valid for the complex twists `g_i` because `|g_i|<=f_i`. Translation invariance of the one-dimensional arguments keeps every `t(b_I)_i`. Therefore

`int_(R^3) prod_i |hat g_i(u v_i+(Ry)_i+t(b_I)_i)| du dy
 <=(4 pi)^3 delta^(-1).`                                       (3.19)

Combining (3.15) and (3.19),

`|phi(t)|
 <=8 pi^(5/2) K_2 |lambda|^(-1/2) delta^(-1) |t|^(-5/2).`      (3.20)

This is the new joint averaged-frequency decay. It is **not** a scalar pointwise Fresnel estimate: the full `|t|^-2` part comes from averaging the genuinely random two-dimensional slope `eta`, and only then is the single quadratic direction Fresnel-linearized inside a three-dimensional BL integral.

Let

`A_0=8 pi^(5/2) K_2 |lambda|^(-1/2) delta^(-1)`.                (3.21)

Together with `|phi(t)|<=1`,

`int_R |phi(t)|dt
 <=int_R min(1,A_0 |t|^(-5/2))dt
 =(10/3) A_0^(2/5).`                                            (3.22)

Fourier inversion gives

`||p_Q||_infinity
 <=(5/(3pi))A_0^(2/5)
 =(5/3)2^(6/5)K_2^(2/5)|lambda|^(-1/5)delta^(-2/5).`            (3.23)

Finally insert (3.10), with `Delta_2(C)^2=pdet(CC^T)`, to obtain (3.7). The integrable envelope (3.20) also gives a continuous representative in `C_0(R)`. QED.

## 4. Exact strict-N3 family paid uniformly

Let `m` be divisible by four. On an original-coordinate bank `I` of size `m`, choose three orthonormal Walsh vectors

`v=(1,1,...,1)/sqrt(m)`,
`r_1=(1,-1,1,-1,...)/sqrt(m)`,
`r_2=(1,1,-1,-1,...)/sqrt(m)`.

On a disjoint bank `J` of size `m`, choose two orthonormal Walsh vectors `a,b`, each having entries `+-1/sqrt(m)`. Define

`C=r_1 a^T+r_2 b^T`,                                             (4.1)

and

`A_m=[[v v^T, C],[C^T,0]].`                                     (4.2)

On the orthogonal decomposition generated by

`v`, `(r_1,a)`, `(r_2,b)`,

the matrix is the direct sum of `[1]` and two copies of

`[[0,1],[1,0]]`.

Hence its nonzero spectrum is exactly

`{1,1,1,-1,-1}`.                                                (4.3)

Thus it lies in the exact QFORM spectral target. Moreover,

`max_i |(A_m)_ii|=1/m`,                                         (4.4)

all `I-I` and `J-J` physical `2x2` principal determinants vanish, and for an `I-J` pair

`|det A_m[{i,j},{i,j}]|=|C_ij|^2<=4/m^2`.                       (4.5)

Therefore, for every fixed no-pivot threshold `tau>0`, the family is in strict N3(tau) for all sufficiently large `m`.

For Theorem 3.1,

`lambda=1`, `range(C)=span(r_1,r_2)`, `delta=1`,
`pdet(CC^T)=1`,                                                  (4.6)

and the augmented three-dimensional row leverage on `I` is exactly `3/m`. Hence for `m>=8`,

`boxed: ||p_(X^T A_m X)||_infinity <5.713`                       (4.7)

for **every** collection of independent cap-one input laws.

This family also shows why the aggregate slope bank matters. If `B=[a^T;b^T]`, then every fixed two-column slope minor satisfies

`|det B[:,{j,k}]|<=2/m`,                                        (4.8)

while

`det(BB^T)=1`.                                                   (4.9)

Thus selecting two physical slope coordinates before paying the oscillatory integral would incur an artificial reciprocal power of `m`; (3.7) first aggregates all columns into the invariant two-volume (4.9), eliminating that loss.

The natural `I|J` cross block has rank exactly two, so all three-volume and five-volume currencies on that cut vanish. The theorem is therefore genuinely complementary to D'/D5 on this low-cross-rank geometry, even though other global exits can overlap on particular highly diffuse examples.

## 5. Relation to the latest volume-stability theorem

The volume-stability package at `c2414ef...` gives a powerful exit whenever an original-coordinate cross block has three substantial singular directions and admissible volume marginals. Theorem 3.1 addresses a different geometry: the chosen cross block has **exact rank two**, so `e_3(C^TC)=e_5(C^TC)=0` identically. The missing third direction is supplied by one self-curvature direction `v` transverse to the cross range, and the two currencies are joined before absolute inversion.

The source condition (3.6) is still a real gate. It is not claimed to follow from the bare three-large-eigenvalue hypothesis. In particular, concentrated augmented rows and general self-blocks not of `rank-one + diagonal` form remain outside this theorem.

## 6. First unpaid implication after this run

The new analytic packet suggests a sharper structural target:

`QFORM-N3-RANK2-CROSS-PLUS-TRANSVERSE-CURVATURE-ROUTING-v1`:

> In a strict no-pivot state that escapes the rank-at-least-three volume/tail exits, either find an original-coordinate cut whose rank-two cross bank has dimension-free aggregate area `Delta_2(C)` together with a transverse rank-one-plus-diagonal curvature packet satisfying the augmented leverage gate, or route the same state to an already-paid grouped-pair, hub, near-coloop, ridge, or finite-core branch — without selecting a vanishing fixed two-column minor.

Theorem 3.1 pays the analytic side once such a packet is exposed. What remains is the exhaustive matrix/product-source routing, especially concentrated augmented rows and arbitrary higher-rank self-curvature. Full QFORM is therefore still **OPEN / NOT PROVED / NOT DISPROVED**.

## 7. Arithmetic regression

For the family (4.2), direct finite-dimensional checks at `m=8,12,16,20` give nonzero spectra exactly `{-1,-1,1,1,1}`, maximum physical diagonal `1/m`, maximum physical pair-determinant magnitude `4/m^2`, and augmented leverage `3/m`. The numerical constant in (3.7) is

`(5/3)2^(6/5)e^(2/5)=5.712188587081587...`.

These are regression checks only; the proof is Sections 2-4 above.
