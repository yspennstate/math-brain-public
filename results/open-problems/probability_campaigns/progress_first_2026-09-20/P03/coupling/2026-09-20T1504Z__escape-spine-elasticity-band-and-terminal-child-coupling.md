Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum reasoning was requested as a preference, but no authenticated runtime telemetry establishes that setting.

# P03-B coupling report — escape-spine elasticity band and terminal-child coupling

**Status:** PROVED PARTIAL / NEW QUENCHED SPINE REPRESENTATION / NEW COMPLETE DESCENDANT-SKELETON COUPLING. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains open.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling, spine comparison and source-valid bounded-support counterexample/certificate role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `251a94d3075721b3c6666c734016600bfc31fd04`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T1416Z__excursion-block-marginalization-and-heterogeneity-loop-reversal.md`.

**Complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1409Z__finite-second-moment-critical-profile-and-support-free-tail-identity.md`. P03-A now controls the critical-edge escape/speed profile under only a finite second moment and develops analytic terminal-strip arguments. This report stays in the distinct quenched regeneration/spine/coupling direction for bounded support, chiefly in the region `beta d>1`.

---

## 1. Source normalization and current benchmark

The primary source is G. Ben Arous, A. Fribergh and V. Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865. Their `beta` is the **outward child bias**. At a non-root vertex with `k` children,

\[
P_\beta(x,x^*)=\frac1{1+\beta k},
\qquad
P_\beta(x,x_i)=\frac\beta{1+\beta k}.
\tag{1.1}
\]

The source assumes a supercritical Galton–Watson tree without leaves, `P(Z=0)=0`, and the transient regime is `beta>1/EZ`. The LPP conjecture asks that the speed be increasing throughout that interval. The old arXiv high-bias theorem (`beta>=717`, with the minimum-degree refinement in that work) is source history only, not the present frontier.

Bowditch–Tokushige, arXiv:1906.07913, prove differentiability of the speed in their ballistic/CLT regime and express the derivative through a Gaussian covariance; arXiv:2006.03433 proves analyticity in the ballistic regime. These are regularity tools, not derivative-sign theorems.

A fresh bounded literature check on 20 September 2026 again found the broad later primary monotonicity theorem of H. Song, L. Wang and K. Xiang, *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias*, J. Appl. Probab. 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`. They use reciprocal **parent bias** `lambda=1/beta` and, when the minimum offspring is `d>=2`, prove strict decrease for

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

No inverse-parametrization contradiction is inferred. The full-source conjecture remains open in the checked literature.

---

## 2. Inherited descendant-block reduction

The `1416Z` P03-B report coarse-grained a visit to a fixed vertex `v` by deleting complete child excursions that return to `v`. If the children are `u_1,...,u_k`, set

\[
h_i(\beta)=P_\beta^{u_i}(T_v<\infty),
\qquad
\ell_i(\beta)=\frac{\beta}{1+\beta k}h_i(\beta),
\qquad
 e_i(\beta)=\frac{\beta}{1+\beta k}(1-h_i(\beta)).
\tag{2.1}
\]

Write

\[
L=\sum_i\ell_i,
\qquad
S=\sum_i(1-h_i).
\tag{2.2}
\]

For `beta d>1`, every complete returning-child kernel `ell_i` decreases with `beta`, hence `L` decreases. After summing the geometric stack of returned child excursions, the decisive parent-exit probability is exactly

\[
h_v(\beta)=\frac1{1+\beta S},
\tag{2.3}
\]

and, conditional on a decisive outward exit, the terminal child law is

\[
\pi_i(\beta)=\frac{1-h_i(\beta)}{S(\beta)}.
\tag{2.4}
\]

The previous report bounded the motion of `pi` with only the one-sided estimate `0<=g_i<=1/(beta d-1)`, where

\[
g_i:=\beta\,\partial_\beta\log(1-h_i)
=-\frac{\beta h_i'}{1-h_i}.
\tag{2.5}
\]

The main advance below is a sharp **two-sided support-dependent band** for `g`, obtained from an exact escape-spine representation. It makes terminal branch-selection cost proportional to offspring heterogeneity `D-d` and exactly zero on a regular tree.

---

## 3. Two-sided return bounds for bounded-support deterministic trees

Fix any deterministic rooted tree whose non-root offspring counts satisfy

\[
1\le d\le k_x\le D<\infty,
\qquad \beta d>1.
\tag{3.1}
\]

For a non-root vertex `x`, let

\[
h_x(\beta)=P_\beta^x(T_{x^*}<\infty).
\tag{3.2}
\]

### Lemma 3.1 — regular-tree sandwich

For every such `x`,

\[
\boxed{
\frac1{\beta D}\le h_x(\beta)\le\frac1{\beta d}.
}
\tag{3.3}
\]

#### Proof

Before hitting `x^*`, the distance from `x^*` is a nearest-neighbor process. At a vertex with `k` children its probability of moving one level toward `x^*` is

\[
q_k=\frac1{1+\beta k},
\]

and its probability of moving one level away is `1-q_k`. Since `d<=k<=D`, this distance process is squeezed between the homogeneous biased walks with offspring `d` and `D`. For the homogeneous `m`-ary tree with `beta m>1`, the probability, starting one level above zero, ever to hit zero is exactly `1/(beta m)`. Standard monotone coupling of the one-dimensional distance chains therefore gives (3.3). `square`

Both constants are sharp as deterministic-tree bounds, attained on the regular `D`-ary and `d`-ary trees respectively.

---

## 4. Exact escape-spine representation for return elasticity

Put

\[
t_x:=1-h_x,
\qquad
S_x:=\sum_{y:\,y^*=x}t_y,
\qquad
\pi_x(y):=\frac{t_y}{S_x}.
\tag{4.1}
\]

The exact return recursion is

\[
h_x=\frac1{1+\beta S_x},
\qquad
t_x=\frac{\beta S_x}{1+\beta S_x}.
\tag{4.2}
\]

Define the logarithmic escape elasticity

\[
g_x:=\beta\,\partial_\beta\log t_x
=-\frac{\beta h_x'}{1-h_x}.
\tag{4.3}
\]

The inherited two-sided differentiability/elasticity result justifies these derivatives throughout `beta d>1`.

Differentiating (4.2), and using

\[
\beta S_x'=
\sum_y t_y g_y,
\]

gives the exact recursion

\[
\boxed{
g_x=h_x\left(1+\sum_y\pi_x(y)g_y\right).}
\tag{4.4}
\]

This has a useful probabilistic expansion. Starting at `Y_0=x`, define an **escape spine** by choosing

\[
P(Y_{n+1}=y\mid Y_n)=\pi_{Y_n}(y).
\tag{4.5}
\]

Thus the next vertex is selected proportionally to its permanent-escape weight `1-h_y`; this is the quenched harmonic child law after returned excursions have been erased.

### Theorem 4.1 — escape-spine Green representation

Throughout `beta d>1`,

\[
\boxed{
 g_x
 =E_x^{\pi}\left[
 \sum_{n\ge0}\prod_{j=0}^{n}h_{Y_j}
 \right].
}
\tag{4.6}
\]

#### Proof

Iterating (4.4) `N` times gives

\[
g_x
=E_x^{\pi}\left[
\sum_{n=0}^{N}\prod_{j=0}^{n}h_{Y_j}
+\left(\prod_{j=0}^{N}h_{Y_j}\right)g_{Y_{N+1}}
\right].
\tag{4.7}
\]

The inherited bound `g_z<=1/(beta d-1)` and Lemma 3.1 give

\[
0\le
\left(\prod_{j=0}^{N}h_{Y_j}\right)g_{Y_{N+1}}
\le
\left(\frac1{\beta d}\right)^{N+1}
\frac1{\beta d-1}\to0.
\]

Let `N->infinity`. `square`

### Corollary 4.2 — sharp two-sided elasticity band

Lemma 3.1 inserted into (4.6) gives

\[
\boxed{
\frac1{\beta D-1}
\le g_x(\beta)
\le
\frac1{\beta d-1}.
}
\tag{4.8}
\]

Both endpoints are sharp: on the regular `m`-ary tree,

\[
h=\frac1{\beta m},
\qquad
g=\frac1{\beta m-1}.
\tag{4.9}
\]

Hence the **entire possible child-to-child elasticity spread** is

\[
\boxed{
\Delta_{d,D}(\beta)
:=\frac1{\beta d-1}-\frac1{\beta D-1}
=
\frac{\beta(D-d)}{(\beta d-1)(\beta D-1)}.
}
\tag{4.10}
\]

This vanishes exactly in the regular case `D=d`, as any branch-selection error term should.

---

## 5. Terminal child-selection score, Fisher energy and finite-bias coupling

From (2.4),

\[
\boxed{
\beta\,\partial_\beta\log\pi_i
=g_i-\bar g,
\qquad
\bar g:=\sum_j\pi_jg_j.
}
\tag{5.1}
\]

Thus for arbitrary continuation values `F_i(beta)`,

\[
\boxed{
\beta\frac d{d\beta}\sum_i\pi_iF_i
=
\sum_i\pi_i\,\beta F_i'
+
\operatorname{Cov}_\pi(F,g).
}
\tag{5.2}
\]

The second term is the complete terminal branch-selection contribution at `v`.

### Theorem 5.1 — heterogeneity-only terminal-selection bound

Using (4.8) and the weighted Gruss inequality,

\[
\boxed{
|\operatorname{Cov}_\pi(F,g)|
\le
\frac{\operatorname{osc}(F)}4\,
\Delta_{d,D}(\beta).
}
\tag{5.3}
\]

Therefore the adverse contribution to the ordinary `beta` derivative is at most

\[
\boxed{
\frac{\operatorname{osc}(F)}{4\beta}
\Delta_{d,D}(\beta).
}
\tag{5.4}
\]

This is strictly sharper than the inherited `osc(F)/(4 beta(beta d-1))` whenever `D<infinity`, and it is exact-zero for a regular tree.

The terminal child-selection Fisher information satisfies

\[
\boxed{
I_{\rm sel}(\beta)
:=\sum_i\frac{(\pi_i')^2}{\pi_i}
=
\frac{\operatorname{Var}_\pi(g)}{\beta^2}
\le
\frac{\Delta_{d,D}(\beta)^2}{4\beta^2}.
}
\tag{5.5}
\]

Also

\[
\boxed{
\frac12\sum_i|\pi_i'|
\le
\frac{\Delta_{d,D}(\beta)}{4\beta}.
}
\tag{5.6}
\]

Integrating (5.6), for `beta_2>beta_1>1/d`, gives the non-infinitesimal total-variation estimate

\[
\boxed{
\|\pi(\beta_2)-\pi(\beta_1)\|_{\rm TV}
\le
\frac14\log
\frac{(\beta_2d-1)(\beta_1D-1)}
{(\beta_2D-1)(\beta_1d-1)}.
}
\tag{5.7}
\]

The right side can of course be truncated at `1`.

Consequently a maximal coupling of the decisive outward child at the two biases can be chosen so that

\[
P(I_{\beta_2}\ne I_{\beta_1}\mid\text{both decisive exits outward},T)
\le \text{RHS of (5.7)}.
\tag{5.8}
\]

At derivative scale,

\[
\boxed{
P(I_{\beta+\varepsilon}\ne I_\beta
\mid\text{both outward},T)
\le
\frac{\Delta_{d,D}(\beta)}{4\beta}\,\varepsilon+o(\varepsilon).
}
\tag{5.9}
\]

This is a direct regeneration-coupling use of the spine bound rather than an analytic recursion for speed.

---

## 6. Complete coarse descendant-skeleton coupling

Let `C_beta` be the number of complete returned child excursions made from `v` before the first decisive event. Let `J_beta` be that decisive event (`P` for a parent step, `O` for a permanent outward escape), and when `J_beta=O` let `I_beta` be the selected child.

Quenched, the joint law factorizes exactly:

\[
P(C=n,J=P)=L^n q_v,
\qquad
P(C=n,J=O,I=i)=L^n e_i,
\tag{6.1}
\]

so

\[
\boxed{
P(C=n)=(1-L)L^n,
\quad
P(J=P)=h_v,
\quad
P(I=i\mid J=O)=\pi_i,
}
\tag{6.2}
\]

and `C` is independent of the decisive type/child after this coarse marginalization.

For `beta_2>beta_1>1/d`, the inherited complete-returned-excursion theorem gives

\[
L(\beta_2)\le L(\beta_1),
\tag{6.3}
\]

and the return recursion gives

\[
h_v(\beta_2)\le h_v(\beta_1).
\tag{6.4}
\]

### Theorem 6.1 — one-vertex coarse Strassen coupling

There exists a quenched coupling of the two coarse descendant skeletons such that

\[
\boxed{
C_{\beta_2}\le C_{\beta_1},
\qquad
\mathbf 1_{\{J_{\beta_2}=P\}}
\le
\mathbf 1_{\{J_{\beta_1}=P\}}
}
\tag{6.5}
\]

almost surely. On the event that both decisive exits are outward, the terminal children can simultaneously be maximally coupled with disagreement bounded by (5.7).

#### Proof

Couple the two geometric variables `C` monotonically using a common uniform sequence and (6.3). Independently, couple the Bernoulli parent indicators monotonically using a common uniform and (6.4). Conditional on both indicators being outward, use a maximal coupling of the two `pi` laws. The factorization (6.2) preserves each marginal exactly. `square`

Thus, after all returned descendant excursions are marginalized, **every non-monotone descendant-side discrepancy is localized to terminal child selection**, and its probability is explicitly heterogeneity-controlled by (5.7). The extra decisive-direction mismatch is favorable: the more outward-biased walk may escape when the less biased walk returns to the parent, but not conversely under this coupling.

This is the cleanest coupling reduction obtained so far in P03-B.

---

## 7. New local harmonic-spine drift certificate

The terminal child law can select subtrees differently as `beta` changes. A natural test is whether this selection can overturn the direct favorable derivative of the selected child's one-step parent threshold.

Let child `i` have degree `k_i in [d,D]` and

\[
q_i(\beta)=\frac1{1+\beta k_i}.
\tag{7.1}
\]

Set

\[
\bar q_{\rm esc}(\beta):=\sum_i\pi_i(\beta)q_i(\beta).
\tag{7.2}
\]

By (5.2),

\[
\beta\bar q_{\rm esc}'
=
-\sum_i\pi_i q_i(1-q_i)
+
\operatorname{Cov}_\pi(q,g).
\tag{7.3}
\]

Because `beta d>1`, all `q_i<1/2`, so `q(1-q)` is increasing on the allowed interval. Hence

\[
\sum_i\pi_i q_i(1-q_i)
\ge
q_D(1-q_D)
=
\frac{\beta D}{(1+\beta D)^2}.
\tag{7.4}
\]

Also

\[
\operatorname{osc}(q)
=q_d-q_D
=
\frac{\beta(D-d)}{(1+\beta d)(1+\beta D)}.
\tag{7.5}
\]

Combining (5.3), (7.4) and (7.5) proves:

### Theorem 7.1 — selected-child threshold remains favorably monotone under an explicit support-ratio condition

A sufficient quenched condition for

\[
\boxed{\bar q_{\rm esc}'(\beta)<0}
\tag{7.6}
\]

for **every deterministic tree with offspring in `[d,D]`** is

\[
\boxed{
4D(1+\beta d)(\beta d-1)(\beta D-1)
>
\beta(D-d)^2(1+\beta D).
}
\tag{7.7}
\]

Writing

\[
x=\beta d>1,
\qquad
\kappa=D/d,
\tag{7.8}
\]

this becomes the dimensionless criterion

\[
\boxed{
4\kappa(1+x)(x-1)(\kappa x-1)
>
 x(\kappa-1)^2(1+\kappa x).
}
\tag{7.9}
\]

This is a **component theorem**: it proves monotonicity of the expected one-step parent threshold along the terminal escape child selected by the decisive skeleton. It is not a theorem about the asymptotic speed.

For support `{2,3}` (`kappa=3/2`), (7.7) reduces to

\[
144\beta^3-51\beta^2-37\beta+12>0,
\tag{7.10}
\]

whose relevant root is

\[
\boxed{\beta_*=0.545077030676670\ldots .}
\tag{7.11}
\]

Therefore for **every** offspring law supported on `{2,3}` and, more strongly, every deterministic tree with degrees in `{2,3}`, the selected-child parent threshold decreases for all

\[
\boxed{\beta>0.545077030676670\ldots .}
\tag{7.12}
\]

This is well below the old high-bias scale and is genuinely about the harmonic/escape-selected environment, but it remains only one local derivative component.

For comparison, the dimensionless threshold `x=beta d` from (7.9) is approximately

- `1.09015406135` for `D/d=1.5`;
- `1.16814412955` for `D/d=2`;
- `1.31785670845` for `D/d=3`.

These numbers are exact consequences of the support-only certificate, not simulations.

---

## 8. What this rules out and what remains

### New positive information

The descendant side of the coupling is now organized into three pieces with rigorous direction:

1. **returned-loop count:** decreases with outward bias for `beta d>1`;
2. **decisive parent-vs-outward direction:** parent probability decreases with outward bias;
3. **terminal outward child identity:** the only residual non-monotone descendant mismatch, with derivative-scale coupling cost at most `Delta_{d,D}(beta)/(4 beta)` and finite-bias cost (5.7).

The new escape-spine representation also shows that terminal-selection sensitivity is a discounted return Green function along the harmonic escape ray, not an arbitrary recursive Fisher term.

### Rigorous obstruction / limitation

The factor `Delta_{d,D}` blows up as `beta d downarrow1`, and the previous `1416Z` report gave an exact annealed short-loop reversal in the larger source-transient region `1/EZ<beta<1/d`. Thus this particular monotone descendant-skeleton architecture **cannot** by itself cover the entire LPP interval when `d<EZ`; below `1/d` returned loops need not decrease. This is consistent with, and complementary to, P03-A's separate critical-edge analysis near `beta=1/EZ`.

Even for `beta d>1`, Theorem 6.1 does not yet compare complete regeneration times. The terminal child mismatch changes the law of the future escape-selected environment, and parent-side revisits to already selected ancestors remain outside the one-vertex descendant skeleton.

---

## 9. Next attack

The next probabilistic target is now precise and nonrecursive.

1. Work under the coarse coupling of Theorem 6.1 at each fresh frontier vertex.
2. Charge a terminal child mismatch only once, at the first decisive outward escape, using (5.9).
3. Follow the resulting harmonic escape spine. The score increment at one spine transition is exactly

\[
\xi_x=g_{Y_1}-E_{\pi_x}g_{Y_1},
\tag{9.1}
\]

with

\[
E(\xi_x\mid x)=0,
\qquad
E(\xi_x^2\mid x)\le \frac14\Delta_{d,D}(\beta)^2.
\tag{9.2}
\]

Thus successive terminal-selection scores form martingale differences under quenched harmonic measure. The next run should combine their orthogonality with the existing selected-ancestor/common-spine return bounds to obtain an `O(epsilon)` regeneration-time mismatch whose constant is explicitly proportional to `Delta_{d,D}`.

A particularly useful first test is the `{2,3}` family for `beta>0.545077...`, where Theorem 7.1 already proves the terminal selected degree has the favorable local derivative sign. If the remaining regeneration-time covariance is also dominated there, this would produce a genuinely new bounded-support monotonicity interval component beyond a purely high-bias argument. If that fails, construct an exact positive-probability multi-vertex cylinder identifying whether the failure is caused by harmonic-spine selection or parent-side ancestor transport.

---

## 10. Obligation ledger

- **Full-source LPP conjecture:** OPEN.
- **Source convention / inverse-bias hazard:** CHECKED and fixed.
- **Returned descendant blocks for `beta d>1`:** CONTROLLED by prior P03-B block contraction.
- **Return elasticity:** NEW sharp support band `1/(beta D-1) <= g <= 1/(beta d-1)`.
- **Terminal child-selection derivative:** NEW heterogeneity-only covariance/Fisher/TV bounds.
- **One-vertex coarse descendant skeleton:** NEW monotone coupling except for explicitly bounded terminal child mismatch.
- **Harmonic selected-child one-step threshold:** NEW explicit sufficient monotonicity criterion (7.9), including all `{2,3}` trees for `beta>0.545077030676670...`.
- **Parent-side selected-ancestor transport:** still open; use earlier common-spine/ancestor-stack lemmas.
- **Critical gap `1/EZ<beta<=1/d`:** monotone returned-loop architecture is unavailable in general; P03-A critical-edge results are complementary, not overwritten.

**Fixed source metric:** `R_full: 1 -> 1`.

**Intermediate progress:** terminal child-selection uncertainty changed from an uncontrolled branch covariance to an explicit escape-spine martingale with sharp heterogeneity width `Delta_{d,D}` and a complete coarse coupling theorem.
