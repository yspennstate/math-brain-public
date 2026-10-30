# FOREST B02 r11 — source-correct homogenization and exact triangle q-tilt

Run: `20260922T060836Z-b02-forest-r11`  
Account/slot: `fleet02/B02`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Owner control: `2026-09-22.2`  
Outcome: **CANDIDATE_REFUTED** for the current rank-homogenized lead mechanism, plus an **ESSENTIAL_STEP_APPLIED** exact triangle-contraction reduction. The parent FOREST target remains **OPEN**. No novelty or public solved-problem claim is made.  
Context: `WITHOUT_VERIFIED_BRAIN`.

## Fresh controls and assignment

Fresh main was resolved before work and refreshed before substantive writes. The operative later owner instruction is research-only FOREST work; stale installation/benchmark language is superseded. Current control object identities used in this run:

- AGENTS blob `94387098453b9f4a9b10179183f6f6ec780fd987`;
- scheduled README blob `3d4a9372c87802ab734141a3374d04c8823372e3`;
- fleet blob `e647d5d2479749f80ce7bb4862bee0f28513c7d9`;
- roles blob `ed17ecc94f76720c0345b3e32249b791b20ec611`;
- PROTOCOL blob `83a9268bf5287ca203e4be69a79e25382397bca7`;
- collective ORDER blob `a70e03208ae00795ca7c6cdf9b7dbce854347138`;
- TARGETS blob `a8cafa98cdb074ed15d0e214f8f54ee514c500df`;
- ASSIGNMENTS blob `fe144a4be3522d57f8cb2dc40b1fc57df7c7fda`.


Exact B02 assignment: derive a source-valid polynomial/probabilistic comparison for uniform unrooted forests at unit edge weights and justify any log-concavity/Rayleigh input. Named partner: `fleet03/B03`. Campaign lead: `fleet01/B01`.

## Lead and peer consumed

I read lead run `20260922T050946Z-b01-forest-auto11`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, shared handoff blob `4cee205cb7d254caf785692838111988a0b8a155`. Its main new route is a triangle-free minimal-counterexample spectral budget plus a remaining `STAR-2` triangle-contraction debt. The lead invokes a rank-degree homogenization

\[
 h_R(y,\mathbf z)=\sum_{F\text{ forest}} y^{R-|F|}\mathbf z^F,
\]

where `R` is graphic rank, in order to replace the source ground-set slack by `R-E|F|`. That is the exact claim audited below.

I also consumed the newest named-partner result, `fleet03/B03` run `20260922T055815Z-fleet03-B03-forest-r12`, report blob `b0640c214b6bb7ae849b3ef46dd6feba888e79c0`. Its source-safe local theorem is the exact degree-three terminal-partition factorization

\[
\Delta(e_1,e_2)=4B_{12}T+(B_{13}+C)(B_{23}+C)\ge0
\]

for two unit star edges incident to a cubic vertex, with arbitrary positive weights elsewhere. I use this as a valid local boundary input. I do **not** import the partner's separate fixed-host globalization sentence, because the current lead and accessible source audit do not verify that stronger fixed-host implication.

## 1. Decisive source correction: ALOV homogenizes to ground-set size, not rank

For a matroid on `m` ground elements, Anari--Liu--Oveis Gharan--Vinzant prove complete log-concavity for

\[
 g_M(y,\mathbf z)=\sum_{I\in\mathcal I} y^{m-|I|}\mathbf z^I.
\]

In the graphic case the independent sets are exactly **all unrooted forests**, including the empty forest, disconnected forests, and every forest size. At the all-ones point this polynomial therefore represents the exact source unit law. The source also explicitly distinguishes spectral negative dependence from entrywise negative correlation; complete log-concavity by itself does not give the desired Rayleigh signs.

The current lead's rank-degree replacement is not covered by that theorem, and it actually fails log-concavity on the smallest cycle.

### Exact K3 counterexample to rank homogenization

For `K3`, graphic rank is `R=2`. The rank-degree polynomial is

\[
 h_R=y^2+y(z_1+z_2+z_3)+(z_1z_2+z_1z_3+z_2z_3).
\]

For a homogeneous positive polynomial at the all-ones point, if `U` is its exponent vector under monomial weights, then

\[
-\nabla^2\log h(\mathbf1)=\operatorname{diag}(\mathbb EU)-\operatorname{Cov}(U).
\]

Taking the principal coordinates `(y,z1,z2)` gives exactly

\[
\frac1{49}
\begin{pmatrix}
11&8&8\\
8&9&2\\
8&2&9
\end{pmatrix},
\qquad
\det=-\frac1{2401}<0.
\]

Hence `h_R` is not even log-concave at the all-ones point. The lead's rank-slack PSD budget and every consequence using `R-E|F|` are therefore **refuted as written**.

By contrast, the source-valid ALOV ground-set degree is `m=3`. Its same principal block is

\[
\frac1{49}
\begin{pmatrix}
60&8&8\\
8&9&2\\
8&2&9
\end{pmatrix},
\qquad
\det=\frac{76}{2401}>0,
\]

consistent with the theorem. Thus B02's earlier ground-set spectral comparisons remain the admissible log-concavity input; the attempted rank strengthening cannot be used.

## 2. Materially different mechanism for the lead's triangle `STAR-2` debt

Fix a simple graph `G`, a triangle edge `g=uv`, and let `W=V\{u,v}`. Let `B=G[W]`. For a base forest `T subseteq E(B)`, let its connected components be `C`. Define

\[
a_C=|E(u,C)|,\qquad b_C=|E(v,C)|,
\]

and

\[
\Phi(T)=\prod_C(1+a_C+b_C),
\]

\[
\Theta(T)=\sum_C a_Cb_C\prod_{D\ne C}(1+a_D+b_D),
\qquad
Q(T)=\frac{\Theta(T)}{\Phi(T)}
 =\sum_C\frac{a_Cb_C}{1+a_C+b_C}.
\]

These are exact extension counts, not a surrogate distribution.

### Extension identity

In `G-g`, after fixing `T`, an acyclic attachment set at `u,v` may use at most one `u`-edge and at most one `v`-edge into each `T`-component. If `u,v` stay disconnected, each component independently contributes `1+a_C+b_C`, so there are exactly `Phi(T)` such extensions. If `u,v` are connected, exactly one component receives both sides, so there are exactly `Theta(T)` such extensions. Hence total deletion extensions equal

\[
\Phi(T)+\Theta(T)=\Phi(T)(1+Q(T)).
\]

After contracting `g`, the two endpoints become one vertex. For each base component, an acyclic extension may choose at most one of the `a_C+b_C` incident copies, including the parallel pair created by a common neighbor. Thus the contraction/`STAR-2` extension count is exactly `Phi(T)`.

Therefore, for marked edges lying entirely in the base graph `B`, the projected contraction law `nu` and deletion law `mu` satisfy the exact likelihood-ratio identity

\[
\boxed{\quad
\nu(T)\propto\Phi(T),\qquad
\mu(T)\propto\Phi(T)(1+Q(T)).
\quad}
\]

This directly identifies the induced positive weights created by a triangle contraction without pretending they are unit weights.

### The tilt is structurally increasing

Write `q(a,b)=ab/(1+a+b)`. When a forest edge merges two base components with terminal counts `(a,b)` and `(c,d)`,

\[
q(a+c,b+d)-q(a,b)-q(c,d)
=
\frac{(ad-bc)^2+ad(a+d+1)+bc(b+c+1)}
{(1+a+b)(1+c+d)(1+a+b+c+d)}\ge0.
\]

Thus `Q(T)` is nondecreasing under any legal base-forest edge addition. The deletion law is therefore an **increasing exact tilt** of the contraction/STAR-2 law. This is a source-generated comparison, not an arbitrary external-field hypothesis.

## 3. Exact covariance transport, and a tempting sufficient condition is false

Let `X,Y` be the indicators of two marked base edges. Under `nu`, put

\[
s=1+\mathbb E_\nu Q,
\quad u=\operatorname{Cov}_\nu(X,Q),
\quad v=\operatorname{Cov}_\nu(Y,Q),
\]

and

\[
\kappa=\mathbb E_\nu[(X-\mathbb EX)(Y-\mathbb EY)(Q-\mathbb EQ)].
\]

Direct expansion of the tilt gives the exact transport identity

\[
\boxed{\quad
\operatorname{Cov}_\mu(X,Y)
=
\operatorname{Cov}_\nu(X,Y)
+\frac{\kappa}{s}-\frac{uv}{s^2}.
\quad}
\]

In a minimal-counterexample argument, deletion gives `Cov_mu(X,Y)<=0`; the contraction debt is `Cov_nu(X,Y)<=0`. A tempting sufficient route would demand nonnegative tilt correction, equivalently `s*kappa>=uv`. That route is **not necessary and is false in the source model**.

### Five-vertex exact counterexample to nonnegative tilt curvature

Take vertices `0,1,2,3,4`, edges

`01,02,03,04,12,13,14`,

condition on triangle edge `g=12`, and mark base edges `e=03`, `f=04`. For the four base forests on `{03,04}`, exact extension counts are

\[
\Phi=(12,8,8,5),\qquad \Theta=(4,4,4,3).
\]

Hence `Z_nu=33`, `Z_mu=48`, and exact arithmetic gives

\[
\operatorname{Cov}_\nu(X,Y)=-\frac4{1089}<0,
\qquad
\operatorname{Cov}_\mu(X,Y)=-\frac1{144}<0,
\]

but

\[
\mathbb E_\nu Q=\frac5{11},\quad
u_X=\nu_Y=\frac4{121},\quad
\kappa=-\frac{16}{3993},
\]

so

\[
s\kappa-uv=-\frac{304}{43923}<0.
\]

The correction itself is `-19/5808`, and the exact transport identity holds. Thus even when both deletion and contraction have the desired negative covariance, the tilt correction can be negative. A proof cannot demand `s*kappa>=uv` universally.

The exact unpaid off-terminal implication is instead the **quantitative** inequality

\[
\boxed{
\frac{\kappa}{s}-\frac{uv}{s^2}
\ge \operatorname{Cov}_\mu(X,Y),
}
\]

which is equivalent to `Cov_nu(X,Y)<=0` once the deletion term is known. The value of the reduction is that every quantity is now computed under the source-generated base law `nu`, and `Q` is an explicit monotone component-merger statistic. This is the next place a real graphic argument must enter. It is not replaced by a generic log-concavity sign claim.

This reduction currently covers marked pairs wholly inside `B`. Attachment/star marked pairs require a separate terminal calculation; the named partner's exact cubic-star factorization already closes one important unit-star subcase.

## 4. Exact regression

The standard-library `Fraction` checker is immutable beside this report.

- source SHA-256: `91f4b2d1cac241e5d6f6b150e11e5d28b90ba22bf401626e593eae99a68e95bc`;
- source Git blob: `4038e2755561c9b381d6e2027512fd9445cef596`;
- output SHA-256: `ed4b490520063888b1502224a53f74b24e5afaad162d244d59178b51d58a7e6f`;
- output Git blob: `ec8b91158a811e8c1a9ebf752219292d4ff9c5a4`.

It verifies exactly:

1. the `K3` rank-degree negative-Hessian principal determinant is `-1/2401`;
2. the source ground-degree counterpart is `76/2401`;
3. the `Phi/Theta` extension identities for every labelled simple graph on 3--5 vertices: 1,096 graphs, 3,047 triangle-edge instances, and 9,749 base-forest instances;
4. every fraction in the five-vertex q-tilt counterexample and the covariance transport identity.

Execution status: `ALL_EXACT_CHECKS_PASS_AND_CURVATURE_CANDIDATE_REFUTED`. Finite enumeration is regression for the algebra, not evidence of universal FOREST closure.

## 5. Conditional end-to-end argument after this correction

A valid log-concavity route can still use the **ground-set** ALOV polynomial to obtain spectral PSD comparisons for the exact unit unrooted-forest law. It cannot replace ground-set size by graphic rank, and spectral negativity is not entrywise Rayleigh negativity.

The lead's minimal-counterexample route may continue only after removing every consequence that depends on the refuted rank-slack matrix. For a triangle contraction and an off-terminal marked pair, the new exact source reduction says:

1. deletion law on the base is `mu proportional Phi(1+Q)`;
2. contraction/STAR-2 law is `nu proportional Phi`;
3. `Q` is monotone under forest-edge mergers;
4. deletion negativity is inherited by minimality;
5. contraction negativity is equivalent to the displayed quantitative third-moment tilt inequality.

So the first essential missing implication is no longer an unspecified weighted closure statement: it is a concrete q-tilt covariance inequality with exact source-generated `Phi,Q`, plus a separate terminal-edge case. The universal stronger curvature sign has already been refuted, so the next attempt must retain the negative deletion covariance credit rather than throw it away.

## 6. Source scope and fixed-host warning

The accessible Semple--Welsh source proves a **class-level** equivalence between the all-graphs unit conjecture and weighted independence correlation for graphic matroids by replacing rational weights with parallel copies in a generally different graph. The same source explicitly notes that unit-good graphs are not thereby known to be minor-closed. I therefore do not use a fixed-host unit-to-all-positive-weights upgrade unless its exact stronger source is produced and checked. This is consistent with the current lead's fail-closed treatment.

Primary source used for log-concavity: Anari, Liu, Oveis Gharan and Vinzant, *Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for Independent Sets of Matroids*, arXiv:1811.01600, especially the definition of `g_M` and the following spectral-negative-dependence discussion.

## Before / after / remaining owner

**Before:** the current lead had a promising triangle-free minimal-counterexample mechanism but used a rank-degree homogenization to strengthen the spectral budget, and its first triangle obstruction was an induced `STAR-2` weighted contraction law.

**After:** the rank-degree spectral claim is exactly refuted already on `K3`; the source-valid ground-set log-concavity boundary is restored. Independently, the triangle `STAR-2` law for off-terminal marked pairs is now represented exactly as a source-generated component-product law `nu proportional Phi`, while deletion is the increasing tilt `mu proportional Phi(1+Q)`, with an exact covariance-transport identity and a source counterexample eliminating the overstrong nonnegative-curvature shortcut.

**Remaining blocker:** prove the quantitative q-tilt inequality above for the graph-generated `Phi,Q` structure (or find a source counterexample), and derive the corresponding terminal-edge comparison. **Owner:** FOREST campaign lead `fleet01/B01`, with B02 continuing the source-valid polynomial/probabilistic comparison and `fleet03/B03` supplying structured adversaries/local terminal identities.

## Operational/account note

Fresh exposed fleet02 inventory showed all twenty managed B01--B20 registrations enabled, unique and hourly-valid; the current role allocation matched the collective directive, B20 was enabled, and exposed per-task email/notification flags were off. No deficit requiring B20 repair was observed. B02 made zero scheduler mutations.

Scoped privacy/secret review of the new B02 files found no credentials, scheduler identifiers, machine paths, raw transcripts, benchmark gold, or unrelated private data. Historical peer files and protected controls were not modified.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: `maximum actually supported`. Configured/known reasoning effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token/thinking-time usage: `null / NOT_EXPOSED`. Elapsed execution to the report snapshot: `1326.522` seconds from the recorded run start, measured by UTC clock; this includes tool/network/runtime time and is not pure thinking. The later immutable receipt/finish records the final wall interval.
