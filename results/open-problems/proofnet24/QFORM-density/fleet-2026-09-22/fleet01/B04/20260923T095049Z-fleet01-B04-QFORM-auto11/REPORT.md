SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T09:50:49Z.
attacking: two disjoint aggregate product projections forming a definite 2D quadratic packet; exact shell-volume bound and integrated Fourier L2 estimate, compared on the same rotated target matrix with fleet02/B04 aggregate-square smoothing

# fleet01/B04 — definite aggregate-pair shell smoothing and Fourier L2


Outcome: **SUPPORTING THEOREM PROVED / EXPLICIT ROTATED-INDEFINITE TARGET ESTIMATE / INTEGRATED FOURIER L2 / FULL TARGET OPEN**. The theorem proves absolute continuity and an essentially bounded density in its scope. It does **not** prove continuity for arbitrary merely measurable cap-one input densities.

## 1. First unpaid implication attacked

The preceding B04 work paid one aggregate rank-one square followed by a rank-two residual packet. The next natural question is whether two independent *delocalized* original-coordinate product projections can be consumed together before selecting any physical coordinate. This is useful exactly where all physical diagonal coefficients may be `O(1/m)` but a two-dimensional aggregate quadratic packet is macroscopically definite.

The result below gives a target-scale bound with no dependence on bank cardinality and no reciprocal local coefficient. Its remaining connection to full QFORM is structural: one must force such a definite aggregate two-bank packet, or route the survivor into an already-paid indefinite/pair/hub/ridge endpoint.

## 2. Source-pinned input actually used

The designated partner result actually applied to an equation below is fleet02/B04's completed

`QFORM-DELOCALIZED-SQUARE-PAIRVOLUME-SPLICE-v1`,

source:

- repository `yspennstate/math-open-problems`,
- commit `ce94013cd8928e997a42341f11ea53dc58a98545`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260923T081907Z-r11/REPORT.md`.

Its theorem says that for a disjoint original-coordinate product bank `Z`, arbitrary residual-dependent shift `m`, residual quadratic `R`, and a residual physical cross block `M` with `E2=e2(M^T M)>0`,

`Q=a[c^T Z+m]^2+R`

satisfies

`||p_Q||_inf <= C_pair (|a| ||c||_2^2)^(-1/2) E2^(-1/8)`,       (2.1)

where

`C_pair=12*2^(4/3)*e^(5/24)=37.2419652609898...`.                (2.2)

The same source also records the product-projection density cap

`||p_(c^T Z)||_inf <= sqrt(2)/||c||_2`.                          (2.3)

A repository source-match search found the already-completed *physical-coordinate* definite principal-block shell theorem, but not the two-disjoint-aggregate-projection formulation proved below. The distinction is essential: the present theorem can keep all physical diagonal entries vanishing while `||c||_2,||d||_2` stay at target scale.

## 3. New theorem: two aggregate product banks form an exact definite shell smoother

Let `K,L,R` be pairwise disjoint sets of ORIGINAL coordinates. Write the independent product banks as `Z=(Z_k)_(k in K)`, `W=(W_l)_(l in L)`, and the remaining variables as `Y`. Every original coordinate has probability density at most one.

Let `c in R^K\{0}`, `d in R^L\{0}`, and define

`S=c^T Z`, `T=d^T W`, `U=(S,T)^T`.                               (3.1)

Let `B` be a real symmetric **definite** `2x2` matrix. Let `h(Y) in R^2` and `R0(Y) in R` be arbitrary measurable functions (in the ambient QFORM application they are the linear and residual quadratic terms induced after conditioning the other original coordinates). Put

`Q = U^T B U + 2 h(Y)^T U + R0(Y)`.                              (3.2)

### Theorem `QFORM-DEFINITE-AGGREGATE-PAIR-SHELL-v1`

The law of `Q` is absolutely continuous and

`boxed:
 ||p_Q||_infinity
 <= 2*pi / ( ||c||_2 ||d||_2 sqrt(|det B|) ).`                   (3.3)

Moreover, for `phi_Q(t)=E exp(itQ)`,

`boxed:
 int_R |phi_Q(t)|^2 dt
 <= 4*pi^2 / ( ||c||_2 ||d||_2 sqrt(|det B|) ),`                 (3.4)

and hence

`boxed:
 ||phi_Q||_2
 <= 2*pi (||c||_2||d||_2)^(-1/2)|det B|^(-1/4).`                (3.5)

No pointwise characteristic-function decay is asserted or used. Continuity of `p_Q` is not claimed.

### Proof

By the product-projection rearrangement estimate (2.3),

`L_S:=||p_S||_infinity <= sqrt(2)/||c||_2`,
`L_T:=||p_T||_infinity <= sqrt(2)/||d||_2`.                      (3.6)

Because the two banks are disjoint subsets of the original independent coordinates, `S` and `T` are independent. Therefore their joint density satisfies

`p_U(s,t) <= L_S L_T <= 2/(||c||_2||d||_2)`.                    (3.7)

Fix `Y=y`. Since `B` is invertible and definite, complete the square:

`U^TBU+2h(y)^TU
 =(U+B^(-1)h(y))^T B (U+B^(-1)h(y))
  -h(y)^TB^(-1)h(y).`                                           (3.8)

Translation of `U` preserves the joint density cap (3.7). If `B>0`, the sublevel ellipse satisfies exactly

`Leb{u:u^T B u <= r}=pi*r/sqrt(det B),  r>=0`.                  (3.9)

Consequently for every interval `I` of length `eta`, including intervals crossing zero,

`Leb{u:u^TBu in I} <= pi*eta/sqrt(det B).`                       (3.10)

If `B<0`, replace `B` by `-B`; the same estimate holds with `sqrt(|det B|)`. Thus uniformly in the conditioned value `y` and in the induced translation/output shift,

`P(Q in I | Y=y)
 <= L_S L_T * pi*eta/sqrt(|det B|)
 <= [2*pi/(||c||_2||d||_2 sqrt(|det B|))] eta.`                  (3.11)

Average over `Y`. The distribution function of `Q` is therefore Lipschitz with the displayed constant, so the output law is absolutely continuous and its Radon--Nikodym density is bounded a.e. by (3.3).

Since `p_Q` is a probability density and `p_Q in L^infinity`, it belongs to `L^2` and

`||p_Q||_2^2 <= ||p_Q||_infinity`.                               (3.12)

Plancherel in the convention `phi_Q(t)=int exp(itx)p_Q(x)dx` gives

`int |phi_Q(t)|^2 dt = 2*pi ||p_Q||_2^2`.                        (3.13)

Combine (3.3), (3.12), and (3.13) to obtain (3.4)-(3.5). QED.

### What the theorem pays and what it does not

It pays a macroscopically definite quadratic packet carried by two *aggregate independent product projections*. It does not select a physical coordinate, does not rotate the random inputs, and does not assume moments, compact support, connected support, identical laws, Gaussianity, or log-concavity.

The definiteness hypothesis is real: the planar shell area for an indefinite `2x2` form has a logarithmic singularity and cannot be bounded by the same area derivative. That signature must be handled by the existing pair-log / higher-dimensional smoothing mechanisms rather than silently absorbed here.

## 4. Genuinely rotated indefinite target family

For every integer `m>=2`, let

`c_m=d_m=m^(-1/2)(1,...,1) in R^m`,                              (4.1)

and define the two aggregate product projections

`S=c_m^T Z`, `T=d_m^T W`.                                        (4.2)

Take

`B=[[1,1/2],[1/2,1]],   det B=3/4`,                              (4.3)

and the physical `2x2` cross block

`M=[[5/4,3/4],[3/4,5/4]],`                                      (4.4)

whose singular/eigenvalue magnitudes are `2` and `1/2` and whose determinant is `1`.

For mutually independent original-coordinate banks `Z in R^m`, `W in R^m`, `X in R^2`, `Y in R^2`, set

`Q_m = S^2 + S*T + T^2 + 2 X^T M Y`.                            (4.5)

This is non-diagonal in the original product coordinates. In the `Z,W` banks every physical diagonal coefficient is only `1/m`, while every `Z-W` cross coefficient is `1/(2m)`. The deterministic spectrum of the full symmetric coefficient matrix is exactly

`{3/2, 1/2, +2, -2, +1/2, -1/2, 0^(2m-2)}.`                    (4.6)

Hence **exactly three** eigenvalues have modulus at least one: `3/2,+2,-2`. The form is therefore a genuine rotated indefinite instance of the owner's full spectral hypothesis for every `m`.

The new theorem uses `||c_m||=||d_m||=1` and `det B=3/4` to give, for every admissible product input law,

`boxed:
 ||p_(Q_m)||_infinity
 <= 4*pi/sqrt(3)
 = 7.255197456936871... .`                                      (4.7)

The integrated Fourier estimate is

`boxed:
 int |phi_(Q_m)(t)|^2 dt
 <= 8*pi^2/sqrt(3)
 = 45.585750062112446... ,`                                     (4.8)

so

`||phi_(Q_m)||_2 <= 6.751722007170648...`.                       (4.9)

No Monte Carlo input enters these claims.

## 5. Designated-partner theorem applied to the same actual inequality

Complete the aggregate definite packet as

`S^2+ST+T^2=(S+T/2)^2+(3/4)T^2`.                                (5.1)

Now regard the `Z` bank as the partner theorem's disjoint square bank. Its coefficient is `a=1`, `c=c_m`, and its residual-dependent shift is the actual function `m=T/2`. The residual is

`R=(3/4)T^2+2X^T M Y`.                                          (5.2)

The `X-Y` physical cross block is precisely (4.4), with

`E2=e2(M^TM)=det(M)^2=1`.                                       (5.3)

Therefore the completed fleet02/B04 theorem (2.1) applies at equation level and gives on this same target-valid matrix

`||p_(Q_m)||_infinity <=37.2419652609898...`                     (5.4)

uniformly in `m`. The new simultaneous-two-bank shell payment improves this same-matrix certificate by the factor

`37.2419652609898... /(4*pi/sqrt(3))
 =5.133142892669568...`.                                        (5.5)

The comparison is not a criticism of the partner theorem: that theorem handles arbitrary residual two-sided curvature and an aggregate square, whereas the new theorem exploits extra definiteness available jointly in the two aggregate projections.

## 6. Exact remaining implication

The new structural debt is

`QFORM-DEFINITE-AGGREGATE-PAIR-OR-INDEFINITE-ENDPOINT-ROUTING-v1`:

> Starting only from the three-large-eigenvalue hypothesis, find disjoint original-coordinate banks and product projections carrying a target-scale definite `2x2` aggregate quadratic matrix `B` with `||c||||d|| sqrt(|det B|)>=c0`, or prove that failure forces an already-paid indefinite pair-log, aggregate-square, ridge, grouped-hub, or higher-volume endpoint.

The theorem removes the need to select a large physical pivot in the definite aggregate branch, but it does not establish that such a branch must occur for every target matrix. Zero/near-zero local pivots and genuinely indefinite aggregate planes remain part of the global routing problem.

## 7. Status

- Full QFORM: **OPEN**.
- New theorem: proved supporting theorem in exact stated scope.
- Density regularity in new theorem: absolute continuity + essential bound.
- Continuity: **not proved** in this branch.
- Pointwise Fourier decay: neither used nor claimed.
- Designated partner fleet02/B04 result: applied to the same explicit matrix at (5.4).
- Native brain ingestion: **WITHOUT_VERIFIED_BRAIN**.
