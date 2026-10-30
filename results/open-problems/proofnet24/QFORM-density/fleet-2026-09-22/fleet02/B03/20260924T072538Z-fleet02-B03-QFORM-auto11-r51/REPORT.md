SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-24T07:25:38Z.
attacking: complementary weighted time after source separation — pair the newest fresh-hub negative-half Plancherel resource with an aggregate two-slope positive-half resource, and quantify why local 2x2-minor payment is the wrong scale.

# fleet02/B03 r51 — aggregate positive-half slope compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING WEIGHTED-TIME COMPILER + TARGET-VALID LINEAR SMALL-BALL FAMILY + LOCALIZATION OBSTRUCTION / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

After the already-paid physical-E3, grouped-hub, finite-carrier, and aggregate rank-two exits, the remaining B03 debt is now a **source-disjointification / partial-overlap bridge**. One wants to expose either

1. a genuine original-coordinate one-hub random-slope packet furnishing the negative-half collision energy, source-disjoint from an aggregate two-hub/two-slope packet furnishing a positive-half energy; or
2. a full three-dimensional joint random-slope packet; or
3. another already-paid aggregate receiver.

The hard residue is partial source overlap: rank information alone need not supply a bounded 3D slope density, while the live correction `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` rules out closing the overlap by first taking the absolute mixed norm `int |t|^{-1/2} ||G_t||_2 dt`. Shared sources must stay coupled until an additional orthogonality/positive-weight resource is exposed.

## 2. Aggregate two-slope positive-half corollary

### Proposition 2.1 — `QFORM-TWO-SLOPE-POSHALF-PLANCHEREL-v1`

Let `H=(H_1,H_2)` have independent real densities bounded by one and be independent of an arbitrary random object `W`. Let `L=L(W) in R^2` have a Lebesgue density bounded by `M`. Let `B` be any real symmetric `2x2` matrix and `R=R(W)` arbitrary, with no independence assumed between `L` and `R`. Put

`T = H^T B H + 2 L^T H + R`.

Then for every `t != 0`,

`|phi_T(t)|^2 <= min{1, pi^2 M |t|^{-2}}`,

and consequently

`boxed: A_+(T):=int_R |t|^(1/2)|phi_T(t)|^2 dt <= (16/3) pi^(3/2) M^(3/4).`

### Proof

For fixed `t`, define

`g_t(h)=f_{H_1}(h_1)f_{H_2}(h_2) exp(i t h^T B h)`.

Conditioning on `W` and applying Cauchy--Schwarz exactly as in random-slope Plancherel gives

`|phi_T(t)|^2 <= E |hat g_t(2tL)|^2 <= M int_R2 |hat g_t(2tl)|^2 dl`.

The change `xi=2tl` and two-dimensional Plancherel yield

`int |hat g_t(2tl)|^2 dl = (2pi)^2/(2|t|)^2 * int f_{H_1}^2 f_{H_2}^2 <= pi^2 |t|^{-2}`,

because `int f_{H_j}^2 <=1`. This proves the squared-characteristic envelope. Put `K=pi^2 M`. Its crossover is `T_0=K^(1/2)=pi M^(1/2)`, and direct integration gives

`int_R |t|^(1/2) min(1,K|t|^{-2}) dt`
`=2[(2/3)T_0^(3/2)+2K T_0^(-1/2)]`
`=(16/3)K^(3/4)`.

QED.

This is the positive-half weighted corollary of the completed two-dimensional random-slope Plancherel mechanism; no singular-vector coordinate is declared probabilistically independent.

## 3. Splice with the newest designated partner result

The newest compatible fleet03/B03 result is r50, `QFORM-FRESH-HUB-SLOPE-PLANCHEREL-v1`. In its notation, for

`S=aH_0^2+2 gamma H_0 L_0+R_0`,

with a genuine cap-one hub `H_0`, scalar slope-density cap `M_1`, and arbitrary same-source `R_0`, it proves

`A_-(S):=int |t|^(-1/2)|phi_S(t)|^2 dt <= 8 sqrt(pi M_1/|gamma|)`.

It also proves the complementary-weight splice: if `S,T` are independent, then

`||p_(S+T)||_infinity <= (2pi)^(-1) sqrt(A_-(S)A_+(T))`.

Writing `K_1=M_1/|gamma|` and letting `K_2` denote the effective two-slope density cap in Proposition 2.1, substitution gives the explicit compiler

`boxed: ||p_(S+T)||_infinity <= 4 sqrt(2/3) K_1^(1/4) K_2^(3/8).`

The characteristic function is in `L^1`, so this branch actually has a continuous `C_0` density. This is an equation-level application of r50, not a citation-only handoff.

## 4. Exact target family: aggregate slope wins while every local minor vanishes

Let `n>=4` be even and let all displayed coordinates be genuine original independent cap-one sources. Define

`v_1=n^(-1/2)(1,...,1)`,
`v_2=n^(-1/2)(1,...,1,-1,...,-1)`,

with `n/2` plus and `n/2` minus signs, and set

`Q_n = 2H_0 Z_0 + 2H_1 <v_1,Y> + 2H_2 <v_2,Y>.`

The three crossing singular values are exactly `1,1,1`, on mutually orthogonal coefficient modes, so the nonzero spectrum of the symmetric coefficient matrix is

`boxed: {+1,+1,+1,-1,-1,-1}.`

Thus every `Q_n` lies strictly inside the owner target.

Split `Q_n=S+T` with

`S=2H_0 Z_0`,
`T=2H_1<v_1,Y>+2H_2<v_2,Y>`.

These two scalar packets are independent. The partner r50 theorem applies to `S` with `gamma=1`, scalar slope `Z_0`, and `M_1=1`; hence `K_1=1` and

`A_-(S)<=8 sqrt(pi)`.

For the two-slope packet put

`L=(<v_1,Y>,<v_2,Y>).`

The completed two-dimensional product-projection estimate used in the pinned `e5f71d79...` package gives `||p_L||_infinity<=2`; this uses the original product source and does not assert independence after rotation. Proposition 2.1 therefore gives `K_2<=2`, and the splice yields

`boxed: ||p_(Q_n)||_infinity <= 4 sqrt(2/3) 2^(3/8) = 2^(23/8)/sqrt(3) = 4.235460249537537... .`

Hence every interval `I` satisfies

`boxed: P(Q_n in I) <= 4.235460249537537 |I|.`

The family has a continuous `C_0` density by the same weighted splice.

## 5. Assigned whole-copy integral

Because `|phi_T|<=1`, source independence also gives the immediate dimension-free collision-energy bound

`boxed: int_R |t|^(-1/2)|phi_(Q_n)(t)|^2 dt <= A_-(S) <= 8 sqrt(pi) = 14.179630807244127... .`

Using only the whole-output independent-copy identity

`|phi_(Q_n)(t)|^2 = E exp(i t(Q_n-Q_n'))`

and the positive Riesz identity,

`boxed: E|Q_n-Q_n'|^(-1/2) <= 4 sqrt(2) = 5.656854249492381... .`

No coordinatewise `X-X'` variable is separated from its conjugate `X+X'`. From the density bound and convolution,

`boxed: P(|Q_n-Q_n'|<=epsilon) <= 8.470920499075074 epsilon.`

## 6. Source-valid obstruction to physical-minor localization

For the aggregate `2xn` crossing matrix `V` with rows `v_1^T,v_2^T`, every physical `2x2` minor is either zero or has determinant modulus `2/n`. Thus every fixed two-leaf localization sees determinant scale tending to zero, even though the complete two-dimensional slope map has orthonormal rows and its output density cap stays at most two. A determinant-paid positive-half compiler based on one such local minor necessarily deteriorates polynomially in `n`, whereas the aggregate slope compiler above stays at `4.23546...`.

The required pinned `e5f71d79eff325201dd0274053d20268ce65b837` package was also applied to this same family. Its completed Theorem B gives

`||p_Q||_infinity <= 2 sqrt(2pi) sum_i ||P e_i||`,

where `P` is the range projection. Here the four hub coordinates `H_0,Z_0,H_1,H_2` each have projection norm one, while every leaf coordinate has projection norm `sqrt(2/n)`. Consequently

`boxed: ||p_(Q_n)||_infinity <= 2 sqrt(2pi)(4+sqrt(2n)).`

This is a valid inequality, but diverges like `sqrt(n)` on a family for which the source-separated aggregate weighted-time proof gives the uniform `4.23546...` bound. It is therefore an actual obstruction to treating range-projection mass or one physical minor as the final scale.

## 7. Correction-aware conclusion

The live correction `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` is respected rather than bypassed: the proof above never integrates an absolute fiber mixed norm through a shared source. It first obtains `A_-` and `A_+` on **source-disjoint scalar packets** and only then uses Cauchy--Schwarz in time. Thus the logarithmic fiber obstruction does not apply.

The unrestricted conjecture remains OPEN, and unrestricted continuity remains OPEN. The useful new debt is structural: prove a product-preserving source-disjointification/partial-overlap theorem that exposes the one-hub negative-half packet and the aggregate two-slope positive-half packet at uniform scale, or routes the overlap-heavy case to an already-paid three-slope/grouped-carrier receiver.

Sources consumed: fresh owner controls and live correction inbox; pinned `e5f71d79eff325201dd0274053d20268ce65b837` `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`; newest compatible fleet03/B03 r50 report. Narrow publication review found no credentials, scheduler identifiers, machine paths, or unrelated private data in this report.
