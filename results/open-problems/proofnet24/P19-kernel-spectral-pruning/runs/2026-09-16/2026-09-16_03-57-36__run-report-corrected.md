# ProofNet24 P19 — Kernel Spectral Pruning

**Run timestamp:** 2026-09-16 03:57:36 Asia/Jerusalem  
**Repository / branch:** `yspennstate/math-open-problems` / `master`  
**Scope:** singular values/vectors, deterministic spectral/structured pruning, Marchenko–Pastur nulls, neural/random features, kernel/operator-learning prediction risk; **NO number theory**.  
**Delivery:** GitHub only. No email/Gmail/draft/forward action was used.  
**Runtime honesty:** the requested GPT-6 / explicit maximum-reasoning selector is not exposed as a controllable setting in this run. I used the deepest useful reasoning actually available and do not claim an unexposed model switch, hidden effort override, or independent agents.

## Correction history

An earlier immutable same-run draft was committed at

`proofnet24/P19-kernel-spectral-pruning/runs/2026-09-16/2026-09-16_03-57-36__run-report.md`

with creation commit `ace85647199d74598d74fc2cc27d5b85b1942fe3`, blob `a99bd933e85c8933d478f3e133d556b325a8af9e`. Exact-commit readback exposed one notation-serialization defect in equation `(8.4)`: a missing closing bracket in the exponential. The mathematics and surrounding derivation were unchanged. The earlier immutable file is intentionally left untouched. This file is the **corrected canonical report** and records the corrected formula explicitly.

---

# 0. Executive result

P19 remains **OPEN**. This run attacks the predecessor's exact target:

`P19-GHOST-RAREBOUNDARY-36` — replace the distribution-free `O(T)` hard-pruning replacement range by an analytically certified **rare-boundary** mechanism whenever a leave-one-out/deletion anchor has a genuine top-`k` score margin and one-observation retraining perturbations have a controlled tail.

The central observation is dependence-safe: deterministic trained top-`k` is **not** an iid pruning mask. Support changes are score-crossing events of the actual retrained matrix. A deletion-anchor gap makes those crossings quantitatively rare.

New results:

- `P19-DELETION-GAP-LOCK-36 — PROVED`;
- `P19-PAIRWISE-MARGIN-FLIP-36 — PROVED`;
- `P19-SUBGAUSS-GAP-FLIP-36 — PROVED`;
- `P19-RAREBOUNDARY-CLIPPED-RMS-36 — PROVED`;
- `P19-RAREBOUNDARY-PREDVAR-36 — PROVED`;
- `P19-RAREJUMP-MGF-36 — PROVED`;
- `P19-MARGIN-SCALE-CE-36 — PROVED`;
- `P19-SMALLCOEFF-NOT-PATHWISELOSS-CE-36 — PROVED`;
- `P19-AUDIT-P16-OVERLAP-ORTHANT-36 — PASS`.

The main quantitative conclusion is the following. If a deletion-trained top-`k` score gap is `gamma`, one-observation insertion retraining has Frobenius tail scale `sigma`, insertion RMS drift `v <= L/n`, and the common proxy feature Gram has `k`-restricted upper edge at most `B`, then under

```text
gamma^2/(8 sigma^2) >= 2 log n + u,
```

the post-pruning clipped replacement influence is `O(1/n)` in RMS and the true predictable LOO coordinate variance obeys

```text
q_j
 <= [ T + 4 L sqrt(TB) + 2 T e^(-u/2) ]^2 / n^2.
```

Thus the preceding `Theta(n^2)` blind-ghost-discovery obstruction can be bypassed when the rare support-flip probability is certified analytically from the **trained score margin** and the actual retraining perturbation law.

A fresh primary-source search also found a public post-referee v1:

**Yitzchak Shmalo, _Mesoscopic Rectangular Spikes under Subspace Local Laws: Outlier Values and Singular Subspaces_, arXiv:2608.19594v1, 20 August 2026.**

Its primary arXiv abstract says that a subspace-local-law hypothesis locates/counts outliers and, in holomorphic form, determines outlier singular subspaces; conclusions use spectral projectors; the law is verified in four settings, including independent entries with fixed deterministic signal directions; and the Marchenko–Pastur constants are explicit. This is one day later than the 19 August referee report and directly addresses the referee-facing RMT themes. The current tool path did not expose the PDF theorem text for a line-by-line theorem audit, so these are recorded only as `PRIMARY-SOURCE-ABSTRACT-VERIFIED`; exact v1 rank windows, tail assumptions, theorem numbering, constants, and equivalence with July assumptions remain **UNVERIFIED THIS RUN**.

---

# 1. Mandatory continuity

Read before the attack from `master`:

- root `README.md`, blob `9d18531dff608e0165fe4434614d8c9121903c4c`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, blob `a5773ae98d59ab7d6420f809452c3b20565c3379`.

The protocol requires GitHub-only immutable complete reports, exact source discipline, explicit `PROVED / CONDITIONAL / DISPROVED / OPEN` bookkeeping, a real peer audit, exact-commit readback, no routine research email, and two complete independent OTHER-worker audits before closure.

Pre-write `master` head observed:

`baf1d382891faca004349963c5dccb10a3105b21`.

## 1.1 Latest P19 predecessor

`proofnet24/P19-kernel-spectral-pruning/runs/2026-09-16/2026-09-16_02-56-51__run-report.md`

- creation commit: `aa4629d5a7f99e4ea8987b31585714102e8c381d`;
- blob: `50b0599eb5a22d23402bd59c5aae4f52fd4504df`.

Its new package was:

- `P19-GHOST-CONDITIONAL-RESAMPLING-35`;
- `P19-GHOST-VAR-UCB-35`;
- `P19-GHOST-STITCHED-RISK-35`;
- `P19-GHOST-SPLIT-SELECTION-35`;
- `P19-GHOST-RAW-RISK-35`;
- `P19-GHOST-PLUGIN-CE-35`;
- `P19-GHOST-FROZEN-MASK-CE-35`;
- `P19-GHOST-MP-DYAD-35`.

Its obstruction was explicit: with only the universal clipped range, estimating a rare predictable variance `q_j` to relative accuracy costs generically

```text
M >= const * T^2 log(n/delta) / q_j.
```

For `q_j=Theta(n^-2)` this can mean order `n^2 log n` full ghost retrainings. Its named next target was exactly `P19-GHOST-RAREBOUNDARY-36`.

## 1.2 P15 peer snapshot

`proofnet24/P15-kernel-mean-correction/runs/2026-09-16/2026-09-16_03-22-33__run-report.md`

- creation commit: `82f3c1f498d17be305e683b3bb3cc4b05e85ad22`;
- blob: `3ac68e5938f4bb213116795698689c5f15ddd03d`.

Its current package gives exact fixed-cardinality overlap diagonalization and binomial inversion for same-observation reuse. No P15 theorem is imported into the P19 proof below.

## 1.3 P16 peer snapshot

`proofnet24/P16-relu-contraction/runs/2026-09-16/2026-09-16_03-49-12__run-report.md`

- creation commit: `38b261e451df857ddfa55a2f748caa3a49106a27`;
- blob: `e0d63649eefc1713ef91acda196db2f965ef4d44`.

Its current package includes `P16-DISJOINT-CYCLE-FIRST-MOMENT-39`, `P16-DISJOINT-CYCLE-EXCLUSION-39`, and `P16-OVERLAP-EXTERNAL-ORTHANT-39`. Section 11 independently audits the latter claim.

---

# 2. Exact July–August source boundary

The standalone July manuscript and the 19 August referee PDF still did not resolve as standalone current Library files. GitHub search returns source-certified P19 reports referring to their historical filenames, not the original binaries. Therefore the exact source statements below are retained from the already archived direct-read source chain, and no unseen assumptions are reconstructed.

The July manuscript is identified as:

**Growing-rank spiked singular vectors and singular values, with applications to pruning deep neural networks.**

Historical attachment:

`Growing_rank_spiked_singular_vectors_and_singular_values__with_applications_to_pruning_deep_neural_networks.pdf`.

The exact additive rectangular model is

```text
W_n = X_n + P_n,
P_n = U_n Theta_n V_n*.
```

Retained source hypotheses:

```text
X_n in R^(n x m),
n/m -> c in (0,1],
r_n := rank(P_n) -> infinity,
r_n = o(n),
spike strengths uniformly bounded,
and if P_n is random then P_n is independent of X_n.
```

For spectral parameter `z` away from the noise singular spectrum, the compressed blocks are

```text
A_n(z) = U_n* z(z^2-X_n X_n*)^(-1) U_n,
D_n(z) = V_n* z(z^2-X_n* X_n)^(-1) V_n,
B_n(z) = U_n* X_n (z^2-X_n* X_n)^(-1) V_n.
```

The contour hypothesis requires operator-norm scalarization

```text
A_n(z) approx phi_n(z) I,
D_n(z) approx phitilde_n(z) I,
B_n(z) approx 0,
```

with contour compression debt `beta_n^(cc)`, empirical-transform debt `zeta_n`, and deterministic cluster separation `Delta_n(C_n)`.

For a separated supercritical cluster `C_n`, the stable growing-rank singular-vector objects are the cluster projectors and sign-free mixed dyad

```text
Pihat_L(C_n),
Pihat_R(C_n),
Fhat(C_n)=sum_(j in C_n) uhat_j vhat_j*.
```

With

```text
eta_(n,C)=[beta_n^(cc)+zeta_n]/Delta_n(C_n),
```

the source-certified statements are

```text
U_n* Pihat_L(C_n) U_n
 = diag(alpha_L(theta_(n,i)) 1_(i in C_n)) + O_op(eta_(n,C)),

V_n* Pihat_R(C_n) V_n
 = diag(alpha_R(theta_(n,i)) 1_(i in C_n)) + O_op(eta_(n,C)),

U_n* Fhat(C_n) V_n
 = diag(sqrt(alpha_L(theta_(n,i)) alpha_R(theta_(n,i))) 1_(i in C_n))
   + O_op(eta_(n,C)).
```

In the Marchenko–Pastur normalization,

```text
theta_c = c^(1/4),
rho(theta)^2 = theta^2 + (1+c) + c/theta^2,

1-alpha_L(theta)
 = c(theta^2+1)/[theta^2(theta^2+c)],

1-alpha_R(theta)
 = (theta^2+c)/[theta^2(theta^2+1)].
```

The source Frobenius-optimal retained singular value is

```text
eta*(rho(theta))
 = theta sqrt(alpha_L(theta) alpha_R(theta)).
```

The deterministic realized-activation pruning identity is

```text
||E a||^2
 = sum_j (sigma_j-eta_j)^2 |<vhat_j,a>|^2.
```

This last identity is a realized-network perturbation ledger, not a fresh-population risk theorem.

The source-certified 19 August referee state remains:

1. resolvent compression contains the principal RMT difficulty;
2. concrete verification is mainly Haar/Gaussian;
3. the relation to isotropic/anisotropic local laws needs strengthening;
4. singular-vector theory and its extra technical obstacles need explicit treatment.

The 20 August arXiv v1 abstract is a primary-source indication that the revised manuscript directly reorganized around these issues, but exact theorem-level verification awaits the v1 PDF text.

---

# 3. Hard top-k setup and target

Let

```text
C=(c_1,...,c_r) in R^(q x r),
s_l(C)=||c_l||_2,
S_k(C)=deterministic exact-cardinality top-k support,
H_k(C)=C P_(S_k(C)).
```

The fixed tie rule is inherited from earlier P19 reports.

Earlier P19 proved `P19-HARD-BOUNDARY-SYMDIFF-31`: if `||C-C'||_F<=rho`, every support disagreement lies in the trained `2rho` score boundary. It also proved exact counterexamples showing that an `O(1/n)` pre-pruning perturbation can produce an order-one post-pruning jump when the score boundary is tied.

The useful unresolved question is therefore:

> Given a common deletion-trained anchor, when is the score boundary sufficiently far away relative to one-observation retraining noise that post-pruning replacement influence remains `O(1/n)`?

---

# 4. `P19-DELETION-GAP-LOCK-36` — PROVED

Let `D` be a fixed deletion context and let

```text
C_0=C_0(D),
S_0=S_k(C_0).
```

Assume `1<=k<r` and define the strict deletion-anchor gap

```text
gamma(D)=s_(k)(C_0)-s_(k+1)(C_0)>0.
```

For a fresh insertion value `z`, let `C(z)` be the fully retrained readout. The optimizer/refit may otherwise be arbitrary.

Then

```text
boxed:
S_k(C(z)) != S_0
 => ||C(z)-C_0||_F >= gamma(D)/2.                      (4.1)
```

## Proof

Set `delta=||C(z)-C_0||_F`. Every channel score is 1-Lipschitz:

```text
|s_l(C(z))-s_l(C_0)|
 <= ||c_l(z)-c_l(0)||
 <= delta.                                             (4.2)
```

If `delta<gamma/2`, every anchor-selected score after insertion is at least `s_(k)(C_0)-delta`, and every anchor-unselected score is at most `s_(k+1)(C_0)+delta`. Their difference exceeds `gamma-2delta>0`. Hence all selected anchor channels remain above all unselected ones, so the exact-cardinality support is unchanged. Contraposition proves `(4.1)`.

QED.

No random pruning mask appears.

---

# 5. Pairwise and sub-Gaussian support-flip bounds

## `P19-PAIRWISE-MARGIN-FLIP-36` — PROVED

For `a in S_0`, `b notin S_0`, put

```text
m_ab=s_a(C_0)-s_b(C_0)>0,
delta_l(z)=s_l(C(z))-s_l(C_0).
```

Assume, conditional on `D`, that for every selected/unselected pair,

```text
P{delta_b(Z)-delta_a(Z) >= t | D}
 <= exp[-t^2/(2 nu_ab^2)]                              (5.1)
```

for all `t>=0` and a fresh insertion `Z`.

Then

```text
boxed:
P{S_k(C(Z)) != S_0 | D}
 <= sum_(a in S_0,b notin S_0)
      exp[-m_ab^2/(2 nu_ab^2)].                        (5.2)
```

For two conditionally iid fresh insertions `Z,Z'`,

```text
boxed:
P{S_k(C(Z)) != S_k(C(Z')) | D}
 <= 2 sum_(a in S_0,b notin S_0)
      exp[-m_ab^2/(2 nu_ab^2)].                        (5.3)
```

### Proof

If the insertion support differs from `S_0`, cardinality preservation gives an `a` dropped from `S_0` and a `b` inserted from its complement. Since `b` is selected while `a` is not,

```text
s_b(C(Z)) >= s_a(C(Z)),
```

so

```text
delta_b(Z)-delta_a(Z)
 >= s_a(C_0)-s_b(C_0)
 = m_ab.
```

Union over selected/unselected pairs proves `(5.2)`. If two insertion supports differ, at least one differs from `S_0`; another union bound gives `(5.3)`.

QED.

## `P19-SUBGAUSS-GAP-FLIP-36` — PROVED

Assume instead the simpler conditional Frobenius tail

```text
P{||C(Z)-C_0||_F >= t | D}
 <= 2 exp[-t^2/(2 sigma(D)^2)]                         (5.4)
```

for all `t>=0`. By `(4.1)`,

```text
boxed:
P{S_k(C(Z)) != S_0 | D}
 <= 2 exp[-gamma(D)^2/(8 sigma(D)^2)].                 (5.5)
```

For two iid insertions,

```text
boxed:
p_bad(D)
:=P{S_k(C(Z)) != S_0 or S_k(C(Z')) != S_0 | D}
 <= 4 exp[-gamma(D)^2/(8 sigma(D)^2)].                 (5.6)
```

Thus if

```text
gamma(D)^2/(8 sigma(D)^2) >= 2 log n + u,             (5.7)
```

then

```text
boxed:
p_bad(D) <= 4 e^(-u)/n^2.                            (5.8)
```

Only a `sqrt(log n)` margin in units of the insertion-noise scale is needed; no constant-size absolute gap is required.

---

# 6. `P19-RAREBOUNDARY-CLIPPED-RMS-36` — PROVED

Let `psi(X) in R^r` be a common honest fresh-query proxy, independent of the insertion values conditional on `D`, with Gram

```text
G(D)=E[psi(X)psi(X)* | D].
```

Define

```text
b_k(D)=sup_(|I|<=k) lambda_max(G_II).
```

For insertion `Z`, let

```text
f_Z(X)=H_k(C(Z)) psi(X),
v(D)^2=E[||C(Z)-C_0||_F^2 | D].                        (6.1)
```

For target `Y`, let

```text
ell_T(f;(X,Y))=min{||Y-f(X)||^2,T}.
```

For two iid insertions `Z,Z'`, define

```text
beta_T(D)^2
=E[|ell_T(f_Z;Q)-ell_T(f_Z';Q)|^2 | D],               (6.2)
```

where `Q=(X,Y)` is fresh and independent of the insertions conditional on `D`.

Under `(5.4)`,

```text
boxed:
beta_T(D)^2
 <= 16 T b_k(D) v(D)^2
    + 4 T^2 exp[-gamma(D)^2/(8 sigma(D)^2)].           (6.3)
```

Therefore

```text
boxed:
beta_T(D)
 <= 4 sqrt(T b_k(D)) v(D)
    + 2 T exp[-gamma(D)^2/(16 sigma(D)^2)].            (6.4)
```

Equation `(6.4)` is the corrected rendering of the only malformed formula in the first immutable draft.

## Proof

Let `E_good` be the event that both insertion supports equal `S_0`. By `(5.6)`,

```text
P(E_good^c|D)
 <= 4 exp[-gamma^2/(8 sigma^2)].                       (6.5)
```

On `E_good`,

```text
f_Z-f_Z'
=(C(Z)-C(Z'))P_(S_0) psi.
```

Hence

```text
E[||f_Z-f_Z'||^2 1_(E_good)|D]
 <= b_k(D) E||C(Z)-C(Z')||_F^2
 <= 4 b_k(D) v(D)^2.                                  (6.6)
```

The last inequality follows from

```text
||A-B||^2
 <=2||A-C_0||^2+2||B-C_0||^2.
```

The scalar map `r -> min{||r||^2,T}` is globally `2sqrt(T)`-Lipschitz in the residual norm, so on `E_good`,

```text
|ell_T(f_Z)-ell_T(f_Z')|^2
 <= 4T ||f_Z-f_Z'||^2.                                (6.7)
```

Thus the good-event contribution is at most `16Tb_kv^2`. On `E_good^c`, both clipped losses lie in `[0,T]`, so their difference has magnitude at most `T`; the contribution is at most `T^2 P(E_good^c|D)`. Combining with `(6.5)` proves `(6.3)`. Apply `sqrt(a+b)<=sqrt(a)+sqrt(b)` to get `(6.4)`.

QED.

### Representation-debt boundary

This theorem deliberately uses a common proxy feature map. If retraining changes the representation, decompose

```text
phi_Z=psi+(phi_Z-psi)
```

and add the coefficient-weighted representation debts from the inherited P19 trained-to-proxy results. No iid feature substitution is permitted.

---

# 7. `P19-RAREBOUNDARY-PREDVAR-36` — PROVED

For the inherited clipped leave-one-out gap `H_T`, the previous P19 chain established the exact coordinate-replacement decomposition

```text
Delta_j H_T
=(1/n)[A_j + sum_(i != j) xi_ij],                     (7.1)
```

where `|A_j|<=T` and each `xi_ij` is a deletion/replacement clipped-loss influence.

Conditional `L^2` Minkowski gives

```text
sqrt(q_j)
:=||Delta_j H_T||_(L^2|F_(j-1))
 <=(1/n)[T+sum_(i != j)||xi_ij||_(L^2|F_(j-1))].      (7.2)
```

Suppose the deletion-anchor theorem applies uniformly to all relevant `(i,j)` contexts with predictable or deterministic envelopes

```text
b_k<=B,
v<=L/n,
gamma^2/(8 sigma^2)>=2 log n+u.                      (7.3)
```

Then `(6.4)` and `(5.8)` yield

```text
||xi_ij||_2
 <=[4L sqrt(TB)+2T e^(-u/2)]/n.                       (7.4)
```

Substituting in `(7.2)` gives

```text
boxed:
sqrt(q_j)
 <=[T+4L sqrt(TB)+2T e^(-u/2)]/n,                    (7.5)
```

and

```text
boxed:
q_j
 <=[T+4L sqrt(TB)+2T e^(-u/2)]^2/n^2.               (7.6)
```

This closes the **variance-scale** part of `P19-GHOST-RAREBOUNDARY-36`.

The preceding ghost-UCB theorem remains useful, but the margin theorem removes the need for blind ghost sampling to discover a rare order-one support flip when its probability is already controlled by `gamma/sigma`. A safe hybrid upper bound is

```text
U_j^hybrid=min{U_j^ghost,U_j^margin},
```

on the joint event where both upper bounds are valid. If `L,sigma,gamma,B` are estimated, their estimation error and any model selection must be paid explicitly.

---

# 8. `P19-RAREJUMP-MGF-36` — PROVED

Small predictable variance alone does not yield a sub-Gaussian martingale increment because a rare support flip can remain order one. The right object is an MGF retaining the rare-jump probability.

Let `X` be conditionally mean zero given sigma-field `G`. Assume

```text
|X|<=B,
P{|X|>a|G}<=p,
0<=a<=B.
```

Then for every `lambda>=0`,

```text
boxed:
log E[e^(lambda X)|G]
 <=(lambda^2/2)
   [a^2 e^(lambda a)+pB^2 e^(lambda B)].              (8.1)
```

## Proof

For every real `x`, Taylor's formula with remainder gives

```text
e^(lambda x)
 <=1+lambda x+(lambda^2 x^2/2)e^(lambda|x|).
```

Taking conditional expectation kills the linear term. On `|X|<=a`, the remainder is at most `a^2 e^(lambda a)`; on the complement it is at most `B^2 e^(lambda B)`, incurred with probability at most `p`. Thus

```text
E[e^(lambda X)|G]
 <=1+(lambda^2/2)[a^2 e^(lambda a)+pB^2 e^(lambda B)].
```

Use `log(1+y)<=y`.

QED.

For the inherited replacement identity

```text
D_j=E[Delta_j H_T|F_j],
```

conditional Jensen gives

```text
E[e^(lambda D_j)|F_(j-1)]
 <=E[e^(lambda Delta_j H_T)|F_(j-1)].                 (8.2)
```

So any good/bad decomposition for the **actual full coordinate replacement**, including retraining and support reselection, transfers to the Doob increment.

Equation `(8.1)` shows exactly when the universal `O(T)` jump range is irrelevant at a desired confidence level: if the good-region increment is `a=O(1/n)` and the support-flip probability is small enough that `p e^(lambda B)` remains negligible at the chosen `lambda`. It also shows why a variance-only theorem cannot do this.

The score-gap theorem supplies `p`. A small **pathwise** good-region increment `a` still needs a legal feature/output envelope or conditional feature-tail theorem; covariance/RMS control alone is insufficient.

---

# 9. New counterexamples

## `P19-MARGIN-SCALE-CE-36` — PROVED

Take `r=2`, `q=1`, `k=1`, anchor

```text
C_0=(1,1),
```

with the fixed tie rule selecting coordinate 1. Let a fresh insertion produce

```text
C_Z=(1+Z/n,1-Z/n),
```

where `Z` is Rademacher. Then

```text
||C_Z-C_0||_F=sqrt(2)/n
```

deterministically, but

```text
S_1(C_Z)={1} if Z=+1,
S_1(C_Z)={2} if Z=-1.
```

For two iid insertions, support disagreement has probability `1/2`. Under an honest proxy `psi~N(0,I_2)`, when the supports differ the pruned coefficient vectors are orthogonal and have prediction `L^2` distance squared `2(1+1/n)^2`. Hence post-pruning prediction RMS stays order one despite `O(1/n)` pre-pruning drift.

Therefore small one-observation coefficient drift does not imply small post-pruning RMS without a score-margin condition.

## `P19-SMALLCOEFF-NOT-PATHWISELOSS-CE-36` — PROVED

Even with fixed support, take `Y=0`, `C=0`, `C'=epsilon`, and a deterministic query feature

```text
psi(X)=sqrt(T)/epsilon.
```

Then `||C-C'||=epsilon->0`, but `f=0`, `f'=sqrt(T)`, so the clipped squared losses differ by exactly `T`. Thus a small coefficient perturbation does not yield a small pathwise clipped-loss increment for unbounded features. A feature/output tail or envelope remains necessary for an `O(1/n)` Bernstein-scale theorem.

---

# 10. Same-trained-matrix dependence audit

The new theorem is compatible with adaptive trained pruning because:

1. `S_k(C(Z))` is the deterministic support selected from the fully retrained matrix for insertion `Z`;
2. support selection is rerun after replacement, not frozen;
3. no Bernoulli/iid mask is introduced;
4. support-change probability is bounded by actual score crossings relative to a common deletion-trained anchor;
5. if an honest Gaussian proxy is used, any sparse-RIP statement must hold simultaneously over the relevant supports, rather than conditioning on an adaptively selected support and pretending it was independent.

Thus pruning based on the trained matrix invalidates iid-mask arguments, but it does not invalidate the deletion-anchor margin theorem because the retraining and reselection dependence is inside the event being bounded.

---

# 11. Independent peer audit

## `P19-AUDIT-P16-OVERLAP-ORTHANT-36 — PASS`

Audited path:

`proofnet24/P16-relu-contraction/runs/2026-09-16/2026-09-16_03-49-12__run-report.md`

- creation commit: `38b261e451df857ddfa55a2f748caa3a49106a27`;
- blob: `e0d63649eefc1713ef91acda196db2f965ef4d44`;
- claim ID: `P16-OVERLAP-EXTERNAL-ORTHANT-39`.

P16 considers a period-two tied-Gaussian ReLU candidate with positive phase vectors `u` on support `S` and `v` on support `T`. Put

```text
I=S cap T,
U=S union T,
R=U^c.
```

For an outside row `i in R`, after conditioning on all internal rows, P16 claims the two inactive linear forms are centered Gaussian with correlation

```text
rho=<u_I,v_I>/(||u||||v||),
```

and

```text
P{X_i<=0,Y_i<=0}
=1/4+arcsin(rho)/(2 pi).                               (11.1)
```

### Independent derivation

Rows of the tied Gaussian matrix are iid. Conditioning on all rows indexed by `U` leaves each outside row independent with its original Gaussian law. Hence

```text
Var(X_i)=(alpha/N)||u||^2,
Var(Y_i)=(alpha/N)||v||^2,
Cov(X_i,Y_i)=(alpha/N)<u_I,v_I>.
```

This gives `rho` exactly. For a standardized bivariate Gaussian, write

```text
X=G_1,
Y=rho G_1+sqrt(1-rho^2)G_2,
```

where `(G_1,G_2)` is isotropic in the plane. The event `X>0,Y>0` is a wedge of angle

```text
pi/2+arcsin(rho).
```

Rotational invariance gives probability

```text
[pi/2+arcsin(rho)]/(2pi)
=1/4+arcsin(rho)/(2pi).
```

Central symmetry gives the same value in the negative orthant. Nondegeneracy removes `<` versus `<=`. Different outside rows are conditionally independent, so the total outside-row factor is exactly

```text
[1/4+arcsin(rho)/(2pi)]^(N-|U|).
```

**Verdict: PASS.** The conditioning, covariance, orthant constant, and row-product exponent are correct. The claim does not assert independence of the overlapping internal blocks.

A 500,000-pair numerical sanity check at `rho=0.6` gave empirical `0.352042` versus exact `0.3524163823`; this check is not used as proof.

This is a component audit, not one of the two complete independent OTHER-worker P19 audits required for closure.

---

# 12. Spectral-layer separation and MP composition

The new theorem is a learning/dependence result. It does not conflate the RMT layers.

## Eigenvalue distribution / MP bulk

An honest iid Gaussian feature Gram can obey the global Marchenko–Pastur law. If `r/n>1`, the global Gram is singular and has an MP zero atom. This is about the global empirical eigenvalue distribution/hard edge.

## Restricted extreme singular values

If simultaneously for every `|J|<=2k`,

```text
(1-delta)I <= G_JJ <= (1+delta)I,                     (12.1)
```

then the rare-boundary theorem may use `B=1+delta`, while coefficient identifiability uses `a_(2k)>=1-delta`. This sparse restricted geometry can remain nondegenerate even when the global Gram is singular.

## Singular-vector overlap

The July `alpha_L,alpha_R` laws are compressed-resolvent/residue statements. They stay on the subspace-local-law branch. They are not derived from Wedin or from the pruning-margin theorem.

## Prediction risk

Equations `(6.3)` and `(7.6)` control post-pruning clipped replacement RMS and predictable LOO variance under explicit deletion-gap/retraining-tail conditions.

## Coefficient/operator and singular-subspace stability

If an independently valid risk certificate gives

```text
E||(C_1-C_2)psi||^2 <= Rbar_delta
```

for two legally aligned `k`-sparse deployed readouts and their support union obeys

```text
G_JJ >= a I,
```

then

```text
||C_1-C_2||_op <= sqrt(Rbar_delta/a).                 (12.2)
```

Only if the right side is at most half a genuine protected singular-value gap `Delta_K` is Wedin/Hermitian dilation invoked:

```text
||Delta Pihat_K^L||_op,
||Delta Pihat_K^R||_op,
||Delta Fhat_K||_op
 <=(4/Delta_K)sqrt(Rbar_delta/a).                     (12.3)
```

No Wedin/Davis–Kahan statement is used without a gap, and no such perturbation estimate is presented as a BBP overlap formula.

## Finite-width debts

The finite-width chain now separates:

- insertion/retraining RMS `L/n`;
- insertion tail scale `sigma` or pairwise score scales `nu_ab`;
- trained score gap `gamma`;
- sparse Gram edges `a,b`;
- representation-transfer debt;
- raw feature/output tails for pathwise exponential confidence;
- ghost estimation error only for quantities not already certified analytically.

---

# 13. Route comparison

## Resolvent/subspace-local-law route

This remains the correct route for source BBP outlier locations and singular-subspace overlaps. The newly found arXiv v1 abstract explicitly centers the problem on a subspace local law. Exact v1 theorem hypotheses still need direct PDF audit.

## Davis–Kahan/Wedin

Useful only after a genuine operator perturbation and protected singular gap are available. It is a second-stage stability theorem, not a substitute for the source resolvent overlap law.

## Leave-one-out/deletion

This run strengthens this route. A deletion-trained anchor makes the two one-observation insertions conditionally comparable and turns hard top-`k` support changes into explicit score-crossing events.

## Free probability

No free-probability reduction is needed for the new theorem. A free-probability heuristic would not solve the trained-mask dependence or score-boundary problem.

## Deterministic equivalents / sparse Gram transfer

These remain useful for converting prediction discrepancy to coefficient/operator discrepancy, provided restricted support geometry is certified.

## Sparsification concentration

A simultaneous sparse-RIP event can be used because it is uniform over all relevant supports. An iid-mask argument is invalid when pruning uses the trained matrix.

## Counterexamples

The zero-gap and unbounded-feature examples show exactly why the new margin and feature-tail obligations cannot be dropped.

---

# 14. Tests and limitations

The constants in `(6.3)` were checked directly:

```text
E_good prediction square <= 4 b_k v^2,
clipped loss is 2 sqrt(T)-Lipschitz,
P(E_good^c)<=4 exp[-gamma^2/(8 sigma^2)],
```

so the good term is `4T*4b_kv^2=16Tb_kv^2` and the bad term is `4T^2 exp[-gamma^2/(8sigma^2)]`.

The `sqrt(log n)` threshold is exact from `(5.7)`.

The July and 19 August original PDFs were inaccessible as standalone current files. The 20 August arXiv abstract was accessible as primary-source text, but the theorem-level PDF text was not exposed through the current tool path. No exact arXiv v1 theorem assumptions beyond the abstract are claimed.

No source deletion/replacement checkpoints, feature matrices, or training code were accessible. Therefore the source values of `gamma`, `sigma`, `L`, restricted Gram edges, representation debt, raw feature-tail envelope, and deployed singular gap remain conditional obligations.

---

# 15. Failed routes and preserved counterexamples

The inherited failures remain active:

- MP-looking bulk ESD does not imply vector isotropy or selected-support conditioning;
- global MP hard-edge singularity does not imply failure of every sparse certificate;
- prediction agreement does not imply coefficient/singular-vector agreement without restricted identifiability;
- reused training/audit fit is not automatically a fresh-population certificate;
- pre-pruning stability does not imply post-hard-pruning stability at a score boundary;
- clipped covariance lower-certifies identifiability but does not upper-control unbounded raw risk without tails;
- small `L^2` influence does not automatically give small `psi_1` influence;
- variance-only self-normalization cannot remove jump-scale control;
- blind ghost sample variance is not a valid predictable-variance UCB;
- freezing the trained mask during ghost calibration can miss order-one adaptive hard-pruning influence.

Newly added failures:

- `P19-MARGIN-SCALE-CE-36`: `O(1/n)` coefficient drift with zero score gap can still give order-one post-pruning RMS;
- `P19-SMALLCOEFF-NOT-PATHWISELOSS-CE-36`: small coefficient drift, even with fixed support, does not shrink the pathwise clipped-loss range for unbounded features.

---

# 16. Cumulative claim ledger

## PROVED / validated

Retained source-certified chain:

- July additive growing-rank rectangular model and cluster-projector/mixed-dyad/MP formulas stated in Section 2;
- realized-activation pruning identity;
- all preceding P19 hard-boundary, covariance-boundary, restricted-Gram, fresh/reused audit, LOO, clipping, self-normalized, ghost-UCB, sparse-MP, and counterexample results with their original hypotheses.

New this run:

- `P19-DELETION-GAP-LOCK-36`;
- `P19-PAIRWISE-MARGIN-FLIP-36`;
- `P19-SUBGAUSS-GAP-FLIP-36`;
- `P19-RAREBOUNDARY-CLIPPED-RMS-36`;
- `P19-RAREBOUNDARY-PREDVAR-36`;
- `P19-RAREJUMP-MGF-36`;
- `P19-MARGIN-SCALE-CE-36`;
- `P19-SMALLCOEFF-NOT-PATHWISELOSS-CE-36`;
- `P19-AUDIT-P16-OVERLAP-ORTHANT-36 = PASS`.

Primary-source update:

- arXiv:2608.19594v1 title, author, date, and abstract-level claims are `PRIMARY-SOURCE-ABSTRACT-VERIFIED`.

## CONDITIONAL

- actual source deletion-anchor gaps `gamma`;
- source one-observation retraining RMS `L/n`;
- source insertion-tail scale `sigma` or pairwise score-difference scales `nu_ab`;
- legal alignment of learned representations across deletion/insertion retrainings;
- representation-transfer debt to a common honest proxy;
- feature/output tails needed to shrink the pathwise Bernstein scale;
- source sparse restricted Gram lower/upper edges;
- source raw-loss tail envelope;
- actual protected deployed singular-value gap `Delta_K`;
- any equivalence claim between exact arXiv v1 theorem assumptions and the archived July hypotheses.

## DISPROVED / REJECTED

- trained deterministic top-`k` may be replaced by an iid mask;
- MP bulk ESD implies selected-support vector isotropy;
- global MP hard-edge singularity implies sparse-pruning failure;
- small prediction discrepancy implies singular-vector stability without restricted identifiability;
- pre-pruning stability implies post-pruning stability without boundary control;
- reused empirical audit is automatically fresh-population valid;
- clipped covariance alone upper-controls unbounded raw risk;
- small `L^2` influence automatically gives small subexponential influence;
- variance alone gives sub-Gaussian self-normalization;
- raw ghost sample variance may be plugged in as predictable variance;
- ghost calibration may freeze the original trained mask;
- `O(1/n)` coefficient drift alone yields `O(1/n)` post-pruning RMS;
- small coefficient drift alone yields a small pathwise clipped-loss increment with unbounded features.

## OPEN

1. `P19-ARXIV-V1-EXACT-AUDIT-37`: obtain the exact theorem text of arXiv:2608.19594v1 and map its subspace-local-law hypotheses, rank regime, independent-entry verification, projector theorem, and MP constants against the archived July source statements and 19 August referee objections.
2. `P19-SOURCE-MARGIN-AUDIT-37`: recover source deletion/replacement checkpoints and measure/prove `gamma`, insertion drift/tails, score-difference tails, boundary flips, representation debt, restricted Gram edges, and a deployed singular gap.
3. `P19-RAREBOUNDARY-MGF-COMPOSE-37`: combine `(8.1)` with a legal common-proxy feature tail/good-region pathwise increment to obtain exponential-confidence LOO bounds with effective `O(1/n)` scale on the desired confidence range.
4. Any non-Haar/fixed-deterministic-frame subspace local-law regime not already covered by the exact v1 theorem after that theorem is directly audited.
5. Critical `n^(-1/3)` BBP coupling / near-threshold growing-rank regime.
6. Two OTHER independent complete end-to-end P19 audits before any closure claim.

---

# 17. Next concrete attack

The highest-value analytic target is `P19-RAREBOUNDARY-MGF-COMPOSE-37`:

> Starting from `p_bad <= 4 exp[-gamma^2/(8sigma^2)]`, add a legal Gaussian/sub-Gaussian/source-measured feature tail to construct a good-region pathwise increment `a_j`, insert `(a_j,p_j,B)` into `P19-RAREJUMP-MGF-36`, and derive a martingale confidence inequality whose effective linear scale is `O(1/n)` when the trained score margin is sufficiently many insertion-noise standard deviations from the pruning boundary.

The highest-value source target is `P19-ARXIV-V1-EXACT-AUDIT-37` because the newly found public 20 August v1 appears, at abstract level, to address the 19 August referee's local-law and singular-subspace objections.

If source checkpoints become accessible, `P19-SOURCE-MARGIN-AUDIT-37` should take precedence over another abstract analytic layer because the present theorem gives a direct finite-sample checklist.

---

# 18. Source and method checklist

Repository evidence consumed:

- `README.md`, blob `9d18531dff608e0165fe4434614d8c9121903c4c`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, blob `a5773ae98d59ab7d6420f809452c3b20565c3379`;
- P19 predecessor `2026-09-16_02-56-51__run-report.md`, creation commit `aa4629d5a7f99e4ea8987b31585714102e8c381d`, blob `50b0599eb5a22d23402bd59c5aae4f52fd4504df`;
- P15 peer `2026-09-16_03-22-33__run-report.md`, creation commit `82f3c1f498d17be305e683b3bb3cc4b05e85ad22`, blob `3ac68e5938f4bb213116795698689c5f15ddd03d`;
- P16 peer `2026-09-16_03-49-12__run-report.md`, creation commit `38b261e451df857ddfa55a2f748caa3a49106a27`, blob `e0d63649eefc1713ef91acda196db2f965ef4d44`.

Primary public update checked:

- Yitzchak Shmalo, _Mesoscopic Rectangular Spikes under Subspace Local Laws: Outlier Values and Singular Subspaces_, arXiv:2608.19594v1, 20 August 2026; primary abstract directly read, theorem text not yet directly audited.

Methods retained/compared:

- compressed resolvents / subspace local laws for BBP outlier values and singular subspaces;
- Wedin/Hermitian dilation only with an actual operator perturbation and protected gap;
- leave-one-out/deletion anchors for trained-matrix dependence;
- sparse Gram/deterministic-equivalent transfer for prediction-to-operator conversion;
- simultaneous sparsification concentration rather than iid-mask substitution;
- exact counterexamples at pruning boundaries and under unbounded feature tails;
- no free-probability shortcut where the direct deletion-margin argument is stronger.

No number theory was introduced. No email was used.

---

# 19. Delivery checklist

- [x] Corrected complete canonical UTF-8 report authored.
- [x] Earlier immutable draft preserved rather than overwritten.
- [x] Exact target, full new proof work, failures/counterexamples, tests, source update, peer audit, cumulative ledger, obligations, and next attack included.
- [x] No email/Gmail used.
- [ ] Corrected report commit SHA and exact-commit readback to be verified after creation.
