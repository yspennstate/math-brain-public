Overall verdict: SOUND WITH GAPS

The continuous-time conclusions on even cycles are correct, and I found no counterexample to them. The posted proof needs repairs in its stopped comparison arguments and in its application of the martingale array CLT. The abstract must also distinguish this asynchronous process from the synchronous discrete-time urn studied by Chen–Lucas and Lima: the paper proves no transfer of the limit law to that model.

There is a substantially stronger independent check. With unit initial counts, the alternating terminal charge on an even cycle has the **exact** characteristic function

\[
 \mathbb E e^{i\theta M_\infty}
 =\left(\frac{\pi\theta}{\sinh(\pi\theta)}\right)^{L/2}.
\]

Thus it is a sum of \(L/2\) independent standard logistic random variables. In particular the paper's constant is exactly \(c=\pi^2/6\), rather than an unidentified constant estimated as 1.64. Proofs below establish this without using the authors' programs or the claimed CLT. This strengthening is not needed to excuse any missing argument: I give the missing arguments separately.

Line references are to `PAPER.tex`. Results are identified by their LaTeX labels; the source uses one shared theorem counter, rather than section numbering such as “Theorem 2.1.”

## 1. The charge martingale, `thm:mart` (§2, lines 42–72): SOUND

The model is understood to be a finite, loopless graph, with isolated vertices either absent or ignored. At state \(n\), the rate of an increment of edge \(e=uv\) is

\[
 r_e(n)=n_e(S_u^{-1}+S_v^{-1}).
\]

Lines 53–55 give the correct increment \(\sigma_e/n_e\), conditional mean, and conditional second moment. The generator is

\[
 \mathcal A M_\sigma(n)=\sum_v\frac{(B\sigma)_v}{S_v}.
\]

It vanishes for \(B\sigma=0\). The displayed predictable bracket is therefore correct. Counts in a stochastic-integral integrand are evaluated before the jump; this does not affect its displayed Lebesgue integral.

**These are true martingales.** The total number of rings before a fixed deterministic time \(T\) is Poisson with mean \(|V|T\), and the integrand of each compensated marked-clock integral is bounded by \(\|\sigma\|_\infty\). Its squared-integrand intensity on \([0,T]\) is bounded by \(|V|T\|\sigma\|_\infty^2\). Hence the compensated integrals are square integrable, not merely local martingales. An unbounded random number of rings causes no integrability problem. Simultaneous rings have probability zero.

There is also a stronger all-time bound, missing from the paper. Write \(H^{(p)}(m)=\sum_{j=1}^m j^{-p}\). Every reinforcement visits the next integer count exactly once, so pathwise

\[
 [M_\sigma]_t=\sum_e\sigma_e^2 H^{(2)}(N_e(t)-1)
 \le \zeta(2)\sum_e\sigma_e^2. \tag{A}
\]

Consequently \(M_\sigma\) is uniformly bounded in \(L^2\), converges almost surely and in \(L^2\), and its terminal mean is zero. Once every edge diverges, (A) gives

\[
 \mathbb E M_{\sigma,\infty}^2
 =\mathbb E\langle M_\sigma\rangle_\infty
 =\zeta(2)\sum_e\sigma_e^2. \tag{B}
\]

This is stronger than the almost-sure bracket finiteness proved later. Merely knowing that a local martingale has finite terminal bracket almost surely would not, by itself, establish a zero terminal mean; (A) supplies the required uniform integrability.

The rank formula and the characterization by even cycles/two distinct odd cycles in a component (lines 59–61) are correct for finite loopless graphs. Summing the vertex constraints gives \(2\sum_e\sigma_e=0\). The digamma identity, its sign, and the asymptotic error in lines 61–65 are correct. In particular, no term involving \(\log t\) or Euler's constant survives.

Lines 66–67 correctly describe conservation under the ODE, with \(S_v\) there interpreted as \(S_v(x)\). Lines 69–72 correctly simplify the bracket on the even cycle to \(\int\sum_v (N_{v-1}N_v)^{-1}dt\).

For a vector outside the kernel, the drift is the generator displayed above, and generally is nonzero. Importantly, zero **unconditional** mean is not a test of the martingale property. On \(C_4\), \(\sigma=(1,-1,0,0)\) has mean-zero charge at every time by rotation symmetry, but at the reachable state \((2,1,1,1)\) its drift is \(-1/6\). It is not a martingale.

For an arbitrary vector, subtracting the integral of that drift gives a true compensated martingale, with the same predictable bracket integrand. The uncorrected charge need not be conserved.

## 2. Edge growth, `lem:growth` (lines 75–89): GAP, with a routine stopped-comparison fix

The asserted lower growth bound is correct. The estimate
\(S_v(t)\le d+\sum_{w\in\{v\}\cup N(v)}F_w(t)\)
and the resulting eventual rate bound \(r_e\ge\lambda' N_e/t\) are correct. A Yule process with rate \(\lambda'\), in logarithmic time, has a strictly positive normalized terminal value. Taking \(\lambda<\lambda'\) proves the stated positive liminf, in fact a stronger eventual bound.

The issue is that the “a.s. finite \(T\)” selected using a bound that holds **for every future time** is not necessarily a stopping time. One cannot condition at that \(T\) and simply call the ensuing comparison an ordinary fresh Yule process.

**Fix:** for each deterministic integer \(m\ge1\), construct a fresh lower Yule comparison starting at time \(m\) with count 1, and stop its domination at the first violation of the required denominator bound. On the event that the bound holds for all \(t\ge m\), the comparison is never stopped. For each deterministic \(m\), its Yule limit is positive almost surely. Intersect these probability-one events over the integers; the Poisson strong law ensures that at least one \(m\) has no violation. This proves the claim without conditioning on a future-dependent random time.

For the last assertion take a positive \(\lambda<2/(d+1)\). Since \(S_v\ge F_v\sim t\), each vertex's bracket integrand is \(O(t^{-1-\lambda})\), and the graph is finite. The integral near zero is bounded as well. Thus the claimed almost-sure finiteness follows. Identity (A) gives an independent and stronger integrability proof for the bracket.

## 3. Equilibria, `lem:eq` (lines 101–122): SOUND

The state space here must include \(x_e\ge0\), as is implicit in the urn/ODE formulation. The classification is correct on that state space.

For an interior equilibrium, neighboring vertex sums satisfy \(1/s+1/s'=1\). The mass constraint gives \(s+s'=4\); together these give \(ss'=4\), and hence \(s=s'=2\). Solving \(x_{v-1}+x_v=2\) gives exactly the stated segment.

At a boundary equilibrium, no two consecutive edges can be zero, because every \(S_v\) is positive. Thus maximal positive blocks really are paths separated by single zero edges. Direct substitution in the path recurrence gives

\[
 x_{2i}=i(s'-s),\qquad x_{2i+1}=s-i(s'-s).
\]

For an odd block the endpoint equation forces \(s=s'\); all lengths greater than one would then contain an internal zero edge, contradicting maximal positivity. The sole allowed odd block is one edge of weight 2. For an even block of length \(k\), the endpoint equation gives \(s'-s=2s/k\), and the reciprocal equation gives \(s=(2k+2)/(k+2)\). All the displayed block weights are positive.

There are finitely many supports and at most one such configuration for each proper support. A zero edge next to an even block has derivative at least \(1/(2k+2)\ge1/(2L)\), because the sum at its other endpoint is at most 2. If there are no even blocks, the configuration is precisely a segment endpoint. The claimed finiteness and transverse positive derivative follow.

The Lyapunov value on the whole segment is \(L\log2-L\). There are only finitely many other equilibria, so its values on equilibria form a finite set. This particular hypothesis needed later is genuinely verified, rather than assumed from strict monotonicity alone.

`analytic_checks.py` also checks the block formula, total mass, all equilibrium equations, and the derivative bound by exact rational arithmetic on every admissible support for \(L=4,6,10\).

## 4. Convergence and charge identification, `thm:conv` (lines 92–99, 124–146): GAP, fillable

The conclusion, including exclusion of both endpoints, is correct. The following details complete the proof.

**Normalization and stochastic approximation.** With \(X=N/t\), for \(t>0\), the exact semimartingale decomposition is

\[
 dX_e(t)=\frac{F_e(X(t))}{t}\,dt+\frac{dK_e(t)}{t},\qquad
 F_e(x)=x_e\left(\frac1{S_u(x)}+\frac1{S_v(x)}-1\right),
\]

where \(K_e\) is the compensated count. Thus logarithmic time gives exactly the stated ODE, with no missing normalization factor. Total mass tends to \(L\) by the Poisson strong law, and the ODE mass equation is \(\dot s=L-s\).

Eventually \(X\) is in the indicated compact set \(K\), with nonnegative coordinates understood. The field is smooth in a neighborhood of \(K\) inside \(\{S_v>0\}\). The set is also forward invariant: at \(S_v=1/2\), \(\dot S_v=1-S_v+\text{nonnegative}>0\), and at total mass \(2L\), the mass derivative is negative. Nonnegative coordinates remain nonnegative.

On any bounded logarithmic-time window starting at \(\tau\), the noise has expected quadratic variation at most \(C e^{-\tau}\); total ring rate is \(L\). Doob's inequality and Borel–Cantelli on integer \(\tau\) give uniform almost-sure vanishing of the noise on such windows. Jump sizes also vanish. Interpolating the jumps if necessary gives an asymptotic pseudotrajectory of the smooth flow. This supplies the noise hypothesis needed for Benaïm, rather than merely asserting an almost-sure \(O(t^{-1/2})\) rate.

**Lyapunov step.** Direct differentiation gives
\(\dot{\mathcal L}=\sum_e x_e(\partial_e\mathcal L)^2\).
It is strictly positive away from equilibria, including in the allowed boundary faces. Benaïm's internally chain transitive limit-set conclusion and the Lyapunov criterion apply: the equilibrium Lyapunov values have empty interior because they form a finite set. The limit set is therefore a connected subset of equilibria. By the classification, it lies in the segment or is a single isolated point of type (2). All hypotheses used at lines 131–134 can be supplied as above.

**Exclusion of type (2).** Line 138 literally starts the comparison at the stopping time of *leaving* the neighborhood, then argues on the event of never leaving. That is not a valid formulation. Start at a deterministic integer \(m\), and kill the comparison at the first exit instead. In a sufficiently small neighborhood, the edge in question has rate at least \((1+\delta)N_e/t\). The lower logarithmic-time Yule comparison has a positive normalized limit. On never exiting, it forces \(N_e\ge C t^{1+\delta/2}\), contradicting both convergence to the equilibrium and the linear upper growth of the total count. Take the countable union over deterministic \(m\) and the finite set of type (2) points. This is the required repair.

**Terminal charge and boundary exchange.** Almost-sure finiteness of the bracket gives convergence of the local martingale after localization; alternatively (A) gives the stronger \(L^2\) convergence directly. Edge growth makes the digamma error in (63) vanish for the fixed finite cycle. Therefore
\(\Phi(X(t)):=\sum_e(-1)^e\log X_e(t)\to M_\infty\).

One must not simply substitute a boundary limit into a discontinuous logarithm. Along a subsequence approaching \(x^{(1)}\), every even coordinate tends to 2 and **every** odd coordinate tends to zero. Hence \(\Phi\to+\infty\), with no cancellation among divergent terms. At \(x^{(-1)}\) it tends to \(-\infty\). Both contradict finite \(M_\infty\). Every remaining limit point is interior, where continuity legitimately gives

\[
 \Phi(x^{(u)})=\frac L2\log\frac{1+u}{1-u}=L\operatorname{artanh}u.
\]

This is strictly increasing, so the limit set contains only one point. This establishes convergence and the precise charge identity without interchanging an unjustified limit at the boundary.

## 5. The numbered Birch/fibre remark (lines 148–153): GAP in the general convergence extension; fibre assertion SOUND

The stated map on \(P=\{x>0:Bx=b\}\) is a bijection provided \(P\) is nonempty. Its closure is compact: \(2\sum x_e=\sum b_v\). For \(m\in\ker B\), minimize

\[
 \sum_e x_e(\log x_e-1)-m\cdot x
\]

over the closed fibre. Strict convexity gives uniqueness. A minimizer is positive, since moving toward any positive feasible point has derivative \(-\infty\) at a zero coordinate. The first-order condition is exactly \(\operatorname{proj}_{\ker B}\log x=m\), proving surjectivity. Injectivity also follows from
\(\sum_e(x_e-y_e)(\log x_e-\log y_e)>0\) for distinct positive \(x,y\).

This verifies the substance of the invoked convex-duality/Birch fact independently. For a general unsigned graph incidence matrix this need not be an ordinary bipartite transportation polytope; the terminology is broader than the usual one.

The introductory “same argument applies whenever” is not, by itself, a proved general convergence theorem. One also needs the compactness/Lyapunov hypotheses and an exclusion argument for the entire possible boundary limit set. Repulsion at each point is not automatically the particular single-equilibrium comparison used on the cycle. **Fix:** retain the proved fibre bijection as a separate remark, and either restrict the convergence extension to the hypotheses actually verified here (in particular isolated competing boundary equilibria with the stated growth comparison), or state and prove an appropriate unstable-set exclusion result. This does not affect the cycle theorem.

## 6. Uniform tails, `lem:tail` (lines 159–183): SOUND; clarify the stopped Yule step

The initial reciprocal bound is valid, though deliberately loose. The marked-clock construction of \(\widetilde N_e\) is monotone: if the lower count is dominated immediately before a ring, its acceptance interval is contained in the actual edge's acceptance interval. Each lower edge process uses only the four stated clocks. The joint expression for the two adjacent lower counts uses five distinct clocks, whose law is independent of \(L\ge6\). No independence between the lower count and \(F_v\) is assumed or needed in Cauchy–Schwarz.

The Poisson bound \(\mathbb E(F_v\vee1)^{-2}\le Ct^{-2}\) holds for large \(t\). Also \(\widetilde N^{-2}\le\widetilde N^{-1}\). Thus an inverse-count bound \(O(t^{-a})\), with any \(a>0\), is sufficient.

For the last paragraph, interpret all clock quantities predictably at rings and stop the comparison when a denominator bound fails. Poisson exponential bounds give
\(\mathbb P(\sup_{r\ge\sqrt t}\max(G_v(r),G_{v+1}(r))/r>4)\le Ce^{-c\sqrt t}\).
The two endpoint clocks, each with acceptance probability \(\widehat Y/(4r)\), give logarithmic-time birth rate \(\widehat Y/2\) **until the cap is hit**.

The geometric formula is for an uncapped Yule process, not automatically for the entire capped process. The justification for using it is to couple an uncapped process identically until the first cap crossing. On no crossing their terminal values agree. On a crossing at \(r\ge\sqrt t\), monotonicity gives \(\widehat Y(t)\ge4\sqrt t\). Splitting those two events yields exactly the extra \((4\sqrt t)^{-1}\) term in line 182. Thus the displayed bound is valid; one must retain this cap-crossing term.

Cauchy–Schwarz consequently bounds the expected reciprocal-product integrand by
\(C t^{-9/8}\sqrt{\log t}\), plus an integrable exponentially small term. This proves a uniform integrable envelope and hence the asserted tail limit. The same local proof works on \(\mathbb Z\). For \(C_4\) the pair of lower processes has a different joint clock identification, but each individual lower edge still uses four distinct clocks and has the same inverse-moment estimate. Applying Cauchy–Schwarz separately to the two terms extends the tail expectation bound to that cycle too, if wanted.

## 7. Finite-time locality, `lem:local` (lines 185–198): SOUND

The graphical construction is valid. A causal path reaching distance \(R\) needs an ordered chain of at least \(R\) nearest-neighbor ring events. Counting spatial paths and integrating their ordered times gives a factorial tail of the stated form, with harmless shifts of the initial radius for the two incident edges. This bound tends to zero for each fixed \(T\), and also constructs the infinite-line process without a finite-time infinite causal ancestry.

For a precise independence argument, replace \(Q_v^{\le T}\) by its version computed using only clocks/marks in its radius-\(R\) neighborhood, with fixed boundary data. These replacements are genuinely independent for disjoint neighborhoods and differ from the full quantities only on the exceptional causal-path event. Since the quantities are bounded by \(T\), the expectation and covariance bounds follow. Choose \(L>2R+2\) before coupling the neighborhood to the line; use cycle distance in the covariance count. The stated variance bound, or the same bound with an immaterial absolute constant, tends to zero by first sending \(L\) and then \(R\) to infinity.

Monotonicity of \(q(T)\) is immediate. The preceding uniform tail argument on the line proves finiteness of its limit. Moreover the following identity identifies it exactly. Let \(A_e(t)=H^{(2)}(N_e(t)-1)\). Its generator is

\[
 \mathcal A A_0=\frac1{N_0S_0}+\frac1{N_0S_1}.
\]

Translation invariance changes the second expected term into \(\mathbb E[1/(N_{-1}S_0)]\), so

\[
 q(T)=\mathbb E H^{(2)}(N_0(T)-1).
\]

Every fixed edge of the line diverges: the local denominator bound in the growth proof only needs its finitely many neighboring clocks. Thus bounded convergence gives

\[
 c=\lim_{T\to\infty}q(T)=\zeta(2)=\pi^2/6. \tag{C}
\]

The proof using these two lemmas really does give \(L^1\), not just convergence of expectations: for fixed \(T\), apply the finite-time \(L^2\) result, and bound the nonnegative discarded spatial tail in \(L^1\) by \(\varepsilon(T)\), as well as \(c-q(T)\). Then send \(T\to\infty\).

## 8. Gaussian limit, `thm:clt` (lines 200–213): GAP in the cited-array application; conclusion SOUND

The bracket limit and the jump bound are the right conditions for a continuous-time martingale CLT, but Hall–Heyde's martingale-difference array theorem requires an array and a **conditional variance** check. The text supplies neither a finite-row reduction of the infinite time horizon nor identification of that conditional variance with the displayed continuous-time bracket. This is fillable, not a counterexample.

Here is a particularly short independent fix. List all vertex rings of a cycle, let \(D_{L,j}\) be the corresponding charge increment divided by \(\sqrt L\), and use the embedded-chain filtration before each ring. These are martingale differences and \(|D_{L,j}|\le L^{-1/2}\). By edge divergence and (A),

\[
 \sum_{j\ge1}D_{L,j}^2=\zeta(2)\quad\text{almost surely}.
\]

Let \(A_L=\sum_j\mathbb E(D_{L,j}^2\mid\mathcal F_{j-1})\). The differences between the squares and their conditional expectations are orthogonal martingale differences, and

\[
 \mathbb E\left|A_L-\zeta(2)\right|^2
 \le\sum_j\mathbb E D_{L,j}^4
 =\frac{\zeta(4)}L. \tag{D}
\]

Thus the required conditional variance converges to \(c\) in probability, indeed in \(L^2\). Lindeberg is automatic from the deterministic jump bound. For each \(L\), choose a deterministic finite number of rings \(k_L\) so the expected remaining sum of squares is at most \(1/L\). The omitted martingale tail then tends to zero in \(L^2\), and the omitted conditional variance tends to zero in \(L^1\). Hall–Heyde now applies to the finite rows. This supplies all the missing array conditions.

There is also an exact audit of the paper's **continuous-time predictable** bracket. The martingale \(R=[M]-\langle M\rangle\) has
\([R]_\infty=\sum_e H^{(4)}(N_e(\infty)-1)=L\zeta(4)\).
It is uniformly square integrable. Since \([M]_\infty=L\zeta(2)\) is deterministic,

\[
 \mathbb E\langle M\rangle_\infty=L\zeta(2),\qquad
 \operatorname{Var}(\langle M\rangle_\infty)=L\zeta(4),\qquad
 \mathbb E\left|\frac{\langle M\rangle_\infty}{L}-c\right|^2
 =\frac{\zeta(4)}L. \tag{E}
\]

This independently proves the claimed bracket convergence, more strongly than \(L^1\), without any locality argument. Together with (C) it checks that the line constant is the same one.

The final passage from the charge to \(\sqrt L\operatorname{artanh}u_\infty\) uses the already proved fixed-cycle identity and is valid. The stated rate is \(u_\infty=O_{\mathbb P}(L^{-1/2})\); in fact \(\sqrt L u_\infty\) has the same Gaussian limit. Equation (B) supplies the terminal means and second moments at line 212, including \(L=4\), which the stated tail lemma alone did not cover.

## Independent checks and programs

### Exact terminal law: two independent derivations

First, construct independent rate-\(n\) Yule processes \(Y_e\), starting from one, and give edge \(e=uv\) internal time
\(a_e(t)=\int_0^t(S_u^{-1}+S_v^{-1})ds\).
The random time-change construction \(N_e(t)=Y_e(a_e(t))\) has exactly the urn's transition rates. Every \(a_e\) tends to infinity because every count diverges. The independent Yule limits \(e^{-s}Y_e(s)\to W_e\) are independent \(\operatorname{Exp}(1)\) variables. For a kernel vector, \(\sum_e\sigma_e a_e(t)=0\). Therefore

\[
 M_{\sigma,\infty}\ \stackrel d=\ \sum_e\sigma_e\log W_e,
 \qquad
 \mathbb E e^{i\theta M_{\sigma,\infty}}=\prod_e\Gamma(1+i\theta\sigma_e). \tag{F}
\]

Second, this formula can be checked without a time-change independence argument. For real \(\theta\), define

\[
 P_\theta(n)=\prod_e\frac{\Gamma(n_e+i\theta\sigma_e)}{\Gamma(n_e)\Gamma(1+i\theta\sigma_e)}.
\]

An increment of edge \(e\) multiplies this by \(1+i\theta\sigma_e/n_e\), so its generator is zero by the kernel constraint. It is a bounded complex martingale, since its modulus is bounded by
\(\prod_e\prod_{k\ge1}(1+\theta^2\sigma_e^2/k^2)^{1/2}<\infty\).
Gamma-ratio asymptotics, edge divergence, and dominated convergence give (F) from \(\mathbb E P_\theta=1\).

For alternating signs, the gamma reflection identity gives the characteristic function at the start of this report. This yields an ordinary independent-sum CLT as another verification of Theorem `thm:clt`. For \(Z_L=M_\infty/\sqrt L\),

\[
 \operatorname{Var}Z_L=\pi^2/6\quad\text{for every even }L,
 \qquad \text{excess kurtosis}(Z_L)=\frac{12}{5L}.
\]

Thus there is no finite-size variance correction for the *terminal charge*. The departures from a Gaussian are in its shape: excess kurtosis is 0.6, 0.4, 0.24, 0.12, and 0.048 for \(L=4,6,10,20,50\).

For \(C_4\), put \(p=(1+u_\infty)/2\). Convolution of two logistic densities gives the charge density

\[
 f_M(s)=\frac{s\coth(s/2)-2}{4\sinh^2(s/2)},\qquad f_M(0)=1/6,
\]

and integration yields

\[
 \operatorname{Var}p=\frac{\pi^2}{32}-\frac14=0.0584251375\ldots.
\]

For an algebraic check, the change of variable \(u=\tanh(s/4)\) gives
\(\mathbb E u^2=\int_0^1(u^{-1}-u^3)\operatorname{artanh}u\,du-2/3=\pi^2/8-1\): the two integrals are \(\pi^2/8\) and \(1/3\), by their convergent power series.

`analytic_checks.py` checks this by independent high-precision quadrature and the closed expression. It also samples the exact terminal law directly, independently of the urn simulator. The actual \(C_4\) law is not a symmetric beta law: its density near \(p=1\) has a \((1-p)\log(1/(1-p))\) factor, whereas a beta density has a pure power. Merely fitting a variance does not establish this distinction.

### Exact finite-state and continuous-time martingale checks

`exact_checks.py` uses `fractions.Fraction`, enumerates every count state after a fixed number of rings, checks the generator at every such state, and separately computes the second moment, the expected embedded predictable variance, and the optional variation from harmonic squares. It also computes continuous-time values by a Poisson mixture. For the continuous predictable bracket, it independently integrates over the conditional uniform event times: conditional on \(k\) rings, all \(k+1\) gaps have mean \(t/(k+1)\). Explicit Poisson-tail error bounds are printed in `exact_checks.txt`.

The odd-cycle test graph is \(K_4\), not a triangle with a vacuous zero kernel. With edge order \((01,02,03,12,13,23)\), the tested nonzero kernel vector is \((1,-1,0,0,-1,1)\). The triangle alone has no nonzero kernel vector.

At six rings the exact second moments are 3.48036540216 on \(C_4\) and 2.64049751848 on \(K_4\); in each case the exact rational difference from both computed expected variations is zero. The enumeration extends to 14 rings/680 states on \(C_4\), and 12 rings/6,188 states on \(K_4\).

At continuous time \(t=0.25\), the following are independent exact/Monte Carlo checks. Each Monte Carlo entry is based on 100,000 replicas; “±” denotes one estimated standard error, not a confidence interval. The exact predictable-bracket truncation errors are below \(3.1\times10^{-13}\) and \(6.4\times10^{-11}\), respectively.

| Graph | Exact \(\mathbb E M\) | Exact \(\mathbb E M^2=\mathbb E\langle M\rangle\) | Simulated \(\mathbb E M\) | Simulated \(\mathbb E M^2\) | Simulated \(\mathbb E\langle M\rangle\) |
|---|---:|---:|---:|---:|---:|
| \(C_4\) | 0 | 0.887373431 | 0.00210 ± 0.00298 | 0.88864 ± 0.00410 | 0.887404 ± 0.000382 |
| \(K_4\) | 0 | 0.609193340 | 0.00240 ± 0.00247 | 0.60813 ± 0.00315 | 0.609235 ± 0.000204 |

These tests support the theorem on both a bipartite graph and a graph containing odd cycles. They do not replace the integrability proof above.

### Independent cycle simulation and finite-size effects

`independent_sim.c` is a new, single-threaded Gillespie implementation, using PCG32 rather than the authors' RNG. It chooses a uniformly random ringing vertex and then an incident edge with the correct current probability. It draws the exact exponential holding time, stops before the first event beyond the requested horizon, and integrates the **full pre-jump bracket rate over the holding time**. Only the two affected vertex terms need updating. The optional variation is separately accumulated from squared actual charge jumps. `synchronous_sim.c` implements a separate, simultaneous-update urn and is not used for the continuous-time checks.

Raw outputs are `cycles*_t*.csv`, `smallgraph_C4.csv`, `smallgraph_K4.csv`, `line32768.csv`, and `synchronous*.csv`. `summarize_checks.py` produces `simulation_summary.txt`; `run_checks.sh` records a serial reproduction recipe. Numerical Python library thread counts are set to one. No authors' executable or source code was reused.

Define \(Z_T=M(T)/\sqrt L\), the count projection \(\widehat u_T=L^{-1}\sum_e(-1)^eN_e(T)/T\), and

\[
 r_T=\left[L^{-1}\sum_e\{N_e(T)/T-1-(-1)^e\widehat u_T\}^2\right]^{1/2}.
\]

The table gives empirical standard deviations/errors across independent runs. The residual column is \((\mathbb E_{\rm sample}r_T^2)^{1/2}\), so it measures failure of the actual counts to be a pure alternation, not a quantity defined from the charge.

| \(L\) | \(T\) | Runs | \(\operatorname{Var}Z_T\), ± s.e. | Mean \(\langle M\rangle_T/L\), ± s.e. | Alternation residual |
|---:|---:|---:|---:|---:|---:|
| 4 | 1,000 | 20,000 | 1.6476 ± 0.0187 | 1.64426 ± 0.00369 | 0.0810 |
| 6 | 1,000 | 10,000 | 1.6726 ± 0.0259 | 1.64696 ± 0.00430 | 0.1822 |
| 10 | 1,000 | 6,000 | 1.6148 ± 0.0303 | 1.64259 ± 0.00425 | 0.2895 |
| 20 | 1,000 | 3,000 | 1.6460 ± 0.0445 | 1.63625 ± 0.00417 | 0.3601 |
| 50 | 1,000 | 2,000 | 1.6143 ± 0.0518 | 1.63899 ± 0.00329 | 0.3995 |
| 100 | 1,000 | 1,000 | 1.6141 ± 0.0699 | 1.64029 ± 0.00321 | 0.4087 |
| 400 | 1,000 | 1,200, pooled | 1.4903 ± 0.0604 | 1.64465 ± 0.00145 | 0.4184 |
| 4 | 10,000 | 2,000 | 1.5993 ± 0.0539 | 1.63844 ± 0.01142 | 0.0461 |
| 6 | 10,000 | 2,000 | 1.6617 ± 0.0558 | 1.64525 ± 0.00924 | 0.1255 |
| 10 | 10,000 | 1,000 | 1.5569 ± 0.0753 | 1.64442 ± 0.01075 | 0.2502 |
| 20 | 10,000 | 500 | 1.6246 ± 0.1076 | 1.64117 ± 0.01055 | 0.3283 |
| 50 | 10,000 | 400 | 1.5997 ± 0.1104 | 1.64183 ± 0.00769 | 0.3771 |
| 100 | 10,000 | 1,200, pooled | 1.6626 ± 0.0688 | 1.64742 ± 0.00295 | 0.3893 |

The theoretical terminal variance is 1.644934 for **every** row. At \(T=1000\), the count-based estimate of the missing variance of \(Z\) is about 0.0021–0.0025; at \(T=10000\) it is about 0.0002. This follows from the exact isometry

\[
 \mathbb E\{(M_\infty-M_T)/\sqrt L\}^2
 =\zeta(2)-\mathbb E[M]_T/L.
\]

Consequently the distribution of the terminal charge is already well approximated, even while the counts are not yet close to the segment on large cycles. For example, the \(L=50\) residual falls only from 0.3995 to 0.3771 when time increases tenfold. The simulations support convergence of the shape for small cycles, but they plainly do not exhibit a fully equilibrated \(C_{50}\), \(C_{100}\), or \(C_{400}\). This is consistent with the slow near-alternating ODE modes, not evidence against the fixed-cycle theorem.

I retained the low \(L=400\) variance rather than discarding it: the initial 200-replica batch gave 1.2153; a separate 1,000-replica seed gave a pooled 1.4903. This remains low by about 2.5 empirical standard errors. Its predictable variation does not show that deficit. A second implementation/RNG diagnostic is recorded below; the exact moment identities, not a favorable Monte Carlo sample, are the load-bearing verification.

For normality, the \(T=1000\) measured excess kurtoses at \(L=4,6,10,20,50\) are 0.574, 0.399, 0.118, 0.202, 0.064; the exact terminal values are 0.600, 0.400, 0.240, 0.120, 0.048. Small-cycle nonnormality is detectable: the Kolmogorov distance of \(Z_T\) from \(N(0,\pi^2/6)\) is 0.01695 for \(L=4\) (20,000 runs, unadjusted KS \(p\approx2.0\times10^{-5}\)), 0.01527 for \(L=6\), and 0.01420 for \(L=50\) (2,000 runs, \(p\approx0.81\)). These are descriptive, multiple comparisons, not a collection of independent acceptance tests. The exact kurtosis formula quantifies the finite-size departure more reliably. `analytic_checks.py` separately generates 200,000 samples of the exact terminal law for each tested size through \(L=400\).

### Does the measured limit parameter satisfy the charge identity?

Reading \(u\) from \(\tanh(\sum(-1)^e\log X_e/L)\), as the authors do, cannot independently check that the counts have reached an alternating limit: that identity is a definition at finite time. I checked both the count projection \(\widehat u_T\) and the logarithmic/harmonic charge difference.

| \(L\) | RMS of \(\sum(-1)^e\log X_e-M_T\), \(T=1000\) | Same, \(T=10000\) | RMS of \(L\operatorname{artanh}\widehat u_T-M_T\), \(T=10000\) |
|---:|---:|---:|---:|
| 4 | 0.01900 | 0.000870 | 0.275 |
| 6 | 0.02423 | 0.003168 | 0.495 |
| 10 | 0.03081 | 0.002796 | 0.758 |
| 20 | 0.03934 | 0.002523 | 1.223 |
| 50 | 0.06040 | 0.002969 | 2.272 |

All \(T=10000\) projections in these rows lie in \((-1,1)\), so none were excluded. At \(T=1000,L=4\), two of 20,000 projections fall outside that interval because of finite-time count/mass fluctuations; the program reports that rather than clipping them. The much larger count-projection discrepancy is exactly the distinction between an unequilibrated count projection and the charge parameter. It decreases with time but must not be confused with the vanishing digamma error.

For \(L=100,T=10000\), the pooled 1,200-run harmonic/log RMS is 0.02416, versus the paper's 0.007. The absolute-error median, 90th percentile, 99th percentile, and maximum are 0.00119, 0.00548, 0.05704, and 0.58236. A single largest observation contributes roughly 48% of the squared-error sum, so this RMS is very sampling-sensitive; its plug-in delta-method standard error is approximately 0.0062 and is itself unstable. I did **not** reproduce 0.007 as an ensemble RMS. This is a numerical qualification requiring uncertainty and more information about the authors' sample, not a contradiction to the harmonic/log identity.

For \(C_4\), the measured variance of the charge-based \((1+\tanh(M_T/4))/2\) is 0.05835 at \(T=1000\), agreeing with the exact terminal 0.0584251. The variance of the actual finite-time count statistic \((X_0+X_2)/4\) is only 0.05453, and at \(T=10000\) it is 0.05581. Thus the paper's 0.0564 is plausible as a noisy or incompletely equilibrated count measurement; it is not a justified estimate with the displayed precision of the terminal variance. Its implied beta parameter 1.72 likewise differs from the exact moment-matched parameter 1.63949.

The authors' large-cycle variance and mean-bracket entries, unlike the harmonic/log RMS, are consistent with the exact references and my sampling uncertainties. For example their variances 161.6 at \(L=100,R=400\), 620 at \(L=400,R=200\), and 154.9 at \(L=100,R=200\) are all ordinary Monte Carlo deviations around terminal variances 164.49, 657.97, and 164.49. Their bracket estimator is near the correct mean even though its name in the code is inaccurate.

### Independent estimate from the infinite-line process

`independent_sim.c line 32768 1000 16 9918273 8192` simulates a **path**, with 32,768 vertices and rate-one clocks, retaining the central 16,384 vertex integrals and discarding 8,192 vertices at either end. These are 16 independent finite-volume realizations, not a claim to simulate infinitely many clocks. At the maximum time, the causal-chain bound for distance 8,191 has \(\log_{10}\delta<-1460\). Even a union bound over every retained target in all realizations gives a boundary-error probability below \(10^{-1450}\). Hence finite-volume error is negligible here, with a quantitative justification independent of an assumed mixing length.

The standard errors below use the 16 independent **realizations**, allowing arbitrary spatial dependence within each one.

| \(T\) | Direct spatial/replica estimate of \(q(T)\), ± s.e. | Count-based estimate of expected remaining tail |
|---:|---:|---:|
| 1 | 0.655167 ± 0.000524 | 0.989881 |
| 10 | 1.452845 ± 0.001701 | 0.190992 |
| 100 | 1.621989 ± 0.001814 | 0.021292 |
| 1000 | 1.641192 ± 0.001814 | 0.002182 |

The tail estimate uses the separately computed central-edge average of \(\zeta(2)-H^{(2)}(N_e(T)-1)\), whose expectation equals the missing line integral by (C). At \(T=1000\), direct integral plus this tail is 1.643374 ± 0.001800, consistent with the independently derived \(c=1.6449340668\). The raw integral alone underestimates the terminal constant, as it must. Neither the tail correction nor the simulation assumes convergence of \(N_e(t)/t\) on the infinite line.

### Synchronous comparison and a second urn implementation

`synchronous_sim.c` uses a distinct RNG and copies all choices for a round before modifying any count. On the dual \(C_4\), 10,000 runs of 2,000 synchronous rounds give variance 1.25724 ± 0.02124 for the logarithmic charge divided by \(\sqrt4\), compared with the continuous-time terminal value 1.64493. On \(C_{100}\), 1,000 runs of 1,000 rounds give 1.33457 ± 0.05794. These are finite-time comparisons, not a proof of a different terminal law, but the discrepancy is substantial. The exact drift counterexamples in the next subsection already show why no equivalence follows from the manuscript.

`vector_check.py` is another independent implementation of the single-ring urn, using NumPy's distinct PCG64 generator and vectorizing independent replicas. It uses a **deterministic number of rings**, so its finite-horizon reference is \(\mathbb E M_k^2=\mathbb E[M]_k\), without an exponential-time approximation. Its complete output is `vector_check.txt`:

| \(L\) | Independent replicas | Rings per replica | \(\operatorname{Var}(M_k/\sqrt L)\), ± s.e. | Mean \([M]_k/L\), the exact finite-horizon second-moment reference |
|---:|---:|---:|---:|---:|
| 4 | 10,000 | 4,000 | 1.63981 ± 0.02617 | 1.64232 |
| 400 | 10,000 | 40,000 | 1.66258 ± 0.02332 | 1.62336 |

The \(L=400\) diagnostic is about 1.7 standard errors above its finite-horizon reference, whereas the first implementation's batches were below. This is consistent with sampling fluctuations, and supplies no reproducible evidence of a theorem failure or a systematic low-variance algorithm. I retain the original low batches and their uncertainties. The whole diagnostic took 39.1 seconds and its largest count array is 16 MB; it completed all requested rings, without triggering its 220-second cutoff.

### Model identification, cited results, and the discrete-time claim

**GAP in any claimed transfer; ERROR if “continuous-time form” means a mere clock change of the cited urn.** On a cycle the underlying vertex/edge roles can be exchanged, but the update schedules cannot. Superposing rate-one vertex clocks gives one uniformly selected comparison per event, with subsequent probabilities updated immediately. In the BBCL/Chen–Lucas/Lima model as described at lines 24–27, every comparison acts once in a round, using the counts at the start of the round. One color can gain two balls in a round. Poissonizing the number of whole rounds does not remove these simultaneous updates.

The difference can be checked exactly, without any citation. With the usual conditionally independent synchronous choices, the state \((3,1,3,1)\) on the dual \(C_4\) is reachable from unit counts in a single round. Its alternating harmonic charge has next-round conditional drift \(-1/32\); at the also-reachable state \((3,2,1,2)\) the drift is \(1/300\). In the continuous-time urn the generator drift of that charge is identically zero at both states. These calculations are in `exact_checks.py`. Therefore the proof and charge representation in this paper do not transfer to that synchronous urn by a time change. Different transition laws alone do not prove that terminal laws must differ, but they rule out that proposed justification of equivalence; an additional theorem would be necessary. If “continuous-time form” means only an asynchronous analogue, it should say so. The synchronous numerical comparison above is further evidence of a difference.

Benaïm's citation is being used for an appropriate type of result once the compactness, smoothness, almost-sure noise control, and finite critical-value hypotheses detailed above are supplied. Hall–Heyde is appropriate after the finite-array/conditional-variance repair (D). The HHKR citation is not needed to trust the displayed ODE or Lyapunov derivative: both have been independently derived here. The Birch assertion has the direct convex proof above.

The Chen–Lucas, Lima, and BBCL references concern the background synchronous model as the paper itself defines it. They supply no equivalence theorem in this manuscript. The claim to describe a “continuous-time form” of their distribution question must be narrowed to an analogous asynchronous question, explicitly identifying the cycle duality and the different update rule. It does bear on a related model; it is not a solution for the discrete-time urn.

No web access was used. Full texts of the cited works were not supplied in this folder, so I cannot certify their exact theorem numbering, historical priority, or the precise scope of the background descriptions by inspecting those sources. The assessment here distinguishes the standard theorem hypotheses that can be checked in the manuscript from bibliographic claims that cannot be externally verified under this run's rules.

The infinite-line continuity equation at lines 239–242 has the correct sign, and the linearized decay rate is \((1+\cos k)/2\). The subsequent nonlinear continuum equation and logarithmic decay interpretation are explicitly formal. They do not prove the conjectured infinite-line convergence, and the numerical evidence should remain described as such.

## Corrections required, by line/display

1. **Lines 15–16 and 24–27:** clarify that the result concerns an asynchronous analogue on the dual cycle, rather than identifying it with the Chen–Lucas/Lima synchronous urn. No transfer of the limit law is proved. The nonzero synchronous charge drifts above rule out a simple time-change justification.
2. **Line 23:** “For \(\alpha>1\) the counts localise” is too broad as a statement about all graphs and all \(\alpha>1\). For example, on the triangle the uniform equilibrium has tangent eigenvalue \(3\alpha/4-1\), so it remains attracting for \(1<\alpha<4/3\); the stochastic approximation has positive probability of convergence to this interior attractor. State the appropriate graph/parameter qualification or remove this unrelated general assertion.
3. **Lines 56–57:** explicitly give the finite-horizon squared-integrand/Poisson bound if the integrability question is to be closed within the proof. Add (A) to obtain all-time \(L^2\) boundedness. The original finite-time conclusion itself is correct.
4. **Lines 82–86:** replace the comparison started at a future-dependent random \(T\) by comparisons started at deterministic integers and killed when the denominator bound fails.
5. **Lines 102 and 130:** state nonnegative coordinates in the state-space/compact-set definitions. The urn interpretation makes this implicit, but the displayed sets alone omit it.
6. **Lines 131–134:** supply a maximal noise estimate and the almost-sure asymptotic-pseudotrajectory argument. Specify the finite equilibrium Lyapunov values and the internally chain transitive/Lyapunov criterion being invoked. Interpret “order \(t^{-1/2}\)” as a windowwise \(L^2\) estimate, not an unproved uniform almost-sure rate.
7. **Lines 137–140:** start the comparison *before* the exit time, then kill it at exit; do not start it at a nonexistent exit on the event of never exiting. Use countably many deterministic starting times.
8. **Lines 143–145:** add the one-sided divergence argument at each endpoint before evaluating logarithms at a limit point. Explain that every coordinate tending to zero there carries the same sign in the charge.
9. **Lines 150–152:** specify a nonempty positive fibre and the hypotheses of the general convergence remark; provide a source for the precise Birch fact or use the short convex proof. A general unsigned-incidence fibre is not necessarily a usual transportation polytope.
10. **Lines 176–182:** make the stopping and cap-crossing decomposition explicit. Apply the geometric reciprocal formula only to the uncapped Yule process on the no-crossing event, retaining the \((4\sqrt t)^{-1}\) error on crossing.
11. **Lines 189–195:** define the genuinely local truncated variables, use cycle distance, and require \(L\) large relative to \(R\). “Independent up to probability” should be expressed as a coupling/covariance estimate.
12. **Lines 201–213:** identify \(c=\pi^2/6\), prove the conditional variance condition and finite-row reduction before invoking Hall–Heyde, or give the exact-law proof (F). Equations (A), (D), and (E) also establish the asserted terminal mean/isometry and bracket convergence, including \(C_4\).
13. **Lines 216, 218, and the table's bracket column:** `code/warm2.c` accumulates \(\sum_{\text{rings at }v}1/(N_{v-1}N_v)\), not the continuous-time predictable bracket \(\int\sum_v1/(N_{v-1}N_v)dt\). This is a ring-sampled estimator with that compensator, and is also not the optional quadratic variation \(\sum(\Delta M)^2\). Label it as an estimator or integrate the holding times and full pre-jump rate as the independent simulator does. The authors' loop also applies the first event after \(T\); stop before that event for a true fixed-time sample. Neither issue explains a large discrepancy in their reported large-\(T\) numbers, but “exact” bracket values at \(T\) is an incorrect description of the code.
14. **Lines 228–229:** the estimate 1.64 is consistent with the exact constant. Separate finite-time truncation, Monte Carlo error, and the harmonic/log error, rather than inferring the infinite-time constant from two cycle sizes alone.
15. **Lines 235–237:** give \(T\), number of runs, and uncertainty for the \(C_4\) variance. Its exact limit is \(\pi^2/32-1/4\), not a justified exact value of 0.0564. A variance-matched \(\mathrm{Beta}(b,b)\) fit cannot itself rule out the beta family; use an actual distributional calculation. Also distinguish the finite-time statistic \((X_0+X_2)/4\) from the terminal \((1+u_\infty)/2\).

All created programs, outputs, and this report are in the current folder. No author program was executed, no other agent was started, and no web access, push, or visible-window operation was used. The simulators are single-threaded and use small arrays; numerical Python runs set numerical-library thread counts to one.

Task: “You are refereeing a mathematical paper that has been posted.” First recorded audit clock: 12 November 2026, 18:52:10 +04 (Asia/Tbilisi); the request's own timestamp was not exposed.
