Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: for the remaining dimension-30 F0111 `k=2` cells `N=|K|=12,13`, I prove exact distribution-free K-excess roofs, arbitrary-heterogeneity heavy-coordinate caps `r_*<1-15s` and `r_*<1-17s`, and eliminate the entire block-constant subfamily in both cells. Methods #6 DEFORM TO A POINT YOU CAN SOLVE, #14 FIND THE GROUP ACTING, #20 FIND WHY THE ALGORITHM FAILS.**

# R15 retained screen — K-excess compression and block-constant elimination for the last two n=30 cells

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about Talagrand/F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, does not solve Talagrand's discrete Convexity Conjecture, and does not satisfy the two-other-track audit closure rule.

The immediately preceding complete report used methods `#5/#13/#18`. All thirty Section-B moves have already appeared somewhere in the older R15 history, so the literal globally-never-used condition is exhausted. The present `#6/#14/#20` triple is nonconsecutive and is applied to a new reduced object. The route was written before any checker in `artifacts/R15/f0111_n1213_heavycap_kexcess_idea_o100w.md` at commit `2855d5a2ac41205d5620ec85452f04255d2a8f8a`.

## 1. Whole-repository continuity, ownership, source and exclusions

Before new mathematics I reread the current campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the latest operations implementation record, the newest R15 report, and the neighboring Burdzy track. The current reserve still states **zero newly certified free READY entries**. I did not claim a PENDING queue item, steal another worker's source, reopen Problem 7.5, or edit any shared root.

### Exact Burdzy--Scheutzow source rechecked

I rechecked the primary UW-hosted PDF of Burdzy--Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), especially Definition 2.1, Proposition 6.2, and Problem 7.2.

- FBM means there are random origins `S_n -> -infinity` a.s. whose complete centered futures are standard Brownian motions.
- BBM means the time-reversed process is an FBM.
- 2BM means there is one random time `S` for which the complete centered future and complete centered past are independent standard Brownian motions.
- Problem 7.2 assumes FBM + BBM + existence of an arbitrary random time `T` at which the two complete centered half-processes are independent. It does **not** require `T` to be a stopping time and does **not** separately assume either half at `T` is Brownian.
- Proposition 6.2 rules out, for its construction, an independent seam together with a Brownian forward half. That is a different, stronger seam condition and does not itself answer Problem 7.2.

The controlling I0076 handoff therefore remains unchanged. The source Theorem-6.1 construction gives FBM, BBM and non-2BM but no source-valid independent seam; the later Brownian-prefix/BES construction gives the source-valid independent seam but was proved to be 2BM. There is no surviving frozen counterexample candidate on which the requested four obligations can honestly be counted. Historical `2/4` or `3/4` diagnostics are not a current frozen-candidate score.

Dated 2026-09-20 searches for the exact title/problem number, later Burdzy/Scheutzow material, and citing work recovered the source and related Brownian-pasting literature but no accessible later primary paper explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only, not a global openness certificate.

## 2. Carried F0111 state

The retained screen concerns the `k=2` quadratic-majorant hazard

\[
F(t)=\sum_i t_i-\log\!\left(\sum_i e^{t_i}-29\right)
\]

in dimension `n=30`. The preceding exact reductions eliminate the `N=11` and `N=14` full-support two-level Hessian-null branches. Any survivor of this particular first-bifurcation mechanism on `z=1+s>1` must therefore have

\[
N=|K|\in\{12,13\}.
\]

Put

\[
a=1+\delta,\qquad b=1-\delta,\qquad z=1+s,
\]

and carry the exact cubic-null quantities

\[
k=\frac{2z(1-z^2)}{(1-\delta^2)(\delta+3z)},
\qquad
 y=\frac{(\delta+z)(1-z)(1-\delta-2z)}{2(1-\delta)(\delta+3z)},
\qquad x=1-k-y,
\]

\[
K_2=\frac{(\delta+z)(1-z^2)}{\delta+3z},
\quad t_J=(1-z)^2-K_2,
\quad t_K=(1+z)^2-K_2,
\]

\[
R=-\frac{2(\delta+z)(1-z^2)(\delta^2z+3\delta z^2+\delta+3z^3)}{(\delta+3z)^2},
\]

\[
A_J=1+\frac{3t_J^2}{R},\qquad A_K=1+\frac{3t_K^2}{R},\qquad
A_{JK}=1+\frac{3t_Jt_K}{R}.
\]

Define

\[
L_K=yA_K,\qquad Q_K=-kA_K,\qquad U_K=-\frac{29y}{k}.
\]

Scalar feasibility for a fixed integer `N=|K|` requires

\[
L_K\le N<U_K.
\tag{2.1}
\]

The carried scalar-envelope report gives

\[
N=12:\quad \frac{12}{25}<\delta<\frac12,\qquad 0<s<0.014404,
\]

\[
N=13:\quad \frac{13}{25}<\delta<\frac7{13},\qquad 0<s<0.012637.
\tag{2.2}
\]

At an exact contact `q`, write

\[
r_i=\frac{e^{q_i}}{S(q)},\qquad S(q)=\sum_i e^{q_i}-29,
\]

so that `sum r_i=1-k`. The projective fourth-order condition gives the residual Gram matrix

\[
K=H-\frac3R\beta\beta^T\succeq0,
\]

with `beta_i=r_i t_J` on `J` and `beta_j=r_j t_K` on `K`. Thus there are Gram vectors `w_i` with

\[
\|w_i\|^2=r_i(1-A_Jr_i)\quad(i\in J),
\qquad
\|w_j\|^2=r_j(1-A_Kr_j)\quad(j\in K).
\tag{2.3}
\]

If `U,V,W` are the aggregate pair-coefficient masses on `JxJ`, `KxK`, and `JxK`, and

\[
T=\Bigl\|\sum_{j\in K}w_j\Bigr\|^2,
\]

then

\[
2U=\frac{b^2}{a^2}T-x+A_Jx^2,
\quad
2V=T-y+A_Ky^2,
\quad
W=\frac baT+A_{JK}xy,
\tag{2.4}
\]

and Cauchy gives

\[
T\le T_{\rm cap}:=y(N-L_K).
\tag{2.5}
\]

No within-block symmetry is assumed in (2.3)--(2.5).

## 3. Method #6 — exact K-excess invariant and sharp distribution-free roofs

The identity

\[
S(q)y=\sum_{j\in K}e^{q_j}=U_K
\tag{3.1}
\]

is immediate from `S(q)=-29/k`. Hence

\[
\boxed{\sum_{j\in K}(e^{q_j}-1)=U_K-N}
\tag{3.2}
\]

and, since `q_j>0` and `e^{q_j}-1\ge q_j`,

\[
\boxed{\sum_{j\in K}q_j\le U_K-N.}
\tag{3.3}
\]

This compresses every possible heterogeneous `K` block into one scalar slack.

The new point is that this slack has an exact global roof. Differentiate `U_K` along a level curve `L_K=N`. Set

\[
\mathcal H=(\partial_sU_K)(\partial_\delta L_K)-(\partial_\delta U_K)(\partial_sL_K).
\]

Exact factorization gives

\[
\mathcal H=
\frac{87(\delta+2s+1)(\delta+2s+3)P(\delta,s)}
{8(\delta-1)(s+1)(s+2)Q(\delta,s)^2},
\tag{3.4}
\]

where every coefficient of `P` is strictly positive and `Q>0` on `0<delta<1,s>0`. Hence `H<0`. Also `partial_delta L_K>0` and `partial_delta U_K>0`; their numerators have only positive coefficients after the obvious positive denominators are removed. Therefore along the unique level root `delta_N(s)` satisfying `L_K=N`,

\[
\frac d{ds}U_K(\delta_N(s),s)=\frac{\mathcal H}{\partial_\delta L_K}<0.
\]

At `s=0`,

\[
L_K(\delta,0)=\frac6{1-\delta},\qquad
U_K(\delta,0)=\frac{29(1+\delta)^3}{8}.
\]

Thus `delta_N(0)=1-6/N`, and scalar feasibility (2.1), together with monotonicity in `delta`, yields

\[
\boxed{U_K\le29\left(1-\frac3N\right)^3.}
\tag{3.5}
\]

For the two remaining cells this is exactly

\[
\boxed{U_K-12\le\frac{15}{64}},
\qquad
\boxed{U_K-13\le\frac{439}{2197}}.
\tag{3.6}
\]

Combining (3.3) and (3.6) gives the new distribution-free logarithmic roofs

\[
N=12:\quad \sum_{j\in K}q_j\le\frac{15}{64},
\qquad
N=13:\quad \sum_{j\in K}q_j\le\frac{439}{2197}.
\tag{3.7}
\]

## 4. Method #20 — arbitrary-heterogeneity heavy-coordinate caps

I next ported the residual-Gram obstruction from the eliminated `N=11` cell, but with constants adapted to the two remaining cells.

Exact Bernstein certificates prove that every scalar survivor lies in the following rational slanted bands:

\[
N=12:\quad 0<s<\frac{3601}{250000},\qquad
\frac{49}{100}-\frac s4<\delta<\frac12-\frac{9s}{10},
\tag{4.1}
\]

\[
N=13:\quad 0<s<\frac{12637}{10^6},\qquad
\frac{53}{100}-\frac s5<\delta<\frac7{13}-\frac{4s}{5}.
\tag{4.2}
\]

Indeed the lower walls satisfy `U_K<N`, the upper walls satisfy `L_K>N`, and both scalar functions increase with `delta`.

Let

\[
r_*=\max_{i\in J}r_i.
\]

For a candidate threshold `r_0=1-Cs`, put

\[
\ell=x-r_0,
\qquad e=r_0(1-A_Jr_0),
\]

\[
\Delta=\frac{s(x-2\ell)}b-\frac baT_{\rm cap}-A_{JK}\ell y.
\tag{4.3}
\]

Suppose `r_*>=r_0`, let `*` attain the maximum, let `L=J\setminus{*}`, and write `ell_0=sum_{i in L}r_i<=ell`. The coordinate null equations imply

\[
B_{L,K}\ge\frac{s(x-2\ell_0)}b.
\tag{4.4}
\]

The residual Gram representation gives

\[
B_{L,K}=\langle W_L,W_K\rangle+A_{JK}\ell_0y,
\]

while `Kh=0` yields

\[
w_*+W_L=\frac baW_K.
\]

Since `A_{JK}>0`, `T<=T_cap`, and `ell_0<=ell`, (4.4) implies

\[
\langle w_*,W_K\rangle\le-\Delta.
\tag{4.5}
\]

If, in addition,

\[
e>0,\qquad 2A_Jr_0>1,
\tag{4.6}
\]

then residual positivity `r_*<=1/A_J` makes `u(1-A_Ju)` decreasing on `[r_0,1/A_J]`, and therefore

\[
\|w_*\|^2\le e.
\]

Cauchy would force

\[
\Delta^2\le eT_{\rm cap}.
\tag{4.7}
\]

The exact checker proves the strict reverse inequality in the entire corresponding rational band:

- for `N=12`, with `C=15`, it certifies `e>0`, `2A_Jr_0>1`, `Delta>0`, and `Delta^2>eT_cap`;
- for `N=13`, with `C=17`, the same four inequalities hold (the final polynomial uses an exact 2x2 Bernstein subdivision).

Hence every heterogeneous survivor obeys

\[
\boxed{N=12:\quad r_*<1-15s,}
\qquad
\boxed{N=13:\quad r_*<1-17s.}
\tag{4.8}
\]

These are genuine arbitrary-within-block restrictions. I also tried simply pushing the constants farther on the same outer bands; that direct route loses sign, so another idea is required for complete heterogeneous elimination.

## 5. Method #14 — eliminate both block-constant cells completely

Now suppose the contact itself is block-constant:

\[
q_i=u\quad(i\in J),\qquad q_j=v\quad(j\in K),
\]

with `M=30-N`. Average any certificate over `S_M x S_N`. Symmetry of `F` preserves global majorization, coefficient nonnegativity, exact contact, PSD, and the block null vector, so the averaged certificate has only three pair coefficients `beta_J,beta_K,eta`.

Let

\[
U=\binom M2\beta_J,
\qquad V=\binom N2\beta_K,
\qquad W=MN\eta.
\]

The summed null equations are exactly

\[
2aU-bW=xs,
\qquad aW-2bV=y(s+2).
\tag{5.1}
\]

The Hessian eigenvalue on the `K`-orthogonal subspace is `r_K-beta_K`, so PSD implies

\[
\beta_K\le r_K=\frac yN,
\qquad V\le\frac{N-1}{2}y.
\tag{5.2}
\]

Across both cells, exact rational bounds give

\[
\frac{29}{20}<\kappa:=-\frac ks<\frac{13}{8},
\qquad 1<x<\frac{41}{40},
\qquad 0<y<\frac34s,
\tag{5.3}
\]

with `12/25<delta<7/13` and `s<3/200`. Equations (5.1)--(5.3) imply

\[
\boxed{U<\frac98s,
\qquad V<\frac92s,
\qquad W<\frac{17}{4}s.}
\tag{5.4}
\]

The K-excess roofs are especially strong in the block-constant case, because `Ne^v=U_K`. Thus

\[
v=\log(U_K/N)<\frac{U_K-N}{N}<\frac1{50}.
\tag{5.5}
\]

Also `S(q)s=29/kappa<20`, `M>=17`, and `x<41/40`, so

\[
u=\log\frac{S(q)x}{M}<\log\frac5{4s}.
\tag{5.6}
\]

For `0<s<3/200`, the functions `s log(5/(4s))` and `s log^2(5/(4s))` are increasing, and the exact rational Taylor bound `log(250/3)<9/2` gives

\[
su<\frac{27}{400},
\qquad su^2<\frac{243}{800}.
\tag{5.7}
\]

The quadratic coefficient side of exact value contact therefore satisfies

\[
E_{\rm cert}=Uu^2+Vv^2+Wuv
<\frac{1389933}{4000000}<0.348.
\tag{5.8}
\]

But exact value contact also has the entropy form

\[
E=k\log S(q)-\sum_i r_i\log r_i
=k\log S(q)+x\log\frac Mx+y\log\frac Ny.
\tag{5.9}
\]

The last term is positive. Since `1<x<41/40`, `M>=17`, the function `x log(M/x)` is increasing over this interval, hence it is at least `log17`. The exact rational Taylor bound `log17>14/5` applies. Moreover

\[
-k\log S(q)=\kappa s\log S(q)
<\frac{13}{8}\frac3{200}\log\frac{4000}{3}
<\frac{351}{2000},
\]

using the exact bound `log(4000/3)<36/5`. Hence

\[
E>\frac{14}{5}-\frac{351}{2000}
=\frac{5249}{2000}.
\tag{5.10}
\]

The two exact bounds (5.8) and (5.10) are incompatible; the certified rational gap is

\[
\boxed{
\frac{5249}{2000}-\frac{1389933}{4000000}
=\frac{9108067}{4000000}>0.
}
\tag{5.11}
\]

Therefore

\[
\boxed{
\text{No block-constant full-support two-level Hessian-null exact quadratic contact exists}
\atop
\text{in either remaining dimension-30 cell }N=12\text{ or }N=13.
}
\tag{5.12}
\]

This removes the entire `S_M x S_N` symmetric subfamily, not merely a boundary neighborhood.

## 6. What method #20 says is still missing

I tried to port the complete `N=11` entropy-energy elimination to arbitrary within-block heterogeneity using the new caps (4.8) and K-excess roofs (3.7). The K-side terms become tiny, but the conservative heterogeneous `J-J` energy bound remains too large near the top of both cells: the corresponding worst-case gap changes sign (approximately `-0.155` for `N=12` and `-0.085` for `N=13` under this direct envelope). The obstruction is now precise: light `J` masses can route `J-J` coefficient energy through unequal logarithmic coordinates, and the present heavy caps `15,17` do not by themselves control that routing sharply enough.

So I do **not** claim the full `N=12` or `N=13` branches are eliminated. Any surviving contact must instead satisfy all of the following simultaneously:

\[
N\in\{12,13\},
\]

\[
\sum_{j\in K}q_j\le
\begin{cases}
15/64,&N=12,\\
439/2197,&N=13,
\end{cases}
\]

\[
r_*<
\begin{cases}
1-15s,&N=12,\\
1-17s,&N=13,
\end{cases}
\]

and it must genuinely break block symmetry. The next useful route is therefore not another scalar checker: it is a heterogeneity penalty, probably a Schur-convex/majorization bound coupling `J-J` coefficient flow to the entropy of the light `J` masses.

## 7. Validation and literature

Only after the route was written did I create and run `artifacts/R15/f0111_n1213_kexcess_block_checker_o100w.py`. The archived output verifies the K-excess derivative and exact roofs, both rational cell walls, all eight heavy-cap inequalities, the uniform scalar and aggregate coefficient bounds, the rational exponential/logarithm enclosures, and the block-constant value-gap. It ends `BLOCK_CONSTANT_N12_N13_IMPOSSIBLE` and `ALL_EXACT_CHECKS_PASS`. This is a **self-check**, not an independent audit.

Fresh 2026-09-20 literature checks do not support calling the retained F0111 work a solution of Talagrand's full discrete Convexity Conjecture. Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), reformulate the conjecture through `k`-thresholds and prove broad classes. Jinyoung Park, arXiv:2609.14681 (2026-09-13), explicitly states a dimension-independent bound *toward* the conjecture. The Princeton 2026-10-08 seminar description likewise advertises open problems after the reformulation. Novelty of the restricted statements proved here remains **UNVERIFIED**.

## 8. Model/scheduler control

The currently documented scheduler surface still exposes prompt/title, schedule/timing, enabled state and ordinary update controls, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution control. GPT-6/maximum is therefore a prompt request only in this run. The historical P26 `You cannot modify this task` event was authorization-context-specific; the repository records a later successful update from an authorized P/C context. The compliant workaround is the owning/authorized workspace/account/API/admin context or platform support, not task duplication or permission bypass. I made no scheduler change in this run.

## ledger_delta

```yaml
source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2; intake I0076"
metric_name: "number of four source-matching obligations proved for one frozen counterexample candidate"
metric_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
metric_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
status: "OPEN / PARTIAL / RETIRED-HANDOFF"
unchanged_count: "UNKNOWN (native source already beyond mandatory six-run handoff; do not reset)"
tried_moves: [6, 14, 20]
remaining_obligation: "No surviving frozen I0076 counterexample candidate; no newly certified free READY+CLOSABLE successor. Retained F0111 screen still has arbitrary-heterogeneity N=12,13 branches, non-two-level/null-zero directions, and second-contact mechanism."
retained_screen: "Talagrand F0111 k=2; PENDING / SELF_CHECK_ONLY / NOT CLAIMED"
retained_aux_before: "dimension-30 full-support two-level branch reduced to N in {12,13}"
retained_aux_after: "N in {12,13}; exact K-excess roofs; heterogeneous heavy caps; entire block-constant N=12,13 subfamilies eliminated"
evidence:
  - "artifacts/R15/f0111_n1213_heavycap_kexcess_idea_o100w.md @ 2855d5a2ac41205d5620ec85452f04255d2a8f8a"
  - "artifacts/R15/f0111_n1213_kexcess_block_checker_o100w.py @ 10416dfe864b8089b596585898d5835a6eba559d"
  - "artifacts/R15/f0111_n1213_kexcess_block_checker_o100w.out @ a2a3085fe86dca4972814247b3f5d103f7d24e8a"
audit_ids: []
```
