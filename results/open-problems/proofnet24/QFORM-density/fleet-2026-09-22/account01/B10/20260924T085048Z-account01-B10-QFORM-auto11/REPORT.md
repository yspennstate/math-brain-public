SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-24T08:50:48Z.
attacking: the near-coloop two-sheet survivor by a real-space parabolic pullback receiver; convert the final `V^2` curvature into an integrable `|L|^{-3/4}` singularity while retaining a source-provenance sectional mixed norm.

# account01/B10 — parabolic pullback turns the hyperbolic logarithm into a sectional `L^1_z L^2_v` debt

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T085048Z-account01-B10-QFORM-auto11`  
Assignment: rank-three coupled case  
Status: `NEW_PARABOLIC_PULLBACK_RECEIVER / NEW_EXACT-NULL_COROLLARY / NEW_INTERFACE_COUNTEREXAMPLE / PARTNER_RESULT_APPLIED / FULL_EXACT_RANK3_OPEN / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and mechanism change

Fresh `math-research-brain` controls keep all work on the full QFORM target under OWNER CONTROL revision `2026-09-22.15`; the full conjecture and the full continuity conclusion remain open. The live corrections against pointwise quadratic van der Corput, post-rotation independence, arbitrary-joint coarea, conditional-cap-as-independence, fiber suprema, and full absolute phase-Wiener receivers are retained.

The immediate predecessor `account01/B10` Fourier mechanism reduced the harmonic near-coloop endpoint to the dynamic amplitude

`phi_Q(t)=int exp(i t v^2) g_t(v) dv`

and proved useful `L^1/L^2/L^infinity` bounds on `g_t`, but those norms alone cannot exclude exact quadratic anti-phase alignment. After the prescribed repeated source-overlap/Fourier attempts, this run changes mechanism on the SAME target: work directly with the physical output density and spend the `V^2` curvature before taking any fiber supremum.

The newest completed designated partner input consumed is

`yspennstate/math-open-problems@174f2ac95a7e63dc88172bc6fcf5b319e8613d44`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260924T081305Z-account02-B10-QFORM-r12/REPORT.md`.

It gives the exact target-valid harmonic survivor

`Q=2(sqrt(c)H+sqrt(rho)Z)L+V^2`,

with `0<rho<1/64`, `c=1-rho`, `H` one ORIGINAL coordinate independent of the entire leaf product bank, and `(Z,L,V)` three orthogonal linear forms of that SAME leaf bank. It also proves that a bare joint-density cap cannot control the final curved marginal. The theorem below keeps exactly the extra fixed-kernel structure supplied by the independent hub.

## 2. A scalar square-pullback lemma

### Lemma 2.1 — `QFORM-SQUARE-PULLBACK-L2-v1`

Let `f` be any probability density on `R` satisfying `0<=f<=K`. For every `A!=0` and `b in R`,

`boxed: int_R f((b-v^2)/A)^2 dv <= 2 K^(3/2) |A|^(1/2).`             (2.1)

No moment, support, connected-support, smoothness, or log-concavity assumption is present.

### Proof

Since `f^2<=K f`, it is enough to bound the corresponding `L^1` pullback. Scale `v=sqrt(|A|)x`. Depending on the sign of `A`, the remaining integral is one of

`int f(c-x^2) dx`,   `int f(c+x^2) dx`.

For the first sign,

`int_R f(c-x^2) dx = int_{u<c} f(u)(c-u)^(-1/2) du`;                (2.2)

for the second sign the same formula holds on `u>c` with `(u-c)^(-1/2)`. Under `0<=f<=K` and `int f=1`, the decreasing-kernel bathtub bound puts density `K` on the interval of length `1/K` adjacent to the singular endpoint, giving

`sup_c int f(c plus_or_minus x^2) dx <= 2 sqrt(K)`.                 (2.3)

Multiplying by `K` from `f^2<=Kf` and by `|A|^(1/2)` from the scaling proves (2.1). QED.

## 3. Main new receiver: a scale-stable mixed sectional norm

Let `H` be independent of the entire vector `(Z,L,V)`. Assume `H` has density `f_H` with

`||f_H||_infinity<=K_H`,

and `(Z,L,V)` has a joint density `varrho(z,l,v)`. Let `s>0`, `a in R`, and

`Q=2(sH+aZ)L+V^2`.                                                   (3.1)

For `R>0` define the weighted sectional mixed norm

`M_R(varrho)
 := int_{0<|l|<=R} |l|^(-3/4)
      [ int_R ( int_R varrho(z,l,v)^2 dv )^(1/2) dz ] dl`.         (3.2)

### Theorem 3.1 — `QFORM-PARABOLIC-PULLBACK-SECTIONAL-RECEIVER-v1`

Under the hypotheses above, `Q` is absolutely continuous and, for every `R>0`,

`boxed:
 ||p_Q||_infinity
 <= 2^(-1/4) K_H^(3/4) s^(-3/4) M_R(varrho)
    + K_H/(2sR).`                                                   (3.3)

The estimate is **uniform in the longitudinal leakage `a`**. Thus it remains stable as `a downarrow0`; no small coefficient is deleted and no moment of `Z` is paid.

### Proof

Because `(Z,L,V)` has a density, `P(L=0)=0`. Conditional on `(Z,L,V)=(z,l,v)` with `l!=0`, the map

`h -> 2(s h+a z)l+v^2`

is affine with derivative `2sl`. Hence Tonelli gives the density representative

`p_Q(q)=int varrho(z,l,v) [2s|l|]^(-1)
          f_H((q-2azl-v^2)/(2sl)) dz dl dv`.                       (3.4)

Fix `(z,l)` and put `A=2sl`, `b=q-2azl`. Cauchy-Schwarz in the **curved variable `v`**, followed by Lemma 2.1, gives

`int varrho(z,l,v) f_H((b-v^2)/A) dv`

` <= (int varrho(z,l,v)^2 dv)^(1/2)
      (int f_H((b-v^2)/A)^2 dv)^(1/2)`

` <= sqrt(2) K_H^(3/4) |A|^(1/4)
      (int varrho(z,l,v)^2 dv)^(1/2).`                             (3.5)

Multiplying by `|A|^(-1)` turns the hyperbolic singularity into

`sqrt(2)|2sl|^(-3/4)
 =2^(-1/4)s^(-3/4)|l|^(-3/4)`.                                    (3.6)

Integrating (3.5) on `0<|l|<=R` proves the first term of (3.3).

For `|l|>R`, use only `f_H<=K_H` in (3.4). Integrating `varrho` in `(z,v)` gives the marginal density `p_L(l)`, so

`int_{|l|>R} ... <= K_H/(2s) int_{|l|>R} p_L(l)/|l| dl
                  <= K_H/(2sR).`                                  (3.7)

Combining (3.6)-(3.7) proves (3.3). QED.

### What the theorem actually buys

Conditioning on the hub alone gives the familiar nonintegrable `|L|^(-1)` envelope. The square curvature plus one Cauchy-Schwarz step changes it to the locally integrable `|L|^(-3/4)` singularity. The remaining quantity is no longer a fiber supremum or a conditional density cap: it is the averaged original-projection sectional norm `M_R(varrho)`. This is a strictly different proof interface.

## 4. Exact-null / no-longitudinal-leakage corollary

When `a=0`, `Z` disappears before any estimate. Let `g(l,v)` be the joint density of `(L,V)`, assume

`||g||_infinity<=K_2`,   `||p_L||_infinity<=K_L`.                  (4.1)

Then

`||g(l,.)||_2^2 <= K_2 p_L(l) <= K_2 K_L`,                        (4.2)

so

`int_{|l|<=R}|l|^(-3/4)||g(l,.)||_2 dl
 <=8 sqrt(K_2K_L) R^(1/4).`                                       (4.3)

Theorem 3.1 therefore gives

`||p_Q||_infinity
 <=2^(11/4) K_H^(3/4)s^(-3/4)(K_2K_L)^(1/2) R^(1/4)
   +K_H/(2sR).`                                                     (4.4)

Optimizing in `R` yields the closed-form bound

`boxed:
 ||p_Q||_infinity
 <=5*2^(2/5) K_H^(4/5)s^(-4/5)(K_2K_L)^(2/5).`                    (4.5)

For a genuine cap-one ORIGINAL product source with `H` one original coordinate and `(L,V)` an orthonormal two-dimensional projection, the standard source-valid marginal bounds used in the completed fleet work give

`K_H<=1`, `K_L<=sqrt(2)`, `K_2<=2`.                                (4.6)

Thus

`boxed: ||p_Q||_infinity <=10 s^(-4/5).`                            (4.7)

In particular if `s=sqrt(c)` with `c>63/64`, the right side is below `10.064`; at the exact physical-coloop endpoint `c=1` it is at most `10`.

This branch proves an **essentially bounded density**. No continuity claim is made from this argument.

## 5. Ordinary joint/marginal caps cannot pay `M_R`

The new receiver deliberately leaves product provenance visible. That is necessary: even simultaneously bounding the full density and every coordinate one- and two-dimensional marginal does not bound `M_R`.

### Proposition 5.1 — `QFORM-SECTIONAL-MIXED-NORM-NOT-JOINT-CAPS-v1`

For every integer `N>=1` there is a probability density `varrho_N(z,l,v)` satisfying

- `0<=varrho_N<=1`;
- every scalar coordinate marginal has density cap at most one;
- every coordinate-pair marginal has density cap at most one;

but

`boxed: M_1(varrho_N)=4 sqrt(N).`                                   (5.1)

### Proof

Let

`I_k=(k,k+1)`,   `J_k=(k,k+1/N)`, `k=1,...,N`,

and put

`varrho_N(z,l,v)=1_{0<l<1} sum_{k=1}^N 1_{I_k}(z)1_{J_k}(v).`       (5.2)

The boxes are disjoint and have total volume

`N * 1 * 1 * (1/N)=1`,

so this is a probability density capped by one. Direct integration gives

`p_L=1_(0,1)`,
`p_Z=(1/N) sum_k 1_{I_k}`,
`p_V=sum_k 1_{J_k}`,
`p_(Z,L)=(1/N)1_(0,1)(l)sum_k1_{I_k}(z)`,
`p_(L,V)=1_(0,1)(l)sum_k1_{J_k}(v)`,
`p_(Z,V)=sum_k1_{I_k}(z)1_{J_k}(v)`,                                (5.3)

so all listed caps are at most one. Yet for every `l in(0,1)` and every `z in union I_k`,

`(int varrho_N(z,l,v)^2 dv)^(1/2)=N^(-1/2)`.                       (5.4)

The total `z`-length is `N`, hence the inner `L^1_z L^2_v` norm equals `sqrt(N)`. Therefore

`M_1(varrho_N)=sqrt(N) int_0^1 l^(-3/4) dl=4sqrt(N)`.               (5.5)

QED.

This is **not** a QFORM counterexample: `varrho_N` is not asserted to be the orthogonal projection of an original independent product law. It is an exact falsifier of a weaker proof interface. It strengthens the partner's curved-cap warning in exactly the norm exposed by Theorem 3.1.

## 6. Designated partner result applied at an actual target inequality

Apply Theorem 3.1 to the latest completed `account02/B10` harmonic frame. Its target-valid variables satisfy

`Q=2(sqrt(c)H+sqrt(rho)Z)L+V^2`,
`0<rho<1/64`, `c=1-rho>63/64`,                                    (6.1)

and `(Z,L,V)` is the genuine three-dimensional linear projection of the SAME original leaf product vector. Let `varrho_harm` denote that actual projection density. With `K_H<=1` and `s=sqrt(c)`, (3.3) becomes, for every `R>0`,

`boxed:
 ||p_Q||_infinity
 <=2^(-1/4)c^(-3/8) M_R(varrho_harm)
   +1/(2 sqrt(c) R).`                                              (6.2)

This is the required actual application of a completed partner result: the partner supplies the exact harmonic target family and original-coordinate provenance, and the new receiver turns its remaining two-sheet endpoint into the concrete source-valid inequality (6.2). The bound has **no inverse power or logarithm of `rho`**.

The same partner report already pays the majority-sign levels of this signature by

`p_Q(q)<=pi sqrt(2)<4.443` for `q>=0`.                              (6.3)

Thus (6.2) is most relevant to the still-unpaid minority/two-sheet side. It does not assume `Z,L,V` are independent.

## 7. First unpaid implication

The remaining source-level debt is now

`QFORM-PRODUCT-PROJECTION-SECTIONAL-L1L2-v1`:

> For the genuine near-coloop leaf law `varrho_harm` (or, more generally, the corresponding Parseval product projection in the rank-three coupled collar), prove a dimension-free bound for the scale-local sectional quantity
> 
> `M_1(varrho)=int_{0<|l|<=1}|l|^(-3/4) int dz ||varrho(z,l,.)||_2 dl`,
> 
> using that `(Z,L,V)` are simultaneous linear forms of independent cap-one ORIGINAL coordinates.

A universal bound on `M_1` would close (6.2) immediately with a universal constant (take `R=1`). Proposition 5.1 proves that this cannot follow from ordinary finite-dimensional density caps alone. The needed estimate must use source-level product structure, e.g. a mixed-norm Brascamp-Lieb/Finner inequality, a collision estimate retaining original-coordinate factors, or an equivalent two-copy argument.

This real-space debt is equivalent in purpose to the partner's curved-complex-section endpoint, but it has two advantages: the square curvature has already reduced the singularity from `|L|^(-1)` to integrable `|L|^(-3/4)`, and the longitudinal leakage parameter has disappeared from the constant.

## 8. Status

- `QFORM-SQUARE-PULLBACK-L2-v1`: PROVED supporting lemma.
- `QFORM-PARABOLIC-PULLBACK-SECTIONAL-RECEIVER-v1`: PROVED supporting theorem.
- exact-null/no-longitudinal-leakage corollary: PROVED essential density bound (4.5), including target-valid product-projection specialization (4.7).
- `QFORM-SECTIONAL-MIXED-NORM-NOT-JOINT-CAPS-v1`: PROVED exact counterexample to the weaker joint/marginal-cap interface; NOT a QFORM counterexample.
- latest `account02/B10` harmonic result applied at the actual target inequality (6.2).
- arbitrary mixed-row exact rank three: OPEN.
- full QFORM: OPEN / NOT PROVED / NOT DISPROVED.
- full-target continuous density: OPEN; this run proves absolute continuity and essential boundedness only in the stated paid branch.
- repository transport was used; no authenticated native learned-memory receiver was observed: `WITHOUT_VERIFIED_BRAIN`.

No scheduler/task/cadence, email, notification, public-release, permission, cross-account-authentication, paid-model/API, or remote-workflow change was made.
