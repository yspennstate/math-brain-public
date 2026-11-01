Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime does not expose authenticated GPT-6/maximum-effort attestation.

# P09 progress-first run — KKT-selected local zonotopes, a multiscale dictionary inequality, and an unavoidable sqrt(log d) loss for every tensor order at p=2

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic symmetric tensors. The fixed full-source metric is unchanged in the unresolved regime `2 <= p < 2r`:

```text
old arbitrary exponent = 1/2 - 1/(2r),
new arbitrary exponent = 1/2 - 1/(2r),
target exponent        = 1/2 - 1/p.
```

The mathematical progress is different from the predecessor's zonotopal transverse-area calculation. The predecessor suggested trying to sparsify the transverse area of local switching models. This run shows that **pointwise transverse-area sparsification is not the real missing lemma**: every tensor already has a canonical local coordinate-tangent zonotope whose radius is `O_r(S)`, whose mean Gaussian width is `O_r(d^(1/2-1/p) S)`, and whose transverse-area energy is automatically at the conjectured squared scale. At an actual maximizer, KKT makes that local zonotope expose exactly the original tensor value.

The remaining obstruction is therefore the **selection complexity among many locally cheap zonotopes**. A new finite/multiscale dictionary inequality quantifies that obstruction without paying output dimension `n`: if the KKT-relevant local zonotopes can be dominated by `M` fixed models of radius `R` and local mean width `L`, then

```text
E ||sum_i g_i T_i||_(I_p)
 <= L + R sqrt(2 log M)
```

(up to the displayed constants below). Since the canonical local models have `R = O_r(S)` and `L = O_r(d^(1/2-1/p)S)`, the conjectured polynomial exponent survives even for

```text
log M <= d^(1-2/p) * polylog(d,n)^2.
```

This is substantially more permissive than a single global zonotope or common-frame condition.

A sharp countertest is also proved. The matrix hypercube example has **zero local transverse area at every selected model** (each selected local zonotope is just a segment), yet the union over `d` selected segments has Gaussian width `Theta(sqrt(log d))`. Thus any lemma asserting that pointwise local transverse area alone controls the full process is false. The dictionary selection term is necessary.

Finally, the same matrix hypercube lower bound is homogenized to **every fixed order `r >= 2` at `p=2`**. For every order there are symmetric order-`r` tensor families with source normalization `S=1` and

```text
E ||sum_i g_i T_i||_(I_2) >= c_r sqrt(log d).
```

Hence a dimension-free constant type-2 bound is impossible for every tensor order, not only for matrices. Any full proof of Conjecture 16 at `p=2` must allow at least a logarithmic loss.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Registered role: `chaining / geometric-probabilistic proof`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Pre-write master observed: `c9c7614e34022dd38c2e69c039abedb360e84d52`
- Immediate predecessor: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T135800Z__zonotopal-switching-curvature-and-transverse-area-factorization.md`.
- Historical C0035 material, prior P09 reports, and peer files are preserved. This report is additive and immutable.

---

## 1. Exact source normalization and bounded current-source check

Primary source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizić-Nikolac, A. Rödder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 16.

For symmetric deterministic order-`r` tensors `T_1,...,T_n` on `R^d`, iid standard Gaussian `g_i`, and

```text
||T||_(I_p) := sup_(||x||_p<=1) |T[x,...,x]|,
```

the source asks for

```text
E ||sum_i g_i T_i||_(I_p)
 <= C(r,p) polylog(d,n) d^(1/2-1/p)
    (sum_i ||T_i||_(I_p)^2)^(1/2).                       (1.1)
```

Set

```text
alpha := 1/2 - 1/p,
S^2   := sum_i ||T_i||_(I_p)^2.                           (1.2)
```

A bounded primary/current literature check on 20 September 2026 again recovers:

1. `arXiv:2603.29571`, still recording Conjecture 16;
2. Bandeira--Gopi--Jiang--Lucca--Rothvoss, `arXiv:2411.10633`, as the general correlated-tensor geometric/covering baseline;
3. Ishaq Aden-Ali, `arXiv:2503.10580`, especially Theorem 1.2 / Corollary 1.4, as the PAC-Bayesian variance-parameter improvement which removes a logarithm from the first term but still retains higher-order variance/Frobenius terms and explicitly describes the remaining mechanism as volumetric in the problematic regimes;
4. Dartois--McKenna, `arXiv:2603.01342`, as a 2026 moment-method advance for specific random-tensor ensembles (including independent-up-to-symmetry and bounded-rank models), not a resolution of the arbitrary deterministic correlated Gaussian-sum type-2 statement (1.1).

No full resolution of the exact arbitrary deterministic `2 <= p < 2r` statement was found in that bounded check. This is not a claim about unpublished or unindexed work.

The inherited general polynomial exponent in the low-`p` regime therefore remains

```text
gamma = 1/2 - 1/(2r),                                    (1.3)
```

rather than `alpha`.

---

## 2. Polarization convention and the tangent map

Let `\widetilde T_i` denote the symmetric `r`-linear form associated with the diagonal polynomial `x -> T_i[x^r]`. Fix a real polarization constant `kappa_r < infinity`, depending only on `r`, such that

```text
|\widetilde T_i(x_1,...,x_r)|
 <= kappa_r ||T_i||_(I_p) prod_(a=1)^r ||x_a||_p.         (2.1)
```

For example one may take a standard real polarization constant bounded in terms of `r` only. Nothing below depends on optimizing `kappa_r`.

Define the output map

```text
F(x) := ( T_i[x^r] )_(i=1)^n in R^n                     (2.2)
```

and the one-free-slot tangent contraction

```text
A_x v := ( \widetilde T_i(x,...,x,v) )_(i=1)^n.          (2.3)
```

Then homogeneity gives

```text
F(x) = A_x x,                                            (2.4)
DF(x)[v] = r A_x v.                                      (2.5)
```

For every `x,v in B_p^d`, (2.1) and Cauchy across the output index imply

```text
||A_x v||_2 <= kappa_r S.                                (2.6)
```

The same polarization estimate gives a dimension-free Hilbert--Schmidt bound for `A_x`.

### Lemma 2.1 — tangent Hilbert--Schmidt bound

For every `x in B_p^d`,

```text
boxed:
||A_x||_(HS) <= kappa_r S.                               (2.7)
```

#### Proof

For each `i`, write the row vector

```text
a_i(x)_j := \widetilde T_i(x,...,x,e_j).                 (2.8)
```

Let `q=p/(p-1) <= 2`. Then

```text
||a_i(x)||_q
 = sup_(||v||_p<=1) |\widetilde T_i(x^(r-1),v)|
 <= kappa_r ||T_i||_(I_p).                               (2.9)
```

Since `q<=2`, `||z||_2 <= ||z||_q`. Therefore

```text
||A_x||_(HS)^2
 = sum_i ||a_i(x)||_2^2
 <= sum_i ||a_i(x)||_q^2
 <= kappa_r^2 S^2.                                       (2.10)
```

QED.

This apparently small observation is what makes the local zonotope below have the correct mean-width scale.

---

## 3. Canonical coordinate-tangent zonotope

For `x in B_p^d`, define the diagonal multiplier

```text
D_x t := t odot x,                                       (3.1)
```

and the linear map

```text
B_x := A_x D_x : l_infinity^d -> l_2^n.                 (3.2)
```

The associated centrally symmetric zonotope is

```text
Z_x
 := B_x(B_infinity^d)
  = { A_x(t odot x) : ||t||_infinity<=1 }
  = sum_(j=1)^d [-v_j(x),v_j(x)],                        (3.3)
```

where

```text
v_j(x) := x_j A_x e_j.                                   (3.4)
```

Because `F(x)=A_xx`, taking `t=(1,...,1)` shows

```text
F(x) in Z_x.                                             (3.5)
```

Thus the original output body

```text
K := conv( F(B_p^d) union -F(B_p^d) )                   (3.6)
```

is contained in

```text
K subset conv( union_(x in B_p^d) Z_x ).                (3.7)
```

The key point is that every individual `Z_x` is much cheaper than a generic global zonotopal envelope.

---

## 4. Universal local radius bound: no d^alpha loss

Define the Euclidean radius

```text
R_x := sup_(z in Z_x) ||z||_2
     = ||B_x||_(infinity -> 2).                          (4.1)
```

### Theorem 4.1 — canonical local zonotopes have source-scale radius

For every `x in B_p^d`,

```text
boxed:
R_x <= kappa_r S.                                        (4.2)
```

#### Proof

Every point of `Z_x` has the form

```text
z=A_x(t odot x),  ||t||_infinity<=1.                    (4.3)
```

But coordinatewise domination gives

```text
||t odot x||_p <= ||x||_p <=1.                          (4.4)
```

Therefore (2.6) yields

```text
||z||_2 <= kappa_r S.                                    (4.5)
```

Taking the supremum proves (4.2). QED.

This is stronger than the `d^alpha S` scale: the entire sign cube generated by the coordinate tangent vectors fits in an `O_r(S)` Euclidean ball.

---

## 5. Universal local mean width and transverse-area energy

Let

```text
L_x := sum_(j=1)^d ||v_j(x)||_2
     = sum_j |x_j| ||A_xe_j||_2.                         (5.1)
```

### Theorem 5.1 — generator-length bound at the conjectured scale

For every `x in B_p^d`,

```text
boxed:
L_x <= kappa_r d^alpha S.                                (5.2)
```

#### Proof

By Cauchy--Schwarz,

```text
L_x
 <= (sum_j |x_j|^2)^(1/2)
    (sum_j ||A_xe_j||_2^2)^(1/2)
 = ||x||_2 ||A_x||_(HS).                                 (5.3)
```

Since `p>=2`,

```text
||x||_2 <= d^(1/2-1/p)||x||_p <= d^alpha.                (5.4)
```

Apply Lemma 2.1. QED.

For standard Gaussian `g in R^n`, the zonotope support function is

```text
h_(Z_x)(g)
 = sum_j |<g,v_j(x)>|.                                   (5.5)
```

Consequently

```text
E h_(Z_x)(g)
 = sqrt(2/pi) L_x
 <= sqrt(2/pi) kappa_r d^alpha S.                        (5.6)
```

So **each local tangent zonotope already has the conjectured polynomial scale in Gaussian mean width**.

Now define its transverse-area complexity

```text
A_x^(wedge)
 := sum_(j<l) ||v_j(x) wedge v_l(x)||_2.                 (5.7)
```

Since `||u wedge v|| <= ||u|| ||v||`,

```text
A_x^(wedge)
 <= sum_(j<l)||v_j||||v_l||
 <= 1/2 (sum_j ||v_j||)^2.                               (5.8)
```

Hence

```text
boxed:
A_x^(wedge)
 <= (kappa_r^2/2) d^(2alpha) S^2.                        (5.9)
```

Combining (4.2), (5.9), and the predecessor's exact zonotopal curvature formula gives, for every single local model,

```text
R_x^2 + (4/pi)A_x^(wedge)
 <= C_r [ S^2 + d^(2alpha)S^2 ]
 <= C_r d^(2alpha)S^2                                   (5.10)
```

(with the obvious interpretation `d^(2alpha)=1` at `p=2`).

**Conclusion.** The predecessor's proposed local transverse-area sparsification problem is already solved for the canonical tensor-adapted zonotope. The difficult part is not the geometry *inside one local model*.

---

## 6. Exact KKT exposure: a maximizer selects a locally cheap zonotope with no loss

The previous section only used containment `F(x) in Z_x`. At an actual optimizer there is a much stronger identity.

Let

```text
P_g(x) := <g,F(x)> = sum_i g_i T_i[x^r],                 (6.1)

h(g) := ||sum_i g_i T_i||_(I_p)
      = sup_(||x||_p<=1) |P_g(x)|.                       (6.2)
```

Assume `h(g)>0`, choose `sigma in {+1,-1}` and `x=x(g)` with `||x||_p=1` such that

```text
sigma P_g(x)=h(g).                                       (6.3)
```

For `p>1`, the boundary of the `l_p` ball is differentiable. The KKT equation is

```text
r sigma A_x^* g
 = lambda p ( |x_j|^(p-2)x_j )_(j=1)^d.                 (6.4)
```

Pairing with `x` and using Euler homogeneity gives

```text
r h(g)=lambda p,                                         (6.5)
```

so coordinatewise

```text
boxed:
sigma <g,A_xe_j>
 = h(g)|x_j|^(p-2)x_j.                                   (6.6)
```

Multiplying by `x_j` yields the more geometric identity

```text
boxed:
sigma <g,v_j(x)>
 = h(g)|x_j|^p >=0.                                      (6.7)
```

Summing and using `sum_j|x_j|^p=1`,

```text
sum_j |<g,v_j(x)>|
 = h(g).                                                  (6.8)
```

But the left side is exactly `h_(Z_x)(g)`. Therefore:

### Theorem 6.1 — KKT-selected local-zonotope identity

For every `g` with `h(g)>0`, there exists a maximizing `x(g)` such that

```text
boxed:
h(g)=h_(Z_(x(g)))(g).                                    (6.9)
```

Moreover the exposure mass of the `j`th generator is exactly

```text
boxed:
|<g,v_j(x(g))>|
 = h(g)|x_j(g)|^p.                                       (6.10)
```

Thus the probability vector `(|x_j|^p)_j` is literally the normalized support contribution of the local tangent generators at the selected optimizer.

This is a stronger structural statement than the earlier balanced-column decomposition: it is not an approximation and it applies to the actual selected Gaussian maximizer.

---

## 7. What the KKT identity rules out

It is tempting to combine the pointwise estimates

```text
R_x       <= C_r S,
E h_(Z_x) <= C_r d^alpha S,
A_x^(wedge) <= C_r d^(2alpha)S^2                        (7.1)
```

and conclude the full conjecture. That is false because `x=x(g)` is selected from the Gaussian realization. A large family of individually cheap local models can still have a much larger maximum.

The remaining problem is therefore a **model-selection entropy** problem:

```text
How many genuinely different locally cheap zonotopes can be selected,
at each Gaussian resolution scale?                       (7.2)
```

The next theorem quantifies exactly how much selection can be tolerated.

---

## 8. A finite local-zonotope dictionary inequality

Let `W_1,...,W_M` be fixed centrally symmetric convex bodies in `R^n`. Assume that every canonical local zonotope is dominated by one dictionary element:

```text
for every x in B_p^d there exists a(x) in [M] such that
Z_x subset W_(a(x)).                                     (8.1)
```

Set

```text
mu := max_a E h_(W_a)(g),                                (8.2)
R  := max_a sup_(w in W_a)||w||_2.                       (8.3)
```

### Theorem 8.1 — finite dictionary bound

Under (8.1),

```text
boxed:
E ||sum_i g_iT_i||_(I_p)
 <= mu + R sqrt(2 log M).                                (8.4)
```

For `M=1`, interpret the second term as zero.

#### Proof

By (3.5) and (8.1),

```text
h(g)
 = sup_x |<g,F(x)>|
 <= max_(a<=M) h_(W_a)(g).                               (8.5)
```

For each fixed `a`, the support function `g -> h_(W_a)(g)` is `R`-Lipschitz, because

```text
|h_(W_a)(g)-h_(W_a)(g')|
 <= h_(W_a)(g-g')
 <= R ||g-g'||_2.                                       (8.6)
```

Gaussian concentration in moment-generating-function form gives

```text
E exp( lambda (h_(W_a)-E h_(W_a)) )
 <= exp(lambda^2 R^2/2).                                 (8.7)
```

Therefore

```text
E max_a h_(W_a)
 <= mu + inf_(lambda>0)
    [ log M/lambda + lambda R^2/2 ]
 = mu + R sqrt(2 log M).                                 (8.8)
```

Combine with (8.5). QED.

### Zonotopal specialization

If

```text
W_a = sum_l [-w_(a,l),w_(a,l)]                          (8.9)
```

and

```text
L := max_a sum_l ||w_(a,l)||_2,                         (8.10)
```

then

```text
E h_(W_a)(g)
 = sqrt(2/pi) sum_l||w_(a,l)||_2
 <= sqrt(2/pi)L.                                         (8.11)
```

Hence

```text
boxed:
E ||sum_i g_iT_i||_(I_p)
 <= sqrt(2/pi)L + R sqrt(2 log M).                       (8.12)
```

This is the first new covering inequality of the run.

---

## 9. The exact entropy budget compatible with Conjecture 16

The canonical local models themselves satisfy

```text
local mean-width scale L_local = O_r(d^alpha S),
local radius scale     R_local = O_r(S).                 (9.1)
```

Suppose a dictionary can dominate them with only polylogarithmic inflation:

```text
L <= C_r d^alpha S * P(d,n),
R <= C_r S * P(d,n),                                    (9.2)
```

where `P` is polylogarithmic. Then (8.12) remains at the conjectured polynomial exponent as long as

```text
sqrt(log M) <= d^alpha * P(d,n),                         (9.3)
```

i.e.

```text
boxed:
log M <= d^(2alpha) * P(d,n)^2
      = d^(1-2/p) * P(d,n)^2.                            (9.4)
```

So a one-scale proof does **not** need a polynomial-size dictionary when `p>2`. It may use as many as

```text
M = exp( d^(1-2/p) polylog(d,n)^2 )                      (9.5)
```

local geometric models and still preserve the conjectured power of `d`.

At `p=2`, `alpha=0`, this reduces to a polylogarithmic entropy allowance, consistent with the unavoidable matrix `sqrt(log d)` behavior discussed below.

This is a more precise replacement for the predecessor's transverse-area target.

---

## 10. Multiscale dictionary / chaining version

The finite dictionary theorem extends immediately to a scale decomposition and is the form that appears usable for the arbitrary problem.

Let `E` be a fixed centrally symmetric residual body. For levels `q=0,...,Q`, let

```text
{W_(q,a) : a=1,...,M_q}                                  (10.1)
```

be fixed centrally symmetric convex bodies. Assume that for every `x in B_p^d` one can choose indices `a_q(x)` such that

```text
Z_x
 subset E + W_(0,a_0(x)) + ... + W_(Q,a_Q(x)).           (10.2)
```

Define

```text
mu_q := max_a E h_(W_(q,a))(g),
R_q  := max_a sup_(w in W_(q,a))||w||_2.                 (10.3)
```

### Theorem 10.1 — multiscale local-zonotope dictionary inequality

Under (10.2),

```text
boxed:
E ||sum_i g_iT_i||_(I_p)
 <= E h_E(g)
    + sum_(q=0)^Q [ mu_q + R_q sqrt(2 log M_q) ].         (10.4)
```

#### Proof

Support functions turn Minkowski sums into sums. Thus

```text
h_(Z_x)(g)
 <= h_E(g)+sum_q h_(W_(q,a_q(x)))(g).                    (10.5)
```

Taking the supremum over `x` gives

```text
h(g)
 <= h_E(g)+sum_q max_(a<=M_q)h_(W_(q,a))(g),             (10.6)
```

where we used `F(x) in Z_x`. Apply the same Gaussian maximum argument as in Theorem 8.1 at each level and take expectations. QED.

If each `W_(q,a)` is a zonotope with total generator length at most `L_q`, then `mu_q <= sqrt(2/pi)L_q`, yielding

```text
E h(g)
 <= E h_E(g)
    + sum_q [ sqrt(2/pi)L_q + R_q sqrt(2 log M_q) ].      (10.7)
```

This is a genuine chaining-style sufficient condition. It permits very large fine-scale dictionaries as long as their Euclidean radii `R_q` decay fast enough.

---

## 11. Lipschitz geometry of the local-zonotope map

The canonical map `x -> Z_x` has two simultaneous Lipschitz controls with exactly the two scales appearing in Theorem 10.1.

### Lemma 11.1 — radius/Hausdorff Lipschitz control

For all `x,y in B_p^d`,

```text
boxed:
||B_x-B_y||_(infinity -> 2)
 <= r kappa_r S ||x-y||_p.                               (11.1)
```

#### Proof

Fix `t` with `||t||_infinity<=1`. The `i`th coordinate of `(B_x-B_y)t` is

```text
\widetilde T_i(x^(r-1),t odot x)
 - \widetilde T_i(y^(r-1),t odot y).                    (11.2)
```

Telescope the `r` arguments one at a time. Each term contains exactly one factor equal to either `x-y` or `t odot(x-y)`, whose `p`-norm is at most `||x-y||_p`; all remaining factors have `p`-norm at most one. Hence by (2.1), for every `i`, the absolute value is at most

```text
r kappa_r ||T_i||_(I_p) ||x-y||_p.                       (11.3)
```

Square and sum in `i`, then take the supremum over `t`. QED.

Since `Z_x=B_xB_infinity`, (11.1) also bounds the Euclidean Hausdorff distance between `Z_x` and `Z_y`.

### Lemma 11.2 — generator-length Lipschitz control

For all `x,y in B_p^d`,

```text
boxed:
sum_j ||B_xe_j-B_ye_j||_2
 <= C_r d^alpha S ||x-y||_p.                             (11.4)
```

#### Proof

Write

```text
B_xe_j-B_ye_j
 = (x_j-y_j)A_xe_j
   + y_j(A_x-A_y)e_j.                                    (11.5)
```

For the first sum, Cauchy--Schwarz and Lemma 2.1 give

```text
sum_j |x_j-y_j| ||A_xe_j||
 <= ||x-y||_2 ||A_x||_(HS)
 <= kappa_r d^alpha S ||x-y||_p.                         (11.6)
```

For the second sum,

```text
sum_j |y_j| ||(A_x-A_y)e_j||
 <= ||y||_2 ||A_x-A_y||_(HS).                            (11.7)
```

The same row-`l_q` argument as Lemma 2.1, after telescoping the `r-1` repeated `x` slots, gives

```text
||A_x-A_y||_(HS)
 <= (r-1)kappa_r S ||x-y||_p.                            (11.8)
```

Since `||y||_2<=d^alpha`, combine (11.6)--(11.8). QED.

The paired scales are therefore

```text
radius variation       ~ S ||x-y||_p,
mean-width variation   ~ d^alpha S ||x-y||_p.            (11.9)
```

This is exactly the asymmetry needed by the dictionary theorem.

---

## 12. The volumetric obstruction in the new coordinates

Lemma 11.1 by itself still does not solve the problem. A naive `l_p`-net of `B_p^d` at fixed relative mesh has

```text
log M = Theta(d).                                        (12.1)
```

The selection term in Theorem 8.1 would then be

```text
S sqrt(log M) = Theta(S sqrt(d)).                        (12.2)
```

The target is

```text
d^alpha S = d^(1/2-1/p)S.                               (12.3)
```

Thus naive volumetric discretization loses exactly

```text
sqrt(d)/d^alpha = d^(1/p).                               (12.4)
```

This gives a clean restatement of the low-`p` barrier:

> The local tensor geometry already has the correct radius and mean width. The missing gain is a factor `d^(1/p)` in the number of **selectable local models** relative to a full-dimensional volumetric net.

Equivalently, at a coarse one-scale level we need effective logarithmic dictionary size around

```text
log M_eff ~ d^(1-2/p) polylog                           (12.5)
```

rather than `d`.

The next proof attempt should attack this selected-model entropy, not re-sparsify generators inside each `Z_x`.

---

## 13. Counterexample: local transverse area can be zero while the global width is sqrt(log d)

The predecessor's matrix hypercube example now becomes a decisive falsification test for the wrong intermediate lemma.

Let `m>=1`, `D=2^m`, and index the standard basis of `R^D` by sign vectors

```text
s in {+1,-1}^m.                                         (13.1)
```

For `i=1,...,m`, define the symmetric matrices

```text
T_i
 := (1/sqrt(m)) diag( s_i )_(s in {+1,-1}^m).           (13.2)
```

At `p=2`,

```text
||T_i||_(I_2)=||T_i||_(op)=1/sqrt(m),
S^2=sum_i 1/m =1.                                        (13.3)
```

For Gaussian `g=(g_1,...,g_m)`,

```text
||sum_i g_iT_i||_(I_2)
 = (1/sqrt(m)) max_(s in {+-1}^m)|sum_i g_i s_i|
 = (1/sqrt(m)) sum_i |g_i|.                              (13.4)
```

Therefore

```text
boxed:
E ||sum_i g_iT_i||_(I_2)
 = sqrt(2/pi) sqrt(m)
 = sqrt(2/(pi log 2)) sqrt(log D).                       (13.5)
```

Now examine the canonical local zonotope at a coordinate optimizer `x=e_s`. Because the matrices are diagonal, all tangent generators vanish except the `s`th one, and

```text
Z_(e_s)
 = [-v_s,v_s],

v_s=(s_1,...,s_m)/sqrt(m),
||v_s||_2=1.                                             (13.6)
```

Hence each selected local model satisfies

```text
R_(e_s)=1,
E h_(Z_(e_s))=sqrt(2/pi),
A_(e_s)^(wedge)=0.                                       (13.7)
```

There is literally **no internal transverse area** to sparsify. Nevertheless there are `D=2^m` possible selected segments and

```text
E max_s h_([-v_s,v_s])(g)
 = Theta(sqrt(log D)).                                   (13.8)
```

Theorem 8.1 predicts the correct order:

```text
local mean O(1)
+ radius 1 * sqrt(log M),  M=D.                          (13.9)
```

### Consequence

The following proposed intermediate statement is false:

```text
"If every KKT-selected local tangent zonotope has
 radius O(S) and transverse area O(d^(2alpha)S^2),
 then the full Gaussian tensor width is O(d^alpha S polylog)."
```

At `p=2`, the matrix cube satisfies the pointwise hypotheses with *zero* area and still incurs `sqrt(log d)` through selection among local models.

This does not refute Conjecture 16 because the conjecture explicitly permits polylogarithmic factors. It identifies the missing term correctly.

---

## 14. New lower bound: sqrt(log d) is unavoidable for every fixed order r at p=2

The previous example is a matrix (`r=2`) construction. A simple homogenization transports it to every tensor order without changing the Gaussian type-2 ratio up to an order-dependent constant; in fact the even-order construction is exact.

### Theorem 14.1 — all-order logarithmic lower bound

For every fixed integer `r>=2`, there exists `c_r>0` such that for infinitely many dimensions `d` there are symmetric order-`r` tensors `T_1,...,T_m` on `R^d` satisfying

```text
sum_i ||T_i||_(I_2)^2 =1                                (14.1)
```

and

```text
boxed:
E ||sum_i g_iT_i||_(I_2)
 >= c_r sqrt(log d).                                     (14.2)
```

In fact the ratio inherited from (13.5) is preserved exactly after the normalizations below.

#### Proof: even orders

Let

```text
r=2+2q,  q>=0.                                           (14.3)
```

Use the matrix family `A_i=T_i` from Section 13 in dimension `D=2^m`. Define the homogeneous order-`r` polynomial

```text
P_(i,r)(x)
 := (x^T A_i x) (x^T x)^q.                               (14.4)
```

This is represented by a symmetric order-`r` tensor, call it `\mathcal T_(i,r)`.

For `||x||_2=1`,

```text
P_(i,r)(x)=x^TA_i x.                                     (14.5)
```

Because `P_(i,r)` is homogeneous of degree `r`, its supremum on `B_2^D` is attained on the sphere unless it vanishes identically. Therefore

```text
||\mathcal T_(i,r)||_(I_2)
 = ||A_i||_(op).                                         (14.6)
```

For every coefficient vector `a=(a_i)`,

```text
||sum_i a_i \mathcal T_(i,r)||_(I_2)
 = ||sum_i a_i A_i||_(op),                               (14.7)
```

because on the unit sphere the common factor `(x^Tx)^q` equals one. Thus both the denominator `S` and the Gaussian numerator are exactly preserved. Applying (13.5) proves (14.2) for every even `r` with `d=D`.

#### Proof: odd orders

Let

```text
r=3+2q,  q>=0.                                           (14.8)
```

Work on `R^(D+1)` with coordinates `(t,y)`, `y in R^D`. For a symmetric matrix `A`, consider

```text
Q_A(t,y)
 := c_* t (y^T A y) (t^2+||y||_2^2)^q,                  (14.9)
```

where

```text
c_* := 3 sqrt(3)/2.                                      (14.10)
```

On the unit sphere `t^2+||y||_2^2=1`,

```text
|Q_A(t,y)|
 <= c_* |t| ||y||_2^2 ||A||_(op).                       (14.11)
```

Let `u=|t|`. Then `||y||_2^2=1-u^2`, so the scalar factor is

```text
u(1-u^2).                                                (14.12)
```

Its maximum on `[0,1]` occurs at `u=1/sqrt(3)` and equals

```text
2/(3sqrt(3)).                                            (14.13)
```

The choice (14.10) therefore gives

```text
||Q_A||_(I_2)=||A||_(op).                                (14.14)
```

Moreover (14.14) holds for every linear combination of the matrices. Define `\mathcal T_(i,r)` from `A_i` by (14.9). Then

```text
||sum_i a_i \mathcal T_(i,r)||_(I_2)
 = ||sum_i a_i A_i||_(op)                               (14.15)
```

for every coefficient vector `a`. Again both `S` and the Gaussian numerator are exactly preserved. Since the new dimension is `d=D+1`, we still have `m=Theta(log d)`. Apply (13.5). QED.

### Interpretation

For every `r>=2`, the order-`r` symmetric tensor normed space at `p=2` contains, up to the explicit homogenization above, the matrix operator-norm obstruction. Therefore no proof can establish

```text
E ||sum_i g_iT_i||_(I_2) <= C_r S                       (14.16)
```

uniformly in `d`. At least a `sqrt(log d)` loss is necessary.

This is consistent with Conjecture 16, which allows polylogarithmic factors. It is useful as a mandatory falsification test for any future candidate lemma claiming dimension-free type 2 at `p=2`.

---

## 15. Comparison with the predecessor and exact change in obligations

### Inherited theorem before this run

The predecessor proved exact switching curvature for a *fixed* zonotope:

```text
I_switch(Z)
 = (4/pi) sum_(j<l)||v_j wedge v_l||,                    (15.1)
```

and proposed transverse-area sparsification as the next local target.

### New theorem after this run

For the tensor's canonical local coordinate-tangent zonotope `Z_x`, uniformly in `x`, we now have

```text
radius:       R_x <= kappa_r S,
mean width:   E h_(Z_x) <= C_r d^alpha S,
area energy:  A_x^(wedge) <= C_r d^(2alpha)S^2,          (15.2)
```

and at a true maximizer

```text
h(g)=h_(Z_(x(g)))(g).                                    (15.3)
```

So the local area target is already met automatically.

The new global reduction is the dictionary inequality

```text
E h(g)
 <= local-mean budget
    + local-radius * sqrt(model entropy),                (15.4)
```

with the multiscale refinement (10.4).

### New obstruction

The matrix cube proves that model selection is a real phenomenon even when every local model is a segment with zero transverse area. The entropy term cannot simply be dropped.

### Fixed full-source metric

No arbitrary-tensor polynomial exponent changed:

```text
gamma_old = gamma_new = 1/2 - 1/(2r),
alpha_target           = 1/2 - 1/p.                     (15.5)
```

This report is therefore labeled **PROVED PARTIAL**, not a full solution.

---

## 16. A concrete new intermediate theorem target

The new one-scale target can be stated cleanly.

### Selected local-zonotope dictionary target

Construct fixed centrally symmetric bodies `W_1,...,W_M` such that

```text
Z_x subset W_(a(x))  for every KKT-relevant x,           (16.1)
```

with

```text
max_a E h_(W_a)(g)
 <= C_r d^alpha S polylog(d,n),                          (16.2)

max_a radius(W_a)
 <= C_r S polylog(d,n),                                  (16.3)

log M
 <= C_r d^(2alpha) polylog(d,n)^2.                       (16.4)
```

Then Theorem 8.1 proves Conjecture 16's desired polynomial exponent.

The multiscale version is weaker and more plausible: find level dictionaries satisfying

```text
sum_q mu_q
 <= C_r d^alpha S polylog,                               (16.5)

sum_q R_q sqrt(log M_q)
 <= C_r d^alpha S polylog.                               (16.6)
```

The main geometric question is therefore no longer whether every local tangent configuration can be sparsified. It is whether **the local configurations that can actually be selected by a degree-`r` tensor process have effective entropy `d^(1-2/p)` rather than `d` once weighted by their Euclidean radii**.

---

## 17. Mandatory countertests for the next lemma

Any proposed selected-model entropy theorem must pass all of the following.

### Test A — matrix hypercube

At `p=2`, there are `d` selected segment models and the process genuinely costs `sqrt(log d)`. A theorem demanding `O(1)` exact models is false; a theorem allowing polylog entropy is consistent.

### Test B — decaying weighted cube

The predecessor showed that exponentially many formal branches can have `O(1)` effective width when amplitudes decay. Raw model count is therefore too pessimistic unless models are grouped by radius/amplitude.

### Test C — constant-level-set tangent rotation

Earlier P09 reports constructed processes where the full tangent field rotates through exponentially many directions while the actual output process is constant or zero on the relevant orbit. The dictionary must be built from `Z_x=B_xB_infinity`, or another process-visible object, not from unweighted tangent directions.

### Test D — global Haar sketch counterexample

A shared low-rank random sketch can create exponentially more complexity than the original process. The selected-model dictionary should be deterministic/process-adaptive, not a single global sketch.

### Test E — all-order logarithmic embedding

The homogenized matrix cube from Theorem 14.1 shows that a candidate `p=2` proof with no logarithmic loss is impossible for every order `r`.

---

## 18. Next mathematical attack

The next run should attack the **selected local-zonotope entropy** directly, using the structure

```text
B_x t
 = ( \widetilde T_i(x^(r-1),t odot x) )_i               (18.1)
```

rather than the whole tangent operator `A_x`.

There are three concrete sub-attacks.

### 18.1 Radius-weighted chaining of local models

Use Lemmas 11.1--11.2 to construct a tree of local models where each increment is controlled simultaneously by

```text
radius increment      <= C_r S delta_q,
mean-width increment  <= C_r d^alpha S delta_q.          (18.2)
```

A naive volumetric tree has `log M_q ~ d log(1/delta_q)` and loses `d^(1/p)`. The target is to use KKT exposure (6.7) to prune cells that cannot be selected at scale `q`.

### 18.2 KKT mass pruning

At a selected maximizer,

```text
|<g,v_j(x)>|/h(g)=|x_j|^p.                               (18.3)
```

Thus the coordinate `p`-mass is exactly the exposure-mass distribution. Use this to group coordinates by dyadic masses and show that fine geometric distinctions in a cell carrying tiny total exposure mass can be deferred to a finer radius level, where Theorem 10.1 charges them by the smaller `R_q`.

The matrix cube is a useful calibration: its selected optimizer has one coordinate of mass one, and the remaining complexity is the `d`-way choice of that coordinate, producing precisely `sqrt(log d)`.

### 18.3 Search for a counterexample to the entropy target before proving it

Try to construct, for fixed `r`, a family with source normalization `S=1` and at least

```text
exp(c d)                                                   (18.4)
```

KKT-selectable local zonotopes that are pairwise separated at `O(1)` Euclidean radius and each have mean width `O(d^alpha)`. If such a construction exists at `p=2`, it would contradict Conjecture 16 by the finite-family Sudakov heuristic only if the selected support values also form a genuine constant-separated output code; previous tangent-rotation examples fail precisely because they are process-invisible. Therefore the counterexample search must test actual selected `Z_x`, not formal tangent planes.

If the search fails for structural reasons, turn that obstruction into the desired entropy lemma.

---

## 19. Obligation ledger

| Item | Status after this run |
|---|---|
| Exact outside source and normalization | recovered |
| Full arbitrary `2<=p<2r` conjecture | OPEN |
| Arbitrary polynomial exponent | unchanged: `1/2-1/(2r)` |
| Target exponent | `alpha=1/2-1/p` |
| Fixed-zonotope switching formula | inherited PROVED PARTIAL |
| Canonical local tangent-zonotope radius `O_r(S)` | **PROVED** |
| Canonical local tangent-zonotope mean width `O_r(d^alpha S)` | **PROVED** |
| Canonical local transverse area `O_r(d^(2alpha)S^2)` | **PROVED** |
| Exact KKT local exposure identity | **PROVED** |
| Finite local-zonotope dictionary inequality | **PROVED** |
| Multiscale dictionary/chaining inequality | **PROVED** |
| Pointwise local-area sufficiency | **REFUTED** by matrix cube |
| `sqrt(log d)` lower bound for all fixed `r>=2` at `p=2` | **PROVED** |
| Effective selected-model entropy `d^(1-2/p) polylog` | OPEN; next target |

---

## 20. Bottom line

The predecessor localized switching curvature inside fixed zonotopes. This run shows that the tensor process itself supplies, at every parameter point, a canonical local zonotope that is already as cheap as Conjecture 16 could reasonably require:

```text
radius       = O_r(S),
mean width   = O_r(d^(1/2-1/p)S),
area energy  = O_r(d^(1-2/p)S^2).                        (20.1)
```

KKT then says that the actual Gaussian maximizer is exposed by exactly one of these locally cheap models with no value loss.

The remaining low-`p` problem has therefore been sharpened to a **selection/chaining problem among locally cheap models**. The finite and multiscale dictionary inequalities quantify the exact entropy budget: the selection term is paid at the small radius `S`, not at the larger local mean-width scale `d^alpha S`. This allows `exp(d^(1-2/p) polylog^2)` local models at one scale without changing the conjectured power of `d`.

The matrix hypercube proves that this selection term is real even when every local model has zero transverse area, and the homogenization theorem transports its `sqrt(log d)` loss to every fixed tensor order at `p=2`. Thus the next proof must neither ignore selection entropy nor try to remove all logarithms.

The next concrete attack is to combine the exact KKT exposure masses `|x_j|^p` with the radius-weighted multiscale dictionary theorem to prune the naive `exp(Theta(d))` volumetric family down to effective entropy `d^(1-2/p) polylog`, or to extract a process-visible counterexample to that intermediate target.