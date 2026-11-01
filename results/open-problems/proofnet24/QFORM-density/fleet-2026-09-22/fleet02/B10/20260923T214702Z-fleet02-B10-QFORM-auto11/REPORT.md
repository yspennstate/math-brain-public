SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B10, 2026-09-23T21:47:02Z.
attacking: the exact-rank-three near-coloop endpoint; test fragmentation-insensitive joint hub-plus-bank gluing, consume the ruled-side theorem on its paid side, and preserve original-coordinate product provenance.

# fleet02/B10 — fragmented physical hub is not an endpoint obstruction in the pure-longitudinal near-coloop subfamily

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: rank-three coupled case, complementary constructions/source-valid counterexamples; partner `fleet03/B10`.
Status: `ESSENTIAL_SOURCE_RESULT_APPLIED / FRAGMENTATION-ROUTE_COUNTEREXAMPLE / UNIFORM-PURE-LONGITUDINAL-SUBCASE / FULL_QFORM_OPEN`.

The unrestricted conjecture remains OPEN. Everything below is an exact-rank-three supporting result or a counterexample to an intermediate proof interface, not a counterexample to QFORM.

## 0. First unpaid implication

The next unpaid implication is

`QFORM-NEARCOLOOP-FRAGMENTATION-INSENSITIVE-JOINT-GLUING-v3`:

> In the generic diffuse near-coloop collar, obtain a density bound uniform as the leakage `rho -> 0` and uniform over arbitrary cap-one physical-hub densities, without a final constant involving the hub superlevel fragmentation functional `K(f_H)`, the number of hub components, `TV(f_H)`, the partner loss `rho^{-1/6}`, or a hub-first absolute inverse-discriminant payment. Retain/recombine at least one ORIGINAL-coordinate leakage/transverse bank before taking layer-cake sums or absolute values.

The construction below proves that arbitrary hub fragmentation by itself is not a genuine obstruction: one admissible hub has infinitely many components and infinite `K(f_H)` and `TV(f_H)`, while the corresponding exact-rank-three outputs have a uniform density bound all the way to the null endpoint. Thus any endpoint proof that first reduces the hub to componentwise intervals and then pays `sum sqrt(length)` is too lossy for the unrestricted target.

## 1. Exact target-valid near-coloop family

Fix

`0 <= rho < 1/64`,  `c=1-rho`.

For `rho>0` this is inside the partner's positive-leakage collar; `rho=0` is its exact-null endpoint. Define a Parseval frame in `R^3` by the ORIGINAL physical rows

`u_0 = sqrt(c) e_1`,
`u_1 = sqrt(rho) e_1`,
`u_2,...,u_65 = e_2/8`,
`u_66,...,u_129 = e_3/8`.

Then

`sum_i u_i u_i^T = I_3`.

Take the fixed spectral matrix

`M = [[0,1,0],[1,0,0],[0,0,1]]`.

Its eigenvalues are exactly `{-1,1,1}`. If `R` is the `130 x 3` matrix with rows `u_i^T` and

`A_rho = R M R^T`,

then `R^T R=I_3`, hence the three nonzero eigenvalues of `A_rho` are exactly `{-1,1,1}` for every `rho`. This is therefore a target-valid exact-rank-three family with no small spectral eigenvalue hidden in the construction.

The near-coloop bookkeeping is exact. With hub direction `e=e_1`,

`c>63/64`, `alpha=e^T M e=0`, `A_{00}=u_0^T M u_0=0`,

and the leaf decomposition `u_j=t_j e+p_j` has

`sum_j t_j^2=rho`, `sum_j t_j p_j=0`, `sum_j p_j p_j^T=I_2`.

The pure longitudinal leaf is `u_1=sqrt(rho)e_1`, while every nonzero transverse leaf has leverage

`||p_j||^2=1/64 < 1/61`.

Thus for `rho>0` the family lies beyond the completed partner `fleet03/B10` large-transverse-leaf gate and inside its diffuse positive-leakage survivor.

## 2. ORIGINAL-coordinate product provenance and canonical form

Let all physical originals be independent. Write the hub original as `H`, the pure-longitudinal original as `P`, the sixty-four `e_2` originals as `U_1,...,U_64`, and the sixty-four `e_3` originals as `V_1,...,V_64`. Define

`Z = sqrt(c) H + sqrt(rho) P`,
`Y = (1/8) sum_{i=1}^{64} U_i`,
`W = (1/8) sum_{i=1}^{64} V_i`.

These are genuinely independent because they are functions of three disjoint ORIGINAL-coordinate banks. No spectral rotation is used to infer independence. Direct substitution gives

`Q_rho = X^T A_rho X = 2 ZY + W^2`.                                      (2.1)

Equally, in physical-hub canonical notation,

`L=sqrt(c)Y`, `Vcan=W`, `epsilon=sqrt(rho/c)`, `beta=0`,

so

`Q_rho = 2HL + Vcan^2 + 2 epsilon L P`.                                (2.2)

This is exactly the positive-leakage canonical shape targeted by the fresh two-bank conditional-strip theorem, with `P` allowed to overlap a light bank and with no moment assumption.

## 3. A single infinitely fragmented admissible hub

Choose

`a_j = 6/(pi^2 j^2)`,  `I_j=[4j,4j+a_j]`,  `E=union_{j>=1} I_j`,

and let

`f_H = 1_E`.

The intervals are disjoint, `sum_j a_j=1`, and therefore `f_H` is a probability density satisfying the exact target hypothesis `0<=f_H<=1`.

For every `t in (0,1)`, the superlevel set `{f_H>t}` equals `E` up to null sets. Hence the fragmentation functional appearing in the fresh layer-cake extension is

`K(f_H) = sum_{j>=1} sqrt(a_j)
        = (sqrt(6)/pi) sum_{j>=1} 1/j
        = infinity`.                                                     (3.1)

Also `TV(f_H)=infinity`, since every component contributes two jumps. Thus this one admissible source law lies outside both the finite-`K` and finite-variation hub corollaries.

For a finite stress sequence, instead take

`E_N = union_{j=1}^N [4j,4j+1/N]`, `f_{H,N}=1_{E_N}`.

Then for every `t in (0,1)`,

`K(f_{H,N}) = N sqrt(1/N)=sqrt(N)`, `TV(f_{H,N})=2N`.                    (3.2)

So the guarantees obtained by summing interval-component estimates necessarily deteriorate like `sqrt(N)` on this sequence, even though the actual quadratic output below stays uniformly bounded.

Take, for definiteness, `P,U_i,V_i` all uniform on `[-1/2,1/2]`, mutually independent and independent of `H`. These are all target-admissible cap-one originals. No support condition is asserted in the theorem being studied; compact support is used only to provide one legal counterexample to an intermediate proof interface.

## 4. Fragmentation-insensitive uniform payment of the whole special family

The key point is to combine the fragmented physical hub with the pure longitudinal leakage original *before* paying any hub level-set geometry.

### 4.1 Three aggregate density caps

Because `sqrt(c)H` has density cap `c^{-1/2}` and convolution with an independent probability law cannot increase `L^infinity`,

`||p_Z||_infinity <= c^{-1/2}`.                                         (4.1)

This is uniform in `rho`, including the limit `rho -> 0`, and is completely insensitive to the number or arrangement of the components of the hub density.

For `Y`, isolate the first summand. The variable `U_1/8` has density cap `8`, and convolution with the other sixty-three summands cannot increase the cap. Hence

`||p_Y||_infinity <= 8`; similarly `||p_W||_infinity <= 8`.              (4.2)

No concentration theorem is needed for these coarse but absolute constants.

### 4.2 Elementary fractional-potential lemma

If a real random variable `S` has a probability density bounded by `K`, then for every `a in R`,

`E |S-a|^{-1/2} <= 2 sqrt(2K)`.                                         (4.3)

Indeed, among densities of mass one bounded by `K`, the integral against the decreasing kernel `|x-a|^{-1/2}` is maximized by filling the interval of length `1/K` centered at `a` at height `K`; its integral is exactly `2 sqrt(2K)`.

Let `Z,Y` be independent with density caps `K_Z,K_Y`. For every `s`, conditioning first on `Z=z` and applying (4.3) to `Y` gives

`E_Y |2zY-s|^{-1/2}
 <= (2|z|)^{-1/2} 2 sqrt(2K_Y)
 = 2 sqrt(K_Y) |z|^{-1/2}`.

Apply (4.3) once more, now to `Z` at `a=0`:

`sup_s E |2ZY-s|^{-1/2} <= 4 sqrt(2) sqrt(K_Z K_Y)`.                    (4.4)

This estimate does not require moments, support bounds, unimodality, or any conditional density supremum.

### 4.3 Square peel with the independent transverse bank

If `W` has density cap `K_W`, then `W^2` has density

`g(u) = [p_W(sqrt(u))+p_W(-sqrt(u))]/(2 sqrt(u)) <= K_W/sqrt(u)`, `u>0`.

With `T=2ZY`, independence of `W` from `(Z,Y)` gives for almost every `s`

`p_{Q_rho}(s)
 = E[g(s-T) 1_{T<s}]
 <= K_W E[(s-T)_+^{-1/2}]
 <= K_W E|s-T|^{-1/2}`.

Using (4.4), (4.1), and (4.2),

`||p_{Q_rho}||_infinity
 <= 4 sqrt(2) K_W sqrt(K_Z K_Y)
 <= 4 sqrt(2) * 8 * sqrt(8 c^{-1/2})
 = 128 c^{-1/4}
 < 128 (64/63)^{1/4}
 < 128.51`.                                                            (4.5)

This is uniform simultaneously in `0<=rho<1/64` and in the infinite fragmentation of the physical hub. It proves an endpoint-stable whole-density bound for this nontrivial pure-longitudinal near-coloop subfamily. In particular, the infinitely fragmented `f_H` from Section 3 is not a QFORM counterexample.

The proof is source-product valid throughout: the only independent objects used are functions of disjoint original-coordinate banks `({H,P})`, `(U_i)`, `(V_i)`.

## 5. Completed source results applied to actual inequalities

### 5.1 Required ruled-side theorem

The completed ruled-level-set theorem in the required source commit `e5f71d79eff325201dd0274053d20268ce65b837` applies directly because the nonzero spectrum is `(+1,+1,-1)`. Therefore, for every majority-sign level `s>=0`,

`p_{Q_rho}(s) <= pi sqrt(2) < 4.443`.                                   (5.1)

This is an actual inequality for the present family. Its proof in the source is dimension-free and product-valid through original-coordinate marginals; no post-rotation independence is assumed. The new work above concerns the endpoint mechanism needed on the other side and supplies the coarser global bound (4.5) for this special family.

### 5.2 Partner `fleet03/B10` result

For `0<rho<1/64`, the exact checks in Section 1 pass the partner r26 diffuse-leaf gate: every nonzero transverse leverage is `1/64<1/61`. Its completed positive-leakage projected-crossing estimate therefore gives the genuine inequality

`||p_{Q_rho}||_infinity < 16.652 rho^{-1/6}`.                           (5.2)

The partner bound is finite for every positive leakage but diverges at the endpoint. Equation (4.5) shows that this divergence is not intrinsic even for an infinitely fragmented physical hub when the leakage is purely longitudinal and can be recombined with the hub in an ORIGINAL-coordinate aggregate. The generic case still has same-bank transverse contamination, so (4.5) is not a proof of the full near-coloop collar.

### 5.3 Fresh two-bank strip theorem and the exact obstruction to its layer-cake completion

The fresh two-bank theorem proves, for independent light banks with planar density caps `M_A,M_B`, the slice Fourier estimate

`||g_t||_infinity <= sqrt(pi M_A M_B / |t|)`

and the resulting interval small-ball bound. Its hub extensions pay a superlevel fragmentation functional `K(f_H)`; finite variation gives `K(f_H)<=sqrt(TV(f_H)/2)`.

Our family meets the light-bank hypotheses with absolute constants. Split the `U` and `V` originals into two groups of thirty-two, put `P` in the first bank, and write `L=L_A+L_B`, `Vcan=V_A+V_B`. Each `L_A` or `L_B` contains a summand with coefficient `sqrt(c)/8`, so its one-dimensional density cap is at most `8/sqrt(c)`; each `V_A,V_B` has cap at most `8`. The `U` and `V` subcollections are independent, hence each planar `(L_j,V_j)` density has cap

`M_j <= 64/sqrt(c)`.                                                    (5.3)

Thus the fresh theorem is fully compatible with this source. But its finite-component/layer-cake corollary gives a guarantee proportional to `K(f_H)`: it grows like `sqrt(N)` for (3.2) and gives no finite conclusion for (3.1). In contrast, the direct product-preserving recombination (4.5) remains below `128.51` in all those cases.

Therefore the following proposed intermediate closure is false as a route to the unrestricted theorem:

`QFORM-CAPONE-HUB-COMPONENT-SUM-CLOSURE-v0`: "cap one alone supplies a uniform bound on the componentwise interval-layer-cake cost needed by the conditional-strip proof."

It fails already for the single density (3.1), where that cost is infinite. The failure is in the proof interface, not in QFORM.

## 6. What this changes

The earlier two-sheet stress test showed that hub-first absolute inverse-discriminant payment can diverge logarithmically while the actual density remains bounded. The present construction is orthogonal: it shows that even after replacing inverse-discriminant payment by the new conditional-strip interval estimate, summing the physical hub one component at a time can introduce an arbitrarily large or infinite artificial loss.

The special-family mechanism that succeeds is explicit: keep the physical hub `H` and the pure longitudinal source `P` together as `Z=sqrt(c)H+sqrt(rho)P`; use the untouched transverse original-coordinate banks only afterward. This makes both leakage size and hub fragmentation disappear from the density cap of `Z`.

For the generic near-coloop state, the longitudinal leaf variables also feed transverse coordinates after the required algebraic shears, and the same-bank remainder cannot simply be deleted or assumed independent. The first unpaid implication in Section 0 is therefore genuinely joint: manufacture a source-valid analogue of the aggregate `Z` while retaining enough transverse curvature to apply a fractional-potential/Fresnel payment without `rho^{-1/6}`, `K(f_H)`, `TV(f_H)`, or conditional-profile suprema.

## 7. Scope and integrity checks

- Exact target spectrum: yes, nonzero eigenvalues are exactly `{-1,1,1}`.
- Independent source laws: yes, only ORIGINAL physical coordinates are independent; no rotated/projected coordinates are declared independent.
- Density hypothesis: every physical original has density at most one.
- Hidden moments/support/log-concavity: none are used in the target statement. Compact uniform laws are chosen only for non-hub coordinates to instantiate one legal route-obstruction family; the hub itself is highly disconnected. The bound (4.5) uses only the displayed aggregate density caps.
- Continuity: separate. This report proves existence of an essential density for the displayed special family through convolution with `W^2`; it makes no unrestricted continuity claim.
- Full QFORM: still OPEN.

## 8. Source pins consumed

Required interactive source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `COUNTEREXAMPLE_SEARCH.md` Theorem C, applied in (5.1), together with the requested `RESULTS.md` and `FOURIER_ROUTE_REPORT.md`.

Partner: `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T181522Z-fleet03-B10-QFORM-r26/REPORT.md`, read from a later compatible repository state and applied in (5.2).

Fresh compatible strip result: `yspennstate/math-open-problems@5bb8c5faaf65393ba42f440dce575d8ffdaf1f52`, `proofnet24/QFORM-density/interactive/20260923T214500Z-two-bank-conditional-strip/{REPORT.md,QUASICONCAVE_HUB_ADDENDUM.md,FINITE_VARIATION_HUB_ADDENDUM.md}`, applied in (5.3) and stress-tested by (3.1)-(4.5).

Final source refresh before this write observed master `96b7296e7bb30bdddb70522eda0177190e316bc4`; no later partner B10 result than r26 was present there.
