Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen source metric: `beta_MST^- >= eta -> beta_MST^- >= eta`; methods B9 / B12 / B28.**

# HARD7-04 — BHS heavy-tailed configuration-model MST universality — MD5 and post-giant one-collar geometry

**Status:** PARTIAL / source OPEN / STUCK2 RECOVERY  
**Canonical claim:** `operations/claims/BHS-MST-CM-UNIV.md`  
**Owner:** HARD7-04  
**Frozen quantity:** `beta_MST^-`  
**Before:** `beta_MST^- >= eta`, `eta=(tau-3)/(tau-1)`.  
**After:** `beta_MST^- >= eta`. **No movement.**

This run makes substantive route progress despite no source-metric movement. For the explicit Pareto-quantile subclass and the concrete mesoscopic scale `epsilon_n=(log n)^3 n^{-eta}`, it proves the five-mark outside-principal-component profile **MD5** at `o_P(epsilon_n n)` accuracy. It then converts the resulting strict two-type collar deficit into an exact finite-matching diameter bound on the **post-giant residual**:

\[
\Delta_{\max}\bigl(G_{A\cup B}[V_{\rm post}]\bigr)
 =O_P(\varepsilon_n^{-1}\log n)
 =O_P\!\left(\frac{n^\eta}{(\log n)^2}\right)
 =o_P(n^\eta).
\]

The qualification `V_post` is essential. An earlier immutable idea checkpoint in this same run briefly overstated the result to all outside-giant vertices and used the outside `B`-stub pool as a pairing denominator. I caught that error before the report, preserved the immutable checkpoint, and wrote a correction at commit `b91a5e76237b3ec403525adebfb3bdb7d759421d`. Only the corrected post-giant statement is promoted here.

## 1. Continuity, required reads, ownership, and source status

This execution resumed the newest HARD7-04 state rather than restarting admission. I re-read the current versions of:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the active claim `operations/claims/BHS-MST-CM-UNIV.md`;
- the current HARD7-04 chain through `2026-09-19T2030Z__bhs_mst_cm_colored_matching_dual_operator.md` and the subsequent immutable idea checkpoints;
- the newest visible neighboring HARD7-03 report `20260919T2123Z__d0025-central-double-outrunner-local-minimum.md`;
- the newest visible neighboring HARD7-05 report `2026-09-19T2148Z__softening_frontier_164700.md`;
- targeted intake/queue records and repository searches for `I0049`, the Bhamidi--Sen title/arXiv ID, `configuration model MST heavy-tailed`, and the canonical claim key.

The connector does not expose a useful way to byte-materialize every very large intake JSONL plus the entire repository in one bounded invocation, so I do not claim a literal byte-for-byte full-repository dump. The controlling ledgers, posting register, queue, active claim, own chain, neighboring hard tracks, and target/alias intake searches were checked.

`I0049` remains unsuitable: repository task-health records already mark it `KNOWN / RESOLVED IN QUEUED SCOPE`, and a fresh external check confirms that Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937 (22 Dec 2025), covers uniformly grown random graphs within its sparse-growing-graph class and determines the critical window. I0049 is not reopened.

The active claim remains exclusively owned by HARD7-04. No release, competing canonical owner, posted equivalent, or equivalent claimed target appeared in the current searches.

### Primary source and dated current-literature check

Primary source remains:

Shankar Bhamidi and Sanchayan Sen, *Geometry of the minimal spanning tree in the heavy-tailed regime: new universality classes*, Probab. Theory Relat. Fields 188 (2024), 729--804, DOI `10.1007/s00440-024-01259-3`, arXiv:`2009.10696`.

The paper treats a rank-one heavy-tailed model and identifies configuration models / simple graphs with prescribed heavy-tailed degrees as the next expected universality class. The source warning that the critical maximal-component limit is not by itself sufficient, because the complement must be controlled through the MST construction, is exactly the obstruction retained here.

Fresh searches on 19--20 September 2026 used the exact Bhamidi--Sen title together with

- `configuration model MST heavy-tailed 2025 2026`,
- `configuration model minimum spanning tree heavy-tailed tau 3 4`,
- `minimal spanning tree configuration model heavy-tailed random graph`,
- and the author/title variants.

They recovered the 2024 source, the critical heavy-tailed configuration-model metric literature, the finite-third-moment/random-regular MST line, and no later theorem matching the `tau in (3,4)` configuration-model MST scaling-limit target. This is bounded dated negative evidence, **not** a worldwide novelty certificate.

Two nearest published engines were rechecked:

1. Bhamidi--Dhara--van der Hofstad--Sen, *Universality for critical heavy-tailed network models: Metric structure of maximal components*, Electron. J. Probab. 25 (2020), Article 47, DOI `10.1214/19-EJP408`, arXiv:`1703.07145`. It proves critical configuration-model metric universality and refined barely-subcritical diameter estimates.
2. van der Hofstad--Janson--Luczak, *Component structure of the configuration model: Barely supercritical case*, Random Structures & Algorithms 55 (2019), 3--55, DOI `10.1002/rsa.20837`, arXiv:`1611.05728`. Its continuous-time exploration supplies the deterministic-time independence and the large-component start/end-time control used below. In particular its Theorem 5.4 discussion states that the large component starts within `o_P` of the natural exploration time scale and ends at that scale times `1+o_P(1)`.

No folklore mechanism below is presented as a novelty claim: deferred decisions for uniform matchings, the continuous-time configuration-model exploration, and first-moment path counting are standard. The contribution of this track is the source-specific assembly and quantitative heavy-tail bookkeeping.

## 2. Runtime / scheduler capability honesty

The exposed task surface still offers title/prompt, schedule/timing mode, and enabled state. It exposes **no binding model selector, no reasoning-effort selector, no authenticated reasoning telemetry, and no guaranteed execution-duration field**. Therefore GPT-6/maximum remains prompt-requested only. This run identifies as GPT-5.6 Sol and has no authenticated reasoning-effort telemetry, hence `UNVERIFIED`.

Making GPT-6/maximum binding would require a product/runtime scheduler or API that actually exposes authenticated model and reasoning-effort controls. Repository edits cannot manufacture those fields. Historical `You cannot modify this task` failures, including the earlier P26 context, are authorization/context restrictions; current `RESULTS.md` records that P26 later succeeded from another authorized context. The compliant workaround is the owning/authorized account or workspace, or platform support, never a duplicate schedule or permission bypass. No schedule was created, modified, disabled, re-enabled, or probed in this run.

## 3. Frozen source quantity and Section-I accounting

The fixed source metric remains

\[
\beta^-_{\rm MST}:=\sup\left\{\beta\ge0:
\forall \delta_0\in(0,1)\ \exists c_{\delta_0}>0,
\ \liminf_n\Pr\bigl(\operatorname{diam}(M_n)\ge c_{\delta_0}n^\beta\bigr)
\ge1-\delta_0\right\}.
\]

The 16:31Z run proved

\[
\beta^-_{\rm MST}\ge \eta:=\frac{\tau-3}{\tau-1},
\]

which is already the source-predicted lower exponent. The later runs have attacked the missing upper/tightness side and full scaling-limit universality. This run does not prove an MST upper bound or Hausdorff convergence, so the metric honestly remains

\[
\boxed{\beta^-_{\rm MST}\ge\eta\quad\longrightarrow\quad\beta^-_{\rm MST}\ge\eta.}
\]

The 19:30Z report triggered STUCK1; the 20:30Z colored-matching run executed the first recovery and replaced the stopped available-degree blocker by the static five-mark profile MD5. This run is the **second permitted hard-task recovery**. It discharges MD5 for the explicit Pareto subclass and proves a post-giant one-collar geometric consequence, but the frozen source metric still does not move. Under Section I, a further unchanged-metric BHS auxiliary-lemma run is not permitted: the next invocation must hand off/rotate before doing more mathematics on this target unless the source has meanwhile been externally resolved or closure has actually been obtained.

## 4. Fresh 90% methods — B9 / B12 / B28

The previous BHS triple was B5/B8/B21. This run uses a different triple.

### B9 — RANDOMIZE

Instead of writing five coupled exploration martingales, randomize twice: first through independent edge colors on the exact uniform matching, then through the continuous-time maximal-lifetime representation of the lower-color configuration model. This creates deterministic-time independent sleeping indicators. **Successful.** It reduces all five marked sums to Laplace-weighted concentration plus a small exploration discrepancy.

### B12 — FIND WHAT IS CONSERVED

The useful invariant is not the old scalar stopped `available-degree` ratio. It is the collection of half-edge factorial/mixed moments, together with the fact that deferred uniform matchings retain exact finite-population symmetry. **Successful.** MD5 transfers to a rank-one two-type collar matrix with row sum `1-(tau-3-delta+o_P(1))epsilon_n`, and the same moment structure drives an exact path count.

### B28 — REPLACE FOR ALL WITH TYPICAL

The source needs a high-probability asymptotic theorem, not a deterministic statement for every matching. I therefore target simultaneous `o_P(epsilon_n n)` control of the five marks and a high-probability good-profile event, instead of impossible worst-case matching bounds. **Successful for MD5 and the post-giant one-collar geometry.** It does not by itself give the uniform Kruskal-level control still required for the full source target.

### Counterexample pressure came first

Two possible negations were tested.

1. A few hubs awakened before the principal lower component could carry enough quadratic marked mass to destroy the five-moment dual profile. The early-awakening estimate below shows their total original squared-degree mass is `o_P(epsilon_n n)`.
2. Even with a strict collar spectral deficit, a rare finite matching might create a path much longer than `epsilon_n^{-1} log n`. The corrected finite-matching color-word count below makes the expected number of such post-giant paths tend to zero.

Neither attacks the source statement itself; they attack the two most plausible failure modes of the current proof route.

## 5. Explicit Pareto-quantile scale retained from 18:30Z

Write

\[
r=\tau-1\in(2,3),\qquad \beta=r-2=\tau-3,\qquad
a=1/r,\qquad \eta=\beta/r.
\]

For the explicit deterministic subclass,

\[
A_n(k)=\#\{v:d_v\ge k\}=Cnk^{-r}+O(1)
\]

up to `K_n=Theta(n^a)`. Set

\[
\varepsilon_n=\lambda_n n^{-\eta},\qquad \lambda_n=(\log n)^3,
\qquad p_n=\frac{1+\varepsilon_n}{\nu_n}.
\]

Let

\[
h_n(s)=\frac1{L_n}\sum_v d_v s^{d_v-1},
\]

and let `psi_n` solve

\[
\psi_n=h_n(1-p_n+p_n\psi_n).
\]

Put

\[
t_n=-\log\psi_n,\qquad q_n=1-p_n+p_n\psi_n.
\]

The already proved finite-`n` Abelian estimate gives

\[
\varepsilon_n\asymp t_n^\beta,\qquad
t_n=n^{-1/r}z_n,\qquad z_n\to\infty,
\]

with polylogarithmic `z_n` here. Define the natural five-mark error scale

\[
b_n:=nt_n^\beta\asymp n\varepsilon_n.
\]

## 6. The five-mark static Laplace law

Color original matched edges `A` with probability `p_n`. At a vertex let `X_v` be the number of incident `A` half-edges and `R_v=d_v-X_v`. Define

\[
w_1=X,\quad w_2=X(X-1),\quad w_3=R,\quad
w_4=XR,\quad w_5=R(R-1),
\]

and for `psi=e^{-t}`

\[
F_j(t):=\sum_v w_j(X_v,R_v)e^{-tX_v}.
\]

If incident colors were independent by half-edge, `X_v\sim\mathrm{Bin}(d_v,p)` and differentiation of `(1-p+p\psi)^d` gives exactly

\[
\begin{aligned}
M_1&=pL\psi^2,\\
M_2&=p^2L\psi^2 h_n'(q),\\
M_3&=(1-p)L\psi,\\
M_4&=p(1-p)L\psi h_n'(q),\\
M_5&=(1-p)^2L h_n'(q).
\end{aligned}
\tag{6.1}
\]

In the actual edge-coloring, non-loop incident edges have independent colors; a self-loop is the only local reason two half-edge color indicators at one vertex coincide. For each of the five functions `g_{j,d}(x)=w_j(x,d-x)e^{-tx}`, changing `x` by one or two satisfies the uniform bound

\[
|g_{j,d}(x+m)-g_{j,d}(x)|
\le C d(1+td)e^{-t x+2t},\qquad m=1,2.
\tag{6.2}
\]

The expected self-loop correction is bounded by

\[
\frac{C}{L_n}\sum_v d_v^3(1+t_nd_v)
=O\!\left(K_n^{3-r}+t_nK_n^{4-r}\right)
=o(b_n).
\tag{6.3}
\]

Conditional on the underlying matching, edge colors are independent. Efron--Stein with (6.2) yields

\[
\operatorname{Var}(F_j(t_n)\mid M)
\le C\sum_v d_v^3(1+t_nd_v)^2 e^{-c t_nd_v}
=O(nt_n^{r-3}).
\tag{6.4}
\]

Since

\[
\frac{nt_n^{r-3}}{b_n^2}
=\frac1{nt_n^{r-1}}\longrightarrow0,
\tag{6.5}
\]

Chebyshev and a union bound over the five fixed marks give simultaneously

\[
\boxed{F_j(t_n)=M_j+o_P(b_n),\qquad j=1,\ldots,5.}
\tag{6.6}
\]

No finite simulation is being promoted here.

## 7. Stability of the empirical extinction time

Conditional on `X=(X_v)`, the `A` graph is a uniform configuration model with degree sequence `X`. Let `psi_X` be the nontrivial extinction root of its empirical excess pgf and `t_X=-\log\psi_X`.

Use the root numerator

\[
Z_X(s):=\sum_v X_v\bigl(s^{X_v-1}-s\bigr).
\]

Its ideal mean is

\[
\mathbb E Z_X(s)=pL\{h_n(1-p+ps)-s\}+o(nt_n^{r-1}),
\tag{7.1}
\]

where the displayed error includes the same negligible loop correction. The 18:30Z Abelian expansion gives, uniformly for fixed `u` in a neighborhood of one,

\[
1-p_n h_n'\!\left(1-p_n+p_ne^{-u t_n}\right)
=\varepsilon_n\{(\beta+1)u^\beta-1\}+o(\varepsilon_n).
\tag{7.2}
\]

Therefore for every fixed small `gamma>0`, at

\[
s_-=e^{-(1+\gamma)t_n},\qquad
s_+=e^{-(1-\gamma)t_n},
\]

the deterministic root numerator has opposite signs and magnitude at least

\[
c_\gamma n\varepsilon_nt_n
=c_\gamma n t_n^{r-1}.
\tag{7.3}
\]

The cancellation `Z_X(1)=0` is important. Flipping one edge color changes `Z_X(e^{-ut_n})` by at most `C min(1,t_nd_v)` at an incident vertex, so

\[
\operatorname{Var} Z_X(e^{-ut_n})
\le C\sum_v d_v\min(1,t_nd_v)^2
=O(nt_n^{r-1}).
\tag{7.4}
\]

Because `nt_n^{r-1}->infinity`, the standard deviation in (7.4) is little-o of the signal in (7.3). Thus the two signs persist with probability tending to one. Convexity of the empirical excess pgf brackets its unique subunit root and gives

\[
\boxed{t_X/t_n\longrightarrow1\quad\text{in probability}.}
\tag{7.5}
\]

## 8. Continuous-time exploration and the giant endpoint

The thinned degree sequence `X` satisfies the hypotheses of the van der Hofstad--Janson--Luczak barely-supercritical theorem with probability tending to one in this retained subclass. Briefly:

- fixed-degree empirical frequencies converge to the corresponding binomial thinning of the original law;
- `X_v<=d_v` preserves the uniformly bounded second moment;
- nondegeneracy holds, and because `p_c<1` with original minimum degree at least three, the thinned limit has positive degree-one mass;
- the empirical branching excess is `epsilon_n+o_P(epsilon_n)` by the same color concentration;
- the heavy-tail third-moment scale is the one treated in their power-law example, while `epsilon_n/n^{-eta}=lambda_n=(log n)^3->infinity`, so the process is outside the heavy-tail critical window.

Their continuous-time construction and Theorem 5.4 imply that the principal component exploration begins at a time

\[
T_1=o_P(t_X)
\]

and ends at

\[
T_2=t_X(1+o_P(1)).
\]

By (7.5),

\[
T_1=o_P(t_n),\qquad T_2/t_n\to1.
\tag{8.1}
\]

## 9. Sleeping five-mark sums at the random endpoint

Assign the lower `A` half-edges independent exponential maximal lifetimes in the continuous-time representation. Conditional on `X`, let

\[
I_v(s)=\mathbf 1\{\text{all }X_v\text{ maximal lifetimes exceed }s\},
\qquad
\widetilde F_j(s)=\sum_v w_j I_v(s).
\]

At deterministic `s`, the indicators are independent and

\[
\mathbb E[\widetilde F_j(s)\mid X]
=\sum_v w_j e^{-sX_v}.
\]

A weighted Chernoff bound gives, with probability tending to one, `X_v>=c d_v` for all `d_v>=A log n`. Splitting small and large original degrees then yields uniformly for `s` comparable to `t_n`,

\[
\operatorname{Var}(\widetilde F_j(s)\mid X)
\le Cn s(\log n)^5+Cns^{r-4}.
\tag{9.1}
\]

The heavy-tail term is the decisive one:

\[
\frac{nt_n^{r-4}}{b_n^2}
=\frac1{nt_n^r}=z_n^{-r}\to0.
\tag{9.2}
\]

Also, for `|s-t_n|<=gamma t_n`,

\[
|F_j(s)-F_j(t_n)|
\le \gamma t_n\sum_v w_jX_v e^{-(1-\gamma)t_nX_v}
=O(\gamma b_n)+o(b_n).
\tag{9.3}
\]

Monotonicity of the sleeping indicators and a deterministic shrinking sandwich now imply that every random `T` with `T/t_n->1` satisfies

\[
\widetilde F_j(T)=M_j+o_P(b_n),\qquad j=1,\ldots,5.
\tag{9.4}
\]

In particular (9.4) holds for `T=T_2`.

## 10. B28 payoff: kill the pre-giant marked correction without a five-martingale theorem

Let

\[
P_n:=\sum_{v\text{ in components completed before the principal component}}d_v^2.
\]

From `T_1/t_n->0`, choose deterministic `gamma_n downarrow0` so that

\[
\Pr(T_1>\gamma_nt_n)\to0,
\]

and put `s_n=gamma_nt_n`.

Before sleeping `A`-half-edge mass drops below half its initial value:

- a vertex can be awakened by a spontaneous C3 event by time `s` only if one of its `X_v` maximal lifetimes expires, with probability at most `sX_v`;
- the number of C1 component starts is at most one plus the number of C3 events;
- the expected number of C3 events by time `s` is at most `L_A s`;
- at a C1 start, the conditional chance of selecting a specified sleeping vertex is at most `2X_v/L_A`.

Hence

\[
\Pr(v\text{ awake by }s\text{ before the stop}\mid X)
\le C\left(sX_v+\frac{X_v}{L_A}\right)\wedge1.
\tag{10.1}
\]

The Pareto tail gives the deterministic weighted estimate

\[
\sum_v d_v^2\min(1,sd_v)\le Cns^\beta,
\qquad s=o(1),
\tag{10.2}
\]

including the case `s<1/K_n`. Also

\[
L_A^{-1}\sum_vd_v^3=o(b_n).
\tag{10.3}
\]

Combining (10.1)--(10.3) at `s=s_n`, the expected original squared-degree mass awakened before the giant starts is

\[
O(ns_n^\beta)+o(b_n)
=O(\gamma_n^\beta b_n)+o(b_n)
=o(b_n).
\tag{10.4}
\]

The same argument with weight `X_v` shows that the auxiliary half-mass stop is not reached by `s_n` with high probability. Markov therefore gives

\[
\boxed{P_n=o_P(b_n).}
\tag{10.5}
\]

This rules out the hub-driven counterexample to MD5.

## 11. Theorem 1 of this run: MD5

Immediately before `T_2`, the actually sleeping vertices are the post-giant components. In the maximal-lifetime construction, the surrogate sleeping set can differ from the actually sleeping set only through C1-start vertices; every C3-awakened vertex has had a spontaneous lifetime expiration.

Each mark satisfies `w_j<=d_v^2`. Through the pre-giant phase the discrepancy is at most `P_n`; during the principal component there is no C1 restart. Adding back the completed pre-giant components contributes another `P_n`. The boundary vertex/start convention contributes at most `d_max^2`, and

\[
d_{\max}^2=\Theta(n^{2/r})=o(b_n)
\]

because `b_n=n^{2/r}z_n^\beta` with `z_n->infinity`.

Thus, using (9.4), (10.5), and (6.1), all five actual outside-principal-component sums satisfy

\[
\boxed{
\begin{aligned}
\sum_{v\notin C_A}X_v
 &=p_nL_n\psi_n^2+o_P(\varepsilon_n n),\\
\sum_{v\notin C_A}X_v(X_v-1)
 &=p_n^2L_n\psi_n^2h_n'(q_n)+o_P(\varepsilon_n n),\\
\sum_{v\notin C_A}R_v
 &=(1-p_n)L_n\psi_n+o_P(\varepsilon_n n),\\
\sum_{v\notin C_A}X_vR_v
 &=p_n(1-p_n)L_n\psi_nh_n'(q_n)+o_P(\varepsilon_n n),\\
\sum_{v\notin C_A}R_v(R_v-1)
 &=(1-p_n)^2L_nh_n'(q_n)+o_P(\varepsilon_n n).
\end{aligned}}
\tag{MD5}
\]

This discharges the 20:30Z MD5 blocker for the explicit Pareto-quantile subclass and `lambda_n=(log n)^3`.

## 12. From MD5 to the actual two-type collar deficit

Use the exact colored-matching decomposition from the preceding run. Conditional on the `A` data, the `B` half-edge set is a hypergeometric sample of the non-`A` half-edges, and its matching is fresh and uniform. The five moment estimates above have fluctuation margin `o_P(epsilon_n n)`, so standard without-replacement concentration transfers them to the actual `A/B` mixed factorial moments.

Take

\[
p_n^+=\frac{1+(1+\delta)\varepsilon_n}{\nu_n},
\qquad
\Delta_n=p_n^+-p_n=\frac{\delta\varepsilon_n}{\nu_n},
\qquad 0<\delta<\beta.
\]

The ideal two-type matrix is

\[
h_n'(q_n)
\begin{pmatrix}
p_n&\Delta_n\\p_n&\Delta_n\end{pmatrix}.
\]

The 18:30Z finite-`n` duality calculation gives

\[
p_nh_n'(q_n)=1-(\beta+o(1))\varepsilon_n,
\qquad
\Delta_nh_n'(q_n)=(\delta+o(1))\varepsilon_n.
\]

Therefore its row sum, and after MD5 the actual effective row sum, is

\[
1-(\beta-\delta+o_P(1))\varepsilon_n.
\tag{12.1}
\]

For any fixed `c_0<(beta-delta)/2`, with high probability this is at most `1-c_0 epsilon_n`.

## 13. Correction before promotion: the pairing pool matters

The first immutable idea checkpoint of this run, commit `98dd0f657c2e788b1b340800f6b214570ed3d72b`, attempted to turn (12.1) into an all-outside one-collar path bound. On rereading the finite matching law I found two scope errors:

1. a specified `B` pair is drawn from the **total** `B` matching pool, not merely the outside `B` pool;
2. the exact deferred-decision uniformity for the `A` matching after principal-component exploration applies to the still-unexplored **post-giant residual**, whereas pre-giant components have already been exposed.

I did not overwrite the checkpoint. The correction was committed as

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T2208Z__bhs_mst_cm_one_collar_diameter_correction.md`

at commit `b91a5e76237b3ec403525adebfb3bdb7d759421d` and read back successfully. Only the corrected statement below is part of this report's promoted mathematics.

## 14. Theorem 2 of this run: post-giant one-collar diameter

Let `V_post` be the vertices still sleeping immediately after the principal lower `A` component finishes. Conditional on the exploration history through `T_2`, the residual `A` half-edges on `V_post` have a uniform perfect matching by deferred decisions. The entire `B` matching remains independent and uniform on the total `B` half-edge set.

Write `A_v,B_v` for the residual `A` and collar-`B` half-edge counts at `v in V_post`, and

\[
S_A=\sum_{V_{post}}A_v,\qquad
S_B=\sum_{V_{post}}B_v,\qquad
L_B=\sum_vB_v.
\]

Deleting pre-giant vertices from MD5 changes every first/second mixed marked sum by at most `o_P(epsilon_n n)` because of (10.5). Hypergeometric collar sampling therefore gives the effective post-giant matrix

\[
\widehat M_{post}=
\begin{pmatrix}
\frac{\sum A_v(A_v-1)}{S_A}&
\frac{S_B}{L_B}\frac{\sum A_vB_v}{S_A}\\
\frac{\sum A_vB_v}{S_B}&
\frac{\sum B_v(B_v-1)}{L_B}
\end{pmatrix}
=h_n'(q_n)
\begin{pmatrix}p_n&\Delta_n\\p_n&\Delta_n\end{pmatrix}
+o_P(\varepsilon_n)
\tag{14.1}
\]

entrywise. The `S_B/L_B` factor is exactly the probability that an outgoing `B` stub pairs back into `V_post`; in the `B->B` entry it cancels the `S_B` size-bias denominator. Consequently

\[
\|\widehat M_{post}\|_\infty\le1-c_0\varepsilon_n
\tag{14.2}
\]

with high probability for fixed `c_0<(beta-delta)/2`.

Now let `N_ell^post` be the number of oriented vertex-simple `(A,B)` paths of length `ell` staying in `V_post`. Conditional on the exploration history and the colored degree profile, a fixed color word requiring `m_A` distinct residual `A` pairs and `m_B` distinct `B` pairs has exact pairing probability

\[
\prod_{j=0}^{m_A-1}(S_A-(2j+1))^{-1}
\prod_{j=0}^{m_B-1}(L_B-(2j+1))^{-1}.
\tag{14.3}
\]

Dropping vertex-distinctness only enlarges the first moment. Summing over candidate vertices and color words produces the factorial/mixed sums in (14.1), hence

\[
\mathbb E[N_\ell^{post}\mid\text{good profile, history}]
\le Cn R_\ell\|\widehat M_{post}\|_\infty^{\ell-1},
\tag{14.4}
\]

where the finite-population correction satisfies

\[
\log R_\ell=O(\ell^2/S_A+\ell^2/L_B).
\tag{14.5}
\]

Here `S_A=Theta(n)` and `L_B=Theta(epsilon_n n)`. Choose

\[
\ell_n=\left\lceil K\varepsilon_n^{-1}\log n\right\rceil.
\]

Since `eta<1/3`,

\[
\frac{\ell_n^2}{L_B}
=O\!\left(\frac{\varepsilon_n^{-3}(\log n)^2}{n}\right)
=O\!\left(\frac{n^{3\eta-1}}{(\log n)^7}\right)\to0,
\tag{14.6}
\]

and `ell_n^2/S_A->0`. Thus `R_{ell_n}=1+o(1)`. From (14.2)--(14.4),

\[
\mathbb E[N_{\ell_n}^{post}\mid\text{good profile, history}]
\le Cn\exp\{-c_0\varepsilon_n\ell_n+o(1)\}.
\]

Taking `K>3/c_0` makes the right side tend to zero. Markov gives `N_{ell_n}^{post}=0` with probability tending to one. Any graph component of diameter at least `ell_n` contains a vertex-simple shortest path of that length. Therefore

\[
\boxed{
\Delta_{\max}(G_{A\cup B}[V_{post}])
=O_P(\varepsilon_n^{-1}\log n)
=O_P\!\left(\frac{n^\eta}{(\log n)^2}\right)
=o_P(n^\eta).}
\tag{14.7}
\]

This is a theorem-sized asymptotic argument on the page. It is not a finite-size fit, a Galton--Watson heuristic, or an exhaustive finite certificate.

## 15. What remains: exact STUCK2 blocker

The source-level obstruction is now sharper. MD5 and one post-giant mesoscopic collar are not the full MST approximation theorem.

### (a) Exact blocking statement

A source-matching configuration-model upper approximation would in particular imply, for every `varepsilon>0`,

\[
\boxed{
\lim_{\lambda\to\infty}\limsup_{n\to\infty}
\Pr\!\left(n^{-\eta}d_H(M_{n,\lambda},M_n)>\varepsilon\right)=0.}
\tag{15.1}
\]

Here `M_{n,lambda}` denotes the MST structure retained through a fixed critical-window level under the source normalization, and `M_n` is the final giant-component MST.

### (b) Routes already tried and why each stops

- **B1/B2/B19:** deterministic Kruskal filtration inheritance transferred the published critical diameter to the final MST and proved the lower exponent `beta_MST^- >= eta`; it gives no upper attachment control.
- **B6/B20/B30:** deformation away from the critical point found the correct postcritical dual deficit, but only at the deterministic generating-function level.
- **B3/B11/B25:** finite-`n` Pareto Abelian duality proved the mesoscopic coefficient `tau-3`, but the actual stopped lower graph had not yet been transferred.
- **B4/B13/B18:** isolated the stopped available-degree obstruction and triggered STUCK1; the scalar quantity was too representation-dependent.
- **B5/B8/B21:** exact edge-color-first decomposition removed that stopping-time obstruction and produced the two-type collar matrix, but left the static five-mark profile MD5.
- **B9/B12/B28 (this run):** continuous-time clocks plus the early-awakening estimate prove MD5; deferred decisions plus exact color-word path counting prove the post-giant one-collar diameter bound. They still do not control pre-giant geometry or the entire sequence of Kruskal thresholds in the source order of limits.

### (c) What a proof must contain that no route yet contains

It needs a **uniform attachment-height mechanism** that simultaneously:

1. controls components exposed before the principal barely-supercritical component, not merely their aggregate quadratic marked mass;
2. iterates collar control from a fixed large critical-window parameter `lambda` through mesoscopic levels without losing the `n^eta` scale;
3. handles the dependence created by repeated configuration-model matching / deletion while keeping the dual deficit quantitatively uniform;
4. sums or maximizes the resulting attachment heights to prove (15.1), rather than only a single-level component bound.

### (d) Simplest special case still unproved

For the **same explicit Pareto-quantile subclass used in this run**, prove (15.1). A still narrower sufficient milestone is: start from a fixed large critical-window `lambda`, use a deterministic geometric sequence of threshold collars up to `lambda_n=(log n)^3`, control both pre- and post-principal residual component diameters at every level, and show the total attachment height is `o_P(n^eta)` uniformly before passing to the full graph.

### (e) Nearest solved problem and missing ingredient

The nearest solved source-side object is the **rank-one heavy-tailed MST theorem in Bhamidi--Sen 2024**, whose upper approximation theorem controls the Hausdorff distance between a critical-window MST core and the final MST uniformly as `lambda->infinity`. Its independent-edge structure makes complement exploration and attachment-tree control much more tractable.

The nearest configuration-model geometric input is Bhamidi--Dhara--van der Hofstad--Sen 2020. Its barely-subcritical diameter theorem obtains path-count bounds in a one-sided subcritical regime and its critical theorem gives the metric core. It does not supply the repeated postcritical MST attachment ladder in (15.1).

The missing ingredient is therefore not another local moment identity. It is a configuration-model **uniform duality/height theorem across Kruskal levels**.

## 16. Section-I decision

This run is the second allowed stuck recovery on `BHS-MST-CM-UNIV`. The frozen source metric still does not move. The next HARD7-04 invocation must therefore **hand off this target and rotate to a fresh admissible external hard problem before doing new mathematics**, unless a genuine closure or external resolution is first found. The BHS handoff should preserve:

- lower exponent `beta_MST^- >= eta`;
- finite-`n` Pareto duality and coefficient `tau-3`;
- exact colored-matching decomposition;
- MD5 for `lambda_n=(log n)^3`;
- corrected post-giant one-collar diameter (14.7);
- exact remaining blocker (15.1).

This is a rotation instruction for the next invocation, **not** a reason to disable the recurring worker. No schedule was changed.

## 17. Verification / bookkeeping — deliberately the last ten percent

Idea-before-code checkpoint:

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T2130Z__bhs_mst_cm_five_mark_early_awake_idea.md`

creation commit `fb43ecaadbffac9ff70afeb10141ae2b4314fd1c`, read back successfully.

An initial one-collar path-count idea was preserved immutably at commit `98dd0f657c2e788b1b340800f6b214570ed3d72b`. Its denominator/scope issue was then corrected, not hidden or overwritten, in

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T2208Z__bhs_mst_cm_one_collar_diameter_correction.md`

creation commit `b91a5e76237b3ec403525adebfb3bdb7d759421d`, read back successfully.

No arithmetic checker was manufactured because this run promotes no finite enumeration or finite arithmetic claim. The new claims are asymptotic theorems with arguments written on the page. This follows the owner's 90/10 rule rather than producing a checker merely to prove that the task ran.

No independent closure audit is requested because the source target is not closed. No shared root ledger was edited.

### Coordinator-only ledger delta

`HARD7-04 | BHS-MST-CM-UNIV | beta_MST^- | >=eta -> >=eta (NO MOVEMENT) | PARTIAL / STUCK2 recovery; explicit Pareto subclass: MD5 proved at lambda_n=(log n)^3 and post-giant one-collar Delta_max=O_P(epsilon_n^-1 log n)=o_P(n^eta); all-outside/pre-giant + uniform Kruskal Hausdorff ladder remains; next invocation mandatory handoff/rotation if no closure.`

### External sources checked this run

- `https://arxiv.org/abs/2009.10696` — Bhamidi--Sen heavy-tailed MST source.
- `https://arxiv.org/abs/1703.07145` — critical heavy-tailed configuration-model metric universality.
- `https://onlinelibrary.wiley.com/doi/full/10.1002/rsa.20837` — barely-supercritical configuration-model exploration.
- `https://arxiv.org/abs/2512.18937` — later growing-random-graph critical-window result resolving queued I0049 scope.
