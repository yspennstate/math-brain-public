Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: the remaining one-dimensional `J` split in the last F0111 `n=30`, `N=12,13` arbitrary-heterogeneity reduction is eliminated analytically by an adaptive face ray; together with the previous capped-convex `K` extremizer, every contact-distribution variable is removed and the feasibility gate is now a two-scalar `(delta,s)` inequality. Methods #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #13 FIND WHAT ONLY INCREASES, #30 DO ONE SCALE/DIRECTION AT A TIME.**

# R15 retained screen — adaptive-ray monotonicity removes the last contact-distribution variable

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, does not solve Talagrand's discrete Convexity Conjecture, and does not satisfy the two-other-track audit rule.

The immediately preceding complete R15 report is

`runs/R15/20260920_0754Z_successor_screen_f0111_twoheavy_extremal_q102y.md`.

It used moves `#13/#24/#30`. All thirty Section-B moves have appeared somewhere in the older R15 history, so the present `#5/#13/#30` triple is a nonidentical re-entry on a new reduced object, not a claim that these move numbers have never appeared before.

The new route was written before the repository checker in

`artifacts/R15/f0111_adaptive_ray_monotonicity_idea_r103z.md`

at commit

`a9cbb784b030304d436b78658ea7e7ccb1640631`.

Only after the analytic route was fixed did I add and execute the small exact arithmetic checker in Section 9.

## 1. Repository continuity, exclusions, source, and ownership

Before new mathematics I reread or source-recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the controlling I0076 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the newest own report `runs/R15/20260920_0754Z_successor_screen_f0111_twoheavy_extremal_q102y.md`;
- the neighboring Burdzy--Scheutzow Problem 7.8 terminal handoff `runs/R07/20260919T093413Z_i0077_random_reroot_periodic_completion_59_handoff_rr59s3.md`;
- current exact-source / current-literature searches for Burdzy--Scheutzow Problem 7.2 and the 2026 discrete Convexity Conjecture literature.

`QUEUE.md` still distinguishes PENDING reserve entries from genuinely READY inventory and still records **zero newly certified free READY entries**. I therefore did not claim another worker's source, promote a PENDING row, or edit a shared root.

`POSTED.md` excludes the already-posted/settled exact claims recorded there; Problem 7.5 remains excluded. Nothing in the current posting inventory reactivates I0076 or certifies F0111 as an assignment.

## 2. Exact native I0076 source rechecked

Primary source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- FBM: there are random times `S_n -> -infinity` a.s. such that every complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there exists one random time `S` such that the complete centered future and past at `S` are independent standard Brownian motions.

Problem 7.2 asks whether **FBM + BBM + existence of an arbitrary random time `T` at which the two complete centered half-processes are independent** implies 2BM. The source does **not** make `T` a stopping time and does **not** separately assume either half at `T` is Brownian.

The nearby Proposition 6.2 proves a different stronger-seam obstruction for the Section-6 construction: it excludes a random seam having independence **and** a Brownian forward half. It neither supplies nor rules out bare Problem-7.2 independence by itself.

### Native candidate and metric state

The mandatory six-run handoff remains binding.

- The source Theorem-6.1 construction has FBM, BBM and failure of 2BM but no source-valid independent random seam.
- The later Brownian-prefix/BES candidate has FBM, BBM and an exact independent seam, but R15's Palm analysis proves that candidate is actually 2BM.

Therefore there is **no surviving frozen counterexample candidate** on which the user's four obligations can honestly be counted. Historical `2/4` and `3/4` values belong to eliminated candidates or the retired positive-route diagnostic; they are not a current frozen-candidate score.

Native status remains **OPEN / PARTIAL / RETIRED-HANDOFF**. The unchanged count stays frozen at the six-run handoff; retained-screen work does not increment it.

### Fresh dated literature pass, 2026-09-20

Queries included exact-title and exact-Problem-7.2 variants, Burdzy/Scheutzow later/citing work, and current Talagrand discrete-convexity papers. They recovered the original article, the University of Washington publication record, Ascoli--He--Park--Talagrand arXiv:2608.11183 (2026-08-11), and Park arXiv:2609.14681 (2026-09-13). I found no accessible later primary source explicitly announcing a resolution of exact Problem 7.2. That is **bounded negative evidence only**, not a worldwide openness certificate.

Ascoli--He--Park--Talagrand reformulate the broader discrete Convexity Conjecture through `k`-thresholds and prove substantial classes; Park's abstract explicitly describes its dimension-free consequence as a bound *toward* the conjecture. The restricted mechanism below therefore remains only retained-screen work; novelty is **UNVERIFIED**.

## 3. Carried q102y reduction

The retained hazard is

\[
F(t)=\sum_{i=1}^{30}t_i-\log\!\left(\sum_{i=1}^{30}e^{t_i}-29\right).
\tag{3.1}
\]

For the full-support, two-level Hessian-null first-bifurcation screen on the surviving outer scalar branch `z=1+s>1`, preceding exact reductions leave only

\[
N:=|K|\in\{12,13\},\qquad M:=|J|=30-N.
\tag{3.2}
\]

Write

\[
a=1+\delta,\qquad b=1-\delta,
\]

and retain the exact scalar quantities `x=sum_J r_i`, `y=sum_K r_j`, `A_J`, `A_K`, `L_K=A_Ky`, `U_K=-29y/k`, and

\[
S=-\frac{29}{k}.
\tag{3.3}
\]

The carried exact cell bounds are

\[
0<s<\frac3{200},\qquad
1<x<\frac{41}{40},\qquad
\frac{29}{20}<\frac{-k}{s}<\frac{13}{8},
\tag{3.4}
\]

and

\[
N=12:\quad r_*<1-15s,
\qquad
N=13:\quad r_*<1-17s.
\tag{3.5}
\]

The preceding q102y report proves that for every fixed face ray `t>1`, arbitrary `J` heterogeneity can be compressed to a two-heavy profile in the closure. Put

\[
u_i=e^{q_i},\qquad
T_2=Sx-(M-2),
\]

and

\[
c_J=S(1-C_Ns),\qquad C_{12}=15,\ C_{13}=17.
\tag{3.6}
\]

Then the only remaining `J` optimization is

\[
H_t(u)=
\frac1t\log\!\left(u^t+(T_2-u)^t-1\right)
+(t-1)U_{\max}\log u\log(T_2-u),
\tag{3.7}
\]

on the ordered feasible split interval, with

\[
U_{\max}
=\frac12\left[\left(\frac ba\right)^2y(N-L_K)-x+A_Jx^2\right].
\tag{3.8}
\]

The carried exact scalar certificate gives

\[
U_{\max}<\frac98s.
\tag{3.9}
\]

q102y also gives the exact capped-convex extremizer for the `K` entropy moment and the sharper complementary pair-energy roof

\[
E_{KK}\le \frac{y(N-1)}2\log^2\!\left(\frac{U_K}{L_K}\right).
\tag{3.10}
\]

Thus one `J` split variable was the last contact-distribution degree of freedom. This run removes it.

## 4. Move #5 — choose an adaptive ray and differentiate

Let

\[
L:=\log S,
\qquad
c:=\frac7{100},
\qquad
\varepsilon:=\frac{c}{L},
\qquad
t:=1+\varepsilon.
\tag{4.1}
\]

Since `S>1`, this is well-defined and `t>1`. The point of this choice is the exact normalization

\[
S^{\varepsilon}=e^c.
\tag{4.2}
\]

Write the ordered two-heavy split as

\[
u+v=T_2,\qquad u\ge v\ge1.
\]

Then

\[
H(u)
:=\frac1t\log(u^t+v^t-1)
+\varepsilon U_{\max}\log u\log v.
\tag{4.3}
\]

Because `dv/du=-1`, direct differentiation gives

\[
H'(u)
=
\frac{u^\varepsilon-v^\varepsilon}
{u^{1+\varepsilon}+v^{1+\varepsilon}-1}
+\varepsilon U_{\max}
\left(\frac{\log v}{u}-\frac{\log u}{v}\right).
\tag{4.4}
\]

For `x>=1`, `x^{\varepsilon-1}>=1/x`, hence

\[
u^\varepsilon-v^\varepsilon
=\varepsilon\int_v^u x^{\varepsilon-1}\,dx
\ge \varepsilon\log\frac uv.
\tag{4.5}
\]

Also `u,v<S`, so by (4.2)

\[
u^{1+\varepsilon}+v^{1+\varepsilon}-1
\le e^c(u+v).
\tag{4.6}
\]

Therefore `H'(u)>0` follows if

\[
R(u,v):=
\frac{uv\log(u/v)}{(u+v)(u\log u-v\log v)}
>e^cU_{\max}.
\tag{4.7}
\]

The rest of the proof is a uniform lower bound on `R` over both remaining scalar cells.

## 5. Move #30 — localize the split ratio with exact carried bounds

At the heavy-cap endpoint the smaller coordinate is

\[
v_*=T_2-c_J
=S(x-1+C_Ns)-(M-2).
\tag{5.1}
\]

From `-k/s<13/8`,

\[
S=\frac{29}{(-k/s)s}>\frac{232}{13s}.
\tag{5.2}
\]

Using `x>1`, this gives

\[
N=12:\quad
v_*>\frac{232\cdot15}{13}-16
=\frac{3272}{13}>250,
\tag{5.3}
\]

\[
N=13:\quad
v_*>\frac{232\cdot17}{13}-15
=\frac{3749}{13}>250.
\tag{5.4}
\]

Since the ordered feasible split has `u<=c_J<S`, the same lower bound holds for its smaller coordinate whenever the larger one is moved toward the cap. Moreover `-k/s>29/20` gives

\[
S<\frac{20}{s}.
\tag{5.5}
\]

Thus with

\[
r:=\frac uv\ge1,
\]

we have the uniform ratio roof

\[
1\le r<\frac{2}{25s}.
\tag{5.6}
\]

## 6. Move #13 — the split objective is strictly increasing

We prove

\[
R(u,v)>\frac{121}{100}s
\tag{6.1}
\]

throughout the ordered feasible interval.

### Case 1: `1<=r<=e`

For `f(x)=x\log x`, the mean value theorem gives

\[
u\log u-v\log v
\le (u-v)(\log u+1).
\tag{6.2}
\]

Also

\[
\log r\ge\frac{r-1}{r}.
\tag{6.3}
\]

Hence

\[
R(u,v)
\ge\frac1{(r+1)(\log u+1)}
>\frac1{4(L+1)},
\tag{6.4}
\]

using the elementary `e<3` and `u<S`.

From `S<20/s`,

\[
s(L+1)<s\left(\log\frac{20}{s}+1\right).
\]

The right side is increasing for `0<s<3/200`; the carried exact bound

\[
\log\frac{4000}{3}<\frac{36}{5}
\]

therefore gives

\[
s(L+1)<\frac3{200}\cdot\frac{41}{5}=\frac{123}{1000}.
\tag{6.5}
\]

Consequently

\[
\frac1{4(L+1)}>\frac{121}{100}s,
\tag{6.6}
\]

because the exact residual margin is

\[
1-4\frac{121}{100}\frac{123}{1000}
=\frac{10117}{25000}>0.
\tag{6.7}
\]

### Case 2: `r>=e`

Since `v\log v>=0`,

\[
u\log u-v\log v\le u\log u,
\]

and therefore

\[
R(u,v)
\ge
\frac{\log r}{(r+1)\log u}
>
\frac{\log r}{(r+1)L}.
\tag{6.8}
\]

The function

\[
f(r)=\frac{\log r}{r+1}
\]

has derivative with numerator `1+1/r-log r`, which is strictly decreasing. Thus `f` is unimodal, so its minimum on

\[
[e,2/(25s)]
\]

is attained at an endpoint.

At `r=e`,

\[
f(e)=\frac1{e+1}>\frac14,
\]

and Case 1's bound applies.

At the other endpoint, put `A=2/25`. Then

\[
\frac{f(A/s)}{L}
>
\frac{s}{A+s}
\frac{\log(A/s)}{\log(20/s)}.
\tag{6.9}
\]

Because

\[
A^5>20\left(\frac3{200}\right)^4,
\tag{6.10}
\]

we have for every `s<3/200`

\[
5\log(A/s)>\log(20/s).
\tag{6.11}
\]

Also `A+s<19/200`, so

\[
\frac{f(A/s)}{L}
>
\frac{40}{19}s
>
\frac{121}{100}s.
\tag{6.12}
\]

This proves (6.1) in all cases.

Finally the exact Taylor enclosure in Section 9 gives

\[
e^{7/100}<\frac{43}{40}.
\tag{6.13}
\]

Together with (3.9),

\[
e^cU_{\max}
<\frac{43}{40}\frac98s
=\frac{387}{320}s
<\frac{121}{100}s.
\tag{6.14}
\]

Comparing (6.1) and (6.14) in (4.7) yields the strict conclusion

\[
\boxed{H'(u)>0\quad\text{whenever }u>v.}
\tag{6.15}
\]

## 7. New theorem — the `J` extremizer is forced to the heavy cap

The q102y two-heavy theorem already proves that every arbitrary `J` distribution can be moved, without decreasing the adversarial face objective, into the two-heavy closure.

The present strict monotonicity then pushes that remaining split all the way to its largest allowed ordered coordinate. The two-cap inequality from q102y guarantees that this endpoint is feasible in the closure.

### Theorem R15-F0111-ADAPTIVE-EXTREMAL

For `N=12` and `N=13`, on the entire carried scalar-feasible cells, choose the adaptive ray

\[
t=1+\frac{7}{100\log S}.
\]

Then the supremum over **all** admissible `J` contact distributions of the left-favoring relaxation in the exact complement-face inequality is attained in the closure at

\[
\boxed{
u_1^*=S(1-C_Ns),
}
\tag{7.1}
\]

\[
\boxed{
u_2^*=S(x-1+C_Ns)-(M-2),
}
\tag{7.2}

and

\[
\boxed{
u_3^*=\cdots=u_M^*=1.
}
\tag{7.3}
\]

Because the actual heavy cap (3.5) is strict, an interior contact never attains this boundary profile; it is the exact **supremizing closure profile** used for an upper bound.

No within-block symmetry assumption is used.

This strictly improves q102y: the high-dimensional `J` optimization was first reduced to one scalar split, and is now reduced to **no free contact-distribution variable at all**.

## 8. The complete arbitrary-heterogeneity gate is now two-dimensional

The `K` distribution was already solved exactly in q102y. Put

\[
c_K:=\frac{U_K}{L_K},\qquad
\eta_K:=U_K-N,\qquad
d_K:=c_K-1.
\]

For `d_K>0`, let

\[
m_K:=\left\lfloor\frac{\eta_K}{d_K}\right\rfloor,
\qquad
\rho_K:=\eta_K-m_Kd_K.
\tag{8.1}
\]

Then convexity of `v\mapsto v\log v` gives the exact capped-simplex upper extremizer

\[
K_{\max}
=\frac1S
\left[
 m_Kc_K\log c_K
 +(1+\rho_K)\log(1+\rho_K)
\right].
\tag{8.2}
\]

Together with (3.10), define

\[
\overline E_K
:=\frac{y(N-1)}2\log^2c_K.
\tag{8.3}
\]

For the `J` side define `u_1^*,u_2^*` by (7.1)--(7.2) and

\[
H_J^*
:=
\frac1t\log\left((u_1^*)^t+(u_2^*)^t-1\right)
+(t-1)U_{\max}\log u_1^*\log u_2^*.
\tag{8.4}
\]

The exact complement-face inequality therefore yields the scalar necessary condition

\[
\boxed{
\log S
\le
\overline E_K+K_{\max}+H_J^*.
}
\tag{8.5}
\]

Every quantity on the right is now an explicit function of only

\[
(\delta,s),\qquad N\in\{12,13\}.
\]

There is no remaining coefficient matrix, Gram-vector choice, `J` contact distribution, `K` contact distribution, or split parameter to optimize.

This is the main movement of the run. It turns the last arbitrary-heterogeneity obstruction into a **piecewise two-variable scalar sign problem** over the already narrow exact cells.

I have **not** declared either cell eliminated. Numerical route-finding is not proof, and no such sample is counted toward a Brownian-law or F0111 verification. The next proof obligation is to certify that (8.5) fails throughout each complete scalar cell, or find a genuine scalar survivor.

## 9. Exact arithmetic self-check

Only the finite rational/exponential inequalities used above were sent to code; the theorem-sized monotonicity argument is written on the page.

Checker:

`artifacts/R15/f0111_adaptive_ray_monotonicity_checker_r103z.py`

created at commit

`22503b9abd29530d2dc86dcd29f720aad78665fa`.

Archived executed output:

`artifacts/R15/f0111_adaptive_ray_monotonicity_checker_r103z.out`

created at commit

`b359949f72620936804ca33e767441dd69bf96d5`.

The output verifies, in exact rational arithmetic:

- `e^(7/100)<43/40` by a positive-term Taylor sum plus a geometric tail bound;
- the two-cap margin `93/200`;
- the two second-heavy lower margins `22/13` and `499/13` above `250`;
- `121/100-(43/40)(9/8)=1/1600>0`;
- the Case-1 margin `10117/25000>0`;
- `(2/25)^5-20(3/200)^4=22643/10^10>0`;
- `40/19-121/100=1701/1900>0`.

It ends

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit.

## 10. What remains and next route

### Native I0076

Nothing source-valid moved. To resume exact Problem 7.2 in the future, a reassigned worker needs either:

1. a genuinely new frozen process satisfying a credible route to all four source obligations, especially bare seam independence at an arbitrary random time without imposing a stopping-time hypothesis; or
2. a proof that the source's complete hypotheses force a 2BM seam.

The retired handoff should not be reopened merely to repackage the two eliminated candidates.

### Retained F0111 screen

The arbitrary-heterogeneity `N=12,13` first-bifurcation screen is now reduced to (8.5). The highest-value next move is **not another generic entropy lemma**. It is to exploit the exact narrow scalar cells and prove a sign for

\[
\Gamma_N(\delta,s)
:=\log S-\overline E_K-K_{\max}-H_J^*.
\]

Because `m_K` changes only at explicit algebraic boundaries, this becomes finitely many scalar cells. A useful route is either:

- prove monotonicity of `Gamma_N` toward the scalar-collision boundary and certify the boundary sign; or
- subdivide those algebraic cells and use exact rational Taylor/Bernstein envelopes for the logarithms and the adaptive exponent.

Do not call either `N=12` or `N=13` eliminated until the entire corresponding scalar band is covered exactly.

## 11. Scheduler/model-control status

The exposed task-control surface available to this run still provides prompt/title, schedule or relative-start timing, enabled state, and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated per-run model/effort attestation, and no guaranteed hour-long execution field**. Hence `GPT-6 / maximum` remains prompt text only on this surface; this run actually identifies as GPT-5.6 Sol and its applied reasoning level is UNVERIFIED.

The implementation manifest still records the historical P26 task response

`You cannot modify this task.`

That is an authorization-context boundary. A genuine fix requires a scheduler/workspace/API or admin surface with persistent model and reasoning fields, propagation of those fields into inference routing, and trustworthy per-run attestation. The compliant workaround for an edit-denied P26 task is the owning/authorized context or platform support, not task duplication or permission bypass.

No scheduler mutation was attempted in this run, consistent with the worker contract.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  native_source:
    id: I0076
    source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2"
    metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
    before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    unchanged_count: 6_FROZEN_AT_HANDOFF
    remaining_obligation: "new source-valid frozen candidate satisfying all four obligations, or full implication proof under arbitrary-random-time independence"
  retained_screen:
    source: "Talagrand discrete Convexity Conjecture / F0111, k=2 hazard screen; PENDING / NOT CLAIMED"
    before: "N=12,13 arbitrary heterogeneity reduced to one J split variable plus explicit K extremizer"
    after: "all J and K contact-distribution variables eliminated; necessary gate depends only on (delta,s), piecewise in m_K"
    status: PARTIAL_SELF_CHECK_ONLY
    new_claims:
      - R15-F0111-ADAPTIVE-EXTREMAL
      - "two-variable scalar necessary gate Gamma_N(delta,s) for N=12,13"
    remaining_obligation: "certify Gamma_N(delta,s)>0 on every complete scalar-feasible cell, or exhibit a genuine scalar survivor; broader non-two-level and second-contact mechanisms remain outside this screen"
  tried_moves: [5, 13, 30]
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260920_0754Z_successor_screen_f0111_twoheavy_extremal_q102y.md"
    - "artifacts/R15/f0111_adaptive_ray_monotonicity_idea_r103z.md @ a9cbb784b030304d436b78658ea7e7ccb1640631"
    - "artifacts/R15/f0111_adaptive_ray_monotonicity_checker_r103z.py @ 22503b9abd29530d2dc86dcd29f720aad78665fa"
    - "artifacts/R15/f0111_adaptive_ray_monotonicity_checker_r103z.out @ b359949f72620936804ca33e767441dd69bf96d5"
  audits:
    new_independent_other_track_audits: []
    note: "new retained-screen theorem has only self-check arithmetic; no closure claim"
```
