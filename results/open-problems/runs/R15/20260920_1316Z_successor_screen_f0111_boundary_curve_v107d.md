Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: the entire lower scalar closure `U_K=N` is now excluded for both remaining F0111 dimension-30 branches `N=12,13`, using a new entropy inequality and an exact rational interval certificate. Methods #7 TAKE THE LIMIT, #12 FIND WHAT IS CONSERVED, #29 ADD THE POINTS AT INFINITY.**

# R15 retained screen — exact exclusion of the full lower scalar boundary for N=12,13

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, and does not claim Talagrand's full discrete Convexity Conjecture is solved.

All thirty Section-B move numbers already occur in older R15 history. The preceding completed report used `#3/#25/#27`; this run uses the nonconsecutive triple `#7/#12/#29` on the reduced two-cell scalar object.

## 1. Continuity, source fidelity, ownership and whole-repository readback

Before new mathematics I reread/recovered the current `master` state required by the owner policy:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the controlling native handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the I0124 six-run handoff history and later R15 successor-admission history, confirming I0124 is also retired despite its older canonical claim file;
- the newest completed own report `runs/R15/20260920_0953Z_successor_screen_f0111_kenergy_excess_t105b.md` and the already-committed boundary-minimum route note;
- the newest neighboring same-source Burdzy report `runs/R07/20260919T093413Z_i0077_random_reroot_periodic_completion_59_handoff_rr59s3.md`;
- exact repository searches for `I0076`, `Problem 7.2`, `I0124`, F0111, and current claim/queue state.

The current queue still does not supply a newly certified free READY+CLOSABLE successor for R15. The old I0124 canonical claim is historical: its own six-run handoff records `H_288=112` and retires further attack, and later R15 admission reports explicitly preserve it as `PARTIAL / RETIRED-HANDOFF`. I therefore did not reopen I0124, steal another track, or promote a PENDING queue row.

### Exact Burdzy--Scheutzow source, checked again 2026-09-20

Primary source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- FBM: there exist random origins `S_n -> -infinity` a.s. whose complete centered futures are standard Brownian motions;
- BBM: the time-reversed process is FBM;
- 2BM: there exists one random time `S` at which the complete centered future and complete centered past are **independent standard Brownian motions**.

Problem 7.2 assumes only FBM + BBM and existence of **an arbitrary random time** `T` for which the two complete centered half-processes are independent. It does not say `T` is a stopping time and does not separately assume either seam half is Brownian. Proposition 6.2 excludes, for the Section-6 construction, a stronger seam that also has a Brownian forward half; it does not settle the bare Problem-7.2 independence hypothesis.

The native I0076 state is therefore unchanged. The source-Theorem-6.1 construction has FBM, BBM and non-2BM but no source-valid independent seam. The later Brownian-prefix/BES construction had the exact independent seam but the R15 Palm analysis proved it is actually 2BM. Thus there is **no surviving frozen counterexample candidate** on which the four requested obligations can honestly be rescored. The old `2/4` / `3/4` quantities belong to retired candidates and are not a current score. Native research remains at the mandatory six-run handoff.

Fresh public searches dated 2026-09-20 used the exact title/arXiv number/`Problem 7.2` language. They recovered the source and later references but no accessible later primary paper explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only, not a universal openness certificate.

## 2. Retained F0111 continuity

The retained screen concerns the cardinality-two hazard

\[
F(q)=\sum_i q_i-\log S(q),\qquad
S(q)=\sum_i e^{q_i}-29,
\]

and a hypothetical nonnegative-coefficient quadratic global majorant exact at an interior point in dimension `n=30`. The carried first-bifurcation analysis assumes the contact Hessian has a full-support two-level mixed-sign null direction and writes

\[
z=1+s>1,\qquad N=|K|.
\]

Earlier exact R15 reports eliminate `N=11` and `N=14`; arbitrary-heterogeneity survivors are confined to `N in {12,13}`. Their scalar region satisfies

\[
L_K(d,s)\le N<U_K(d,s),
\]

where

\[
U_K(d,s)=
\frac{29(d+1)(d+s+1)(d+2s+1)}{4(s+1)(s+2)}.
\tag{2.1}
\]

The rational outer scale roofs are

\[
0<s<\frac{3601}{250000}\quad(N=12),
\qquad
0<s<\frac{12637}{10^6}\quad(N=13).
\tag{2.2}
\]

The predecessor proves the distribution-free K-excess identity

\[
\eta:=U_K-N=\sum_{j\in K}(e^{q_j}-1),
\]

the secant moment roof

\[
E_{1,K}\le K_{\rm sec}
:=\frac{\eta}{S}
\frac{c_K\log c_K}{c_K-1},
\qquad c_K=\frac{U_K}{L_K},
\]

and the sharper pair-energy bound

\[
0\le E_{KK}\le\frac\eta2K_{\rm sec}.
\]

Consequently every survivor satisfies the sharpened necessary gate

\[
\boxed{
\widehat\Gamma_N(d,s)
:=\log S-\left(1+\frac\eta2\right)K_{\rm sec}-H_J^*(d,s)\le0.
}
\tag{2.3}
\]

The new run attacks the lower scalar closure `U_K=N` of the two remaining cells.

## 3. Methods #7 and #29 — add the missing boundary and simplify it exactly

On the algebraic closure

\[
U_K=N,
\tag{3.1}
\]

one has `eta=0`. Since every `v_j=e^{q_j}` obeys `v_j>=1` and their sum is exactly `N`, all K coordinates collapse:

\[
v_j=1,\qquad q_j=0,
\qquad K_{\rm sec}=E_{1,K}=E_{KK}=0.
\tag{3.2}
\]

The exact mass equations also give

\[
Sy=N,\qquad Sx=S+29-N.
\tag{3.3}
\]

The arbitrary-heterogeneity heavy-coordinate caps from the earlier full-cell proof are

\[
r_*<1-C_Ns,\qquad C_{12}=15,\quad C_{13}=17.
\tag{3.4}
\]

The adaptive-ray extremizer therefore becomes exactly two-heavy on the closure. Put

\[
p=C_Ns.
\]

Then

\[
u_1=S(1-p),
\qquad
u_2=1+pS.
\tag{3.5}
\]

The previous adaptive monotonicity proof was written for `c=7/100` in

\[
\varepsilon=\frac c{\log S},\qquad t=1+\varepsilon.
\]

Its only c-dependent comparison is monotone in `e^c`, and it was certified at `c=7/100`; hence the same proof applies to every `0<c<=7/100`. For the present boundary theorem choose the more robust

\[
\boxed{c=\frac3{100}.}
\tag{3.6}
\]

Define

\[
A=1-p,\qquad D=S^{-1},\qquad B=p+D.
\tag{3.7}
\]

Then `A+B-D=1`, `u_1=SA`, `u_2=SB`, and (2.3) reduces on the boundary to

\[
\widehat\Gamma_N^\partial
=-\frac1t\log F
-\varepsilon U_{\max}\log(SA)\log(SB),
\tag{3.8}
\]

where

\[
F=A^t+B^t-D^t.
\tag{3.9}
\]

## 4. Method #12 — a conserved entropy inequality removes the transcendental power

The key identity is

\[
D^t=D e^{-c},
\tag{4.1}
\]

because `epsilon log D=-c` exactly. For `0<x<=1`,

\[
e^u\le1+u+\frac{u^2}{2}\qquad(u\le0),
\]

so

\[
x^{1+\varepsilon}
\le x\left(1+\varepsilon\log x
+\frac{\varepsilon^2\log^2x}{2}\right).
\tag{4.2}
\]

Introduce

\[
\mathcal E
=-A\log A-B\log B+D\log D,
\]

\[
\mathcal V
=A\log^2A+B\log^2B.
\tag{4.3}
\]

Using `A+B-D=1`, (4.1)--(4.2) give

\[
1-F\ge
\varepsilon\mathcal E-rac{\varepsilon^2}{2}\mathcal V
+D(c-1+e^{-c}).
\tag{4.4}
\]

The last term is nonnegative because `e^{-c}>=1-c`. Therefore if

\[
\boxed{
\mathcal J_N
:=\mathcal E
-tU_{\max}\log(SA)\log(SB)
-\frac\varepsilon2\mathcal V>0,
}
\tag{4.5}
\]

then `F<1`, and `-log F>=1-F` yields the strict boundary contradiction

\[
\boxed{\widehat\Gamma_N^\partial>0.}
\tag{4.6}
\]

This is the conceptual advance of the run: the boundary gate no longer needs direct control of fractional powers. It becomes an entropy-versus-energy inequality involving only logarithms and rational scalar functions.

## 5. Analytic proof for 0<s<=10^{-4}

On both retained cells the earlier exact checker proves

\[
\frac{29}{20}<\kappa:=\frac{-k}{s}<\frac{13}{8},
\qquad
U_{\max}<\frac98s.
\tag{5.1}
\]

Since `S=29/(kappa s)`, for `s<=10^{-4}`

\[
S>\frac{232}{13s}\ge\frac{2320000}{13}>e^{12},
\qquad L:=\log S>12.
\tag{5.2}
\]

The exact checker establishes `e^3<201/10` and `(201/10)^4<2320000/13`. Also

\[
pS=\frac{29C_N}{\kappa}<20C_N,
\]

so

\[
q_2:=\log(1+pS)<\log341<6,
\tag{5.3}
\]

where the exact Taylor partial sum gives `e^6>1709/5>341`.

Write

\[
\beta_N=C_N+\frac{13}{232}.
\]

Then `B<beta_N s`, `q_1=log(SA)<L`, and the entropy has the stable exact form

\[
\mathcal E
=-(1-p)\log(1-p)+pL-Bq_2.
\tag{5.4}
\]

Hence

\[
\mathcal E>C_NsL-6\beta_Ns.
\tag{5.5}
\]

For the variance term, `|log B|<L` and

\[
-\log(1-p)\le\frac{p}{1-p},
\]

so

\[
\mathcal V
\le BL^2+\frac{p^2}{1-p}.
\tag{5.6}
\]

Because `c=3/100` and `L>12`,

\[
t<\frac{401}{400}.
\]

Substitution into (4.5) yields

\[
\mathcal J_N
>s\left[
L\left(
C_N-\frac{401}{400}\frac{27}{4}
-\frac3{200}\beta_N
\right)
-6\beta_N-\rho_N
\right],
\tag{5.7}
\]

where the residual A-variance contribution is bounded by

\[
\rho_N
=\frac{(3/100)C_N^2}
{24\cdot10^4(1-C_N/10^4)}.
\]

At `L=12` the exact rational margins are

\[
\boxed{
N=12:\quad
\frac{266454411}{46330400}>0,
}
\tag{5.8}
\]

\[
\boxed{
N=13:\quad
\frac{4027892527}{231605600}>0.
}
\tag{5.9}
\]

Thus `J_N>0` for the complete small-scale range `0<s<=10^{-4}`.

## 6. Exact rational interval certificate for the remaining boundary curve

It remains to cover

\[
10^{-4}\le s\le\frac{3601}{250000}\quad(N=12),
\]

\[
10^{-4}\le s\le\frac{12637}{10^6}\quad(N=13).
\tag{6.1}
\]

The checker uses only exact `Fraction` arithmetic. The formula (2.1) is strictly increasing in `d` and in `s`; explicitly

\[
\partial_sU_K
=-\frac{29(d-1)(d+1)
(2ds+3d+3s^2+6s+3)}
{4(s+1)^2(s+2)^2}>0
\]

for `0<d<1`. Therefore the unique root `d_N(s)` of `U_K(d,s)=N` decreases in `s`.

For each rational `s`-slab the checker brackets `d_N(s)` by 42 steps of exact dyadic bisection at the slab endpoints. It then evaluates an interval extension of `J_N` over the resulting enclosing rectangle. Every logarithm is enclosed rigorously by

\[
\log y
=2\sum_{j\ge0}
\frac{w^{2j+1}}{2j+1},
\qquad
w=\frac{y-1}{y+1},
\]

after exact dyadic normalization to `1<=y<2`; the omitted positive tail is bounded by a rational geometric series. No floating-point sign decision is used.

Starting from 16 slabs and bisecting only uncertified slabs, the executed exact checker closes both curves:

- `N=12`: 203 terminal rational slabs, maximum additional depth 6; the smallest exact lower endpoint is positive (displayed float `1.4471338958495323e-05`, with a 27392-bit numerator and 27408-bit denominator);
- `N=13`: 93 terminal rational slabs, maximum additional depth 6; the smallest exact lower endpoint is positive (displayed float `0.0008211663580218144`, with a 26384-bit numerator and 26394-bit denominator).

The float renderings are only summaries of exact rational lower bounds; the sign tests themselves are exact. The archived output ends

`BOUNDARY_UK_EQ_N_N12_N13_EXCLUDED`  
`ALL_EXACT_CHECKS_PASS`.

## 7. New restricted theorem

Combining Sections 3--6 gives:

**Theorem R15-F0111-LOWER-BOUNDARY.**  
For either remaining dimension-30 full-support two-level Hessian-null scalar branch `N=12` or `N=13`, let `d_N(s)` be the algebraic lower boundary determined by `U_K(d_N(s),s)=N`. Throughout the complete scalar range containing every feasible branch point, the continuous extension of the sharpened arbitrary-heterogeneity necessary gate satisfies

\[
\boxed{
\widehat\Gamma_N(d_N(s),s)>0
\qquad(s>0).
}
\tag{7.1}
\]

Hence the entire lower scalar boundary is incompatible with the contact inequality `widehat Gamma_N<=0`. No surviving full-support contact can approach any fixed positive-s point of that boundary.

This theorem permits arbitrary heterogeneity within both sign blocks. It is stronger than the earlier `s->0` boundary repulsion: it covers the **entire** algebraic `U_K=N` boundary of both final scalar cells, including the tight collision end where `U_K=L_K=N`.

It still does **not** eliminate the interiors of `N=12,13`. The missing step is now one-dimensional in spirit: prove that `widehat Gamma_N` cannot decrease from its positive lower-boundary value fast enough when `d` moves into the feasible strip, ideally by proving

\[
\partial_d\widehat\Gamma_N\ge0
\]

on each cell or by an exact one-sided boundary-to-interior comparison. Numerical scratch suggests this monotonicity, but no numerical sample is counted as evidence.

## 8. Fresh literature scope

Fresh searches dated 2026-09-20 recover Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), which reformulates Talagrand's **discrete** Convexity Conjecture via `k`-thresholds and proves broad classes, and Jinyoung Park, arXiv:2609.14681 (2026-09-13), which gives a dimension-free expectation/fractional-expectation comparison described as a bound *toward* the conjecture. These do not authorize calling the present restricted theorem a full solution. I found no accessible primary source matching Theorem R15-F0111-LOWER-BOUNDARY in this bounded search. **Novelty remains UNVERIFIED.**

## 9. Validation / delivery

The research route was written before code in the already committed boundary-minimum note and the explicit pivot note

`artifacts/R15/f0111_boundary_entropy_pivot_v107d.md`

at commit

`d4c6f7a77f1bfc6db4f3822ade5f65d7c5d360ac`.

Only afterward I created and executed

`artifacts/R15/f0111_boundary_curve_checker_v107d.py`

(commit `8e998587f354ae999af8332e32fa2658cc35820c`) and archived its actual output in

`artifacts/R15/f0111_boundary_curve_checker_v107d.out`

(commit `7cda54e02dd80ae12816b01b0d15372bae25c015`). All three files were read back at the exact returned commit SHAs. This is a **self-check**, not an independent audit.

No shared roots, other tracks' files, public repositories, email, Drive, purchases, permission settings or scheduler settings were changed.

## 10. Model / scheduler control

The limitation is still real. The currently exposed scheduling surface offers title/prompt, schedule or relative start timing, timing mode, enabled state and ordinary update controls. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution control**. GPT-6 / maximum therefore remains prompt-only; this run actually reports GPT-5.6 Sol with reasoning level UNVERIFIED.

The repository's implementation record still contains the historical P26 response `You cannot modify this task.` That is an authorization-context boundary, not a research failure. The compliant workaround is to modify the same task from the owning/authorized workspace/account/API/admin context or use platform support. A genuine GPT-6/maximum fix requires a scheduler/backend surface that accepts and persists binding model/effort fields and returns authenticated per-run routing telemetry. Task duplication or permission bypass is not a valid workaround.

## ledger_delta

```yaml
source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2; intake I0076"
metric_name: "number of four source-matching obligations proved for one frozen counterexample candidate"
metric_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
metric_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
status: "OPEN / PARTIAL / RETIRED-HANDOFF"
unchanged_count: "UNKNOWN (native source already beyond mandatory six-run handoff; do not reset)"
tried_moves: [7, 12, 29]
remaining_obligation: "No surviving frozen I0076 candidate and no newly certified free READY+CLOSABLE successor. Retained F0111 screen now has positive sharpened gate on the complete U_K=N lower boundary for N=12,13; interiors still require one-sided d-monotonicity/boundary-to-interior control."
retained_screen: "Talagrand F0111 k=2; PENDING / SELF_CHECK_ONLY / NOT CLAIMED"
retained_aux_before: "N=12,13 interiors remain; sharpened gate widehat Gamma_N<=0 known, but whole U_K=N boundary not certified"
retained_aux_after: "exact theorem widehat Gamma_N(d_N(s),s)>0 on the entire lower scalar boundary U_K=N for both N=12 and N=13"
evidence:
  - "artifacts/R15/f0111_boundary_minimum_idea_u106c.md @ db8d145ac9cc38a9c4fbc51693d4ed2a799be6bc"
  - "artifacts/R15/f0111_boundary_entropy_pivot_v107d.md @ d4c6f7a77f1bfc6db4f3822ade5f65d7c5d360ac"
  - "artifacts/R15/f0111_boundary_curve_checker_v107d.py @ 8e998587f354ae999af8332e32fa2658cc35820c"
  - "artifacts/R15/f0111_boundary_curve_checker_v107d.out @ 7cda54e02dd80ae12816b01b0d15372bae25c015"
audit_ids: []
```
