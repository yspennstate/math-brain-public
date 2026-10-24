Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime does not expose authenticated GPT-6/maximum-effort attestation.

# P09 progress-first run — canonical KKT barycenter, a counterexample to raw critical-atom width, and selection-entropy chaining

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic symmetric tensors. In the unresolved regime `2 <= p < 2r`, the fixed full-source metric remains

```text
old arbitrary exponent = 1/2 - 1/(2r),
new arbitrary exponent = 1/2 - 1/(2r),
target exponent        = 1/2 - 1/p.
```

The substantive change is a method pivot forced by a new counterexample. The preceding report reduced the tensor norm to deterministic fixed-coordinate critical-atom classes `C_j`. This run proves that the raw Gaussian width of such a class can be polynomially larger than the original tensor process even at `r=3, p=2`: a tiny tensor channel can be amplified by the KKT rescaling at nonselected points while a separate anchor tensor fixes the source normalization. Therefore a worst-case deterministic cover of the whole `C_j` is not the right next lemma.

The replacement keeps only the **actually selected Gaussian witness**. Two new ingredients are proved:

1. every Gaussian maximizer admits a canonical, coordinate-free KKT barycenter `b_x` with exact exposure and norm at the conjectured scale `d^(1/2-1/p) S`;
2. an adaptive Gaussian chaining inequality replaces worst-case covering entropy by the **Shannon entropy of the quantized selected witness** at each Euclidean scale.

This gives a precise new full-source reduction: prove a polylogarithmic rate-distortion/selection-entropy profile for the canonical KKT witness distribution. Rare, geometrically complicated atoms then cost according to how often Gaussian optimization actually selects them, not according to their mere existence.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Registered role: `chaining / geometric-probabilistic proof`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Pre-write master observed: `6a22875227f4bae55034f2b12a260ffa9bfa6a90`.
- Immediate predecessor: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T154900Z__single-coordinate-kkt-witness-and-contraction-rank-bound.md`.
- Historical C0035 material, all earlier P09 reports, and peer-owned files are preserved. This report is additive and immutable.

---

## 1. Source target and bounded current-primary check

Primary source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizić-Nikolac, A. Rödder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 16.

For symmetric deterministic order-`r` tensors `T_1,...,T_n` on `R^d`, iid standard Gaussians `g_i`, and

```text
||T||_(I_p)
 := max_(||x||_p<=1) | <T,x^(tensor r)> |,
```

the source asks for

```text
E ||sum_i g_i T_i||_(I_p)
 <= C(r,p) polylog(d,n) d^(1/2-1/p)
    (sum_i ||T_i||_(I_p)^2)^(1/2).                       (1.1)
```

Write

```text
alpha := 1/2 - 1/p,
S^2   := sum_i ||T_i||_(I_p)^2.                           (1.2)
```

A bounded fresh check on 20 September 2026 again recovered the following primary/general references:

- Randomstrasse101, arXiv:2603.29571, still states Conjecture 16 and identifies the low-`p` volumetric obstruction;
- Bandeira--Gopi--Jiang--Lucca--Rothvoss, arXiv:2411.10633, remains the geometric/covering baseline for correlated random tensors;
- Ishaq Aden-Ali, arXiv:2503.10580, gives the PAC-Bayesian improvement of that general bound;
- Dartois--McKenna, arXiv:2603.01342, gives a newer moment approach for structured random-tensor models, not a resolution of the arbitrary deterministic correlated-summand statement (1.1).

No full resolution of the exact arbitrary deterministic `2 <= p < 2r` statement was found in this bounded check. This is not a claim about unpublished or unindexed work.

---

## 2. Inherited normalization and KKT identity

Let `\widetilde T_i` denote the symmetric `r`-linear form associated with the diagonal polynomial of `T_i`. Fix a real polarization constant `kappa_r` such that

```text
|\widetilde T_i(x_1,...,x_r)|
 <= kappa_r ||T_i||_(I_p) prod_a ||x_a||_p.               (2.1)
```

Define

```text
F(x) := (\widetilde T_i(x,...,x))_i in R^n,              (2.2)
(A_x v)_i := \widetilde T_i(x,...,x,v),                   (2.3)
```

where `A_x` has `r-1` copies of `x`. Then

```text
F(x)=A_x x,
DF(x)[v]=r A_x v.                                         (2.4)
```

The inherited source-normalized estimate is

```text
||A_x||_(HS) <= kappa_r S
for ||x||_p<=1.                                           (2.5)
```

For `g in R^n`, set

```text
h(g) := sup_(||x||_p<=1) |<g,F(x)>|.                      (2.6)
```

If `h(g)>0`, choose a sign `sigma` and a maximizer `x=x(g)` with `||x||_p=1` and

```text
sigma <g,F(x)> = h(g).                                    (2.7)
```

Let

```text
J_p(x)_j := |x_j|^(p-2) x_j.                              (2.8)
```

The KKT calculation from the preceding report gives the exact vector identity

```text
boxed:
sigma A_x^* g = h(g) J_p(x).                             (2.9)
```

Also

```text
||J_p(x)||_2
 = (sum_j |x_j|^(2p-2))^(1/2)
 >= d^(-alpha).                                           (2.10)
```

Equation (2.10) is the sharp finite-dimensional norm comparison already proved in the predecessor.

---

## 3. New theorem: a canonical coordinate-free KKT barycenter

The preceding report selected one coordinate `j`. The exact KKT relation actually yields a canonical convex average of *all* coordinate witnesses and removes that discrete choice entirely.

Let

```text
z := J_p(x),
D := ||z||_2^2.                                           (3.1)
```

Define

```text
boxed:
b_x := A_x z / D.                                        (3.2)
```

### Theorem 3.1 — canonical exact-exposure witness

At every Gaussian maximizer chosen above,

```text
boxed:
<sigma g,b_x> = h(g),                                    (3.3)
```

and

```text
boxed:
||b_x||_2 <= kappa_r d^alpha S.                          (3.4)
```

#### Proof

By (2.9),

```text
<sigma g,A_x z>
 = <sigma A_x^* g,z>
 = h(g) ||z||_2^2
 = h(g) D.                                                (3.5)
```

Division by `D` proves (3.3).

For the norm,

```text
||b_x||_2
 <= ||A_x||_(2->2) ||z||_2 / D
 <= ||A_x||_(HS) / ||z||_2
 <= kappa_r S / ||z||_2.                                 (3.6)
```

Using (2.10) gives (3.4). QED.

### Relation to the coordinate witnesses

The predecessor defined, for `x_j !=0`,

```text
a_(x,j)
 := sgn(x_j)|x_j|^(1-p) A_x e_j.                         (3.7)
```

Let

```text
w_j := |x_j|^(2p-2) / D.                                 (3.8)
```

Then `w_j>=0`, `sum_j w_j=1`, and

```text
sum_j w_j a_(x,j)
 = (1/D) sum_j sgn(x_j)|x_j|^(p-1) A_x e_j
 = A_x J_p(x)/D
 = b_x.                                                   (3.9)
```

Thus the new witness is literally the KKT-weighted barycenter of all exact-exposure coordinate atoms. Every atom in that convex combination lies on the same supporting hyperplane, so averaging loses **zero** objective value while improving stability.

### Why this is stronger than the preceding pointwise reduction

The one-coordinate theorem required a choice among `d` coordinates and then enlarged to deterministic classes `C_j`. The barycenter gives a single measurable witness map with no coordinate label:

```text
h(g)=<g,B(g)>,
B(g):=sigma(g) b_(x(g)),
||B(g)||_2 <= R_*:=kappa_r d^alpha S.                    (3.10)
```

The remaining problem is therefore the complexity of the **distribution of the selected vector `B(g)`**, not the union of all algebraically possible rescaled columns.

---

## 4. Dual-normal parametrization: where the dimension exponent comes from

Let

```text
q := p/(p-1) in [1,2],
y := z/||z||_2 in S^(d-1).                               (4.1)
```

Since `||J_p(x)||_q=1`, we have

```text
z = y / ||y||_q.                                         (4.2)
```

The inverse duality map gives

```text
x
 = J_q(y) / ||y||_q^(q-1),                               (4.3)
```

where `J_q(y)_j=sgn(y_j)|y_j|^(q-1)`. Also

```text
D = 1/||y||_q^2.                                         (4.4)
```

Substituting into (3.2) yields the exact representation

```text
boxed:
b_x
 = ||y||_q A_(x(y)) y.                                   (4.5)
```

Since `||y||_2=1`,

```text
||y||_q <= d^(1/q-1/2)=d^alpha.                          (4.6)
```

Therefore the conjectured polynomial factor appears here as exactly the distortion between the Euclidean normal direction and its `l_q` norm. At `p=2`, `q=2`, `x(y)=y` and

```text
b_x=A_x x=F(x).                                           (4.7)
```

So in the Euclidean case the canonical witness collapses to the original exposed output point, as it should.

This parametrization suggests that the arbitrary problem should be attacked through the distribution of exposed **normal directions**, not through the full tangent field.

---

## 5. Counterexample: the raw fixed-coordinate critical-atom class can have huge width

The predecessor proposed bounding, for a fixed coordinate `j`, the Gaussian width of the deterministic critical-atom class `C_j`. The following example shows that this is too large a target even though the original tensor process is small.

It already occurs for

```text
r=3,
p=2.                                                     (5.1)
```

### Construction

Let the input dimension be

```text
d=m+1,
x=(t,y),
y in R^m.                                               (5.2)
```

Let `{B_a}_{a=1}^M` be an orthonormal basis of the real symmetric `m x m` matrices in Frobenius norm, where

```text
M=m(m+1)/2,                                               (5.3)
```

chosen so that `||B_a||_op<=1` for every `a`.

Take

```text
epsilon := m^(-2).                                       (5.4)
```

Define one anchor cubic and `M` tiny cubics by their diagonal polynomials:

```text
P_0(t,y) := t^3,                                          (5.5)
P_a(t,y) := epsilon t y^T B_a y,
1<=a<=M.                                                  (5.6)
```

Let `T_0,T_1,...,T_M` be the corresponding symmetric order-three tensors.

### Source normalization remains constant

Clearly

```text
||T_0||_(I_2)=1.                                         (5.7)
```

For `a>=1`, if `t^2+||y||_2^2<=1`,

```text
|t y^T B_a y|
 <= |t| ||B_a||_op ||y||_2^2
 <= 2/(3 sqrt(3)),                                       (5.8)
```

because `max_(0<=s<=1) s(1-s^2)=2/(3sqrt(3))`. Hence

```text
||T_a||_(I_2) <= C epsilon.                              (5.9)
```

Therefore

```text
S^2
 = sum_(a=0)^M ||T_a||_(I_2)^2
 <= 1 + C M epsilon^2
 = 1+O(m^(-2)).                                           (5.10)
```

So `S asymp 1`.

### The raw class `C_0` contains a large matrix-sphere image

For cubics, `DF(x)=3A_x`. Differentiating in the `t` direction gives

```text
(A_x e_0)_0 = t^2,                                       (5.11)
(A_x e_0)_a = (epsilon/3) y^T B_a y.                    (5.12)
```

At points with

```text
t=epsilon,
||y||_2^2=1-epsilon^2,                                   (5.13)
```

the `p=2` rescaled coordinate atom is

```text
a_(x,0)
 = t^(-1) A_x e_0
 = ( epsilon,
     (1/3)(y^T B_a y)_(a=1)^M ).                         (5.14)
```

By Frobenius orthonormality,

```text
sum_a (y^T B_a y)^2
 = ||y y^T||_F^2
 = ||y||_2^4.                                            (5.15)
```

Thus every atom in (5.14) has Euclidean norm bounded above and below by absolute constants. Since `S asymp1`, these atoms satisfy the predecessor's radius cutoff and belong to `C_0` after harmless fixed polarization constants.

Let `gamma_a` be iid standard Gaussians and

```text
G := sum_a gamma_a B_a.                                  (5.16)
```

Then

```text
sup_(||u||_2=1)
 |sum_a gamma_a u^T B_a u|
 = ||G||_op.                                              (5.17)
```

For this standard Gaussian symmetric-matrix ensemble,

```text
E||G||_op >= c sqrt(m).                                  (5.18)
```

Consequently

```text
boxed:
E sup_(a in C_0) |<g,a>|
 >= c sqrt(m).                                           (5.19)
```

### Yet the original tensor process has constant expected norm

For the same Gaussian coefficients,

```text
sum_a g_a P_a(t,y)
 = g_0 t^3 + epsilon t y^T G y.                          (5.20)
```

Therefore

```text
h(g)
 <= |g_0|
    + (2/(3sqrt(3))) epsilon ||G||_op.                   (5.21)
```

Taking expectations and using `epsilon=m^(-2)` gives

```text
boxed:
E h(g) = O(1),                                           (5.22)
```

while `S asymp1` and the raw critical-atom width in (5.19) is `Omega(sqrt(m))`.

### Interpretation

The tiny channels `P_a` have total source energy `o(1)`, but at nonselected points with `t=epsilon`, division by `t` amplifies their directions to constant radius. The anchor `P_0=t^3` keeps `S` of order one. The deterministic class `C_0` therefore remembers many directions that Gaussian optimization almost never uses.

This counterexample refutes the proposed intermediate statement

```text
max_j GaussianWidth(C_j)
 <= polylog(d,n) S                                      (5.23)
```

in the generality needed for the full conjecture. It does **not** refute Conjecture 16; indeed the actual process in the example is bounded by (5.22).

This is the exact reason to switch from worst-case atom entropy to **selection-weighted entropy**.

---

## 6. New probability lemma: entropy cost of adaptive Gaussian selection

The following elementary lemma is the core replacement for raw branch counts. No literature-novelty claim is made; it is a direct Gaussian concentration/information argument specialized to the present proof architecture.

### Lemma 6.1 — conditional mean shift on a Gaussian event

Let `G~N(0,I_n)`. Let `Z=Z(G)` be `R`-Lipschitz and let

```text
mu := E Z.                                                (6.1)
```

If `E` is any measurable event with probability `pi in (0,1]`, then

```text
boxed:
E[Z | E]
 <= mu + R sqrt(2 log(1/pi)).                            (6.2)
```

#### Proof

Gaussian concentration in exponential-moment form gives, for `lambda>0`,

```text
E exp(lambda(Z-mu))
 <= exp(lambda^2 R^2/2).                                 (6.3)
```

On the other hand, conditional Jensen gives

```text
E exp(lambda(Z-mu))
 >= pi exp(lambda(E[Z|E]-mu)).                           (6.4)
```

Combining,

```text
E[Z|E]-mu
 <= log(1/pi)/lambda + lambda R^2/2.                    (6.5)
```

Optimize at

```text
lambda=sqrt(2 log(1/pi))/R.                              (6.6)
```

This proves (6.2). QED.

### Theorem 6.2 — finite adaptive model-selection inequality

Let `{E_a}` be a finite or countable measurable partition of Gaussian space, with

```text
pi_a := P(E_a).                                          (6.7)
```

For each `a`, let `Z_a(G)` be `R_a`-Lipschitz with mean

```text
mu_a:=E Z_a.                                             (6.8)
```

Suppose a nonnegative random quantity `H(G)` satisfies

```text
H(G) <= Z_a(G) on E_a.                                   (6.9)
```

Then

```text
boxed:
E H
 <= sum_a pi_a mu_a
    + sqrt(2) sum_a pi_a R_a sqrt(log(1/pi_a)).          (6.10)
```

In particular, writing Shannon entropy

```text
Ent(pi):=sum_a pi_a log(1/pi_a),                         (6.11)
```

Cauchy--Schwarz gives

```text
boxed:
E H
 <= sum_a pi_a mu_a
    + sqrt( 2 Ent(pi) sum_a pi_a R_a^2 ).                (6.12)
```

If all `R_a<=R` and all `mu_a<=mu`, then

```text
boxed:
E H <= mu + R sqrt(2 Ent(pi)).                           (6.13)
```

#### Proof

Apply Lemma 6.1 to `Z_a` on `E_a`, multiply by `pi_a`, and sum. This gives (6.10). Apply Cauchy--Schwarz to the second sum for (6.12). QED.

### Linear-vector specialization

If a finite-valued random vector `V=V(G)` takes values `v_a` on `E_a`, then `Z_a(G)=<G,v_a>` has mean zero and Lipschitz constant `||v_a||_2`. Therefore

```text
boxed:
E <G,V(G)>
 <= sqrt(2 E||V||_2^2 H(V)),                             (6.14)
```

where `H(V)` is the Shannon entropy of the discrete law of `V`.

This inequality is exactly suited to selected KKT witnesses: directions that exist geometrically but are chosen only on rare Gaussian events are automatically discounted.

---

## 7. Main new chaining theorem: quantized selector entropy replaces covering entropy

Worst-case Dudley chaining pays `log N(A,epsilon)` for every point in a deterministic set `A`. Here the optimizer itself is random and highly nonuniform. The next theorem chains the **selected vector** directly.

### Theorem 7.1 — adaptive Gaussian selector chaining

Let

```text
G~N(0,I_n),                                               (7.1)
```

and let `B=B(G)` be a measurable `R^n`-valued random vector satisfying

```text
||B||_2 <= R almost surely.                              (7.2)
```

For scales

```text
epsilon_0:=R,
epsilon_k downarrow 0,                                   (7.3)
```

let `Q_k(B)` be any finite-valued quantizations such that

```text
||B-Q_k(B)||_2 <= epsilon_k almost surely.               (7.4)
```

Set `Q_0:=0`. Then

```text
boxed:
E <G,B>
 <= sqrt(2) sum_(k>=1)
      (epsilon_(k-1)+epsilon_k)
      sqrt( H(Q_(k-1),Q_k) ).                            (7.5)
```

whenever the right side is finite. More generally, for finite `K`,

```text
E <G,B>
 <= sqrt(2) sum_(k=1)^K
      (epsilon_(k-1)+epsilon_k)
      sqrt( H(Q_(k-1),Q_k) )
    + epsilon_K E||G||_2.                                (7.6)
```

#### Proof

Write

```text
V_k:=Q_k-Q_(k-1).                                        (7.7)
```

Then `V_k` is finite-valued and

```text
||V_k||_2
 <= ||Q_k-B||_2+||B-Q_(k-1)||_2
 <= epsilon_k+epsilon_(k-1).                             (7.8)
```

By the linear specialization (6.14),

```text
E<G,V_k>
 <= sqrt(2 E||V_k||_2^2 H(V_k))                         (7.9)
```

and therefore

```text
E<G,V_k>
 <= sqrt(2)(epsilon_(k-1)+epsilon_k) sqrt(H(V_k)).        (7.10)
```

Since `V_k` is a deterministic function of the pair `(Q_(k-1),Q_k)`,

```text
H(V_k)
 <= H(Q_(k-1),Q_k).                                      (7.11)
```

Summing the telescoping identity

```text
Q_K=sum_(k=1)^K V_k                                     (7.12)
```

gives the main sum in (7.6). The residual obeys

```text
|E<G,B-Q_K>|
 <= E ||G||_2 ||B-Q_K||_2
 <= epsilon_K E||G||_2.                                 (7.13)
```

This proves (7.6). Letting `K->infinity` proves (7.5). QED.

### Dyadic form

Take

```text
epsilon_k=2^(-k)R.                                      (7.14)
```

Then

```text
H(Q_(k-1),Q_k)
 <= H(Q_(k-1))+H(Q_k),                                   (7.15)
```

so

```text
boxed:
E<G,B>
 <= C R sum_(k>=1) 2^(-k)
    sqrt( H(Q_(k-1))+H(Q_k) ).                           (7.16)
```

for an absolute `C`.

The analogy with Dudley is exact, except that **worst-case log covering numbers are replaced by Shannon entropies of the actually selected quantized vector**.

---

## 8. Rate-distortion entropy formulation

For a bounded random vector `B`, define the hard-error quantization entropy

```text
H_B(epsilon)
 := inf {
          H(Q(B)) :
          Q finite-valued,
          ||B-Q(B)||_2 <= epsilon a.s.
        }.                                               (8.1)
```

No independence is imposed: `B` is itself a deterministic function of the same Gaussian vector `G`. The entropy is taken only over the induced selector distribution.

Choosing near-optimal quantizers at dyadic scales in Theorem 7.1 gives

```text
boxed:
E<G,B>
 <= C sum_(k>=1) epsilon_(k-1)
    sqrt(
      H_B(epsilon_(k-1))
      + H_B(epsilon_k)
    ),                                                   (8.2)
```

with `epsilon_k=2^(-k)R`.

A convenient sufficient condition is

```text
H_B(epsilon)
 <= L^2 [1+log(R/epsilon)]^2                             (8.3)
```

for all `0<epsilon<=R`. Then

```text
sum_k 2^(-k)(1+k)<infinity,                              (8.4)
```

so

```text
boxed:
E<G,B> <= C L R.                                         (8.5)
```

This condition permits the support of `B` to have arbitrarily large or even infinite worst-case covering entropy, provided the high-complexity regions carry sufficiently little selector probability.

---

## 9. Application to Conjecture 16: a new exact probabilistic reduction

Choose a measurable maximizing pair `(sigma(g),x(g))` in (2.7). Such a selection exists by the standard measurable maximum theorem because the `l_p` unit sphere is compact and the polynomial objective is continuous.

Define the canonical selected KKT witness

```text
B(g):=sigma(g) b_(x(g)).                                 (9.1)
```

By Theorem 3.1,

```text
boxed:
h(g)=<g,B(g)>,                                           (9.2)
```

and

```text
boxed:
||B(g)||_2 <= R_*:=kappa_r d^alpha S.                   (9.3)
```

Therefore Theorem 7.1 applies directly.

### Corollary 9.1 — selection-entropy reduction for P09

If the canonical witness distribution satisfies

```text
H_B(epsilon)
 <= L(d,n)^2 [1+log(R_*/epsilon)]^2                      (9.4)
```

for all scales, then

```text
boxed:
E ||sum_i g_i T_i||_(I_p)
 <= C kappa_r L(d,n)
    d^(1/2-1/p) S.                                       (9.5)
```

Hence Conjecture 16 follows whenever

```text
L(d,n)=polylog(d,n).                                     (9.6)
```

This is a **conditional reduction**, not the full conjecture.

### What changed relative to the old volumetric obstruction

A deterministic volumetric cover pays for every possible parameter/tangent/atom. The counterexample in Section 5 shows this can be grossly wrong because tiny channels create many rescaled atoms that are practically never selected.

The new obligation is not

```text
log N(all possible atoms,epsilon) <= polylog.             (9.7)
```

It is

```text
entropy of the actually selected quantized witness
at each scale <= polylogarithmic profile.                 (9.8)
```

The distinction is essential rather than cosmetic.

---

## 10. Calibration on the Hadamard-hypercube obstruction

The preceding report constructed a `p=2` matrix/tensor example with flat maximizers and unavoidable `sqrt(log d)` growth. In that example the exposed output witness takes a finite set of sign-code values.

For the matrix model with `d=2^m`, the canonical `p=2` witness equals the exposed output point and, up to normalization, takes values

```text
B(g) in { s/sqrt(m) : s in {+-1}^m }.                   (10.1)
```

The maximizing sign code is determined by the signs of `m` independent Gaussian coordinates, so its law is uniform and

```text
H(B)=m log 2=log d.                                      (10.2)
```

Also `||B||_2=1`. The finite-selector form (6.14) therefore gives

```text
E h(g)
 <= sqrt(2 log d),                                       (10.3)
```

matching the known `Theta(sqrt(log d))` behavior up to an absolute constant.

Thus the selector-entropy theorem correctly charges the genuine sign-code complexity that KKT mass profiles and local transverse area both missed.

---

## 11. Why the new counterexample is neutralized by selection weighting

Return to the anchored cubic family of Section 5. The large raw width came from points with

```text
t=epsilon=m^(-2),                                       (11.1)
```

where tiny quadratic channels were divided by `t`.

For a Gaussian coefficient matrix `G`, optimization over `y` reduces the small-channel part at fixed `t` to a Rayleigh quotient. Along an extremal eigenvector with eigenvalue `lambda`, the one-dimensional objective has the form

```text
f(t)=g_0 t^3 + epsilon lambda t(1-t^2).                  (11.2)
```

An interior stationary point satisfies

```text
epsilon lambda
 + 3(g_0-epsilon lambda)t^2=0.                           (11.3)
```

Thus forcing a stationary point at `t` of order `epsilon` requires

```text
|g_0|
 of order |lambda|/epsilon,                              (11.4)
```

apart from fixed constants. For a typical Gaussian symmetric matrix `|lambda|` is order `sqrt(m)`, whereas `epsilon=m^(-2)`. Such directions require an anchor coefficient of polynomially enormous Gaussian size and therefore lie in an extremely small selector region.

This calculation is only a calibration, not a full normal-cone estimate, but it explains exactly why the deterministic width in (5.19) is spurious and why entropy weighted by actual Gaussian selection is the correct quantity.

---

## 12. A genuinely broader restricted theorem

The new machinery yields an unconditional theorem for a class defined by **low-information exposed geometry**, rather than low algebraic rank or a common frame.

### Theorem 12.1 — low selector-rate class

Under the source normalization, suppose the canonical KKT witness `B(g)` from (9.1) has hard-error quantization entropy satisfying

```text
H_B(epsilon)
 <= L^2 [1+log(R_*/epsilon)]^2                           (12.1)
```

for some finite `L`. Then

```text
E ||sum_i g_i T_i||_(I_p)
 <= C_r L d^(1/2-1/p) S.                                (12.2)
```

In particular, if `L=polylog(d,n)`, the conjectured polynomial dimension exponent holds.

This class permits:

- continuously rotating tangent and covariance frames;
- very large or infinite worst-case atom sets;
- exponentially many algebraic branches;
- rare high-complexity branches;
- no common invariant output subspace;
- no low coordinate-contraction rank assumption.

It is therefore genuinely different from, and in many cases broader than, the preceding deterministic rank/frame/dictionary hypotheses. The theorem is still **restricted/conditional on the selector-entropy profile** and is not asserted as a literature-new named class.

A finite-valued special case is especially simple: if the canonical selected witness takes values in an arbitrary finite set but has Shannon entropy at most `H_0`, then

```text
boxed:
E h(g)
 <= R_* sqrt(2H_0)
 <= kappa_r d^alpha S sqrt(2H_0).                        (12.3)
```

The number of possible witness values may be enormous; only the entropy of the selected law matters.

---

## 13. Remaining full-source gap

The arbitrary conjecture is not solved. The new exact obligation is to exploit the tensor/KKT structure to bound the scale-dependent entropy of

```text
B(g)
 = sigma(g)
   A_(x(g)) J_p(x(g))
   / ||J_p(x(g))||_2^2.                                  (13.1)
```

The raw support of this map can still be complicated. What must now be shown is that Gaussian optimization cannot distribute substantial probability mass over too many separated values of `B(g)` at too many scales.

The desired scale statement is of the form

```text
H_B(2^(-k)R_*)
 <= polylog(d,n)^2 (1+k)^2,                              (13.2)
```

or any comparable profile whose weighted dyadic square-root sum is polylogarithmic.

This is a probability/normal-fan statement rather than a volumetric covering statement.

---

## 14. Next concrete attack

The next run should attack (13.2) directly, with the following sequence.

### 14.1 First branch: Gaussian normal-cone entropy

For a quantized witness cell `Q`, estimate

```text
P(B(g) in Q)                                             (14.1)
```

through the KKT relation

```text
A_x^* g = sigma h(g) J_p(x).                             (14.2)
```

The goal is a coding inequality saying that many well-separated witness cells force correspondingly small Gaussian normal-cone masses. This would convert geometric separation into Shannon entropy without counting all cells uniformly.

### 14.2 Second branch: multiscale coarea/Kac--Rice

The earlier P09 Kac--Rice reports already derived that inverse curvature cancels against the critical-field Jacobian on regular image sheets and that switching strata are weighted by actual output chords. Reuse that machinery only to estimate **selector probabilities of witness cells**, not to integrate every critical point. This is a materially different target from the failed raw curvature-counting route.

### 14.3 Mandatory falsification tests

Any proposed entropy lemma must survive:

1. the Hadamard-hypercube example, where `H(B)=Theta(log d)` is genuinely necessary;
2. the anchored cubic example in Section 5, where raw atom width is `Omega(sqrt d)` but actual process width is `O(1)`;
3. the previous zero-process rotating-column example, which should receive essentially zero selected mass;
4. the dense-dust example, where many tiny directions must be deferred to fine scales;
5. the previous global-Haar-sketch example, to ensure auxiliary randomness does not manufacture entropy.

### 14.4 Pivot rule

This run materially changed method because the deterministic `C_j` width target was falsified. If two subsequent runs fail to obtain a nontrivial selector-entropy bound from KKT normal cones/coarea, preserve the reduction above and hand off to another registered probability bottleneck as directed by the owner policy.

---

## 15. Obligation ledger

| Item | Before this run | After this run |
|---|---|---|
| Full arbitrary exponent in `2<=p<2r` | `1/2-1/(2r)` | unchanged |
| Target exponent | `1/2-1/p` | unchanged |
| Pointwise witness | one selected coordinate atom | **canonical KKT barycenter; exact exposure and target-scale radius** |
| Coordinate-selection cost | `sqrt(log d)` from union over `j` | **removed at the pointwise level** |
| Proposed next entropy object | full deterministic `C_j` | **refuted as too large** |
| New counterexample | none to raw `C_j` width | **cubic anchored tiny-channel family: `width(C_0)=Omega(sqrt d)` while original width `O(1)`** |
| New probability inequality | finite dictionary concentration only | **selection-entropy inequality + adaptive selector chaining** |
| New full-source reduction | cover one fixed-coordinate contraction class | **bound rate-distortion entropy of the actually selected canonical KKT witness** |
| Restricted theorem | low coordinate-contraction rank | **low selector-rate class, allowing huge worst-case support** |
| Remaining gap | worst-case contraction entropy | **Gaussian normal-cone/selector entropy profile** |

---

## 16. Status

**PROVED PARTIAL.** The full Randomstrasse101 Conjecture 16 remains open here. The arbitrary exponent has not improved. The mathematical progress is instead a sharper and probability-correct reduction:

- a canonical exact KKT barycenter at the conjectured radius;
- an explicit counterexample proving that worst-case critical-atom width is the wrong target;
- a rigorous Gaussian selection-entropy inequality;
- a rigorous multiscale adaptive chaining theorem for the selected witness;
- and a new exact route from a polylogarithmic selector rate-distortion profile to the source exponent.

No matrix, rank-one, independent-entry, `p>=2r`, or other known structured case is relabeled as new. No full-source solution is claimed.