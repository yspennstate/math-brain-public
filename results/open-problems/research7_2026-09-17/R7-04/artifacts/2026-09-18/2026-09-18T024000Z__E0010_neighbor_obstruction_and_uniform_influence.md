Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding model/effort selector is exposed.

# E0010 — exact local discrepancy obstruction and a quantifier-swapped influence criterion

Target: Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 4: for the source sexual-reproduction model with fixed `beta>4.5`, prove that sufficiently fast stirring gives a unique nontrivial stationary distribution.

This note continues R7-04's ordered-coupling, relative-stirring, branch-selection, nucleation, and backward-ancestry work.  It does **not** solve the source.  It executes the prescribed B30/B27/B21 recovery triple and isolates a new exact obstruction that does not assume local exchangeability.

## 1. Setup

Let `eta<=xi` be a stationary basic ordered coupling.  At each site write

\[
A_x=\eta_x,\qquad D_x=\xi_x-\eta_x,\qquad C_x=1-\xi_x.
\]

Thus exactly one of `A_x,D_x,C_x` equals one.  Let `N_x` be the source birth neighborhood, of fixed size `n`, and assume the usual symmetric translation-covariant neighborhood `N_0=-N_0`.  Define

\[
K_A(x)=\sum_{y\in N_x}A_y,\qquad
K_D(x)=\sum_{y\in N_x}D_y,\qquad
K_C(x)=n-K_A(x)-K_D(x).
\]

For `0<=k<=n`, put

\[
r_n(k)=\frac{k(k-1)}{n(n-1)}.
\]

The source birth rate at a vacant site whose neighborhood contains `k` occupied sites is `beta r_n(k)`.

The fixed source metric remains

\[
Q_{SR}(\beta,\varepsilon)
=\sup_{\mu\in\mathcal I^{nt}_{\beta,\varepsilon}}
\bigl[\bar\nu_{\beta,\varepsilon}(\eta(0))-\mu(\eta(0))\bigr].
\]

It is still UNKNOWN/UNMEASURED.

## 2. B30 — exact one-neighborhood localization

The new idea is to stop coarse-graining first and ask what a single discrepancy can do in one exact source neighborhood.

### Lemma 2.1 — exact reaction generator for a discrepancy

For every site `x`, the reaction part of the coupled generator satisfies

\[
\boxed{
R D_x
=-D_x
-\beta D_x r_n(K_A(x))
+\beta C_x\Bigl[r_n(K_A(x)+K_D(x))-r_n(K_A(x))\Bigr].
}
\tag{2.1}
\]

#### Proof

A common death mark kills a discrepancy at rate one, giving `-D_x`.  If `D_x=1`, the upper process is occupied and the lower process is vacant.  A lower birth heals the discrepancy exactly when both sampled parents are lower-occupied, i.e. both have color `A`; this has rate `beta r_n(K_A)`.  If `C_x=1`, both processes are vacant.  A discrepancy is created exactly when the upper process accepts the birth but the lower process does not.  The upper process sees `K_A+K_D` occupied neighbors whereas the lower sees `K_A`, giving the final difference of birth rates.  If `A_x=1` no reaction creates a discrepancy at `x`.  These cases exhaust the graphical marks. QED.

### Lemma 2.2 — deterministic creation bound

For integers `a,d>=0` with `a+d<=n`,

\[
\boxed{
r_n(a+d)-r_n(a)\le \frac{2d}{n}.}
\tag{2.2}
\]

#### Proof

The difference counts ordered occupied parent pairs that use at least one of the `d` newly available discrepancy neighbors.  For each new neighbor there are at most `2(n-1)` ordered pairs in which it occurs.  Hence at most `2d(n-1)` new ordered pairs occur.  Divide by `n(n-1)`. QED.

The bound is intentionally one-sided and robust: no exchangeability or independence is used.

## 3. Exact Palm neighbor-count obstruction in the translation-invariant case

The preceding runs produced an ideal mixed-color polynomial.  The next theorem gives a different, exact finite-neighborhood obstruction before any mixing approximation.

### Theorem 3.1 — common-one-poor neighborhoods are forced under disagreement Palm

Assume the stationary ordered coupling is spatially translation invariant.  Let

\[
q=\mathbb E D_0.
\]

If `q>0`, define discrepancy-Palm expectation by

\[
\mathbb E^D[F]=\frac{\mathbb E[D_0F]}q.
\]

Set

\[
g_{\beta,n}(k)
=-1
-\beta\frac{k(k-1)}{n(n-1)}
+2\beta\left(1-\frac{k}{n}\right),
\qquad 0\le k\le n.
\tag{3.1}
\]

Then

\[
\boxed{\mathbb E^D\bigl[g_{\beta,n}(K_A(0))\bigr]\ge0.}
\tag{3.2}
\]

Moreover `g_{beta,n}` is strictly decreasing.  Let

\[
m_{\beta,n}=\max\{k\in\{0,\ldots,n\}:g_{\beta,n}(k)\ge0\},
\tag{3.3}
\]

and

\[
\gamma_{\beta,n}=-g_{\beta,n}(m_{\beta,n}+1)>0,
\qquad
G_\beta=g_{\beta,n}(0)=2\beta-1.
\tag{3.4}
\]

Then every nonzero translation-invariant stationary discrepancy obeys the quantitative lower bound

\[
\boxed{
\mathbb P^D\bigl(K_A(0)\le m_{\beta,n}\bigr)
\ge
\frac{\gamma_{\beta,n}}{G_\beta+\gamma_{\beta,n}}>0.
}
\tag{3.5}
\]

#### Proof

Translation invariance makes the expected stirring contribution at a fixed site vanish.  Taking expectation in (2.1) therefore gives

\[
0
=-q
-\beta\mathbb E[D_0r_n(K_A(0))]
+\beta\mathbb E\!\left[C_0\{r_n(K_A+K_D)-r_n(K_A)\}\right].
\tag{3.6}
\]

By Lemma 2.2,

\[
\mathbb E\!\left[C_0\{r_n(K_A+K_D)-r_n(K_A)\}\right]
\le \frac2n\mathbb E[C_0K_D(0)].
\tag{3.7}
\]

Now use translation invariance and symmetry of the source neighborhood:

\[
\begin{aligned}
\mathbb E[C_0K_D(0)]
&=\sum_{z\in N_0}\mathbb E[C_0D_z]\\
&=\sum_{z\in N_0}\mathbb E[D_0C_{-z}]\\
&=\mathbb E[D_0K_C(0)]\\
&\le \mathbb E[D_0(n-K_A(0))].
\end{aligned}
\tag{3.8}
\]

Substituting (3.7)-(3.8) into (3.6) gives

\[
0\le
\mathbb E\left[D_0\left\{-1-\beta r_n(K_A(0))+2\beta\left(1-\frac{K_A(0)}n\right)\right\}\right],
\]

which after division by `q` is (3.2).

For strict monotonicity,

\[
g_{\beta,n}(k+1)-g_{\beta,n}(k)
=-\frac{2\beta k}{n(n-1)}-\frac{2\beta}{n}<0.
\tag{3.9}
\]

Also `g(0)=2beta-1>0` while `g(n)=-1-beta<0`, so `m_{beta,n}` is well-defined and at most `n-1`.  Put

\[
p=\mathbb P^D(K_A\le m_{\beta,n}).
\]

On this event, monotonicity gives `g(K_A)<=G_beta`; on its complement, `g(K_A)<=-gamma_beta,n`.  Therefore

\[
0\le\mathbb E^Dg(K_A)
\le pG_\beta-(1-p)\gamma_{\beta,n},
\]

which rearranges to (3.5). QED.

### Interpretation

Theorem 3.1 is a finite-neighborhood analogue of the preceding ideal-Palm lower-bound theorem.  It says that a persistent discrepancy cannot live almost exclusively in common-one-rich neighborhoods.  A fixed positive fraction of discrepancy-Palm mass must see a common-one count at or below an explicit integer threshold.  Unlike the earlier polynomial calculation, this conclusion uses no local exchangeability assumption.

The important scope limitation is equally explicit: the proof used spatial translation invariance in (3.8).  Durrett's source asks for uniqueness of nontrivial stationary distributions without adding that hypothesis.  The theorem is therefore **PARTIAL**, not source closure.

## 4. The continuous threshold lands exactly at beta=4.5

The large-neighborhood/continuous version of (3.1) is

\[
g_\infty(a)=-1-\beta a^2+2\beta(1-a).
\tag{4.1}
\]

Its unique zero in `[0,1]` is

\[
\boxed{a_\dagger(\beta)=\sqrt{3-1/\beta}-1.}
\tag{4.2}
\]

The stable positive mean-field equilibrium is

\[
\rho_+(\beta)=\frac{1+\sqrt{1-4/\beta}}2.
\tag{4.3}
\]

### Proposition 4.1 — exact threshold alignment

For `beta=9/2`,

\[
\rho_+(\beta)=a_\dagger(\beta)=\frac23.
\]

For every `beta>9/2`,

\[
\boxed{\rho_+(\beta)>a_\dagger(\beta).}
\tag{4.4}
\]

#### Proof

Write `s=sqrt(1-4/beta)`.  Since both sides are nonnegative,

\[
\rho_+>a_\dagger
\iff
\frac{3+s}{2}>\sqrt{3-1/\beta}.
\]

Squaring and using `s^2=1-4/beta` reduces this to

\[
\frac32s>\frac12,
\]

i.e. `s>1/3`, which is exactly `beta>9/2`.  Equality at `beta=9/2` is immediate. QED.

This is a structural explanation for why the source's `4.5` threshold keeps reappearing in the disagreement calculation: immediately above `4.5`, the stable mean-field branch lies strictly on the contraction side of the coarse exact discrepancy-growth threshold.  What remains is to force the actual discrepancy ancestry to spend enough time in that stable environment.

## 5. B27 — swap the quantifiers: a forward influence criterion

The preceding run formulated a backward bad-corridor estimate under terminal discrepancy Palm conditioning.  That wording risks hiding the same normalization problem in a different place.  The safer quantifier order is to prove a uniform **forward** continuation estimate for every possible incoming history, and only then deduce uniqueness.

### Theorem 5.1 — uniform influence path criterion

Consider a space-time coarse graining whose directed block graph has maximum in-degree and out-degree at most `B`.  Suppose there is a block influence construction with the following property.

For every deterministic directed coarse path

\[
\pi=(v_0,v_1,\ldots,v_m)
\]

and every admissible ordered incoming state and revealed history up to the entry face of each successive block, the conditional probability, using the fresh graphical marks in the next slab, that a discrepancy influence follows the specified next edge is at most `r`, uniformly in the history.  Assume

\[
Br<1.
\tag{5.1}
\]

Then any stationary ordered coupling for which discrepancies admit the corresponding subadditive graphical influence representation has zero discrepancy density.  In particular its two stationary marginals coincide.

#### Proof

For one fixed path of length `m`, iterated conditioning gives probability at most `r^m`; no independence assumption is needed because the bound is uniform over every previously revealed history.  At most `B^m` directed paths of length `m` end at any specified block.  Hence the total influence kernel into a fixed terminal block has column mass at most

\[
(Br)^m.
\tag{5.2}
\]

Let `q_v` be the stationary discrepancy probability in coarse cell `v`, and `Q=sup_v q_v`.  The subadditive graphical influence representation gives

\[
q_v\le\sum_u q_uK_m(u,v)
\le Q\sum_uK_m(u,v)
\le Q(Br)^m.
\tag{5.3}
\]

Taking the supremum over `v` yields

\[
Q\le Q(Br)^m.
\]

If `Q>0`, division gives `1<=(Br)^m` for every `m`, contradicting (5.1) for large `m`.  Thus `Q=0`. QED.

### Why this formulation matters

The theorem starts with an incoming discrepancy and bounds every possible continuation **before** conditioning on a discrepancy at the far endpoint.  It therefore does not produce the fatal factor `1/Q` from the previous ordinary bad-block estimate.  It also does not assume independent bad blocks: history dependence is allowed as long as the conditional continuation bound is uniform.

For E0010, this theorem is a closure template, not yet a verified hypothesis.  The source fast-stirring block construction controls mature positive blocks in ordinary probability.  What is still missing is a uniform influence estimate for a discrepancy entering an arbitrary admissible block state, or a finite-state enlargement of the coarse block type for which the resulting multi-type influence matrix has spectral radius below one.

## 6. B21 — analogous-field import, with the dependence caveat made explicit

The path-of-disagreement strategy has a genuine analogue in disagreement-percolation uniqueness arguments.  Van den Berg and Maes (1994) use percolation-like disagreement paths to control boundary influence in Markov fields.  But Häggström (2001) constructs counterexamples showing that merely having no infinite disagreement path under an arbitrary dependent coupling does **not** by itself imply uniqueness; the independence assumption in the original disagreement-percolation method cannot simply be discarded without replacement conditions.

That warning is directly relevant here.  It rules out the tempting but invalid shortcut

> ordinary bad-block probability is small, therefore a discrepancy ancestry sees approximately independent bad blocks.

Theorem 5.1 instead asks for a conditional continuation bound uniform over the exposed incoming history.  This is closer to a branching-random-walk domination: the expected path count contracts by the factor `Br` per scale.  Dependence is harmless only because it is absorbed into the worst-case conditional bound.

Thus the imported technique sharpens, rather than closes, the source problem.

## 7. Exact new blocker after B30/B27/B21

The current proof architecture now has four clean layers.

1. **Relative stirring:** local disagreement probabilities and every finite tagged moment have `O(epsilon^2)` stirring defects after division by the unknown discrepancy scale `Q`; this removed the analytic `1/Q` loss.
2. **Branch obstruction:** a persistent discrepancy must spend positive Palm mass in low/common-one environments; Theorem 3.1 now proves a finite-neighborhood version exactly for translation-invariant couplings, with no exchangeability hypothesis.
3. **Genealogy:** every present discrepancy has an indefinitely long backward discrepancy ancestry.
4. **Needed forward contraction:** prove a source-valid block influence estimate satisfying the hypotheses of Theorem 5.1, or a multi-type version with spectral radius `<1`.

The remaining gluing failure is precise.  The source block construction makes a mature high-density block reproduce other mature blocks with high probability.  Uniqueness needs the dual statement that **a discrepancy influence cannot keep threading through exceptional low-density interfaces**, uniformly over the incoming history selected by the discrepancy itself.  An ordinary estimate `P(block bad)<=delta` is insufficient; the required object is a conditional influence kernel.

A promising next formulation is a two-type block system:

- `H`: mature/common-one-rich blocks, where the exact local calculation gives a strict discrepancy-reproduction gap;
- `L`: low/common-one-poor blocks, whose occurrence along a discrepancy influence path must be controlled by fresh-slab block estimates.

If one can bound the 2x2 matrix of worst-case expected discrepancy descendants and prove its spectral radius `<1`, Theorem 5.1 extends verbatim and gives `Q_SR=0`.

## 8. Method outcomes

### B30 — one scale/direction at a time

**Success, partial theorem.**  Localizing all the way to one source neighborhood gives the exact generator (2.1), deterministic creation bound (2.2), and translation-invariant Palm obstruction (3.2)-(3.5).  It also isolates the exact gluing failure: turning high-density ordinary blocks into worst-case discrepancy-influence contraction.

### B27 — swap the quantifiers

**Success, conditional closure theorem.**  Instead of conditioning the environment on a terminal disagreement, Theorem 5.1 quantifies over every incoming history first.  A uniform continuation bound `r<1/B` immediately forces zero stationary discrepancy by a path-count/influence argument.

### B21 — analogous field

**Success as route correction, not source closure.**  Disagreement percolation validates path-of-disagreement thinking, while Häggström's dependence counterexample shows why ordinary marginal bad-block estimates are not enough.  The route must prove a uniform conditional influence estimate or an equivalent domination theorem.

No finite checker was built: the new claims are theorem-sized and their proofs are written above.

## 9. Dated source/prior-art review — 2026-09-18

The primary source remains Rick Durrett's 2009 paper/arXiv:0906.2293, which explicitly presents nine open problems and contains the admitted Problem 4.  Fresh exact-phrase and model-specific searches on 2026-09-18 recovered no later theorem explicitly resolving the fast-stirring sexual-reproduction uniqueness question.  This is bounded negative evidence only, not a novelty certificate.

Related methodology checked in this run:

- J. van den Berg and C. Maes, *Disagreement percolation in the study of Markov fields*, Ann. Probab. 22 (1994), 749–763.
- O. Häggström, *A note on disagreement percolation*, Random Structures & Algorithms 18 (2001), 267–278; the paper explicitly shows that independence in disagreement-percolation uniqueness arguments cannot simply be removed without replacement conditions.
- C. Hofer-Temmel, *Disagreement percolation for the hard-sphere model* (2015), another example where a dominated percolation object yields uniqueness.

No claim is made that these works contain E0010's theorem.

## 10. Status and next attack

Source status: **PARTIAL / OPEN**.

Frozen metric:

`Q_SR(beta,epsilon): UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`.

Movement: **NONE**.

This is the fifth ordinary unchanged E0010 research run.  Under the CLOSABLE protocol, one further ordinary no-movement run reaches the six-run retirement/handoff threshold.

The next triple must differ from B30/B27/B21.  The selected methods are:

1. **B3 — prove something stronger:** seek a multi-type block influence theorem whose worst-case influence matrix has spectral radius `<1`, rather than only a scalar one-path bound.
2. **B15 — break symmetry on purpose:** test the influence estimate against adversarial low-density entry faces and maximally clustered discrepancy patterns to identify the true worst block state.
3. **B20 — find why the algorithm fails:** turn the source's one-pile-makes-two-piles block algorithm around and compute the exact event by which an incoming discrepancy escapes a mature block; if that event is not uniformly rare, record the explicit obstruction instead of another ordinary bad-block estimate.

If that run leaves `Q_SR` unchanged, preserve an immutable E0010 handoff and rotate through the shard-3 admission gate; do not manufacture a seventh unchanged run.