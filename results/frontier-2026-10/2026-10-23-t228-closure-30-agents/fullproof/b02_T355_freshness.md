# B02 focused novelty audit: T355 quantitative slow-time SGD

Date: 2026-10-24. Primary papers, theorem statements and assumptions were checked online. This is a freshness audit, not an endorsement of any new proof that has not yet been reviewed.

**Finding:** The claim that no polynomial quantitative weak-approximation rate is known for ambient SGD near a compact smooth normally attracting minimizer manifold is false. Gu–Lyu–Huang–Arora, ICLR 2023, already give a `tilde O(eta^(1/4))` approximation on the slow time scale. A new `O(sqrt(eta))` result under finite regularity may improve their exponent and hypotheses; it cannot be described as the first quantitative answer to T355's existential-positive-exponent request.

## 1. Exact local target

T355 in `a03/registry422.jsonl` requests, for a stated smooth minimizer-manifold or stratified class and a stated noise class,

\[
\sup_{k\leq T/\eta^2}
\left|\mathbb E f(\theta_k)-\mathbb E f(X_{k\eta^2})\right|
\leq C(T)\eta^a,
\qquad a>0,
\]

with a test-function norm and explicit constants. The invariant-law problem is expressly separate. Root's intended theorem has a compact normally attracting `C6` minimizer manifold, bounded centered state-dependent noise with `C4` coefficients, initial point on the manifold, and exponent `a=1/2`, together with an explicit transient for initial points in the attraction basin.

The comparisons below concern exactly this ambient-SGD slow-time problem. Ordinary-time modified equations and algorithms projected onto a constraint manifold at every step are distinct.

## 2. Decisive prior: Gu–Lyu–Huang–Arora (ICLR 2023)

Primary source: [Why (and When) does Local SGD Generalize Better than SGD?, arXiv:2303.01215v2](https://arxiv.org/html/2303.01215v2), 9 March 2023. This is the ICLR 2023 paper by Xinran Gu, Kaifeng Lyu, Longbo Huang and Sanjeev Arora.

Relevant exact locators:

* Assumptions 3.1–3.3: smooth loss and covariance square root, uniformly bounded stochastic gradients, compact smooth manifold of local minima, and Hessian rank equal to codimension.
* Theorem 3.2: projected Local-SGD weak approximation with exponent `1/4`, up to logarithms, over `eta^-2` gradient steps; the test is `C3`.
* Theorem 3.3: uniform distance from the iterate to its gradient-flow projection after burn-in.
* Section 3.2's technical-contribution paragraph: the paper explicitly identifies ordinary SGD (`K=1`) as a quantitative consequence.
* Appendix I, Theorem I.4: an explicit `C_g eta^(1/4)(log(1/eta))^b` statement, with `C_g,b` independent of `eta`.
* Appendix I, Lemma I.17 and its proof, equations (43)–(45): contraction from a nearby initial point, and control of local iterates inside the tube.

These are not just qualitative weak-convergence theorems. They already provide a polynomial approximation exponent in the same normally attracting compact-manifold setting.

## 3. Independent published restatement removes ambiguity about the SGD time grid

Primary source: [A Quadratic Synchronization Rule for Distributed Deep Learning, ICLR 2024 conference PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/128911cc894d57bcae78074a9551c132-Paper-Conference.pdf), Theorem 3.1, item 1, printed page 5. The theorem attributes its ordinary-SGD item to Gu et al. (2023) and states the slow-SDE estimate at every SGD step, rather than only at local synchronization times. It uses `C4` test functions. Appendix E, Assumption E.1, specifies the bounded-gradient and smoothness assumptions. Appendix E, pages 26–28, also reuses the distance theorem from Gu2023.

Therefore the objection that Gu's main theorem only observes a sparse grid of `H~eta^-1` synchronization rounds does not preserve the original SGD question as open. Its SGD specialization is explicitly recorded in a subsequent primary publication.

## 4. Projected-versus-raw observables: a rigorous bridge

The cited rate is written for `f(Phi(theta_k))`, where `Phi` is the gradient-flow retraction, whereas the registry writes `f(theta_k)`. This is a real difference, but on bounded smooth tests it is not a basis for claiming a new qualitative frontier.

Here is the elementary bridge, stated independently. Suppose on a time set `I_eta` there is a common event `E_eta` of probability at least `1-delta_eta` on which all iterates remain in a fixed tube and

\[
\sup_{k\in I_\eta}\|\theta_k-\Phi(\theta_k)\|
\leq r_\eta.
\]

For a bounded function `f` that is `Lip(f)`-Lipschitz on that tube,

\[
\begin{aligned}
\sup_{k\in I_\eta}
|\mathbb E f(\theta_k)-\mathbb E f(\Phi(\theta_k))|
&\leq \operatorname{Lip}(f)r_\eta
     +2\|f\|_\infty\delta_\eta.
\end{aligned}
\tag{1}
\]

The bound follows by splitting the expectation over `E_eta` and its complement. Combining it with any projected weak error `e_eta` gives raw weak error at most

\[
e_\eta+\operatorname{Lip}(f)r_\eta
+2\|f\|_\infty\delta_\eta.
\tag{2}
\]

For the prior rates, `r_eta` is of order `sqrt(eta log(1/(eta delta_eta)))` and `delta_eta` can be a fixed sufficiently large power of `eta`. Both additional terms are lower order than `eta^(1/4)` up to logarithms. This gives a raw-observable positive-power estimate after the stated burn-in.

For on-manifold initialization, Gu's Lemma I.17 has zero initial-distance term: the induction bound for its normal potential consists of an exponentially decaying initial potential plus a constant multiple of `sqrt(eta log(R/(eta delta)))`. Thus the tube part need not wait for an attraction transient when the initial potential is zero. Local-iterate bounds, not only synchronization-time bounds, appear in the same lemma. This supports applying (1) over the full time window in the on-manifold case.

For a general off-manifold initial point, a raw-observable uniform estimate starting at `k=0` cannot compare with a diffusion initialized at `Phi(theta_0)` without an initial discrepancy term. For example, a bounded smooth `f` separating `theta_0` from `Phi(theta_0)` already has a fixed positive error at time zero. The initial-layer term or exclusion of a burn-in is mathematically necessary, not an optional technical improvement.

This bridge is an inference from the published projection and tube bounds. It should be labeled as such if used, rather than claiming Gu literally printed the raw-observable theorem in this notation.

## 5. What the other named references do and do not cover

| Primary reference | Verified theorem content | Relevance to the proposed `eta^(1/2)` theorem |
|---|---|---|
| [Li–Wang–Arora, arXiv:2110.06914v4](https://arxiv.org/html/2110.06914v4), Theorem 4.6 and Appendix B.4 | Ambient SGD has the manifold diffusion as its distributional limit on the `eta^-2` step scale under attraction, Hessian-rank and global-limit-solution hypotheses. | This source alone does not give a rate. It is not the latest quantitative predecessor. |
| [Shalova–Schlichting–Peletier, JMLR 27(146), 2026](https://jmlr.org/papers/v27/24-0571.html), [published PDF](https://jmlr.org/papers/volume27/24-0571/24-0571.pdf), Sections 3–4 | Broad noise-injection singular limits, with distinct slow scales depending on the noise structure. | Main statements are convergence/limit identification; I did not locate a matching finite-step `eta^(1/2)` weak-error theorem. This is a scoped negative search, not proof of absence. |
| [Gess–Kassing–Rana, arXiv:2402.03467v2](https://arxiv.org/html/2402.03467v2), Theorems 1.2/5.1 | An order-two weak approximation for Riemannian SGD through `floor(T/eta)` steps by an `eta`-dependent Riemannian stochastic modified flow. | Different algorithm, ordinary-time horizon and comparison process. It does not directly close the ambient normally-attracting `eta^-2` theorem. |
| [Wang et al., arXiv:2307.15196v2](https://arxiv.org/html/2307.15196v2), Section 4 and Theorem 4.5 | SGD and momentum SGD share their slow manifold limit; the short-time weak rate is a separate theorem on `eta^-1` steps. | Does not itself establish the proposed all-step `eta^(1/2)` slow approximation rate. |

The Gu2023 theorem is the closest located predecessor, not any of these four.

## 6. Novelty decision and proof-review checklist

It is legitimate to investigate the following theorem as a potential **rate improvement and finite-regularity extension**:

* old quantified compact smooth-manifold bound: `tilde O(eta^(1/4))`;
* proposed new bound: `O(sqrt(eta))`, with explicit `C(T)` and derivative dependence;
* old coefficients/geometry: `C-infinity` in the displayed assumptions;
* proposed finite orders: `C6` loss/geometry and `C4` noise coefficients;
* explicit raw-observable and transient terms, rather than hiding their derivation.

The targeted searches performed here did not locate a theorem with exactly this stronger exponent for this same ambient-SGD class. That is a narrow search result. It is not a novelty certificate, and the exact finite-regularity formulation could be an elementary consequence of general singular-perturbation estimates outside the machine-learning literature.

Before accepting the root's proof, independently verify all of the following:

1. The gradient-flow retraction has the derivative orders claimed on a fixed tube, with quantitative norm bounds; finite regularity of a stable foliation should not be assumed without proof or a correctly matched theorem.
2. The identity `D Phi(x) grad L(x)=0` is valid throughout that tube. It cancels the order-`eta` projected drift; its use only on the manifold would leave an accumulated error.
3. Tube confinement or exit estimates apply uniformly for `O(eta^-2)` steps and support the stated expectation bounds for the unstopped chain.
4. The manifold diffusion semigroup has bounded derivatives through the order needed by the one-step Taylor expansion, uniformly for `0<=t<=T`; ellipticity is not required if a smooth stochastic-flow argument is used, but the actual coefficient regularity must support it.
5. A one-step generator discrepancy of order `eta^(5/2)` in expectation is enough for `eta^-2` telescoping; merely pathwise `O(eta^(5/2) sqrt(log(1/eta)))` would retain a logarithm unless the expectation estimate removes it.
6. The `grad L tensor grad L` term in the second-order discrete expansion is accounted for. With normal second moment `O(eta)`, its cumulative contribution is `O(eta)`, but it is not identically zero.
7. The off-manifold initial condition includes its unavoidable transient term at `k=0`.
8. Every claim of solving T355 is phrased relative to the already published `eta^(1/4)` rate. An improved theorem may be valuable but does not retroactively make the registry's existential-rate claim an unsolved original problem.

**Recommended status:** retain and review the stronger proof if correct; describe it as a candidate improvement over Gu et al. (2023). Do not count the existence of any `a>0` as a new full Top200 problem solution.
