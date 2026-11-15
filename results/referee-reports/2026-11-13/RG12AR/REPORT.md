Overall verdict: MINOR

The proof of (R) in the supplied paper is sound. I found no missing regular-variation assumption, unjustified martingale law of large numbers, or reversal of an inequality in its proof. The exhaustion argument also works for arbitrary adapted peeling algorithms, including algorithms using independent randomness. The minor corrections requested below concern the change of variables at the single endpoint g=0 and making the algorithm/filtration convention explicit. Neither requires a new estimate or a change to the theorem.

There is a real danger nearby: for some admissible critical sequences the **untruncated** increment of log h(P_n) has infinite expectation. I give an explicit example below. The paper does not center that increment. Its bounded truncation and localization are essential, and they address precisely this obstruction. Thus the earlier PARTIAL assessment does not identify a gap in the proof supplied here.

I checked PAPER.tex against text extracted from PAPER.pdf. Line references below are to PAPER.tex. In the compiled numbering, **Lemma 3.2 is `lem:est`, lines 152–173**, including (a)–(d) and the assertion about b. **Proposition 4.4 is `prop:sum`, lines 235–253**. The inequality display (3.2), lines 138–141, is a separate item from Lemma 3.2.

No external sources were opened. The standard map construction, disk integral, harmonicity, and spatial Markov law are examined in the forms stated in the manuscript; the original cited publications are not supplied here. My new computations import no author program. All new programs and outputs are in this directory.

## Theorem 1.1 — SOUND

Statement: lines 51–53. Proof: lines 277–285.

Here and throughout, “algorithm” must have its usual peeling meaning: the selected boundary edge is a function of the explored information and independent auxiliary randomness, not of the unseen map. This is the convention under which the spatial Markov law in the Setting applies. To remove a minor filtration ambiguity, include the choice of the next edge in F_n, or enlarge the exploration filtration at the outset by the whole independent random seed. Such enlargement preserves the conditional map law.

With this convention, the proof has the following valid implications.

1. Propositions 4.2 and 4.4 give eventual P_n≥16 and divergence of the sum of R(P_n). Lemma 3.2 therefore gives (5.1), the divergent sum of the swallowing lower bounds. No estimate for the finitely many small perimeters is needed.
2. Each edge *occurrence* indexed by (n,i) is measurable when it is indexed. For m≥n, its continued exposure is F_m-measurable. Its first loss of exposure is consequently a stopping time. Before n its stopping event is empty; the artificial value n+1 for an invalid index causes no difficulty.
3. On survival, Lemma 5.1 gives a lower bound for its conditional loss probability at every later step. Lemma 5.2 and the divergent sum contradict eternal survival. This argument does not require independence of the gluing events.
4. There are only countably many pairs (n,i). Hence one probability-one event covers every edge ever exposed. The proof does not improperly choose an unobserved, map-dependent vertex and then apply a conditional estimate to it.
5. On that event the finite dual-path argument in line 284 is pathwise. The first missing face along the path has an edge adjacent to an already discovered face; that edge is exposed, and its eventual loss of exposure adds the other face. This is a contradiction. This uses the ordinary connected dual and finite faces of the map in the stated setting. Every edge and vertex is incident to a face, giving exhaustion of the map.

The lower bound is uniform in the selected edge. Thus neither an adversarial adapted choice nor independent randomization breaks the argument. The event of exhaustion may depend on the algorithm; the theorem asserts probability one for each algorithm, not a single event simultaneously covering every conceivable algorithm.

## Proposition 3.1 (`prop:kernel`) — SOUND, with an endpoint correction in the proof

Lines 106–136.

**Criticality and differentiability, lines 119–123.** With a_k as defined, admissibility and criticality give

\[
\sum_k a_k=1-1/Z,\qquad
\sum_k(k-1)a_k=1/Z,\qquad
\sum_k k a_k=1.
\]

In particular the derivative series has a summable uniform majorant. Thus J is continuously differentiable on [0,1], with the one-sided derivative at 1, and

\[
J'(r)=Z\sum_{k\ge2}k a_k(1-r^{k-1})\ge0.
\]

The sign is correct. Some a_k with k≥2 is positive, so J'>0 for r<1. Also J(0)=0 and J(1)=1. No second moment, f''(Z), or analytic extension past Z is used. The argument remains valid when Z is exactly the convergence radius.

**The substitution, lines 115–126.** For 0<g≤1, putting y=gx in the defining equation for Z_{q_g} gives y(1-f(y))=g. Monotonicity on [0,Z] identifies the smallest positive solution as Z J^{-1}(g). A smaller solution would lie in this interval, where strict monotonicity excludes it. Consequently g c_{q_g}=c J^{-1}(g), as required. The substitution in the disk integral is legitimate even though J'(1)=0: it is a monotone C^1 substitution, and the proof does not differentiate J^{-1}.

There is a literal endpoint defect in the stated equivalence at line 123: when g=0, y=gx=0 for every x, so the transformed equation cannot characterize which x solves the original equation. Restrict that sentence to g>0. At g=0, q_g has only its q_1 weight and g c_{q_g}=0; the desired identity follows directly or by continuity. A single integration endpoint has no effect on the integral. This is the reason for a minor correction, not a gap in the proposition.

**Interchange and constants, lines 127–135.** Tonelli is applied to the nonnegative functions r^{k-1}(1-r^{l-1}); it is not an interchange of two separately divergent series. The resulting integral is

\[
Z\sum_{l\ge2}l a_l\left(\frac1k-\frac1{k+l-1}\right)
=\frac Zk\sum_{m\ge1}\frac{m(m+1)a_{m+1}}{m+k}.
\]

The difference has the correct positive sign. The coefficient identity

\[
(m+1)a_{m+1}=(2m+1)d(m)\nu(m)
\]

is exact. Multiplication by 2c^{-k}c^{k-1}d(k-1), with c=4Z, gives d(k-1)T(k)/(2k); the recurrence for d converts this to d(k)T(k)/(2k-1). There is no missing factor of two or perimeter shift. At k=1, W^{(0)}=1 gives ν(-1)=1/(2Z), and the formula gives the same answer since d(1)=1/2 and T(1)=1/Z.

The finiteness bounds in line 135 and strict positivity are valid. The comparisons (3.2) and (3.3), lines 138–145, also hold: for example, (m+p)/(m+k)≤p/k when k≤p. These comparisons require positivity of the weights, not tail regularity.

The external starting point is the disk representation (3.1). In the normalization printed here it is consistent with the standard critical quadrangulation check Z=2, q_2=1/12, J'(r)=2(1-r), giving W^{(1)}=4/3. I cannot independently verify the cited equation number in Curien's unsupplied preliminary version.

## Lemma 3.2 (`lem:est`) — SOUND, all four parts and the lower bound

Lines 152–173. All constants can be chosen independent of q.

**(a), line 164.** For k>p/2, either k≥p and T(k)≤T(p), or k<p and T(k)≤(p/k)T(p)<2T(p). Therefore

\[
\sum_{k>p/2}\nu(-k)
\le 2T(p)\sum_{k\ge\lfloor p/2\rfloor+1}k^{-3/2}
\le6\sqrt2\,R(p).
\]

The displayed integral comparison is valid also at p=1. Since k≥p implies k>p/2, the same upper bound applies to δ(p). No lower bound on δ is claimed or subsequently substituted for this upper bound.

**(b), line 166.** Termwise upper bounds give

\[
\sum_{k\le p}k^2\nu(-k)
\le pT(p)\sum_{k\le p}k^{-1/2}
\le2p^{3/2}T(p)=2p^2R(p).
\]

The inequality uses T(k)≤pT(p)/k in the correct direction.

**(c), line 168.** Since w_m≥m^{3/2}ν(m), m^2ν(m)≤p^{1/2}w_m for m≤p. Also w_m≤2p w_m/(m+p) in that range. Summation gives the claimed bound with constant 2. No second moment of the unrestricted positive law is being assumed.

**(d), line 170.** For m>p/2, m+p<3m, so

\[
T(p)\ge\frac13\sum_{m>p/2}\sqrt m\,\nu(m).
\]

After division by sqrt(p), this is exactly (d) with constant 3. The direction of this inequality is particularly important and is correct. It controls the positive h-transform tail, whose weighting is of order sqrt(m/p).

**Swallowing lower bound, line 172.** For p≥16, the integers j in [ceil(p/2)+1,floor(3p/4)] number at least p/8. They correspond to permitted gluing indices k=j-1≤p-2, leave p-j≥p/4, and satisfy j≤p. Thus, using a lower bound this time,

\[
\nu(-j)\ge\tfrac14p^{-3/2}T(p),\qquad
h(p-j)/h(p)\ge\tfrac14.
\]

Including the prescribed-side factor 1/2 gives exactly R(p)/256. There is no conversion of an upper bound into a lower bound. For p≥4 the original sum is nonempty with positive terms. At p=1,2,3 it may be empty; the paper does not claim otherwise or rely on positivity there.

## Lemma 4.1 (`lem:big`) — SOUND

Lines 179–188.

For downward transitions in B_p the h ratio is at most one, and Lemma 3.2(a) bounds both required sums. For upward transitions m>p/2, (2.2) gives

\[
h(p+m)/h(p)\le2\sqrt{(p+m)/p}\le2\sqrt3\sqrt{m/p}.
\]

Lemma 3.2(d) therefore bounds their K mass. The unweighted ν mass is bounded because 1≤sqrt(2)sqrt(m/p) on this range. This establishes both bounds, including for small p. No estimate of an untruncated logarithmic moment is concealed here.

## Proposition 4.2 (`prop:escape`) — SOUND

Lines 190–200.

The cancellation of h in the transition law gives exactly

\[
E_p[1/h(P_1)]=(1-\delta(p))/h(p).
\]

All quantities are nonnegative and finite. Telescoping expectations up to a deterministic time N and then using monotone convergence gives the bound printed in the proof. Finite expectation of this nonnegative accumulated drift implies its almost-sure finiteness.

For every fixed p, δ(p)>0, since all the negative kernel values are positive. An infinite number of visits to p would contribute infinitely many copies of the fixed positive number δ(p)/h(p). Thus each state is visited finitely often, simultaneously for all states by countability. Each finite set is then eventually avoided, which is exactly P_n→∞. Irreducibility, finite mean jumps, a scaling limit, and a law of large numbers are unnecessary.

## Lemma 4.3 (`lem:L`) — SOUND

Lines 202–231.

The bound on U(y)-U(p) follows by summing log(1+1/(2j)) over indices j≥min(y,p)≥p/2. It is valid at the endpoints of S_p and for p=1. Hence |L|≤1/2. On S_p the h ratio is <2; the second-moment bound follows from Lemma 3.2(b),(c), exactly as printed.

For the mean, H=h(P_1)/h(p) is strictly positive. Its reciprocal is integrable, and

\[
E_p[H^{-1}]=1-\delta(p).
\]

In particular E|1-H^{-1}|≤1+E[H^{-1}]≤2, so separating this expectation over S_p and B_p is justified. On B_p, multiplying |1-H^{-1}| by K cancels the troublesome reciprocal and yields precisely

\[
\sum_{y\in B_p}\nu(y-p)|h(y)/h(p)-1|
\le K(p,B_p)+\sum_{y\in B_p}\nu(y-p).
\]

Together with the upper bound on δ, this makes the signed expectation on S_p O(R(p)). On S_p only, |u|≤1/2 and |u-(1-e^{-u})|≤u^2. The already proved second-moment bound then establishes |E L|≤C R(p) uniformly.

The proof bounds the mean of **L**, not E[U(P_1)-U(p)]. This distinction is substantive: the latter expectation need not exist as a finite number. There is no integrability gap in the lemma as actually stated.

## Proposition 4.4 (`prop:sum`) — SOUND

Lines 235–253. This is the decisive proof of the requested divergence.

**Definitions and centering, line 240.** L_n is F_{n+1}-measurable, bounded by 1/2, and integrable. Its conditional mean μ_n is F_n-measurable, |μ_n|≤C R(P_n), and |D_n|≤1. Also E[D_n^2|F_n]≤E[L_n^2|F_n]≤C R(P_n). These facts involve no untruncated logarithmic expectation.

**Localization, lines 240–243.** A_n is adapted (indeed F_{n-1}-measurable for n≥1), so τ_K is a stopping time and 1{n<τ_K} is an F_n-measurable multiplier of D_n. At its first crossing A can overshoot K by at most R(1). Thus the stated deterministic bound on the stopped sum is correct. It also covers τ_K=∞ by taking increasing partial sums.

**Martingale convergence, lines 244–248.** The stopped centered differences are martingale differences. Their cross terms have expectation zero by conditioning on the earlier filtration; independence is not required. The displayed bound is a uniform L^2 bound on the stopped martingale. The L^2 martingale convergence theorem gives almost-sure convergence. This is not an unsupported strong law for a martingale with random quadratic variation.

**Large jumps, lines 249–251.** The expected number of stopped large relative jumps is bounded by C(K+R(1)). Tonelli and conditional expectation justify the equality in the paper. A nonnegative integer-valued count with finite expectation is finite almost surely. Neither independence nor summability of unconditional probabilities along the unstopped trajectory is needed.

**Removing the stop, line 252.** Work on the intersection of the probability-one conclusions for positive integer K. On E={A_infinity<∞}, some integer K exceeds A_infinity and τ_K=∞. This is a valid countable localization, not a substitution of a random K into an unproved almost-sure statement. On E the centered series converges, the means sum absolutely, and only finitely many transitions are omitted by truncation. Each omitted log increment is finite, even when its distribution has infinite expectation. The untruncated telescoping sum therefore converges to a finite limit on E. Proposition 4.2 makes that impossible.

There is no uncovered “very rapid growth” event. Rapid growth through infinitely many large relative jumps contradicts their finiteness on E; rapid growth through the remaining small jumps contradicts convergence of their centered sum plus the absolutely summable drift. Bounded trajectories are excluded by Proposition 4.2; alternatively, R has a positive minimum on every finite set, so such trajectories could not have a finite accumulated rate anyway.

## Remark 4.5 — SOUND

Lines 255–257.

When the asymptotic premise stated in the remark holds, the exact kernel and d(p) asymptotics yield T(p) comparable to p^{3/2-a}, and hence R(p) comparable to p^{1-a}. This is an interpretation of Proposition 4.4 in a regular regime, not an input to it. The remark includes a=5/2 and excludes a=3/2 in its own wording. Nothing in the main proof requires extending this remark beyond its premise.

## Lemma 5.1 (`lem:swallow`) — SOUND

Lines 261–267, with the measurability convention stated under Theorem 1.1.

For a currently exposed, F_n-measurable edge distinct from the selected edge, one of its two cyclic distances from that edge is ≤p. On that prescribed side, every allowed k≥ceil(p/2) swallows all positions 1 through 2k+1, which include the marked edge. For even p, 2k+1≥p+1; for odd p the bound is still stronger. The range k≤p-2 leaves positive infinite-side half-perimeter. These events have the disjoint probabilities in (P2), and their sum is b(p). If the marked edge is selected, its removal is certain.

The factor 1/2 is retained; the proof does not add left and right probabilities that overlap. The chosen side may depend on both the marked edge and the selected edge: both are known before the peeling outcome, and either side has the same specified gluing probabilities. This is why the lower bound survives arbitrary adapted edge selection. Boundary occurrences can be indexed when the boundary is not simple; no assumption of a simple cycle of distinct vertices is used.

## Lemma 5.2 (`lem:hazard`) — SOUND

Lines 269–275.

Since τ is a stopping time, r_m=0 on {τ≤m}; on {τ>m}, the next survival probability is 1-r_m. The displayed conditional expectation is correct. For each fixed m, Y_m≤e^m, so it is integrable. The nonnegative supermartingale converges almost surely to a finite limit, implying the assertion on {τ=∞}.

There is also a shorter independent check of the lemma:

\[
E\sum_{n\ge0}r_n
=\sum_{n\ge0}P(\tau=n+1)
=P(\tau<\infty)\le1.
\]

Thus the sum is actually finite almost surely on the whole space. This follows from Tonelli and uses no independence. These r_n are the survival-inclusive conditional event probabilities defined in the paper, rather than hazard probabilities conditioned separately on survival. On the eternal-survival event their lower bound by b(P_n) is exactly what is needed. The application is a valid conditional Borel–Cantelli/compensator argument.

## (R)

**Verdict: correct for every admissible critical q in the stated map setting.** Proposition 4.4 proves the equivalent sum of R, and (3.2) gives termwise

\[
\tfrac14R(p)\le p\nu(-p)\le R(p),\qquad p\ge1.
\]

Thus (R) follows with precisely the normalization requested. No tail limit appears in this inference.

All inputs to the proof are positivity, the critical equations, the disk/harmonic identities, and the resulting elementary kernel comparisons. Oscillating and sparse positive tails retain these properties. At the a=5/2 endpoint even a positive law supported on one atom works. At the lower borderline it is important not to insert a false positive-constant pure power asymptotic: write β_m=(m+1)a_{m+1}, so sum β_m=1-q_1<∞ and

\[
T(p)=\sum_m\beta_m\frac{m}{m+p}\longrightarrow0
\]

by dominated convergence. Hence critical sequences here satisfy ν(-p)=o(p^{-3/2}); index-3/2 behavior can carry a decaying slowly varying factor. The proof places no lower bound on how slowly T tends to zero and covers such legitimate borderline sequences too.

**A counterexample to a tempting replacement argument, not to the paper.** Let m_j=2^{j^2} and β_{m_j}=6/(π²j²), j≥1, all other β zero. Set q_1=0 and

\[
Z=\left(1-\sum_m\frac{\beta_m}{m+1}\right)^{-1},\qquad
q_{m+1}=\frac{\beta_m}{(m+1)\binom{2m+1}{m}Z^m}.
\]

This is admissible critical: the two critical equations hold, and the corresponding J is strictly increasing up to Z, ensuring the required smallest root. At p=1 there are no allowed downward transitions and

\[
K(1,m+1)=\nu(m)h(m+1)=\beta_m.
\]

Consequently

\[
E_1\log h(P_1)=\sum_j\frac{6}{\pi^2j^2}\log h(2^{j^2}+1)=\infty,
\]

because the jth summand tends to 3 log(2)/π²>0. An argument claiming a finite full logarithmic drift O(R(1)) would fail on this example. In the actual paper L(1,P_1)=0 for this example, and the stopped large-jump argument is valid. This distinction resolves the main integrability concern raised in the question.

## Independent checks, programs, and outputs

### Files and resource use

The programs are `audit_setup.sh`, `audit_environment.py`, `audit_exact.py`, `audit_simulate.py`, `audit_pathologies.py`, and `audit_verify.py`. Reproducible numerical outputs are `audit_environment_out.txt`, `audit_exact_out.txt`, `audit_exact_results.json`, `audit_simulate_out.txt`, `audit_simulation_results.json`, `audit_pathologies_out.txt`, and `audit_verify_out.txt`. The extracted compiled text is `audit_pdf.txt`.

The numerical programs set a 240-second wall alarm and a 220-second CPU limit. They use a single Python process and no worker pool. The recorded numerical runs took about 3.68, 2.81, and 0.14 seconds, with peak resident sizes about 22.8, 59.0, and 19.5 MB, respectively. All new artifacts together are far below 200 MB. An attempted nice(10) in the environment check was denied by the sandbox; it is recorded in its output. No long-running or background computation was launched. The supplied author programs were read but not run.

### Critical sequences, computed from q and the disk formula

All examples use a genuine probability β on the positive integers and the q construction displayed in the (R) section. Then sum a_k=sum β_m/(m+1), sum k a_k=1, and Z sum(k-1)a_k=1. This tunes criticality exactly, including for infinitely many lacunary atoms.

For the regular examples choose

\[
\beta_m=\frac{\alpha\,\Gamma(m-\alpha)}{\Gamma(1-\alpha)\Gamma(m+1)},
\quad 0<\alpha<1,
\qquad \sum_m\beta_m r^m=1-(1-r)^\alpha.
\]

Here Z=1+α and J'(r)=Z(1-r)^α. The limiting α=1 law is β_1=1. Direct evaluation of the disk integral gives

\[
\nu(-k)=\tfrac12d(k-1)B(k,1+\alpha),\qquad
T(k)=kB(k,1+\alpha).
\]

The negative tail exponent is a=3/2+α. For α=1/2 there is the additional check ν(m)=ν(-m)=1/(4m²-1). For α=1 the construction is the critical quadrangulation law q_2=1/12, Z=2.

| Model | Definition of β | Z | Tail regime |
|---|---|---:|---|
| `type_2` | Sibuya α=1/2 | 1.5 | a=2 |
| `type_2.45` | Sibuya α=19/20 | 1.95 | near a=5/2 |
| `lacunary` | β_(16^j)=(3/5)(2/5)^j, j≥0 | 1.4587909095589306659138536681 | infinite sparse support; negative tail not regularly varying |
| `type_2.5` | β_1=1 | 2 | a=5/2 endpoint |

`audit_exact.py` obtains ν(m)=q_{m+1}c^m from the defining weights, obtains ν(-k) from the disk integral, and compares it to an independently evaluated positive-law expression for T(k). It uses quadrature for the regular laws and integrates each nonnegative monomial difference for the lacunary law. It tests k=1,2,3,8,31,100,1000. The maximum relative disk/kernel discrepancy over all four laws is 7.14×10^{-63} in 65-digit arithmetic.

For the three rational α values, harmonicity is checked **exactly with fractions** at p=1,2,3,4,8,16,32. To sum the infinite positive part, the program decomposes the rational function

\[
\frac{h(p+m)}{h(m+1)}=\prod_{j=1}^{p-1}\left(1+\frac1{2(m+j)}\right)
\]

into partial fractions and evaluates E_β[1/(m+j)] from the generating function of β. The finite negative part is computed from the disk integral. Every exact residual is zero. This avoids cutting off an infinite harmonic row and calling its deficit roundoff.

For the lacunary law, 170 atoms leave omitted β mass (2/5)^170=2.23975×10^{-68}. The harmonic-row residuals are at most 4.75×10^{-66}; the analytic omission bound used is (1+p) times that omitted mass, separate from arithmetic rounding. The total-mass check uses an independent integral of the central-binomial generating function. Its final mass residual is about 9.50×10^{-66}. The positive and negative masses are:

| Model | positive mass | negative mass |
|---|---:|---:|
| type 2 | 0.5 | 0.5 |
| type 2.45 | 0.655172413793103448 | 0.344827586206896552 |
| lacunary | 0.45786699315734060583 | 0.54213300684265939417 |
| type 2.5 | 2/3 | 1/3 |

### The lacunary example really tests nonregular negative tails

This is an infinite law, not a finite-support approximation passed off as irregular asymptotics. Put ρ=2/5. Directly from its positive definition,

\[
T(16p)=\rho T(p)+\frac{1-\rho}{1+16p}.
\]

With

\[
F(x)=(1-\rho)\sum_{\ell\in\mathbb Z}\frac{\rho^\ell16^\ell}{16^\ell+x},
\]

we have ρ^{-n}T(16^n x)→F(x). The program `audit_pathologies.py` gives

```text
F(4)/F(1)       = 0.6294238939688718810688257915365860756461
rho F(1)/F(4)   = 0.6355017720693361137986068547879839613972
sqrt(rho)      = 0.632455532033675866399778708887...
```

The first two numbers are different subsequential limits of T(4p)/T(p), along p=16^n and p=4·16^n. Their inequality is certified by **disjoint exact rational intervals**, of widths below 1.34×10^{-40}, using explicit geometric bounds on both tails of the bilateral series. Therefore T is not regularly varying. Multiplication by the smooth central-binomial factor shows ν(-p) is not regularly varying either. This tests the disputed generality rather than just a familiar power law.

The same program checks the infinite-log-moment example above. Its truncated positive expectations E_1 log h(P_1), summing the first J support points only, are:

```text
J= 5    1.2624948575835095428
J=10    2.3222784537112237804
J=20    4.4325999107266630917
J=40    8.6481976471283968533
J=80   17.076757572681634862
```

Their divergence is established analytically by the nonzero limiting summand, not inferred from these finite numbers.

### Inequality diagnostics

`audit_simulate.py` checks p=1,2,3,4,8,16,31,64,255,1024,4096. These finite diagnostics supplement the proofs above. Ratios are normalized as in Lemma 3.2; the (b),(c) denominators are p²R(p). For (d), the regular-law entries are valid computed upper bounds from the β survival function; the lacunary entries sum its weighted tail with negligible geometric remainder.

| Model | (a)/R | (b)/(p²R) | (c)/(p²R) | (d)/R, upper bound where indicated | K(B)/R | abs(E L)/R | E L²/R | δ/R | min b/R, p≥16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| type 2 | .7500 | .5000 | .5000 | 1.3294 | 1.5000 | .00762 | .15189 | .7500 | .06302 |
| type 2.45 | .67242 | .50687 | 1.2350 | 1.7282 | 1.9500 | .44688 | .27466 | .67242 | .07451 |
| lacunary | .79086 | .5000 | .69977 | 1.3994 | 2.1580 | .23685 | .15428 | .79086 | .05913 |
| type 2.5 | .66667 | .55403 | 1.3334 | 1.7725 | 2.0000 | .52146 | .29230 | .66667 | .07590 |

The required swallowing lower bound is only 1/256≈.00390625. The printed maxima and minima refer to this finite grid, not to a computer proof of universal constants.

### Perimeter paths and partial sums

The h-transformed chain is sampled without a perimeter or jump cutoff. The sampler first samples ν from an infinite mixture: choose M with law β and Q with Sibuya(1/2) law; return -Q with probability M/(M+Q), otherwise +M. The beta integral gives E[Q/(m+Q)]=1/h(m+1), so this has the required positive law and the independently checked negative law. For the h transform, use the envelope ν(j)+1{j>0}β_j/h(p), of total mass 1+1/h(p). The acceptance probability is h(p+j)/(h(p)+h(j+1)) for positive j, h(p+j)/h(p) for permitted negative j, and zero at p+j≤0. The envelope follows from decreasing increments h(r+1)-h(r)=d(r). Sibuya draws use a beta-geometric mixture. These are floating-point simulations of infinite-support laws, not certified exact random-bit sampling.

Each path starts at P_0=1. Write S_N=sum_{n=0}^{N-1}P_nν(-P_n). Three seeds were used for each law:

| Model | Seed | S_1000 | S_10000 | S_50000 | P_50000 | sum R through 50000 |
|---|---:|---:|---:|---:|---:|---:|
| type 2 | 1729 | 1.308294 | 1.405487 | 1.571636 | 69,247 | 4.998529 |
| type 2 | 2718 | 1.114139 | 1.231728 | 1.355314 | 61,621 | 4.184035 |
| type 2 | 31415 | .352006 | .530605 | 1.033383 | 47,350 | 3.148218 |
| type 2.45 | 1729 | 2.387212 | 2.918458 | 3.267277 | 2,169 | 10.388224 |
| type 2.45 | 2718 | 2.253443 | 3.429574 | 4.458083 | 2,680 | 15.090450 |
| type 2.45 | 31415 | 3.008617 | 4.719356 | 5.424105 | 806 | 18.372013 |
| lacunary | 1729 | 1.014068 | 2.119443 | 2.128382 | 16,863,599 | 6.813995 |
| lacunary | 2718 | .610244 | .865579 | 1.235262 | 532,276 | 3.746769 |
| lacunary | 31415 | 1.066490 | 1.066510 | 1.066600 | 4,292,103,698 | 3.081396 |
| type 2.5 | 1729 | 5.538982 | 6.952146 | 7.164471 | 2,278 | 22.381968 |
| type 2.5 | 2718 | 3.491479 | 4.572031 | 5.771545 | 1,052 | 18.371567 |
| type 2.5 | 31415 | 1.662180 | 2.005900 | 2.270211 | 1,635 | 7.050914 |

The nearly flat lacunary path after an early jump to around 2^32 is particularly instructive. A finite simulation could easily suggest convergence. These data neither establish nor refute almost-sure divergence; the localization proof establishes it. Complete checkpoint values, maximum perimeters, and relative-large-jump counts are saved in the JSON output.

## Corrections requested

1. **Line 123, change-of-variable equivalence:** state it for 0<g≤1. Treat g=0 directly or by continuity. As written the “if and only if” with y=gx is false at g=0, although the integral argument is unaffected.
2. **Lines 52, 88 and 282, algorithm and filtration:** explicitly require a peeling algorithm to be nonanticipating, and specify that F_n contains the selected edge before the next outcome. Alternatively adjoin the full independent auxiliary seed to the exploration filtration. State Lemma 5.1 for an F_n-measurable currently exposed edge/occurrence. This makes the stopping-time assertion for the position-indexed edges unambiguous.
3. **Line 293, numerical precision:** distinguish the high-precision kernel/harmonicity checks from the total-mass check. The supplied `kernel_check_out.txt` reports a total-mass residual of -2.22×10^{-16}, using a double-precision positive sum, whereas its harmonic residuals are about 10^{-41}. “The total mass and the harmonicity agree to the same accuracy” is ambiguous after the mixed precision statements. Report the two accuracies separately. This has no bearing on the proof.
4. **Lines 47–49 and bibliography, literature scope:** discuss Curien–Marzouk's work on roundish Markovian explorations separately from the swallowing-rate paper already cited as [CM]. The roundish paper is not listed under its own title. State the hypotheses of any comparison, particularly whether it assumes a regular/type regime. This is a literature clarification, not a replacement for Proposition 4.4.

No correction to Lemma 3.2(a)–(d), Lemma 4.3, or Proposition 4.4 is requested. In particular, do not replace the truncated martingale by a centered full log increment: that proposed simplification would introduce an actual error.

## Citation-use audit

The following assesses the use visible in the supplied text. It does not certify exact theorem numbers, quotations, or bibliographic details against unsupplied originals.

| Citation | Use in the paper | Assessment |
|---|---|---|
| Angel [Ang], line 39 | Historical introduction of peeling for UIPT | Background only; no mathematical inference in the proof depends on it. |
| Curien [Cur], Proposition 5 / Definition 9, line 71 | Admissibility and the two critical equations | These are the precise hypotheses used in the kernel derivation. No extra regularity is silently borrowed from this citation. |
| Curien [Cur], Lemma 11, lines 79–82 | ν is a probability and h is harmonic for the killed walk | Used in exactly this form for K and the reciprocal identities. The new examples check it independently, but they do not substitute for the general cited theorem. |
| Curien [Cur], Theorem 8, line 88 | Existence/law of the infinite critical map with boundary | A foundational external input. Nothing in the new proof verifies this construction anew. The claimed all-critical scope of this source should be checked against the cited version in an editorial source audit. |
| Curien [Cur], Section 4.2, lines 88–97 | Algorithm-independent spatial Markov peeling probabilities | Used for both the h-transform and the prescribed-side gluing events. The algebra retains its perimeter shifts and side factor. Applies to adapted choices with independent auxiliary randomness. |
| Curien [Cur], equation (5.3), lines 115–118 | Disk integral for q_g=(g^{k-1}q_k) | The central external enumeration input. The subsequent derivation is complete and independent of type assumptions. The formula's original equation number was not checked. |
| Curien [Cur], Corollary 27/open question; [CurLNM] | Motivation and comparison with the known type result | Not used circularly to prove exhaustion in the general case. The manuscript identifies a preliminary online version for numbering, but does not pin its date/version. The published book is a companion reference. |
| Budd [Bud], line 61 | Prior attribution of the negative-jump kernel in another normalization | The paper rederives the identity, so its validity here does not rely on a possibly different normalization in Budd. The priority/translation claim needs the original source for bibliographic confirmation. |
| Curien–Le Gall [CLG], line 47 | Previously known exhaustion for standard maps | Context only. No quantitative estimate from it enters the new proof. |
| Curien–Marzouk [CM], line 47 | Polynomial swallowing bound in standard maps | Context only. This is a swallowing-rate citation, not an explicit citation to the separate roundish-exploration work. |
| Jeulin [Jeu], lines 49 and 256 | Explaining the former scaling-limit route to the divergent series | Not invoked by the present proof. Thus no unverified independence or convergence-mode premise from that route is needed for (R). |
| Le Gall–Miermont [LGM], line 49 | Description of non-generic critical large-face models | Background; it supplies no hidden regularity hypothesis for the new argument. |
| Budd–Curien [BC] and Budd–Curien–Marzouk [BCM], line 49 | Geometry in type regimes, including a=2 | Background; no stated result is used to bridge the general case. |
| [code], Section 6 | Author computations | Finite checks are described as checks, not used as a proof of the all-q assertions. The provided mass output needs the precision clarification above. The described Lean file is not supplied in this directory, so its contents were not audited. |
| [MathBrainRepo], [MathBrainPaper], [BrainFramework] | Project description, acknowledgements and AI disclosure | No mathematical result from these is invoked. They do not support the theorem's proof. |

From my recollection, Curien and Marzouk's roundish-exploration results are relevant prior work on how arbitrary Markovian explorations cover metric neighborhoods in standard regular random-map regimes. Such coverage bears directly on exhaustion in those regimes. I do not recall a theorem from that work establishing the unrestricted oscillatory/lacunary critical case, and I cannot certify its full hypotheses from the materials here. It should be compared explicitly, but it supplies neither a demonstrated counterexample to this paper nor an audited substitute for its general rate argument.

Task: “You are refereeing a mathematical paper that has been posted” — 14 November 2026, 00:25:40 +04, the first local timestamp recorded by this audit.
