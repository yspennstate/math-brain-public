Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No source-metric movement: `D_B=2 -> D_B=2`; this is the third consecutive no-movement run on the current weak-(B) target, so STUCK1 is now triggered for the next invocation. Methods tried: B11 / B20 / B30.**

# HARD7-01 run 12 — cone-measure variance–dissipation, an exact angular-mixture obstruction, and homogeneous scalarization

Status: **PARTIAL / source OPEN / STUCK1 TRIGGERED**.

## 1. Continuity, ownership, exclusions, and current status

This run resumes the unique current HARD7-01 target and the newest immutable checkpoint

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T07-04-40Z__weakB_reverse_hazard_radial_score.md`

at commit

`123b0d3126904f1683d2006ad2e332c42de715a1`.

That report used B1/B3/B6 and ended with the second consecutive unchanged source metric. I therefore did not restart admission, did not return to the exhausted dimensional Brunn--Minkowski predecessor, and did not reuse the previous method triple.

The canonical create-only claim remains

`operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`,

owned by HARD7-01 and marked `CLAIMED / source OPEN / research PARTIAL only`.

At run start I reread/reconciled the HARD7 control, the new-methods policy and owner directive, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current claim, the newest own report, and the newest neighboring R02 state available from the repository. Repository-wide alias searches for `(B)-conjecture`, `B-conjecture`, log-concavity of dilates, and the frozen metric recovered no competing canonical owner. Indexed search covers intake material, but I do not claim a byte-for-byte reread of every append-only intake ledger through a bounded connector response.

The exact source target remains:

> For every integer `n>=1`, every even log-concave probability measure `mu` on `R^n`, and every origin-symmetric convex body `K`, prove that `t -> mu(e^t K)` is log-concave on `R`.

The frozen source metric is

\[
D_B:=\max\{d:\text{the exact weak (B) statement is proved for all admissible }(\mu,K)
\text{ in every }n\le d\}.
\]

The verified baseline is Saroglou's planar theorem, hence

\[
\boxed{D_B=2.}
\]

A fresh bounded current-literature screen on 2026-09-19 again found no primary paper claiming the unrestricted all-dimensional even-log-concave statement. The checked current landmarks were:

- C. Saroglou, *More on logarithmic sums of convex bodies*, Mathematika 62 (2016), arXiv:1409.4346: log-Brunn--Minkowski implies `(B)` in the same dimension, yielding the planar case.
- D. Cordero-Erausquin and L. Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), arXiv:2111.05110: proves `(B)` for rotationally invariant log-concave measures.
- D. Cordero-Erausquin and A. Eskenazis, *Concavity principles for weighted marginals*, arXiv:2506.16941 (2025): proves substantial structured classes, not the unrestricted statement.
- S. Armeniakos and J. Ulivelli, *A strengthening of the dimensional Brunn-Minkowski conjecture implies the (B)-Conjecture*, arXiv:2602.23350 (submitted 2026-02-26): gives a stronger-dimensional-BM implication and the hereditarily-convex class.
- E. Putterman, *Sharp stability for the (B)-theorem*, arXiv:2608.08472 (2026): concerns the Gaussian `(B)` theorem and stability/strong variants, not the unrestricted even-log-concave conjecture.

This is bounded negative evidence only, not a worldwide novelty certificate. No exclusion or ownership collision was found. Therefore the metric for this run is

\[
\boxed{D_B:2\longrightarrow2.}
\]

The restricted identities below are not misreported as `D_B=3`.

## 2. New idea before code: separate the radial one-dimensional theorem from the angular mixing problem

The previous run showed that the curvature of

\[
Q(t):=\mu(e^tK)
\]

can be written as a radial-score variance minus a radial-acceleration mean. That formula does not yet identify which part is genuinely one-dimensional and which part is caused by angular geometry.

This run changes viewpoint completely: disintegrate Lebesgue measure into **cone direction plus logarithmic radius**. The resulting formula shows that every individual ray already has the desired log-concavity. The only possible failure is a quantitatively identifiable angular mixing variance.

This is the principal research move of the run; the exact checker was written only after this route produced a concrete obstruction worth checking.

## 3. B11 — DUALIZE: cone-measure variance–dissipation identity

Assume first that

\[
d\mu(x)=Z^{-1}e^{-V(x)}\,dx,
\]

where `V` is finite, even, convex and coercive. Let `K` be an origin-symmetric convex body with `0` in its interior. Let `nu_K` be the cone probability measure on `partial K`, characterized by the polar-disintegration identity

\[
\int_K g(x)\,dx
= n|K|\int_{\partial K}\int_0^1 g(ru)r^{n-1}\,dr\,\nu_K(du)
\tag{3.1}
\]

for nonnegative measurable `g`. This definition does not require a smooth boundary.

For each cone direction `u in partial K`, set

\[
f_u(s):=\exp\{ns-V(e^su)\},
\qquad
q_u(t):=\int_{-\infty}^t f_u(s)\,ds.
\tag{3.2}
\]

Applying (3.1) to `e^tK` and then using `r=e^s` gives the exact decomposition

\[
\boxed{
Q(t)=\mu(e^tK)
=\frac{n|K|}{Z}\int_{\partial K}q_u(t)\,\nu_K(du).
}
\tag{3.3}
\]

### Proposition 3.1 — every ray is already log-concave

For each fixed `u`, `q_u` is log-concave on `R`.

#### Proof

The one-variable function

\[
r\mapsto V(ru),\qquad r\ge0,
\]

is convex. Because `V` is even, it attains its minimum at `r=0`; hence it is nondecreasing on `[0,infinity)`. The exponential map `s -> e^s` is convex, so the standard composition rule for a convex nondecreasing outer function gives

\[
s\mapsto V(e^su)
\]

convex. Therefore

\[
s\mapsto ns-V(e^su)
\]

is concave, and `f_u` is log-concave. The cumulative integral

\[
q_u(t)=\int_{s\le t}f_u(s)\,ds
\]

is log-concave by the one-dimensional Prékopa theorem (equivalently, integrate the jointly log-concave function `f_u(s) 1_{s<=t}` in `s`). This proves the proposition. `square`

So a source counterexample cannot live on a single radial line. It must be created by **mixing different already-good rays**.

Now assume `V` is `C^2`, so all derivatives below are classical; the formulas also hold at a.e. differentiability points under the usual approximation. Define the directional reverse hazard and its one-dimensional damping by

\[
h_u(t):=\frac{q'_u(t)}{q_u(t)},
\qquad
\kappa_u(t):=-(\log q_u)''(t)\ge0.
\tag{3.4}
\]

Let the scale-dependent angular law be

\[
w_t(du)
:=\frac{q_u(t)\nu_K(du)}{\int q_v(t)\nu_K(dv)}.
\tag{3.5}
\]

Differentiating (3.3) gives

\[
(\log Q)'(t)=\mathbb E_{w_t}h_u(t).
\tag{3.6}
\]

For any differentiable family `a_u(t)`, differentiation under the tilted law gives

\[
\frac d{dt}\mathbb E_{w_t}a_u
=\mathbb E_{w_t}a'_u+\operatorname{Cov}_{w_t}(a_u,h_u).
\tag{3.7}
\]

Putting `a_u=h_u` and using `h'_u=-kappa_u` yields the exact identity

\[
\boxed{
(\log Q)''(t)
=\operatorname{Var}_{w_t}(h_u(t))
-\mathbb E_{w_t}\kappa_u(t).
}
\tag{3.8}
\]

Thus, at every scale where the derivatives exist, weak `(B)` is exactly the angular variance–dissipation inequality

\[
\boxed{
\operatorname{Var}_{w_t}(h_u(t))
\le
\mathbb E_{w_t}\kappa_u(t).
}
\tag{3.9}
\]

This separates the problem sharply:

- each ray contributes a nonnegative one-dimensional damping `kappa_u`;
- angular heterogeneity contributes the positive variance of the raywise reverse hazards;
- the full conjecture says convex geometry never allows the angular variance to dominate the average radial damping.

There is also a direct link to the previous radial-score formula. Let

\[
A(x):=\langle x,\nabla V(x)\rangle.
\]

Since

\[
\frac d{dt}\log f_u(t)=n-A(e^tu),
\]

we have

\[
h'_u=h_u\big(n-A(e^tu)-h_u\big),
\]

and therefore

\[
\boxed{
\kappa_u(t)=h_u(t)\big(h_u(t)+A(e^tu)-n\big).
}
\tag{3.10}
\]

Proposition 3.1 forces the right side to be nonnegative. Equations (3.8)--(3.10) are a new exact localization of the same curvature sign into radial damping versus angular mixing.

**Outcome B11.** Successful structural reduction. It does not prove the source conjecture, but it identifies the only possible mechanism of failure after every one-dimensional ray has already been solved.

## 4. B20 — FIND WHY THE ALGORITHM FAILS: arbitrary mixtures of the good ray kernels are false

The obvious algorithm suggested by Proposition 3.1 is:

> prove every `q_u` log-concave, then invoke a generic principle that their positive mixture is log-concave.

That generic principle is false. More importantly, it already fails inside the exact kernel family generated by homogeneous radial restrictions.

Take `n=p=3` and consider a positively 3-homogeneous potential along a ray. If

\[
v:=V(u)>0,
\qquad s=e^{3t},
\]

then the directional cumulative in (3.2) is

\[
q_v(t)=\frac1{3v}\big(1-e^{-sv}\big).
\tag{4.1}
\]

Each such `q_v` is log-concave by Proposition 3.1.

Now relax the geometric realizability constraint and allow the angular `v`-law to be an arbitrary probability measure. Take the exact two-point law

\[
\rho=\frac1{20}\delta_L+\frac{19}{20}\delta_{20L},
\qquad L:=\log2.
\tag{4.2}
\]

Let `M(t)` be the corresponding mixture of (4.1). Removing the irrelevant common factor `1/3`, write

\[
F(s)=\frac1{20}\frac{1-e^{-sL}}{L}
+\frac{19}{20}\frac{1-e^{-20sL}}{20L},
\qquad M(t)\propto F(e^{3t}).
\tag{4.3}
\]

At `t=0`, hence `s=1`, define rational numbers `A,B,C` by

\[
F(1)=\frac A L,
\qquad F'(1)=B,
\qquad F''(1)=-LC.
\tag{4.4}
\]

Direct exact arithmetic gives

\[
A=\frac{6081737}{83886080},
\quad
B=\frac{524307}{20971520},
\quad
C=\frac{131167}{5242880}.
\tag{4.5}
\]

Put

\[
P:=\frac BA=\frac{2097228}{6081737},
\qquad
R:=\frac CA+P^2
=\frac{17161936437248}{36987524937169}.
\tag{4.6}
\]

By the chain rule,

\[
\frac1{9}(\log M)''(0)
=\frac{F'(1)}{F(1)}+\frac{F''(1)}{F(1)}
-\left(\frac{F'(1)}{F(1)}\right)^2
=L(P-LR).
\tag{4.7}
\]

The exact rational threshold is

\[
\frac PR
=\frac{3188697281259}{4290484109312}
>\frac7{10},
\tag{4.8}
\]

because

\[
10\cdot3188697281259-7\cdot4290484109312
=1853584047406>0.
\]

Also `log 2<7/10`: indeed

\[
e^{7/10}
>\sum_{j=0}^4\frac{(7/10)^j}{j!}
=\frac{482921}{240000}
=2+\frac{2921}{240000}>2.
\tag{4.9}
\]

Therefore

\[
L<\frac7{10}<\frac PR,
\]

so (4.7) is strictly positive:

\[
\boxed{(\log M)''(0)>0.}
\tag{4.10}
\]

Hence **even the exact 3-homogeneous directional kernels do not remain log-concave under arbitrary angular mixing**.

This is deliberately *not* called a counterexample to weak `(B)`. The law (4.2) is a relaxation of the angular geometry. In fact, for `n>=2`, if `V` is continuous on connected `partial K` and cone measure has full support, a nonconstant pushforward `V_*nu_K` cannot be supported on exactly two separated points. If it were, any intermediate value supplied by connectedness and continuity would have a relatively open preimage neighborhood of positive cone measure, contradicting two-point support.

So the exact computation isolates rather than solves the source problem: **the missing theorem has to use geometric realizability of the angular law.**

The finite rational core was executed and archived at

- checker commit `183332d00df2e6c813d4be6565c5110728459520`,
- output commit `a447749ceb6fa19e935a67b6d67e1593ce776cf3`,

with final line

`ALL_EXACT_CHECKS_PASS = True`.

This is a self-check, not an independent audit.

**Outcome B20.** Successful obstruction. It kills the naive “raywise log-concavity + arbitrary mixture” proof route with an exact source-shaped kernel calculation and identifies the extra ingredient any proof must contain.

## 5. B30 — ONE SCALE / ONE DIRECTION AT A TIME: homogeneous scalarization to a realizable angular law

The preceding obstruction suggests localizing all remaining geometry into the law of one scalar.

Let `V` be even, convex, positive away from the origin and positively `p`-homogeneous:

\[
V(rx)=r^pV(x),\qquad p\ge1.
\]

For `u in partial K`, put `v=V(u)` and `alpha=n/p`. Then

\[
q_u(t)
=\int_{-\infty}^t e^{ns-e^{ps}v}\,ds.
\]

With the substitution `z=e^{ps}v`, this becomes exactly

\[
\boxed{
q_v(t)=\frac1p v^{-\alpha}
\gamma\!\left(\alpha,e^{pt}v\right),
\qquad \alpha=\frac np,
}
\tag{5.1}
\]

where `gamma(alpha,z)=int_0^z y^{alpha-1}e^{-y}dy` is the lower incomplete gamma function.

Let

\[
\rho:=V_*\nu_K
\]

be the pushforward of cone measure on `partial K`. Then (3.3) collapses to the one-dimensional integral transform

\[
\boxed{
Q(t)=\frac{n|K|}{Zp}
\int_0^\infty v^{-n/p}
\gamma\!\left(\frac np,e^{pt}v\right)\rho(dv).
}
\tag{5.2}
\]

Thus the whole homogeneous subclass has only one angular datum: the scalar probability law `rho` of `V(U)` under cone direction `U`.

The B20 certificate proves that (5.2) is **not** log-concave for every abstract probability law `rho`, already for `n=p=3`. Therefore a homogeneous proof cannot be a pure total-positivity statement for the gamma kernel over arbitrary mixing measures. It must prove and exploit a nontrivial constraint on those `rho` which are actually representable as

\[
\rho=V_*\nu_K
\]

for a convex `p`-homogeneous `V` and a symmetric convex body `K`.

This is a materially smaller target than the original two-body/function problem: characterize enough of the realizable one-dimensional laws `rho` to force the variance–dissipation inequality (3.9), or construct a realizable law close enough to the exact violating relaxation (4.2) to disprove the conjecture.

I did **not** infer source failure from the relaxed two-atom calculation. Finite/discrete or abstract angular laws are not substituted for an actual convex measure/body pair.

**Outcome B30.** Successful localization. The homogeneous problem is reduced to a one-dimensional gamma-kernel transform plus a geometric realizability constraint on `rho`. The relaxed transform fails, so the realizability constraint is now the exact place where new geometry is required.

## 6. Before/after metric and the exact blocker now exposed

The source-relevant metric remains

\[
\boxed{D_B:2\to2.}
\]

No restricted class proved here changes the all-measures/all-bodies dimension threshold.

The most concentrated exact obstruction after this run is no longer the global covariance formula from run 11. It is:

\[
\boxed{
\operatorname{Var}_{w_t}(h_u(t))
\stackrel{?}{\le}
\mathbb E_{w_t}\kappa_u(t)
\quad\text{for every source-realizable angular family.}
}
\tag{6.1}
\]

Every ray separately has `kappa_u>=0`, but B20 proves that arbitrary mixtures of the exact homogeneous ray kernels can violate (6.1). Hence a proof must contain a genuinely geometric inequality coupling the directional profiles; raywise log-concavity alone is logically insufficient.

For the homogeneous subproblem, the same blocker is:

\[
\boxed{
\rho=V_*\nu_K\ \text{realizable by convex }(V,K)
\quad\Longrightarrow\quad
\text{the gamma transform (5.2) is log-concave.}
}
\tag{6.2}
\]

The two-atom relaxed law in (4.2) shows that “realizable” cannot simply be deleted.

## 7. Stuck accounting and mandatory next-run protocol

Run 10 admitted weak `(B)` with `D_B=2 -> 2`.

Run 11 again had `D_B=2 -> 2`.

This run again has `D_B=2 -> 2`.

Therefore this is the **third consecutive unchanged run** on the current hard target, and Section I now applies. I do not disguise the new structural lemmas as metric movement.

The **next invocation must be a thinking-only STUCK1 report** for this same target unless an external resolution/source collision is discovered first. It must contain the five required items: exact blocking statement, every route tried and precise failure, missing ingredient, simplest still-unproved source-valid special case, and nearest solved analogue/its extra mechanism; then it must choose exactly one permitted recovery action and name a fresh three-method triple. It must not simply append another lemma.

The natural candidate for that recovery analysis is to decide whether the geometric realizability constraint in (6.2) admits a quantitative anti-bimodality inequality strong enough to rule out the exact B20 relaxation, rather than continuing generic radial-score algebra.

## 8. Capability honesty

The automation interface available under the controlling policy exposes title, prompt, schedule, timing mode and enabled state, but no model selector, no reasoning-effort selector and no guaranteed execution duration. GPT-6 maximum therefore remains a prompt request only. This run actually identifies as **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**.

The repository policy records historical native modification probes for P26, P01 and P03 returning `You cannot modify this task`. No such task was modified in this run, because HARD7-01 is forbidden to modify other schedules. The non-bypass remedy remains to resolve authorized task/account/workspace ownership through the native interface or platform support; creating a duplicate job or editing the repository is not a scheduler repair.

No Gmail, Drive, public posting, workflow execution, force-push, shared-ledger rewrite or other-track file edit was performed.

## 9. Checkpoint / ledger delta

```yaml
ledger_delta:
  track: HARD7-01
  canonical_claim: B-WEAK-EVEN-LOGCONCAVE
  source_status: OPEN
  research_status: PARTIAL / STUCK1_TRIGGERED
  metric: D_B
  before: 2
  after: 2
  movement: none
  consecutive_no_movement_on_current_target: 3
  methods_this_run: [B11, B20, B30]
  exact_checker: artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T08-02-26Z__angular_two_atom_relaxation_check.py
  exact_output: artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T08-02-26Z__angular_two_atom_relaxation_check.out
  checker_result: ALL_EXACT_CHECKS_PASS = True
  next_required_action: Section-I thinking-only STUCK1 report; choose exactly one recovery action
  shared_RESULTS_edit: false
```
