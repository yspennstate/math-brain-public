# B12 FEI — balanced bent selector refutes pointwise local restriction payment

**Classification:** `MECHANISM_REFUTED / ESSENTIAL_STEP_APPLIED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Live scalar candidate `LIMIT-PRIME-GATE-LIFT-v1`:** **OPEN / NOT REFUTED by this report.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub controls and mathematical sources were read directly; no authenticated cognitive-brain retrieval/context was used in the mathematics.

## 0. Live target, last-three comparison, and the exact implication attacked

Fresh owner control revision `2026-09-22.2` supersedes the older native B12 harmonic-row wording for this invocation and asks all FEI workers to converge on the source-exact all-gate inequality

\[
D_\Gamma(G;p):=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
       \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u),
\tag{0.1}
\]

for every finite Boolean gate and every interior product bias. Existence of one finite symmetric nonnegative `Gamma` satisfying (0.1) is equivalent to full FEI.

The last three own substantive B12 reports before this run were:

1. `20260922T025438Z-gate-margin-falsification/REPORT.md`: a source-valid balanced ten-input gate and the inherited shared-graft family refute AND/read-once extremality for the old potential; FEI remains open.
2. `20260922T013941Z-shared-graft-tail/REPORT.md`: proves an analytic infinite-tail increase for the genuine Boolean shared-graft family and the lower floor `C_FEI > 6.5218509495457`; this is lower-bound movement only.
3. `20260921T232119Z-harmonic-root-marked-spectrum/REPORT.md`: proves the one-source harmonic first-mark code but leaves the global continuation/address entropy unpaid.

The current run does not reopen any retired row-local depth/second-moment/rank/l1 route. It attacks a **new exact sufficient implication** introduced by the restriction-cocycle programme.

Two completed other-account results are consumed substantively.

* `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`, creation commit `b6897a3675bb78bb3c262bc73f64ffb1e9c20301`, proves the exact biased restriction entropy/defect cocycle with both mandatory information credits retained and the exact quadratic currency.
* `proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T033410Z-local-boundary-repulsion/REPORT.md`, blob `1734d9c369048def5488adf228dc03e433af3216`, proves that genuinely two-sided local gluing is repelled from a pivot-bias boundary and isolates the still-unproved pointwise interior inequality
  \[
  \mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j+a_*\mathcal W_j\ge0,
  \qquad a_*=0.2682048,
  \tag{0.2}
  \]
  as a sufficient local condition for the live candidate.

I also use `account01/B12/20260922T0342Z-b0-two-overlap-shannon/REPORT.md`, blob `077fb66fc99525d525139ab059409170a87a49b3`, which fixes the live candidate

\[
\Gamma_*(u)=\Gamma_{\rm RO}(u)+a_*u(1-u),
\quad a_*=0.2682048,
\quad \Gamma_*(1/2)=C_*=6.5218512.
\tag{0.3}
\]

The first essential unproved implication is therefore (0.2). This report attacks its negation on a single actual Boolean source.

## 1. Exact restriction interface used

For a pivot of bias `t`, let `f_0,f_1` be the two Boolean sign restrictions, with output probabilities `r_0,r_1`, disagreement probability `delta`, and parent output `r=(1-t)r_0+tr_1`. Account04/B17 proves the exact identity

\[
D_\Gamma(G)
=(1-t)D_\Gamma(G_0)+tD_\Gamma(G_1)
+\mathcal R_{\Gamma,j}+\mathcal C_j,
\tag{1.1}
\]

where the nonnegative credit `C_j` is not discarded, and

\[
\mathcal W_j=t(1-t)\bigl(\delta-(r_1-r_0)^2\bigr)
\tag{1.2}
\]

is the exact local quadratic currency. Equivalently, if

\[
E:=\widetilde H_G-(1-t)\widetilde H_{G_0}-t\widetilde H_{G_1}
\tag{1.3}
\]

is the **actual** conditional spectral-Shannon increment, then combining the exact entropy and defect cocycles gives

\[
\mathcal R_{\Gamma,j}+\mathcal C_j
=(1-t)\Gamma(r_0)+t\Gamma(r_1)-\Gamma(r)
+\delta\bigl(\Gamma(t)+h_2(V_t)\bigr)-E.
\tag{1.4}
\]

This form is useful because it already includes the branch/KL and vertical-overlap refunds. A negative value below is therefore not a dropped-credit artefact.

## 2. A balanced two-point bent selector

Let `m` be even, `N=2^m`, and use coordinates in pairs. Define the Boolean sign function

\[
f_0(x)=(-1)^{x_1x_2+x_3x_4+\cdots+x_{m-1}x_m}
\qquad (x\in\{0,1\}^m).
\tag{2.1}
\]

This is the standard quadratic bent function. Every normalized Walsh coefficient has magnitude `N^{-1/2}`. Put

\[
z=(1,1,0,\ldots,0).
\]

Then `f_0(0)=+1` and `f_0(z)=-1`. Define `f_1` by flipping **exactly these two values**. Thus `f_1-f_0=-2` at `0`, `+2` at `z`, and zero elsewhere. Both restrictions are genuine Boolean signs, they disagree on exactly two physical points, and because the two flipped signs are opposite their means are equal:

\[
\delta={2\over N},
\qquad r_1-r_0=0.
\tag{2.2}
\]

Now make the actual selector gate

\[
F(y,x)=
\begin{cases}
f_0(x),&y=0,\\
f_1(x),&y=1,
\end{cases}
\tag{2.3}
\]

and put the selector at the exactly interior bias `t=1/2`, with all `x`-coordinates uniform.

The equal-output invariant (2.2) is the key. For **every** symmetric or nonsymmetric potential `Gamma`, the first three terms of (1.4) cancel, while `h_2(V_{1/2})=h_2(1)=0`. Therefore

\[
\boxed{
\mathcal R_{\Gamma,y}+\mathcal C_y
=\delta\,\Gamma(1/2)-E_m,
}
\tag{2.4}
\]

and by (1.2)

\[
\boxed{
\mathcal W_y={\delta\over4}.
}
\tag{2.5}
\]

Consequently, relative to any base potential of finite centre `C=Gamma(1/2)`, the exact local quadratic correction demanded by this Boolean node is

\[
\boxed{
 c_y^{\rm loc}=4\left({E_m\over\delta}-C\right).
}
\tag{2.6}
\]

The whole shape of `Gamma` away from `1/2` has disappeared exactly.

## 3. Exact spectrum and the asymptotic local obstruction

Write

\[
u=N^{-1/2}=2^{-m/2}.
\]

Let the normalized bent spectrum be

\[
\widehat f_0(S)=\sigma_S u,
\qquad \sigma_S\in\{\pm1\}.
\]

Let

\[
Z=\{S:\chi_S(z)=-1\}.
\]

Then `|Z|=N/2`. Fourier inversion at `0` and `z` gives

\[
\sum_{S\in Z}\sigma_S=\sqrt N=u^{-1}.
\tag{3.1}
\]

Hence, inside `Z`, the numbers of positive and negative bent signs are exactly

\[
 n_+=\frac N4+\frac{\sqrt N}{2},
\qquad
 n_-=\frac N4-\frac{\sqrt N}{2}.
\tag{3.2}
\]

The two-point flip has normalized Fourier increment

\[
\widehat f_1(S)-\widehat f_0(S)
={-2+2\chi_S(z)\over N},
\]

so it vanishes off `Z` and equals `-4/N=-4u^2` on `Z`. At selector bias `1/2`, the parent horizontal/vertical pair is therefore

\[
\widehat F(S)=
\begin{cases}
\sigma_Su,&S\notin Z,\\
\sigma_Su-2u^2,&S\in Z,
\end{cases}
\qquad
\widehat F(S\cup\{y\})=
\begin{cases}
0,&S\notin Z,\\
-2u^2,&S\in Z.
\end{cases}
\tag{3.3}
\]

All signs and the full Boolean realization are retained.

For compact notation define

\[
L_a(u)={1\over4}\Bigl[
(1+2u)(1-au)^2\log_2(1-au)^2
+(1-2u)(1+au)^2\log_2(1+au)^2
\Bigr].
\tag{3.4}
\]

The exact histograms (3.2)--(3.3) give

\[
\widetilde H(f_0)=m,
\qquad
\widetilde H(f_1)=m-L_4(u),
\tag{3.5}
\]

and

\[
\widetilde H(F)=m(1+2u^2)-4u^2-L_2(u).
\tag{3.6}
\]

Thus

\[
\boxed{
E_m=2mu^2-4u^2-L_2(u)+{1\over2}L_4(u).
}
\tag{3.7}
\]

Since `delta=2u^2`, the Taylor expansion at zero

\[
L_a(u)=
{\frac32a^2-2a\over\ln2}u^2+O_a(u^4)
\tag{3.8}
\]

implies

\[
\boxed{
{E_m\over\delta}
=m-2+{3\over\ln2}+O(2^{-m}).
}
\tag{3.9}
\]

Combining (2.6) and (3.9) proves the central theorem of this report:

### Theorem 3.1 — no finite-centre pointwise local payment

For every boundary-normalized potential whose centre `C=Gamma(1/2)` is finite, the genuine Boolean selector family (2.1)--(2.3) has

\[
 c_y^{\rm loc}\longrightarrow+\infty
\qquad(m\to\infty,\ m\text{ even}).
\tag{3.10}
\]

Equivalently, no finite quadratic lift can make

\[
\mathcal R_{\Gamma,y}+\mathcal C_y+c\mathcal W_y\ge0
\]

hold **pointwise at every exact Boolean restriction node**, even with the full account04/B17 information credit retained.

This does not contradict the weighted-average restriction theorem. The theorem says the **global gate margin** is a weighted average after descendant defects/currencies telescope. The present construction says a proof cannot strengthen that identity into nonnegativity of every individual node: some descendants must supply compensating slack.

## 4. A completely explicit six-bit witness against the live local implication

Take `m=6`, so `N=64`, `delta=1/32`, and `z=3`. The standard-library integer FWHT checker beside this report obtains the exact unnormalized Walsh absolute-value histograms

\[
\begin{array}{c|c}
\text{function}& |W|\text{ histogram}\\ \hline
f_0&8^{\times64}\\
f_1&8^{\times32},\ 4^{\times20},\ 12^{\times12}\\
F&16^{\times32},\ 0^{\times32},\ 4^{\times32},\ 12^{\times20},\ 20^{\times12}.
\end{array}
\tag{4.1}
\]

Therefore, with no numerical optimization,

\[
H(f_0)=6,
\tag{4.2}
\]

\[
H(f_1)=7-{27\over64}\log_2 9,
\tag{4.3}
\]

\[
H(F)=8-{45\over256}\log_2 9-{75\over256}\log_2 25,
\tag{4.4}
\]

and hence

\[
\boxed{
{E_6\over\delta}
=48+{9\over4}\log_2 3-{75\over4}\log_2 5.
}
\tag{4.5}
\]

The elementary integer comparisons

\[
3^2>2^3,
\qquad
5^3<2^7
\]

give the rigorous bounds `log_2 3>3/2` and `log_2 5<7/3`. Hence

\[
\boxed{
{E_6\over\delta}>{61\over8}=7.625.
}
\tag{4.6}
\]

For the live candidate from account01/B12,

\[
C_*=6.5218512={4076157\over625000},
\]

so (2.4) yields the strict exact estimate

\[
\boxed{
\mathcal R_{\Gamma_*,y}+\mathcal C_y
< {1\over32}\left({4076157\over625000}-{61\over8}\right)
=-{172367\over5000000}
=-0.0344734.
}
\tag{4.7}
\]

Thus the pointwise local inequality isolated in account01/B13 is false on an actual Boolean interior gluing, **despite retaining both exact information credits**.

Relative to the base read-once centre

\[
C_0=6.4548={16137\over2500},
\]

the same exact lower bound gives

\[
\boxed{
 c_y^{\rm loc}>4\left({61\over8}-{16137\over2500}\right)
={5851\over1250}=4.6808,
}
\tag{4.8}
\]

far above the live lift `a_*=0.2682048`. Floating evaluation of the exact histogram gives `E_6/delta = 8.03001384748...`, corresponding to local margin about `6.30085539`; those decimals are diagnostic only, not the certificate.

## 5. What survives, and the precise new remaining implication

Three statements must be kept distinct.

1. **Refuted:** the pointwise interior local-payment strengthening (0.2), and in fact every version with a fixed finite quadratic lift and only a finite centre value. The obstruction is source-valid, Boolean, signed, interior, and already includes the exact KL/overlap credits.
2. **Not refuted:** account04/B17's exact restriction-tree cocycle and weighted-average theorem. They are identities and survive unchanged.
3. **Not refuted:** the live scalar candidate `Gamma_*` itself. A negative local node need not make the parent gate defect negative because the two child defects in (1.1) may be positive. This report does not compute or claim a global counterexample to `(G)` for `Gamma_*`.

The needed replacement is therefore genuinely **tree-amortized** rather than pointwise. One must prove a nonreusing sequential/harmonic statement in which high-priced local selector entropy such as (4.5) is charged to descendant gate slack/currency before those descendants are reused elsewhere. In the notation of (1.1), the remaining implication is not `R+C+aW>=0` node by node, but a dimension-free inequality for the **telescoping sum** that retains the signed child defects and pays each descendant reserve at most once. Any valid version must survive the family above, where the raw local price per unit currency grows linearly in `m`.

This is precisely the type of nonlocal marked-spectrum/sequential accounting that the original B12 role was seeking, but the new counterexample now fixes the form it must have: descendant slack is mandatory, not optional.

## 6. Movement fields

**FULL-PROBLEM CHANGE:** `NO FEI UPPER-BOUND CHANGE`. Full uniform-cube FEI remains open. No universal finite `C` is proved in this run, and no Boolean counterexample to FEI is claimed.

**MECHANISM CHANGE:** `YES — decisive falsification`. Before this run, the restriction-cocycle programme had reduced the live candidate to the proposed pointwise interior inequality (0.2) after closing the bias boundary. After this run, (0.2) is rigorously false; more strongly, the exact local margin is unbounded over genuine Boolean restriction nodes for every finite-centre potential. Any continuation using the restriction cocycle must amortize against descendant slack on the whole restriction tree rather than certify nodes individually.

**Quantified remaining implication:** construct a dimension-free, nonreusing tree/sequential inequality that controls the aggregate negative local contributions in (1.1) by the positive child defects and/or aggregate currency, while preserving the exact information credits. The family here forces any such theorem to allow a single node with local margin at least `4.6808` already at `m=6` and margins diverging like `4m+O(1)` along the even-dimensional family.

## 7. Verification and method notes

`verify_balanced_bent_local_obstruction.py` is standard-library only. It checks Booleanity, equal child means, the three integer Walsh histograms in (4.1), the elementary logarithmic bounds behind (4.6), and the exact rational inequalities (4.7)--(4.8). The archived `verification.json` reports `PASS`; its floating entropy values are explicitly diagnostics.

The three fresh FLEET_RULES moves used substantively were **#2 attack the negation first** (test the proposed local implication rather than trying to prove it), **#12 find what is conserved** (equal child output measure cancels the entire unknown potential shape), and **#30 one prime/scale/direction at a time** (one selector over one two-point bent perturbation isolates the first failing gluing step).

Scoped privacy/provenance review: changed files contain mathematical formulas, repository-relative source identifiers, public theorem/function names, and harmless exact arithmetic only. No credentials, scheduler identifiers, machine paths, raw transcripts, unrelated private data, benchmark gold, email/Drive content, paid/remote compute, workflow triggers, permission changes, or public posting are included.
