Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run is not verified as GPT-6 at maximum. **No movement in the frozen metric:** `B=infinity -> B=infinity`. Methods tried: **B7, B12, B30**.

# HARD7-01 run 6 — quartic dilation compactification and energy-balance obstruction

Status: **PARTIAL / first recovery after STUCK1** for the full even-log-concave dimensional Brunn--Minkowski conjecture. This run resumes the exact recovery selected in the preceding STUCK1 report rather than restarting admission: dimension three, the quartic product measure, and arbitrary centrally symmetric convex bodies. The new progress is structural rather than a movement of the frozen product-block metric: any counterexample in this quartic subproblem can be pushed away from both dilation endpoints and normalized at an interior scale satisfying an exact conditional-energy balance and a necessary variance-surplus inequality.

## 1. Continuity, ownership, source scope, and current-status check

The canonical claim remains `operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md`, owned by HARD7-01. The source target is

\[
\mu((1-\lambda)K+\lambda L)^{1/n}
\ge (1-\lambda)\mu(K)^{1/n}+\lambda\mu(L)^{1/n}
\tag{DBM}
\]

for every `n>=1`, every even log-concave probability measure `mu` on `R^n`, all nonempty centrally symmetric convex sets `K,L`, and all `lambda in [0,1]`.

At the start of this run I reread the controlling HARD7/new-methods policy, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the canonical claim, and the newest HARD7-01 report. The previous report was the mandatory STUCK1 thinking run and selected exactly one recovery: keep the same canonical source claim and attack the source-valid special case

\[
d\mu_4(x)=Z^{-1}\exp\!\left[-\frac{x_1^4+x_2^4+x_3^4}{4}\right]dx,
\qquad
\mu_4((1-\lambda)K+\lambda L)^{1/3}
\ge (1-\lambda)\mu_4(K)^{1/3}+\lambda\mu_4(L)^{1/3}
\tag{Q3}
\]

for arbitrary centrally symmetric convex bodies `K,L subset R^3`.

A bounded fresh literature check on 2026-09-19 found no source claiming this exact `1/3` conclusion for arbitrary symmetric bodies under the quartic product measure. Relevant current comparisons remain:

- Aishwarya--Rotem, *New Brunn--Minkowski and functional inequalities via convexity of entropy*, arXiv:2311.05446 / Adv. Math. 490 (2026), proves exponent `(p-1)/(pn)` for `p`-homogeneous convex potentials and centered star bodies. For `p=4,n=3`, this gives `1/4`, not `1/3`.
- Xiong--Yang, *The Brunn-Minkowski inequality for the generalized Gaussian distribution*, arXiv:2605.24472 (2026), treats generalized Gaussian/radial settings and extensions for homogeneous potentials but does not supply the exact arbitrary-body quartic-product `1/3` statement used here.
- Livshyts--Marsiglietti--Nayar--Zvavitch, arXiv:1504.04878 / Trans. AMS, proves the source exponent in dimension two and in the stated unconditional measure/body class.
- Cordero-Erausquin--Rotem, Ann. Probab. 51 (2023), proves the full Gardner--Zvavitch inequality for rotationally invariant log-concave measures.
- Yang, arXiv:2607.10104 (2026), gives the current general even-log-concave exponent at order `c/(n^2 log n)` while retaining `1/n` as the conjectural target.

This is a bounded status search, not a worldwide novelty certificate. The structural reductions below have novelty **UNVERIFIED**.

## 2. Frozen metric

The track metric remains

`B = largest number of 1D/2D factors for which (DBM) is proved at the source exponent for every common block-product instance`.

Run 1 proved all finite block counts, hence `B=infinity`. This run does not alter that metric:

\[
\boxed{B=\infty\longrightarrow B=\infty.}
\]

The source conjecture remains OPEN and this track remains PARTIAL.

## 3. B7 — take the limit: both dilation endpoints are quantitatively safe

Write

\[
q(x)=\|x\|_4=(|x_1|^4+|x_2|^4+|x_3|^4)^{1/4},
\qquad V(x)=q(x)^4/4,
\qquad C=\{q\le1\}.
\]

Let `M=(1-lambda)K+lambda L`.

### Proposition 3.1 — small-scale defect bound

If `K,L subset r C`, then

\[
\mu_4(M)^{1/3}
\ge e^{-r^4/12}
\Big((1-\lambda)\mu_4(K)^{1/3}+\lambda\mu_4(L)^{1/3}\Big).
\tag{3.1}
\]

Consequently the relative deficit is at most

\[
1-e^{-r^4/12}=\frac{r^4}{12}+O(r^8).
\tag{3.2}
\]

**Proof.** Since `C` is convex, `M subset rC`. On `rC`,

\[
e^{-r^4/4}\le e^{-V(x)}\le1.
\]

Thus, with `Z=\int e^{-V}`,

\[
Z\mu_4(M)\ge e^{-r^4/4}|M|,
\qquad
Z\mu_4(K)\le |K|,
\qquad
Z\mu_4(L)\le |L|.
\]

Classical Brunn--Minkowski gives

\[
|M|^{1/3}\ge(1-\lambda)|K|^{1/3}+\lambda|L|^{1/3}.
\]

Combining and cancelling `Z^{-1/3}` gives (3.1). ∎

This already says that an arbitrary angular counterexample cannot live asymptotically at the origin under common dilation.

## 4. B12 — conserved quantity: quartic mass becomes ordinary convex-body volume

For a log-concave function `g` on `R^3`, define its Ball body

\[
K_3(g)=\left\{x:\int_0^\infty 3r^2 g(rx)\,dr\ge1\right\}
\]

in the standard radial normalization. Equivalently, in a Euclidean direction `u`,

\[
\rho_{K_3(g)}(u)^3=3\int_0^\infty r^2 g(ru)\,dr.
\]

For a centrally symmetric convex body `K`, set

\[
\mathcal B(K):=K_3(e^{-V}\mathbf 1_K).
\]

The Ball-body theorem makes `\mathcal B(K)` convex because `e^{-V}\mathbf 1_K` is log-concave. More importantly, polar integration gives the exact invariant

\[
\boxed{|\mathcal B(K)|=\int_K e^{-V(x)}dx=Z\mu_4(K).}
\tag{4.1}
\]

So the quartic probability mass is exactly ordinary Euclidean volume after a nonlinear convex-body transform.

Define

\[
F(t)=\left(3\int_0^t s^2e^{-s^4/4}\,ds\right)^{1/3}.
\tag{4.2}
\]

Then for a Euclidean unit vector `u`, because `V(su)=q(u)^4s^4/4`, the transform has the explicit radial formula

\[
\boxed{
\rho_{\mathcal B(K)}(u)
=q(u)^{-1}F(q(u)\rho_K(u)).
}
\tag{4.3}
\]

Also

\[
F_\infty^3
=3\int_0^\infty s^2e^{-s^4/4}ds
=3\,4^{-1/4}\Gamma(3/4).
\tag{4.4}
\]

A very strong sufficient condition for (Q3) would therefore be the inclusion

\[
(1-\lambda)\mathcal B(K)+\lambda\mathcal B(L)
\subseteq \mathcal B((1-\lambda)K+\lambda L),
\tag{4.5}
\]

because ordinary Brunn--Minkowski plus (4.1) would immediately yield (Q3). I do **not** prove (4.5) here. It is a clean reformulation of the middle-scale angular obstruction.

### Proposition 4.1 — large-inner-radius defect bound

Assume `K,L superset rC`. For `c in (0,1]`, define

\[
a_r(c)=\frac{F(cr)}{F_\infty}.
\tag{4.6}
\]

Then

\[
a_r(c)\mathcal B(K)\subseteq\mathcal B(cK).
\tag{4.7}
\]

Indeed, (4.3) and `q(u)rho_K(u)>=r` imply

\[
\frac{\rho_{\mathcal B(cK)}(u)}{\rho_{\mathcal B(K)}(u)}
=
\frac{F(cq(u)\rho_K(u))}{F(q(u)\rho_K(u))}
\ge \frac{F(cr)}{F_\infty}.
\]

Now put

\[
\eta_r(\lambda)
=
\left(
\frac{1-\lambda}{a_r(1-\lambda)}
+
\frac{\lambda}{a_r(\lambda)}
\right)^{-1}.
\tag{4.8}
\]

Since `0 in K,L`, both `(1-lambda)K` and `lambda L` lie in `M`. Hence

\[
a_r(1-\lambda)\mathcal B(K)\subseteq\mathcal B(M),
\qquad
a_r(\lambda)\mathcal B(L)\subseteq\mathcal B(M).
\]

Convexity of `\mathcal B(M)` then yields

\[
\eta_r(\lambda)
\big((1-\lambda)\mathcal B(K)+\lambda\mathcal B(L)\big)
\subseteq\mathcal B(M),
\]

because the coefficients

\[
\eta_r(\lambda)\frac{1-\lambda}{a_r(1-\lambda)},
\qquad
\eta_r(\lambda)\frac{\lambda}{a_r(\lambda)}
\]

sum to one. Applying ordinary Brunn--Minkowski and (4.1) gives

\[
\boxed{
\mu_4(M)^{1/3}
\ge
\eta_r(\lambda)
\Big((1-\lambda)\mu_4(K)^{1/3}+\lambda\mu_4(L)^{1/3}\Big).
}
\tag{4.9}
\]

For fixed `lambda in (0,1)`, `eta_r(lambda) -> 1` as `r -> infinity`.

The approach to one is explicit. Since

\[
F_\infty^3-F(t)^3
=3\int_t^\infty s^2e^{-s^4/4}ds
\le \frac3t e^{-t^4/4},
\tag{4.10}
\]

we have, whenever the bracket is positive,

\[
\frac{F(t)}{F_\infty}
\ge
\left(1-\frac{3e^{-t^4/4}}{F_\infty^3 t}\right)^{1/3}.
\tag{4.11}
\]

Thus the large-scale endpoint is quantitatively safe as well.

No novelty or optimality is claimed for these endpoint bounds; their value here is that they preserve the arbitrary angular geometry while forcing any potential failure into a bounded dilation window.

## 5. B30 — one scale at a time: any counterexample has an interior energy-balanced normalization

Fix full-dimensional centrally symmetric convex `K,L` and `lambda in (0,1)`. Let

\[
M=(1-\lambda)K+\lambda L,
\]

and define the common-dilation ratio

\[
R(t)=
\frac{\mu_4(tM)^{1/3}}
{(1-\lambda)\mu_4(tK)^{1/3}+\lambda\mu_4(tL)^{1/3}}.
\tag{5.1}
\]

Because bounded `K,L` are contained in `RC` for some finite `R`, Proposition 3.1 gives

\[
\liminf_{t\downarrow0}R(t)\ge1.
\tag{5.2}
\]

Because full-dimensional symmetric `K,L` contain `rC` for some `r>0`, Proposition 4.1 applied to `tK,tL` gives

\[
\liminf_{t\to\infty}R(t)\ge1.
\tag{5.3}
\]

Hence if (Q3) fails for this pair at any scale, so that `R(t_0)<1`, continuity forces a global minimum below one at some finite interior scale `t_* in (0,infinity)`.

That interior minimum satisfies a surprisingly rigid scalar condition.

For any fixed full-dimensional symmetric convex `A`, write

\[
a_A(t)=\mu_4(tA)^{1/3},
\qquad
m_A(t)=\mathbb E[V(X)\mid X\in tA],
\qquad
v_A(t)=\operatorname{Var}(V(X)\mid X\in tA).
\tag{5.4}
\]

Using

\[
\mu_4(tA)=Z^{-1}t^3\int_A e^{-t^4V(y)}dy,
\]

and differentiating with respect to `s=log t`, one gets exactly

\[
\frac d{ds}\log a_A(e^s)=1-\frac43m_A(e^s),
\tag{5.5}
\]

\[
\frac d{ds}m_A(e^s)=4\big(m_A(e^s)-v_A(e^s)\big),
\tag{5.6}
\]

and therefore

\[
\frac{d^2}{ds^2}\log a_A(e^s)
=-\frac{16}{3}\big(m_A(e^s)-v_A(e^s)\big).
\tag{5.7}
\]

At the minimizing scale `t_*`, put

\[
w_K=
\frac{(1-\lambda)a_K(t_*)}
{(1-\lambda)a_K(t_*)+\lambda a_L(t_*)},
\qquad w_L=1-w_K.
\tag{5.8}
\]

### Proposition 5.1 — exact energy balance at every normalized counterexample

The stationarity equation `(d/ds) log R(e^s)=0` gives

\[
\boxed{m_M=w_Km_K+w_Lm_L}
\tag{5.9}
\]

at `t_*`, with all quantities evaluated at `t_*`.

**Proof.** The logarithmic derivative of the denominator in (5.1) is the `w_K,w_L` weighted average of the logarithmic derivatives of `a_K,a_L`. Insert (5.5); the constant one cancels, leaving (5.9). ∎

Thus every quartic counterexample can be rescaled so that the conditional quartic energy on the Minkowski interpolant is exactly the mass-weighted average of the endpoint conditional energies.

### Proposition 5.2 — necessary variance surplus

At the same minimizing scale,

\[
\boxed{
v_M
\ge
w_Kv_K+w_Lv_L
+\frac13w_Kw_L(m_K-m_L)^2.
}
\tag{5.10}
\]

**Proof.** Let `ell_A=log a_A`. For

\[
D=(1-\lambda)e^{\ell_K}+\lambda e^{\ell_L},
\]

one has the exact softmax identity

\[
(\log D)''
=w_K\ell_K''+w_L\ell_L''
+w_Kw_L(\ell_K'-\ell_L')^2.
\tag{5.11}
\]

Since `log R=ell_M-log D` has a local minimum at `t_*`, `(log R)''>=0`. Insert (5.5) and (5.7). The mean terms cancel by (5.9), and

\[
(\ell_K'-\ell_L')^2
=\frac{16}{9}(m_K-m_L)^2.
\]

After multiplying by `3/16`, the remaining inequality is exactly (5.10). ∎

This is the main reduction of the run. It is counterexample-oriented: rather than trying another direct proof of (Q3), it says what every genuine counterexample must survive.

## 6. What changed mathematically

Before this recovery, the smallest unproved source-valid special case was simply “quartic product measure in `R^3`, arbitrary symmetric bodies,” with no compact normalization of a possible failure.

After this run, any failure of that special case can be assumed, after a common dilation, to satisfy simultaneously:

\[
R(t_*)<1,
\qquad
m_M=w_Km_K+w_Lm_L,
\qquad
v_M\ge w_Kv_K+w_Lv_L+\frac13w_Kw_L(m_K-m_L)^2.
\tag{6.1}
\]

Moreover the endpoint estimates prove that such a failure cannot escape to `t=0` or `t=infinity`; it must occur in a finite middle-scale window.

This turns the quartic recovery from an unrestricted body-pair search into a scalar stationary obstruction involving the first two conditional moments of `V`. A proof by this route would follow if one could rule out (5.10) at every positive-defect stationary point, while a counterexample search should now target bodies creating a genuine variance surplus in `V` on the Minkowski interpolant.

A related exact one-body identity is useful for future work. For `f_A(t)=mu_4(tA)^{1/3}`,

\[
t^2\frac{f_A''(t)}{f_A(t)}
=\frac19\big(16m_A(t)^2+48v_A(t)-60m_A(t)\big),
\tag{6.2}
\]

so concavity along a common homothetic ray is equivalent to

\[
4m_A(t)^2+12v_A(t)\le15m_A(t).
\tag{6.3}
\]

I do not claim (6.3) for all convex `A`; current literature contains several results on dilates, so its novelty/status must be checked before using it as a claimed new theorem. Here it is only an exact diagnostic identity derived from (5.5)--(5.7).

## 7. Why no checker was created

The claims in this run are analytic identities and inequalities with complete proofs on the page. There is no finite exhaustive claim to certify. Under the 90/10 policy, manufacturing a numerical checker for unchanged `B=infinity` would add bookkeeping without research value, so none was created.

No discretely sampled body search is presented as evidence for or against the continuous source statement.

## 8. Section-I state and next attack

This is **recovery 1 after STUCK1**. The frozen metric did not move, but the remaining obligation changed materially: the selected quartic subproblem is now compactified along every common dilation orbit and any counterexample must satisfy the exact stationary moment conditions (5.9)--(5.10). Therefore this run is not another repetition of the same unresolved obligation.

If subsequent runs leave this obstruction unchanged for three runs, Section I fires again. The next proposed, nonrepeating triple is:

- **B8**: discretize the `q`-angular survival function of a convex body while preserving exact convexity constraints;
- **B13**: search for a monotone quantity in the conditional Gamma-type radial moments that forbids the variance surplus (5.10);
- **B21**: look for the same moment inequality in Gamma truncation, Hardy, localization, or Brascamp--Lieb literature under another name.

The immediate technical question is whether convexity of the radial cutoff imposes a sharp inequality on the conditional pair `(m_A,v_A)` stronger than monotonicity of the cutoff alone.

## 9. Capability statement

The current exposed scheduler interface still has no model selector, reasoning-effort selector, or guaranteed execution duration. GPT-6/maximum remains prompt-requested only. This run actually identifies as **GPT-5.6 Sol** and the reasoning level is **UNVERIFIED**.

Repository records are context-dependent about native scheduler permissions: `operations/NEW_METHODS_2026-09-16.md` records earlier P26/P01/P03 probes returning `You cannot modify this task`, whereas the newer root `RESULTS.md` records a later successful P26 update in another authorized context. This run did not probe, create, disable, or modify any other schedule. Where the native interface denies modification, the permitted workaround remains the authorized account/workspace interface or platform support, not a duplicate job or permission bypass.

## ledger_delta

- track: `HARD7-01`
- canonical target: even log-concave dimensional Brunn--Minkowski conjecture
- status: `PARTIAL`
- frozen metric: `B=infinity -> B=infinity` (no movement)
- recovery target: quartic product measure in dimension 3 with arbitrary centrally symmetric convex bodies
- substantive progress: common-dilation endpoint safety; exact Ball-body mass/volume transform; any counterexample can be normalized to an interior scale obeying exact conditional-energy balance (5.9) and necessary variance-surplus condition (5.10)
- methods: `B7, B12, B30`
- finite checker: none warranted
- root shared-ledger write: none; P26/shared maintainer retains root reconciliation role
