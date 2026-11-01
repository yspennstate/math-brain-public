Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on H0008: `I_mf = a_hi-a_lo -> same`; this is the third consecutive unchanged H0008 run after the preceding certification movement. Methods actually used: #9 RANDOMIZE, #16 COMPUTE EVERY SMALL CASE, #27 SWAP THE QUANTIFIERS.**

# R14 HARD OUTSIDE — H0008 harmonic measure: an exact Palm transfer operator and a subcritical pipe Jacobian

## 0. Continuity, ownership, metric, and status

This run preserves all prior R14 hard-task handoffs. I do **not** reopen the original negative-margin spherical-perceptron target, H0017, D0036, D0039, or D0034. The active exclusive R14 HARD OUTSIDE claim remains `operations/claims/H0008.md`.

The source is Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3, open problem (6), **Boundary fluctuations**. The source asks for the multifractal spectrum of transmission-weighted flows and the harmonic measure of the failed cluster, where a dimension drop is expected.

The frozen metric remains

\[
I_{\rm mf}=a_{\rm hi}-a_{\rm lo},
\]

the exact maximal interval length already certified for the finite-type multifractal clause. The present work attacks the remaining harmonic-measure clause and cannot enlarge an already maximal multifractal interval. Therefore the honest metric entry is **NO MOVEMENT**.

This is the **third consecutive unchanged H0008 metric run** after the certification movement. Under Section I of `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the **next R14 invocation must be a thinking-only STUCK-RECOVERY-1/2 report with no new theorem claims**. This report does not pre-empt that mandatory next step.

Status after this run: **PARTIAL / SOURCE OPEN**. The new result is an exact reduction of the missing harmonic-stationarity problem from the full rooted-tree space to a finite vector of scalar conductance-density equations. A second theorem identifies the entire `one infinite child / no infinite sibling` channel with the transpose of the extinction Jacobian and proves that channel strictly subcritical. The remaining obstruction is a positive fixed point for the branch-producing part of the conductance transfer operator; I do **not** claim it is solved.

## 1. Required repository and current-source read

Before research I read or scoped:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/claims/H0008.md`;
- the newest R14 report `runs/R14/2026-09-19T06-50-28Z_h0008_pf_kl_harmonic_reduction_f31a.md`;
- repository-wide H0008 ownership/neighbor searches.

The canonical claim is still exclusively R14-owned, HARD OUTSIDE, SOURCE-OPEN. No release, reassignment, posting exclusion, or competing mathematical owner was found.

Fresh primary-source check on 19 September 2026:

- `https://arxiv.org/abs/2608.15987` is still v1, submitted 17 Aug 2026;
- the HTML source, Section 12.3 item (6), still says that the unresolved boundary-fluctuation theory consists of the multifractal spectrum and **the harmonic measure of the cluster itself, where the dimension drop should reappear**;
- the source Appendix D still gives the finite-type offspring law used below: conditional on the UGW forward count, child types are iid with law `q` and are independently thinned by `Bernoulli(p_ij)` transmissions;
- bounded fresh searches for `multitype Galton-Watson harmonic measure invariant measure`, `multitype harmonic exit environment`, and neighboring phrases did not locate a later theorem resolving this exact clause. This is bounded negative search evidence, not a novelty certificate.

Relevant prior art checked again:

- P. Rousselin, arXiv:1708.06965 / EJP 2018, constructs explicit invariant measures for a class of flow rules on one-type marked Galton-Watson trees and applies them to harmonic dimension;
- A. Dembo and N. Sun, arXiv:1011.4056, construct an explicit reversing measure for biased random walk on finite-type MGW at critical bias and prove multitype conductance estimates;
- S. Altok, arXiv:1307.5962 / Bernoulli 2013, characterizes reversible multitype GW measures for simple random walk under a different rerooting setup.

Those results support the invariant-environment strategy but do not directly supply the transient harmonic-descendant fixed point derived below.

## 2. Source law and the exact remaining gate from the preceding run

Let the finite type set be `D={1,...,d}`. Write

\[
q_j>0,\qquad \sum_j q_j=1,
\]

and let `nu` be the common potential-child count in the source finite-type reduction. Put

\[
G(z):=\mathbb E[z^\nu],\qquad m_*:=G'(1)=\mathbb E\nu.
\]

For a parent of type `i`, every one of its `nu` potential slots independently:

1. receives a child type `J` with law `q`;
2. is transmitted with indicator `A\sim Bernoulli(p_{iJ})`;
3. if transmitted, carries an independent descendant tree with the source law `P_J`.

Thus

\[
M_{ij}=m_*q_jp_{ij}.
\tag{2.1}
\]

Assume the source finite-type hypotheses used in the preceding reports: finite `D`, `q_j>0`, `p_{ij}>0`, irreducible `M`, and

\[
\rho:=\rho(M)>1.
\]

For an unconditioned descendant tree `T\sim P_i`, define `B(T)=0` on extinction and, on survival, let `B(T)` be the probability that simple random walk started at the root never hits an added parent. If the transmitted child subtrees are `T_u`, put `B_u=B(T_u)` and

\[
S(T):=\sum_u B_u.
\]

The electrical recursion from the earlier R14 run is

\[
B(T)=\frac{S(T)}{1+S(T)},
\tag{2.2}
\]

and the harmonic child split is

\[
H_T(u)=\frac{B_u}{S(T)}
\qquad (S(T)>0).
\tag{2.3}
\]

The preceding run proved a PF--KL identity: once an ergodic stationary law for the descendant environment under (2.3) exists, equivalent to the source survival law and with the needed integrability, the harmonic dimension equals `log rho` minus a mean KL divergence from the Perron limit-uniform flow. It also proved that this KL divergence can vanish source-a.s. only for the deterministic regular no-thinning case. Thus the exact remaining gate was

\[
\boxed{\texttt{HARM-STATIONARY-MTGW}.}
\]

This run changes the *form* of that gate substantially.

## 3. Method #9 — RANDOMIZE: Palm a distinguished potential child

The full rooted-tree state is unnecessary for the one-step stationarity calculation. Randomizing which potential child slot is the harmonic descendant closes the Radon--Nikodym calculation on only two pieces of data:

\[
(\text{root type},\ B(T)).
\]

For a vector of measurable nonnegative functions

\[
h=(h_i)_{i\in D},\qquad h_i:[0,1]\to[0,\infty),\qquad h_i(0)=0,
\]

define a finite measure on rooted typed trees by

\[
\Lambda_h(f)
:=\sum_i \mathbb E_i\big[h_i(B(T))f(i,T)\big].
\tag{3.1}
\]

The condition `h_i(0)=0` removes extinct trees. The masses of the type components are encoded inside `h`; no separate root-type prior is needed.

Let `K_H` be the harmonic descendant kernel,

\[
(K_Hf)(i,T)
=\sum_u \frac{B_u}{S(T)}f(\tau(u),T_u)
\qquad\text{on }S(T)>0.
\tag{3.2}
\]

Now size-bias the **potential** offspring number:

\[
\mathbb P(\widehat\nu=n)
=\frac{n\,\mathbb P(\nu=n)}{m_*}.
\tag{3.3}
\]

For a fixed parent type `i`, after distinguishing potential slot 1, let the remaining `\widehat\nu-1` slots be generated from the original source law and set

\[
R_i
:=\sum_{r=2}^{\widehat\nu} A_r B(T_r).
\tag{3.4}
\]

`R_i` is the total escape conductance supplied by all siblings of the distinguished potential child.

### Theorem R14-H0008-07A — exact Palm conductance transfer operator

For every finite `Lambda_h`, the push-forward `Lambda_h K_H` is again in the same conductance-density class:

\[
\boxed{\Lambda_h K_H=\Lambda_{\mathcal L h},}
\tag{3.5}
\]

where, for `b>0`,

\[
\boxed{
(\mathcal Lh)_j(b)
=
 m_* q_j b\sum_i p_{ij}\,
 \mathbb E\!\left[
 \frac{
 h_i\!\left(\dfrac{b+R_i}{1+b+R_i}\right)
 }{b+R_i}
 \right],
}
\tag{3.6}
\]

and `(Lh)_j(0)=0`.

Moreover `L` is positive, linear, and exactly mass-preserving:

\[
\sum_j\mathbb E_j[(\mathcal Lh)_j(B)]
=
\sum_i\mathbb E_i[h_i(B)].
\tag{3.7}
\]

Consequently, a normalized nonnegative solution

\[
\boxed{\mathcal Lh=h}
\tag{3.8}
\]

produces a harmonic-descendant stationary law. If in addition

\[
h_i(b)>0\quad\text{for }P_i\text{-a.e. }b>0\text{ and every }i,
\tag{3.9}
\]

then that stationary law is equivalent, type by type, to the source law conditioned on survival. Thus (3.8), plus the integrability required in the previous PF--KL theorem, is sufficient to close the remaining harmonic dimension-drop clause.

Conversely, every harmonic-stationary law whose Radon--Nikodym derivative with respect to the source laws depends only on `(type,B)` gives a fixed point of (3.8).

### Proof

Start from the left side of (3.5). Under `P_i`, write the potential slots as

\[
(J_r,A_r,T_r),\qquad r=1,\dots,\nu,
\]

where `J_r\sim q`, `A_r|J_r\sim Bernoulli(p_{iJ_r})`, and `T_r|J_r\sim P_{J_r}`, independently over `r`. Put

\[
S=\sum_{r=1}^{\nu}A_rB(T_r).
\]

Then, since `h_i(0)=0`, the contribution of `S=0` vanishes and

\[
\begin{aligned}
(\Lambda_hK_H)(f)
&=\sum_i\mathbb E_i\left[
 h_i\!\left(\frac{S}{1+S}\right)
 \sum_{r=1}^{\nu}
 \frac{A_rB(T_r)}{S}
 f(J_r,T_r)
 \right].
\end{aligned}
\tag{3.10}
\]

Exchangeability of the potential slots gives

\[
\sum_i\mathbb E_i\left[
 \nu\,
 h_i\!\left(\frac{S}{1+S}\right)
 \frac{A_1B(T_1)}{S}
 f(J_1,T_1)
 \right].
\tag{3.11}
\]

Use (3.3) to absorb the factor `nu`. Conditional on `J_1=j`, `A_1=1`, and `T_1=T`, set `b=B(T)`. The remaining sum is exactly `R_i` from (3.4), so `S=b+R_i`. Thus (3.11) equals

\[
\sum_{i,j}m_*q_jp_{ij}\,
\mathbb E_{T\sim P_j}\left[
 f(j,T)\,B(T)\,
 \mathbb E\left[
 \frac{h_i\!\left(\dfrac{B(T)+R_i}{1+B(T)+R_i}\right)}{B(T)+R_i}
 \right]
\right].
\tag{3.12}
\]

Collecting the sum over `i` gives exactly `Lambda_{Lh}(f)` with (3.6).

Taking `f=1`, `K_H1=1` on survival. Since `Lambda_h` is supported on survival by `h_i(0)=0`,

\[
(\Lambda_hK_H)(1)=\Lambda_h(1),
\]

which is (3.7). Positivity and linearity are manifest in (3.6). A normalized fixed point therefore makes `Lambda_h` stationary. Strict positivity (3.9) gives equivalence to the survival law on every type component. The converse inside this density class follows by uniqueness of Radon--Nikodym derivatives in (3.5). `square`

### Why (3.6) matters

The old remaining obligation was an invariant probability measure on an infinite-dimensional rooted-tree space. The new exact obligation is a **finite vector of scalar integral equations on `[0,1]`**. No approximation has entered:

\[
\boxed{
\texttt{HARM-STATIONARY-MTGW}
\quad\Longleftarrow\quad
\exists h>0:\ \mathcal Lh=h.
}
\tag{3.13}
\]

This is the main quantifier swap of the run: instead of proving stationarity against every tree test function directly, solve one positive fixed-point equation whose validity automatically gives stationarity against every test function.

## 4. Method #16 — COMPUTE EVERY SMALL CASE: the one-lineage channel is exactly the extinction Jacobian

The transfer operator has one obvious possible source of noncompact behavior: arbitrarily long stretches along which the harmonic ray is the **only infinite child**. The source law lets us compute that channel exactly.

Let

\[
e_i:=P_i(B=0),\qquad s_i:=1-e_i>0.
\]

The failed-process offspring generating map is

\[
F_i(z_1,\dots,z_d)
=G\!\left(1-\sum_j q_jp_{ij}(1-z_j)\right),
\tag{4.1}
\]

and `e=F(e)`. Define

\[
t_i:=\sum_jq_jp_{ij}s_j.
\tag{4.2}
\]

Thus one potential slot of a type-`i` parent carries an **infinite** transmitted child with probability `t_i`.

The extinction Jacobian is

\[
J:=DF(e),\qquad
J_{ij}=G'(1-t_i)q_jp_{ij}.
\tag{4.3}
\]

Under the size-biased law (3.3), the probability that none of the siblings of the distinguished child is infinite is

\[
\begin{aligned}
c_i
&:=P(R_i=0)\\
&=\mathbb E\big[(1-t_i)^{\widehat\nu-1}\big]\\
&=\frac{G'(1-t_i)}{m_*}.
\end{aligned}
\tag{4.4}
\]

Therefore the `R_i=0` part of (3.6) is

\[
\boxed{
(\mathcal L_0h)_j(b)
=\sum_iJ_{ij}\,
 h_i\!\left(\frac{b}{1+b}\right)
=\big[J^T h(b/(1+b))\big]_j.
}
\tag{4.5}
\]

So the entire sole-infinite-lineage transfer is **exactly the transpose extinction Jacobian**, followed only by the deterministic electrical map `b -> b/(1+b)`.

### Theorem R14-H0008-07B — strict subcriticality of the pipe channel

Under the source assumptions above,

\[
\boxed{\rho(J)<1.}
\tag{4.6}
\]

In fact, if `s=1-e`, then

\[
Js<s
\qquad\text{componentwise}.
\tag{4.7}
\]

Consequently the probability that a surviving type-`i` genealogy begins with `n` consecutive vertices each having exactly one infinite child is

\[
\boxed{(J^ns)_i,}
\tag{4.8}
\]

which decays exponentially in `n`.

#### Proof

First, `rho(M)>1` implies `m_*=E nu>1`, since every row sum of `M` is at most `m_*`. Hence `P(nu>=2)>0`, so `G` is strictly convex on every nontrivial interval in `[0,1]`. Irreducibility and supercriticality give `s_j>0` for all `j`, and strict positivity of `q_j,p_ij` gives `t_i>0` for every `i`.

Using `e=F(e)`,

\[
s_i=1-G(1-t_i).
\tag{4.9}
\]

On the other hand,

\[
(Js)_i=G'(1-t_i)t_i.
\tag{4.10}
\]

Strict convexity gives the strict tangent inequality

\[
G(1)>G(1-t_i)+G'(1-t_i)t_i.
\tag{4.11}
\]

Since `G(1)=1`, (4.9)--(4.11) give `(Js)_i<s_i` for every `i`. Because `s>0`, the Collatz--Wielandt bound yields `rho(J)<1`.

For (4.8), let `v_n(i)` be the probability that from a type-`i` root there is an infinite descendant and, along the unique infinite descendant line, the first `n` roots each have exactly one infinite child. At depth zero, `v_0=s`. If the unique infinite child has type `j`, one potential slot must generate the required type-`j` continuation while every other slot must fail to produce an infinite child. Differentiating the offspring pgf at `e` is exactly this distinguished-child count, so

\[
v_{n+1}=Jv_n.
\]

Thus `v_n=J^ns`. Since `rho(J)<1`, finite-dimensional Perron--Frobenius theory gives exponential decay. `square`

### Interpretation

This removes a concrete failure mode. A hypothetical harmonic stationary density does **not** need to fight a critical or supercritical one-child pipe process: that channel is automatically strictly subcritical, and its matrix is not mysterious — it is the extinction Jacobian already present in standard multitype branching theory.

On bounded vector densities, (4.5) and `rho(J)<1` also imply that `I-L_0` has a convergent Neumann inverse in a suitable weighted sup norm. Hence, for bounded candidate densities, the stationary equation can be rewritten as

\[
h=(I-\mathcal L_0)^{-1}\mathcal L_+h,
\qquad
\mathcal L_+:=\mathcal L-\mathcal L_0,
\tag{4.12}
\]

where `L_+` is exactly the part with at least one **other** infinite sibling. I do **not** promote (4.12) to an existence theorem on the full `L^1` cone: the remaining branch-producing operator can still concentrate density and need not be compact.

This is the certified obstruction produced by the run: **single-lineage pipes are not the missing stationarity obstruction; the only unresolved mechanism is the branch-producing conductance transfer.**

## 5. Method #16 continued — exact small-case consistency checks

These checks are algebraic consequences of the theorem, not numerical evidence.

### 5.1 One type

For `D={1}`, (3.6) becomes one scalar equation

\[
(\mathcal Lh)(b)
=m_*p\,b\,
\mathbb E\left[
\frac{h((b+R)/(1+b+R))}{b+R}
\right].
\tag{5.1}
\]

The `R=0` coefficient is

\[
G'(1-ps),
\tag{5.2}
\]

which is the derivative of the scalar extinction map at its minimal fixed point. This is exactly the scalar invariant-density architecture expected from the one-type Galton--Watson harmonic-flow literature. I do not claim Rousselin's notation or hypotheses are literally identical; the point is that the multitype formula reduces to the known one-dimensional fixed-point structure rather than producing a new tree-space object.

### 5.2 The exact one-block lumpable source slice from the preceding report

Assume

\[
\bar p_i:=\sum_jq_jp_{ij}=c
\qquad\text{for every }i.
\tag{5.3}
\]

The type-erased failed genealogy is then an ordinary one-type GW tree: each potential child is retained with probability `c`, independently. In particular the conductance law `P_i\circ B^{-1}` is the same for every root type and the sibling sum `R_i` in (3.4) has one common law `R`.

Let `kappa(b)` be any scalar fixed-point density for the corresponding one-type harmonic flow, so

\[
\kappa(b)
=m_*c\,b\,
\mathbb E\left[
\frac{\kappa((b+R)/(1+b+R))}{b+R}
\right].
\tag{5.4}
\]

Define the positive stochastic matrix

\[
Q_{ij}:=\frac{q_jp_{ij}}{c},
\qquad \sum_jQ_{ij}=1,
\tag{5.5}
\]

and let `a` be its stationary row vector, `a=aQ`. Then

\[
\boxed{h_i(b):=a_i\kappa(b)}
\tag{5.6}
\]

solves the full multitype equation (3.8). Indeed,

\[
\begin{aligned}
(\mathcal Lh)_j(b)
&=m_*q_jb\sum_i p_{ij}a_i
\mathbb E\left[
\frac{\kappa((b+R)/(1+b+R))}{b+R}
\right]\\
&=\frac{q_j\sum_i a_ip_{ij}}{c}\,\kappa(b)
=(aQ)_j\kappa(b)
=a_j\kappa(b).
\end{aligned}
\tag{5.7}
\]

Thus the new operator exactly recovers the previously solved type-lumpable family and identifies the stationary type bias as the stationary distribution of `Q`.

### 5.3 Deterministic regular no-thinning endpoint

If `nu equiv k>=2` and every `p_ij=1`, the type-erased tree is deterministic `k`-ary. Its escape conductance satisfies

\[
b=\frac{kb}{1+kb},
\]

so

\[
b=\frac{k-1}{k}.
\tag{5.8}
\]

The harmonic split is exactly uniform over the `k` children, agreeing with the PF limit-uniform flow. This is precisely the equality class isolated in the preceding R14 rigidity theorem. Thus the transfer-operator reduction also lands correctly on the sole no-dimension-drop source case.

No finite-enumeration claim was introduced in this section, so no checker-only artifact was manufactured.

## 6. Method #27 — SWAP THE QUANTIFIERS: the remaining theorem is now a scalar fixed-point existence problem

Before this run the remaining statement was:

> construct an invariant probability law on an infinite-dimensional space of surviving rooted typed trees for the harmonic descendant shift, prove equivalence to the source survival law, and verify the entropy integrability needed by the PF--KL theorem.

After Theorems 07A--07B, a sufficient route is:

> find a normalized positive vector function `h=(h_i)` on the **scalar conductance interval** `[0,1]` satisfying `Lh=h`, prove `h_i>0` on the positive-conductance support and the required logarithmic integrability, then invoke the already-proved PF--KL and rigidity theorems.

In displayed form, the exact blocker is now

\[
\boxed{
 h_j(b)
 =m_*q_jb\sum_i p_{ij}
 \mathbb E\!\left[
 \frac{h_i((b+R_i)/(1+b+R_i))}{b+R_i}
 \right],
 \quad b>0,
}
\tag{6.1}
\]

with

\[
h_i>0,\qquad
0<\sum_i\mathbb E_i[h_i(B)]<\infty,
\tag{6.2}
\]

plus the logarithmic integrability from the PF--KL theorem.

The part of (6.1) with `R_i=0` is already spectrally harmless by (4.6). Therefore any future proof has to control the `R_i>0` branch-producing term, i.e. a positive integral/composition operator generated when the harmonic ray has at least one other infinite sibling.

This is substantially narrower than the old gate, but it is not yet source closure.

## 7. Why I am not claiming the final fixed point

A tempting but invalid last step would be:

1. `L` is positive and mass-preserving;
2. therefore `L` has a positive `L^1` fixed density.

That inference is false for general positive Markov/Perron operators: mass preservation alone does not give an absolutely continuous invariant density. One needs compactness, uniform integrability/mean compactness of Cesaro iterates, a Harris/Doeblin mechanism, or some other positive-recurrence input. The source itself warns that compactness is the wrong generic infinite-dimensional mechanism in its boundary-fluctuation discussion.

The new decomposition shows precisely where such an input is needed. Long one-child pipes are exponentially subcritical because their transfer matrix is `J^T`; the unresolved operator is the one generated by actual branching points. A proof would now have to establish one of the following without silently assuming it:

- uniform integrability of a normalized Cesaro family for `L`;
- an explicit invariant density generalizing the one-type formula;
- a regeneration/minorization argument for the branch-producing conductance kernel;
- or a different stationary construction whose Radon--Nikodym derivative can then be identified with a fixed point of (6.1).

The bounded literature search found related one-type invariant-flow and multitype reversible-walk constructions, but no theorem that directly supplies this exact fixed point for the source harmonic descendant kernel.

## 8. Status relative to the source

What is now on file for H0008:

1. the pressure normalization was corrected from the ambient potential tree to the failed genealogy;
2. the full finite-type multifractal spectrum was proved throughout the finite positive-free-energy phase;
3. zero-temperature endpoints were identified by critical cycle means and critical-edge Perron growth, completing the frozen multifractal interval `I_mf=a_hi-a_lo`;
4. the harmonic flow was reduced electrically to descendant escape conductances;
5. exact one-type and exact type-lumpable source slices have strict dimension drop by classical one-type theory;
6. a general PF--KL identity reduces dimension drop to existence of a harmonic stationary environment plus a KL term;
7. the source equality case `H=U` was classified as exactly the deterministic regular no-thinning model;
8. **this run:** the stationarity gate was compressed exactly to (6.1), and the sole-infinite-lineage channel was proved strictly subcritical through the extinction Jacobian.

The source remains **OPEN / PARTIAL** because the positive fixed point of (6.1) has not been constructed in the general finite-type source law and the campaign's closure audits have therefore not begun.

## 9. Stagnation consequence and mandatory next-run protocol

The frozen metric history after its last certification movement is now:

- 2026-09-19T05-52-24Z: unchanged;
- 2026-09-19T06-50-28Z: unchanged;
- **this run:** unchanged.

Hence H0008 is now **STUCK by the campaign's metric rule**, even though the mathematical obstruction was sharpened.

The next R14 invocation must be **STUCK-RECOVERY-1/2, thinking-only, no new theorem claims**, and must include all five required items:

(a) the blocker in one displayed formula — use (6.1)--(6.2);

(b) every route already tried and the precise reason each failed;

(c) what a proof must contain that none of those routes contains;

(d) the simplest still-unproved special case;

(e) the nearest solved problem in the literature and the ingredient it has that the multitype source lacks.

That next report must then choose exactly one Section-I action and name a fresh three-move Section-B triple. Good unused candidates after this run are #7 TAKE THE LIMIT, #15 BREAK THE SYMMETRY ON PURPOSE, and #24 FIND THE EXTREMAL OBJECT, but the mandatory stuck report should choose only after re-reading the current repository and literature state.

## 10. Model/runtime control

The requested line `Model: GPT-6. Reasoning: maximum` remains prompt text only in the exposed scheduling/control surface. This run identifies itself from the actually available model context as **GPT-5.6 Sol**, with reasoning level **UNVERIFIED**. The repository ledger still records no binding scheduler model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed hour-long execution control.

The historical P26 `You cannot modify this task` event is an authorization-context issue, not a mathematical one. The legitimate workaround remains an owning/admin-authorized context or platform support. No permission bypass, duplicate schedule, or scheduler change was attempted in this run.

## 11. `ledger_delta`

```yaml
ledger_delta:
  worker: R14
  allocation: HARD_OUTSIDE
  active_target: H0008
  source: "Achyut Kumar, arXiv:2608.15987v1, Section 12.3 open problem (6), Boundary fluctuations"
  owner: R14
  source_status: OPEN_PARTIAL
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: UNVERIFIED
  metric:
    name: I_mf
    before: "a_hi-a_lo (exact maximal finite-type multifractal interval already certified)"
    after: "a_hi-a_lo"
    movement: NONE
    unchanged_streak_after_certification: 3
  methods_used: [9, 16, 27]
  new_results:
    - id: R14-H0008-07A
      status: PROVED_PARTIAL
      statement: "Harmonic descendant push-forward preserves the type/conductance Radon-Nikodym class and is exactly the positive mass-preserving operator L in equation (3.6); a positive normalized fixed point Lh=h supplies the missing stationary environment."
    - id: R14-H0008-07B
      status: PROVED_PARTIAL
      statement: "The R_i=0 / sole-infinite-lineage part of L equals J^T composed with b->b/(1+b), where J is the multitype extinction Jacobian; J s<s and rho(J)<1."
    - id: R14-H0008-07C
      status: PROVED_PARTIAL
      statement: "The probability of n consecutive sole-infinite-child generations from type i is exactly (J^n s)_i and therefore decays exponentially."
    - id: R14-H0008-07D
      status: CONSISTENCY_CHECK
      statement: "On the exact one-block lumpable slice, the fixed point factors as h_i(b)=a_i kappa(b), where a is stationary for Q_ij=q_j p_ij/c and kappa is the one-type harmonic fixed-point density."
  remaining_obligation: "Construct a positive normalized fixed point of the scalar conductance transfer equation (6.1), with equivalence and PF-KL integrability; the only unresolved operator channel is R_i>0 (actual branching)."
  novelty: UNVERIFIED
  checker: "none; theorem-sized arguments are proved on the page and no finite enumeration claim was introduced"
  stuck_state: "TRIGGERED: next invocation must be STUCK-RECOVERY-1/2 thinking-only"
  next_run_rule: "No new theorem claims; execute Section-I stuck report before any further H0008 mathematics."
```
