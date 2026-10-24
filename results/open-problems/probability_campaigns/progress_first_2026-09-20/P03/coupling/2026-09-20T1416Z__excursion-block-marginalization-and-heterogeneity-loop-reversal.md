Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum reasoning was requested as a preference, but no authenticated runtime telemetry establishes that setting.

# P03-B coupling report — excursion-block marginalization and heterogeneity loop reversal

**Status:** PROVED PARTIAL / NEW EXACT EXCURSION-BLOCK LEMMA / NEW SOURCE-VALID ANNEALED OBSTRUCTION. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains open.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling, spine comparison and source-valid counterexample role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `0c2914d342e370155cf4857a9fe6cbe42cef3b65`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T1320Z__uniform-child-loop-contraction-and-recursive-selection.md`.

**Complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1308Z__uniform-scaled-terminal-strip-for-bounded-support-and-explicit-K3.md`. P03-A is developing recursive escape/speed identities and a terminal strip near the critical bias. This report stays on excursion blocks, coupling and source-valid probabilistic obstructions.

---

## 1. Source normalization and current primary benchmark

The primary source remains G. Ben Arous, A. Fribergh and V. Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865. Their parameter `beta` is the **outward child bias**. If a non-root vertex has `k` children,

\[
q_k(\beta):=P_\beta(\text{parent}\mid k)=\frac1{1+\beta k},
\qquad
P_\beta(\text{specified child}\mid k)=\frac\beta{1+\beta k}.
\tag{1.1}
\]

The offspring variable `Z` obeys `P(Z=0)=0`. The source transient regime is

\[
\beta>\frac1{E Z},
\tag{1.2}
\]

and the LPP conjecture asks that the asymptotic speed be increasing throughout that interval. The arXiv paper proves the historical high-bias result `beta>=717`, with the minimum-degree refinement `beta>=717/d`; this is retained only as source history, not treated as a new frontier.

Bowditch–Tokushige, arXiv:1906.07913, prove differentiability of the speed for parent-bias `lambda` in the ballistic/CLT range under an exponential offspring moment, with derivative represented by a Gaussian covariance; arXiv:2006.03433 proves analyticity in the ballistic regime. These are regularity tools, not sign theorems.

A fresh bounded source check on 20 September 2026 again found the broad later primary monotonicity result of H. Song, L. Wang and K. Xiang, *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias*, J. Appl. Probab. 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`. In their reciprocal **parent-bias** parameter `lambda=1/beta`, if the minimum offspring is `d>=2`, they prove strict decrease for

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.3}
\]

No inverse-parametrization contradiction is inferred. The bounded 2026 search did not surface a full-source resolution.

---

## 2. Inherited bottleneck and the change of filtration

The `1320Z` P03-B report proved that on a deterministic tree of minimum offspring `d`, throughout `beta d>1`, every **quenched returning child-excursion kernel** contracts with outward bias. For a vertex `v` with `k` children and child `u`, write

\[
h_u(\beta):=P_\beta^u(T_v<\infty),
\qquad
\ell_{v,u}(\beta):=\frac{\beta}{1+\beta k}h_u(\beta).
\tag{2.1}
\]

For `beta_2>beta_1>1/d`, that report proved

\[
\ell_{v,u}(\beta_2)
\le
R_d(\beta_1,\beta_2)\ell_{v,u}(\beta_1),
\tag{2.2}
\]

where

\[
R_d(\beta_1,\beta_2)
:=
\frac{\beta_2}{\beta_1}
\left(\frac{1+\beta_1d}{1+\beta_2d}\right)^2
<1.
\tag{2.3}
\]

At differentiability points,

\[
-\beta\,\partial_\beta\log\ell_{v,u}(\beta)
\ge
c_d(\beta):=\frac{\beta d-1}{\beta d+1}>0.
\tag{2.4}
\]

The same report then conditioned on the detailed internal history of an already explored child subtree. At that finer filtration, a posterior Fisher term of the form

\[
\frac{V}{2d}\sqrt{I_u}
\tag{2.5}
\]

appeared. The open question was whether this recursive score had to be propagated down the tree generation by generation.

The main point of the present run is that, for **complete returned descendant excursions**, the answer is no. The recursive Fisher term is a cost of conditioning too finely. If the entire returning excursion is marginalized before the coupling ledger is charged, all its internal posterior-selection scores recombine into the single quenched factor `h_u(beta)`, and (2.2) controls the whole block directly.

This does not solve the speed problem: terminal branch selection and parent-side history remain. But it removes one genuinely recursive piece of the descendant ledger.

The proof of (2.2) in fact only uses `d>=1` and `beta d>1`; the earlier report fixed `d>=2` to match the later source theorem. Below, the block statements are valid for any integer `d>=1` whenever `beta d>1`.

---

## 3. Exact excursion-block marginalization

Fix a deterministic rooted tree with minimum offspring at least `d>=1`, fix `beta d>1`, and let a non-root vertex `v` have children `u_1,...,u_k`, `k>=d`.

Set

\[
q_v:=\frac1{1+\beta k},
\qquad
\ell_i:=\frac\beta{1+\beta k}h_{u_i},
\qquad
 e_i:=\frac\beta{1+\beta k}(1-h_{u_i}).
\tag{3.1}
\]

Thus at a visit to `v` there are three kinds of coarse outcomes:

- step to the parent, probability `q_v`;
- step to child `u_i` and eventually return to `v`, probability `ell_i`;
- step to child `u_i` and never return to `v`, probability `e_i`.

They satisfy

\[
q_v+\sum_{i=1}^k(\ell_i+e_i)=1.
\tag{3.2}
\]

Let

\[
L:=\sum_i\ell_i.
\tag{3.3}
\]

### Theorem 3.1 — every complete returned-excursion word contracts multiplicatively

Fix `m>=1`. Let `W` be any collection of words

\[
w=(i_1,\ldots,i_m)\in\{1,\ldots,k\}^m
\]

whose membership is independent of `beta`. Starting from `v`, let `A_W(beta;T)` be the quenched probability that the first `m` coarse excursions are all returning child excursions and that their child-label word belongs to `W`.

Then

\[
\boxed{
A_W(\beta;T)
=
\sum_{w\in W}\prod_{j=1}^m\ell_{i_j}(\beta).
}
\tag{3.4}
\]

Consequently, for `beta_2>beta_1>1/d`,

\[
\boxed{
A_W(\beta_2;T)
\le
R_d(\beta_1,\beta_2)^m A_W(\beta_1;T).
}
\tag{3.5}
\]

The same inequality survives averaging over **any beta-independent law of trees**.

At differentiability points,

\[
\boxed{
-\beta\,\partial_\beta\log A_W(\beta;T)
\ge m\,c_d(\beta)
}
\tag{3.6}
\]

whenever `A_W>0`.

#### Proof

After a returned child excursion the walk is exactly back at `v`. The strong Markov property therefore gives the product in (3.4), including when the same child is used repeatedly. Equation (2.2) applies to each factor, so every degree-`m` monomial contracts by `R_d^m`; summing nonnegative monomials proves (3.5). Since the environment law is independent of `beta`, averaging preserves the pointwise inequality. Taking one-sided derivatives gives (3.6). `square`

### Corollary 3.2 — canonical discovery/equality patterns also contract

Suppose child labels are forgotten and one records only the equality pattern: for example `new,new,same-as-first,new,same-as-second`. Such an event is a union of labeled words of the same length. Therefore it obeys the same bound (3.5).

This point matters for the posterior filtration used in previous P03-B runs. The detailed internal path inside a previously discovered child may create a nontrivial posterior on its degree and subtree, but after one sums over **all internal histories that return to `v`**, their total likelihood is exactly `h_u(beta)`. Hence no separate recursive Fisher payment is needed for a completed returned excursion block.

The previous `sqrt(I_u)` term remains mathematically correct at the finer filtration; Theorem 3.1 shows that it should not be charged independently when the proof is reorganized at the excursion-block filtration.

### Corollary 3.3 — tail domination of the entire returned-descendant stack

Let `C_v` be the number of consecutive returning child excursions made from `v` before the first coarse outcome that is either a parent step or a nonreturning descendant escape. Then, quenched,

\[
P_\beta(C_v\ge m\mid T)=L(\beta)^m.
\tag{3.7}
\]

Thus

\[
P_{\beta_2}(C_v\ge m\mid T)
\le
R_d(\beta_1,\beta_2)^m
P_{\beta_1}(C_v\ge m\mid T).
\tag{3.8}
\]

The same stochastic tail comparison holds annealed. The full returned-descendant stack therefore shortens with outward bias throughout `beta d>1`, even after all internal subtree histories have been integrated out.

---

## 4. Exact decisive skeleton after deleting returned child excursions

The block filtration has a particularly simple terminal kernel.

Put

\[
S_v:=\sum_{i=1}^k(1-h_{u_i}).
\tag{4.1}
\]

Summing the geometric series over any number of returned child loops gives

\[
P_\beta(\text{decisive parent exit from }v\mid T)
=
\frac{q_v}{1-L}
=
\boxed{\frac1{1+\beta S_v}}.
\tag{4.2}
\]

The right-hand side is exactly the usual child-to-parent return recursion, so

\[
\boxed{
P_\beta(\text{decisive parent exit from }v\mid T)=h_v(\beta).
}
\tag{4.3}
\]

Similarly,

\[
\boxed{
P_\beta(\text{decisive nonreturn escape through }u_i\mid T)
=
\frac{\beta(1-h_{u_i})}{1+\beta S_v}.
}
\tag{4.4}
\]

Conditional on the decisive exit being outward, the chosen child has quenched law

\[
\boxed{
\pi_i(\beta;T)
=
\frac{1-h_{u_i}(\beta)}{S_v(\beta)}.
}
\tag{4.5}
\]

Thus the entire descendant side decomposes into two pieces:

1. the parent-versus-permanent-outward decision, whose parent probability is `h_v(beta)` and is already known to decrease with outward bias;
2. the **choice among outward children**, represented by `pi_i`.

All returned-child posterior recursion has disappeared from the coarse kernel. The only descendant selection still capable of carrying adverse covariance is the terminal child choice (4.5).

---

## 5. New nonbranching bound on terminal child-selection drift

The previous two-sided return-elasticity theorem gives, with

\[
r:=\frac1{\beta d}<1,
\tag{5.1}
\]

\[
\frac{h_i(1-h_i)}{\beta}
\le -h_i'
\le
\frac{h_i(1-h_i)}{\beta(1-r)}.
\tag{5.2}
\]

Define the logarithmic growth rate of the permanent-escape weight

\[
g_i
:=
\beta\,\partial_\beta\log(1-h_i)
=
-\frac{\beta h_i'}{1-h_i}.
\tag{5.3}
\]

Then

\[
\boxed{
h_i\le g_i\le\frac{h_i}{1-r}\le\frac1{\beta d-1}.}
\tag{5.4}
\]

Differentiating (4.5) gives the exact centered-score identity

\[
\boxed{
\beta\pi_i'
=
\pi_i(g_i-\bar g),
\qquad
\bar g:=\sum_j\pi_j g_j.
}
\tag{5.5}
\]

Therefore, if `F_i(beta)` is any continuation value attached to choosing child `u_i`,

\[
\boxed{
\beta\frac d{d\beta}\sum_i\pi_iF_i
=
\sum_i\pi_i\,\beta F_i'
+
\operatorname{Cov}_\pi(F,g).
}
\tag{5.6}
\]

The first term is physical evolution inside the chosen branch. The second term is the **entire child-selection debt** created at `v` by changing the bias.

By the weighted Gruss inequality and (5.4),

\[
\boxed{
|\operatorname{Cov}_\pi(F,g)|
\le
\frac{\operatorname{osc}(F)}{4(\beta d-1)}.
}
\tag{5.7}
\]

Equivalently, the infinitesimal total-variation motion of the terminal child law satisfies

\[
\boxed{
\frac12\sum_i|\pi_i'|
\le
\frac1{4\beta(\beta d-1)}.
}
\tag{5.8}
\]

This is a nonbranching replacement for the recursive `sqrt(I_u)` ledger from the previous run. It does **not** require propagating a Fisher term down every explored child. Once returned excursions are marginalized, the only descendant selection term at a vertex is a single covariance whose coefficient is explicit.

The cost necessarily deteriorates as `beta d downarrow1`; Section 7 below shows that this is not merely a weakness of the estimate.

---

## 6. New exact annealed obstruction: heterogeneity makes the shortest return loop increase near the transient edge

The block contraction above only applies when `beta d>1`. It is natural to ask whether one could extend the same mechanism annealed to the full transient interval `beta>1/EZ`.

There is a sharp obstruction even for the **shortest possible descendant loop**.

Let

\[
m:=EZ>1,
\qquad
\mu(\beta):=E\frac1{1+\beta Z}.
\tag{6.1}
\]

Start at a newly discovered non-root vertex `v` before its offspring and those of its children have been exposed. Let `A_2(beta)` be the annealed probability that the next step is outward to one of the children of `v` and that the following step returns immediately to `v`.

Because the offspring number at `v` and at the newly selected child are independent copies of `Z`,

\[
\boxed{
A_2(\beta)
=
E\left[\frac{\beta Z}{1+\beta Z}\right]
E\left[\frac1{1+\beta Z}\right]
=
\mu(\beta)(1-\mu(\beta)).
}
\tag{6.2}
\]

Moreover

\[
\mu'(\beta)
=-E\frac{Z}{(1+\beta Z)^2}<0,
\tag{6.3}
\]

so

\[
\boxed{
A_2'(\beta)
=
\mu'(\beta)(1-2\mu(\beta)).
}
\tag{6.4}
\]

Thus the shortest returned descendant loop becomes **more frequent** as outward bias increases whenever `mu(beta)>1/2`.

### Theorem 6.1 — a universal heterogeneity-reversal interval

Assume the offspring law is nondegenerate, has no leaves, and has finite mean `m>1`. Then

\[
\boxed{
\mu(1/m)-\frac12
=
E\frac{(Z-m)^2}{4m(m+Z)}>0.
}
\tag{6.5}
\]

If the minimum offspring is

\[
d:=\min\{k\ge1:P(Z=k)>0\},
\tag{6.6}
\]

then

\[
\mu(1/d)<\frac12.
\tag{6.7}
\]

Hence there is a unique

\[
\boxed{
\beta_*\in(1/m,1/d)
\quad\text{such that}\quad
\mu(\beta_*)=\frac12.
}
\tag{6.8}
\]

On the entire interval

\[
\boxed{
\frac1m<\beta<\beta_*,
}
\tag{6.9}
\]

the source-valid annealed two-step return-loop probability satisfies

\[
\boxed{A_2'(\beta)>0.}
\tag{6.10}
\]

It reaches its maximum `1/4` at `beta_*`, then decreases for `beta>beta_*`.

#### Proof of the critical Jensen gap

At `beta=1/m`,

\[
\mu(1/m)-\frac12
=E\left[\frac{m}{m+Z}-\frac12\right]
=E\frac{m-Z}{2(m+Z)}.
\]

Since `E(m-Z)=0`, subtract the constant `1/(4m)` inside the final factor:

\[
E\frac{m-Z}{2(m+Z)}
=
E\left[(m-Z)\left(\frac1{2(m+Z)}-\frac1{4m}\right)\right]
=
E\frac{(Z-m)^2}{4m(m+Z)}.
\]

This is strictly positive for a nondegenerate law. At `beta=1/d`, every `Z>=d` gives `(1+Z/d)^{-1}<=1/2`, with strict inequality on the positive-probability event `Z>d`. Since `mu` is strictly decreasing, (6.8) follows, and (6.4) gives the sign statement. `square`

### Explicit bounded-support width

If additionally `Z<=D`, then from (6.5)

\[
\mu(1/m)-\frac12
\ge
\frac{\operatorname{Var}(Z)}{4m(m+D)}.
\tag{6.11}
\]

Since `-mu'(beta)<=EZ=m`,

\[
\boxed{
\beta_*-\frac1m
\ge
\frac{\operatorname{Var}(Z)}{4m^2(m+D)}.
}
\tag{6.12}
\]

So the failure of loop suppression is not merely infinitesimal: every nondegenerate bounded-support law has an explicit positive-width interval above the source transience threshold on which the shortest annealed return loop increases with outward bias.

### Exact two-point family

For

\[
P(Z=d)=p,
\qquad
P(Z=D)=1-p,
\qquad d<D,
\tag{6.13}
\]

write `m=pd+(1-p)D`. Solving `mu(beta_*)=1/2` gives

\[
\boxed{
\beta_*
=
\frac{d+D-2m+\sqrt{(d+D-2m)^2+4dD}}{2dD}.
}
\tag{6.14}
\]

For the balanced law `P(Z=2)=P(Z=3)=1/2`,

\[
m=\frac52,
\qquad
\boxed{\beta_*=\frac1{\sqrt6}=0.408248\ldots}
\tag{6.15}
\]

whereas the transient edge is `1/m=2/5=0.4` and `1/d=1/2`. In fact

\[
\mu(2/5)=\frac{50}{99}>\frac12.
\]

Therefore the exact annealed probability of the immediate out-and-back loop **increases** throughout

\[
\boxed{
0.4<\beta<1/\sqrt6.
}
\tag{6.16}
\]

For a balanced `{d,D}` law in general, (6.14) simplifies to

\[
\boxed{\beta_*=\frac1{\sqrt{dD}}.}
\tag{6.17}
\]

This is not a counterexample to speed monotonicity. In fact the historical Einstein-relation result cited by Ben Arous–Fribergh–Sidoravicius gives monotonicity in a neighborhood of `1/m`. The point is more specific and important for coupling architecture: **speed can increase even while the frequency of the shortest returned descendant loop also increases**. Therefore a full proof cannot require all return-loop statistics to move monotonically in the favorable direction.

---

## 7. Sharp finite-cylinder obstruction to extending the pointwise loop theorem below `beta d=1`

The threshold `beta d>1` in the quenched loop-contraction theorem is structurally sharp.

Condition on the source-valid finite cylinder that a fresh non-root vertex `v` has exactly `d` children and that the child `u` selected on the next outward step also has exactly `d` children. The probability of the two-step path

\[
v\to u\to v
\]

conditional on these two local degrees is

\[
\boxed{
K_d(\beta)
=
\frac\beta{(1+\beta d)^2}.
}
\tag{7.1}
\]

Its derivative is

\[
\boxed{
K_d'(\beta)
=
\frac{1-\beta d}{(1+\beta d)^3}.
}
\tag{7.2}
\]

Hence

\[
K_d'(\beta)>0
\quad\Longleftrightarrow\quad
\beta d<1.
\tag{7.3}
\]

If `P(Z=d)>0`, this cylinder has strictly positive Galton–Watson probability. More generally, for parent degree `k` and child degree `j`, the corresponding two-step kernel is

\[
K_{k,j}(\beta)=\frac\beta{(1+\beta k)(1+\beta j)},
\]

and

\[
\operatorname{sign}K_{k,j}'(\beta)
=
\operatorname{sign}(1-\beta^2kj).
\tag{7.4}
\]

Thus no pointwise argument can extend Theorem 3.1's loop contraction through `beta d=1`: on actual positive-probability source cylinders, the sign really reverses below that threshold.

This explains why the critical-edge work of P03-A and the excursion-coupling work of P03-B require genuinely different mechanisms in the gap

\[
1/EZ<\beta\le1/d.
\tag{7.5}
\]

---

## 8. A second source-valid selection test: successful outward cylinders tilt toward thinner vertices

There is another exact local selection effect worth preserving because it identifies the direction of the remaining terminal child-choice covariance.

At a fresh vertex, condition on the event `E_2` that the walk makes two successive outward steps. Given that the intermediate child has degree `K=k`, the second outward step has probability

\[
a_k(\beta)=\frac{\beta k}{1+\beta k}.
\tag{8.1}
\]

Therefore, for a two-point offspring law `Z in {d,D}`, the posterior degree law of the intermediate vertex under `E_2` is

\[
P_\beta(K=k\mid E_2)
\propto
P(Z=k)a_k(\beta).
\tag{8.2}
\]

Writing the conditional probabilities as `pi_d,pi_D`,

\[
\frac{\pi_d}{\pi_D}
=
\frac{P(Z=d)}{P(Z=D)}
\frac{d(1+\beta D)}{D(1+\beta d)},
\tag{8.3}
\]

so

\[
\boxed{
\frac d{d\beta}\log\frac{\pi_d}{\pi_D}
=
\frac{D-d}{(1+\beta d)(1+\beta D)}>0.
}
\tag{8.4}
\]

Equivalently,

\[
\boxed{
\frac d{d\beta}E[K\mid E_2]
=
-\frac{(D-d)^2\pi_d\pi_D}
{(1+\beta d)(1+\beta D)}<0.
}
\tag{8.5}
\]

So increasing outward bias can make a successful outward cylinder select a **lower-degree** intermediate vertex more often. This is an exact positive-probability Galton–Watson cylinder, not a deterministic-tree thought experiment.

For the balanced `{2,3}` law at `beta=3/5`,

\[
\pi_2=\frac{28}{61},
\qquad
\pi_3=\frac{33}{61},
\qquad
E[K\mid E_2]=\frac{155}{61},
\]

and

\[
\boxed{
\frac d{d\beta}E[K\mid E_2]
=-\frac{150}{3721}<0.
}
\tag{8.6}
\]

Again this is not a speed counterexample. It is a rigorous warning that the surviving terminal branch-selection covariance in (5.6) need not have a favorable sign merely because the physical outward drift is stronger.

---

## 9. What changed in the proof architecture

The previous descendant ledger had three apparent difficulties:

1. one-shot fresh-child discovery debt;
2. repeated known-child physical returns;
3. recursively stored subtree posterior/Fisher information.

The `1320Z` report removed (2) physically but still left (3) as a recursive score. The present block marginalization removes the need to carry (3) **for complete returned child excursions**. All detailed internal histories that return are summed into `h_u(beta)`, and the whole returned block contracts by Theorem 3.1 when `beta d>1`.

After this reorganization, the descendant side has only:

- the terminal parent-versus-permanent-outward decision, already favorable because `h_v(beta)` decreases;
- the terminal child-choice covariance `Cov_pi(F,g)`, bounded nonrecursively by (5.7);
- in the interval `1/EZ<beta<=1/d`, a genuine loop-reversal mechanism that prevents pointwise contraction and must be compensated rather than denied.

The parent-side selected-ancestor/common-spine debt from earlier P03-B reports is unchanged and remains separate.

Theorem 6.1 is especially useful for coordination with P03-A: near the transient edge, any attempted probabilistic proof based on suppressing return loops is structurally impossible for nondegenerate laws, exactly where P03-A's critical analytic expansion is strongest.

---

## 10. Remaining obstruction and next attack

**Full-source metric:** unchanged. The Lyons–Pemantle–Peres conjecture remains open.

**New proved partial results:**

- complete returned-descendant excursion words can be marginalized and contract by an explicit factor `R_d^m` for every `beta d>1`; the recursive known-child Fisher term is not needed at this block filtration;
- the only remaining descendant branch-selection derivative at a fixed vertex is the single covariance (5.6), with deterministic bound (5.7);
- every nondegenerate source law has a rigorous interval immediately above `1/EZ` on which the annealed shortest out-and-back loop becomes **more** frequent as outward bias increases;
- the pointwise threshold `beta d=1` is sharp on positive-probability Galton–Watson cylinders.

**Remaining obstruction:** combine the terminal child-choice covariance with the parent-side selected-ancestor debt without paying a crude continuation oscillation large enough to erase the favorable decisive-drift margin. Below `beta d=1`, loop suppression is false, so a different compensation identity is required.

**Next attack in the `beta d>1` region:** rewrite the regeneration-gap derivative at the excursion-block filtration. Charge returned descendant blocks by Theorem 3.1, parent exits by the existing common-spine occupation bounds, and terminal child choice only once through `Cov_pi(F,g)`. For the bounded-support `{2,3}` family, insert the exact downcrossing clock from the earlier P03-B reports and target an explicit block inequality in which the continuation oscillation in (5.7) is replaced by the return-weighted difference between two child continuations.

**Next attack in the critical gap `1/EZ<beta<=1/d`:** do not try to resurrect loop contraction. Use the exact identity `A_2=mu(1-mu)` as the first delay term in a local renewal/time-change decomposition and pair `A_2' > 0` against the simultaneous increase in decisive outward displacement. The goal is a compensation lemma, not a sign lemma for each loop statistic.

No simulation is used for any theorem above.

---

## 11. Obligation ledger

- `P03-B-full-LPP`: **OPEN** — no full-source monotonicity claim.
- `P03-B-returned-child-physical-stack`: **PROVED PARTIAL** for `beta d>1`.
- `P03-B-returned-child-internal-selection`: **REDUCED** — disappears from the ledger after complete excursion-block marginalization; no separate recursive Fisher payment is needed for returned blocks.
- `P03-B-terminal-child-selection`: **OPEN BUT BOUNDED** by the single covariance (5.7).
- `P03-B-parent-side-selected-ancestor`: **OPEN**, with earlier stack/common-spine bounds preserved.
- `P03-B-critical-gap-loop-suppression`: **RIGOROUSLY OBSTRUCTED** — Theorem 6.1 and (7.2) show the loop statistic can move in the wrong direction on source-valid annealed and finite-cylinder tests.
- `P03-A-interface`: share Theorem 6.1 and the `beta_*` crossover; do not duplicate P03-A's recursive speed identities.

**ledger_delta:** one recursive descendant obligation is removed by changing to the exact excursion-block filtration; one near-critical obstruction is made exact and quantitative.