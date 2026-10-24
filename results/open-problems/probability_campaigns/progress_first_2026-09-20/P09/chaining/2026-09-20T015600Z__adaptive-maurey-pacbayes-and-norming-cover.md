Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 progress-first run — adaptive Maurey/PAC-Bayes posterior, exact covariance localization, and overlapping norming covers

**Status: PROVED PARTIAL.** The full arbitrary-tensor exponent in Randomstrasse101 Conjecture 16 is not improved in this run. The substantive advance is a new one-shot PAC-Bayes inequality whose posterior is a coordinate-adaptive sparse empirical measure rather than a full-dimensional Gaussian. Its second-moment penalty is an exact `x`-dependent covariance tensor, not an ambient Frobenius contraction. This posterior escapes the polynomial `d^(1/(2r))` obstruction proved in the preceding P09 report on the diagonal witness. A second theorem gives the conjectured exponent for a substantially broader overlapping coordinate-norming class, with no disjoint-support or bounded interaction-degree requirement. A counter-calculation on the completely flat vector shows that a *single-scale* application of the new posterior still collapses to the same polynomial balance as Aden-Ali's isotropic PAC-Bayes inequality; therefore the next step must be genuinely multiscale/incremental rather than another one-shot covariance optimization.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Installed title: `Gaussian Tensor Bounds`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac, A. Rodder, *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.
- Exact source norm used here:

```text
||T||_sym(I_p) := sup_{||x||_p<=1} |T[x,...,x]|.
```

- Source target for symmetric deterministic order-`r` tensors `T_i` and iid standard Gaussian `g_i`:

```text
E ||sum_i g_i T_i||_sym(I_p)
 <= polylog(d,n) C(r,p) d^(1/2-1/p)
    (sum_i ||T_i||_sym(I_p)^2)^(1/2).
```

- Regime attacked: `2 <= p < 2r`.
- Historical continuity: old C0035 and successor-gate history is preserved. The immediately preceding P09 report is `2026-09-20T005500Z__sparse-interaction-and-anisotropic-pacbayes.md`, creation commit `9647760b7abed919bfab85ff6bcb0363d0973b58`. No historical or peer file is modified here.

## 1. Primary baseline and fixed full-source metric

Put

```text
alpha := 1/2 - 1/p,
gamma := 1/2 - 1/(2r),
S := (sum_i ||T_i||_sym(I_p)^2)^(1/2).
```

The current primary baseline remains:

1. Bandeira--Gopi--Jiang--Lucca--Rothvoss, arXiv:2411.10633, give the general type-2 polynomial exponent `gamma` for `p<2r` (their headline statement has a logarithm), and prove the contraction/Frobenius comparison

```text
sigma_q <= C_r d^max(q/p-1/2,0) S.
```

2. Aden-Ali, arXiv:2503.10580, Theorem 1.2 / Corollaries 1.3--1.4, gives the sharper PAC-Bayes contraction inequality. Combining his Corollary 1.4 with the preceding contraction comparison removes the unnecessary headline `log d` from the *worst-case polynomial* `d^gamma` local bound, but does not change `gamma` to `alpha`.

3. Randomstrasse101 Conjecture 16 records the desired exponent `alpha`, says `p>=2r` is already settled up to polylogarithms by the current geometry, and identifies the low-`p` volumetric obstruction. Matrix, rank-one, independent-entry and other special structures are not being relabeled as new here.

Thus the fixed full-source metric remains

```text
old arbitrary-tensor exponent: gamma,
new arbitrary-tensor exponent: gamma,
target exponent:               alpha.
```

There is no full-source closure claim in this report.

## 2. Inherited P09 theorem and the obstruction left by the previous run

The preceding P09 report proved two things relevant here.

First, if the coordinate blocks have size at most `b` and their family-level interaction hypergraphs have bounded maximum degree `Delta_*`, then a matching-layer projection lemma plus edge coloring gives

```text
E ||sum_i g_i T_i||
 <= C(r,p) (1+Delta_*) [local_dimension_term] S.
```

This genuinely permits cross-block interactions, but a dense interaction hypergraph still costs too many matching layers.

Second, it proved an anisotropic product-Gaussian PAC-Bayes inequality with arbitrary positive-definite slot covariances `D_t`, and then proved a no-go statement for that entire ellipsoidal template: for

```text
A_diag = sum_{j=1}^d e_j^(tensor r),   p=2,
```

the true Gaussian-series norm for one scalar Gaussian is dimension-free, while every product-Gaussian covariance choice in that template pays at least `c_r d^(1/(2r))`.

Therefore the promised next attack was a sparse/mixture posterior that randomizes the test vector before an ambient Frobenius aggregation. That is the main calculation below.

## 3. A self-normalized barycentric PAC-Bayes lemma

The useful form is slightly more general than the standard shifted-Gaussian calculation because the variance term is allowed to be evaluated under the posterior itself.

### Lemma 3.1 (self-normalized barycentric PAC-Bayes)

Let

```text
X_u(g) = sum_{i=1}^n g_i a_i(u),    u in U,
```

where `g_i` are iid standard Gaussians. Let `(Theta,pi)` be an arbitrary measurable parameter space with a fixed prior probability `pi`. For each `u in U`, suppose there is a posterior `rho_u << pi` such that

```text
E_{theta~rho_u} a_i(theta) = a_i(u)    for every i.
```

Define

```text
V(theta) := sum_i a_i(theta)^2,
K(u) := KL(rho_u || pi),
W(u)^2 := E_{rho_u} V(theta).
```

Then for every `lambda>0`,

```text
E_g sup_{u in U} X_u(g)
 <= sup_u { K(u)/lambda + (lambda/2) W(u)^2 }.             (3.1)
```

Consequently

```text
E_g sup_u |X_u(g)|
 <= 2 inf_{lambda>0}
       sup_u { K(u)/lambda + (lambda/2) W(u)^2 }.          (3.2)
```

In particular, if `K(u)<=K` and `W(u)<=W` uniformly, then

```text
E sup_u |X_u| <= 2 sqrt(2 K) W.                            (3.3)
```

### Proof

For fixed `g`, apply the Donsker--Varadhan entropy inequality to

```text
F_g(theta)
 := lambda sum_i g_i a_i(theta)
    - (lambda^2/2) V(theta).
```

For every `u`,

```text
E_{rho_u} F_g
 <= K(u) + log E_{pi} exp(F_g).
```

By the barycentric identity,

```text
E_{rho_u} sum_i g_i a_i(theta) = X_u(g).
```

Hence

```text
X_u(g)
 <= K(u)/lambda
    + (lambda/2) W(u)^2
    + (1/lambda) log Z_g,

Z_g := E_pi exp(F_g).
```

Take the supremum over `u` and then expectation in `g`. For each fixed `theta`, the Gaussian MGF identity gives

```text
E_g exp(lambda sum_i g_i a_i(theta)
        -lambda^2 V(theta)/2) = 1.
```

Therefore, by Jensen and Tonelli,

```text
E_g log Z_g <= log E_g Z_g = 0.
```

This proves (3.1). Applying the same inequality to `-X_u` and adding proves (3.2). Optimizing `K/lambda + lambda W^2/2` gives (3.3). QED.

### Why this differs from the previous Gaussian posterior

The prior can now be heavy-tailed and combinatorial. The only quantity that enters the quadratic penalty is the **posterior** second moment `W(u)^2`. Thus a posterior may localize onto a small support without forcing every unused ambient direction into one Frobenius term.

## 4. Coordinate-adaptive empirical posterior

We now construct a universal prior and a family of posteriors with exact mean `x`.

### 4.1 One latent coordinate atom

Let the prior `mu` on pairs `(J,Z)` be

```text
J ~ Uniform({1,...,d}),
Z ~ standard Cauchy, density h(z)=1/[pi(1+z^2)],
```

independently. The evaluated vector is

```text
Y := Z e_J.
```

Fix `x in R^d`. Choose any probability vector `q=q(x)` satisfying

```text
q_j>0 whenever x_j != 0.
```

Define the posterior `nu_{x,q}` by

```text
J ~ q,
Z | (J=j) ~ N(m_j,1),
m_j := x_j/q_j.
```

Then

```text
E Y = sum_j q_j (x_j/q_j) e_j = x.                        (4.1)
```

Set

```text
D_{x,q}
 := diag(q_j + x_j^2/q_j)_{j=1}^d.                        (4.2)
```

Since `E[Z^2|J=j]=1+m_j^2`,

```text
E YY^T = D_{x,q}.                                          (4.3)
```

### 4.2 Exact KL cost

Let

```text
kappa(x,q) := KL(nu_{x,q} || mu).
```

It splits as

```text
kappa(x,q)
 = D(q || uniform_d)
   + sum_j q_j KL(N(x_j/q_j,1) || Cauchy).                 (4.4)
```

For `Z~N(m,1)`,

```text
KL(N(m,1) || Cauchy)
 = c_0 + E log(1+Z^2)
 <= c_0 + log(2+m^2),                                      (4.5)
```

where `c_0` is a universal constant; the inequality is Jensen and `E Z^2=1+m^2`.

Therefore

```text
kappa(x,q)
 <= log d - H(q)
    + c_0
    + sum_j q_j log(2+x_j^2/q_j^2)

 <= log d - H(q)
    + c_0
    + log(2 + sum_j x_j^2/q_j).                            (4.6)
```

The last step is Jensen for the concave logarithm.

A canonical choice which never has a tiny-probability / huge-shift mismatch is

```text
q_j = |x_j| / ||x||_1       (x != 0).                      (4.7)
```

Then

```text
sum_j x_j^2/q_j = ||x||_1^2.                              (4.8)
```

For `||x||_p<=1`,

```text
||x||_1 <= d^(1-1/p),
```

so (4.6) gives the uniform logarithmic estimate

```text
kappa(x,q(x)) <= C + 3 log(2d).                            (4.9)
```

The exact entropy deficit `log d-H(q)` is retained in (4.6); (4.9) is only the coarse form.

### 4.3 Average `s` atoms: exact localized covariance

Take `s` iid posterior atoms `Y_1,...,Y_s` and set

```text
Theta := (Y_1+...+Y_s)/s.
```

Then `E Theta=x`. Independence gives the **exact** second moment matrix

```text
M_{s,x,q}
 := E Theta Theta^T
  = (1-1/s) x x^T + (1/s) D_{x,q}.                         (4.10)
```

The latent posterior KL is additive:

```text
KL(nu_{x,q}^{tensor s} || mu^{tensor s})
 = s kappa(x,q).                                           (4.11)
```

This is a Maurey-style empirical representation with a PAC-Bayes receipt: `s` controls the covariance noise, while the entropy cost is linear in `s` and only logarithmic in the ambient coordinate label/amplitude scale.

## 5. New tensor inequality: adaptive sparse-posterior PAC-Bayes

For a symmetric order-`r` tensor `T`, use its associated symmetric `r`-linear form when different slot vectors are supplied.

For `x in B_p^d`, choose a probability vector `q(x)` as above and an integer `s>=1`. Define

```text
M_x := M_{s,x,q(x)}.
```

Define the exact posterior variance functional

```text
V_{s,q}(x)
 := sum_i < T_i, M_x^(tensor r) T_i >_F.                   (5.1)
```

Equivalently, if `Theta_1,...,Theta_r` are independent copies of the `s`-atom empirical posterior with mean `x`, then

```text
V_{s,q}(x)
 = sum_i E [ T_i[Theta_1,...,Theta_r]^2 ].                 (5.2)
```

### Theorem 5.1 (adaptive coordinate posterior)

For every integer `s>=1`, every measurable choice `x -> q(x)`, and every `lambda>0`,

```text
E ||sum_i g_i T_i||_sym(I_p)
 <= 2 sup_{||x||_p<=1}
       { r s kappa(x,q(x))/lambda
         + (lambda/2) V_{s,q}(x) }.                        (5.3)
```

In the coarse uniform form, writing

```text
K_s := r s sup_x kappa(x,q(x)),
V_s := sup_x V_{s,q}(x),
```

we get

```text
E ||sum_i g_i T_i||_sym(I_p)
 <= 2 sqrt(2 K_s V_s).                                     (5.4)
```

For the canonical choice (4.7),

```text
E ||sum_i g_i T_i||_sym(I_p)
 <= C_r sqrt(s log(2d))
      sup_{||x||_p<=1} V_{s,q}(x)^(1/2).                  (5.5)
```

### Proof

For each of the `r` tensor slots, take an independent `s`-atom latent posterior from Section 4. Let the parameter `theta` consist of all `rs` latent pairs. Let the evaluated slot vectors be `Theta_1,...,Theta_r`, and define

```text
a_i(theta) := T_i[Theta_1,...,Theta_r].
```

By independence across slots and multilinearity,

```text
E_{rho_x} a_i(theta)
 = T_i[E Theta_1,...,E Theta_r]
 = T_i[x,...,x].                                           (5.6)
```

The total KL is `r s kappa(x,q(x))` by (4.11), and the posterior quadratic variance is exactly (5.2). Apply Lemma 3.1 to the Gaussian process indexed by `x in B_p^d`. QED.

### 5.2 Exact weighted-contraction expansion

Because the tensors are symmetric, expanding (4.10) gives

```text
V_{s,q}(x)
 = sum_{ell=0}^r binom(r,ell)
   (1-1/s)^(r-ell) s^(-ell)
   W_ell(x;D_{x,q})^2,                                    (5.7)
```

where

```text
W_ell(x;D)^2
 := sum_i ||
       (D^(1/2))^(tensor ell)
       T_i[x,...,x, dot,...,dot]
    ||_F^2.                                                (5.8)
```

There are `r-ell` copies of `x` and `ell` free slots in (5.8).

The crucial difference from a fixed anisotropic Gaussian posterior is that `D_{x,q}` may depend on the actual test vector `x` at only a KL cost, and it may be rank-deficient on coordinates which the posterior never uses.

For the canonical `q_j=|x_j|/L`, `L=||x||_1`, on the `l_p` unit sphere we have `L>=1` and

```text
D_{x,q}
 = diag( |x_j|/L + L |x_j| )
 <= 2 L diag(|x|).                                        (5.9)
```

Thus (5.7) becomes an `x`-weighted contraction hierarchy rather than one ambient Frobenius hierarchy.

## 6. The new posterior passes the previous diagonal no-go witness

This is a method test, not a new claim about the already-easy diagonal class.

Take `p=2` and an arbitrary Gaussian series of diagonal symmetric tensors

```text
T_i = sum_j a_{ij} e_j^(tensor r).
```

Since `p=2<=r`, every diagonal tensor is normed by a coordinate axis:

```text
||sum_i g_i T_i||_sym(I_2)
 = max_j |sum_i g_i a_{ij}|.                               (6.1)
```

For the index `x=e_j`, choose `s=1` and `q=delta_j`. Then

```text
D_{x,q}=2 e_j e_j^T,
M_x=2 e_j e_j^T.                                           (6.2)
```

Therefore

```text
V_{1,q}(e_j)
 = 2^r sum_i a_{ij}^2
 <= 2^r S^2.                                               (6.3)
```

The support-selection KL pays only `log d+O_r(1)`. Theorem 5.1 therefore gives

```text
E ||sum_i g_i T_i||_sym(I_2)
 <= C_r sqrt(log(2d)) S.                                   (6.4)
```

The previous report proved that every product-Gaussian covariance posterior, even fully anisotropic, pays at least `c_r d^(1/(2r))` on the single tensor `sum_j e_j^(tensor r)`. Equation (6.4) shows that the new sparse posterior **does not inherit that polynomial obstruction**: its covariance is allowed to collapse onto the selected coordinate.

This does not make the diagonal estimate itself novel; it is a sanity check that the new mechanism fixes the exact proof-template failure identified last run.

## 7. Counter-test: a one-scale sparse posterior still hits the flat-vector volumetric barrier

The new posterior is not by itself a full proof. Before treating it as one, test the opposite extreme.

Take the flat point

```text
x_flat = d^(-1/p) (1,...,1),
||x_flat||_p=1.
```

For the canonical choice `q_j=1/d`,

```text
D_{x,q}
 = (1/d + d^(1-2/p)) I
 = (1/d + d^(2 alpha)) I.                                 (7.1)
```

The second term dominates for the unresolved regime except the trivial tiny-dimensional boundary. Hence

```text
M_x
 approximately x x^T + [d^(2 alpha)/s] I.                 (7.2)
```

Write

```text
beta := s / d^(2 alpha).
```

Then the polynomial part of (5.7) becomes the same contraction balance

```text
sum_{ell=0}^r beta^(-ell) sigma_ell(x)^2
```

that appears in shifted isotropic Gaussian smoothing. Since the KL is `O_r(s log d)`, the squared one-shot bound has the schematic form

```text
d^(2 alpha) log d
  * sum_{ell=0}^r beta^(1-ell) sigma_ell^2.                (7.3)
```

Up to the extra logarithm caused by the deliberately universal heavy-tailed amplitude prior, (7.3) is Aden-Ali's polynomial PAC-Bayes objective.

So the naive statement

> "replace the Gaussian posterior by one sparse empirical posterior and optimize one scale"

is **not** a route through the full volumetric obstruction. Flat vectors regenerate it.

This is the informative failed intermediate lemma required by the owner directive: the new posterior helps precisely when coordinate localization is real, but a single global `s` still overpays the dense/flat stratum.

## 8. New broader class: overlapping coordinate norming covers

The preceding adaptive machinery suggests separating the geometry of *where a tensor norm is witnessed* from where its coefficients live. That yields a clean class substantially broader than the previous disjoint-block and bounded-interaction-support assumptions.

Let `E=span{T_1,...,T_n}`. Let

```text
S_1,...,S_K subseteq [d],
|S_a| <= b.
```

The sets may overlap arbitrarily. There is no assumption that coefficients of tensors in `E` vanish outside these sets, and no interaction-degree condition.

Assume only the norming property

```text
||A||_sym(I_p)
 <= L max_{1<=a<=K}
      || P_{S_a}^(tensor r) A ||_sym(I_p)
for every A in E.                                          (8.1)
```

### Theorem 8.1 (overlapping norming-cover type-2 bound)

For `2<=p<2r`, put `gamma=1/2-1/(2r)`. Under (8.1),

```text
E ||sum_i g_i T_i||_sym(I_p)
 <= C(r,p) L [ b^gamma + sqrt(log(2K)) ] S.                (8.2)
```

The `b^gamma` term uses the strongest current primary local polynomial bound (Aden-Ali Corollary 1.4 combined with the BGJLR contraction/injective comparison), not the older headline `b^gamma log b` estimate.

### Proof

For each `a`, set

```text
T_i^(a) := P_{S_a}^(tensor r) T_i,
Y_a(g) := ||sum_i g_i T_i^(a)||_sym(I_p).
```

Coordinate restriction is contractive, so

```text
(sum_i ||T_i^(a)||_sym(I_p)^2)^(1/2) <= S.                 (8.3)
```

In ambient dimension at most `b`, the current contraction bound gives

```text
E Y_a <= C(r,p) b^gamma S.                                 (8.4)
```

For completeness, this follows by inserting

```text
sigma_ell <= C_r b^max(ell/p-1/2,0) S
```

into Aden-Ali's symmetric Corollary 1.4. Multiplying by its prefactor `b^(1/2-1/p)`, the largest polynomial exponent over `ell<=r` is

```text
(1/2-1/p) + (1/p-1/(2r)) = gamma
```

when `p<2r`.

Also `Y_a` is `S`-Lipschitz as a function of `g`:

```text
|Y_a(g)-Y_a(h)|
 <= ||sum_i (g_i-h_i)T_i^(a)||
 <= ||g-h||_2
    (sum_i ||T_i^(a)||^2)^(1/2)
 <= S ||g-h||_2.                                           (8.5)
```

Gaussian concentration and the standard bound for the maximum of `K` subgaussian variables give

```text
E max_a Y_a
 <= max_a E Y_a + C S sqrt(log(2K)).                       (8.6)
```

Finally (8.1), applied pointwise to `A=sum_i g_iT_i`, yields

```text
||sum_i g_iT_i|| <= L max_a Y_a.
```

Combine with (8.4)--(8.6). QED.

### Dimension consequence

Suppose, up to polylogarithmic factors,

```text
L <= d^lambda,
b <= d^beta,
K <= d^C.
```

Then the polynomial exponent in (8.2) is

```text
lambda + beta gamma.                                       (8.7)
```

Hence this class reaches the conjectured source exponent whenever

```text
lambda + beta gamma <= alpha.                              (8.8)
```

This strictly removes the old requirements that the tensors decompose over disjoint blocks or that their coefficient-interaction hypergraph have bounded degree. Dense cross-support coefficients are allowed. What is required instead is a geometric statement about a small overlapping family of coordinate restrictions norming the whole span `E`.

This is still a restricted structural theorem, not the full conjecture.

## 9. Relation to the two C05 handoffs received this hour

Two reusable C05 lemmas were inspected rather than ignored:

1. the affine-cube entropy / flat-leverage handoff;
2. the logdet-deficit `=>` Frobenius covariance-defect lemma under `tr Sigma=d` and `0<Sigma<=2I`.

Neither lemma by itself verifies a missing hypothesis for Conjecture 16, so neither is inserted as an unsupported source claim. They do suggest a concrete way to organize the next multiscale attack: after normalizing/truncating the adaptive covariance in (4.10), a small logdet deficit certifies a near-isotropic bulk, while a large deficit identifies a volume-deficient / effectively sparse stratum. The affine-cube lemma can then reduce entropy if a decoupled sign selector is shown to lie in a low-dimensional affine constraint family. Establishing that bridge remains work, not a theorem claimed here.

## 10. What changed mathematically this run

### New proved statements

1. **Lemma 3.1:** a self-normalized barycentric PAC-Bayes inequality in which the quadratic cost is the posterior second moment, not a prior/global worst-case variance.

2. **Theorem 5.1:** an exact coordinate-adaptive empirical-posterior tensor inequality with covariance

```text
M_x=(1-1/s)xx^T + D_{x,q}/s
```

and explicit KL cost (4.6).

3. **Theorem 8.1:** a type-2 bound for arbitrary tensor spans normed by a polynomial-size family of overlapping low-dimensional coordinate restrictions. No disjoint-support or bounded interaction-degree condition is needed.

### Negative result / method boundary

The flat-vector calculation (7.1)--(7.3) proves that a one-scale use of Theorem 5.1 regenerates the Aden-Ali polynomial balance. Therefore one-shot sparsification is not enough for arbitrary tensors.

### Full-source metric

```text
arbitrary deterministic tensors:
    gamma -> gamma   (no full exponent movement)

target:
    alpha = 1/2-1/p
```

The progress is structural: a new posterior that passes the previous diagonal proof obstruction, plus a larger proved structural class and a sharper identification of where the remaining volumetric loss survives.

## 11. Remaining gap

The exact missing implication is now more specific than "beat Frobenius volume":

> Construct a multiscale decomposition of the source index set `B_p^d` for which the entropy paid at each scale is paired only with the **incremental** adaptive covariance energy at that scale, rather than multiplying one global selection entropy by the `ell=0` mean-square term at every point.

The reason is visible in Section 7. The posterior covariance can localize spiky vectors, but flat vectors make `D_{x,q}` essentially isotropic. A one-shot supremum then pays the whole point-selection KL against the whole process variance. Generic chaining avoids exactly this mistake by paying entropy only for increments.

## 12. Next concrete attack

The next run should build a **multiscale Maurey/PAC-Bayes chaining inequality** rather than another covariance variant.

Concrete target:

1. Stratify `x in B_p` by the entropy/effective support of

```text
q_x(j)=|x_j|/||x||_1
```

and by dyadic levels of the diagonal covariance

```text
D_x = diag(q_x + x^2/q_x).
```

2. Construct nested empirical posteriors with sample counts `s_0<s_1<...` and couple them so that

```text
E Theta_k = x
```

at every level but the PAC-Bayes loss is applied to the **difference process** between levels.

3. Prove an increment analogue of Lemma 3.1 whose scale-`k` contribution is

```text
sqrt( Delta_KL_k * Delta_V_k )
```

(or the corresponding optimized two-term expression), then sum over `k`.

4. Test the construction first on both extremal witnesses:
   - the diagonal/direct-sum tensor, where it must remain polylogarithmic;
   - a flat dense tensor / flat `x`, where it must not simply reproduce (7.3) at every scale.

5. Use the C05 logdet-to-Frobenius lemma only after a spectral cap is actually established: near-isotropic covariance should enter the dense branch, while large determinant deficit should trigger sparse-coordinate refinement.

A successful multiscale inequality would be a genuine route to arbitrary deterministic tensors because it leaves every `T_i` intact and decomposes only the test-vector geometry. If the first two-scale calculation still telescopes to the same global Aden-Ali objective, that is the next method pivot point.

## 13. Obligation ledger

| obligation | before | after |
|---|---|---|
| Full arbitrary-tensor exponent `gamma -> alpha` | OPEN | OPEN |
| Sparse/mixture posterior promised last run | not constructed | **PROVED: Theorem 5.1** |
| Escape previous diagonal anisotropic-Gaussian no-go | unknown | **YES, polylog on that witness** |
| Determine whether one sparse scale beats volumetric barrier | unknown | **NO: flat-vector calculation regenerates it** |
| Broader structural tensor class beyond disjoint / bounded-degree support | partial | **PROVED: overlapping norming-cover Theorem 8.1** |
| Multiscale/incremental entropy-variance coupling | OPEN | next attack |

No checker artifact is added because every claim in this run is analytic and the useful work is in the proofs above rather than a finite computation.
