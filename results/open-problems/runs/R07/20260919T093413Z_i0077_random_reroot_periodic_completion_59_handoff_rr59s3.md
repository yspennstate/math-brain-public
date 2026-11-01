Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: 59 -> 59; unchanged count 5 -> 6; CLOSABLE TERMINAL HANDOFF / R07 RESEARCH RETIRED ON I0077; Section-B moves actually used: #12 FIND WHAT IS CONSERVED, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #3 PROVE SOMETHING STRONGER.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, PTRF 160 (2014), 95–126; arXiv:1302.6958v4, Problem 7.8 / intake I0077: generalize Theorem 4.3 from parabolic regions to other space-time shapes.

Status after this run: **PARTIAL / FULL THREE-CLAUSE THEOREM CANDIDATE FOR THE ALREADY-COUNTED LOG-PERIODIC FAMILY / AUDIT-PENDING / R07 RESEARCH RETIRED-HANDOFF**. The fixed metric does not move because the log-periodically modulated square-root-tube family was already counted at metric point 6. The substantive advance is that the finite-prefix obstruction left by the previous phase-blind sewing report is removed: Definition 2.2 itself permits an arbitrary random re-root, and this can be combined with a source-style periodic slow anchor to give exact all-negative-time confinement in the strict subcritical regime. Together with the earlier critical universal theorem and a vanishing-expansion construction at the critical exponent, this yields a complete symmetric periodic-Floquet analogue of all three clauses of Theorem 4.3. It is **not fleet-closed**: there are still 0/2 independent OTHER-track audits and publication novelty remains UNVERIFIED.

# R07 CLOSABLE OUTSIDE — random re-rooting closes the periodic sewing gap

## 1. Continuity / source / ownership / whole-repository readback

Before new mathematics I re-read the current `master` state required by the owner policy:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- newest own report `runs/R07/20260919T0825Z_i0077_phase_blind_eventual_sewing_59_pbe59s2.md` and the immediately relevant periodic reports `20260919T0521Z`, `20260919T0624Z`, `20260919T0721Z`;
- the current neighboring R15 history. Its Burdzy--Scheutzow Problem 7.2 / I0076 track is `OPEN / PARTIAL / RETIRED-HANDOFF`; R15 is now screening a different successor and does not own I0077;
- targeted repository searches for `I0077`, `Problem 7.8`, `1302.6958`, and the current queue/claim state. The large intake JSONL mirrors are not practically renderable end-to-end through this connector, so I used exact identifier/source searches rather than pretending an exhaustive row-by-row read.

The canonical I0077 file still says `Owner: R07` and `Status: PENDING_ADMISSION, not READY`. `INDEX.md` / `RANKING.md` settle Burdzy--Scheutzow Problem 7.5, not 7.8. `POSTED.md` contains no Problem-7.8 closure. The old R07 KPZ route remains preserved by immutable handoff and was not reopened or deleted.

The current coordinator snapshot also says newly certified free READY inventory is still zero. Therefore after the six-run retirement below I do **not** fabricate or steal a successor claim. The next R07 invocation should admission-screen the queue in order and claim only a genuinely free, source-checked CLOSABLE target.

## 2. Primary source recovered exactly again

I rechecked the primary PDF, arXiv:1302.6958v4, including the actual definitions rather than the intake snippet.

Definition 2.2 is decisive. If independent stopped Brownian pairs are concatenated into a process `X`, and a process `X'` has the property that for **some arbitrary random time** `U`,

\[
\{X'_{U+t}-X'_U:t\in\mathbb R\}
\]

has such a representation, then `X'` is called decomposable. There is no requirement that this re-rooting time `U` be deterministic or a stopping time. The stopped Brownian pairs themselves must be independent.

Theorem 4.3 has three clauses at the static OU Dirichlet exponent `lambda_0(c_1,c_2)`:

1. `lambda_0>=1`: every FBM asymptotically touches/exits one parabolic boundary;
2. `lambda_0<=1`: there exists a decomposable FBM satisfying the reverse asymptotic inequalities;
3. if `c_1<=0<=c_2` and `lambda_0<1`: there exists a decomposable FBM pointwise inside the parabolic region for every negative time.

In the proof of (ii)--(iii), the source uses Perkins's slow-point theorem, time reversal, support, scaling, independent distant Brownian trial blocks and the LIL to obtain equation (4.13): arbitrarily far terminals whose **entire reversed past from the terminal back to the Brownian origin** stays in the parabolic tube and whose endpoint is biased into a small interval. It then concatenates independent stopped pieces. At criticality the source uses a sequence of slightly enlarged subcritical upper boundaries.

Problem 7.8 is exactly: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” The following forward-Levy sentence is separately Problem 7.9 and is not part of I0077.

## 3. Fresh bounded literature / later-author pass, dated 2026-09-19

Fresh public searches this run included:

- exact `"Forward Brownian Motion" "Problem 7.8" Burdzy Scheutzow`;
- `"Forward Brownian Motion" Burdzy Scheutzow later paper`;
- `"Brownian slow points" periodic moving boundary`;
- `"Ornstein-Uhlenbeck" periodic moving boundary Floquet principal eigenvalue survival`.

They recovered the 2014 primary paper / University of Washington publication page and nearby OU/slow-point literature, but no accessible later primary source explicitly announcing a resolution of exact Problem 7.8 or the theorem below. This is bounded negative evidence only, not a worldwide-openness or novelty certificate.

Prior art which remains explicitly non-novel here includes Perkins (1983) and Bass--Burdzy (1996) on Brownian slow points, the standard Lamperti correspondence, and periodic-parabolic / Floquet principal-eigenvalue theory (e.g. Nadin 2009 and later monotonicity work). The previous R07 reports already treated those ingredients as established machinery. Publication novelty of the source-specific sewing theorem remains **UNVERIFIED**.

## 4. The family and the carried analytic input

Let

\[
w:\mathbb R\to(0,\infty)
\]

be nonconstant, `P`-periodic and Lipschitz. Write

\[
m:=\min w>0,\qquad L:=\operatorname{Lip}(w),
\]

and define the genuinely nonparabolic logarithmically corrugated square-root tube

\[
\mathcal D_w
=\{(-u,x):u>0,\ |x|\le \sqrt u\,w(\log u)\}.
\tag{4.1}
\]

Under Lamperti time `r=log u`, Brownian motion becomes stationary Ornstein--Uhlenbeck motion killed in the moving periodic interval

\[
(-w(r),w(r)).
\]

Let `Lambda(w)` denote its principal Floquet killing exponent. If `w` is constant `c`, then

\[
\Lambda(w)=\lambda_0(-c,c).
\tag{4.2}
\]

I carry forward three fully written ingredients from the preceding R07 chain.

**(F1) Strict periodic domain monotonicity.** If one periodic moving interval is uniformly strictly contained in another, its Floquet killing exponent is strictly larger.

**(F2) Universal boundary contact.** The report `20260919T0521Z_i0077_critical_periodic_floquet_boundary_59_cf59n2.md` proves that if `Lambda(w)>=1`, every FBM satisfies

\[
\limsup_{u\to\infty}
\left(
\frac{|X_{-u}|}{\sqrt u}-w(\log u)
\right)\ge0
\quad\text{a.s.}
\tag{4.3}
\]

The proof uses inward erosion, strict Floquet monotonicity, and an all-terminal Brownian mesh estimate, so it includes the critical equality case without conditioning on a random FBM witness.

**(F3) Periodic slow terminals and phase-blind stopped pieces.** The `20260919T0624Z` report proves the sharp periodic Perkins input for `Lambda<1` by a two-terminal second moment with overlap singularity `r^{-Lambda}`. The `20260919T0825Z` report proves the phase-blind finite-cutoff stopping lemma: for any deterministic `A>r>0`, `q>0`, `delta>0`, and subcritical positive periodic profile `v`, standard Brownian motion has an a.s.-finite stopping time `T>=A` with

\[
|B_T|\le\delta\sqrt T,
\tag{4.4}
\]

\[
|B_{T-s}-B_T|\le\sqrt s\,v(\log s),\qquad r\le s\le T,
\tag{4.5}
\]

and

\[
\sup_{0\le s\le r}|B_{T-s}-B_T|\le q.
\tag{4.6}
\]

The rule uses only that Brownian path and deterministic parameters. Hence independent drivers give independent stopped pairs, exactly as Definition 2.2 requires.

The previous report obtained eventual confinement from these facts but thought a finite number of quantile-window failures blocked exact confinement. That diagnosis missed the random-time clause in Definition 2.2.

## 5. Method #12 — the conserved structure: decomposability survives arbitrary random re-rooting

This is the small structural observation that changes the problem.

### Lemma T91-R — random re-root invariance

Let `X` be decomposable and let `U` be **any** finite random time, with no stopping-time assumption. Define

\[
Y_t:=X_{U+t}-X_U,\qquad t\in\mathbb R.
\tag{5.1}
\]

Then `Y` is decomposable.

### Proof

Choose a random time `V` which puts `X` into the independent-stopped-piece representation of Definition 2.2. Replacing `X` by that represented version, we may take `V=0` and `X_0=0`. For `Y` put

\[
V_Y:=-U.
\]

Then for every `t`,

\[
Y_{V_Y+t}-Y_{V_Y}
=
(X_t-X_U)-(X_0-X_U)
=X_t-X_0=X_t.
\tag{5.2}
\]

Thus after the arbitrary random time `V_Y`, `Y` has exactly the original independent stopped-pair representation. This is literally the second sentence of Definition 2.2. No conditioning, sample rejection, or modification of any Brownian piece occurs. QED.

This is the invariant the previous two sewing runs were missing. A finite random prefix may be discarded by re-rooting **after it**, provided the new negative-time origin itself is placed at a genuine periodic slow terminal.

## 6. Periodic analogue of the source's global slow terminal (4.13)

The local periodic Perkins theorem from `20260919T0624Z` is enough to reproduce the exact source step (4.13), including a small endpoint.

### Lemma T91-A — global periodic slow anchors with endpoint bias

Let `v>0` be `P`-periodic Lipschitz with `Lambda(v)<1`. For every `delta>0` and every `a<infinity`, standard Brownian motion satisfies

\[
\mathbb P\left(
\begin{array}{c}
\exists t\ge a:\ |B_t|\le\delta\sqrt t,\\[0.4ex]
|B_{t-s}-B_t|\le\sqrt s\,v(\log s)
\quad\forall s\in[0,t]
\end{array}
\right)=1.
\tag{6.1}
\]

In particular, such terminals occur arbitrarily far out almost surely.

### Proof

Take a slightly smaller periodic profile `v^-` with `Lambda(v^-)<1` and a uniform positive gap to `v`. The periodic Perkins theorem gives local slow terminals for `v^-`. Exactly as in the source between (4.9) and (4.10), time reversal and the Brownian support theorem upgrade the local event to a positive-probability event on a bounded unit-scale block: there is `p>0` such that with probability at least `p` one can find a terminal `t in [1/2,1]` whose complete reversed segment back to the left endpoint stays in the `v^-` tube and whose net endpoint lies in a prescribed small interval around zero. The zero deterministic path is uniformly interior away from the singular lag `s=0`; the local slow-point input handles that singular endpoint. Therefore the endpoint condition costs only a positive support factor.

Now choose deterministic block lengths

\[
L_j=e^{P m_j},\qquad m_j\in\mathbb N,
\]

so fast increasing that the total length of all earlier blocks is `o(L_j)` and its Brownian LIL envelope is `o(sqrt(L_j))`. Brownian scaling by `L_j` preserves the periodic profile **exactly** because

\[
v(\log(L_j s))=v(Pm_j+\log s)=v(\log s).
\tag{6.2}
\]

Use independent Brownian increments on these disjoint blocks. Every block has the same positive lower success probability `p`. Hence infinitely many block-local successes occur almost surely.

For a successful sufficiently large block, the endpoint bias plus the LIL bound on the preceding prefix extends the reversed tube condition from the successful block to the original Brownian time zero. On lags crossing into the old prefix, the target radius is at least `(min v)sqrt(s)`, while both the old-prefix oscillation and the biased block endpoint are `o(sqrt(L_j))`; the fixed gap between `v^-` and `v` absorbs them. The same estimate turns the block endpoint condition into `|B_t|<=delta sqrt(t)` relative to the original origin. This is the periodic, period-lattice version of the source's equations (4.11)--(4.13). Since successful blocks occur arbitrarily far out, (6.1) follows. QED.

A useful deterministic consequence is the following. Fix any increasing deterministic lower scale `Q_n`. Since the event in (6.1) occurs arbitrarily far out, one can choose a deterministic `M_n>Q_n` so large that

\[
\mathbb P(\text{no T91-A anchor in }[Q_n,M_n])\le2^{-n}.
\tag{6.3}
\]

No conditioning is involved.

## 7. Method #23 — do what the previous sewing argument did not expect: discard the finite bad prefix by a random slow anchor

Assume now the strict subcritical condition

\[
\boxed{\Lambda(w)<1.}
\tag{7.1}
\]

Choose a fixed `eta>0` so small that

\[
10\eta<m,
\qquad
\Lambda(w-4\eta)<1.
\tag{7.2}
\]

Choose deterministic sequences `delta_n>0`, `beta_n>0` such that

\[
\sum_{n\ge1}\delta_n^2<\infty,
\qquad
\delta_n\to0,
\qquad
\beta_n\to0.
\tag{7.3}
\]

Write

\[
d_N:=\left(\sum_{n\ge N}\delta_n^2\right)^{1/2}\downarrow0.
\tag{7.4}
\]

Choose `K_n -> infinity` so fast that, for all sufficiently large `n`,

\[
L\log(1+K_n^{-1})+K_n^{-1/2}<\eta.
\tag{7.5}
\]

Let `B^1,B^2,...` be independent Brownian motions, indexing pieces from the original origin into the negative-time direction. The deterministic parameters are chosen recursively before each piece is sampled.

After `U_1,...,U_{n-1}` have been fixed, set

\[
H_n:=1+\sum_{j<n}U_j,
\qquad
r_n:=K_nH_n.
\tag{7.6}
\]

Choose a deterministic anchor floor `Q_n` much larger than `r_n` and all preceding deterministic scales. Apply Lemma T91-A with profile `w-4eta` and endpoint tolerance `delta_n`; choose a deterministic `M_n>Q_n` so that the anchor-failure probability in `[Q_n,M_n]` is at most `2^{-n}` as in (6.3).

Now choose a deterministic lower stopping scale `A_n>M_n`, as large as required by the recursive seam-error budget. Apply the phase-blind stopped-piece lemma (F3) to `B^n` with

\[
v_n=w-2\eta,\qquad A=A_n,\qquad r=r_n,
\tag{7.7}
\]

endpoint coefficient `delta_n`, and, for `n>1`, flat-bridge radius

\[
q_n:=\beta_n\sqrt{Q_{n-1}}.
\tag{7.8}
\]

(The first piece can use any positive convention.) This gives an a.s.-finite stopping time `T_n>=A_n` such that, with

\[
D_n:=B^n_{T_n},
\qquad
Z_n(s):=B^n_{T_n-s}-B^n_{T_n},
\]

we have

\[
|D_n|\le\delta_n\sqrt{T_n},
\tag{7.9}
\]

\[
|Z_n(s)|\le\sqrt s\,[w(\log s)-2\eta],
\qquad r_n\le s\le T_n,
\tag{7.10}
\]

and

\[
|Z_n(s)|\le q_n,
\qquad0\le s\le r_n.
\tag{7.11}
\]

Since `T_n<infinity` a.s., choose a deterministic quantile `U_n` with

\[
\mathbb P(T_n>U_n)\le2^{-n}.
\tag{7.12}
\]

Only this deterministic `U_n`, never the realized `T_n`, is used to design later pieces.

Every `T_n` is a stopping functional of `B^n` and deterministic data only. Therefore the stopped pairs are independent. Concatenate them as in Definition 2.2 to obtain a decomposable FBM `X`.

There are two summable bad-event families:

\[
F_n:=\{T_n>U_n\},
\qquad
G_n:=\{\text{no T91-A anchor in }[Q_n,M_n]\}.
\tag{7.13}
\]

By Borel--Cantelli, almost surely only finitely many `F_n` and `G_n` occur. Choose a random index `N` after all of them and also beyond a deterministic safety index such that

\[
d_N+\sup_{n\ge N}\beta_n<m/2
\tag{7.14}
\]

and (7.5) holds for every `n>=N`.

Because `G_N` does not occur, there is a T91-A anchor `tau_N in [Q_N,M_N]` in the Brownian path `B^N`, with

\[
|B^N_{\tau_N}|\le\delta_N\sqrt{\tau_N},
\tag{7.15}
\]

and

\[
|B^N_{\tau_N-s}-B^N_{\tau_N}|
\le\sqrt s\,[w(\log s)-4\eta]
\qquad0\le s\le\tau_N.
\tag{7.16}
\]

Because `T_N>=A_N>M_N`, this anchor lies inside the already sampled stopped piece. Re-root the concatenated process at that path point:

\[
Y_t:=X_{U+t}-X_U,
\tag{7.17}
\]

where `U` is the corresponding random global time. By Lemma T91-R, `Y` is still decomposable. This is where the finite bad prefix disappears: every piece closer to the old origin than the anchor moves to positive time and is irrelevant to the desired negative-time inequality.

## 8. Exact deterministic tail estimate after the re-root

It remains to prove that **every** negative time of `Y`, not merely all sufficiently negative times, lies in `D_w`.

### 8.1 The root segment

For `0<=u<=tau_N`, equation (7.16) directly gives

\[
|Y_{-u}|
\le\sqrt u\,[w(\log u)-4\eta]
<\sqrt u\,w(\log u).
\tag{8.1}
\]

So the singular neighborhood of the new origin is handled by a true slow point, not by the flat seam bridge.

### 8.2 Right-seam data for every older piece

For an older piece `n>N`, let `R_n` be the elapsed time from its right seam to the new origin. With our past-directed indexing,

\[
R_n
=
\tau_N+\sum_{j=N+1}^{n-1}T_j.
\tag{8.2}
\]

Since all `F_j` fail for `j>=N`, and since

\[
\tau_N\le M_N<T_N\le U_N,
\]

we have the **deterministic** upper bound

\[
R_n\le\sum_{j=N}^{n-1}U_j\le H_n.
\tag{8.3}
\]

For the first older piece, `R_{N+1}=tau_N>=Q_N`. For every later one,

\[
R_n\ge T_{n-1}\ge A_{n-1}>Q_{n-1}.
\tag{8.4}
\]

Let `Y_n` be the spatial value at the right seam of piece `n`, measured relative to the new origin. The anchor endpoint (7.15), the stopped endpoints (7.9), and Cauchy--Schwarz give

\[
\begin{aligned}
|Y_n|
&\le
\delta_N\sqrt{\tau_N}
+
\sum_{j=N+1}^{n-1}\delta_j\sqrt{T_j}\\
&\le
\left(\sum_{j\ge N}\delta_j^2\right)^{1/2}
\left(\tau_N+\sum_{j=N+1}^{n-1}T_j\right)^{1/2}\\
&=d_N\sqrt{R_n}.
\end{aligned}
\tag{8.5}
\]

This is the clean deterministic substitute for the random finite-prefix constant in the preceding report.

### 8.3 Flat seam layer

If `0<=s<=r_n`, then by (7.11), (8.4), and (8.5),

\[
|Y_n+Z_n(s)|
\le
(d_N+\beta_n)\sqrt{R_n}
\le
m\sqrt{R_n}
\le
\sqrt{R_n+s}\,w(\log(R_n+s)).
\tag{8.6}
\]

Thus the whole seam layer is inside the global tube. No phase comparison is needed there; only the positive lower envelope `m` of the periodic profile is used.

### 8.4 Bulk layer

If `s>=r_n`, then (8.3) and (7.6) imply

\[
\frac{R_n}{s}\le\frac{H_n}{r_n}=\frac1{K_n}.
\tag{8.7}
\]

Hence Lipschitz continuity gives

\[
w(\log(R_n+s))
\ge
w(\log s)-L\log(1+K_n^{-1}).
\tag{8.8}
\]

Also, by (8.5) and (8.7),

\[
|Y_n|
\le
\frac{d_N}{\sqrt{K_n}}\sqrt s.
\tag{8.9}
\]

Combining (7.10), (8.8), and (8.9),

\[
\begin{aligned}
|Y_n+Z_n(s)|
&\le
\sqrt s\left[w(\log s)-2\eta+\frac{d_N}{\sqrt{K_n}}\right]\\
&\le
\sqrt s\left[w(\log(R_n+s))-\eta\right]\\
&<
\sqrt{R_n+s}\,w(\log(R_n+s)),
\end{aligned}
\tag{8.10}
\]

where the middle inequality uses (7.5) after increasing the deterministic safety index if necessary.

Equations (8.1), (8.6), and (8.10) cover every negative time of the re-rooted process.

### Theorem T91 — exact subcritical periodic confinement

If `w>0` is nonconstant periodic Lipschitz and

\[
\boxed{\Lambda(w)<1,}
\]

then there exists a decomposable FBM `Y` such that

\[
\boxed{
|Y_{-u}|\le\sqrt u\,w(\log u)
\qquad\forall u\ge0
}
\quad\text{a.s.}
\tag{8.11}
\]

This is the strict-subcritical analogue of Theorem 4.3(iii) for a genuinely nonparabolic shape family.

The crucial point is that the random choice of `N` and `tau_N` does **not** alter or condition the stopped-pair laws. It only chooses the random origin after the decomposable process has already been built, an operation Definition 2.2 explicitly allows.

## 9. Method #3 — prove the full three-clause periodic analogue

Only the critical existence half of source clause (ii) remains after T91 and the carried universal theorem (F2). It follows by the same vanishing-expansion idea used by Burdzy--Scheutzow in the constant case, with the phase-blind sewing parameters allowed to vary from piece to piece.

Assume

\[
\Lambda(w)=1.
\tag{9.1}
\]

Choose any deterministic `epsilon_n downarrow 0`. By strict periodic domain monotonicity,

\[
\Lambda(w+\epsilon_n)<1.
\tag{9.2}
\]

By continuity of the Floquet exponent under uniform perturbation, choose `eta_n>0`, `eta_n downarrow 0`, so small that

\[
\Lambda(w+\epsilon_n-4\eta_n)<1.
\tag{9.3}
\]

Run the phase-blind stopped-piece construction of the preceding report with the `n`th target profile `w+epsilon_n`, inward bulk profile `w+epsilon_n-2eta_n`, and deterministic recursive scales chosen so that on every good sufficiently late piece both

\[
L\log(1+R_n/s)\le\eta_n
\tag{9.4}
\]

in the bulk and the normalized seam-height error is at most `eta_n`. This is possible because, when piece `n` is designed, all earlier deterministic quantiles are already known, while `K_n` and the lower search scale may be enlarged arbitrarily. Choose the endpoint and flat-bridge tolerances tending to zero as in the strict construction.

As before choose deterministic `U_n` with `P(T_n>U_n)<=2^{-n}`. Borel--Cantelli implies that all sufficiently late pieces are good. The same seam/bulk inequalities then give, for all sufficiently large backward times lying in piece `n`,

\[
\frac{|X_{-u}|}{\sqrt u}
\le
w(\log u)+\epsilon_n+O(\eta_n).
\tag{9.5}
\]

As `u->infinity`, the piece index also tends to infinity. Therefore

\[
\boxed{
\limsup_{u\to\infty}
\left(
\frac{|X_{-u}|}{\sqrt u}-w(\log u)
\right)\le0
}
\quad\text{a.s.}
\tag{9.6}
\]

for one decomposable FBM. If `Lambda(w)<1`, T91 is stronger and immediately implies (9.6).

Combining (F2), (9.6), and T91 gives the source-facing statement.

### Theorem T92 — symmetric periodic-Floquet analogue of Burdzy--Scheutzow Theorem 4.3

Let `w:R->(0,infinity)` be nonconstant, `P`-periodic and Lipschitz, let `D_w` be (4.1), and let `Lambda(w)` be the principal Floquet killing exponent of stationary OU in `(-w(r),w(r))`.

1. **Supercritical / critical universal direction.** If `Lambda(w)>=1`, every FBM `X` satisfies

\[
\limsup_{u\to\infty}
\left(
\frac{|X_{-u}|}{\sqrt u}-w(\log u)
\right)\ge0
\quad\text{a.s.}
\tag{9.7}
\]

2. **Subcritical / critical existence direction.** If `Lambda(w)<=1`, there exists a decomposable FBM `X` satisfying

\[
\limsup_{u\to\infty}
\left(
\frac{|X_{-u}|}{\sqrt u}-w(\log u)
\right)\le0
\quad\text{a.s.}
\tag{9.8}
\]

3. **Strict-subcritical exact confinement.** If `Lambda(w)<1`, there exists a decomposable FBM `X` satisfying

\[
|X_{-u}|\le\sqrt u\,w(\log u)
\qquad\forall u\ge0
\quad\text{a.s.}
\tag{9.9}
\]

For constant `w=c`, this reduces to the symmetric specialization `(c_1,c_2)=(-c,c)` of Theorem 4.3. For nonconstant `w`, the boundary is genuinely log-periodically corrugated and cannot be obtained from a parabola by a fixed Brownian scaling or affine space-time rescaling.

This is a **complete internal theorem candidate**, not a fleet closure claim. The periodic slow-point and Floquet lemmas it depends on are themselves fully written in the preceding immutable R07 reports but have not yet received the required two independent audits.

## 10. Why the fixed metric remains 59

The log-periodic square-root-tube family was already counted as one nonparabolic family in `runs/R07/20260916T2226Z_i0077_log_periodic_pulses_06.md`. T92 upgrades that already-counted family from a restricted theorem to a full source-style three-clause threshold theorem. Counting it again as family 60 would violate the frozen equivalence/no-double-count convention.

Therefore the honest metric is

\[
\boxed{59\to59.}
\]

The supported unchanged count is now

\[
\boxed{5\to6.}
\]

This is the closable retirement threshold.

## 11. Six-run terminal handoff and rotation state

Under `operations/NEW_METHODS_2026-09-16.md`, a CLOSABLE target retires after six unchanged runs. Therefore **R07 performs no further I0077 research after this report**. The mathematical package is handed off in its present state:

- exact source and definitions recovered;
- 59 counted nonparabolic families in the historical metric;
- a full three-clause periodic-Floquet theorem candidate T92 now written;
- strict-subcritical exact confinement gap repaired by random re-rooting (T91-R + T91-A + T91);
- no finite arithmetic core requiring a checker in this run;
- current literature / prior-art pass recorded;
- independent audits: **0/2**;
- publication novelty: **UNVERIFIED**;
- source/fleet status: **PARTIAL / FULL-THEOREM CANDIDATE / NOT CLOSED**.

A future P26 audit plus one genuinely different OTHER-track audit should check, in particular: (a) the period-lattice extension in T91-A; (b) the orientation and endpoint bookkeeping in (8.2)--(8.5); (c) the flat/bulk split (8.6)--(8.10); and (d) the varying-profile critical construction (9.2)--(9.6). Those audits should not be performed by R07 itself.

Rotation cannot honestly claim a new target this run because the current coordinator snapshot reports **zero newly certified free READY** candidates. Several apparently high-ranked queue rows are now owned or held (for example I0035 is reserved to C31). So the correct rotation action is: retire I0077 research, preserve this handoff, and on the next invocation perform admission screening in queue order until a genuinely free CLOSABLE outside target passes source/current-literature/prior-attempt/ownership checks. Do not keep adding I0077 refinements merely because the native prompt still names it.

## 12. Model / scheduler / permission truth

The exposed scheduler control surface still offers task title/prompt, schedule or start offset, enabled state, and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model receipt**. Therefore `GPT-6 / maximum` remains prompt-only and I report the actual available metadata as GPT-5.6 Sol / reasoning UNVERIFIED.

The historical P26 `You cannot modify this task` result was authorization-context-specific. The current repository records that a later authorized P/C context successfully updated P26, while another context denied R-series edits. The legitimate workaround for a still-denied task is its owning/authorized workspace/account, an authorized ownership/admin correction, or platform support. No permission bypass, duplicate schedule, or scheduler modification was attempted here.

```yaml
ledger_delta:
  worker: R07
  allocation: CLOSABLE_OUTSIDE
  source_id: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem, modulo frozen no-rescaling/no-double-count convention"
  before: 59
  after: 59
  movement: false
  unchanged_count_before: 5
  unchanged_count_after: 6
  section_B_moves: [12, 23, 3]
  status_before: "PARTIAL / STUCK-RECOVERY-2"
  status_after: "PARTIAL / FULL-THREE-CLAUSE-CANDIDATE / AUDIT-PENDING / R07-RETIRED-HANDOFF"
  new_results:
    - "T91-R: decomposability is invariant under arbitrary random re-rooting"
    - "T91-A: global periodic slow anchors with small endpoint, periodic analogue of source (4.13)"
    - "T91: exact strict-subcritical confinement in nonconstant log-periodic square-root tubes"
    - "T92: complete symmetric periodic-Floquet three-clause analogue of Theorem 4.3"
  finite_core_checker: "none; analytic proof, no substantive finite core"
  audits_other_tracks: "0/2"
  novelty: UNVERIFIED
  ownership: "I0077 remains canonical R07 reservation; PENDING_ADMISSION text preserved"
  retirement: "six unchanged runs reached; no further R07 I0077 research"
  rotation: "successor admission required; no free READY target certified in current coordinator snapshot"
  delivery: "private GitHub only"
```
