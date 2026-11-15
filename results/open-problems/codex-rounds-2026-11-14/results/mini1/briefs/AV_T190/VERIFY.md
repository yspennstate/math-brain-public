# T190: verification of the three OpenAI candidates

Checked 14 November 2026. Verdict: NOT-THIS for each candidate. This is a comparison of claims, not an assessment of the correctness of the three proofs.

## The statement being checked

The row asks for statistically stationary martingale solutions of incompressible Navier–Stokes on the flat three-torus, with additive Gaussian forcing that is white in time and smooth in space, a fixed energy input ε, and

\[
\lim_{\nu\downarrow0}\nu\,\mathbb E\|u^\nu\|_{L^2(\mathbb T^3)}^2=0.
\]

The proposed non-degeneracy hypothesis is a suitable Hörmander bracket condition. This is an asymptotic assertion about stationary probability laws for a family of stochastic equations. The quantity in this limit is kinetic energy multiplied by viscosity; it is not the instantaneous viscous dissipation \(\nu\|\nabla u\|_2^2\).

For the reference model, the PDF of [*A sufficient condition for the Kolmogorov 4/5 law for stationary martingale solutions to the 3D Navier-Stokes equations*](https://arxiv.org/pdf/1803.09695), by **Jacob Bedrossian, Michele Coti Zelati, Samuel Punshon-Smith, and Franziska Weber**, was opened. Its introduction specifies Gaussian white-in-time forcing, fixed noise coefficients and energy input independent of viscosity; Definition 1.1 gives WAD. It assumes WAD to obtain the averaged 4/5 law rather than establishing WAD.

## 1. Universal Computation with Eventually Stationary Navier–Stokes Forcing

Author: **OpenAI**. Date on manuscript: **September 27, 2026**. Opened the [original TeX source](https://github.com/openai/math/blob/main/preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/build/main.tex) and manuscript README; exact local copy: [sources/stationary.tex](sources/stationary.tex). The main theorem begins at source line 146. The quotation below copies the complete theorem environment, including its final uniformity assertion.

```tex
\begin{theorem}[Eventually steady forcing]\label{thm:main}
Fix a positive computable viscosity $\nu$.  There is an effective
procedure taking a deterministic Turing machine and finite input to
a body force $f$ on the flat torus $\mathbb T^3$, such that:
\begin{enumerate}
\item $f$ is smooth on $\mathbb T^3\times[0,\infty)$, has zero
spatial mean, and is independent of time for $t\ge1$.  Every spatial,
temporal, and mixed derivative of $f$ is bounded on this entire domain.
\item With initial velocity zero, the Navier--Stokes equation has a
global smooth solution, unique in the classical class on every finite
time interval.  Its kinetic energy is bounded uniformly in time.
\item For the fixed particle label and fixed open set
\[
 P=(1/4,1/4,0),\qquad
 \mathcal O=\{(X,Y,Z)\in\mathbb T^3:1/32<Y<1/8\},
\]
the material trajectory from $P$ enters $\mathcal O$ at a finite
time if and only if the machine halts on the input.
\end{enumerate}
The force is specified by a finite formula which does not simulate the
chosen execution.  The construction is also uniform as a formula in
an arbitrary positive parameter $\nu$.
\end{theorem}
```

The equation immediately before this theorem is deterministic:
\(u_t+(u\cdot\nabla)u=-\nabla p+\nu\Delta u+f\), \(\nabla\cdot u=0\), \(u(0)=0\). Here \(f\) is an effectively specified smooth function of space and time designed from a machine and its input.

**Comparison.** The incompressible equation, dimension three and flat domain \(\mathbb T^3\) agree with the row. The forcing does not: a smooth deterministic body force, eventually constant in time, is not Gaussian white noise. “Eventually stationary” means \(f(t,x)=f(1,x)\) for \(t\ge1\); the theorem does not assert an invariant probability law for the velocity. The solution starts from rest and evolves during startup and computation.

The observed quantity is a particle entering a strip, equivalent to machine halting. Uniform boundedness of kinetic energy *in time* for the constructed instance does not establish the row's expectation limit for stationary stochastic solutions *as viscosity tends to zero*. The theorem does state uniformity of its formula in a positive viscosity parameter, so it would be inaccurate to say it has no viscosity-parametrized construction. However, the force may vary with that parameter through the residual \(f_\nu=U_t+(U\cdot\nabla)U-\nu\Delta U\); this is not the fixed stochastic forcing law of the row. No energy input ε or Hörmander condition occurs in the theorem. Verdict: **NOT-THIS**.

## 2. Velocity-Field Detection of Computation in Forced Navier–Stokes Flows

Author: **OpenAI**. Date: **September 27, 2026**. Opened the [original TeX source](https://github.com/openai/math/blob/main/preprints/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/build/main.tex) and its included compact and bounded construction sections; local copies: [sources/velocity.tex](sources/velocity.tex), [sources/velocity-compact.tex](sources/velocity-compact.tex), [sources/velocity-bounded.tex](sources/velocity-bounded.tex).

The main theorem refers to two observations defined immediately before it. Their exact source definitions are:

```tex
\begin{equation}\label{eq:torus-event}
 \exists t\ge0\ \exists (x,y,z),\quad
 1/32<y<1/8,\qquad u_3(t,x,y,z)>\tfrac12.
\end{equation}
```

```tex
\begin{equation}\label{eq:plane-event}
 \exists t\ge0,\qquad
 \int_{\{X_2>0\}\times\T}u_3(t,X,z)\dd X\dd z>\tfrac12.
\end{equation}
```

The complete main theorem begins at source line 98:

```tex
\begin{theorem}\label{thm:main}
For each positive computable $\nu$, a machine and a finite input
effectively determine each of the following two forces.
\begin{enumerate}
\item On $\T^3$, a smooth force has a unique global smooth solution
in the torus class above, with pressure zero, for which
\eqref{eq:torus-event} holds exactly when the machine halts.
The force is supported in $K\times\T$ for a compact
$K\subset(0,1)^2$ independent of time. Its derivatives are bounded on every finite time
interval; their bounds may grow with that interval.
\item On $\R^2\times\T$, a smooth force and all its mixed derivatives
are globally bounded. On each finite time interval its horizontal
support is compact. It has a unique global smooth solution in
\eqref{eq:comparison-class}, with pressure zero and integrable
nonnegative third component. Event~\eqref{eq:plane-event} holds exactly
when the machine halts.
\end{enumerate}
The sets and thresholds in both observations are independent of the
machine and input. The compact set $K$ in the first construction may
depend on that instance, but is independent of time. Both force prescriptions install all the required
local instructions, without executing the selected computation.
\end{theorem}
```

For the noncompact comparison class, equation \(\eqref{eq:comparison-class}\) in the quotation requires, on each finite interval, \(u\in C_tH_x^2\cap C_t^1L_x^2\), \(p\in C_tH_x^1\), and bounded \(|u|+|\nabla u|\), in addition to classical regularity. The source defines these classes before the theorem.

**Comparison.** The first branch has the correct domain and dimension; the second has dimension three but the different, noncompact domain \(\mathbb R^2\times\mathbb T\). Both branches use a designed deterministic body force and zero initial velocity. Neither asserts stationary martingale solutions, Gaussian forcing, fixed ε, a Hörmander hypothesis or the WAD expectation limit.

The first observation is a pointwise threshold for a single velocity component somewhere in a strip, not an expected spatial kinetic energy. The second is a half-space integral of that component, not its squared \(L^2\) norm. Bounded derivatives of forcing on finite intervals in the torus construction, or globally in the cylindrical construction, do not supply a viscosity asymptotic. The text following the theorem explicitly allows growing derivative bounds in the torus case and does not claim uniformly bounded total kinetic energy on the cylinder. Its vertical advection–diffusion equation is part of an Eulerian computation detector, not a stochastic anomalous-dissipation theorem. Verdict: **NOT-THIS**.

## 3. Computation under Rapidly Vanishing Navier–Stokes Forcing

Author: **OpenAI**. Date: **September 27, 2026**. Opened [main.tex](https://github.com/openai/math/blob/main/preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/build/main.tex) and every included construction section. The main results occur in those included files, so quoting only main.tex would miss them. The complete statements are copied here, including the torus specialization directly relevant to the domain comparison.

### Compact moving curls: main theorem

Source: [addressed.tex](https://github.com/openai/math/blob/main/preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/build/addressed.tex), line 11; local [sources/vanishing-addressed.tex](sources/vanishing-addressed.tex).

```tex
\begin{theorem}[Compact support and rapid decay]
\label{thm:rapid}
Fix a positive computable viscosity $\nu$. From a deterministic Turing machine $M$ and a
finite input $w$ one can effectively construct a smooth force on
$[0,\infty)\times\R^3$, supported for all times in the fixed compact set
\[
 K=[-2,1]\times[-1,2]\times[-1,1],
\]
such that, for every pair of nonnegative integers $J,l$ and spatial
multi-index $\alpha$,
\begin{equation}
 \sup_{t\geq0,\,x\in\R^3}
 (1+t)^J\bigl|\partial_t^l\partial_x^\alpha f(t,x)\bigr|<\infty.
 \label{eq:rapid-force-bound}
\end{equation}
The Navier--Stokes equation with this force and zero initial velocity has
an explicit global smooth solution, unique in the finite-interval class \eqref{eq:energy-class}.  Its material trajectory from
the origin satisfies
\begin{equation}
 M\text{ halts on }w
 \quad\Longleftrightarrow\quad
 X_1(t,0)<-1\text{ for some }t\geq0.
 \label{eq:rapid-event}
\end{equation}
The velocity has the same fixed support and rapid mixed-derivative bounds.
The pressure is zero. The force is a general body force. Because $K$ is fixed,
the same bounds hold with $(1+t+|x|)^J$ in place of $(1+t)^J$.
\end{theorem}
```

### Torus specialization of the compact construction

Same source, line 337:

```tex
\begin{corollary}[Solenoidal rapid forcing on the torus]
\label{cor:rapid-torus}
Fix a positive computable viscosity.  From any deterministic Turing
machine $M$ and finite input $w$, one can effectively construct on the
unit flat torus $\T^3$ a smooth, solenoidal, spatially mean-zero
force satisfying all the bounds \eqref{eq:rapid-force-bound} with $\T^3$
in place of $\R^3$, with zero
initial velocity, such that the unique smooth solution satisfies
\[
 M\text{ halts on }w
 \quad\Longleftrightarrow\quad
 \frac14<X_1(t,a_*)<\frac38\text{ for some }t\geq0,
 \qquad a_*=(1/2,1/4,1/2).
\]
Here the inequality denotes the indicated open coordinate slab of the
torus. Pressure is normalized to mean zero, and uniqueness holds in the
classical periodic class of Section~\ref{sec:analytic}.  The velocity and all its mixed derivatives also decrease faster
than every inverse power of time.
\end{corollary}
```

### Alternating memories: main theorem

Source: [alternating.tex](https://github.com/openai/math/blob/main/preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/build/alternating.tex), line 11; local [sources/vanishing-alternating.tex](sources/vanishing-alternating.tex).

```tex
\begin{theorem}[Rapid decay with alternating memories]
\label{thm:alternating}
Fix a positive computable viscosity. From a deterministic Turing machine
and a finite input one can effectively
construct a smooth force $f$ on $[0,\infty)\times\mathbb R^3$, with
spatial support contained in a fixed compact set independent of time,
such that for every $J,l\geq0$ and spatial multi-index $\alpha$,
\begin{equation}
 \sup_{t\geq0,\,X\in\mathbb R^3}
 (1+t+|X|)^J
 |\partial_t^l\partial_X^\alpha f(t,X)|<\infty.
 \label{eq:alternating-schwartz}
\end{equation}
The solution with zero initial velocity is explicit, global, and unique
in the class \eqref{eq:energy-class}, with pressure zero.  Its velocity satisfies
the same support and derivative estimates.  The material particle
initially at $(-1,0,0)$ reaches $X_1>0$ if and only if the machine halts.
\end{theorem}
```

### Periodic lattice memory: main theorem

Source: [lattice.tex](https://github.com/openai/math/blob/main/preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/build/lattice.tex), line 18; local [sources/vanishing-lattice.tex](sources/vanishing-lattice.tex).

```tex
\begin{theorem}[Periodic lattice memory]\label{thm:lattice}
Fix a computable viscosity $\nu>0$.  A finite deterministic machine and
a finite input effectively determine a smooth force $g$ on the unit
flat torus $\T^3=(\R/\mathbb Z)^3$ with zero spatial mean.  The
Navier--Stokes equations with force $g$ and zero initial velocity have
a smooth solution $(U,0)$ with zero spatial mean.  Its particle from
\[
 a_*=(1/4,1/2,1/2)
\]
enters the fixed open set
\[
 O=\{x\in\T^3:1/2<x_1<1\pmod 1\}
\]
at some finite time if and only if the machine halts on that input.
For every pair of nonnegative integers $r,J$ and every spatial
multi-index $\alpha$, there is an effective constant $C_{r,\alpha,J}$
such that
\begin{equation}\label{eq:lattice-rapid}
 \|\partial_t^r\partial_x^\alpha U(t)\|_\infty
 +\|\partial_t^r\partial_x^\alpha g(t)\|_\infty
 \le C_{r,\alpha,J}(1+t)^{-J},\qquad t\ge0.
\end{equation}
There is also an effective smooth mean-zero solenoidal force $f$
with the same bounds and exactly the same velocity and material event.
It is $f=g-\nabla\phi$, with pressure $-\phi$, where $\phi$ is the
mean-zero periodic solution of $\Delta\phi=\operatorname{div}g$.

For either force, uniqueness holds among periodic classical solutions
for which the velocity, its time derivative and its spatial derivatives
through order two, and the pressure and its spatial gradient, are
continuous on every $[0,T]\times\T^3$.  Pressure is normalized to have
zero spatial mean.
\end{theorem}
```

In these statements, the noncompact energy class is \(u\in C_tH_x^2\cap C_t^1L_x^2\), \(p\in C_tH_x^1\), with bounded velocity and gradient on each finite interval, as defined in Section 2 of main.tex. All four experiments start with zero velocity.

**Comparison.** The compact and alternating constructions are in \(\mathbb R^3\); the corollary and lattice construction are on the correct flat \(\mathbb T^3\). The forcing remains deterministic in every case. Solenoidal and spatially mean-zero forcing is not the same condition as non-degenerate Gaussian forcing or a Hörmander bracket condition.

“Rapidly vanishing” means \(t\to\infty\), at each fixed positive viscosity. Its bounds quantify decay of every fixed derivative of the prescribed force and velocity in time. The row asks about \(\nu\to0\), with a fixed nonzero stochastic energy input. A decaying deterministic field starting at rest supplies no statistically stationary stochastic law. The source even writes its residual as \(f^{(0)}+\nu f^{(1)}\), with coefficient fields effective independently of viscosity: this parameter dependence does not turn it into a viscosity-independent Gaussian forcing law. The target observation is again particle reachability equivalent to halting. No theorem here claims any part of stochastic WAD. Verdict: **NOT-THIS**.

## Clause-by-clause comparison with the row

| Clause of our statement | Eventually Stationary | Velocity-Field Detection | Rapidly Vanishing |
|---|---|---|---|
| Incompressible Navier–Stokes | Yes | Yes | Yes |
| Three dimensions | Yes | Yes | Yes |
| Flat \(\mathbb T^3\) | Yes | First branch only; second is \(\mathbb R^2\times\mathbb T\) | Torus corollary and lattice theorem; other main constructions are on \(\mathbb R^3\) |
| Additive Gaussian, white-in-time, spatially smooth forcing | No: designed smooth deterministic force | No: designed smooth deterministic force | No: designed smooth deterministic force |
| Fixed stochastic energy input ε across viscosities | Not asserted | Not asserted | Not asserted |
| Statistically stationary martingale solutions | Not asserted; eventual constancy refers to the force | Not asserted | Not asserted; velocity decays in time |
| \(\nu\,\mathbb E\|u^\nu\|_2^2\to0\) | Not asserted | Not asserted | Not asserted |
| Suitable Hörmander bracket condition | Not present | Not present | Not present |
| Actual conclusion | Particle halting detector with eventually steady force | Pointwise/integral velocity halting detector | Particle halting detectors with rapid decay in time |

A deterministic force can formally be placed on a one-point probability space, but that does not create non-degenerate white noise or supply the required stationary solutions. Changing a prescribed velocity into a solution by choosing its residual force is not an existence theorem under the row's fixed noise covariance.

## Follow-ups and what was opened

Searches used the web tool on 14 November 2026: each exact title, each title with arXiv/error/gap/referee/review terms, each exact title restricted to arxiv.org, and searches for stochastic Navier–Stokes WAD with Hörmander and 2025–2026 terms. No matching arXiv version of the three manuscripts, specific mathematical refutation, or referee report was found in those searches. That is a search result, not an assertion that none exists. The following relevant material was actually opened.

1. **Repository notices and revisions.** Opened [OpenAI's README](https://raw.githubusercontent.com/openai/math/main/README.md), [history.md](https://github.com/openai/math/blob/main/history.md), [CONTENTS.md](https://github.com/openai/math/blob/main/CONTENTS.md), all three manuscript READMEs, [lean/README.md](https://github.com/openai/math/blob/main/lean/README.md), and [lean/formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml). The checked history records an October 7 correction to the companion *Incompressible Box Transport and Finite Computation*, specifically its torus-projection and common-clock estimates; it lists no withdrawal of these three candidates. This companion notice is not an error report on the stochastic WAD question. The manuscript READMEs identify OpenAI as author and September 27 as date.

2. **ArXiv exposition.** Opened both the [arXiv page](https://arxiv.org/abs/2610.17090) and [full HTML, Section 9.4.8](https://arxiv.org/html/2610.17090v1#S9.SS4.SSS8) of **Ying Xie**, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*, submitted **12 October 2026**. It discusses these papers as family 376, describes fixed-viscosity computation, and distinguishes extracted mechanisms from certification. It is an exposition/survey, not an arXiv version of a candidate and not a referee acceptance. Its discussion of antecedents does not establish or claim stochastic WAD.

3. **Other expositions.** Opened [*Exact computation with eventually stationary forcing*](https://openmaths.org/courses/NS-BLOWUP/audits/eventually-stationary-computation-audit.html), credited on the page to **GPT-6 Astra (OpenAI)**, and [Latent Seminar, *Universal computation in smooth forced Navier–Stokes flows*](https://lowrank.github.io/latent-seminar/OpenAI-Math/376-forced-fluid-computation). They explain deterministic forcing and the separate clock constructions. The former is expressly AI-generated; neither is treated as an independent referee report.

4. **Actual critical comment.** Opened **Warren D. Smith's 7 October 2026 forum post**, signed by him, in [*First look at mathematics manuscripts from an internal frontier model at OpenAI*, post 6](https://community.openai.com/t/first-look-at-mathematics-manuscripts-from-an-internal-frontier-model-at-openai/1403886/6). He names the eventually stationary paper, claims overlap with earlier work, and expresses doubts about rigor and the absence of a rigid container. The opened comment does not isolate a false lemma or provide a mathematical refutation. Its priority claim is not adjudicated here; his earlier paper was not opened and is not cited as evidence.

5. **Community discovery pages.** Opened the oai-math-revised pages for [Eventually Stationary](https://mathcommunity.github.io/oai-math-revised/papers/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/), [Velocity-Field Detection](https://mathcommunity.github.io/oai-math-revised/papers/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/), and [Rapidly Vanishing](https://mathcommunity.github.io/oai-math-revised/papers/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/). Their collected notes explicitly say they are automatic and unreviewed. Followed their links to the primary Smith comment, Xie's arXiv paper, the Latent Seminar exposition, and the primary Lean documentation. A linked Anders Sandberg X post returned **403** and was not read; its reported content is not used as evidence.

### Lean: precisely what is and is not supplied

Opened the primary [family scope note, lean/docs/376.md](https://github.com/openai/math/blob/main/lean/docs/376.md). It lists four companions, including the rapid-decay and velocity-detection candidates, and describes these selected statements:

- **Rapidly vanishing forcing:** alternating-coordinate memory, shared compact support, rapid decay of velocity, force and all mixed derivatives, and particle-halting equivalence in the stated comparison class. This identifies the alternating construction, not blanket coverage of all three constructions and the torus corollary.
- **Velocity-field detection:** both the torus pointwise test and cylindrical integral test, with their distinct support/derivative bounds and solution classes.
- **Eventually stationary forcing:** this manuscript is not listed as a formalized main result in the scope note. A companion coding-sheet formalization explicitly excludes that companion's fixed-particle detector and solid-box maps. A generic Lean badge on a family page is therefore insufficient evidence for this candidate's entire theorem.

Opened and saved the actual statement files [NavierStokesAlternating.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/NavierStokesAlternating.lean) and [NavierStokesVelocity.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/NavierStokesVelocity.lean), their corresponding JSON configurations, and their proof entry modules. The named target declarations are `OAI.AlternatingNS.alternating` and `OAI.VelocityDetection.main_result`. The configurations point to separate proof modules, permit only `propext`, `Quot.sound` and `Classical.choice`, and disable the optional nanoda recheck. The `sorry` in a Comparator challenge file is the intentionally unproved target statement, not evidence that the separate solution contains that admission.

Also opened the actual [Alternating comparator log](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/NavierStokesAlternating.log), [Velocity comparator log](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/NavierStokesVelocity.log), and [the maintainers' checking explanation](https://github.com/mathcommunity/oai-math-revised/blob/main/docs/LEAN_CHECKS.md). Both logs report acceptance by Lean's default kernel. These are **reported runs from 25–26 October**, not builds performed for this verification. Their documentation notes the AI-assisted setup, precompiled workspace and the distinction between checking a Lean statement and establishing its equivalence to a manuscript. The opened Lean targets concern deterministic computation and contain no stochastic WAD conclusion.

### Access limitations

The three supplied GitHub folder URLs initially returned web cache misses, but the read-only GitHub connector listed them and retrieved their complete TeX sources. Guessed root main.tex URLs failed because the actual files are under build/. The three raw manuscript PDF URLs were attempted but the web tool rejected their application/octet-stream content type. Exact quotations are therefore taken from the primary TeX, not a claimed PDF transcription. No Lean build or whole-proof verification was attempted.

## Recommended replacement for “where it stands” (three sentences)

T190 remains open on the evidence checked here: none of these release papers claims WAD for the stated stationary stochastic Navier–Stokes model. OpenAI's *Universal Computation with Eventually Stationary Navier–Stokes Forcing* and *Velocity-Field Detection of Computation in Forced Navier–Stokes Flows* (both September 27, 2026) concern deterministic fluid computation at fixed positive viscosity. Its *Computation under Rapidly Vanishing Navier–Stokes Forcing* (September 27, 2026) concerns rapid decay in time of specially designed deterministic forces and velocities, rather than the required stochastic limit as viscosity vanishes.

## Spot check

Selected lemma: **“An injective local compiler”**, Lemma 3.1 of *Universal Computation with Eventually Stationary Navier–Stokes Forcing*, [primary source lines 322–422](https://github.com/openai/math/blob/main/preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/build/main.tex#L322). This is the discrete injectivity step needed before machine branches can be realized by invertible fluid maps; the velocity-detection paper also uses this compiler. The other geometric and analytic steps are outside this check.

The seven rows were checked on their entire displayed domains, not just the initialized trajectory. For a destination configuration, its control state first fixes the incoming head displacement. Reading the written full symbol at the previous head position then identifies the incoming rule as follows.

| Destination | Displacement | How its incoming rule is recovered |
|---|---|---|
| \(A_\tau\) | \(d_\tau\) | \(\tau=(q,a)\) determines the old control and read data; the written history letter recovers the unchanged history. |
| \(F_\tau\) | \(+1\) | Written marker 1 identifies the arrival from \(A_\tau\); marker 0 identifies the scan loop. |
| \(C_q\) | \(+1\) | The written tag \(\tau\) identifies the old \(F_\tau\); old history was \(E\). |
| \(L_q\) | \(-1\) | Written history \(E\) identifies arrival from \(C_q\); the scan loop expressly excludes \(E\). |
| \(R_q\) | \(0\) | Only the last row arrives; restore marker 1 and keep data and history. |

Thus the proposed inverse distinguishes every pair of incoming row types, including on uninitialized configurations in the partial table's domain.

The checkpoint invariant was checked separately. After \(n\) augmented machine steps the head satisfies \(|h|\le n\), and the history frontier is \(n+2\). The next work head is \(h'=h+d_\tau\le n+1<n+2\), so neither the data-write row nor the marker-write row reads the frontier symbol \(E\). The rightward scan terminates at \(n+2\), stores the tag there, and the following row writes the new frontier at \(n+3\); the leftward scan then encounters the unique marker at \(h'\). This preserves the data, head and history invariant and ensures that each simulated step takes finitely many defined transitions.

There are five non-loop transitions, \(n+1-h'\) right-scan loop transitions, and \(n+2-h'\) left-scan loop transitions. Their sum is
\[
5+(n+1-h')+(n+2-h')=4+2(n+2-h'),
\]
which matches the source's microstep count. The added fresh start state also handles an originally halting initial state without changing the halting equivalence.

As a second check, a small exact enumeration expanded the seven rows for all 144 binary-alphabet, one-working-state transition tables with a halting destination, after adding the fresh start state. It checked 25,056 expanded rules for uniqueness of the inverse key and consistency of arrival displacement, then 1,008 initialized runs on all binary inputs of length at most two, checking up to eight macrosteps and a total of 4,422 checkpoints. No collision, undefined initialized transition, invariant failure or microstep-count discrepancy occurred; [the saved output](sources/compiler-check.txt) records the counts. This finite enumeration supplements the symbolic argument and is not a proof for arbitrary machines.

No defect was found in this selected compiler lemma. That finding neither verifies the full fluid constructions nor supplies a connection to stochastic WAD.


