SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B03, 2026-09-24T01:42:18Z.
attacking: the genuine-rank-two overlap-one collar by spending the entire rank-two cross singular-product at once; derive an L2 output law, the assigned whole-copy half-Riesz time integral, and a quarter-Riesz residual that can be fed to a literal hyperbola peel for linear one-copy small-ball scaling.

# account03/B03 r44 — aggregate rank-two crossing time compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Classification: **NEW SUPPORTING COMPILER / LIVE EXACT-RANK-TWO COLLAR INTEGRATED / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN**. Full-target continuity remains **OPEN**. The present theorem gives an `L^2` density and dependence-safe weighted time estimates on a live full-law rank-two crossing branch, but by itself does not give an `L^infinity` density there.

## 1. Fresh source boundary and exact debt attacked

Fresh control remained OWNER CONTROL revision `2026-09-22.15`, QFORM-only, with no pause/stop for account03/B03. The live corrections are retained throughout: no law-uniform pointwise quadratic-phase decay, no independence after a spectral rotation, no conditional cap-one law for `X-X'` given `X+X'`, no arbitrary-joint rank-three coarea estimate, no deletion of a small nonzero random quadratic tail, and no inference from a single tiny physical minor.

The immediate full-target structural input is account03/B20 r42, whose one-anchor branch produces a literal original-coordinate partition

`{j} union R union C`

and the anchored cross block

`M = [[b,r^T],[c,N]] = A[{j} union R,{j} union C]`                 (1.1)

with `J_sep>=1/2304`, all physical diagonals small, and either

`E_2(N)>4/9`                                                       (1.2)

or a quantitatively large two-star packet. The exact-rank-one endpoint of (1.2) was paid by account03/B03 r43. The fresh account02/B20 exact-rank-two refinement shows that a still-unpaid exact-rank-two state must carry a Schur/internal-star/extreme-condition-number currency; its rank-two SVD notation will be used below only to identify the live scale.

The analytic input used here is the checked exact-rank crossing theorem in

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For independent source banks `X_R,X_C`, a fixed exact-rank-`r` cross block `B=USV^T`, arbitrary measurable same-bank real functions `F,G`, and density caps `M_R,M_C` for `U^T X_R,V^T X_C`, it proves

`|phi(t)| <= min(1,(pi/|t|)^(r/2)(M_R M_C)^(1/2)(det S)^(-1/2)).` (1.3)

No pointwise one-coordinate quadratic-phase estimate occurs in (1.3); it is a joint bank Plancherel estimate. For an orthonormal two-dimensional projection of a cap-one product bank, the same source gives the universal cap `2`.

The designated account04/B03 source actually applied in Section 5 is the valid collision sublemma from

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260922T193150Z-account04-B03-collision-l2-r1/REPORT.md`.

Its later correction is respected: the old report's advertised two-square unweighted-L2 compiler is not used. Only the elementary valid consequence

`P(|Y-Y'|<=epsilon) <= 2 epsilon ||p_Y||_2^2`                    (1.4)

is consumed. I also reread the newer account04/B03 r2 dependent sum/difference fractional-budget theorem; no independence between conjugate sums and differences is imported from it.

## 2. Aggregate rank-two crossing theorem

The main result is a critical `r=2` integration of (1.3).

### Theorem 2.1 — `QFORM-RANK2-CROSS-L2-TIME-v1`

Let `B_0`, `X_R`, `X_C` be three mutually independent source groups. The scalar coordinates inside each of `X_R,X_C` are independent and have probability densities at most one; no assumption is placed on the law of `B_0` beyond independence from those two banks.

Let `N` be a fixed real matrix of exact rank two, with nonzero singular values

`s_1>=s_2>0`,   `p:=s_1 s_2`.                                    (2.1)

For every background value `z`, let `F_z` and `G_z` be arbitrary measurable real functions on the two source banks, and let `c_z` be real. Set

`S = F_{B_0}(X_R)+G_{B_0}(X_C)+2 X_R^T N X_C+c_{B_0}`.            (2.2)

All background-generated affine terms and all same-bank quadratic terms are therefore allowed.

If the two singular-frame projections have density caps `M_R,M_C`, put

`K := pi (M_R M_C)^(1/2) p^(-1/2).`                              (2.3)

Then:

1. the characteristic function obeys

`boxed: |phi_S(t)| <= min{1,K |t|^(-1)};`                        (2.4)

2. `S` has an `L^2` density and

`boxed: ||p_S||_2^2 <= 2 (M_R M_C)^(1/2) p^(-1/2);`              (2.5)

3. the exact B03 whole-copy weighted time integral satisfies

`boxed:
 int_R |t|^(-1/2)|phi_S(t)|^2 dt
 <= (16/3) sqrt(K)
 = (16/3) sqrt(pi) (M_R M_C)^(1/4) p^(-1/4);`                    (2.6)

4. if `S'` is an independent copy of the **whole** scalar output `S`, then

`boxed:
 E|S-S'|^(-1/2)
 <= (16/(3 sqrt(2))) (M_R M_C)^(1/4) p^(-1/4);`                  (2.7)

5. its one-copy critical quarter-potential obeys

`boxed:
 H_(1/4)(S):=sup_a E|S-a|^(-1/4)
 <= 2^(7/4)(M_R M_C)^(1/8)p^(-1/8).`                             (2.8)

For cap-one product source banks, the orthonormal two-dimensional projection theorem gives `M_R,M_C<=2`; consequently

`boxed: ||p_S||_2^2 <= 4 p^(-1/2),`                              (2.9)

`boxed:
 int |t|^(-1/2)|phi_S(t)|^2dt
 <=(16/3)sqrt(2 pi) p^(-1/4),`                                   (2.10)

`boxed: E|S-S'|^(-1/2) <=(16/3)p^(-1/4),`                        (2.11)

and

`boxed: H_(1/4)(S) <=4p^(-1/8).`                                 (2.12)

### Proof

Condition on `B_0=z`. The two source banks remain independent product banks. All terms depending only on the R bank are absorbed into the phase `F_z`; all terms depending only on the C bank into `G_z`. Apply the exact-rank crossing theorem (1.3) with `r=2` and singular product `p`:

`|phi_{S|z}(t)| <= min{1,K/|t|}`.                                (2.13)

The right side is uniform in `z`, so averaging the conditional characteristic functions gives (2.4):

`|phi_S(t)| <= E_z |phi_{S|z}(t)| <= min{1,K/|t|}`.              (2.14)

Square the envelope and integrate. Its crossover is `|t|=K`, hence

`int_R |phi_S(t)|^2dt
 <=2[int_0^K 1 dt + K^2 int_K^infinity t^(-2)dt]
 =4K.                                                            (2.15)

A finite measure whose Fourier transform lies in `L^2` is absolutely continuous with an `L^2` density. With the Fourier convention used in the source, Plancherel gives

`2pi ||p_S||_2^2 = ||phi_S||_2^2 <=4K`,                          (2.16)

which is exactly (2.5).

For the assigned weighted integral, again split at `K`:

`int_R |t|^(-1/2)|phi_S(t)|^2dt
 <=2[int_0^K t^(-1/2)dt
      +K^2 int_K^infinity t^(-5/2)dt]
 =2[2sqrt(K)+(2/3)sqrt(K)]
 =(16/3)sqrt(K).`                                                 (2.17)

This proves (2.6).

Use the independent-copy identity only at the level of the **whole scalar output**,

`|phi_S(t)|^2 = E exp(it(S-S')).`                                 (2.18)

The positive regularized Riesz identity

`int_R e^(itx)|t|^(-1/2)dt = sqrt(2pi)|x|^(-1/2)`                (2.19)

then turns (2.6) into (2.7). No coordinatewise sum/difference variable is conditioned on or declared independent of its conjugate.

It remains to prove (2.8). Let `L=||p_S||_2`. For any center `a` and radius `R>0`, Cauchy-Schwarz on the near region gives

`int_(|x-a|<=R)|x-a|^(-1/4)p_S(x)dx
 <= L [int_(|u|<=R)|u|^(-1/2)du]^(1/2)
 =2 L R^(1/4).`                                                   (2.20)

The far region is at most `R^(-1/4)`. Optimizing

`2L R^(1/4)+R^(-1/4)`                                            (2.21)

over `R` yields

`H_(1/4)(S) <=2 sqrt(2L).`                                       (2.22)

From (2.5),

`L <= sqrt(2)(M_RM_C)^(1/4)p^(-1/4)`.                            (2.23)

Substitution gives (2.8). The cap-two specialization gives (2.9)-(2.12). QED.

### What this theorem is and is not

The theorem does **not** make `|phi|` integrable: the rank-two envelope is critical `1/|t|`. Therefore it does not itself prove an `L^infinity` density or continuity. Its gain is exactly the one appropriate to the B03 assignment: after squaring, the time integral becomes integrable, producing a dimension-free collision/Riesz budget and a one-copy quarter-potential without paying one individual physical minor.

## 3. Actual application to the live one-anchor exact-rank-two E2 branch

Return to the literal anchored packet (1.1). Condition on the genuine original hub coordinate `X_j=z`. The full remaining polynomial has the form

`F_z(X_R)+G_z(X_C)+2X_R^T N X_C+c_z`,                             (3.1)

because the hub stars become affine terms in their respective banks; every R-R and C-C quadratic term remains inside `F_z,G_z`. Thus Theorem 2.1 applies to the **full ambient law**, not to a simplified model.

Suppose `rank N=2`. Then

`E_2(N)=s_1^2 s_2^2=p^2`.                                        (3.2)

On the live branch `E_2(N)>4/9`, hence

`p>2/3`.                                                         (3.3)

Using the cap-two projection bounds in Theorem 2.1 gives the explicit uniform estimates

`boxed: ||p_Q||_2^2 < 4 sqrt(3/2) = 4.8989794856...;`             (3.4)

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 < (16/3)sqrt(2pi)(3/2)^(1/4)
 =14.7948810184...;`                                             (3.5)

`boxed:
 E|Q-Q'|^(-1/2)
 < (16/3)(3/2)^(1/4)
 =5.9023035717...;`                                              (3.6)

and

`boxed:
 sup_a E|Q-a|^(-1/4)
 <4(3/2)^(1/8)
 =4.2079580220....`                                              (3.7)

Here `Q'` is an independent copy of the whole full-law output. This is uniform even if `s_2` tends to zero while `s_1` grows so that `s_1s_2>2/3`; in particular the estimate does **not** deteriorate in the extreme-condition-number collar identified by account02/B20. It spends the aggregate product `s_1s_2`, not the smallest singular value separately.

This is a genuine advance on the analytic interface: the exact-rank-two `E_2>4/9` chamber now carries a uniform `L^2` output law, a uniform whole-copy half-Riesz budget, and a uniform one-copy quarter-Riesz budget with arbitrary same-bank curvature and arbitrary hub diagonal/stars retained.

It is not yet a full one-copy density payment. A final receiver still has to convert one of the surviving Schur/internal-star currencies into the missing quarter-power without assuming an independent rotated coordinate.

## 4. Linear one-copy small-ball compiler when a literal hyperbola peel is available

The quarter-potential in (2.12) can recover linear one-copy small-ball scale as soon as a genuine literal hyperbolic pair is exposed.

The checked coordinate-hyperbola peel in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

states that for two literal original coordinates with zero diagonals and cross coefficient `mu!=0`, exact product completion yields

`Q_total=2mu(X_i+beta_j)(X_j+beta_i)+S`,                          (4.1)

and

`D(Q_total):=||p_Qtotal||_infinity
 <=2^(3/4) kappa |mu|^(-3/4) H_(1/4)(S),`                        (4.2)

where

`kappa=sup_(y>0) log(1+y)/sqrt(y)=0.8047423425...`.               (4.3)

If the Schur residual `S` is of the aggregate exact-rank-two crossed-bank type of Theorem 2.1 with cap-one product banks, (2.12) gives

`boxed:
 ||p_Qtotal||_infinity
 <=2^(11/4) kappa |mu|^(-3/4)p^(-1/8)
 =5.4136396084... |mu|^(-3/4)p^(-1/8).`                          (4.4)

Therefore every interval `I` satisfies the actual linear one-copy small-ball estimate

`boxed:
 P(Q_total in I)
 <=5.413640 |mu|^(-3/4)p^(-1/8)|I|.`                             (4.5)

This compiler is determinant-aggregate rather than minor-local: its residual currency is the rank-two singular product `p=s_1s_2`. It remains valid through a highly ill-conditioned rank-two crossing as long as `p` stays bounded below.

The current live one-anchor packet has not yet been shown to contain the literal zero-diagonal hyperbola peel disjoint from the aggregate rank-two residual, so (4.4) is a proved **receiver**, not a declaration that the entire remaining one-anchor chamber is closed.

## 5. Designated account04/B03 result applied to the new live estimate

Apply the valid designated-partner collision lemma (1.4) to the new `L^2` density from Theorem 2.1. For an independent whole copy `S'`,

`P(|S-S'|<=epsilon)
 <=2 epsilon ||p_S||_2^2
 <=4 epsilon (M_RM_C)^(1/2)p^(-1/2).`                            (5.1)

For cap-one product banks, `M_R,M_C<=2`, so

`boxed:
 P(|S-S'|<=epsilon) <=8 p^(-1/2) epsilon.`                       (5.2)

On the actual live rank-two `E_2(N)>4/9` branch, `p>2/3`, and therefore

`boxed:
 P(|Q-Q'|<=epsilon)
 <8 sqrt(3/2) epsilon
 =9.7979589711... epsilon.`                                      (5.3)

This is an actual **linear collision small-ball estimate** on the live full-law packet. It is not used backward to infer `L^infinity` for `Q`; the latter implication would be false without additional smoothing. The proof of Theorem 2.1 came first, so the partner lemma is being applied at its valid scope only.

The newer account04/B03 r2 theorem was also reread: its dependent `1/4+1/4` fractional-budget estimate remains valid for literal physical quadratic pairs in the `U=X-X'`, `V=X+X'` marginals, but it is not transplanted to the singular-vector projections here because a general rotation destroys coordinate independence. That distinction is exactly why the present crossed-bank proof uses joint Plancherel before the whole-copy identity.

## 6. First remaining implication

The unrestricted target is still open. Within the exact-rank-two `E_2>4/9` one-anchor chamber, the Fourier debt is now more precise:

> Starting from the uniform aggregate credits (3.4)-(3.7), use one of the deterministic currencies forced by the exact anchored-volume identity — Schur currency, an internal star transverse to the singular plane, or the corresponding opposite-bank currency — to supply the missing quarter-power and obtain a one-copy `L^infinity` density, **without** paying `1/s_2`, deleting the small singular direction, or declaring a rotated coordinate independent.

The extreme-condition-number collar itself is no longer a problem for the time integral: all estimates above depend only on `p=s_1s_2>2/3`. The remaining issue is a product-preserving one-copy transduction.

A promising next step is to combine the quarter-potential (3.7) with the four-currency identity before selecting a physical coordinate: average a literal hyperbola/star receiver over the singular-frame Pluecker weights, so the aggregate `p` pays the crossing while the anchored currency pays only the extra quarter-power. If that averaging necessarily incurs a divergent reciprocal minor, the correct next mechanism is a grouped-star analogue of the hyperbola peel rather than another single-pivot inversion.

## 7. Status

Proved in this run:
- aggregate rank-two crossing envelope (2.4) in the presence of arbitrary background-conditioned same-bank phases;
- `L^2` output density bound (2.5);
- dependence-safe weighted whole-copy time integral (2.6) and half-Riesz estimate (2.7);
- one-copy quarter-Riesz estimate (2.8);
- uniform specialization (3.4)-(3.7) on the actual live `rank N=2`, `E_2(N)>4/9` one-anchor branch;
- linear one-copy small-ball receiver (4.4)-(4.5) when a genuine literal hyperbola peel is structurally available;
- designated-partner linear collision estimate (5.1)-(5.3).

Not proved:
- universal `L^infinity` for the entire exact-rank-two one-anchor branch;
- the unrestricted three-large-eigenvalue theorem;
- full-target continuity.

No Gaussianity, log-concavity, moments, support bounds, post-rotation independence, conditional sum/difference cap, arbitrary-joint coarea, or Monte Carlo inference was introduced.
