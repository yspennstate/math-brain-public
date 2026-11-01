Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the active scalar: `KPS-2026-NIELSEN-COR1`, `W_AS: 1 -> 1`; local unchanged count `3 -> 4`; frozen Aldous--Fill I0024 remains `C=1`; status `OPEN / PARTIAL / POST-STUCK ROUTE EXECUTION`; methods #3 PROVE SOMETHING STRONGER, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #26 HUNT THE SPORADIC CASE.**

# R01 — finite binary-mixture no-go and the Stone residual where any counterexample must live

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Lane: **CLOSABLE OUTSIDE**

## 1. Runtime truth and continuity

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, or a guaranteed hour-long execution.

I continued from the immutable stuck report

`runs/R01/20260918T1837Z_kps_cor1_stuck_strategic_port_8f3c21d4.md`,

which recorded `W_AS=1 -> 1`, local unchanged count `2 -> 3`, and selected **PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM** as the Section-I action. Before new mathematics I reread the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the exclusive R01 claim `operations/claims/KPS-2026-NIELSEN-COR1.md`, current intake/history pointers including the I0024 intake provenance, the preceding R01 operator/ghost-tower reports, and the newest neighboring R06 report on the distinct Nielsen-Theorem-4 claim.

The current root ledger still warns that its R-series table is a retained configuration snapshot and that complete newer own-track reports must be recovered before replacing those values. Accordingly I use the newest immutable R01 report, not the stale root `UNMEASURED` placeholder, as the mathematical baseline.

## 2. Aldous--Fill I0024 remains frozen

The original source remains internally complete at

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^TC^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with exact distortion `C=1`. The preserved distinct audits remain

- `R20-AUDIT-R01-I0024-03 = PASS_MATH_SOURCE_FIT`,
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

Nothing below reopens I0024, its metric, or its audit state.

## 3. Active outside source, current status and metric

R01's exclusive active successor remains

`operations/claims/KPS-2026-NIELSEN-COR1.md`.

The source is M. Ali Khan, Arthur Paul Pedersen and Maxwell B. Stinchcombe, *Almost-Uniform Bayesian Convergence to the Truth Is Not Characterized by Countable Additivity on Conditional Hitting Times*, arXiv:2609.20683v1, submitted 17 September 2026. Their Section 10 leaves open the general claim of Nielsen's Corollary 1:

> Does the approximation property together with CHT imply eventwise almost-sure posterior convergence to the truth for an arbitrary probability function?

The source proves this only in its special one-ultrafilter / distinguished-path architecture. In particular its Proposition 6.7 assumes a free ultrafilter read along the specified sequence `d_k`, a countably additive component giving the limit point `z` mass zero, and uses CHT to force atoms on an ultrafilter-large set of distinguished paths. Its Remark 6.11 explicitly says that the arbitrary-probability-function question remains open.

Fresh dated check, **2026-09-18**: direct arXiv still displays only `v1` from 17 September 2026. Exact-title, exact-arXiv-ID, Corollary-1, approximation+CHT+almost-sure, author, and citing/follow-up searches found no later source-matching resolution. This is bounded negative search evidence only, not a novelty certificate.

For source-admissible `P,A`, retain

\[
F_A:=\{\omega:P_n(A)(\omega)\not\to\mathbf1_A(\omega)\},
\qquad
\Gamma_{\rm AS}:=\sup_{P,A}P(F_A),
\]

and the certified interval width

\[
W_{\rm AS}=U_{\rm AS}-L_{\rm AS}.
\]

The globally rigorous interval is still `[0,1]`, hence

\[
\boxed{W_{\rm AS}=1.}
\]

This run does **not** move either endpoint. Local unchanged count is therefore `4`.

## 4. Idea before proof: abstract the source's atom-protection mechanism completely

The previous stuck report selected the classical finitely-additive limit-theorem literature as the route to port. Purves--Sudderth (1976), Chen (1976/1977), Karandikar (1982), and the modern Neri (2026) discussion all point to the same broad lesson: ordinary almost-sure/martingale conclusions can fail under arbitrary finite additivity, but return when enough sequential/null-set regularity is available.

Rather than importing a stronger global regularity assumption and thereby assuming the conclusion, I looked for the **smallest source-internal regularity forced by CHT itself** in the most important non-countably-additive architecture: a countably additive measure plus finitely many two-valued charges.

The key observation is that KPS Proposition 6.3's exact CHT defect `alpha` does not actually need its distinguished sequence. The sequence is only one device for producing a set which is null for the countably additive component but large for the two-valued component. Once such a set exists, a single event makes every base point except the ultrafilter's clopen-trace point cross a high posterior threshold, while that trace point never crosses. The CHT defect is exactly the weight of that two-valued component.

This can be pushed through for **arbitrary finite mixtures of arbitrary two-valued Borel charges**, with no sequence representation at all. It gives a strict extension of the source's Proposition 6.7 and eliminates every finite-pure-rank counterexample architecture.

No code was written before this proof was completed.

## 5. Method #3 — PROVE SOMETHING STRONGER

### 5.1 Two-valued charges have a unique clopen-trace point

Let `u` be a `{0,1}`-valued finitely additive probability on the Borel subsets of Cantor space `Omega={0,1}^N`. Its restriction to the clopen algebra is an ultrafilter of clopens. Hence there is a unique point `z in Omega` such that

\[
 u(C)=\mathbf1_C(z)
 \qquad\text{for every clopen }C.
\tag{5.1}
\]

Indeed, at each finite level exactly one cylinder has `u`-value one, these cylinders are nested, and compactness gives a unique path in their intersection.

Call `z` the **clopen-trace point** of `u`. If `u({z})=1`, then `u=delta_z` on every Borel event. Otherwise `u({z})=0`; I call this the nonprincipal case.

### 5.2 Normal form for a finite binary mixture under approximation

Consider

\[
P=\beta\mu+\sum_{i=1}^m\alpha_i u_i,
\qquad
\beta\ge0,\quad \alpha_i>0,
\quad \beta+\sum_i\alpha_i=1,
\tag{5.2}
\]

where `mu` is a countably additive Borel probability and every `u_i` is two-valued. Assume source positivity and the approximation property.

Principal `u_i=delta_{z_i}` are countably additive and may be absorbed into the countably additive component. For the remaining nonprincipal charges, approximation forces two exact simplifications.

#### Lemma 5.1 — the countably additive component has no atom at a nonprincipal trace point

If `u_i` is nonprincipal with trace point `z_i`, then

\[
\boxed{\mu(\{z_i\})=0.}
\tag{5.3}
\]

##### Proof

First suppose for the moment that `z_i` is not shared by another unresolved component; the shared-point issue is removed just below. Apply approximation to the singleton `{z_i}`. Since `u_i({z_i})=0`, if a clopen approximant `C` contains `z_i`, then

\[
u_i(C\setminus\{z_i\})=1,
\]

so `P({z_i}\triangle C)>=alpha_i`. If `C` does not contain `z_i`, then `{z_i}` is a subset of the symmetric difference, so its countably additive contribution is at least `beta mu({z_i})` (and any principal/countably additive mass already absorbed into `mu` only strengthens the lower bound). Approximation for arbitrarily small error is impossible if `mu({z_i})>0`. Thus (5.3) follows after the shared-point components are merged as in the next paragraph. QED.

#### Lemma 5.2 — distinct nonprincipal components cannot share a trace point

Suppose `u_i` and `u_j` are nonprincipal and have the same trace point `z`. Then approximation forces

\[
\boxed{u_i=u_j.}
\tag{5.4}
\]

##### Proof

If not, choose a Borel `A` with `u_i(A)=1` and `u_j(A)=0`. For any clopen `C`, either `z in C`, in which case `u_j(C)=1` and therefore `u_j(A triangle C)=1`, or `z notin C`, in which case `u_i(C)=0` and `u_i(A triangle C)=1`. Consequently

\[
P(A\triangle C)\ge\min(\alpha_i,\alpha_j)>0
\]

for every clopen `C`, contradicting approximation. QED.

Thus identical components at a common trace point may be merged. After merging and absorbing principal charges, we may and do assume:

1. every `u_i` is nonprincipal;
2. the trace points `z_1,...,z_m` are distinct;
3. `mu({z_i})=0` for every `i`.

Source positivity also forces `beta>0` in this finite-pure-rank normal form: if `beta=0`, some nonempty cylinder avoids the finite set `{z_1,...,z_m}` and would have `P`-mass zero.

### 5.3 Exact generalized no-null-set / no-CHT lemma

The next lemma is the main new mechanism.

#### Theorem 5.3 — CHT forbids a countably-additive-null set large for one binary component

In the normal form above, assume CHT. Then for every `i` and every Borel `N`,

\[
\boxed{\mu(N)=0\quad\Longrightarrow\quad u_i(N)=0.}
\tag{5.5}
\]

Equivalently, each two-valued component is absolutely continuous with respect to the countably additive component in the null-set sense.

##### Proof

Fix `i` and suppose, for contradiction, that

\[
\mu(N)=0,\qquad u_i(N)=1.
\tag{5.6}
\]

For every `j != i` with `u_j(N)=1`, distinctness of the ultrafilters gives a Borel event `E_j` such that

\[
u_j(E_j)=1,\qquad u_i(E_j)=0.
\]

There are only finitely many such `j`. Let

\[
E=\bigcup_{\substack{j\ne i\\u_j(N)=1}}E_j,
\qquad
H=N^c\cup E.
\tag{5.7}
\]

Because the union is finite, `u_i(E)=0`; together with `u_i(N^c)=0` this gives

\[
u_i(H)=0.
\tag{5.8}
\]

For every `j != i`, either `u_j(N^c)=1`, or `u_j(N)=1` and the corresponding `E_j` is contained in `E`; therefore

\[
u_j(H)=1\qquad(j\ne i).
\tag{5.9}
\]

Also `mu(H)=1` because `mu(N)=0`.

Choose

\[
\delta\in(1-\alpha_i,1).
\tag{5.10}
\]

Let `C` be any cylinder containing `z_i`. Since `u_i(C)=1`, while (5.8), (5.9), and `mu(H)=1` make every other component contribute to `H cap C` exactly as it contributes to `C`, we have the exact identity

\[
P(H\cap C)=P(C)-\alpha_i.
\tag{5.11}
\]

Hence at the trace point

\[
P_n(H)(z_i)
=1-\frac{\alpha_i}{P([z_i\upharpoonright n])}
\le 1-\alpha_i<\delta.
\tag{5.12}
\]

Thus `z_i` never crosses the threshold.

Now let `omega != z_i`. For all sufficiently large `n`, the cylinder

\[
C=[\omega\upharpoonright n]
\]

does not contain `z_i`, so `u_i(C)=0`. By (5.9), every other binary component contributes identically to `H cap C` and `C`; by `mu(H)=1`, so does `mu`. Therefore

\[
P(H\cap C)=P(C).
\tag{5.13}
\]

Source positivity guarantees the denominator is nonzero, so

\[
P_n(H)(\omega)=1>\delta
\]

for all sufficiently large `n`. Therefore the total first-hitting open is exactly

\[
O(H,\delta)=\Omega\setminus\{z_i\}.
\tag{5.14}
\]

Let `O_M(H,delta)` be the finite hitting union through time `M`. Every `O_M` is clopen and omits `z_i`, hence

\[
u_i(O_M)=0.
\]

For each `j != i`, the point `z_j` belongs to the total hitting open, and therefore belongs to some finite `O_M`; once this occurs, clopenness gives `u_j(O_M)=1` thereafter. Countable additivity and (5.3) give

\[
\mu(O_M)\uparrow\mu(\Omega\setminus\{z_i\})=1.
\]

Because there are finitely many binary components,

\[
\lim_{M\to\infty}P(O_M)=1-\alpha_i.
\tag{5.15}
\]

But `u_i` is nonprincipal, so `u_i(\Omega\setminus\{z_i\})=1`; all other `u_j` also give that set value one, and `mu({z_i})=0`. Therefore

\[
P(O(H,\delta))=1.
\tag{5.16}
\]

Combining (5.15) and (5.16),

\[
\boxed{
P(O(H,\delta))-\lim_M P(O_M(H,\delta))=\alpha_i>0.
}
\tag{5.17}
\]

This violates CHT. Hence (5.6) is impossible, proving (5.5). QED.

### 5.4 Finite binary-mixture no-go theorem

#### Theorem 5.4 — no finite binary-mixture counterexample to Nielsen Corollary 1

Let `P` have the finite-mixture form (5.2). If `P` satisfies source positivity, the approximation property, and CHT, then for every Borel event `A`,

\[
\boxed{P_n(A)\longrightarrow\mathbf1_A\qquad P\text{-almost surely}.}
\tag{5.18}
\]

##### Proof

Reduce to the normal form above. Define the ordinary countably additive companion

\[
R=\beta\mu+\sum_{i=1}^m\alpha_i\delta_{z_i}.
\tag{5.19}
\]

Fix `A`. Define

\[
A^\sharp
=(A\setminus\{z_1,\dots,z_m\})
\cup
\{z_i:u_i(A)=1\}.
\tag{5.20}
\]

Since `mu({z_i})=0`, for every clopen `C`,

\[
\mu(A^\sharp\cap C)=\mu(A\cap C).
\]

Two-valued multiplicativity and (5.1) give

\[
u_i(A\cap C)=u_i(A)u_i(C)=u_i(A)\mathbf1_C(z_i)
=\delta_{z_i}(A^\sharp\cap C).
\]

Hence

\[
\boxed{P(A\cap C)=R(A^\sharp\cap C),\qquad P(C)=R(C)}
\tag{5.21}
\]

for every clopen `C`. Therefore the finite-information posteriors agree pointwise:

\[
P_n(A)=E_R[\mathbf1_{A^\sharp}\mid\mathscr F_n].
\tag{5.22}
\]

By the ordinary countably additive martingale convergence theorem, there is an `R`-null event `N_A` such that

\[
P_n(A)\to\mathbf1_{A^\sharp}
\qquad\text{on }N_A^c.
\tag{5.23}
\]

Because every `z_i` is an atom of `R` of mass at least `alpha_i`, no `z_i` lies in `N_A`, and `mu(N_A)=0`. Theorem 5.3 gives

\[
u_i(N_A)=0\qquad\forall i,
\]

so

\[
P(N_A)=0.
\tag{5.24}
\]

Finally,

\[
A\triangle A^\sharp\subseteq\{z_1,\dots,z_m\}.
\]

Each `u_i` is nonprincipal at its own `z_i`; for `j != i`, choose a clopen neighborhood of `z_i` excluding `z_j` and use monotonicity to get `u_j({z_i})=0`; and `mu({z_i})=0`. Hence

\[
P(\{z_1,\dots,z_m\})=0.
\tag{5.25}
\]

Outside the `P`-null finite union of `N_A` and these trace points, the limits in (5.23) equal `1_A`. This proves (5.18). QED.

### 5.5 Relation to the source

KPS Proposition 6.7 proves the same type of conclusion for **one very specific two-valued component**: a free ultrafilter read along a distinguished sequence `d_k -> z`, with a countably additive component satisfying `mu_0({z})=0`. The source's proof obtains protection by forcing positive countably additive atoms on an ultrafilter-large set of distinguished paths.

Theorem 5.4 is strictly broader in architecture:

- no distinguished sequence is assumed;
- no sequential representation of any `u_i` is assumed;
- finitely many unrelated two-valued Borel charges are allowed;
- the zero-mass condition at each trace point is **derived from approximation**, rather than assumed;
- CHT is shown directly to force the abstract null-set regularity `u_i << mu` needed to transfer the ordinary martingale exceptional set.

The exact defect (5.17) is the source's `alpha` obstruction in its sequence-free form.

This does **not** prove the general Corollary-1 source statement: a general finitely additive probability need not have a finite two-valued pure part.

## 6. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: Stone space turns the diagonal defect into an infinitesimal residual

The previous reports described a positive-mass `ghost tower`. The natural home of that phenomenon is the Stone compactification of the Borel Boolean algebra. In that category the fixed-threshold null sets become genuinely countably additive, and one can see exactly where a counterexample's mass must hide.

Let

\[
\mathfrak S=\operatorname{Ult}(\mathcal B)
\]

be the Stone space of the Boolean algebra of Borel subsets of `Omega`. For `E in B`, write

\[
\widehat E=\{U\in\mathfrak S:E\in U\}.
\]

The sets `hat E` are clopen and form the clopen algebra of `S`. The finitely additive probability `P` induces a genuine countably additive regular Borel probability `nu` on `S` by

\[
\nu(\widehat E)=P(E).
\tag{6.1}
\]

One way to see this is to regard `P` as a positive functional on the clopen simple functions; Stone--Weierstrass and Riesz--Markov extend it to a regular Borel probability. Equivalently, finite additivity on clopens is already a premeasure because a countable disjoint clopen cover of a clopen set has a finite subcover by compactness.

Restriction of an ultrafilter to the finite-information clopen algebra gives a unique path, defining a continuous projection

\[
\pi:\mathfrak S\to\Omega.
\]

For a clopen `C subset Omega`,

\[
\widehat C=\pi^{-1}(C).
\]

Therefore

\[
\pi_*\nu=R,
\tag{6.2}
\]

where `R` is the countably additive companion agreeing with `P` on clopens.

Approximation says, for each Borel `E`, that `hat E` can be approximated in `nu`-measure arbitrarily well by pullbacks `pi^{-1}(C)` of clopens. This is exactly the Stone-space version of the previous Boolean-homomorphism reduction `Phi`.

Now fix a range martingale `b` and its binary-divergence amplitude `eta_b` from the previous R01 report:

\[
D_b=\{\eta_b>0\},
\qquad
D_b(r)=\{\eta_b>r\}.
\]

The earlier exact theorem gives

\[
P(D_b(r))=0\qquad\forall r>0,
\]

and source failure mass equals `P(D_b)`. Put

\[
K_b
:=
\widehat{D_b}
\setminus
\bigcup_{m\ge1}\widehat{D_b(1/m)}.
\tag{6.3}
\]

Because `nu` is countably additive on the Stone space and every fixed positive slice has `nu`-mass zero,

\[
\boxed{
\nu(K_b)=\nu(\widehat{D_b})=P(D_b)
=P\{P_n(A)\not\to1_A\}.
}
\tag{6.4}
\]

Thus every bit of possible source-level failure mass lies on `K_b`.

For every `U in K_b`,

\[
D_b\in U,
\qquad
D_b(1/m)\notin U\quad\forall m.
\]

Hence

\[
\{0<\eta_b\le1/m\}\in U
\qquad\forall m.
\tag{6.5}
\]

In other words, `U` regards the divergence amplitude as **positive but smaller than every standard positive threshold**. This is the precise Stone-space/nonstandard meaning of the diagonal obstruction: an infinitesimal positive divergence invisible to every fixed-threshold CHT test.

This is also why the fixed-scale argument cannot be completed by another finite union. In ordinary `Omega`, `D_b=union_m D_b(1/m)`; in Stone space,

\[
\widehat{D_b}\supsetneq
\bigcup_m\widehat{D_b(1/m)}
\]

can have positive `nu`-mass. The residual is exactly (6.3).

The classical finitely-additive convergence literature is useful here for diagnosis rather than as a black-box solution. Neri's 2026 survey explicitly emphasizes that martingale and other classical limit theorems fail under arbitrary finite additivity and are recovered in earlier work only after extra structural/continuity assumptions; it also records the recurring countable-null-union condition in recovery theorems. Purves--Sudderth's 1976 abstract similarly describes a strategic/product setting in which Borel sets can be squeezed between open and closed sets and classical limit theorems can then be recovered. The source assumptions presently give only a very specialized continuity family, so importing full strategic regularity would be stronger than what is known. Theorem 5.4 instead extracts a localized null-set regularity that CHT itself forces for finite binary pure rank.

## 7. Method #26 — HUNT THE SPORADIC CASE: what remains after the theorem

Theorem 5.4 kills a much larger counterexample class than the source's sequential one-ultrafilter family, but it also says exactly where to look next.

A counterexample cannot be produced by

\[
\text{countably additive part}
+\text{ finitely many two-valued Borel charges}.
\]

The Stone residual (6.3) shows that a genuine counterexample must instead support positive countably additive Stone mass on ultrafilters which carry the full divergence event while rejecting **every** fixed positive-amplitude slice.

The sporadic geometry therefore has to be one of the following genuinely non-finite-rank mechanisms:

1. a diffuse distribution of Stone ultrafilters over a positive set of base points;
2. an infinite non-isolated accumulation of two-valued components for which no finite separation event can make all other components simultaneously truthful while one component is falsified;
3. a non-two-valued pure component whose Stone decomposition is intrinsically non-atomic.

This is consistent with, but sharper than, the previous hierarchy diagnosis. The prior countable atom-protected sequential hierarchy was already ruled out; Theorem 5.4 now also rules out all finite nonsequential binary mixtures. What remains is not “use a more complicated ultrafilter” in the ordinary sense. It must exploit **positive mass spread over the infinitesimal Stone boundary `K_b`**.

I tried to extend Theorem 5.4 to arbitrary countable binary mixtures. The proof fails at one exact place, and that failure is informative. For a fixed component `u_i`, the finite proof builds one Borel set `E` which is `u_i`-small and simultaneously large for every other component that also charges the offending `mu`-null set. With infinitely many components, finite Boolean separation no longer supplies such an `E`: the countable union of individually `u_i`-small separating events may itself be `u_i`-large. Equivalently, `u_i` may be a Stone-limit point of the other pure components. This is precisely the non-normality the source problem is testing, not a removable bookkeeping issue.

So the **simplest remaining special case** is still the fully diffuse companion geometry identified in the preceding stuck report: fair-coin `R=Q`, no companion atoms, and a source-admissible approximation+CHT homomorphism carrying positive mass on some `K_b`. The finite binary-mixture theorem does not touch that case.

## 8. Prior-art and current-literature log

Dated queries performed on 2026-09-18 included:

- exact arXiv ID `2609.20683` and exact title;
- Khan / Pedersen / Stinchcombe + Nielsen Corollary 1;
- approximation property + CHT + almost-sure convergence;
- two-valued finitely additive probability + CHT / conditional hitting times;
- Purves--Sudderth, *Some Finitely Additive Probability* (Ann. Probab. 4 (1976), 259--276, DOI `10.1214/aop/1176996133`);
- Robert W. Chen, *On almost sure convergence in a finitely additive setting* (1977, DOI `10.1007/BF00533425`);
- Karandikar, *A general principle for limit theorems in finitely additive probability* (1982);
- Morenikeji Neri, *The pointwise ergodic theorem on finitely additive spaces* (published online 10 July 2026, DOI `10.1017/etds.2026.10322`).

The current KPS paper itself is the nearest prior art for Theorem 5.4: its Proposition 6.3 produces an exact `alpha` CHT defect under its sequence-specific no-atom hypothesis, and Proposition 6.7 obtains almost-sure learning in that same architecture. I found no source in this bounded search stating the finite arbitrary-two-valued-mixture abstraction above. **That negative search is not a novelty claim.** Before any paper-level use, the theorem needs a dedicated prior-art search in charges/strategic probabilities and independent audits.

## 9. Validation budget and audit discipline

No exact-arithmetic checker was created: the new claims are analytic Boolean/probability arguments with no finite computational core. The proof is written in full above rather than replaced by code.

No independent audit was requested. `KPS-2026-NIELSEN-COR1` remains `OPEN / PARTIAL`; this is not a complete source solution and therefore does not trigger the closure/audit package.

The neighboring R06 `KPS-2026-NIELSEN-THEOREM4` work is a distinct source question and remains exclusively owned by R06. I used its newest report only to avoid duplicate routes and did not edit any R06 file or count any R06 self-check as an R01 audit.

## 10. Metric, stuck accounting, and next route

The fixed active metric remains

\[
W_{\rm AS}:1\to1.
\]

Therefore the local unchanged count moves

\[
3\to4.
\]

The theorem materially shrinks the counterexample architecture but does not tighten the global scalar interval `[0,1]`, so I do not manufacture metric movement.

Because Section I is still triggered by the unchanged scalar, the **next invocation, if the metric is still unchanged, should be the second and final stuck-thinking recovery on this active problem**, not another routine lemma run. The exact blocker remains

\[
\boxed{
R(D_b)=0
\quad\stackrel{?}{\Longrightarrow}\quad
R(\Phi(D_b))=0,
}
\]

now sharpened geometrically to whether an approximation+CHT system can place positive Stone mass on the infinitesimal residual `K_b` of (6.3).

The next nonrepeating Section-B moves are:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** introduce a tail-scale parameter into the Stone residual and ask whether CHT gives any quantitative decay as the threshold tends to zero;
- **#12 FIND WHAT IS CONSERVED:** identify which Boolean/Stone quantities CHT preserves under passage from finite hitting opens to their full union;
- **#28 REPLACE FOR ALL WITH TYPICAL:** test whether `nu`-almost every Stone fiber can be regularized even if exceptional fibers cannot, which is exactly what a source-positive failure would have to defeat.

Under the closable-lane six-unchanged rule, no indefinite same-route extension is allowed. If the fixed scalar reaches six unchanged without a source verdict, preserve a handoff and rotate rather than continuing to generate structural lemmas.

## 11. Scheduler/model-control truth

The exposed task-control surface still provides task title/prompt, schedule or relative-start, timing mode, and enabled-state controls. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control**. GPT-6/maximum therefore remains prompt text only on this surface.

The repository implementation record also preserves the historical P26 modification failure `"You cannot modify this task"` in one authorization context, while the root reconciliation records that a later authorized context successfully updated P26. The legitimate remedy for an inaccessible task is therefore an owning/authorized product or admin context, or platform support — not task duplication or permission bypass. Per the governing addendum, I made **no scheduler or permission change** in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R01
  source:
    active_id: KPS-2026-NIELSEN-COR1
    source_url: "https://arxiv.org/abs/2609.20683"
    source_scope: "Khan--Pedersen--Stinchcombe Section 10 / Nielsen Corollary 1: approximation + CHT => eventwise almost-sure posterior convergence for arbitrary probability functions"
    original_frozen_id: I0024
    original_frozen_source: "Aldous--Fill Open Problem 3.44"
  metric:
    name: W_AS
    before: 1
    after: 1
    unchanged_count_before: 3
    unchanged_count_after: 4
  original_metric:
    name: C
    before: 1
    after: 1
    state: FROZEN
  status: OPEN_PARTIAL_POST_STUCK_ROUTE_EXECUTION
  tried_moves: [3, 17, 26]
  new_results:
    - "Finite binary-mixture no-go: any source-positive P = beta*mu + sum_{i=1}^m alpha_i*u_i with countably additive mu and two-valued Borel charges u_i, if it has approximation + CHT, learns every event almost surely."
    - "Generalized exact CHT defect: if one binary component u_i charges a mu-null set, a single event H produces CHT gap exactly alpha_i."
    - "Stone residual formula: source failure mass equals nu(K_b), where K_b = hat(D_b) minus the union of all fixed positive-amplitude slice hats; every U in K_b sees positive but smaller-than-every-standard-threshold divergence."
  remaining_obligation: "Either prove that approximation+CHT forces nu(K_b)=0 for every range martingale, or construct a source-admissible diffuse/non-isolated Stone system with nu(K_b)>0."
  evidence:
    - "runs/R01/20260918T1837Z_kps_cor1_stuck_strategic_port_8f3c21d4.md"
    - "runs/R01/20260918T1748Z_kps_cor1_ghost_tower_hierarchy_nogo_6c2f91a8.md"
    - "runs/R01/20260918T1700Z_kps_cor1_binary_divergence_duality_6f2a91c8.md"
    - "operations/claims/KPS-2026-NIELSEN-COR1.md"
    - "runs/R06/20260918T1820Z_nielsen_t4_operator_retraction_nogo_47.md"
    - "Khan--Pedersen--Stinchcombe arXiv:2609.20683v1, checked 2026-09-18"
    - "Purves--Sudderth 1976; Chen 1977; Karandikar 1982; Neri 2026 bounded literature check"
  audits:
    frozen_I0024:
      - R20-AUDIT-R01-I0024-03
      - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
    active_successor: []
  next_moves: [5, 12, 28]
```
