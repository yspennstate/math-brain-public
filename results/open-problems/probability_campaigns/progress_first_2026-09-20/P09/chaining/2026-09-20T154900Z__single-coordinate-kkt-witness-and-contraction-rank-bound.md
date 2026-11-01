Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime does not expose authenticated GPT-6/maximum-effort attestation.

# P09 progress-first run — a single-coordinate KKT witness, lower-order critical-atom chaining, and a contraction-rank theorem

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic symmetric tensors. In the unresolved regime `2 <= p < 2r`, the fixed full-source metric remains

```text
old arbitrary exponent = 1/2 - 1/(2r),
new arbitrary exponent = 1/2 - 1/(2r),
target exponent        = 1/2 - 1/p.
```

The substantive change in this run is a new one-coordinate reduction. The preceding report showed that every Gaussian maximizer selects a locally cheap coordinate-tangent zonotope, but selection among many local zonotopes remained the obstruction. Here that entire local body is replaced by **one coordinate contraction**.

For every Gaussian direction `g` and every maximizing `x`, there is a coordinate `j` such that the KKT-rescaled one-slot contraction

```text
a_(x,j)
 := sgn(x_j) |x_j|^(1-p) A_x e_j
```

simultaneously satisfies

```text
<sigma g, a_(x,j)> = h(g)
```

and

```text
||a_(x,j)||_2 <= kappa_r d^(1/2-1/p) S.
```

The polynomial dimension factor is **exactly the conjectured one**. The proof is a two-line ratio argument combining the inherited Hilbert--Schmidt tangent bound with the sharp finite-dimensional comparison between `l_p` and `l_(2p-2)`.

This yields a lower-order chaining reduction: the original degree-`r` support process is pointwise dominated by a union of `d` source-normalized **critical atom classes**, each built from an order-`r-1` coordinate contraction. Selection among the `d` coordinates costs only a `sqrt(log d)` factor, which is admissible in Conjecture 16 and is unavoidable already in the matrix case.

As an unconditional application, if the output span of every one-coordinate `(r-1)`-contraction has dimension at most `m`, then

```text
E ||sum_i g_i T_i||_(I_p)
 <= kappa_r d^(1/2-1/p) S
    ( sqrt(m) + sqrt(2 log d) ).
```

Thus the desired polynomial exponent is proved for a genuinely broader **low coordinate-contraction-rank class** whenever `m` is polylogarithmic. The coordinate contraction subspaces may be different, need not commute, need not share a frame, and directions inside each subspace may vary continuously.

A new counterexample calibration is also proved. Orthogonally conjugating the matrix hypercube makes **every maximizing vector flat in the ambient coordinate basis**, so all KKT mass profiles are identical (`|x_j|^2=1/d`) and every selected local zonotope is a single segment, yet the Gaussian norm is still `Theta(sqrt(log d))`. The same construction is homogenized to every fixed tensor order at `p=2`. Therefore KKT masses alone cannot control selection; the missing information is directional complexity of the lower-order contraction atoms. The contraction-rank theorem captures exactly that complexity in this example and is sharp up to constants/log conventions.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Registered role: `chaining / geometric-probabilistic proof`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Pre-write master observed: `fc93db24c0b7bf0e669ddedfaeba2c3b93ae8799`.
- Immediate predecessor: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T144800Z__kkt-local-zonotope-dictionary-and-all-order-log-lower-bound.md`.
- Historical C0035 material, prior P09 reports, and peer files are preserved. This report is additive and immutable.

---

## 1. Exact source target and bounded current-source check

Primary source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizić-Nikolac, A. Rödder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.

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

Set

```text
alpha := 1/2 - 1/p,
S^2   := sum_i ||T_i||_(I_p)^2.                           (1.2)
```

The source itself, in the August 24, 2026 manuscript rendering, states that the BGJLR geometric covering method settles the desired polynomial dependence for `p >= 2r` and that a volumetric barrier prevents the same argument for `p < 2r`. It separately records the matrix, independent-entry, rank-one, Hankel, and other structured cases.

A bounded current check on 20 September 2026 again recovered:

1. `arXiv:2603.29571`, still presenting Conjecture 16 as the target;
2. Bandeira--Gopi--Jiang--Lucca--Rothvoss, `arXiv:2411.10633`, as the primary geometric/covering baseline for correlated random tensors;
3. Ishaq Aden-Ali, `arXiv:2503.10580`, as the PAC-Bayesian improvement of that general bound;
4. Dartois--McKenna, `arXiv:2603.01342`, as a newer moment-based method for structured random-tensor models, not a proof of the universal arbitrary deterministic correlated-summand statement (1.1).

No full resolution of the exact arbitrary deterministic `2 <= p < 2r` statement was found in that bounded check. This is not a claim about unpublished or unindexed work.

---

## 2. Inherited tangent normalization

Let `\widetilde T_i` be the symmetric `r`-linear form associated with the diagonal polynomial `x -> <T_i,x^(tensor r)>`. Fix a real polarization constant `kappa_r` such that

```text
|\widetilde T_i(x_1,...,x_r)|
 <= kappa_r ||T_i||_(I_p) prod_(a=1)^r ||x_a||_p.         (2.1)
```

Only dependence on the fixed tensor order `r` matters here.

Define

```text
F(x) := ( \widetilde T_i(x,...,x) )_(i=1)^n in R^n       (2.2)
```

and

```text
A_x v
 := ( \widetilde T_i(x,...,x,v) )_(i=1)^n,              (2.3)
```

with `r-1` copies of `x` in `A_x`. Then

```text
F(x)=A_x x,
DF(x)[v]=r A_x v.                                        (2.4)
```

The predecessor established the source-normalized tangent Hilbert--Schmidt estimate

```text
boxed:
||A_x||_(HS) <= kappa_r S
for every ||x||_p<=1.                                    (2.5)
```

For completeness, if `a_i(x)` denotes the `i`-th row of `A_x` and `q=p/(p-1)<=2`, then

```text
||a_i(x)||_q
 = sup_(||v||_p<=1)|\widetilde T_i(x^(r-1),v)|
 <= kappa_r ||T_i||_(I_p),                               (2.6)
```

hence `||a_i(x)||_2<=||a_i(x)||_q`, and summing squared row norms yields (2.5).

This is the only inherited analytic estimate needed for the new witness theorem.

---

## 3. KKT identity at a Gaussian maximizer

For `g in R^n`, write

```text
P_g(x):=<g,F(x)>,                                        (3.1)

h(g)
 := sup_(||x||_p<=1)|P_g(x)|
  = ||sum_i g_i T_i||_(I_p).                             (3.2)
```

If `h(g)=0`, all claims below are trivial. Otherwise choose `sigma in {+1,-1}` and a maximizer `x=x(g)` with

```text
||x||_p=1,
sigma P_g(x)=h(g).                                       (3.3)
```

Because `p>=2`, the `l_p` sphere is differentiable. Applying the Lagrange multiplier rule to `sigma P_g` under the constraint `sum_j|x_j|^p=1` gives

```text
r sigma A_x^* g
 = lambda p ( |x_j|^(p-2)x_j )_(j=1)^d.                 (3.4)
```

Pairing with `x` and using `A_x x=F(x)` yields

```text
r h(g)=lambda p.                                         (3.5)
```

Therefore the factors cancel and one obtains the exact coordinatewise identity

```text
boxed:
sigma <g,A_x e_j>
 = h(g)|x_j|^(p-2)x_j.                                   (3.6)
```

For every nonzero coordinate define the KKT-rescaled one-slot atom

```text
a_(x,j)
 := sgn(x_j)|x_j|^(1-p) A_x e_j.                         (3.7)
```

Then (3.6) immediately gives

```text
boxed:
<sigma g,a_(x,j)> = h(g)
for every j with x_j !=0.                                (3.8)
```

Thus **every nonzero coordinate atom lies on exactly the same supporting hyperplane**. The only issue is that the norm in (3.7) can a priori blow up when `x_j` is small. The next theorem removes precisely that problem at the conjectured dimension scale.

---

## 4. Main new lemma: a single well-conditioned coordinate always exists

Let

```text
c_j := ||A_x e_j||_2,
b_j := |x_j|^(p-1).                                      (4.1)
```

For `x_j !=0`,

```text
||a_(x,j)||_2 = c_j/b_j.                                 (4.2)
```

The numerator has an `l_2` square-function bound by (2.5). The denominator has exactly the right finite-dimensional lower bound.

### Lemma 4.1 — sharp denominator lower bound

For every `x in R^d` with `||x||_p=1` and `p>=2`,

```text
boxed:
( sum_j |x_j|^(2p-2) )^(1/2)
 >= d^(-alpha),
alpha=1/2-1/p.                                           (4.3)
```

#### Proof

Set `s=2p-2>=p`. The standard finite-dimensional norm comparison gives

```text
||x||_s
 >= d^(1/s-1/p)||x||_p
 = d^(1/(2p-2)-1/p).                                     (4.4)
```

Now

```text
( sum_j |x_j|^(2p-2) )^(1/2)
 = ||x||_(2p-2)^(p-1).                                  (4.5)
```

Multiplying the exponent in (4.4) by `p-1` gives

```text
(p-1)(1/(2p-2)-1/p)
 = 1/2-(p-1)/p
 = 1/p-1/2
 = -alpha.                                               (4.6)
```

This proves (4.3). QED.

The bound is sharp in its `d` exponent for the flat vector `|x_j|=d^(-1/p)`.

### Theorem 4.2 — single-coordinate KKT witness at the conjectured polynomial scale

Let `g`, `x=x(g)`, `sigma`, and `h(g)` be as above. Then there exists a coordinate `j` with `x_j !=0` such that

```text
boxed:
<sigma g,a_(x,j)> = h(g)                                 (4.7)
```

and

```text
boxed:
||a_(x,j)||_2
 <= kappa_r d^alpha S.                                   (4.8)
```

#### Proof

By the elementary ratio inequality,

```text
min_(j:b_j>0) c_j/b_j
 <= (sum_j c_j^2)^(1/2)/(sum_j b_j^2)^(1/2).             (4.9)
```

Indeed, if every ratio were larger than the right side, squaring and summing `c_j^2 > R^2 b_j^2` would contradict the definition of `R`.

The numerator is

```text
(sum_j c_j^2)^(1/2)=||A_x||_(HS)<=kappa_r S.             (4.10)
```

By Lemma 4.1 the denominator is at least `d^(-alpha)`. Hence

```text
min_(j:x_j!=0)||a_(x,j)||_2
 <= kappa_r d^alpha S.                                   (4.11)
```

Choose a minimizing coordinate. Equation (4.7) is then the KKT identity (3.8). QED.

### Why this matters

The factor `d^alpha` in (4.8) is exactly

```text
d^(1/2-1/p),                                             (4.12)
```

not the inherited low-`p` volumetric factor `d^(1/2-1/(2r))`. Therefore **the pointwise KKT reduction itself has no polynomial gap**. The remaining issue is entropy/width of the family of possible well-conditioned coordinate atoms.

At `p=2`, `alpha=0`, so every Gaussian maximizer has a coordinate atom of norm `O_r(S)` which exactly exposes the full norm.

---

## 5. New critical-atom chaining reduction

Set the critical radius

```text
R_* := kappa_r d^alpha S.                                (5.1)
```

For each coordinate `j`, define the source-normalized critical atom class

```text
C_j
 := {
      sgn(x_j)|x_j|^(1-p) A_x e_j :
      ||x||_p=1,
      x_j !=0,
      ||sgn(x_j)|x_j|^(1-p) A_x e_j||_2 <= R_*
    }.                                                    (5.2)
```

This set is defined entirely from the deterministic tensor family; it does not depend on `g`.

### Theorem 5.1 — pointwise one-coordinate domination

For every `g in R^n`,

```text
boxed:
h(g)
 <= max_(1<=j<=d) sup_(a in C_j) |<g,a>|.                (5.3)
```

#### Proof

If `h(g)=0`, trivial. Otherwise take a maximizing `x`. Theorem 4.2 supplies a coordinate `j` for which `a_(x,j) in C_j` and

```text
|<g,a_(x,j)>|=h(g).                                      (5.4)
```

Therefore the right-hand side of (5.3) is at least `h(g)`. QED.

This reduction is materially smaller than covering all tangent maps `A_x`, all local zonotopes `Z_x`, or all top singular frames. It asks only for the Gaussian complexity of `d` classes of **one-column, one-lower-degree contractions**, with the singular normalization automatically truncated at the source-valid radius `R_*`.

For each `j`, define

```text
W_j
 := E sup_(a in C_j)|<g,a>|.                             (5.5)
```

The function

```text
Z_j(g):=sup_(a in C_j)|<g,a>|                            (5.6)
```

is `R_*`-Lipschitz because every atom in `C_j` has Euclidean norm at most `R_*`. Gaussian concentration and the usual maximal inequality therefore imply

```text
E max_j Z_j(g)
 <= max_j E Z_j(g) + R_* sqrt(2 log d).                  (5.7)
```

Combining (5.3) and (5.7) gives the central reduction:

### Theorem 5.2 — one-coordinate chaining inequality

```text
boxed:
E ||sum_i g_i T_i||_(I_p)
 <= max_j W_j
    + kappa_r d^alpha S sqrt(2 log d).                   (5.8)
```

Thus the **entire coordinate-selection cost is already admissible** for Conjecture 16. The arbitrary problem is reduced to proving, for each fixed coordinate,

```text
W_j
 <= C(r,p) d^alpha S polylog(d,n).                       (5.9)
```

No union over exponentially many local models is needed at this stage.

### Dudley form

Let `N(C_j,epsilon)` denote Euclidean covering numbers of the symmetrized atom class `C_j union (-C_j)`. Standard Gaussian chaining yields

```text
W_j
 <= C int_0^(R_*) sqrt(log N(C_j,epsilon)) d epsilon.    (5.10)
```

Consequently a full-source proof would follow from a scale-sensitive entropy bound for the **single-coordinate rational contraction map**

```text
x -> |x_j|^(1-p) A_x e_j                                (5.11)
```

inside the norm-truncated region `||.|_2<=R_*`.

This is the new concrete volumetric target.

---

## 6. Algebraic meaning: the order drops by one

For each coordinate `j`, define the linear map

```text
Phi_j : Sym^(r-1)(R^d) -> R^n                            (6.1)
```

by

```text
Phi_j(z)_(i)
 := \widetilde T_i(z,e_j).                               (6.2)
```

Then

```text
A_x e_j = Phi_j(x^(tensor(r-1))).                        (6.3)
```

Therefore the atom class `C_j` consists of a scalar rescaling of an **order-`r-1` polynomial image**:

```text
C_j subset {
  sgn(x_j)|x_j|^(1-p)
  Phi_j(x^(tensor(r-1)))
  : ||x||_p=1,
    ||.||_2<=R_*
}.                                                        (6.4)
```

The denominator in (6.4) is singular near `x_j=0`, but Theorem 4.2 shows that one never needs to leave the radius-truncated region. This is substantially more favorable than the earlier full tangent entropy target, where right-singular rotations could create exponentially many irrelevant directions.

The new natural program is therefore an **induction/decoupling on tensor order inside a fixed coordinate patch**, with the norm cutoff preventing the small-coordinate singularity from producing a polynomial loss larger than `d^alpha`.

---

## 7. Unconditional broader class: low coordinate-contraction rank

The lower-order map `Phi_j` has a fixed output subspace

```text
E_j := range(Phi_j)
     = span { A_x e_j : x in R^d } subset R^n.           (7.1)
```

Define the coordinate-contraction rank parameter

```text
m_* := max_(1<=j<=d) dim(E_j).                           (7.2)
```

Because scalar rescaling does not change the containing subspace,

```text
C_j subset E_j intersect R_* B_2^n.                     (7.3)
```

For a Gaussian vector `g`,

```text
sup_(a in C_j)|<g,a>|
 <= R_* ||P_(E_j) g||_2.                                 (7.4)
```

Taking expectation gives

```text
W_j <= R_* E||P_(E_j)g||_2
     <= R_* sqrt(dim E_j)
     <= R_* sqrt(m_*).                                   (7.5)
```

Insert this into Theorem 5.2.

### Theorem 7.1 — coordinate-contraction-rank tensor concentration

For every symmetric deterministic order-`r` tensor family and every `p>=2`,

```text
boxed:
E ||sum_i g_i T_i||_(I_p)
 <= kappa_r d^(1/2-1/p) S
    ( sqrt(m_*) + sqrt(2 log d) ).                       (7.6)
```

In particular, if

```text
m_* <= polylog(d,n)^2,                                   (7.7)
```

then the family satisfies the polynomial dimension dependence predicted by Conjecture 16, with only polylogarithmic losses.

### Structural scope

This theorem does **not** require:

- independent tensor entries;
- rank-one summands;
- a common output eigenframe;
- commuting tangent covariances;
- a block-direct-sum decomposition;
- a fixed local zonotope;
- finitely many tangent directions.

Each coordinate `j` may have its own output subspace `E_j`, and the directions `A_xe_j` may rotate continuously inside that subspace as `x` varies. Only the dimension of each one-coordinate contraction span is controlled.

This is therefore a genuinely broader covariance/algebraic class than the earlier common-frame criteria, although it is of course still a restriction and is not claimed to be new in the literature.

### More refined union-of-subspaces form

The same proof shows a slightly more flexible statement. Suppose that for every `x` on the `l_p` sphere there exists a coordinate `j=j(x)` such that

```text
||a_(x,j)||_2<=R_*                                      (7.8)
```

and `a_(x,j)` belongs to one of `M` fixed subspaces of dimension at most `m`. Then

```text
E h(g)
 <= R_* ( sqrt(m) + sqrt(2 log M) ).                     (7.9)
```

Theorem 7.1 is the automatic special case `M=d`, using `E_1,...,E_d`.

---

## 8. Countertest: KKT mass profiles alone are blind to the required log factor

The preceding report proposed exploiting the exact KKT masses `|x_j|^p` to organize the local-zonotope dictionary. That information is useful, but it is not sufficient by itself. The following example makes this failure exact.

### 8.1 Orthogonally conjugated matrix hypercube

Let

```text
d=2^m.                                                   (8.1)
```

Index `d` labels by sign vectors

```text
s in {+1,-1}^m.                                         (8.2)
```

Let `H` be a normalized Walsh--Hadamard matrix of size `d x d`, so every column `h_s` satisfies

```text
||h_s||_2=1,
|(h_s)_j|=d^(-1/2) for every coordinate j.               (8.3)
```

For `i=1,...,m`, let `D_i` be diagonal in the `s`-basis with

```text
(D_i)_(s,s)=s_i/sqrt(m),                                 (8.4)
```

and define symmetric matrices

```text
M_i := H D_i H^T.                                        (8.5)
```

Then

```text
||M_i||_(op)=1/sqrt(m),
S^2=sum_i||M_i||_(op)^2=1.                               (8.6)
```

For Gaussian `g in R^m`,

```text
sum_i g_i M_i
 = H diag( <g,s>/sqrt(m) )_s H^T.                        (8.7)
```

Therefore

```text
boxed:
||sum_i g_i M_i||_(op)
 = (1/sqrt(m)) max_s |<g,s>|
 = (1/sqrt(m)) sum_i |g_i|.                              (8.8)
```

Hence

```text
boxed:
E ||sum_i g_i M_i||_(op)
 = sqrt(2/pi) sqrt(m)
 = sqrt(2/(pi log 2)) sqrt(log d).                       (8.9)
```

This is the familiar sharp logarithmic obstruction, but now expressed in a basis deliberately chosen to make the KKT coordinates completely flat.

For a generic `g`, choose

```text
s_*(g)_i=sgn(g_i).                                       (8.10)
```

A maximizing eigenvector is

```text
x=h_(s_*).                                               (8.11)
```

By (8.3),

```text
boxed:
|x_j|^2=1/d
for every j.                                             (8.12)
```

Thus **every branch has exactly the same KKT mass profile**. There is only one dyadic mass layer.

### 8.2 Every selected local zonotope is a segment

For `r=p=2`,

```text
(A_x e_j)_i = e_j^T M_i x.                               (8.13)
```

Since `x=h_s` is an eigenvector of every `M_i` with eigenvalue `s_i/sqrt(m)`,

```text
A_x e_j
 = x_j s/sqrt(m).                                        (8.14)
```

The canonical local-zonotope generator is

```text
v_j=x_j A_xe_j
    = x_j^2 s/sqrt(m)
    = (1/d) s/sqrt(m).                                   (8.15)
```

All `d` generators are parallel. Therefore

```text
boxed:
Z_x=[-s/sqrt(m), s/sqrt(m)]                              (8.16)
```

and its transverse-area energy is exactly zero.

The KKT-rescaled atom is even simpler:

```text
a_(x,j)=A_xe_j/x_j=s/sqrt(m)                             (8.17)
```

for every coordinate `j`.

Thus all of the following data are branch-independent:

- the KKT masses (`1/d` each);
- the generator lengths;
- the local radius (`1`);
- the fact that the local model is one-dimensional;
- the transverse-area energy (`0`).

The only changing datum is the **output direction** `s/sqrt(m)`, and there are `d=2^m` such directions. Their Gaussian width is exactly the `Theta(sqrt(log d))` term in (8.9).

This disproves any proposed intermediate lemma that attempts to bound the full process from KKT mass profiles and local scalar budgets alone while ignoring contraction directions.

---

## 9. The countertest persists for every fixed tensor order at p=2

The predecessor homogenized the matrix lower bound to all tensor orders. Here the same homogenization is recorded with the additional observation that the maximizing KKT mass profile remains branch-independent and the selected contraction directions remain the sign-code directions.

### 9.1 Even orders

Let

```text
r=2+2q.                                                   (9.1)
```

For each matrix `M_i` above define the homogeneous polynomial

```text
P_i^(r)(x)
 := (x^T M_i x)(x^T x)^q.                                (9.2)
```

On the Euclidean unit sphere,

```text
P_i^(r)(x)=x^T M_i x,                                    (9.3)
```

so

```text
||T_i^(r)||_(I_2)=||M_i||_(op)=1/sqrt(m),                (9.4)
```

and the Gaussian tensor norm is still exactly (8.8).

The maximizing vectors are the same flat Hadamard columns `h_s`, so the KKT masses are again `1/d`.

To see what happens to the one-slot contraction, differentiate (9.2). At a unit common eigenvector `x=h_s`, where `M_i x=(s_i/sqrt(m))x`,

```text
D P_i^(r)(x)[e_j]
 = 2(M_i x)_j + 2q(x^TM_i x)x_j
 = (2+2q)(s_i/sqrt(m))x_j
 = r (s_i/sqrt(m))x_j.                                  (9.5)
```

Since `DP_i^(r)(x)[e_j]=r(A_xe_j)_i`,

```text
A_xe_j=x_j s/sqrt(m),                                    (9.6)
```

exactly as in the matrix case. Hence

```text
a_(x,j)=s/sqrt(m)                                        (9.7)
```

for every coordinate. The flat-profile/directional-selection obstruction therefore survives unchanged for every even order.

### 9.2 Odd orders

Let

```text
r=3+2q                                                    (9.8)
```

and add one coordinate `t`, writing points as `(t,y) in R^(d+1)`. Define

```text
Q_i^(r)(t,y)
 := (3 sqrt(3)/2)
    t (y^T M_i y) (t^2+||y||_2^2)^q.                    (9.9)
```

On the Euclidean unit sphere,

```text
|Q_i^(r)(t,y)|
 <= (3sqrt(3)/2)|t|(1-t^2)||M_i||_(op).                  (9.10)
```

The scalar factor has maximum one at

```text
|t|=1/sqrt(3),
||y||_2=sqrt(2/3).                                       (9.11)
```

Thus

```text
||T_i^(r)||_(I_2)=||M_i||_(op)=1/sqrt(m),                (9.12)
```

and the Gaussian tensor norm is again (8.8).

At a maximizing branch one may take

```text
t^2=1/3,
y=sqrt(2/3) h_s.                                        (9.13)
```

Hence the KKT mass profile is

```text
boxed:
|t|^2=1/3,
|y_j|^2=2/(3d) for every j,                              (9.14)
```

again independent of the selected sign branch `s`.

Moreover every coordinate derivative at such a common eigenvector is a scalar multiple, independent of `i` except through `s_i`, of the output vector `s/sqrt(m)`. Thus the selected local tangent generators and the KKT-rescaled atoms again lie on the sign-code direction. The local model remains one-dimensional while the branch-selection width remains `Theta(sqrt(log d))`.

Therefore the statement

```text
"identical KKT mass profile + one-dimensional local models"
```

does **not** imply a dimension-free Gaussian type-2 bound, for any fixed tensor order.

---

## 10. Sharpness of the contraction-rank theorem on the flat hypercube

For the matrix construction, fix any ambient coordinate `j`. Equation (8.14) shows that as the maximizing branch `s` varies,

```text
a_(h_s,j)=s/sqrt(m).                                     (10.1)
```

The sign vectors span all of `R^m`. Therefore the coordinate contraction space satisfies

```text
dim(E_j)=m=log_2 d.                                      (10.2)
```

Theorem 7.1 gives

```text
E h(g)
 <= C S ( sqrt(log d) + sqrt(log d) )                    (10.3)
```

at `p=2`, which matches (8.9) up to constants.

For the even-order homogenizations the same identity (9.6) holds at the maximizing branches, so the same lower bound on the coordinate contraction rank persists. For odd orders the `y`-coordinate contraction spaces likewise contain all sign-code directions.

Thus the new parameter `m_*` is not merely an artifact of the proof: on a canonical example where the logarithmic loss is genuinely necessary, `sqrt(m_*)` has exactly the correct magnitude.

---

## 11. What failed, what changed, and the new volumetric obstruction

### Failed stronger idea from the predecessor

The predecessor's next plan was to exploit the KKT masses `|x_j|^p` to defer low-mass coordinate distinctions to fine scales. That remains potentially useful, but a **mass-only** version is false. The conjugated hypercube has identical masses on every maximizing branch, yet branch directions still contribute the full unavoidable logarithmic cost.

### What is now removed

The following sources of overcounting are no longer part of the immediate target:

1. covering the whole tangent map `A_x`;
2. covering right-singular rotations invisible to the output;
3. covering every generator of a local zonotope;
4. paying for all local transverse-area configurations;
5. enumerating arbitrary KKT mass profiles across coordinates.

A single well-conditioned coordinate atom suffices pointwise.

### New precise obstruction

For a fixed coordinate `j`, control

```text
C_j
 = {
   |x_j|^(1-p) A_xe_j
   inside the norm cutoff R_*
   }                                                       (11.1)
```

in Gaussian width / Euclidean entropy.

The map `x -> A_xe_j` has degree `r-1`, one lower than the original process. The singular denominator is explicit. The norm cutoff

```text
|| |x_j|^(1-p)A_xe_j ||_2
 <= kappa_r d^alpha S                                    (11.2)
```

is forced by Theorem 4.2 and should be used before any volumetric estimate.

A naive cover of the entire `l_p` sphere inside one coordinate class would still have exponential-in-`d` entropy and would simply recreate the old barrier. The next theorem must use the lower degree plus the cutoff to obtain a scale-sensitive estimate that is smaller than ambient volume.

---

## 12. Next concrete attack

The next run should work on **one fixed coordinate class**, not return to a global tangent cover.

Fix `j`. Split the sphere into dyadic coordinate bands

```text
2^(-(q+1)) < |x_j|^p <= 2^(-q).                          (12.1)
```

On band `q`, the rescaling in (11.1) is within a fixed factor of

```text
2^(q(1-1/p)),                                            (12.2)
```

while `A_xe_j=Phi_j(x^(tensor(r-1)))` is an order-`r-1` polynomial image. The norm cutoff (11.2) deletes the parts of the band where that scalar blowup actually creates a large output vector.

The target is a bandwise entropy estimate of the schematic form

```text
int sqrt(log N(C_(j,q),epsilon)) d epsilon
 <= C(r,p) d^alpha S polylog(d,n),                       (12.3)
```

with a summable or maximal aggregation over `q`.

Two routes are now concrete:

1. **order-reduction / decoupling:** decouple one of the remaining `r-1` copies of `x` inside `Phi_j` and use the radius cutoff before covering the other variables;
2. **covariance-rank interpolation:** replace the crude fixed rank `m_*` in Theorem 7.1 by a scale-dependent effective rank of `Phi_j` (e.g. Schatten/eigenvalue truncation), so only singular directions above the current entropy scale are counted.

Mandatory countertests before accepting a proposed lemma:

- the orthogonally conjugated flat hypercube in Section 8;
- its even/odd all-order homogenizations in Section 9;
- the earlier zero-process rotating-column example, which should be discarded automatically by the KKT exposure requirement;
- the dense-dust example, which tests whether many low-amplitude contraction directions are incorrectly counted at coarse scales;
- the previous global-Haar-sketch counterexample, which tests whether a shared auxiliary randomization manufactures entropy not present in `C_j`.

The desired end product of the next attack is either a genuine entropy improvement for one fixed `C_j`, or a counterexample showing that even the single-coordinate class can have full ambient volumetric entropy at the critical radius. Either outcome would materially sharpen the arbitrary problem.

---

## 13. Obligation ledger

### Full-source metric

```text
Conjecture 16 for arbitrary deterministic tensors, 2<=p<2r:
OPEN.

Best general polynomial exponent recovered here:
1/2 - 1/(2r).

Target exponent:
1/2 - 1/p.
```

### New proved items this run

1. **PROVED:** sharp `l_(2p-2)` denominator lower bound `>=d^(-alpha)`.
2. **PROVED:** for every Gaussian maximizer, one KKT-rescaled coordinate atom has norm at most `kappa_r d^alpha S` and exposes the full support value exactly.
3. **PROVED:** one-coordinate critical-atom chaining inequality (5.8); selection over all `d` coordinates costs only `sqrt(log d)`.
4. **PROVED:** low coordinate-contraction-rank theorem (7.6), giving the conjectured polynomial exponent for `m_*=polylog^2`.
5. **PROVED COUNTEREXAMPLE/CALIBRATION:** KKT mass profiles alone do not control selection; an orthogonally conjugated hypercube has identical flat mass profiles and one-dimensional local models but still costs `Theta(sqrt(log d))`.
6. **PROVED:** the flat-profile obstruction persists under the previous even/odd homogenizations to every fixed order at `p=2`.
7. **PROVED CALIBRATION:** on the flat hypercube, `m_*=Theta(log d)`, so the new contraction-rank theorem has the correct logarithmic order.

### Remaining gap

Prove a source-normalized entropy/width bound for each fixed-coordinate lower-order rational contraction class `C_j` without assuming small output rank. The denominator `|x_j|^(1-p)` must be handled together with the radius cutoff; covering the whole parameter sphere first will reproduce the old volumetric loss.

### Next attack

Dyadic fixed-coordinate bands + scale-dependent effective rank / one-slot decoupling for `Phi_j`, with the flat hypercube as the mandatory sharpness test.

---

## 14. Status line

**PROVED PARTIAL, not a full solution.** The arbitrary low-`p` dimension exponent is unchanged, but the volumetric obstruction has been reduced from selection among full local tangent models to Gaussian entropy of one-coordinate order-`r-1` critical contraction classes. The new contraction-rank theorem proves the target polynomial exponent for a broad correlated class, and the flat-profile hypercube shows both why directional information is indispensable and why a `sqrt(log d)` coordinate-selection cost is genuinely necessary.
