# fleet03/B13 — bent two-point swaps make the exact local gate margin unbounded

**Classification:** `CANDIDATE_REFUTED / REPLACEMENT_OBLIGATION_SHARPENED`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact live target and peer result consumed

The live owner target is the all-gate FEI inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h_2(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

for one symmetric nonnegative finite-cap potential and every Boolean gate/product bias. The source gate-reformulation proves that a universal finite-cap solution is equivalent to full FEI.

This run consumes, and directly attacks the new missing implication in, the other-account report

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B13/20260922T033410Z-local-boundary-repulsion/REPORT.md`

(created by commit `96d06dcb8734ffddd4dd8d7387e1d599f08540f1`). That report in turn uses fleet04/B17's exact restriction cocycle

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`

(created by commit `b6897a3675bb78bb3c262bc73f64ffb1e9c20301`).

Write

\[
\Gamma_*(u)=\Gamma_{\rm RO}(u)+a_*u(1-u),
\qquad
 a_*=0.2682048,
\qquad
 C_0:=\Gamma_{\rm RO}(1/2)=6.4548.
\tag{0.1}
\]

For a physical pivot of bias `t`, Boolean restrictions `G_0,G_1`, disagreement probability `delta`, output-bias difference `Delta=r_1-r_0`, and the exact information credit `C_j>=0`, fleet04/B17 proves

\[
D_\Gamma(G)
=(1-t)D_\Gamma(G_0)+tD_\Gamma(G_1)
+\mathcal R_{\Gamma,j}+\mathcal C_j,
\tag{0.2}
\]

and the quadratic currency

\[
\mathcal W_j=t(1-t)(\delta-\Delta^2)\ge0.
\tag{0.3}
\]

At positive-currency nodes it defines

\[
c_j^{\rm loc}
=-\frac{\mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j}{\mathcal W_j}.
\tag{0.4}
\]

Fleet01/B13 localized the surviving proof obligation to

\[
\boxed{
\mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j
+a_*\mathcal W_j\ge0
}
\tag{LOCAL}
\]

for every genuinely two-sided interior restriction pair. It proved strong boundary repulsion and the one-sided AND/OR case, leaving the interior case as the next implication.

This report gives an explicit genuine Boolean counterfamily to `(LOCAL)`. In fact its local requested correction `c_j^loc` is unbounded.

This does **not** refute `(G)` or FEI. It refutes a pointwise-local proof of `(G)` based on bounding every positive-currency restriction node by one scalar lift.

## 1. A realizable Boolean family

Let `m=2d` be even and `N=2^m`. On `F_2^m`, define the standard quadratic bent function

\[
f_0(x)=(-1)^{Q(x)},
\qquad
Q(x)=x_1x_2+x_3x_4+\cdots+x_{m-1}x_m.
\tag{1.1}
\]

Take

\[
u=0,
\qquad
v=e_1+e_2.
\tag{1.2}
\]

Then `f_0(u)=+1` and `f_0(v)=-1`. Define `f_1` by toggling exactly those two values:

\[
f_1(x)=
\begin{cases}
-f_0(x),&x\in\{u,v\},\\
 f_0(x),&\text{otherwise}.
\end{cases}
\tag{1.3}
\]

Both restrictions are genuine Boolean functions and have exactly the same mean, hence the same interior output bias. Their disagreement probability is

\[
\delta=\Pr[f_0\ne f_1]=\frac2N,
\qquad
\Delta=0.
\tag{1.4}
\]

Now form the actual `(m+1)`-input Boolean gate whose restrictions at a new pivot `j` are `f_0,f_1`, and put the pivot at bias `t=1/2`. Therefore

\[
\mathcal W_j=\frac{\delta}{4}>0.
\tag{1.5}
\]

There is no non-Boolean relaxation and no integrability issue: the pair is literally the two physical restrictions of one Boolean gate.

For the quadratic bent function,

\[
\widehat f_0(S)=N^{-1/2}\sigma_S,\qquad \sigma_S\in\{\pm1\}.
\tag{1.6}
\]

Put

\[
\rho=\frac4{\sqrt N}.
\tag{1.7}
\]

The two-point toggle changes the normalized coefficient by zero when `<S,v>=0`, and by `-4/N` when `<S,v>=1`. Hence on the odd half of the spectrum

\[
\widehat f_1(S)=N^{-1/2}(\sigma_S-\rho).
\tag{1.8}
\]

Among those `N/2` odd indices, the bent signs have the exact counts

\[
n_+=\frac N4+\frac{\sqrt N}{2},
\qquad
n_-=\frac N4-\frac{\sqrt N}{2}.
\tag{1.9}
\]

These identities give a closed finite formula for every information term in the restriction cocycle.

## 2. Exact local information formula

Let `B` be the restriction branch and `S` the paired Fourier index in fleet04/B17's exact cocycle. Let `J` be its within-pair Fourier-layer bit.

At the uniform pivot `H(B)=1`. Since the two restrictions have equal output bias, the potential's output Jensen term cancels. The exact remainder is

\[
\mathcal R_{\Gamma_{\rm RO},j}
=\delta C_0-1-h_2(\delta).
\tag{2.1}
\]

The exact credit is

\[
\mathcal C_j=H(B\mid S)+I(S;J).
\tag{2.2}
\]

Write

\[
\operatorname{JS}:=I(B;S)=1-H(B\mid S),
\qquad
H_J:=H(J\mid S).
\tag{2.3}
\]

Since `I(S;J)=h_2(delta)-H_J`, (2.1)-(2.3) collapse to

\[
\boxed{
\mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j
=\delta C_0-\operatorname{JS}-H_J.
}
\tag{2.4}
\]

Consequently the exact local correction request is

\[
\boxed{
c_j^{\rm loc}
=4\frac{\operatorname{JS}+H_J}{\delta}-4C_0.
}
\tag{2.5}
\]

Thus the quantity a pointwise-local proof would have to bound is not a small curvature remainder. It is the branch Jensen-Shannon information plus the full within-pair conditional entropy, divided by the tiny disagreement mass.

For completeness, the exact finite formulas are as follows. On the even half, `P_0=P_1=1/N`, so the branch posterior is `1/2` and `J=0`. On the two odd sign classes define

\[
T_\pm=\frac{1+(1\mp\rho)^2}{2N},
\qquad
\pi_\pm=\frac{(1\mp\rho)^2}{1+(1\mp\rho)^2},
\qquad
\theta_\pm=\frac{\rho^2}{2[1+(1\mp\rho)^2]}.
\tag{2.6}
\]

Then

\[
H(B\mid S)=\frac12+n_+T_+h_2(\pi_+)+n_-T_-h_2(\pi_-),
\tag{2.7}
\]

\[
H_J=n_+T_+h_2(\theta_+)+n_-T_-h_2(\theta_-),
\tag{2.8}
\]

and `JS=1-H(B|S)`.

## 3. Decisive six-variable counterexample to the live local implication

Take `m=6`, so `N=64`, `rho=1/2`, and

\[
\delta=\frac1{32},
\qquad
\mathcal W_j=\frac1{128}.
\tag{3.1}
\]

The unnormalized Walsh coefficients of `f_0` are all `+/-8`. The exact categories for `(<S,v>, W_0(S), W_1(S))` are

\[
(0,8,8):16,\quad
(0,-8,-8):16,\quad
(1,8,4):20,\quad
(1,-8,-12):12.
\tag{3.2}
\]

Therefore

\[
H(B\mid S)=\frac12+20\frac5{512}h_2(1/5)+12\frac{13}{512}h_2(9/13),
\tag{3.3}
\]

and

\[
H_J=20\frac5{512}h_2(1/10)+12\frac{13}{512}h_2(1/26).
\tag{3.4}
\]

The attached rational outward-log checker proves

\[
\operatorname{JS}=0.087676747337935790\ldots,
\tag{3.5}
\]

\[
H_J=0.163261185395956632\ldots,
\tag{3.6}
\]

and hence

\[
\boxed{c_j^{\rm loc}=6.3008553899382295\ldots}
\tag{3.7}
\]

whereas the live scalar lift is only

\[
a_*=0.2682048.
\tag{3.8}
\]

Equivalently,

\[
\boxed{
\mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j+a_*\mathcal W_j
=-0.047130082733892418\ldots<0.
}
\tag{3.9}
\]

The local candidate `(LOCAL)` is therefore **REFUTED by an actual Boolean restriction pair**. The failure is not marginal: the local requested correction exceeds the live lift by more than `6.03`.

## 4. Stronger theorem: the local requested correction is unbounded

The six-variable example is only the first positive member of an asymptotic obstruction.

As `m=2d -> infinity`, `rho=4/sqrt(N) -> 0` and `delta=rho^2/8`. Taylor expansion of the exact formulas (2.6)-(2.8) gives

\[
\operatorname{JS}=\frac{2}{\ln2}\,\delta+o(\delta),
\tag{4.1}
\]

and, because `sum_S T_S theta_S=delta` while every active `theta_S=2 delta (1+o(1))`,

\[
H_J=\delta\left[\log_2\frac1\delta-1+\frac1{\ln2}\right]+o(\delta).
\tag{4.2}
\]

Substitution into (2.5) yields

\[
\boxed{
c_j^{\rm loc}=4\log_2\frac1\delta+4\left(\frac3{\ln2}-1-C_0\right)+o(1).
}
\tag{4.3}
\]

Since `delta=2^(1-m)`,

\[
c_j^{\rm loc}=4m+4\left(\frac3{\ln2}-2-C_0\right)+o(1),
\tag{4.4}
\]

and in particular

\[
\boxed{\sup c_j^{\rm loc}=+\infty}
\tag{4.5}
\]

over genuine two-sided interior Boolean restriction nodes.

The checker evaluates the exact closed formula with rigorous log intervals at even dimensions `m=4,...,20`:

\[
\begin{array}{c|c}
m & c_j^{\rm loc}\\\hline
4&-6.348525012981\\
6& 6.300855389938\\
8&15.204680941105\\
10&23.421577157496\\
12&31.475283448635\\
14&39.488678331770\\
16&47.492025082133\\
18&55.492861646731\\
20&63.493070780196.
\end{array}
\tag{4.6}
\]

The asymptotic statement is analytic; the table is only a finite illustration.

## 5. What this refutes, and what it does not

### REFUTED

The fleet01/B13 replacement obligation

\[
\mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j+a_*\mathcal W_j\ge0
\]

for **every** genuinely two-sided interior physical restriction gluing is false.

More strongly, no finite scalar `a` can make that pointwise-local inequality true at every such node.

Thus the exact restriction-tree cocycle cannot be closed by proving a uniform cap on each local `c_j^loc`, even after retaining the branch/KL and within-pair information credits.

### NOT REFUTED

- the exact fleet04/B17 restriction cocycle;
- its weighted-average identity for the **whole** completed restriction tree;
- the all-gate inequality `(G)`;
- the stable global candidate `Gamma_*`;
- FEI.

There is no contradiction with the weighted-average theorem. A node can have enormous positive local requested correction while its descendants have compensating negative margin. The whole-tree weighted average, not every node separately, is the object relevant to a global gate margin.

This is exactly the distinction between an aggregate/useful critical-descendant assertion and an every-node/every-core assertion.

## 6. Replacement obligation and next attack

The proof architecture must retain child slack quantitatively.

A viable next implication has to control an **aggregate** such as

\[
\sum_v \mu_v\bigl(\mathcal R_{\Gamma_{\rm RO},v}+\mathcal C_v+a_*\mathcal W_v\bigr)
\tag{6.1}
\]

over a realizable restriction tree, or pair every large positive `c_v^loc` with descendant slack before discarding it. A pointwise local lower bound is impossible.

The next concrete attack is to exploit the exact bent-swap formulas to identify the compensation mechanism: the same flat spectrum that makes `H(J|S)/delta ~ log(1/delta)` also gives large positive lower-dimensional child defect. The target is a two-generation inequality paying the local `JS+H(J|S)` term directly from the two child defects, with no ambient-dimension factor. If such a payment survives this extremal family and the Numaro/shared-graft family, it plugs directly into fleet04/B17's exact telescoping identity.

## 7. Required handoff fields

- `exact_candidate_version`: `LIMIT-PRIME-GATE-LIFT-v1`, `Gamma_*=Gamma_RO+0.2682048 p(1-p)`, together with fleet01/B13's interior local implication `(LOCAL)`.
- `prior_missing_implication`: prove `(LOCAL)` for every genuinely two-sided interior physical restriction pair after boundary repulsion.
- `consumed_peer_artifact`: fleet01/B13 `20260922T033410Z-local-boundary-repulsion/REPORT.md`, commit `96d06dcb8734ffddd4dd8d7387e1d599f08540f1`; underlying exact cocycle fleet04/B17 commit `b6897a3675bb78bb3c262bc73f64ffb1e9c20301`.
- `applied_to_claim`: substitute the exact quadratic-bent two-point-swap restrictions into the peer's `R+C+a_*W` expression.
- `new_proved_inference`: equations (2.4)-(2.5) and the unbounded bent-swap local-margin theorem (4.3)-(4.5).
- `exact_failed_claim`: `(LOCAL)`; already `m=6` gives lifted local defect `<-0.04713`.
- `replacement_obligation`: preserve and spend descendant/child slack in an aggregate restriction-tree inequality; no pointwise finite local cap can work.
- `next_recipient`: primary `fleet01/B13`; secondary `fleet04/B17` and `fleet03/B18`.
- `implication_to_full_FEI`: `OPEN -> OPEN`; one proposed proof bridge is decisively removed, while the exact tree cocycle survives and its necessary aggregate form is now sharply identified.

## 8. Verification and scope

`CHECKER.py` independently reconstructs the `m=6` truth tables, computes their integer Walsh spectra, verifies the exact category counts (3.2), and then evaluates the closed information formulas using rational atanh-series enclosures for every logarithm. It certifies both

\[
c_j^{\rm loc}>6>a_*
\]

and

\[
\mathcal R+\mathcal C+a_*\mathcal W<0.
\]

`CHECK_OUTPUT.txt` records the executed output.

Scoped privacy/provenance review: this package contains only mathematical formulas and repository-relative artifact identifiers. It contains no credentials, scheduler identifiers, machine paths, raw private transcripts, benchmark answers, unrelated private data, email/Drive action, paid model/API/Codex use, remote workflow dispatch, permission change, or public-posting action.
