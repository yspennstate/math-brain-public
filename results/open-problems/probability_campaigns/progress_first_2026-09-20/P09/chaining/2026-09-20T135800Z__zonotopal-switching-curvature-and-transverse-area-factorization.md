Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime does not expose authenticated GPT-6/maximum-effort attestation.

# P09 progress-first run — exact zonotopal switching curvature, transverse-area complexity, and a multiscale factorization bound

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The full arbitrary-tensor polynomial exponent in the unresolved regime `2 <= p < 2r` remains

```text
gamma = 1/2 - 1/(2r),
```

versus the conjectured

```text
alpha = 1/2 - 1/p.
```

The preceding report reduced the new obstruction to Gaussian-weighted switching curvature on the exposed output image and proved that an equal-weight matrix cube has all of its logarithmic excess in that switching term. This run attacks that obstruction exactly for a much larger polyhedral family: **arbitrary zonotopes, with arbitrary generator lengths and arbitrary correlations**.

The main new identity is that if

```text
Z = sum_(j=1)^m [-v_j,v_j] subset R^n
```

and `h_Z` is its support function, then its entire singular switching-curvature budget is

```text
boxed:
I_switch(Z)
 = (4/pi) sum_(1<=j<l<=m)
     sqrt( ||v_j||_2^2 ||v_l||_2^2 - <v_j,v_l>^2 ).
```

Thus the correct cost is not the number of vertices (`Z` may have exponentially many), and not even the number of generators by itself. It is the sum of pairwise **transverse parallelogram areas** of the generators. Parallel generators create no switching curvature; orthogonal generators are maximally expensive.

Combining this identity with the Gaussian support-curvature identity gives the structural bound

```text
boxed:
(E h_Z(g)^2)^(1/2)
 <= [ R_Z^2 + (4/pi) A_Z ]^(1/2),
```

where

```text
R_Z := max_(z in Z) ||z||_2,
A_Z := sum_(j<l)
       sqrt( ||v_j||_2^2 ||v_l||_2^2 - <v_j,v_l>^2 ).
```

This yields a new tensor sufficient condition: if the symmetrized output body is contained in one zonotope, or in a Minkowski sum of zonotopes, whose radius-plus-transverse-area energy is at most the conjectured `d^alpha S` scale up to polylogarithms, then Conjecture 16's desired polynomial exponent follows for that family. This class allows exponentially many exposed vertices, arbitrary generator correlations, continuously many tensor parameters behind the same output body, and no common-frame or commuting-covariance assumption.

The equal-weight cube from the predecessor is a special orthogonal case. More generally, a weighted cube gives the exact formulas

```text
E h = sqrt(2/pi) ||a||_1,
S = ||a||_2,
I_switch = (2/pi)(||a||_1^2-||a||_2^2).
```

Hence its true effective switching complexity is

```text
m_eff = (||a||_1/||a||_2)^2,
```

not the raw number `2^m` of exposed vertices. This supplies an explicit counterexample to any future intermediate lemma that charges all branches equally: one may have `2^m` branches while `m_eff=O(1)` if the switch amplitudes decay sufficiently fast.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Registered role: `chaining / geometric-probabilistic proof`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Pre-write master observed: `47f77a4f665bc299f7b292b7674d177bb9b2d7f1`
- Immediate predecessor: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T132800Z__intrinsic-image-kac-rice-and-switching-curvature.md`, blob `4bb5fd1f37b261362adca988e58a1815fdbd9365`.
- Historical C0035 material, all prior P09 reports, and peer files are preserved. This report is additive and immutable.

---

## 1. Exact source normalization and current primary baseline

Primary source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizić-Nikolac, A. Rödder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.

For symmetric deterministic order-`r` tensors `T_1,...,T_n` on `R^d`, iid standard Gaussian `g_i`, and

```text
||T||_(I_p) := sup_(||x||_p<=1) |T[x,...,x]|,
```

the source asks for

```text
E ||sum_i g_i T_i||_(I_p)
 <= C(r,p) polylog(d,n) d^(1/2-1/p)
    (sum_i ||T_i||_(I_p)^2)^(1/2).                  (1.1)
```

A bounded primary-source check on 20 September 2026 again recovers:

- Randomstrasse101, arXiv:2603.29571, still stating Conjecture 16;
- Bandeira--Gopi--Jiang--Lucca--Rothvoss, arXiv:2411.10633, as the general geometric correlated-tensor baseline;
- Aden-Ali, arXiv:2503.10580, Theorem 1.2 / Corollary 1.4, as a sharper PAC-Bayesian variance-parameter inequality which improves the first logarithmic term but explicitly describes the remaining higher-order/Frobenius terms as volumetric in the regimes relevant here;
- no full resolution in that bounded search of the exact arbitrary deterministic `2 <= p < 2r` statement.

This is a bounded source check, not a claim about unpublished or unindexed work.

The fixed source metric is therefore unchanged:

```text
old arbitrary exponent = 1/2 - 1/(2r)
new arbitrary exponent = 1/2 - 1/(2r)
target exponent        = 1/2 - 1/p
source status           = OPEN / not solved here.
```

---

## 2. Output-body and support-curvature notation

Set

```text
S^2 := sum_i ||T_i||_(I_p)^2,
F(x) := (T_i[x^r])_(i=1)^n,
K := conv(F(B_p^d) union -F(B_p^d)).                    (2.1)
```

Then

```text
h_K(g)
 := sup_(y in K) <g,y>
  = ||sum_i g_iT_i||_(I_p).                              (2.2)
```

Coordinatewise Cauchy--Schwarz gives

```text
||F(x)||_2 <= S                                           (2.3)
```

for all `x in B_p^d`, so

```text
K subset S B_2^n.                                        (2.4)
```

The predecessor established the distributional Gaussian support-curvature identity

```text
E h_K(g)^2
 = E ||grad h_K(g)||_2^2
   + integral h_K(g) phi_n(g) d(Delta h_K)(g).            (2.5)
```

At branch-switch interfaces, the singular Laplacian density is exactly the output chord length. The equal-weight matrix cube showed that this singular term can be `Theta(S^2 log d)` and can carry the whole excess over the gradient term.

The question left open was: **what geometric aggregate of many switching interfaces has the right scale?**

For zonotopes, this run answers that question exactly.

---

## 3. Zonotopes and their support functions

Let nonzero vectors

```text
v_1,...,v_m in R^n                                       (3.1)
```

be arbitrary; parallelism and linear dependence are allowed. Define the centrally symmetric zonotope

```text
Z
 := sum_(j=1)^m [-v_j,v_j]
 = { sum_j t_j v_j : |t_j|<=1 }.                         (3.2)
```

Put

```text
a_j := ||v_j||_2,
u_j := v_j/a_j.                                       (3.3)
```

Its support function is

```text
h_Z(g)
 = sum_(j=1)^m |<g,v_j>|.                                (3.4)
```

This follows from independent maximization over each coefficient `t_j in [-1,1]`.

Consequently, for standard Gaussian `g`,

```text
E h_Z(g)
 = sqrt(2/pi) sum_j a_j.                                 (3.5)
```

The point of the next theorem is not (3.5), which is elementary. It is the exact decomposition of the **switching-curvature measure** generated by the exponentially large normal fan of `Z`.

---

## 4. Exact Hessian and Laplacian measures of one segment support function

Fix `v=a u` with `a=||v||_2>0` and `||u||_2=1`. Define

```text
f_v(g):=|<g,v>|=a |<g,u>|.                               (4.1)
```

Let

```text
H_u := {g : <g,u>=0}.                                    (4.2)
```

### Lemma 4.1 — one-segment distributional Hessian

Distributionally on `R^n`,

```text
boxed:
D^2 f_v
 = 2a (u tensor u) H^(n-1)|_(H_u),                       (4.3)
```

and hence

```text
boxed:
Delta f_v
 = 2a H^(n-1)|_(H_u).                                    (4.4)
```

#### Proof

Choose orthonormal coordinates `(t,z)` with `t=<g,u>` and `z in H_u`. Then

```text
f_v(t,z)=a|t|.                                           (4.5)
```

In one dimension,

```text
d^2|t|/dt^2 = 2 delta_0                                  (4.6)
```

as distributions. All mixed and tangential derivatives vanish. Returning to ambient coordinates gives (4.3). Taking the trace of `u tensor u` gives (4.4). QED.

Since (3.4) is a sum of such functions,

```text
boxed:
Delta h_Z
 = 2 sum_j a_j H^(n-1)|_(H_(u_j)).                       (4.7)
```

Every term in (4.7) is a branch-switch hyperplane. There is no absolutely continuous curvature because `h_Z` is piecewise linear.

---

## 5. Exact transverse-area formula for zonotopal switching curvature

Define the transverse-area complexity

```text
A_Z
 := sum_(1<=j<l<=m)
    Area(v_j,v_l),                                       (5.1)
```

where

```text
Area(v_j,v_l)
 := sqrt(
      ||v_j||_2^2 ||v_l||_2^2
      - <v_j,v_l>^2
    ).                                                    (5.2)
```

This is the Euclidean area of the parallelogram spanned by `v_j,v_l`. It vanishes exactly when the two generators are parallel.

### Theorem 5.1 — exact zonotopal switching-curvature identity

For standard Gaussian density `phi_n`,

```text
boxed:
I_switch(Z)
 := integral_(R^n) h_Z(g) phi_n(g) d(Delta h_Z)(g)
  = (4/pi) A_Z.                                          (5.3)
```

Equivalently,

```text
I_switch(Z)
 = (2/pi) sum_(j != l)
   sqrt(
     ||v_j||_2^2 ||v_l||_2^2
     - <v_j,v_l>^2
   ).                                                     (5.4)
```

#### Proof

From (4.7),

```text
I_switch(Z)
 = 2 sum_j a_j
   integral_(H_(u_j))
      h_Z(g) phi_n(g) dH^(n-1)(g).                       (5.5)
```

On `H_(u_j)`, the `j`th support term vanishes, so

```text
h_Z(g)
 = sum_(l != j) |<g,v_l>|.                               (5.6)
```

Therefore

```text
I_switch(Z)
 = 2 sum_(j != l) a_j
   integral_(H_(u_j))
      |<g,v_l>| phi_n(g) dH^(n-1)(g).                    (5.7)
```

The restriction of `phi_n(g)dH^(n-1)(g)` to `H_(u_j)` has total mass

```text
phi_1(0)=1/sqrt(2pi),                                    (5.8)
```

and after normalization is standard Gaussian measure on that hyperplane. Hence, with `G_j` standard Gaussian in `H_(u_j)`,

```text
integral_(H_(u_j))
 |<g,v_l>| phi_n(g)dH^(n-1)(g)

 = phi_1(0) E|<G_j,v_l>|

 = (1/sqrt(2pi)) sqrt(2/pi)
   ||P_(H_(u_j)) v_l||_2

 = (1/pi) ||P_(H_(u_j)) v_l||_2.                        (5.9)
```

Now

```text
a_j^2 ||P_(H_(u_j))v_l||_2^2
 = a_j^2 ||v_l||_2^2 - <v_j,v_l>^2,                     (5.10)
```

so

```text
a_j ||P_(H_(u_j))v_l||_2
 = Area(v_j,v_l).                                        (5.11)
```

Substituting (5.9)--(5.11) into (5.7) gives

```text
I_switch(Z)
 = (2/pi) sum_(j != l) Area(v_j,v_l)
 = (4/pi) sum_(j<l) Area(v_j,v_l).                       (5.12)
```

QED.

### Interpretation

The predecessor's switch formula charged each interface by an output chord. In a zonotope, the two output states adjacent across `H_(u_j)` differ by the chord `2v_j`. The Gaussian restriction to that interface then sees only the component of every *other* generator transverse to `v_j`. After integration, the pair `(v_j,v_l)` contributes exactly its parallelogram area.

Thus switch complexity is **two-dimensional and transverse**. Parallel branch directions do not multiply complexity even if their formal sign patterns are numerous.

---

## 6. Radius plus transverse area controls the whole Gaussian width

Let

```text
R_Z := sup_(z in Z)||z||_2
     = max_(epsilon in {+1,-1}^m)
       ||sum_j epsilon_j v_j||_2.                        (6.1)
```

For almost every `g`,

```text
grad h_Z(g)
 = sum_j sign(<g,v_j>) v_j in Z,                         (6.2)
```

hence

```text
||grad h_Z(g)||_2 <= R_Z.                                (6.3)
```

### Theorem 6.1 — radius/transverse-area width bound

For the zonotope `Z`,

```text
boxed:
E h_Z(g)^2
 <= R_Z^2 + (4/pi) A_Z.                                 (6.4)
```

Consequently

```text
boxed:
E h_Z(g)
 <= [ R_Z^2 + (4/pi) A_Z ]^(1/2).                       (6.5)
```

#### Proof

Apply the Gaussian support-curvature identity (2.5) to `h_Z`. There is no smooth curvature and, by Theorem 5.1, the whole curvature term is `(4/pi)A_Z`. Equation (6.3) gives

```text
E||grad h_Z(g)||_2^2 <= R_Z^2.                           (6.6)
```

Therefore

```text
E h_Z(g)^2
 = E||grad h_Z(g)||_2^2 + (4/pi)A_Z
 <= R_Z^2+(4/pi)A_Z.                                    (6.7)
```

Jensen gives (6.5). QED.

### Sanity check against the elementary first-moment formula

Equation (3.5) says

```text
E h_Z = sqrt(2/pi) sum_j a_j.                            (6.8)
```

Theorem 6.1 is consistent with this because `R_Z` captures coherent/parallel accumulation while `A_Z` captures transverse accumulation. Two extremes make this transparent:

- if all generators are parallel, then `A_Z=0` and `R_Z=sum_j a_j`;
- if all generators are pairwise orthogonal, then `R_Z^2=sum_j a_j^2` and

  ```text
  (4/pi)A_Z
  = (4/pi) sum_(j<l) a_ja_l.
  ```

In the second case (6.7) is in fact the exact second moment formula derived below.

---

## 7. Exact weighted-cube tensor calibration

The predecessor used equal weights. The weighted case is more informative because it falsifies raw branch counting.

Fix `m>=1`, let

```text
d := 2^m,                                                (7.1)
```

and index the coordinates of `R^d` by sign vectors

```text
s=(s_1,...,s_m) in {+1,-1}^m.                           (7.2)
```

Let arbitrary weights

```text
a_1,...,a_m >=0                                         (7.3)
```

be given, and define diagonal symmetric matrices

```text
T_i := a_i diag(s_i)_(s in {+1,-1}^m).                  (7.4)
```

Then

```text
||T_i||_(I_2)=||T_i||_op=a_i,
S^2=sum_i a_i^2=||a||_2^2.                              (7.5)
```

The random sum is diagonal, with `s`-th entry

```text
sum_i a_i g_i s_i.                                      (7.6)
```

Choosing `s_i=sign(g_i)` gives the exact identity

```text
boxed:
h(g)
 = ||sum_i g_iT_i||_op
 = sum_i a_i |g_i|.                                     (7.7)
```

### Theorem 7.1 — exact weighted-cube first and second moments

For the family (7.4),

```text
boxed:
E h(g)
 = sqrt(2/pi) ||a||_1,                                  (7.8)
```

and

```text
boxed:
E h(g)^2
 = ||a||_2^2
   + (2/pi)(||a||_1^2-||a||_2^2).                       (7.9)
```

Moreover

```text
boxed:
I_switch
 = (2/pi)(||a||_1^2-||a||_2^2).                         (7.10)
```

#### Proof

Equation (7.8) follows from `E|g_i|=sqrt(2/pi)`. For the second moment,

```text
E (sum_i a_i|g_i|)^2
 = sum_i a_i^2 E g_i^2
   + 2 sum_(i<j)a_ia_j E|g_i||g_j|

 = sum_i a_i^2
   + (4/pi) sum_(i<j)a_ia_j

 = ||a||_2^2
   + (2/pi)(||a||_1^2-||a||_2^2).                       (7.11)
```

The output support body is the axis-aligned box

```text
K
 = product_(i=1)^m [-a_i,a_i]
 = sum_i [-a_i e_i,a_i e_i].                            (7.12)
```

Its generators are orthogonal, so Theorem 5.1 gives

```text
I_switch
 = (4/pi) sum_(i<j)a_ia_j
 = (2/pi)(||a||_1^2-||a||_2^2).                         (7.13)
```

QED.

### Effective switching dimension

Define

```text
m_eff(a)
 := (||a||_1/||a||_2)^2.                                (7.14)
```

Then

```text
1 <= m_eff(a) <= #{i:a_i>0},                            (7.15)
```

and (7.8) reads

```text
E h
 = sqrt(2/pi) S sqrt(m_eff(a)).                         (7.16)
```

For equal weights, `m_eff=m=log_2 d`, recovering the predecessor's sharp `sqrt(log d)` example. But if, for example,

```text
a_i = 2^(-i),                                           (7.17)
```

then `m_eff(a)=O(1)` uniformly in `m`, even though the support body still has up to `2^m=d` vertices.

This is a direct counterexample to the overstrong intermediate principle

```text
switch cost should be charged according to the raw
number of exposed branches.                             (7.18)
```

The raw branch count can grow exponentially while the actual Gaussian norm and switching curvature remain bounded. Any useful arbitrary-case adjacency theorem must be **amplitude weighted**.

---

## 8. A zonotopal-envelope theorem for tensor families

The zonotope computation is useful beyond exact zonotopal output bodies because support functions are monotone under set inclusion.

### Theorem 8.1 — one-zonotope envelope

Let `K` be the symmetrized tensor output body from (2.1). Suppose there exist vectors `v_1,...,v_m in R^n` such that

```text
K subset Z:=sum_j[-v_j,v_j].                             (8.1)
```

Then

```text
boxed:
E ||sum_i g_iT_i||_(I_p)
 <= [R_Z^2+(4/pi)A_Z]^(1/2).                            (8.2)
```

In particular, if

```text
R_Z^2 + A_Z
 <= C_(r,p) d^(1-2/p) S^2 L(d,n)^2                     (8.3)
```

for a polylogarithmic factor `L`, then

```text
boxed:
E ||sum_i g_iT_i||_(I_p)
 <= C'_(r,p) d^(1/2-1/p) S L(d,n).                      (8.4)
```

Thus the conjectured polynomial exponent holds for this class.

#### Proof

Inclusion gives

```text
h_K(g)<=h_Z(g)                                           (8.5)
```

for every `g`. Apply Jensen and Theorem 6.1:

```text
E h_K
 <= E h_Z
 <= (E h_Z^2)^(1/2)
 <= [R_Z^2+(4/pi)A_Z]^(1/2).                            (8.6)
```

Equation (8.4) follows from (8.3). QED.

### Why this class is genuinely broader than a small finite branch dictionary

A zonotope with `m` generators may have exponentially many vertices. Theorem 8.1 never pays `log(number of vertices)` explicitly. It also allows:

- arbitrary pairwise angles between generators;
- arbitrary linear dependence;
- exponentially many formal sign patterns;
- arbitrary tensor ranks and coefficient correlations behind the output body;
- continuous or highly multiply-covered parameter fibers mapping into the same zonotope.

The complexity is measured instead by the geometric energy `R_Z^2+A_Z`.

No literature-priority claim is made for generic zonotope facts. The proved campaign advance is the exact insertion of zonotopal switching geometry into the predecessor's support-curvature identity and the resulting tensor sufficient condition.

---

## 9. Tensor factorization criterion producing a zonotope envelope

The set inclusion in Theorem 8.1 has a direct tensor interpretation.

Suppose there are symmetric order-`r` tensors

```text
R_1,...,R_m                                               (9.1)
```

with

```text
||R_j||_(I_p) <= 1,                                      (9.2)
```

and coefficient vectors

```text
v_j=((v_j)_1,...,(v_j)_n) in R^n                         (9.3)
```

such that, tensorially,

```text
T_i = sum_(j=1)^m (v_j)_i R_j
for every i=1,...,n.                                     (9.4)
```

Then for every `x in B_p^d`,

```text
F(x)
 = sum_j R_j[x^r] v_j,                                   (9.5)
```

and `|R_j[x^r]|<=1`. Therefore

```text
F(B_p^d) subset sum_j[-v_j,v_j]=Z,                       (9.6)
```

and the same is true after symmetrization and convexification.

### Corollary 9.1 — zonotopal tensor factorization inequality

Every factorization (9.1)--(9.4) gives

```text
boxed:
E ||sum_i g_iT_i||_(I_p)
 <= [R_Z^2+(4/pi)A_Z]^(1/2).                            (9.7)
```

Hence define the geometric factorization quantity

```text
Gamma_Z(T_1,...,T_n)
 := inf over factorizations (9.1)--(9.4)
    [R_Z^2+(4/pi)A_Z]^(1/2).                            (9.8)
```

Then

```text
boxed:
E ||sum_i g_iT_i||_(I_p)
 <= Gamma_Z(T_1,...,T_n).                               (9.9)
```

The arbitrary Conjecture-16 target would therefore follow from the still-open comparison

```text
Gamma_Z(T_1,...,T_n)
 <= C_(r,p) polylog(d,n) d^alpha S                      (9.10)
```

or from a multiscale relaxation of it proved below.

### Coordinate factorization sanity check

Taking

```text
R_j=T_j/||T_j||_(I_p),
v_j=||T_j||_(I_p)e_j                                    (9.11)
```

for nonzero `T_j` gives the coordinate box envelope. Then

```text
R_Z=S,
A_Z=sum_(i<j)||T_i||_(I_p)||T_j||_(I_p),                 (9.12)
```

and (9.7) yields the weighted-coordinate estimate consistent with

```text
E sum_i |g_i| ||T_i||_(I_p).                             (9.13)
```

This is not sufficient in general, but it proves that the factorization quantity is always finite and makes clear what must improve: find **rotated/shared generators** that exploit correlations between the deterministic tensors rather than paying for every coefficient axis separately.

---

## 10. Multiscale zonotopal decomposition

A single global zonotope can still overestimate a curved output body. The switching calculation extends cleanly to a multiscale Minkowski envelope.

Let

```text
Z_q = sum_(j=1)^(m_q)[-v_(q,j),v_(q,j)]                 (10.1)
```

for `q=1,...,L`, and define

```text
R_q := sup_(z in Z_q)||z||_2,
A_q := sum_(j<l) Area(v_(q,j),v_(q,l)),
E_q := [R_q^2+(4/pi)A_q]^(1/2).                         (10.2)
```

### Theorem 10.1 — multiscale zonotopal envelope

If

```text
K subset Z_1+...+Z_L,                                    (10.3)
```

then

```text
boxed:
E h_K(g)
 <= sum_(q=1)^L E_q.                                    (10.4)
```

Therefore if

```text
sum_q E_q
 <= C_(r,p) d^alpha S polylog(d,n),                     (10.5)
```

then the full conjectured polynomial dimension exponent holds for that tensor family.

#### Proof

Minkowski addition adds support functions:

```text
h_(Z_1+...+Z_L)(g)=sum_q h_(Z_q)(g).                     (10.6)
```

By inclusion,

```text
h_K(g)<=sum_q h_(Z_q)(g).                               (10.7)
```

Taking expectation and applying Theorem 6.1 to each term gives

```text
E h_K
 <= sum_q E h_(Z_q)
 <= sum_q (E h_(Z_q)^2)^(1/2)
 <= sum_q E_q.                                          (10.8)
```

QED.

### Tensor form

It is enough to write

```text
T_i = sum_q sum_j (v_(q,j))_i R_(q,j),                  (10.9)
```

where each scale-`q` scalar tensor satisfies

```text
||R_(q,j)||_(I_p)<=1.                                   (10.10)
```

Then the corresponding output body is contained in the sum of the `Z_q`.

The key advantage over raw finite-branch counting is that arbitrarily many tiny or nearly parallel switch directions can be placed on a fine scale where their `E_q` contribution is small.

---

## 11. Countertests against earlier false invariants

### 11.1 Equal-weight matrix hypercube

Take `a_i=1/sqrt(m)` in Section 7. Then

```text
S=1,
m_eff=m=log_2 d,
E h=sqrt(2/pi) sqrt(log_2 d),                            (11.1)
```

and

```text
I_switch=(2/pi)(m-1).                                   (11.2)
```

The new area formula reproduces the predecessor exactly.

### 11.2 Exponentially many branches with decaying amplitudes

Take `a_i=2^(-i)` and again `d=2^m`. The support body has up to `2^m` vertices, but

```text
sum_i a_i <=1,
S^2=sum_i4^(-i)<1/3,
A_Z=sum_(i<j)a_ia_j=O(1),                               (11.3)
```

so both the Gaussian width and switching curvature remain `O(1)` as `m -> infinity`.

Therefore a theorem based on branch count, vertex count, or unweighted adjacency count is quantitatively wrong even inside the matrix case.

### 11.3 Completely parallel generators

If `v_j=a_j u` for one unit vector `u`, then

```text
A_Z=0,
Z=[-(sum a_j)u,(sum a_j)u].                             (11.4)
```

There are many formal sign choices in the Minkowski representation, but no transverse switching curvature. All complexity is coherent and is captured by `R_Z=sum a_j`.

### 11.4 Single tensor / scalar output

When `n=1`, the tensor output body is an interval. One generator suffices, so

```text
A_Z=0,
Gamma_Z<=S.                                              (11.5)
```

Thus the new criterion does not suffer from the large flattening/Frobenius overestimate that afflicts many naive matrix-reduction routes for a single high-order tensor.

### 11.5 Rotating tangent field with zero process

The earlier counterexample had a large family of normalized tangent directions on a slice where the actual process image vanished. Here `K={0}` on that slice and the empty zonotope has zero energy. Invisible tangent rotation is not charged.

### 11.6 Exponential regular fiber multiplicity

The criterion is stated entirely in output space. Multiple parameter points mapping to the same output create no extra generators or curvature cost.

### 11.7 `3^d-1` critical-point quartic and flat-sign scalar quartic

Both are scalar-output tests from earlier runs. Their symmetrized output bodies are intervals, so one generator suffices regardless of critical-point multiplicity. Again the false algebraic count disappears.

### 11.8 Dense coordinate dust

A cloud of tiny *orthogonal* switch generators has area cost proportional to the square of their total `l_1` amplitude, while a cloud of nearly parallel tiny generators is much cheaper. This distinguishes actual transverse output complexity from mere coordinate count, which was precisely the failure mode of the early product-posterior construction.

All of these tests pass. They do not establish (9.10) for arbitrary tensors.

---

## 12. Relation to the volumetric obstruction

Aden-Ali's primary theorem gives, for general subgaussian tensors, a bound involving a hierarchy of variance/Frobenius parameters. The paper explicitly notes that the higher-order terms can be much larger than matrix-Khintchine-type control and describes the underlying PAC-Bayes argument as volumetric in the regimes where those terms dominate.

The zonotopal calculation isolates a different geometric quantity:

```text
transverse switch energy
 = sum of pairwise output-generator areas.               (12.1)
```

This matters because a volumetric argument is insensitive to whether many candidate directions are:

- identical or parallel;
- tiny in amplitude;
- redundant representations of the same output displacement.

The area formula automatically removes all three overcounts.

It does **not** yet solve the arbitrary problem because a general tensor output body need not admit a short global zonotopal envelope. The new task is therefore not to bound the number of exposed branches. It is to construct a scale-dependent segment decomposition whose total radius-plus-transverse-area energy is small.

---

## 13. Connection to the earlier weighted-column decomposition

A previous P09 report proved the exact one-slot identity

```text
F(x)=sum_j x_j A_x e_j                                  (13.1)
```

and introduced the balanced mass

```text
q_x(j)
 proportional to |x_j| ||A_xe_j||_2.                    (13.2)
```

It also showed that directions with pathological normalization can have zero `q_x` mass, so unweighted unions of tangent directions are the wrong object.

The present theorem suggests a stronger use of that decomposition. At a fixed scale, treat the significant weighted output columns

```text
x_j A_xe_j                                               (13.3)
```

as candidate segment generators. If these vectors can be clustered into a scale-dependent family `v_(q,j)` so that

```text
1. the residual output error is below the current chaining scale;
2. sum_q [R_q^2+(4/pi)A_q]^(1/2)
   <= C_(r,p) d^alpha S polylog(d,n),                    (13.4)
```

then Theorem 10.1 gives the source target.

Unlike the earlier attempt to cover all normalized tangent columns, (13.4) is amplitude-sensitive and correlation-sensitive:

- zero-mass columns disappear;
- nearly parallel columns cost almost no area;
- small columns can be deferred to a finer scale.

This is a concrete route from the existing balanced-column machinery to the arbitrary tensor problem.

---

## 14. A sharper local target: transverse-area sparsification

The immediate missing lemma can now be stated without reference to branch counts.

### Target 14.1 — scale-`k` transverse-area sparsification

Let

```text
eps_k := C_r d^alpha S/sqrt(k).                         (14.1)
```

Seek a decomposition of the tensor output body at scale `k` of the form

```text
K subset K_res(k) + Z_k,                                (14.2)
```

where

```text
E h_(K_res(k))(g) <= C eps_k                             (14.3)
```

and `Z_k` is a zonotope satisfying

```text
R_(Z_k)^2 + A_(Z_k)
 <= C_(r,p) d^(2alpha) S^2 polylog(d,n)^2.              (14.4)
```

A dyadic refinement with residuals telescoping across `k` would then feed Theorem 10.1.

The critical point is that (14.4) allows many generators. It forbids only too much **transverse area at significant amplitude**.

### Why a naive global version may still fail

A generic curved body can require an enormous zonotope for small Hausdorff error, and a global segment envelope may reintroduce the ambient volumetric loss. Therefore the decomposition must be scale-dependent and process-adapted. The balanced-column mass and active covariance truncations from earlier reports provide two candidate ways to choose generators without covering the entire parameter sphere.

---

## 15. Old theorem, new theorem, remaining gap

| Item | Before this run | After this run |
|---|---|---|
| Full arbitrary `2<=p<2r` exponent | `1/2-1/(2r)` | unchanged; conjecture still open |
| Switching density | exact output chord on each branch interface | exact integrated formula for every zonotope |
| Polyhedral complexity measure | finite branch count / global aggregation bound | radius plus pairwise transverse-generator area |
| Equal matrix cube | `sqrt(log d)` lower bound | generalized to arbitrary weights with exact `m_eff` |
| Raw branch-count heuristic | known to be suspicious | explicitly refuted by exponentially many decaying-amplitude branches |
| New restricted class | finite/piecewise regular image decompositions | zonotopal and multiscale-zonotopal output envelopes |
| Tensor criterion | image-piece count | explicit bounded-tensor factorization into segment generators |
| Current arbitrary bottleneck | scale-sensitive switching-chord estimate | transverse-area sparsification of weighted process-significant columns |

The headline exponent is intentionally unchanged. The advance is that the polyhedral switching problem is now solved exactly for an exponentially rich family and yields a concrete amplitude- and angle-sensitive factorization target.

---

## 16. Next concrete attack

The next run should not return to counting all tangent frames or all exposed branches. It should attack Target 14.1 directly.

### Step A — dyadic balanced-column layers

For each `x`, split the exact weighted columns `x_jA_xe_j` into dyadic classes by their balanced mass from (13.2). Earlier reciprocity estimates imply that layers requiring large normalization have correspondingly small mass. Convert each significant layer into a candidate segment family.

### Step B — area rather than cardinality

For one layer, estimate

```text
sum_(a<b) Area(v_a,v_b)                                 (16.1)
```

through its Gram matrix. Since

```text
Area(v_a,v_b)^2
 = ||v_a||^2||v_b||^2-<v_a,v_b>^2,                     (16.2)
```

small area is equivalent to near rank-one behavior of the local generator Gram family. A large-area branch should therefore force a genuinely multi-directional lower-order contraction, which is exactly the kind of certificate that can be handed to the established structured P09 branches.

### Step C — rank-one-versus-area dichotomy

Attempt to prove at each dyadic layer:

```text
either
  A_layer <= C d^(2alpha) S^2 polylog(d,n)^2,
or
  there exists a lower-order contraction with
  source-normalized energy above the current threshold. (16.3)
```

The second branch would give a recursive/decoupling route instead of an entropy failure.

### Step D — mandatory falsification tests

Any proposed layer lemma must be checked on:

1. equal-weight matrix cube;
2. decaying-weight matrix cube;
3. parallel-generator zonotope;
4. scalar one-tensor case;
5. zero-process rotating-tangent example;
6. dense coordinate dust;
7. flat-sign quartic;
8. exponential-fiber and `3^d-1` critical-point examples.

The equal cube must pay `Theta(log d)` switching energy; the decaying cube must *not* pay for its `2^m` branch count; parallel generators must have zero transverse-area cost.

### Step E — extension from `p=2` to `p>2`

Once the area sparsification is proved at `p=2`, the natural source factor for `p>2` is `d^alpha`. The earlier self-normalized KKT identity suggests replacing ambient `d^alpha` by the maximizer's effective support where possible, but no such improvement is needed for the source conjecture itself.

A successful proof of (16.3) with summable dyadic losses would give a direct route from weighted tangent columns to a multiscale zonotopal envelope and therefore to the desired polynomial exponent.

---

## 17. Claim discipline

- **PROVED PARTIAL:** Lemma 4.1 and Theorems 5.1, 6.1, 7.1, 8.1 and 10.1 are proved under their stated assumptions.
- **PROVED PARTIAL:** For any zonotope, the entire Gaussian singular switching-curvature budget is exactly `(4/pi)` times the sum of pairwise generator parallelogram areas.
- **PROVED PARTIAL:** The weighted matrix cube has exact effective switching dimension `m_eff=(||a||_1/||a||_2)^2`; raw branch count is not the correct complexity measure.
- **PROVED PARTIAL:** Tensor families admitting a one-scale or multiscale zonotopal envelope with controlled radius-plus-area energy satisfy the desired Conjecture-16 polynomial exponent.
- **CONDITIONAL/NEXT TARGET:** The scale-dependent transverse-area sparsification of arbitrary tensor outputs is not proved.
- **NOT CLAIMED:** No arbitrary deterministic `2<=p<2r` solution is claimed.
- **NOT CLAIMED:** No literature novelty priority is claimed for general support functions, zonotopes, Minkowski addition, or elementary Gaussian facts. The campaign contribution is their exact integration with the P09 switching-curvature reduction and the resulting source-normalized factorization target.
- **PRESERVATION:** This is a new immutable report. It does not overwrite C0035 history, prior P09 reports, or peer-owned material.
