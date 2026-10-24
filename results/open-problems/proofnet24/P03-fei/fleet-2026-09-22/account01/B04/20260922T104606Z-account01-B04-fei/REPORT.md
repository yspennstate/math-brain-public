# account01/B04 — signed vanishing-selector boundary functional for FEI gate defects

Run: `20260922T104606Z-account01-B04-fei`  
Programme: `FEI-ALL-TEAM-20260922T095941Z`  
Assignment: `FEI-20260922-account01-B04`  
Pathway: A  
Outcome: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 0. Current scope, corrections, and source discipline

The current owner control redirects this slot from the suspended BT4 campaign to the all-team FEI programme. This report therefore does no new BT4 mathematics. Full uniform-cube FEI remains open: the target is one finite dimension-independent constant `C` such that `H(f) <= C I(f)` for every finite uniform-cube Boolean function.

The exact assignment is to derive a source-uniform leading-order expansion of the all-gate defect as one selector bias tends to an endpoint while the two Boolean restrictions are held fixed, retaining the actual signed packet entropy, all `t log t` contributions, and the child defects.

I use the following source-pinned inputs.

1. **All-gate formulation / exact coordinate recursion source.** `yspennstate/math-open-problems`, commit `f5946fb64d336ed7369de279159643944efc47af`, `proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`.
2. **Named OTHER-account result consumed and applied.** account02/B12, `yspennstate/math-open-problems`, commit `4ccd51ad517f425a529daa52c3352905b86ea69d`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`, Sections 2–4. I use its exact genuine-Boolean packet variables, the identity `Delta_i Htilde = B_i + JS`, and the exact child-defect recursion. Its historical coefficient `c=0.337` is now refuted and is not used as a live candidate.
3. **Independent packet-identity source.** account01/B12, `yspennstate/math-open-problems`, commit `92c75e9bcd2fe9c5dc2bedc8a032b31b4afb5484`, `proofnet24/P03-fei/fleet-2026-09-21/account01/B12/20260922T090347Z-folded-js-shannon/REPORT.md`.
4. The current correction layer marks the broad safe-cone selector-floor inference as `NEEDS_REVALIDATION`, because global gate safety does not permit deleting positive child slack. The expansion below keeps the child defects explicitly and does not use that inference.

The assigned partner account02/B04 had no completed report in the current `fleet-2026-09-22/account02/B04` scientific root at the pre-write snapshot. I therefore did not wait synchronously; the named compatible OTHER-account theorem above is consumed exactly, and the present result is ready for the assigned downstream recipient account03/B01.

## 1. Setup and exact packet identity

Fix a finite Boolean gate `G` and a selector input whose bias is

\[
t\in(0,1).
\]

Hold its two genuine Boolean restrictions `G_0,G_1` fixed, with biased Fourier coefficients on the residual variables

\[
u_T=\widehat{G_0}(T),\qquad v_T=\widehat{G_1}(T).
\]

Write

\[
U_T=u_T^2,\qquad V_T=v_T^2,\qquad c_T=(u_T-v_T)^2.
\]

Since both children are Boolean,

\[
\sum_TU_T=\sum_TV_T=1.
\]

Let

\[
d:=\Pr(G_0\ne G_1)
\]

under the fixed residual product measure. Parseval gives

\[
\boxed{\sum_T c_T=4d.}
\tag{1.1}
\]

For the selector packet at `T`, the exact variables from the consumed source are

\[
e_T(t)=(1-t)U_T+tV_T,
\qquad
q_T(t)=\frac{t(1-t)c_T}{e_T(t)}
\tag{1.2}
\]

when `e_T(t)>0`, and

\[
p(t):=\sum_Te_T(t)q_T(t)=4t(1-t)d=:V_t d.
\tag{1.3}
\]

The exact signed conditional spectral-entropy increment is

\[
\boxed{
\Delta\widetilde H(t)
=B(t)+\operatorname{JS}_t(U,V),
}
\tag{1.4}
\]

where

\[
B(t)=\sum_Te_T(t)h_2(q_T(t))
\tag{1.5}
\]

and

\[
\operatorname{JS}_t(U,V)
=H((1-t)U+tV)-(1-t)H(U)-tH(V).
\tag{1.6}
\]

All entropies in this report are base two. As usual `0 log 0=0`.

## 2. Main theorem: exact singular coefficient and finite boundary functional

Define the support of the limiting child

\[
S_0:=\{T:U_T>0\}
\]

and the finite signed functional

\[
\boxed{
\Lambda_0(u,v)
:=
\sum_{T\in S_0}
\left[
 c_T\log_2\frac{U_T}{c_T}
 +V_T\log_2\frac{V_T}{U_T}
\right].
}
\tag{2.1}
\]

A term with `c_T=0` in the first summand is interpreted as zero, and a term with `V_T=0` in the second is interpreted as zero.

### Theorem 2.1 — signed vanishing-selector expansion

For fixed Boolean restrictions `G_0,G_1`, as `t downarrow 0`,

\[
\boxed{
\Delta\widetilde H(t)
=4dt\log_2\frac1t
+t\left(\frac{4d}{\ln2}+\Lambda_0(u,v)\right)
+O_{u,v}\!\left(t^2\log\frac1t\right).
}
\tag{2.2}
\]

Meanwhile

\[
\boxed{
h_2(V_t)
=4t\log_2\frac1t
+4t\left(\frac1{\ln2}-2\right)
+O\!\left(t^2\log\frac1t\right).
}
\tag{2.3}
\]

Consequently the selector's intrinsic Shannon price cancels the entire singular term:

\[
\boxed{
dh_2(V_t)-\Delta\widetilde H(t)
=tE_0(u,v)
+O_{u,v}\!\left(t^2\log\frac1t\right),
}
\tag{2.4}
\]

with the exact finite boundary functional

\[
\boxed{E_0(u,v):=-8d-\Lambda_0(u,v).}
\tag{2.5}
\]

#### Proof

Split the packets according to whether `U_T>0`.

For `U_T>0`,

\[
e_T(t)=U_T+O(t),
\qquad
q_T(t)=t\frac{c_T}{U_T}+O(t^2).
\]

The binary entropy expansion

\[
h_2(x)=x\log_2\frac1x+\frac{x}{\ln2}+O(x^2)
\tag{2.6}
\]

therefore gives, using the exact identity `e_Tq_T=t(1-t)c_T`,

\[
\begin{aligned}
e_T h_2(q_T)
={}&tc_T\log_2\frac1t
+t c_T\left(
  \log_2\frac{U_T}{c_T}+\frac1{\ln2}
\right)\\
&+O_{u,v}\!\left(t^2\log\frac1t\right).
\end{aligned}
\tag{2.7}
\]

If `U_T=0` and `V_T>0`, then `c_T=V_T`, `e_T=tV_T`, and `q_T=1-t`; hence

\[
e_T h_2(q_T)=tV_T h_2(t)
=O\!\left(t^2\log\frac1t\right).
\tag{2.8}
\]

Let

\[
\alpha:=\sum_{U_T=0}V_T.
\]

A direct entropy expansion of `(1-t)U+tV` gives

\[
\operatorname{JS}_t(U,V)
=\alpha t\log_2\frac1t
+t\left[
 \sum_{U_T>0}V_T\log_2\frac{V_T}{U_T}
 +\frac{\alpha}{\ln2}
\right]
+O_{u,v}(t^2).
\tag{2.9}
\]

Adding (2.7) over `U_T>0`, adding (2.8), and then (2.9), the coefficient of `t log_2(1/t)` is

\[
\sum_{U_T>0}c_T+\alpha.
\]

But on `U_T=0`, `c_T=V_T`, so this equals `sum_T c_T=4d` by (1.1). The finite coefficient is exactly `4d/ln2+Lambda_0`. This proves (2.2).

For (2.3), insert `V_t=4t(1-t)=4t+O(t^2)` into (2.6):

\[
V_t\log_2\frac1{V_t}
=4t\log_2\frac1t-8t+O(t^2\log(1/t)),
\]

and `V_t/ln2=4t/ln2+O(t^2)`. Multiplying (2.3) by `d` and subtracting (2.2), the logarithmic terms and the `4d/ln2` terms cancel, leaving `-8d-Lambda_0`. This proves (2.4)-(2.5). `QED`.

### Why the zero coefficients matter

Packets absent from the limiting child (`U_T=0`) are precisely where a new spectral atom is born with mass `tV_T`. They produce the singular `t log(1/t)` part of the Jensen--Shannon term. They must not be Taylor-expanded as if `U_T>0`. The theorem isolates them exactly through `alpha`, then shows that after adding the packet-splitting entropy the total singular coefficient is the physical quantity `4d`, independent of spectral support geometry.

## 3. Gate-defect expansion with child defects retained

Let

\[
q_j:=\Pr(G_j=1),\qquad q_t=(1-t)q_0+tq_1,
\]

and let `D_0=D_\Gamma(G_0)` and `D_1=D_\Gamma(G_1)` denote the two lower-dimensional gate defects at their fixed residual bias vector.

The exact recursion consumed from account02/B12 is

\[
\begin{aligned}
D_\Gamma(G;t)
={}&(1-t)D_0+tD_1\\
&+(1-t)\Gamma(q_0)+t\Gamma(q_1)-\Gamma(q_t)\\
&+d\Gamma(t)+d h_2(V_t)-\Delta\widetilde H(t).
\end{aligned}
\tag{3.1}
\]

This is the point at which the current safe-cone correction matters: the child term `(1-t)D_0+tD_1` remains present and is not discarded.

Assume only that the relevant one-sided finite derivatives exist:

\[
\gamma_0:=\lim_{t\downarrow0}\frac{\Gamma(t)-\Gamma(0)}t,
\tag{3.2}
\]

and

\[
\dot\Gamma(q_0;q_1-q_0)
:=\lim_{t\downarrow0}
\frac{\Gamma(q_0+t(q_1-q_0))-\Gamma(q_0)}t.
\tag{3.3}
\]

For the usual endpoint-normalized FEI potentials `Gamma(0)=0`. Define the finite potential Jensen boundary term

\[
\boxed{
J_\Gamma(q_0,q_1)
:=\Gamma(q_1)-\Gamma(q_0)-\dot\Gamma(q_0;q_1-q_0).
}
\tag{3.4}
\]

### Corollary 3.1 — first-order gate-defect boundary formula

Under (3.2)-(3.3),

\[
\boxed{
D_\Gamma(G;t)=D_0+tF_0+o(t),
}
\tag{3.5}
\]

where

\[
\boxed{
F_0
=(D_1-D_0)
+J_\Gamma(q_0,q_1)
+d\gamma_0
+E_0(u,v).
}
\tag{3.6}
\]

If `Gamma(t)=gamma_0 t+O(t^2)` at zero and has a second-order directional expansion along the segment from `q_0` to `q_1`, then

\[
D_\Gamma(G;t)
=D_0+tF_0+O_{u,v,\Gamma}\!\left(t^2\log\frac1t\right).
\tag{3.7}
\]

This yields an immediate rigorous sign criterion.

- If `D_0>0`, continuity gives a positive collar near `t=0`.
- If `D_0=0` and `F_0>0`, the boundary face has a positive first-order collar.
- If `D_0=0` and `F_0<0`, the proposed potential is genuinely refuted on all sufficiently small positive selector biases with these fixed Boolean restrictions.
- Only the codimension-one case `D_0=F_0=0` requires a second-order analysis.

This converts endpoint behavior from a singular entropy problem into a finite signed functional test on tight lower-dimensional faces.

## 4. The opposite endpoint

Set `s=1-t` and interchange the two children. Define

\[
\gamma_1:=\lim_{s\downarrow0}\frac{\Gamma(1-s)-\Gamma(1)}s.
\]

Then

\[
\boxed{
D_\Gamma(G;1-s)=D_1+sF_1+o(s),
}
\tag{4.1}
\]

with

\[
\boxed{
F_1
=(D_0-D_1)
+J_\Gamma(q_1,q_0)
+d\gamma_1
+E_0(v,u).
}
\tag{4.2}
\]

For symmetric endpoint-normalized potentials, `gamma_1=gamma_0`. Thus both bias endpoints are covered by the same theorem after swapping the two genuine restrictions.

## 5. Required degeneracy and endpoint checks

### 5.1 Agreeing children

If `G_1=G_0`, then `v=u`, `d=0`, `q_1=q_0`, and `D_1=D_0`. We have `Lambda_0=0`, hence `E_0=0` and `F_0=0`. In fact the selector is fictitious and

\[
D_\Gamma(G;t)=D_0
\]

for every `t`. The expansion therefore handles the exact zero-influence case without division by `d` or by a vanishing packet coefficient.

### 5.2 Opposite children

If `G_1=-G_0`, then `v=-u`, `d=1`. On every nonzero packet, `c_T=4U_T`, while `V_T=U_T`. Therefore

\[
\Lambda_0
=\sum_T4U_T\log_2\frac14=-8,
\qquad E_0=0.
\tag{5.1}
\]

Indeed the packet identity is exact here:

\[
\Delta\widetilde H(t)=h_2(V_t).
\]

For a symmetric differentiable potential, `D_1=D_0`, `q_1=1-q_0`, and

\[
F_0
=\gamma_0-(1-2q_0)\Gamma'(q_0).
\tag{5.2}
\]

This is precisely the infinitesimal boundary form of the XOR/subadditivity constraint. Thus the theorem correctly separates the pure sign-twist endpoint from genuinely new packet entropy.

### 5.3 Constant limiting child: a slope-free boundary test

Suppose `G_0` is the constant sign `sigma` and let

\[
d=\Pr(G_1\ne\sigma).
\]

Then `D_0=0`. Up to the global sign, the only nonzero coefficient of `G_0` is the empty coefficient `u_\varnothing=1`, while

\[
v_\varnothing=1-2d.
\]

For all nonempty `T`, `u_T=0`. A direct substitution in (2.1) gives

\[
\boxed{
E_{\rm const}(d)
=-8d
+4d^2\log_2(4d^2)
-(1-2d)^2\log_2((1-2d)^2).
}
\tag{5.3}
\]

For a symmetric endpoint-normalized potential, `q_0` is `0` or `1`, `q_1=d` or `1-d`, and the endpoint derivative appearing through `J_Gamma` cancels the selector term `d gamma_0` exactly. Therefore

\[
\boxed{
D_\Gamma(G;t)
=t\bigl[D_\Gamma(G_1)+\Gamma(d)+E_{\rm const}(d)\bigr]
+o(t).
}
\tag{5.4}
\]

This is a particularly sharp boundary falsification/proof test because it is independent of the unknown endpoint slope of `Gamma`.

For the current smooth safe direction

\[
\eta_\epsilon(p)=1-(1-2p)^4-\epsilon(4p(1-p))^3,
\]

one has `eta_epsilon(t)=8t+O(t^2)`. Hence adding `lambda eta_epsilon` changes `gamma_0` by `8lambda`, but the constant-child coefficient (5.4) depends only on the final finite value `Gamma(d)`; the endpoint-slope change cancels automatically.

## 6. Compact conditional end-to-end argument

The current all-gate equivalence reduces FEI to constructing one finite symmetric nonnegative potential with `D_Gamma(G;p)>=0` for every finite Boolean gate and every interior product-bias vector.

The theorem above pays the complete codimension-one logarithmic singularity exactly. As one physical selector bias tends to zero or one, no uncontrolled `t log t` term remains after the selector's intrinsic `d h_2(V_t)` credit is retained. Therefore a universal all-gate proof can be organized inductively by boundary faces as follows.

1. Every lower-dimensional face with strictly positive child defect extends to a small positive collar by continuity.
2. Every tight lower-dimensional face is governed at first order by the finite functional `F_0` or `F_1`.
3. A negative boundary functional constructs a genuine small-bias Boolean counterfamily to the *candidate potential* immediately.
4. A positive boundary functional certifies a collar and removes that face from the interior burden.
5. Only faces with simultaneous `D_child=0` and `F=0` require second order; the singular entropy itself is no longer an obstruction.

This is a reduction of the endpoint part of the universal all-gate problem, not a proof of FEI. It is compatible with the current correction that child slack cannot simply be deleted: the exact coefficient `(D_1-D_0)` is present in (3.6).

## 7. First unpaid implication

The next precise target is

`BOUNDARY-TIGHT-SIGN-v1`:

> For the current shaped candidate (or any replacement candidate being tested), prove `F_0>=0` and `F_1>=0` for every genuine restriction pair whose limiting child defect is tight, or exhibit one source-valid pair with `F<0`.

The most concrete first subproblem is the constant/nonconstant boundary. Determine the sign, for every genuine Boolean child `G_1`, of

\[
\boxed{
D_\Gamma(G_1)+\Gamma(d)+E_{\rm const}(d),
\qquad d=\Pr(G_1\ne \sigma),
}
\tag{7.1}
\]

with the exact final candidate `Gamma`. A negative value immediately produces a continuum of small positive selector biases violating that candidate. A positive universal lower bound closes every constant-child selector boundary at first order.

A second target is to classify the equality cases of `F_0=0` after `D_0=0`; agreeing children and exact sign twists are already explicitly identified above.

## 8. Status, provenance, and safeguards

**Outcome:** `ESSENTIAL_STEP_APPLIED`.  
**Full FEI:** `OPEN / NOT PROVED`.  
**Native brain:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is real source access but no authenticated native-memory receiver/context was used.  
**Independent end-to-end review:** none claimed.

The derivation above is analytic. A private arithmetic sanity check during this run compared the packet identity and asymptotic coefficient on small genuine Boolean examples; it is not presented as an independent proof or as a universal certificate. The theorem itself is justified by the displayed expansion.

Scoped artifact review: this report contains only FEI mathematics, source pins, run labels, and harmless status metadata. It contains no credentials, scheduler identifiers, machine paths, unrelated private material, sealed benchmark answers, production-data mutations, email/Drive content, paid/remote compute calls, public posting, or permission changes.
