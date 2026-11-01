Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED by runtime metadata — GPT-6 maximum was requested, but the exposed scheduler/runtime surface has no authenticated model-family selector or reasoning-effort selector, so I do not claim GPT-6 maximum. **METRIC MOVEMENT: 5 -> 6 genuinely distinct nonparabolic shape families; Section-B moves tried: #12 FIND WHAT IS CONSERVED, #14 FIND THE GROUP ACTING, #25 COUNT THE SAME THING TWICE.**
Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Status: PARTIAL; the open-ended source problem is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 6: log-periodic pulsed parabolic-scale tubes

Run date: 2026-09-17 Asia/Jerusalem / 2026-09-16 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Fixed metric and continuity

The frozen metric is the number of genuinely nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

Previous authoritative report:

`runs/R07/20260916T2124Z_i0077_positive_seam_gauges_05.md`.

It records metric `5` from:

1. mixed two-power zero-seam cusps `u^alpha+u^beta`, `0<alpha<1/2<beta`;
2. logarithmic zero-seam cusps of regular-variation index `1/2` at both ends;
3. homogeneous pure-power tubes `u^beta`, including the complete beta<1/2, beta=1/2, beta>1/2 phase portrait;
4. outward `o(sqrt u)` corrugations of a parabolic strip;
5. positive-seam superdiffusive gauges such as `1+u^(3/4)`.

This run proves a universal nonconfinement theorem for a sixth family: **log-periodically pulsed parabolic-scale tubes**. Their normalized width oscillates by order one forever in logarithmic time, so they are not an `o(sqrt u)` corrugation, not a slowly varying logarithmic cusp, not a pure power, and not a positive-seam tube.

Therefore

\[
\boxed{5\longrightarrow6.}
\]

`unchanged_count` resets to `0`.

## 2. Required repository continuity / admission / neighboring work

Before new mathematics I reread/rechecked current `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- newest own report `runs/R07/20260916T2124Z_i0077_positive_seam_gauges_05.md` and all earlier I0077 reports;
- newest same-source neighboring report `runs/R15/20260916_2155Z_i0076_stuck1_palm_boundary_a18.md`; R15 owns distinct Problem 7.2 / I0076;
- targeted repository/intake searches for I0077, Problem 7.8, `1302.6958`, and duplicate attempts.

`INDEX.md` and `RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` contains no Problem-7.8 exclusion. `QUEUE.md` continues to list I0077 distinctly from assigned I0076. `operations/claims/I0077.md` still reserves I0077 exclusively to R07 although its shared status text remains `PENDING_ADMISSION, not READY`; this worker does not mutate shared operational files.

The large `probability_1000_intake_*/problems.jsonl` resources cannot be rendered exhaustively row-by-row through the connector without truncation. I therefore record the whole-intake reread as **PARTIAL / targeted due connector limits**. Exact I0077/source/ownership, duplicate attempts, and neighboring Burdzy–Scheutzow scopes were rechecked. No stale `admitted=true` flag was treated as current permission.

No other track's file was edited.

## 3. Primary source recovered again

Primary source rechecked directly this run: arXiv:1302.6958v4.

Definition 2.1: an FBM is a continuous real-indexed process `X` for which there are random times `S_n -> -infinity` a.s. such that, for every `n`,

\[
(X_{S_n+t}-X_{S_n})_{t\ge0}
\]

is standard Brownian motion.

Definition 2.2 gives decomposable FBMs by concatenating independent Brownian pieces stopped at a.s.-finite stopping times.

For the parabolic strip

\[
c_1\sqrt{|t|}\le x\le c_2\sqrt{|t|},\qquad t\le0,
\]

Theorem 4.3 states:

1. if `lambda_0(c1,c2)>=1`, every FBM has the universal normalized-growth obstruction;
2. if `lambda_0(c1,c2)<=1`, there is a decomposable FBM with the corresponding asymptotic normalized confinement;
3. if `c1<=0<=c2` and `lambda_0(c1,c2)<1`, there is a decomposable FBM pointwise confined in the parabolic strip.

The source identifies `(-1,1)` as a critical pair with `lambda_0(-1,1)=1`, and Remark 4.1 gives strict domain monotonicity of `lambda_0`.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

Problem 7.9 is the distinct forward-Lévy question. The intake trailing text from 7.9 is not part of I0077.

## 4. Current-status / prior-art pass — dated 2026-09-17 Asia/Jerusalem

Fresh bounded searches this run included:

- `"Forward Brownian Motion" "Problem 7.8"`;
- Burdzy / Scheutzow later-author and citing-paper queries;
- `log-periodic Brownian moving boundary Ornstein-Uhlenbeck survival`;
- `time-periodic Ornstein-Uhlenbeck absorbing boundary principal eigenvalue`;
- `principal eigenvalue time-periodic parabolic operator Dirichlet Nadin`;
- `Brownian slow points periodic boundary`;
- `Brownian motion periodic boundary square root survival`;
- `Ornstein-Uhlenbeck moving boundary periodic killing`.

I found no later paper explicitly resolving Burdzy–Scheutzow Problem 7.8 or stating the FBM pulsed-tube theorem proved below. This is **bounded negative evidence only, not a novelty certificate**.

Relevant prior art is substantial. The source itself reduces static parabolic tubes to the Ornstein–Uhlenbeck Sturm–Liouville problem and uses Perkins's Brownian slow-point results. Grégoire Nadin, *The principal eigenvalue of a space–time periodic parabolic operator*, Ann. Mat. Pura Appl. 188 (2009), 269–295, develops principal eigenvalues for time-periodic parabolic operators with spatial Dirichlet conditions. There is later work on time-periodic principal eigenvalues, including Liu–Lou–Peng–Zhou. Burdzy–Chen–Sylvester (Ann. Probab. 2004) study heat equations in time-dependent domains. Thus “periodic killing has a Floquet/principal exponent” is not claimed new. The source-specific result below is a self-contained explicit duty-cycle criterion strong enough to force the critical exponent past `1`, followed by an FBM witness-time argument.

## 5. The new family

Let `w:R->(0,infinity)` be continuous and `1`-periodic. For `u>0`, define the symmetric tube

\[
D_w=
\{(t,x):t<0,\ |x|\le \sqrt{|t|}\,w(\log|t|)\}\cup\{(0,0)\}.
\tag{5.1}
\]

Since `w` is bounded, the tube closes continuously to `(0,0)`. It is invariant under the discrete Brownian dilation

\[
(t,x)\mapsto(e t,\sqrt e\,x),
\tag{5.2}
\]

because `w(r+1)=w(r)`.

The theorem is stated for an explicit duty-cycle class.

Assume that for some `a>0`, `tau in (0,1]`, and `eta>0`, every period contains an interval of logarithmic length at least `tau` on which

\[
w(r)\le a,
\tag{5.3}
\]

and that

\[
\boxed{
\tau\,
\frac{\pi^2 e^{-(a+2\eta)^2/2}}
{8(a+2\eta)^2}
>1.
}
\tag{5.4}
\]

The quantity in (5.4) is an explicit lower bound on the amount of killed-OU spectral decay produced per logarithmic period.

A canonical nonconstant representative is the continuous periodic function `w_*` defined on `[0,1]` by

- `w_*(r)=1/2` for `0<=r<=1/2`;
- linear increase from `1/2` to `3` on `[1/2,5/8]`;
- `w_*(r)=3` on `[5/8,7/8]`;
- linear decrease from `3` to `1/2` on `[7/8,1]`;
- then extend with period `1`.

Take

\[
a=\frac12,\qquad \tau=\frac12,\qquad \eta=\frac1{20}.
\tag{5.5}
\]

Then `a+2eta=3/5`, and

\[
\frac{\pi^2e^{-9/50}}{8(9/25)}
=
\frac{25\pi^2}{72}e^{-9/50}
>
\frac{25\cdot9}{72}\left(1-\frac9{50}\right)
=
\frac{41}{16}.
\tag{5.6}
\]

Hence the left side of (5.4) is strictly greater than

\[
\frac12\cdot\frac{41}{16}
=
\frac{41}{32}>1.
\tag{5.7}
\]

So the canonical `w_*` lies in the theorem's class.

## 6. Move #14 — FIND THE GROUP ACTING: discrete scaling becomes time translation

The group acting on this shape is not the full Brownian scaling group but its discrete subgroup generated by factor `e`.

For standard Brownian motion `B`, define the Lamperti transform

\[
Y_r=e^{-r/2}B_{e^r},\qquad r\in\mathbb R.
\tag{6.1}
\]

Then `Y` is the stationary Ornstein–Uhlenbeck process with generator

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right)
\tag{6.2}
\]

and invariant Gaussian probability measure

\[
\gamma(dx)=(2\pi)^{-1/2}e^{-x^2/2}\,dx.
\tag{6.3}
\]

The Brownian event

\[
|B_s|\le\sqrt s\,h(\log s),\qquad R\le s\le T,
\tag{6.4}
\]

is exactly

\[
|Y_r|\le h(r),\qquad \log R\le r\le\log T.
\tag{6.5}
\]

Thus multiplicative physical-time annuli become ordinary additive periods. The discrete dilation (5.2) becomes translation `r -> r+1`. This is the correct quotient symmetry for the problem.

## 7. Move #12 — FIND WHAT IS CONSERVED: Gaussian mass and an L2 dissipation budget

The conserved reference measure is `gamma`. The OU semigroup is a contraction on `L^2(gamma)`, and killing at a boundary is also contractive. The narrow pulse supplies a strict, quantifiable loss in every period.

For `b>0`, let `K_b(t)` be OU evolution killed on exiting `(-b,b)`, and let `lambda_b` be its principal Dirichlet eigenvalue. The standard Rayleigh quotient is

\[
\lambda_b
=
\inf_{0\ne f\in H^1_0(-b,b)}
\frac{\frac12\int_{-b}^b |f'(x)|^2e^{-x^2/2}\,dx}
{\int_{-b}^b |f(x)|^2e^{-x^2/2}\,dx}.
\tag{7.1}
\]

Because `e^{-b^2/2}<=e^{-x^2/2}<=1` on `[-b,b]` and the first Dirichlet eigenvalue of `-d^2/dx^2` on `(-b,b)` is `(pi/(2b))^2`,

\[
\boxed{
\lambda_b
\ge
\frac{\pi^2e^{-b^2/2}}{8b^2}.
}
\tag{7.2}
\]

The spectral theorem gives

\[
\|K_b(t)\|_{2\to2}=e^{-\lambda_b t}.
\tag{7.3}
\]

Now consider a time-dependent killed OU evolution `Q_{r,s}` in the moving interval `(-h(v),h(v))`. Every time-sliced factor is an OU contraction followed by multiplication by an indicator, hence

\[
\|Q_{r,s}\|_{2\to2}\le1.
\tag{7.4}
\]

If throughout a subinterval of length `tau` we have `h(v)<=b`, then the survival event is contained in survival in the static interval `(-b,b)`. For nonnegative `f`, the corresponding positive kernel is dominated by the static killed kernel; for signed `f` take absolute values. Therefore

\[
\|Q_{r,r+\tau}\|_{2\to2}
\le e^{-\lambda_b\tau}.
\tag{7.5}
\]

Take now

\[
h(r)=w(r)+2\eta,
\qquad b=a+2\eta.
\tag{7.6}
\]

Every complete period has a narrow subinterval of length at least `tau`; all other portions cost at most norm `1`. Therefore one complete period has operator norm at most

\[
e^{-\lambda_b\tau}.
\tag{7.7}
\]

Let

\[
\kappa=
\tau\frac{\pi^2e^{-b^2/2}}{8b^2}>1.
\tag{7.8}
\]

An arbitrary logarithmic interval of length `L` contains at least `L-2` complete periods after discarding at most one partial period at each end. Since `Y` is stationary with initial law `gamma`, Cauchy–Schwarz gives the survival estimate

\[
\boxed{
\mathbb P\bigl(
|B_s|\le\sqrt s\,[w(\log s)+2\eta]
\text{ for every }s\in[R,T]
\bigr)
\le
 e^{2\kappa}(T/R)^{-\kappa}.
}
\tag{7.9}
\]

Indeed, the survival probability is `\langle 1,Q1\rangle_gamma`, bounded by `||Q||_{2->2}`, and the period product gives `||Q||<=exp[-kappa(L-2)]` with `L=log(T/R)`.

For the canonical `w_*`, we may take the completely explicit weaker exponent

\[
\boxed{
\kappa_*=\frac{41}{32}>1,
}
\tag{7.10}
\]

so (7.9) holds with `kappa_*` in place of the actual larger decay rate and with a finite explicit prefactor such as `exp(2 kappa_*)`.

## 8. Move #25 — COUNT THE SAME THING TWICE: multiplicative annuli versus terminal-time intervals

The OU estimate counts survival period by period in logarithmic time. To use the FBM witness property, we must count a different object in physical time: possible Brownian **terminal times** whose entire sufficiently remote past lies in the pulsed tube. The same survival event is now counted on ordinary intervals `[n,n+1]`.

Fix `eta>0` as above and a deterministic `R_0>0`. For a standard Brownian motion `B`, define

\[
G(t;R_0)=
\left\{
|B_{t-s}-B_t|
\le
\sqrt s\,[w(\log s)+\eta]
\quad\forall s\in[R_0,t]
\right\}.
\tag{8.1}
\]

We prove

\[
\boxed{
\mathbb P\{G(t;R_0)\text{ occurs for arbitrarily large }t\}=0.
}
\tag{8.2}
\]

This continuum-terminal statement is the step that a simple integer union bound would miss.

For `n>=3`, set

\[
M_n=
\max_{0\le k\le n}
\operatorname{osc}_{[k,k+2]}B.
\tag{8.3}
\]

Every pair of times in `[0,n+1]` at distance at most `1` lies in one of these length-two blocks. For a single block,

\[
\mathbb P\{\operatorname{osc}_{[k,k+2]}B>x\}
\le
4e^{-x^2/16},
\tag{8.4}
\]

because oscillation greater than `x` forces the absolute Brownian increment from the left endpoint to exceed `x/2`, and reflection plus the Gaussian Chernoff bound applies. Consequently

\[
\mathbb P\{M_n>8\sqrt{\log n}\}
\le
4(n+1)n^{-4}
\le8n^{-3},
\tag{8.5}
\]

which is summable.

Define

\[
R_n=\left\lceil
\frac{256}{\eta^2}\log n
\right\rceil.
\tag{8.6}
\]

On `{M_n<=8 sqrt(log n)}`, for every `s>=R_n`,

\[
2M_n\le16\sqrt{\log n}\le\eta\sqrt s.
\tag{8.7}
\]

Suppose some `t in [n,n+1]` satisfies `G(t;R_0)`, where `n` is large enough that `R_n>=R_0` and `R_n<n`. For every `s in [R_n,n]`,

\[
\begin{aligned}
|(B_{n-s}-B_n)-(B_{t-s}-B_t)|
&\le |B_{n-s}-B_{t-s}|+|B_n-B_t|\\
&\le2M_n\\
&\le\eta\sqrt s.
\end{aligned}
\tag{8.8}
\]

Hence the fixed integer terminal time `n` satisfies the **twice-enlarged** tube

\[
|B_{n-s}-B_n|
\le
\sqrt s\,[w(\log s)+2\eta]
\quad\forall s\in[R_n,n].
\tag{8.9}
\]

By Brownian time reversal, `(B_n-B_{n-s})_{0<=s<=n}` is standard Brownian motion. Applying (7.9),

\[
\mathbb P\{\text{(8.9)}\}
\le
 e^{2\kappa}(n/R_n)^{-\kappa}.
\tag{8.10}
\]

Therefore

\[
\begin{aligned}
\mathbb P\{\exists t\in[n,n+1]:G(t;R_0)\}
&\le 8n^{-3}
+e^{2\kappa}(n/R_n)^{-\kappa}.
\end{aligned}
\tag{8.11}
\]

Since `R_n=O(log n)` and `kappa>1`,

\[
\sum_{n=3}^\infty
n^{-\kappa}(\log n)^\kappa<\infty.
\tag{8.12}
\]

Thus (8.11) is summable. Borel–Cantelli proves (8.2).

This is the second honest count of the same geometric obstruction: the OU side counts multiplicative annuli, while the Brownian side counts continuum terminal times by ordinary integer intervals.

## 9. I0077-R07-T7 — universal obstruction for log-periodic pulsed tubes

**Status: PROVED.**

Assume `w,a,tau,eta` satisfy (5.3)–(5.4). Let `X` be any forward Brownian motion. Then

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
|X_{-u}|\le\sqrt u\,w(\log u)
\quad\forall u\ge R
\right)=0.
}
\tag{T7.1}
\]

Equivalently, every FBM exits the nonparabolic tube `D_w` at arbitrarily large negative times almost surely. In particular, there is no FBM — decomposable or otherwise — which is pointwise confined to `D_w` on the whole negative half-line.

### Complete proof

Suppose for contradiction that for some deterministic `R` the event

\[
E_R=
\left\{
|X_{-u}|\le\sqrt u\,w(\log u)
\quad\forall u\ge R
\right\}
\tag{9.1}
\]

has probability `q_0>0`. (If the event in T7.1 with random finite `R` had positive probability, then one deterministic integer `R` would give positive probability by a countable union.)

Since `X_0` is finite almost surely, choose deterministic `A<infinity` such that

\[
E=E_R\cap\{|X_0|\le A\}
\tag{9.2}
\]

has probability

\[
q:=\mathbb P(E)>0.
\tag{9.3}
\]

Set

\[
R_1=
R\vee(A/\eta)^2.
\tag{9.4}
\]

Then on `E`, for every `u>=R_1`,

\[
\begin{aligned}
|X_{-u}-X_0|
&\le |X_{-u}|+|X_0|\\
&\le \sqrt u\,w(\log u)+A\\
&\le \sqrt u\,[w(\log u)+\eta].
\end{aligned}
\tag{9.5}
\]

By (8.2), if `B` is standard Brownian motion and

\[
p_N=
\mathbb P\{\exists t\ge N:G(t;R_1)\},
\tag{9.6}
\]

then

\[
p_N\downarrow0.
\tag{9.7}
\]

Choose deterministic `N` so large that

\[
p_N<q/4.
\tag{9.8}
\]

By the FBM definition there are witness times `S_j->-infinity` a.s. such that

\[
B^{(j)}_r=X_{S_j+r}-X_{S_j},\qquad r\ge0,
\tag{9.9}
\]

is standard Brownian motion for every `j`. Since `S_j->-infinity` a.s., choose one deterministic index `j` such that

\[
\mathbb P\{S_j\le-N\}>1-q/4.
\tag{9.10}
\]

On

\[
E\cap\{S_j\le-N\},
\tag{9.11}
\]

put `t=-S_j>=N`. For every `s in [R_1,t]`,

\[
B^{(j)}_t-B^{(j)}_{t-s}
=
X_0-X_{-s}.
\tag{9.12}
\]

Therefore (9.5) implies

\[
|B^{(j)}_{t-s}-B^{(j)}_t|
\le
\sqrt s\,[w(\log s)+\eta]
\quad\forall s\in[R_1,t].
\tag{9.13}
\]

That is exactly `G(t;R_1)` for the standard Brownian motion `B^{(j)}` at a terminal time `t>=N`. Hence

\[
\mathbb P(E\cap\{S_j\le-N\})
\le p_N<q/4.
\tag{9.14}
\]

But (9.3) and (9.10) give

\[
\mathbb P(E\cap\{S_j\le-N\})
\ge q-\mathbb P(S_j>-N)
>3q/4,
\tag{9.15}
\]

a contradiction. This proves T7.1.

No independence between `E` and the witness time was used. No decomposability assumption was used. The theorem applies to **every FBM**.

## 10. Canonical representative: a genuine nonparabolic result, not static Theorem 4.3 in disguise

For `w_*` from Section 5, T7 gives

\[
\boxed{
\mathbb P\left(
|X_t|\le\sqrt{|t|}\,w_*(\log|t|)
\text{ eventually as }t\to-\infty
\right)=0
}
\tag{10.1}
\]

for every FBM `X`.

Several adversarial checks matter.

### 10.1 The outer static parabola does not imply the result

The canonical width reaches `3`, so

\[
D_{w_*}\subseteq\{|x|\le3\sqrt{|t|}\}.
\]

But the source has `lambda_0(-1,1)=1`, and strict domain monotonicity gives

\[
\lambda_0(-3,3)<1.
\tag{10.2}
\]

Thus Theorem 4.3(i) does **not** prohibit eventual confinement in the outer static parabola. The obstruction comes from the repeated narrow logarithmic pulses, not from a static envelope comparison.

### 10.2 A static inner parabola also does not imply the result

The tube is as narrow as `|x|<=sqrt{|t|}/2`, but only during half of each logarithmic period. It is not globally contained in that narrow parabola, so source Theorem 4.3(i) cannot simply be applied to the inner envelope either.

### 10.3 It is not the previous `o(sqrt u)` corrugation family

For an outward `o(sqrt u)` corrugation, the normalized width converges to a constant. Here

\[
w_*(\log u)
\]

oscillates between `1/2` and `3` at arbitrarily large `u`; its normalized oscillation never vanishes.

### 10.4 It is not a trivial Brownian rescaling

A Brownian scaling changes logarithmic phase by an additive constant. It can translate the periodic profile but cannot turn a nonconstant periodic profile into a constant one. The tube has exact discrete scale invariance but not full continuous scale invariance.

Hence this is a genuinely distinct sixth family under the frozen equivalence convention. Different amplitudes, phases, or periodic profiles satisfying the same duty-cycle theorem count as parameters inside this one family, not as additional metric points.

## 11. What the three new methods contributed

### #12 FIND WHAT IS CONSERVED

The invariant Gaussian measure of the Lamperti-transformed OU process supplies a single `L^2(gamma)` norm in which all unconstrained evolution and all killing are contractions. The narrow pulse creates a strict Dirichlet-energy loss that can be accumulated without needing independence between periods.

### #14 FIND THE GROUP ACTING

The nonparabolic tube has discrete multiplicative scale symmetry. Passing to the quotient by this group turns the geometric oscillation into an ordinary period-one time dependence. That makes a time-periodic killed-diffusion operator the natural object.

### #25 COUNT THE SAME THING TWICE

First count survival over logarithmic periods by operator norm. Then count possible continuum terminal points by ordinary physical-time intervals `[n,n+1]`. The modulus-of-continuity enlargement links the two counts and converts spectral rate `kappa>1` into a summable terminal-time series.

## 12. Failed/avoided routes and precise obstruction

1. **Naive outer-envelope comparison.** It fails for the canonical example because the outer envelope `[-3 sqrt u,3 sqrt u]` is source-subcritical (`lambda_0<1`).
2. **Naive inner-envelope comparison.** It fails because the narrow interval is present only for a logarithmic duty cycle, not all times.
3. **Integer terminal times only.** Insufficient: FBM witness origins produce arbitrary real terminal times. Section 8 is needed to pass from continuum terminal points to integer terminals with a quantitative two-stage margin `eta+eta`.
4. **Assume a new Floquet theorem.** Avoided. General periodic-parabolic principal-eigenvalue theory exists in the literature, but this proof needs only OU reversibility, a static Dirichlet eigenvalue bound, `L^2` contraction, and Borel–Cantelli.
5. **Treat the new family as a new exact critical phase classification.** Not claimed. T7 is a complete universal nonexistence theorem for the explicit duty-cycle class. A sharp existence/nonexistence boundary for arbitrary periodic profiles remains open in this work.

## 13. Relation to a sharper periodic-operator formulation

For a positive periodic profile `w`, one can define the period-one killed-OU evolution operator `Q_w`. In general its long-time decay should be governed by a periodic-parabolic principal/Floquet exponent, consistent with the Nadin literature. A sharp analogue of source `lambda_0=1` would plausibly compare that exponent with `1`.

This run does **not** assert that general equivalence. Instead, (5.4) is an explicit variational lower bound proving that the unknown periodic exponent is already `>1` for a concrete open set of profiles. That is enough for the source-style universal obstruction and avoids a circular appeal to an unproved moving-boundary theorem.

## 14. Model / reasoning control and permission escalation

The limitation remains unchanged. The exposed scheduler-control schema permits task title/prompt, schedule, enablement and timing-mode changes; it has **no model-family field and no reasoning-effort field**. Therefore `GPT-6 / maximum` can be requested in prompt text but cannot be authenticated or forced from this worker interface.

A real fix requires either:

1. product support for explicit model/reasoning fields on scheduled tasks, or
2. an authorized owner/admin/platform-support context that can set those runtime properties.

The repository records historical native-edit attempts returning `You cannot modify this task` for some IDs, including a P26 attempt, while another authorized context later succeeded on P26. The correct conclusion is that permission is ownership/context scoped. There is no legitimate R07-level bypass, and creating a duplicate task is not an authorized workaround. This run made **no scheduler changes**.

## 15. Audit / closure status

The source Problem 7.8 remains **PARTIAL / open-ended**, not closed. T7 is a complete theorem for one new family but does not classify arbitrary space-time shapes.

No finite combinatorial core exists in T7. The only explicit numerical threshold is proved symbolically on the page using `pi^2>9` and `e^{-x}>1-x`; manufacturing an arithmetic checker would not test the theorem. No checker artifact was created.

T7 has not yet received the two required independent OTHER-track audits, including P26, so it is not closure-certified and no `paper_*` folder is created.

## 16. Structured ledger delta

```yaml
ledger_delta:
  worker: R07
  source:
    authors: [Krzysztof Burdzy, Michael Scheutzow]
    year: 2014
    title: Forward Brownian Motion
    arxiv: 1302.6958
    locator: Problem 7.8
    intake: I0077
  target: "Generalize Theorem 4.3 from parabolic regions to genuinely distinct nonparabolic space-time shape families."
  metric: "number of distinct nonparabolic shape families with a complete source-appropriate theorem, modulo frozen trivial-equivalence convention"
  before: 5
  after: 6
  movement: true
  unchanged_count: 0
  status: PARTIAL
  new_claims:
    - id: I0077-R07-T7
      status: PROVED
      statement: "For every continuous 1-periodic normalized width w satisfying the explicit narrow-duty-cycle condition (5.3)-(5.4), every FBM exits |x|<=sqrt(|t|)w(log|t|) at arbitrarily large negative times almost surely."
      hypotheses: "continuous positive 1-periodic w; narrow logarithmic interval of length tau per period with w<=a; exists eta>0 with tau*pi^2*exp(-(a+2eta)^2/2)/(8(a+2eta)^2)>1"
      quantifiers: "for every FBM; no decomposability assumption"
      normalization: "natural logarithm; period 1; centered tube; terminal point (0,0)"
    - id: I0077-R07-T7-CANONICAL
      status: PROVED
      statement: "The explicit nonconstant profile with half-period width 1/2 and a wide plateau at 3 satisfies T7; an explicit spectral-rate lower bound is 41/32>1."
  exact_evidence:
    - "full analytic proof Sections 6-10 of this immutable report"
    - "primary source arXiv:1302.6958v4 Definitions 2.1-2.2, Theorem 4.3, Problem 7.8"
  audit_ids: []
  closure: false
  prior_art_status: "bounded dated search; general periodic-parabolic eigenvalue machinery is known; exact Problem-7.8/T7 novelty UNVERIFIED"
```

## 17. Next attack

Do **not** count another periodic profile as a seventh family. The next high-value question is the sharp boundary for bounded periodic normalized profiles: can the one-period killed-OU operator replace `lambda_0(c1,c2)` in both the universal-obstruction and decomposable-existence directions?

Next unused-method triple recorded for R07:

- **#15 BREAK THE SYMMETRY ON PURPOSE:** use different periodic lower and upper boundaries, not a symmetric width;
- **#20 FIND WHY THE ALGORITHM FAILS:** run the source stopping-time concatenation against a periodic moving interval and isolate the exact endpoint-selection obstruction;
- **#7 TAKE THE LIMIT:** examine slow/fast oscillation limits of the periodic profile to compare the Floquet exponent with static `lambda_0` data.

A genuine result here would move from an explicit supercritical duty-cycle family toward a source-level periodic analogue of Theorem 4.3 rather than accumulating examples.
