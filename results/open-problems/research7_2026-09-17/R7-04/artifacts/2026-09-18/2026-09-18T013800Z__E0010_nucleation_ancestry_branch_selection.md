Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# E0010 — stationary nucleation, discrepancy ancestry, and the exact branch-selection/Palm gap

Target: Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 4, p. 11; arXiv:0906.2293.  For the source sexual-reproduction model with `beta>4.5`, show that sufficiently fast stirring gives a unique nontrivial stationary distribution.

Status of this note: **PARTIAL / source OPEN**.  It does not claim uniqueness.  It executes the recovery triple B19/B23/B28 selected in the preceding R7-04 stuck diagnosis.  Two statements below are proved completely (finite-cylinder nucleation and backward disagreement ancestry); the block-selection statement is explicitly conditional on the standard high-probability block implication used in the Durrett--Neuhauser fast-stirring proof.  The purpose is to isolate the remaining relative/Palm estimate without silently replacing it by an ordinary density estimate.

## 1. Recovered source input and cumulative blocker

The source process is an attractive spin system on the lattice.  Occupied sites die at rate one.  If a vacant site has `k` occupied sites among its `n` birth neighbors, it becomes occupied at rate

\[
\beta\frac{k(k-1)}{n(n-1)}.
\]

Nearest-neighbor stirring exchanges the two endpoint states at rate of order `epsilon^{-2}`.  The mean-field reaction term is

\[
f(u)=-u+\beta u^2(1-u).
\]

For `beta>4`, its two positive equilibria are

\[
\rho_- = \frac{1-\sqrt{1-4/\beta}}2,
\qquad
\rho_+ = \frac{1+\sqrt{1-4/\beta}}2.
\]

Durrett's Theorem 7 records the Durrett--Neuhauser result that the survival threshold tends to `4.5` as stirring becomes fast.  Its proof sketch uses the positive traveling-wave speed for `beta>4.5`, convergence to the reaction-diffusion PDE, and a one-pile-makes-two-piles block construction.  Problem 4 immediately asks for uniqueness of the nontrivial stationary law in the same regime.

The preceding R7-04 work reduced an ordered stationary coupling `eta<=xi` to a disagreement-Palm reproduction polynomial.  In the exactly color-exchangeable local model, if `a` is the common-one fraction and `d` is the disagreement fraction,

\[
\psi(a,d)=2a-3a^2+d(1-3a)-d^2.
\tag{1.1}
\]

A stationary disagreement needs normalized reproduction at least one, i.e. `beta psi >= 1`.  The stuck diagnosis showed that perfect local mixing alone is not enough because

\[
\psi(\rho_-,0)-\frac1\beta
=\rho_-(1-2\rho_-)>0,
\]

while the stable high branch has the opposite sign.  The missing information is therefore branch selection under the **disagreement Palm law**, not another unconditional stirring estimate.

## 2. B19 — a constructive stationary nucleation theorem

The first new point is that every nontrivial stationary law has positive mass on every finite all-one cylinder.  No translation invariance is assumed.

### Theorem 2.1 (finite-cylinder nucleation)

Let `mu` be any stationary probability law for the source process such that

\[
\mu(\{\mathbf 0\})=0,
\]

where `mathbf 0` is the all-vacant absorbing state.  Then for every finite set `Lambda` of lattice sites,

\[
\boxed{\mu\{\eta:\eta(x)=1\ \forall x\in\Lambda\}>0.}
\tag{2.1}
\]

This uses only positive death rates, positive stirring rates on a connected lattice, and the source fact that every legal ordered two-parent birth clock has positive rate.

#### Proof, step 1: a nontrivial stationary law has no finite-particle mass

For a configuration `eta`, let

\[
N(\eta)=\sum_x\eta(x)\in\{0,1,2,\ldots,\infty\}.
\]

Fix `t>0`.  If `N(eta)=m<infty`, then

\[
P_\eta(\eta_t=\mathbf0)>0.
\tag{2.2}
\]

Indeed, the initially occupied set is finite.  Suppress for time `t` all stirring marks incident to those sites and all birth arrows whose target can be activated by two of those finitely many particles; only finitely many Poisson clocks are involved because the interaction range is finite.  Require in addition that all `m` death clocks ring before time `t`.  This event has strictly positive probability and on it no new particle is born and every old particle dies.

If `mu(N<infty)>0`, (2.2) is a strictly positive measurable function on a set of positive `mu`-mass, so

\[
P_\mu(\eta_t=\mathbf0)
=\int P_\eta(\eta_t=\mathbf0)\,\mu(d\eta)>0.
\]

Stationarity would give `mu({mathbf0})>0`, contradiction.  Hence

\[
\boxed{\mu(N=\infty)=1.}
\tag{2.3}
\]

In particular, since the lattice is countable,

\[
\{N\ge2\}=\bigcup_{x\ne y}\{\eta(x)=\eta(y)=1\},
\]

so there exist fixed sites `x!=y` for which

\[
\mu(\eta(x)=\eta(y)=1)>0.
\tag{2.4}
\]

#### Proof, step 2: finite controllability from two particles

Fix the target `Lambda`.  Choose a large finite connected buffer `V` containing `x`, `y`, `Lambda`, all paths used below, and enough extra vacant sites for finitely many births.  Partition the positive-probability event in (2.4) according to the finitely many configurations on `V`.  At least one cylinder

\[
E_\sigma=\{\eta|_V=\sigma\},
\qquad \sigma(x)=\sigma(y)=1,
\tag{2.5}
\]

has positive `mu`-mass.

Starting from this fixed finite pattern `sigma`, there is a finite legal control word consisting only of stirring transpositions and two-parent births that ends with every site of `Lambda` occupied.  To see this, use connectivity of the stirring graph to move two occupied sites to any prescribed legal pair of parents around a vacant target and fire the corresponding birth arrow, increasing the number of particles by one.  Repeat until at least `|Lambda|` particles are available, enlarging the finite buffer beforehand if needed.  Nearest-neighbor transpositions on a finite connected graph generate every permutation of the occupation pattern, so at the end move `|Lambda|` occupied sites onto `Lambda`.  If `sigma` is already full on `Lambda`, the word may be empty.

#### Proof, step 3: realize the control word with positive graphical probability

In a finite time interval `[0,T]`, require the prescribed finite sequence of stirring and birth marks in disjoint small time windows, suppress all deaths of particles needed by the word, and suppress all competing marks in a finite interaction collar around `V`, including boundary-crossing stirring marks.  Every prescribed clock has positive rate and only finitely many clocks are constrained.  Therefore the graphical event has probability `c_sigma>0`.  On `E_sigma` and this event, the state at time `T` is one on every site of `Lambda`, regardless of the configuration outside the protected collar.  Consequently

\[
P_\mu(\eta_T\equiv1\text{ on }\Lambda)
\ge \mu(E_\sigma)c_\sigma>0.
\]

Stationarity makes the left side equal to `mu(eta equiv1 on Lambda)`, proving (2.1).  QED.

### What Theorem 2.1 does and does not give

It gives a genuine nucleation seed in **every** nontrivial stationary law, even a spatially non-translation-invariant one.  The probability may, however, depend arbitrarily badly on `Lambda`, its location, `beta`, `epsilon`, and `mu`.  There is no uniform lower bound.  That distinction is essential later.

## 3. B23 — stable-branch algebra and the quantitative Palm obstruction

The next step is to make the stable branch margin explicit.

Define the larger root of the ideal disagreement threshold

\[
a_*(\beta)
=\frac{1+\sqrt{1-3/\beta}}3,
\qquad
2a_*-3a_*^2=\frac1\beta.
\tag{3.1}
\]

For `beta>4.5`,

\[
\rho_+>\frac23,
\qquad
a_*(\beta)<\frac23,
\tag{3.2}
\]

because `rho_+=2/3` at `beta=4.5` and increases with `beta`, whereas the square root in (3.1) is strictly less than one.  Hence there is a fixed branch-selection gap

\[
\Delta_\beta:=\rho_+-a_*(\beta)>0.
\tag{3.3}
\]

Take, for example,

\[
\theta_\beta:=\frac{\rho_++a_*}2.
\tag{3.4}
\]

Then `theta_beta>a_*>1/3`.  Since

\[
g(a)=2a-3a^2
\]

is strictly decreasing for `a>1/3`,

\[
\kappa_\beta
:=1-\beta g(\theta_\beta)>0.
\tag{3.5}
\]

There is a useful strengthening: once the common-one fraction satisfies `a>=theta_beta`, the disagreement fraction cannot spoil the margin.  Indeed `theta_beta>1/2` for `beta>4.5`, hence `1-3a<0`, and for every `d>=0`,

\[
\psi(a,d)
=g(a)+d(1-3a)-d^2
\le g(a)
\le g(\theta_\beta).
\]

Therefore

\[
\boxed{a\ge\theta_\beta\Longrightarrow
\beta\psi(a,d)\le1-\kappa_\beta
\quad\text{for every admissible }d.}
\tag{3.6}
\]

So a stable-branch block supplies a **uniform strict disagreement contraction margin**, not merely a perturbative one valid when disagreements are sparse.

### Lemma 3.1 (the bad-Palm mass required by any ideal persistent disagreement)

On the admissible triangle `a>=0`, `d>=0`, `a+d<=1`,

\[
\boxed{\psi(a,d)\le\frac13.}
\tag{3.7}
\]

Proof.  For fixed `a`, the polynomial is concave in `d`.  If `a>=1/3`, its derivative at `d=0` is `1-3a<=0`, so its maximum over `d>=0` occurs at `d=0` and is `g(a)<=1/3`.  If `a<1/3`, the unconstrained maximum occurs at `d=(1-3a)/2`, giving

\[
\psi_{\max}(a)=\frac{1+2a-3a^2}{4},
\]

which increases on `[0,1/3]` and equals `1/3` at `a=1/3`.  QED.

Suppose now that the ideal color-exchangeable Palm closure were exact and that a nonzero stationary discrepancy existed.  Write

\[
p_{\rm bad}
=P^{D}(a<\theta_\beta),
\]

where `P^D` is discrepancy Palm probability.  On the good event, (3.6) gives normalized reproduction at most `1-kappa_beta`; everywhere, (3.7) gives normalized reproduction at most `beta/3`.  Stationarity would force mean reproduction at least one, so

\[
1\le(1-p_{\rm bad})(1-\kappa_\beta)
+p_{\rm bad}\frac\beta3.
\]

Thus

\[
\boxed{
p_{\rm bad}\ge
c_\beta:="frac{\kappa_\beta}{\beta/3-1+\kappa_\beta}"
>0.
}
\tag{3.8}
\]

Here the displayed string in quotes is to be read as the fraction
`kappa_beta/(beta/3-1+kappa_beta)`; it is positive because `beta>4.5`.

Equation (3.8) is the quantitative form of the branch-selection blocker: a persistent disagreement cannot merely visit the low branch occasionally.  It must spend a fixed positive fraction of its **Palm** mass in low-common-one environments.

With the already proved relative stirring error restored, (3.8) is stable: any error smaller than, say, `kappa_beta/4` only changes `c_beta` by a fixed beta-dependent factor.  No `1/Q` loss is needed at this stage.

## 4. B28 — what ordinary branch selection can prove

The source block construction is precisely suited to selecting the stable high phase for ordinary configurations.  The distinction is that it selects the phase under the unconditioned law, whereas (3.8) requires selection under discrepancy Palm conditioning.

### Proposition 4.1 (translation-ergodic ordinary branch selection; block-construction reduction)

Assume the standard Durrett--Neuhauser one-pile-makes-two-piles estimate in the following form.  For every sufficiently small target error `delta>0`, for all sufficiently fast stirring there are macroscopic block parameters `(L,T)` and a local mature event `H` such that:

1. `H` implies empirical particle density at least `theta_beta` in the central block;
2. a fully occupied seed block can initiate `H`;
3. from an `H` block, the prescribed forward child blocks are `H` with conditional probability at least `1-delta`, with finite dependence, so the `H` process dominates supercritical oriented percolation with parameter tending to one as `delta->0`.

Let `mu` be a translation-ergodic nontrivial stationary law.  By Theorem 2.1, a fixed finite full seed has positive `mu` probability.  Translation ergodicity gives positive spatial density of such seeds (using all translates; a finite-color thinning places a positive-density subcollection on the coarse block lattice).  Future graphical marks are independent of the time-zero state.  Standard complete convergence for supercritical oriented percolation started from a stationary ergodic positive-density set then implies that the dominated mature-block process has one-site occupation probability approaching its upper invariant density.  Since that upper density tends to one as the oriented-percolation parameter tends to one, stationarity of `mu` yields

\[
\mu(H_0)\ge 1-o_\delta(1).
\tag{4.1}
\]

In particular, the ordinary empirical density of a translation-ergodic positive stationary phase is selected into the stable basin and cannot remain near `rho_-`.

This is a reduction, not a novelty claim.  Chris Noble's 1992 paper *Equilibrium Behavior of the Sexual Reproduction Process with Rapid Diffusion* already states in its abstract that the equilibrium density is determined for all noncritical reaction rates using a renormalized bond construction and hydrodynamic limits.  The present use of (4.1) should therefore be treated as recovered/adjacent methodology until exact theorem scope is checked, not as a new literature claim.

### Why this still does not prove Problem 4

Let `D_0=xi_0-eta_0` under a stationary ordered coupling and let

\[
Q=P(D_0=1)>0.
\]

For a bad-block event `B`, an ordinary estimate gives only

\[
P(B)\le\delta.
\]

But the discrepancy Palm probability is

\[
\boxed{
P^D(B)=\frac{P(D_0=1,B)}Q\le\frac\delta Q.
}
\tag{4.2}
\]

When uniqueness is nearly true, `Q` is precisely the quantity that may be arbitrarily small.  Thus (4.2) is useless.  Combining (3.8) with an ordinary bad-block estimate yields at best

\[
Q\le\frac\delta{c_\beta},
\tag{4.3}
\]

which is asymptotic smallness, not the exact identity `Q=0` required by the source.

This is the exact gluing failure between branch selection and the preceding relative-stirring theorem.

## 5. A second complete theorem: every discrepancy has a backward disagreement ancestry

The graphical coupling gives a route to attack the relative estimate directly rather than through Bayes' inequality.

### Theorem 5.1 (backward discrepancy ancestry)

Consider the basic monotone coupling `eta_t<=xi_t`.  If

\[
D_t(x)=\xi_t(x)-\eta_t(x)=1,
\]

then for every earlier time `s<t` there is a backwards graphical path from `(x,t)` to some `(y,s)` such that, along the path, the currently followed site is a disagreement immediately before each jump/event.  At a birth-created disagreement one may choose at least one parent that was already a disagreement just before the birth.

Consequently, in a two-sided stationary ordered coupling, under the Palm law conditioned on `D_0(0)=1`, there is an infinite backward discrepancy ancestry reaching every time `-T`, `T>0`.

#### Proof

Trace the most recent graphical event affecting the currently followed site backwards.

- **Stirring.**  A common stirring mark swaps the two coupled configurations at the same edge.  If the endpoint followed after the swap is a disagreement, the opposite endpoint immediately before the swap was a disagreement.  Follow it backwards.
- **Death.**  A common death mark maps both endpoint states to zero whenever occupied.  It cannot create a disagreement.  Therefore a present disagreement cannot have its backward lineage start at a death mark; if the last event is a death, the disagreement must have been elsewhere and transported later, already handled by stirring.
- **Birth.**  A discrepancy can be created at a target `x` only when the upper process accepts a two-parent birth and the lower process does not.  Since the lower configuration is coordinatewise below the upper one, at least one of the two upper occupied parents used by that birth is absent in the lower configuration.  That parent is a disagreement immediately before the birth.  Choose one such parent and continue backwards.
- **No event.**  Between graphical marks the disagreement simply persists at the same site.

The graphical process is locally finite on every bounded time interval, so this recursive tracing reaches any prescribed earlier time unless it terminates.  None of the event types can create a disagreement from a past with no disagreement ancestor, so termination before `s` is impossible.  In a two-sided stationary construction, repeat for every integer `T` and take a diagonal/Konig-lemma choice of compatible finite ancestors to obtain an infinite backward path.  QED.

### Corollary 5.2 (the missing estimate is a bad-corridor estimate)

Any nonzero stationary disagreement must support an infinite backwards spacetime path that continually finds environments in which disagreement reproduction is not killed.  By (3.6), after relative stirring has made the tagged local color law close to its mixed form, a macroscopic region whose common-one fraction is at least `theta_beta` is strictly hostile to such a path.

Therefore a source-level uniqueness proof can be completed by a **relative bad-corridor theorem** of the following type:

> There exist block scales and `lambda<1` such that, uniformly over every stationary ordered coupling with `Q>0` and every approximate-maximal disagreement site, the discrepancy-Palm probability that its backward ancestry can traverse `m` consecutive low-common-one/bad blocks is at most `C lambda^m`.

Theorem 5.1 then says a present discrepancy would need such corridors for all `m`, a probability tending to zero.  This would force `Q=0`.

This criterion is stronger than the ordinary assertion `P(block bad)<=delta`: it is already normalized by the existence of a disagreement and is therefore immune to the `delta/Q` blow-up in (4.2).

## 6. What B19/B23/B28 achieved in this run

### B19 — make it an algorithm

The finite control word in Theorem 2.1 is explicit: locate a positive-probability occupied pair, use stirring transpositions to place it around a legal target, fire a birth, repeat until enough particles exist, then permute them onto the desired seed block.  This converts the qualitative phrase “a nontrivial stationary phase must nucleate” into a rigorous finite graphical event.  It works without spatial translation invariance.

### B23 — assume the opposite

Assuming a persistent low stationary branch exposes two different notions of “low.”  An **ordinary** translation-ergodic low phase is incompatible with the positive-wave-speed block mechanism once a seed is present.  But a **disagreement-Palm** low environment can still occur by concentrating the rare disagreement on rare low-density spacetime islands.  Equation (3.8) shows such concentration must have a fixed positive Palm mass.

### B28 — prove the typical statement first, then identify the lift

The translation-ergodic ordinary branch can be pushed into the stable basin by the source block construction.  The lift to the source's arbitrary stationary laws is not a matter of ergodic decomposition alone: even for an ordinary high phase, Palm conditioning can select rare bad regions according to (4.2).  The correct lift is genealogical, through Theorem 5.1 and a relative bad-corridor estimate.

## 7. Current mathematical status and frozen metric

The source-matching metric remains

\[
Q_{SR}(\beta,\varepsilon)
=\sup_{\mu\in\mathcal I^{nt}_{\beta,\varepsilon}}
\bigl[\bar\nu_{\beta,\varepsilon}(\eta(0))
      -\mu(\eta(0))\bigr].
\]

This run proves new structural lemmas but does not establish an exact positive baseline or `Q_SR=0`.  Therefore

\[
\boxed{Q_{SR}:\;UNKNOWN/UNMEASURED\to UNKNOWN/UNMEASURED.}
\]

There is **no metric movement**.

The ordinary unchanged-run count was 3 before this recovery iteration (the immediately preceding stuck diagnosis deliberately did not increment it), so after this ordinary run it becomes 4.

## 8. Dated source and prior-art check — 2026-09-18

- Primary source: Rick Durrett, *Coexistence in stochastic spatial models*, arXiv:0906.2293 / Ann. Appl. Probab. 19 (2009), Problem 4.  The source explicitly asks for uniqueness for `beta>4.5` and sufficiently fast stirring.
- Chris Noble, *Equilibrium Behavior of the Sexual Reproduction Process with Rapid Diffusion*, Ann. Probab. 20 (1992), 724--745, DOI 10.1214/aop/1176989802.  Its abstract says that the equilibrium density is determined for all noncritical reaction rates using a renormalized bond construction and hydrodynamic limits.  This is relevant prior methodology for ordinary branch selection, not evidence that Problem 4's full uniqueness statement is solved.
- Durrett--Neuhauser, *Particle systems and reaction-diffusion equations*, Ann. Probab. 22 (1994), 289--333, DOI 10.1214/aop/1176988861, supplies the fast-stirring/PDE phase-transition framework cited by the source.
- Rick Durrett, *Discontinuous phase transitions in the one-dimensional pair and triplet creation processes*, arXiv:2608.29878 (submitted 2026-08-30), concerns different one-dimensional pair/triplet creation models and does not state the E0010 uniqueness theorem.
- A bounded fresh search on 2026-09-18 did not recover a later explicit resolution of Durrett Problem 4.  This is negative evidence only; it is not a novelty or openness certificate.

## 9. Next attack

The next useful step is not another unconditional density estimate.  It is to turn the ancestry theorem into a **relative moving-path branch-selection estimate**.  A suitable next triple, distinct from B19/B23/B28, is:

1. **B30 — localize and identify gluing failure:** coarse-grain an actual backward discrepancy ancestry and prove exactly which block interfaces allow it to jump from a high lower phase into a low island.
2. **B27 — swap the quantifiers:** condition first on a realized ancestry skeleton and only then expose the lower-process/block graphical marks; seek a uniform exponential bound for all skeletons instead of conditioning the environment on the final discrepancy.
3. **B21 — import an analogous technique:** adapt disagreement-percolation / branching-random-walk-in-a-random-environment path counting so the estimate is relative to `Q` from the start.

If that produces a `C lambda^m` corridor bound with `lambda<1`, Theorem 5.1 converts it directly to source-level uniqueness.  If it only gives an ordinary `P(B)<=delta` estimate, (4.2) shows exactly why the route has not advanced the frozen metric.
