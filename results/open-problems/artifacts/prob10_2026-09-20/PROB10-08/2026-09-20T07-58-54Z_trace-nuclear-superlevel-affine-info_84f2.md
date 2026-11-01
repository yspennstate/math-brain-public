Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 maximum was requested, but no authenticated runtime metadata available to this run establishes that model/effort setting.

# PROB10-08 artifact — trace/nuclear control of invariant heat-kernel superlevel relations, a universal varentropy envelope, and an affine information monovariant

Status: **PROVED auxiliary mechanism theorems / Salez Problem 2.3 remains OPEN / no new source-level cutoff class certified in this artifact / independent validation pending / worldwide novelty UNVERIFIED**.

This artifact concerns Justin Salez, arXiv:2508.21055v1, Problem 2.3, under the source's rate-one continuous-time simple-random-walk convention. It does not concern the posted Abelian Cayley/product-condition target.

## 1. Continuity and nonduplication

The controlling PROB10 contract, current `POSTED.md`, `operations/claims/I0112.md`, the preserved R16/H0002 handoff, the historical I0112 stuck diagnosis, the newest own report

`runs/prob10_2026-09-20/PROB10-08/2026-09-20T06-57-55Z_relation-block-persistence-affine-quotient_b631.md`,

and the newest neighboring T08 reports were read before this work. In particular:

- the old product-varentropy, synchronous-tensor, moving-weight/local-Poincare, Hecke/information-curvature and time-zero subcommutation routes are not restarted;
- P26 now owns Green/spherical and biregular-halving transfer, most recently `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_10-10-50__biregular-halved-green-transfer.md`;
- NM13-01 now owns arc-cover/Hodge/reversal-orbit routes, most recently `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T07-22-00Z__reversal-arc-orbit-likelihood.md`.

The immediate predecessor left a concrete gap: non-cutoff forces a symmetric automorphism-invariant high-likelihood relation at the **early** mixing threshold, and block concatenation constrains very sparse relations, but the argument stopped in the moderate-localization regime where one composition can already be macroscopic. The first theorem below removes that `m^k=o(n)` restriction completely by changing from relation composition to trace duality.

## 2. Frozen setup

Let `G=(V,E)` be a finite connected `d`-regular vertex-transitive graph, `n=|V|`, and let `P` be discrete-time simple random walk. We use Salez's exact rate-one continuous-time semigroup

\[
H_t=e^{t(P-I)}.
\]

The stationary law is uniform, `pi=1/n`. Let

\[
\gamma=1-\lambda_2(P)>0
\]

be the one-sided spectral gap. For a fixed root `x`, define the heat-kernel likelihood ratio

\[
f_t(x,y):=nH_t(x,y).
\]

Since `P` is symmetric and every graph automorphism commutes with `P`, the kernel `H_t` is symmetric and automorphism-invariant. In particular, every superlevel relation of `f_t` is symmetric, invariant and regular.

## 3. New theorem: trace/nuclear bound for every invariant superlevel relation

Fix a threshold `u>0` and define

\[
R_u(x):=\{y\in V:f_t(x,y)\ge u\}.
\]

Let

\[
m_u:=|R_u(x)|,
\qquad
M_u:=H_t(x,R_u(x)).
\]

By vertex transitivity both quantities are independent of `x`. If `m_u=0`, all claims below are trivial, so assume `m_u>0` and let `Q_u` be normalized adjacency of the relation,

\[
Q_u(x,y)=\frac{1_{\{y\in R_u(x)\}}}{m_u}.
\]

Then `Q_u` is a symmetric stochastic matrix. Loops, if present, cause no problem.

### Theorem 3.1

For every `t>=0` and `u>0`,

\[
\boxed{
M_u\le \frac{m_u}{n}+e^{-\gamma t}\sqrt{m_u}.
}
\tag{3.1}
\]

Since each point in `R_u(x)` has heat-kernel mass at least `u/n`, necessarily `m_u<=n/u`, and hence

\[
\boxed{
M_u\le \frac1u+e^{-\gamma t}\sqrt{\frac{n}{u}}.
}
\tag{3.2}
\]

This is an exact finite-graph statement.

### Proof

First compute the trace exactly. Symmetry and regularity of `R_u` give

\[
\begin{aligned}
\operatorname{tr}(H_tQ_u)
&=\sum_{x,y}H_t(x,y)Q_u(y,x)\\
&=\frac1{m_u}\sum_x H_t(x,R_u(x))\\
&=\frac{nM_u}{m_u}.
\end{aligned}
\tag{3.3}
\]

Let `Pi=J/n` be projection onto constants and write

\[
H_t=\Pi+E_t.
\]

The nonconstant eigenvalues of `E_t` are

\[
e^{-(1-\lambda_i(P))t},\qquad i=2,\ldots,n,
\]

so

\[
\|E_t\|_{op}\le e^{-\gamma t}.
\tag{3.4}
\]

Since `Q_u` is stochastic, `tr(Pi Q_u)=1`. Trace duality therefore gives

\[
\frac{nM_u}{m_u}-1
=\operatorname{tr}(E_tQ_u)
\le \|E_t\|_{op}\,\|Q_u\|_*.
\tag{3.5}
\]

The relation has exactly `nm_u` nonzero entries, each equal to `1/m_u`, hence

\[
\|Q_u\|_F^2=\frac{n}{m_u}.
\]

Using `\|A\|_*<=\sqrt n\|A\|_F`,

\[
\|Q_u\|_*\le \frac{n}{\sqrt{m_u}}.
\tag{3.6}
\]

Substitute (3.4)--(3.6) into (3.5) and multiply by `m_u/n` to obtain (3.1). The deterministic size bound `m_u u/n<=1` then gives (3.2). QED.

## 4. Removal of the predecessor's moderate-localization hole

The preceding R16 run showed that if Salez Problem 2.3 fails, then along a subsequence and for some fixed `epsilon in (0,1/2)` there are fixed `a,b>0` at

\[
t=t_{mix}(1-\varepsilon)
\]

such that the invariant relation

\[
R(x)=\{y:nH_t(x,y)\ge n^a\}
\]

has

\[
H_t(x,R(x))\ge b,
\qquad
m:=|R(x)|\le n^{1-a}.
\tag{4.1}
\]

The predecessor's multi-block theorem was strongest when powers `m^k` remained `o(n)` and therefore did not eliminate the moderate regime `a<=1/2`.

Applying (3.1) directly to (4.1) gives

\[
b\le n^{-a}+e^{-\gamma t}n^{(1-a)/2}.
\tag{4.2}
\]

Consequently every such non-cutoff localization must satisfy

\[
\boxed{
\frac{\gamma t_{mix}(1-\varepsilon)}{\log n}
\le \frac{1-a}{2}+o(1).
}
\tag{4.3}
\]

Equivalently,

\[
\boxed{
a\le 1-2\frac{\gamma t_{mix}(1-\varepsilon)}{\log n}+o(1).}
\tag{4.4}
\]

There is no `k(1-a)<1` hypothesis. Formally, (4.3) is the `k->infinity` endpoint suggested by the predecessor's block inequality, but it is now proved in one step for **all** relation exponents. Thus the moderate-localization gap is genuinely removed at the level of this obstruction.

This still does not prove cutoff: for ordinary bounded-degree expanders the right side of (4.4) can remain a positive constant, so polynomial high-likelihood localization with a small exponent is not excluded.

## 5. A Schatten interpolation hierarchy

The nuclear-norm proof has a useful exact refinement. For `1<=p<infinity`, define

\[
R_p(t):=\sum_{i=2}^n e^{-p(1-\lambda_i(P))t}
=\|E_t\|_{S_p}^p.
\]

Let `q=p/(p-1)` be the conjugate exponent.

### Proposition 5.1

For `1<=p<=2`,

\[
\boxed{
M_u\le \frac{m_u}{n}+
\left(R_p(t)\frac{m_u}{n}\right)^{1/p}.
}
\tag{5.1}
\]

For `2<=p<=infinity`, with the usual limiting interpretation at `p=infinity`,

\[
\boxed{
M_u\le \frac{m_u}{n}+
R_p(t)^{1/p}n^{-1/p}\sqrt{m_u}.
}
\tag{5.2}
\]

Hence, using `m_u<=n/u`,

\[
M_u\le \frac1u+
\begin{cases}
(R_p(t)/u)^{1/p},&1\le p\le2,\\
R_p(t)^{1/p}n^{1/2-1/p}u^{-1/2},&2\le p\le\infty.
\end{cases}
\tag{5.3}
\]

### Proof

Trace duality gives

\[
\operatorname{tr}(E_tQ_u)\le \|E_t\|_{S_p}\|Q_u\|_{S_q}.
\]

When `q>=2`, every eigenvalue of the symmetric stochastic matrix `Q_u` lies in `[-1,1]`, so

\[
\|Q_u\|_{S_q}^q\le\|Q_u\|_{S_2}^2=n/m_u,
\]

giving `\|Q_u\|_{S_q}<=(n/m_u)^{1/q}` and (5.1). When `q<=2`, the finite-dimensional norm comparison yields

\[
\|Q_u\|_{S_q}
\le n^{1/q-1/2}\|Q_u\|_{S_2}
=\frac{n^{1/q}}{\sqrt{m_u}},
\]

giving (5.2). QED.

This hierarchy exposes rather than hides the full-source difficulty. `R_2` is exactly the doubled-time Green/chi-square excess and can be polynomial at the TV scale on the Haiman affine stress family. At `p=infinity` one recovers the universally available spectral-gap estimate (3.2), which is too weak by a constant exponent. Without an additional transitivity-driven spectral-density or information estimate, interpolation alone does not close the source.

## 6. Universal positive-information tail and varentropy envelope

Let `X_t` have law `H_t(x,.)`, and write

\[
Z_t:=\log f_t(x,X_t)=\log(nH_t(x,X_t)).
\]

From (3.2), for every `z>=0`,

\[
\boxed{
\Pr(Z_t\ge z)
\le e^{-z}+\exp\left(\frac{A_t-z}{2}\right),
\qquad
A_t:=\log n-2\gamma t.
}
\tag{6.1}
\]

The probability is of course also at most one.

The negative tail has a dimension-free second moment. Indeed,

\[
\mathbb E[(Z_t^-)^2]
=\frac1n\sum_{f_t(x,y)<1}f_t(x,y)(\log f_t(x,y))^2
\le \frac4{e^2},
\tag{6.2}
\]

because `r(log r)^2<=4/e^2` for `0<r<=1`.

For the positive part, use `E W^2=\int_0^\infty 2z P(W>=z)dz`. If `A_t>=0`, bound the interval `[0,A_t]` by one and use (6.1) afterwards:

\[
\begin{aligned}
\mathbb E[(Z_t^+)^2]
&\le A_t^2
+\int_{A_t}^\infty2ze^{-z}dz
+\int_{A_t}^\infty2z e^{(A_t-z)/2}dz\\
&=A_t^2+2(A_t+1)e^{-A_t}+4A_t+8\\
&\le A_t^2+4A_t+10.
\end{aligned}
\tag{6.3}
\]

If `A_t<0`, direct integration of (6.1) from zero gives at most `2+8e^{A_t/2}<=10`. Therefore, with `A_{t,+}=max(A_t,0)`,

\[
\boxed{
\operatorname{Varent}(H_t(x,.))
\le
\mathbb E[Z_t^2]
\le A_{t,+}^2+4A_{t,+}+11.
}
\tag{6.4}
\]

This is a universal finite-n varentropy envelope for continuous-time SRW on a vertex-transitive regular graph, derived from transitivity plus the ordinary spectral gap alone.

Combining (6.4) with Salez's Theorem 5.1 at the **early** threshold `t_-=t_mix(1-epsilon)` gives the valid auxiliary window estimate

\[
\boxed{
 w_{mix}(\varepsilon)
\le \frac{2}{\gamma\varepsilon^2}
\left[
1+\sqrt{A_{-,+}^2+4A_{-,+}+11}
\right],
\quad
A_-:=\log n-2\gamma t_-.
}
\tag{6.5}
\]

This is not promoted to source-level progress. For a generic fixed-degree expander, `A_-` may remain a positive constant fraction of `log n`, so (6.5) need not be `o(t_mix)`. It is a quantified obstruction envelope, not a proof of Salez 2.3.

## 7. Third, different approach: an exact affine conditional-information monovariant

The preceding run reduced the Haiman affine stress family to relative coordinates

\[
\Gamma_q=\Pi_q\ltimes V_q,
\qquad
(M,x)\longleftrightarrow(M,Y),
\qquad
Y=M^{-1}x,
\]

with `Pi_q=SL(2,q)` and `V_q=F_q^2`. In these coordinates, subgroup steps act as

\[
(M,Y)\mapsto(Ms,s^{-1}Y),
\]

while pure translation steps act as

\[
(M,Y)\mapsto(M,Y\pm e).
\]

In particular the `Y` coordinate is an autonomous Markov chain, and, crucially, the joint transition kernel maps every product law `U_{\Pi}\otimes\nu` to another product law

\[
U_{\Pi}\otimes(\nu Q_Y).
\tag{7.1}
\]

Let `\mu_t` be the law of `(M_t,Y_t)` and `\nu_t` its `Y` marginal. Define the conditional subgroup-information defect

\[
\boxed{
J_t:=D(\mu_t\|U_{\Pi}\otimes\nu_t).
}
\tag{7.2}
\]

By the chain rule,

\[
\boxed{
J_t=D(\mathcal L(M_t)\|U_{\Pi})+I(M_t;Y_t).
}
\tag{7.3}
\]

### Proposition 7.1

`J_t` is nonincreasing in `t`.

### Proof

For `s<t`, evolve both measures `\mu_s` and `U_\Pi\otimes\nu_s` under the same affine semigroup. The first becomes `\mu_t`. By (7.1), the second becomes exactly `U_\Pi\otimes\nu_t`. Relative entropy contracts under every Markov kernel, hence

\[
J_t
=D(\mu_sK_{t-s}\|(U_\Pi\otimes\nu_s)K_{t-s})
\le D(\mu_s\|U_\Pi\otimes\nu_s)
=J_s.
\]
QED.

This replaces the predecessor's two separate quantities `D(M_t||U_\Pi)` and `I(M_t;Y_t)` by one exact monotone defect. It also gives

\[
D(\mu_t\|U_\Pi\otimes U_V)
=J_t+D(\nu_t\|U_V).
\tag{7.4}
\]

Thus a cutoff proof for the affine stress family could be reduced to simultaneous control of the autonomous quotient entropy and the decay of one monotone conditional-information functional.

The missing quantitative step is real. A subgroup move can reveal its generator through the new relative coordinate: from a deterministic `Y=y`, if the points `s^{-1}y` are distinct for the active generators, then observing `Y'` identifies `s`; the simultaneous update `M'=Ms` can therefore preserve essentially all conditional information in one step. Ordinary subgroup spectral expansion alone does not give a one-step contraction of `J_t`. The needed estimate is genuinely hypocoercive and uses interlacing of subgroup and translation moves over several steps, not the retired moving-weight Poincare argument.

No affine TV-cutoff theorem is claimed here.

## 8. Three materially different approaches and outcomes

### A. Invariant-superlevel trace/nuclear duality — RETAINED

This proves (3.1)--(4.4), removes the predecessor's `m^k=o(n)` restriction, and yields an all-exponent localization obstruction. It uses only symmetry of the heat kernel, regularity of invariant relations and trace/Schatten duality.

### B. Schatten interpolation / moment profile — RETAINED AS DIAGNOSTIC, NOT CLOSED

The exact family (5.1)--(5.3) interpolates between Green/chi-square information and the spectral-gap endpoint. It shows precisely what extra spectral-density input would be needed. On arbitrary transitive expanders no such uniform input is presently proved; the Haiman affine family already blocks the naive `p=2` route.

### C. Affine conditional-information monovariant — RETAINED AS A NEW STRUCTURAL ROUTE, QUANTITATIVE DECAY OPEN

The exact monotonicity (7.2)--(7.4) turns the prior mutual-information obstruction into a single Lyapunov quantity. But single subgroup moves can preserve conditional information by encoding the chosen generator in `Y`, so a decay theorem must be multi-step/hypocoercive. This is distinct from product tensorization, moving-weight Poincare, and P26/NM13 shell/arc routes.

## 9. Primary-source and current-status checks

The source remains Salez, arXiv:2508.21055v1, Problem 2.3. Salez's rate-one continuous-time convention is `H_t=e^{t(P-I)}`. His Theorem 5.1 evaluates varentropy at the **early** threshold `t_mix(1-epsilon)`, which is the convention used in (6.5).

Altschuler, arXiv:2609.14945, still exposed only v1 in the bounded 20 September 2026 check. The full proof was re-read. Its long-range-expansion hypothesis is used in Lemma 3.2 to transfer maximal-rate growth to the oriented-edge NBRW state space, in Lemma 3.3 to convert set growth into near-maximal entropy, and hence in Proposition 3.1 to obtain endpoint entropy `log n-O(log log n)`; ordinary spectral expansion then enters only in the short cleanup step. No correction/erratum or v2 surfaced in the bounded check.

A bounded prior-art search was also run for combinations of `vertex-transitive heat kernel superlevel relation trace norm`, `Schatten heat kernel cutoff`, and `vertex-transitive varentropy`. It surfaced Salez's varentropy work and general Schatten/small-set literature, but no exact theorem matching (3.1) or (6.4). This is negative search evidence only; worldwide novelty remains UNVERIFIED.

Pedrotti--Salez, arXiv:2607.05345v2 (13 July 2026), was also checked. Their local-product theorem controls the window by a non-equilibrium Poincare constant. The old R16 moving-weight-Poincare attempt targeted precisely that route and is not reopened here.

## 10. Tests actually run and validation status

No simulation, finite mixing plot, brute-force enumeration or numerical checker was used; there is no finite computational core in this iteration.

Analytic self-checks performed:

- verified the exact trace identity (3.3);
- verified the Frobenius and nuclear norms of a regular relation kernel;
- checked the two Schatten regimes and their agreement at `p=2`;
- integrated the information tail explicitly to obtain the constants in (6.4);
- checked that the affine product manifold `U_\Pi\otimes\nu` is invariant and applied data processing to (7.2).

These are self-checks, not independent audits. Independent audit count for the new claims is `0`.

## 11. Source before/after and remaining full-scope gap

```yaml
source_target: "Salez arXiv:2508.21055 Problem 2.3"
walk: "rate-one continuous-time SRW"
source_status_before: "OPEN / PARTIAL"
source_status_after: "OPEN / PARTIAL"
source_metric: "W_exp"
source_metric_before: "1/2 provisional"
source_metric_after: "1/2 provisional"
source_metric_movement: false
new_source_admissible_cutoff_class_this_run: false
mechanism_progress:
  - "exact all-threshold invariant-relation mass bound M <= m/n + exp(-gamma t) sqrt(m)"
  - "moderate-localization hole removed: non-cutoff exponent a must satisfy gamma t/log n <= (1-a)/2 + o(1) without m^k=o(n)"
  - "Schatten interpolation hierarchy for the same relation mass"
  - "universal transitive varentropy envelope Varent <= A_+^2+4A_++11, A=log n-2 gamma t"
  - "exact monotone affine conditional-information defect J_t=D(joint||U_Pi tensor Y-marginal)"
finite_checker: "not applicable"
independent_audits: 0
publication_novelty: "UNVERIFIED"
status_label: "OPEN/PARTIAL"
```

The full-source gap is now narrower but still substantial. The predecessor's moderate-localization issue is no longer a technical failure of relation composition: (3.1) handles every support exponent in one shot. What remains is a **constant-exponent gap**. Ordinary spectral expansion permits the positive-information envelope `A_t=log n-2 gamma t` to remain `Theta(log n)` at the mixing scale, and known source-admissible affine examples show that global chi-square/Green quantities can indeed remain polynomially large there. A full proof needs a genuinely transitivity-specific mechanism that improves the trace bound for the *particular heat-kernel superlevel relation* beyond worst-case nuclear norm, or a multi-step information theorem controlling the affine-type hypocoercive defect. Conversely, a counterexample must realize the surviving small-exponent localization while producing a nonsharp TV profile.
