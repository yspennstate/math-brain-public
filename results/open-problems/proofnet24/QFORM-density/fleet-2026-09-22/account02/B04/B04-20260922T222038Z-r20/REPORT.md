SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-22T22:20:38Z.
attacking: contamination-safe leakage-packet splicing using the partner overlap-safe square-plus-hyperbolic half-Riesz endpoint.

# account02/B04 r20 — one-sided contamination splice and a sharp obstruction to the two-sided half-Riesz shortcut

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Product Fourier rearrangement  
**Fresh owner control consumed:** revision `2026-09-22.15`; QFORM only.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository retrieval occurred, but no native learned-memory receiver/ingestion was observed.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED / FULL_TARGET_OPEN`.

## 1. Scope, corrections, and the unpaid implication attacked

The full target remains open. The inputs are independent original real coordinates with density caps at most one, and the symmetric physical matrix has at least three eigenvalues of modulus at least one. No moment, compact-support, log-concavity, diagonal-basis independence, post-rotation independence, arbitrary-joint coarea estimate, positive conditional projected-density moment, or law-uniform one-direction pointwise oscillatory decay is used.

The first unpaid implication inherited from the preceding B04 run was `QFORM-LEAKAGE-PACKET-CONTAMINATION-SPLICE-v1`: after splitting a leakage/transverse bank into disjoint original-coordinate packets, use the product structure without pretending the unwanted coefficients on those packets disappear.

This run pays the analytic subbranch in which, after the product-preserving split, one hyperbolic aggregate is allowed **arbitrary same-side contamination**, while the completed scalar-square shift may simultaneously depend on both hyperbolic aggregates. It also proves that the apparently natural extension to arbitrary contamination on **both** hyperbolic variables cannot be obtained through a standalone half-Riesz estimate: that intermediate statement is false, even inside an exact target-valid rotated indefinite matrix which is itself uniformly bounded by another grouped route.

### Source-pinned completed partner mathematics actually consumed

The named partner account03/B04 r19 is read from the immutable source

`yspennstate/math-open-problems@c273d6cdcd751214348ab9a4872c2126ea85cdbb`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/B04-20260922T215045Z-r19/REPORT.md`.

Its completed results used here are:

1. `QFORM-HYPERBOLIC-HALFRIESZ-v1`, with
   `H_6=10.618719667577919...` and
   `sup_t E|t-2c(U+alpha)(V+beta)|^{-1/2} <= H_6 |c|^{-1/2}`
   for independent cap-one `U,V`;
2. `QFORM-SQUARE-OVERLAP-HYPERBOLIC-v1`, which permits the completed-square shift to depend arbitrarily on both hyperbolic variables;
3. its three-disjoint-bank lift.

The bank projection input used in that lift is independently source-pinned to this slot's earlier report

`yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T181702Z-dac07509/REPORT.md`,

which records the original-coordinate product projection bound

`||p_(u^T X_I)||_infinity <= sqrt(2)/||u||_2`.

## 2. New rearrangement theorem: arbitrary contamination on one hyperbolic side

The next lemma is deliberately stated for non-unit density caps, because this makes the bank lift transparent.

### Theorem 2.1 — `QFORM-HYPERBOLIC-ONE-SIDED-CONTAMINATION-L3-v1`

Let `U,V` be independent real random variables with probability densities bounded by `M_U,M_V` respectively. Let `c!=0`, let `alpha,beta` be deterministic real numbers, and let `F` be an arbitrary measurable real function. Put

`T = 2c (U+alpha)(V+beta) + F(U).`                                  (2.1)

Then `T` is absolutely continuous and its density `g` satisfies

`boxed: ||g||_3 <= 3 (M_U M_V/|c|)^(2/3).`                         (2.2)

Consequently,

`boxed: sup_t E |t-T|^(-1/2) <= 8 sqrt(2) sqrt(M_U M_V/|c|).`      (2.3)

The same statement holds with the roles of `U,V` interchanged.

#### Proof of the L3 estimate

The deterministic translation `beta` can be absorbed into `F`, because

`2c(U+alpha)(V+beta)+F(U)
 =2c(U+alpha)V + [F(U)+2c beta(U+alpha)]`.

Set `X=U+alpha`; its density `f_X` is bounded by `M_U`. Conditional on `X=x!=0`, the output is an arbitrary translate of `2cxV`. Hence its conditional density `h_x` satisfies

`||h_x||_3
 = (2|c x|)^(-2/3) ||f_V||_3
 <= (2|c x|)^(-2/3) M_V^(2/3),`                                    (2.4)

because `int f_V^3 <= M_V^2 int f_V=M_V^2`.

Minkowski's integral inequality gives

`||g||_3
 <= (2|c|)^(-2/3) M_V^(2/3)
    int f_X(x)|x|^(-2/3) dx.`                                      (2.5)

Now use decreasing rearrangement / the bathtub principle. Among probability densities bounded by `M_U`, the integral against the symmetric decreasing kernel `|x|^{-2/3}` is maximized by filling the centered interval of length `1/M_U` at height `M_U`. Therefore

`int f_X(x)|x|^(-2/3) dx
 <= M_U int_{-1/(2M_U)}^{1/(2M_U)} |x|^(-2/3) dx
 = 3*2^(2/3) M_U^(2/3).`                                           (2.6)

Substitution in (2.5) cancels the factor `2^(2/3)` and proves (2.2).

This is a product-space decreasing-rearrangement estimate. It does not use a pointwise Fourier-decay assertion.

#### Proof of the half-Riesz estimate

Let `G=||g||_3`. For any center `t` and `R>0`, Hölder on the near region and total mass one on the far region give

`E|t-T|^(-1/2)
 <= G [int_{|x|<=R}|x|^(-3/4)dx]^(2/3) + R^(-1/2)
 = 4G R^(1/6)+R^(-1/2).`                                           (2.7)

Put `y=R^(1/6)`. The right side is `4Gy+y^{-3}` and is minimized at

`y=(3/(4G))^(1/4)`.

The minimum is

`4*3^(-3/4) (4G)^(3/4).`                                           (2.8)

Using (2.2),

`G^(3/4) <= 3^(3/4) sqrt(M_U M_V/|c|)`,

and (2.8) becomes exactly (2.3). QED.

### What is new relative to the two adjacent B04 endpoints

- The preceding account02/B04 one-clean-side theorem allowed arbitrary same-side residual dependence, but its completed-square shift did not overlap the opposite active bank.
- The partner account03/B04 r19 theorem allows the square shift to overlap both active variables, but its hyperbolic defect itself is an uncontaminated translated product.
- Theorem 2.1 plus the next theorem allows **both features simultaneously**: the square shift may reuse `U,V`, while an arbitrary function of one hyperbolic variable remains inside the residual defect.

## 3. Completed square + one-sided contaminated hyperbolic defect

### Theorem 3.1 — `QFORM-SQUARE-OVERLAP-ONE-SIDED-CONTAMINATION-v1`

Let `Z,U,V,W` be mutually independent, where `W` may be vector-valued. Assume scalar density caps

`||p_Z||_infinity<=M_Z`, `||p_U||_infinity<=M_U`, `||p_V||_infinity<=M_V`.

Let `a,c!=0`. Allow arbitrary measurable functions

`m=m(U,V,W)`, `alpha=alpha(W)`, `beta=beta(W)`,
`F=F(U,W)`, `R=R(W)`.

Define

`Q = a[Z+m(U,V,W)]^2
     +2c[U+alpha(W)][V+beta(W)] + F(U,W)+R(W).`                     (3.1)

Then `Q` is absolutely continuous and

`boxed: ||p_Q||_infinity
 <= 8 sqrt(2) M_Z sqrt(M_U M_V) / sqrt(|a c|).`                    (3.2)

The symmetric statement with arbitrary `F(V,W)` is also valid.

#### Proof

Condition on `(U,V,W)=(u,v,w)`. The translated original variable `Z+m(u,v,w)` still has density cap `M_Z`, so the conditional square density is bounded by

`M_Z |a|^(-1/2)|s|^(-1/2)`                                        (3.3)

on its appropriate half-line, and the indicator may be discarded for an upper bound.

For fixed `w`, put

`T_w=2c[U+alpha(w)][V+beta(w)] + F(U,w)`.

Averaging (3.3) over `U,V` gives, for a.e. output `q`,

`p_(Q|W=w)(q)
 <= M_Z |a|^(-1/2)
    E_{U,V}|q-R(w)-T_w|^(-1/2).`                                   (3.4)

Theorem 2.1 bounds the expectation uniformly in `q,w` by

`8 sqrt(2) sqrt(M_U M_V/|c|)`.

Average over `W` to obtain (3.2). Since the conditional square laws are absolutely continuous, so is the mixture. QED.

### Corollary 3.2 — three disjoint original-coordinate banks

Let `I_0,I_1,I_2` be disjoint original-coordinate banks and

`Z=z^T X_(I_0)`, `U=u^T X_(I_1)`, `V=v^T X_(I_2)`,
`s_0=||z||_2`, `s_1=||u||_2`, `s_2=||v||_2`.

The source-pinned product projection bound gives

`M_Z<=sqrt(2)/s_0`, `M_U<=sqrt(2)/s_1`, `M_V<=sqrt(2)/s_2`.

Hence every packet of the form (3.1) obeys

`boxed: ||p_Q||_infinity
 <= 16 sqrt(2) / [s_0 sqrt(s_1 s_2) sqrt(|a c|)].`                 (3.5)

This is an aggregate original-coordinate estimate: no individual physical matrix entry is inverted.

### Relation to the preceding leakage-packet split

The preceding B04 theorem `QFORM-ORTHOGONAL-LEAKAGE-SEPARATION-v1` produces disjoint original-coordinate leakage and transverse packets. Theorem 3.1 now closes the subbranch where, after choosing the scalar hyperbolic aggregates, all remaining contamination on one active packet is a measurable function of that scalar aggregate plus outside variables. Crucially the completed scalar square is still allowed to reuse **both** hyperbolic aggregates. The remaining debt is genuine extra active-projection dependence on both sides, not mere overlap of the scalar square.

## 4. Named-partner theorem applied to an actual family, then the new theorem pays contamination

For every integer `m>=2`, split `3m` original coordinates into three disjoint banks and let `r_0,r_1,r_2` be the corresponding flat unit vectors, each equal to `m^(-1/2)(1,...,1)` on its bank. Put

`Z=r_0^T X`, `U=r_1^T X`, `V=r_2^T X`.

For `0<=d<=1`, set

`Q_(m,d)=2(Z+U-V)^2+8UV+dU^2.`                                     (4.1)

The associated `3 x 3` active matrix is

`K_d = [[2,2,-2],[2,2+d,2],[-2,2,2]].`                             (4.2)

Its characteristic polynomial factors exactly as

`-(lambda-4)(d lambda-lambda^2+2lambda+8)`,                         (4.3)

so its three nonzero eigenvalues are

`4`, and `((d+2) +- sqrt((d+2)^2+32))/2`.                           (4.4)

At `d=1`, these are

`4`, `(3+sqrt(41))/2`, `(3-sqrt(41))/2`,

and the negative eigenvalue has modulus

`(sqrt(41)-3)/2 = 1.701562118716424... >1`.                         (4.5)

Thus every `A_(m,1)=[r_0 r_1 r_2]K_1[r_0 r_1 r_2]^T` is an exact target matrix. It is genuinely rotated and indefinite. Moreover **every physical entry is nonzero** and has magnitude `2/m` or `3/m`; hence all local coefficients vanish as `m->infinity`.

#### Actual partner inequality at `d=0`

When `d=0`, this is exactly the partner r19 family

`Q_(m,0)=2(Z+U-V)^2+8UV`.

Applying account03/B04 r19 Corollary 5.1 with `a=2`, `c=4`, and `s_0=s_1=s_2=1` gives

`boxed: ||p_(Q_(m,0))||_infinity
 <= H_6/sqrt(2)
 = 7.508568684463308... .`                                         (4.6)

This is the required compatible completed partner result applied to an actual all-input-law inequality.

#### New contaminated inequality at `d=1`

For `d=1`, the extra term `F(U)=U^2` is exactly one-sided contamination not covered by r19. Corollary 3.2 gives, uniformly in `m` and over every admissible product input law,

`boxed: ||p_(Q_(m,1))||_infinity <= 8.`                            (4.7)

Thus a genuinely rotated dense indefinite target family with all physical entries tending to zero remains uniformly controlled after adding nontrivial same-bank quadratic contamination to one hyperbolic side.

## 5. Source-valid counterexample: arbitrary two-sided contamination destroys the half-Riesz interface

The most tempting next inference is false.

### Proposition 5.1 — `QFORM-HYPERBOLIC-TWOSIDED-HALFRIESZ-UNIFORM-FALSE-v1`

There is no universal finite constant `C` such that, for all independent cap-one `U,V`, all measurable `F,G`, and fixed nonzero `c`,

`sup_t E|t-[2cUV+F(U)+G(V)]|^(-1/2) <= C |c|^(-1/2).`              (5.1)

#### Proof

Take `c=1`, let `U,V` be independent uniform variables on `[-1/2,1/2]`, and choose

`F(U)=U^2`, `G(V)=V^2`.

Then

`2UV+U^2+V^2=(U+V)^2.`                                              (5.2)

The sum `S=U+V` has triangular density

`p_S(s)=1-|s|`, `|s|<=1`.

Therefore at `t=0`,

`E|t-S^2|^(-1/2)
 = E|S|^(-1)
 = 2 int_0^1 (1-s)s^(-1) ds
 = infinity.`                                                       (5.3)

So the half-Riesz bridge itself fails under arbitrary contamination on both active scalar sides. QED.

### The obstruction already occurs inside an exact target-valid rotated indefinite form

Introduce two further independent original coordinates `Z,W` and consider

`Q_* = Z^2 + U^2+2UV+V^2 - W^2
     = Z^2 + (U+V)^2 - W^2.`                                       (5.4)

Its physical matrix in `(Z,U,V,W)` is

`A_*=[[1,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,-1]]`,                 (5.5)

with exact spectrum

`{-1,0,1,2}`.                                                       (5.6)

Hence it satisfies the full target spectral hypothesis and is genuinely rotated and indefinite.

Yet the full target law is uniformly benign. For **arbitrary** cap-one independent `U,V`, the convolution `S=U+V` has density cap at most one. It is independent of `Z,W`. The square-density bound gives

`p_(Z^2)(x)<=x^(-1/2) 1_{x>0}` and
`p_(S^2)(x)<=x^(-1/2) 1_{x>0}`.

Therefore

`||p_(Z^2+S^2)||_infinity
 <= int_0^t x^(-1/2)(t-x)^(-1/2)dx
 = pi`,                                                            (5.7)

and convolution with the independent probability law of `-W^2` cannot increase the supremum. Thus

`boxed: ||p_(Q_*)||_infinity <= pi`                                (5.8)

for every admissible product input law, although for the uniform `U,V` choice the intermediate half-Riesz quantity in (5.3) is infinite.

This is a counterexample only to the **two-sided-contamination half-Riesz routing mechanism**, not to QFORM. It shows that a proof must sometimes keep another square/grouped smoothing factor alive rather than requiring a standalone half-Riesz bound for the contaminated defect.

## 6. First unpaid implication after this run

`QFORM-TWOSIDED-CONTAMINATION-JOINT-SPLICE-v1`:

Starting from the disjoint leakage/transverse packets already guaranteed by `QFORM-ORTHOGONAL-LEAKAGE-SEPARATION-v1`, route the remaining state when **both** active sides carry genuine extra active-projection contamination. Theorem 3.1 pays one-sided scalar contamination even with complete square overlap. Proposition 5.1 proves that the remaining branch cannot be closed by first demanding a standalone half-Riesz estimate for an arbitrarily two-sided contaminated hyperbolic defect.

A valid next mechanism therefore has to do at least one of the following before taking a reciprocal singular kernel:

1. preserve a second independent square/grouped factor and smooth jointly, as the exact target family (5.4) demonstrates;
2. route one side into an already completed rank-two/ridge/multi-bank endpoint; or
3. obtain a genuinely joint product-space Fourier/rearrangement estimate for the two contaminated packets.

This is a narrower and source-valid frontier than the previous generic `LEAKAGE-PACKET-CONTAMINATION-SPLICE` statement.

## 7. Exact computation used

The immutable checker `CHECK.py` in this run directory contains exactly the symbolic/numerical verification used for (4.3)-(4.7) and (5.6). Its saved output is `CHECK_OUTPUT.txt`:

```text
charpoly = -(lambda - 4)*(d*lambda - lambda**2 + 2*lambda + 8)
d1 exact eigenvalues = ['3/2 + sqrt(41)/2', '3/2 - sqrt(41)/2', '4']
d1 numeric eigenvalues = [-1.7015621187164243, 4.0, 4.701562118716424]
d1 negative magnitude = 1.7015621187164243
partner d0 three-bank bound = 7.508568684463308
new d1 three-bank bound = 8.0
two-sided counterexample charpoly = lambda*(lambda - 2)*(lambda - 1)*(lambda + 1)
two-sided counterexample eigenvalues = [-1.0, 0.0, 1.0, 2.0]
target-family direct grouped bound = 3.141592653589793
```

## 8. Status

- Full QFORM conjecture: **OPEN**.
- `QFORM-HYPERBOLIC-ONE-SIDED-CONTAMINATION-L3-v1`: **PROVED in this report**.
- `QFORM-SQUARE-OVERLAP-ONE-SIDED-CONTAMINATION-v1`: **PROVED in this report**.
- `QFORM-HYPERBOLIC-TWOSIDED-HALFRIESZ-UNIFORM-FALSE-v1`: **REFUTED by exact source-valid construction**.
- Named partner account03/B04 r19: **READ FROM IMMUTABLE SOURCE AND APPLIED** to (4.6).
- No claim of a full solution, continuity of the final density, novelty outside this programme, or native learned-memory use is made.
