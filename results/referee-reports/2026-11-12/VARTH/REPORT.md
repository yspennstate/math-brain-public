Overall verdict: SOUND

I found no mathematical error or missing argument in Theorem 1(i), Theorem 1(ii), Theorem 2, or the five numbered remarks. The discrete-time arguments are also sound under the explicitly stated continuization convention. One introductory sentence is ambiguous about scaling and should be corrected. The numerical claims tested below agree with independently written calculations.

This verdict concerns the mathematical arguments in the supplied files. No Aldous–Fill text is included in this folder. Under the instruction not to browse, I cannot authenticate the precise wording or numbering of its questions, the numerical constant in its cited comparison lemma, or the attribution to Hermon against their original sources. These limitations are distinguished below from gaps in the paper's proofs. I did not run the authors' Python program or recompile Lean.

Line references below are to the supplied, unchanged `PAPER.tex`.

## 1. Definitions, stationary law, and preliminary identities — SOUND

Lines 33–41, 54–56, and 85–88 use consistent conventions. In particular, hitting times include time zero, total variation is half the rowwise L1 distance, and the discrete-time relaxation time later uses the second largest eigenvalue, not the second largest absolute eigenvalue.

For the specified chain,

\[
q_{i,i-1}=1,\quad q_{i,i+1}=\varepsilon,
\qquad
\pi_i=\frac{\varepsilon^i}{\sum_{r=0}^k\varepsilon^r}.
\]

All permitted edges have positive rates when ε>0, so the chain is finite and irreducible. Detailed balance across edge (i,i+1) is exactly π_i ε=π_{i+1}. The formula includes ε=1 without a removable-singularity problem.

Here is an independent hitting-time derivation of Kemeny's constant, useful for checking both the spectral calculation and its limiting behavior. Put F_{i-1}=Σ_{j<i}π_j. Solving the birth-and-death hitting-time recurrence, or summing the flux across each edge, gives

\[
E_0T_j=\sum_{i=1}^j\frac{F_{i-1}}{\pi_i},
\qquad
\tau_0=\sum_{i=1}^k\frac{F_{i-1}(1-F_{i-1})}{\pi_i}.
\]

The denominator is the conductance π_{i-1}ε=π_i. This reproduces the claimed three-state formula without computing eigenvalues. Each summand tends to 1 as ε decreases to zero, giving τ_0→k independently of eigenvalue continuity.

The eigentime identity in line 87 also follows directly from finite-dimensional linear algebra: with Π having every row π and

\[
Z=\int_0^\infty(e^{tQ}-\Pi)\,dt,
\]

one has ZQ=QZ=Π−I and Z1=0. The solution of the hitting equations is E_iT_j=(Z_{jj}−Z_{ij})/π_j. Averaging over j gives tr Z, independently of i. The eigenvalues of Z are 0 and 1/λ_m, m≥2. Thus the random-target and eigentime identities used here are valid.

The reducible ε=0 chain is used for its transition semigroup, not as a chain to which the irreducible random-target lemma is applied. In particular, the limit τ_0→k must not be identified with a stationary-average hitting parameter of the absorbing chain. The paper does not make that identification.

## 2. Theorem 1(i) / Theorem A(i) — SOUND

Lines 91–124 check out, including all signs and constants.

* The three principal minors are ε², ε, and 1. The two nonzero eigenvalues have sum 2+2ε and product 1+ε+ε². Consequently
  \[
  \tau_0=\frac{2(1+\varepsilon)}{1+\varepsilon+\varepsilon^2}
        =2-\frac{2\varepsilon^2}{1+\varepsilon+\varepsilon^2}<2.
  \]
* Testing the two rows on {0} gives line 98, even without identifying the maximizing pair in total variation.
* The probability of making no jump from 0 is exp(−εt), giving line 102. It is a lower bound because returns to 0 are allowed.
* Before first reaching 0 from 2, there are at least two holding times. Conditional on the entire embedded jump chain, the first holding time and the final pre-hit holding time have independent Exp(1) and Exp(1+ε) laws. Their joint conditional law is constant across jump-chain realizations. Thus their unconditional independence, used in line 108, is justified. They are distinct holding times because N≥2.
* The event X_t=0 requires T_0≤t. Dropping intervening holding times decreases T_0; replacing E+E′/(1+ε) by the smaller (E+E′)/(1+ε) increases its distribution function. All inequalities in line 114 therefore point the right way.
* g′(s)=−s exp(−s)≤0. Substitution of t≤2 and exp(−x)≥1−x gives precisely line 118.
* Subtracting e^(−1) from its final expression gives e^(−2)f(ε), with exactly the polynomial printed in line 122. Its derivative is −(4+2e²)−8ε<0.

Independently certified Taylor bounds for e give

\[
f(0.01)>0.09353704956234175,
\qquad e^{-2}f(0.01)>0.01265886309563660.
\]

These are rationally certified lower bounds, not merely floating-point sign checks; the certificate is in `structural_output.txt`. Hence d̄_ε(t)>e^(−1) for every t∈[0,2] and every 0<ε≤0.01. Continuity and convergence to zero ensure that the threshold is attained after 2. A grid alone would not establish the whole parameter range, but this analytic bound does.

## 3. Theorem 1(ii) / Theorem A(ii), and the maximizing pair — SOUND

The eigenvalue argument in line 127 is valid despite the non-diagonalizability of the limiting pure-death generator. Continuity of the roots of its characteristic polynomial suffices: zero stays simple and the other k roots tend to 1. No continuity of eigenvectors at ε=0 is required. The edge-sum formula in section 1 provides a second proof of τ_0→k.

The Duhamel identity in line 129 has the correct order of factors. With the maximum absolute row-sum matrix norm, stochastic semigroups have norm 1 and ||Q_ε−Q_0||=2ε. Therefore

\[
\|P_t^\varepsilon-P_t^0\|\le2\varepsilon t,
\qquad |\bar d_\varepsilon(t)-\bar d_0(t)|\le2\varepsilon t.
\]

This proves precisely the uniform convergence on compact time intervals used in the manuscript.

For the pure-death chain, line 131 is correct: after choosing μ(0)≥ν(0), the contribution of state 0 to the sum of positive differences is μ(0)−ν(0), and the remaining contribution is at most 1−μ(0). Thus the distance is at most 1−ν(0). The absorption time from j is Gamma(j,1), and these absorption times can be coupled increasingly in j. The pair (0,k) attains the upper bound. Hence

\[
\bar d_0(t)=e^{-t}\sum_{j=0}^{k-1}\frac{t^j}{j!}.
\]

Its derivative at the crossing is

\[
\bar d_0'(t_k)=-e^{-t_k}\frac{t_k^{k-1}}{(k-1)!}<0.
\]

Thus the crossing is transversal for every k≥1, including k=1. The bracketing argument in line 133 is complete. In fact strict crossing and compact convergence suffice; derivative convergence is not needed.

The answer to the explicit uniformity question is stronger than the theorem needs: d̄_ε→d̄_0 uniformly on the entire half-line. Every d̄ is nonincreasing by total-variation contraction. For t≥T, both functions are bounded by d̄_0(T)+2εT, while their difference for t≤T is at most 2εT. Therefore

\[
\sup_{t\ge0}|\bar d_\varepsilon(t)-\bar d_0(t)|
\le\bar d_0(T)+2\varepsilon T.
\]

First choose T large, then ε small. The paper claims only compact convergence and uses it correctly; there is no missing global-uniformity assumption.

The paper explicitly proves endpoint maximization for ε=0. Its proof of part (i) only needs an endpoint lower bound, and the numerical computations below maximize over all pairs. For completeness, endpoint maximization is also true for ε>0 for these chains. A proof is as follows. The common rate-1 downward clock and common rate-ε upward clock, with moves clipped at the boundaries, give an order-preserving coupling. Moreover exp(tQ) is totally positive of order two: the additive second compound of a tridiagonal birth-and-death generator has nonnegative off-diagonal entries, so its exponential, whose entries are the corresponding two-by-two minors of exp(tQ), is entrywise nonnegative. For t>0 the entries of exp(tQ) are positive. The row ratio P_t(j,x)/P_t(i,x) is consequently increasing in x when i<j. Row differences have a single sign change, so their total variation is the maximum difference of their cumulative probabilities. Order preservation bounds each such difference by the corresponding difference for rows 0 and k. This proves that (0,k) maximizes d̄. Ties are possible, particularly at time zero.

The law-of-large-numbers statement in line 69 is valid: for each δ>0, the Gamma survival probabilities at (1−δ)k and (1+δ)k tend to 1 and 0, respectively. These bracket the e^(−1) quantile and imply t_k/k→1. No claim about a maximum over all positive integers k is inferred from the finite search k≤60.

## 4. Theorem 2 / Theorem B, continuous and discrete time — SOUND

Lines 147–155 use the additive Dynkin martingale, not an exponentially growing martingale stopped at an unbounded time. This distinction avoids the usual optional-stopping trap.

The sign change of u may be chosen separately for the particular initial state i. It does not alter either the normalization or the eigenfunction equation. Since πQ=0 and λ_2>0, π(u)=0. If E_iU=∞ the asserted lower bound is immediate. Otherwise U<∞ almost surely, bounded convergence applies to u(X_{U∧t}), and

\[
\left|\int_0^{U\wedge t}u(X_s)\,ds\right|\le U
\]

provides the integrable domination needed for the integral. The resulting identity is

\[
u(i)=\lambda_2 E_i\int_0^Uu(X_s)\,ds.
\]

Taking absolute values directly gives |u(i)|≤λ_2 E_iU; equivalently one may use the sign convention in the paper. Thus |u(i)| is the correct quantity. Choosing a state at which |u|=1 proves the maximum-over-starts inequality. It does not assert this stronger bound at every initial state without the |u(i)| factor.

Randomization causes no difficulty: the stated definition requires that X retain its Markov property in the enlarged filtration. The generator martingale and bounded stopping argument are valid there. Revealing independent auxiliary randomness is an example of such an enlargement; anticipating future transitions is not.

In discrete time, stop the printed martingale at U∧N with integer N and then let N→∞. The absolute sum is bounded by U, which is integrable in the nontrivial case. Since λ_2<1, division by 1−λ_2 is legitimate even if λ_2 is negative. Periodicity is allowed. This proves the bound for integer-valued randomized stopping times; it does not rely on replacing them with real-valued times.

## 5. Numbered Remark 1: two-state equality — SOUND

Line 166 gives an actual admissible stopping rule. Its decision at time zero is independent of the chain; otherwise it stops on first hitting the other state. From state 1 it ends at states 1 and 2 with probabilities b/(a+b) and a/(a+b), and has mean 1/(a+b). The symmetric construction works from state 2. Together with Theorem 2 this proves equality for the maximum over starts.

The remaining identities follow from the two-state transition matrix and the hitting means 1/a and 1/b. The same construction works for a discrete matrix with off-diagonal probabilities a,b∈(0,1], using geometric hitting times and the continuized definition of τ_1. This includes the periodic flip a=b=1, where τ_2=τ_1^(2)=1/2 although U is integer valued.

## 6. Numbered Remark 2: random target — SOUND

Line 168's independently sampled target J∼π can be revealed at time zero. Then U=T_J is a randomized stopping time, X_U=J, and its finite mean is Σ_jπ_j E_iT_j=τ_0. This verifies feasibility of the stopping problem and τ_1^(2)≤τ_0, in either time convention. The refinement τ_2≤τ_1^(2)≤τ_0 follows.

## 7. Numbered Remark 3: the fundamental-matrix formula — SOUND

The direct eigenfunction calculation in lines 170–172 is valid. In particular, Σ_jZ_{ij}=0, and Z_{ij}+mπ_j≥0 by definition of m, so the inequality with u(j)≤1 is justified.

Here is an independent derivation of the stopping-time formula, including attainability rather than just a linear-programming lower bound. Let x_j be the expected time spent at j before U. Dynkin's identity applied to coordinate indicators gives

\[
xQ=\pi-\delta_i,\qquad x\ge0,\qquad\sum_jx_j=E_iU.
\]

All solutions of the balance equation have the form

\[
x_j=Z_{ij}+m\pi_j,
\qquad m=\sum_jx_j.
\]

Irreducibility ensures that the only row null vectors of Q are multiples of π. Nonnegativity is therefore equivalent to

\[
m\ge m_i:=\max_j\frac{-Z_{ij}}{\pi_j}.
\]

For discrete time use G=P−I and Z=(I−P+Π)^(−1)−Π. This inverse is defined even for periodic irreducible chains; an ordinary infinite sum Σ(P^n−Π) would not be an appropriate definition in the periodic case. The same balance equation holds when x counts visits strictly before U.

To prove attainability in discrete time, set x_j=Z_{ij}+m_iπ_j and y_j=x_j+π_j. At each visit to j stop with probability

\[
s_j=\frac{\pi_j}{y_j};
\]

otherwise take one P-step. All s_j are positive. The balance equation says y=δ_i+xP. Thus this rule has expected pre-stop visits x, stopping distribution π, and mean m_i. These claims can also be verified by solving the finite absorbing-chain equations; the independent program does so with exact fractions for every tested initial state and terminal state.

For continuous time choose r≥max_j(−q_jj), uniformize with P=I+Q/r, and use the preceding rule with expected pre-stop visit vector rx. Each continued step waits an independent Exp(r) time. The resulting continuous-time rule has occupation vector x, stationary terminal distribution, and mean m_i. The extra clock randomness is admissible. Consequently

\[
\inf_U E_iU=m_i,\qquad
\tau_1^{(2)}=\max_{i,j}\frac{-Z_{ij}}{\pi_j}.
\]

Equivalently, m_i=max_j(E_iT_j−E_πT_j). This is an exact stationary-stopping quantity, not the mean of a strong stationary time. No independence between U and X_U is required.

## 8. Numbered Remark 4: complex eigenfunctions without reversibility — SOUND

Line 175 follows by applying Dynkin's identity to the real and imaginary parts and recombining the identities before taking absolute values:

\[
u(i)-\mu(u)=\lambda E_i\int_0^Uu(X_s)\,ds.
\]

The complex triangle inequality gives the claimed |λ| ||u||_∞ E_iU bound. Bounding the two parts separately and then adding crude bounds would lose a constant, but the combined identity does not. For μ=π and λ≠0, π(u)=0; choosing a state maximizing |u| gives τ_1^(2)≥1/|λ|. Infinite mean again makes the assertion immediate. No reversibility is needed for this extension.

## 9. Numbered Remark 5: absolute relaxation time — SOUND

For the displayed matrix the nontrivial eigenvalue is 2δ−1, its stationary law is uniform, and the proposed randomized hitting rule has mean 1/[2(1−δ)]. Theorem 2 supplies the matching lower bound. The absolute relaxation time is 1/(2δ), which is strictly larger when 0<δ<1/2. At δ=0 it is infinite while the stationary-stopping value is 1/2. This also explains why the eigenvalue convention in the discrete theorem matters.

## 10. Discrete-time transfer and the chain's own threshold — SOUND

Lines 136–142 are correct, with a wording qualification at line 81 discussed below.

The stated restriction on c makes I+cQ stochastic; it is sufficient also for k=1, where it need not be the largest possible range. Its continuization has generator cQ. A continuous-time chain with generator P−I is obtained by running the P-chain at independent rate-one Poisson times, including self transitions. Its mean hitting time equals the expected number of P-steps to hit, because the interarrival times have mean one. Therefore

\[
\tau_0(P)=\tau_0(Q)/c,\qquad
\tau_1(P)=\tau_1(Q)/c,
\]

where the latter is the threshold of the continuization. Their ratio is exactly preserved for every allowed c. This claim does not say that the threshold formed from P^m has the same ratio.

For that latter threshold, the telescoping-product estimate and exponential remainder in line 140 are valid in the specified norm. Multiplication by either stochastic matrix has operator norm at most one. For mc≤2 the error is bounded by c||Q||²exp(c||Q||). The functional d̄ is 1-Lipschitz for this norm: the error in the distance of any pair of rows is at most half the sum of the two row errors.

The uniform positive margin proved in section 2 is larger than 0.01. Subtracting a matrix error at most 0.01 therefore leaves a strict inequality. If every integer m≤2/c fails the threshold test, the first successful integer is strictly larger than the real number 2/c, whether or not that real number is an integer. Thus the final strict inequality in line 142 is correct.

An explicit choice works uniformly over the whole claimed ε-range: 0<c≤0.002. Indeed ||Q||≤2.02, and

\[
0.002(2.02)^2\exp(0.002\cdot2.02)
=0.008193836320433487\ldots<0.01.
\]

At the largest permitted c the chain's own threshold can fail the comparison. For example, ε=0.01 and c=100/101 give its own threshold 2 but τ_0(P)=2.0198000198… . This does not refute the paper: its assertion about that threshold is explicitly restricted to small c. It refutes an interpretation of “same ratio” using the uncontinuized threshold.

## 11. The constant C, source questions, and scope of the introduction — SOUND subject to the cited external comparison

Line 69's lower bound on C follows from an actual sequence of irreducible, reversible five-state chains, taking k=4 and ε↓0. A supremum over all chains is at least that limit, whether or not any chain attains it. There is no inference from a finite grid to a universal upper bound.

The number 66 is imported, not derived or numerically established in this paper. Its indicated source is Aldous–Fill Lemma 4.15, in the list of references attached to line 45. If that cited result is τ_1≤66τ_0 under these conventions, its application is immediate and gives C≤66. The manuscript provides neither its proof nor an excerpt of that source. I cannot independently check that source's hypotheses, normalization, exact constant, or numbering from the supplied folder. The claimed upper bound should therefore be recorded as a cited bound, not a result independently verified by the authors' programs or by this numerical audit. Requiring a full reproof of a correctly cited background theorem would not itself identify a gap in the new argument.

The other comparisons in line 45 have the right mathematical meanings. The spectral/eigenfunction argument gives τ_2≤τ_1, since d̄(t)≥exp(−λ_2t); the eigentime identity gives τ_2≤τ_0; the random-target rule gives τ_1^(2)≤τ_0. The stated equivalence family and Hermon attribution are background source claims, not used to prove Theorems 1 or 2. They cannot be source-authenticated here.

As far as the supplied text shows, the two questions are internally consistent with the declared Aldous–Fill conventions: they concern the continuized variation threshold and the least mean of a stationary stopping time, with maximization over initial states after the infimum. They do not concern a strong stationary time or absolute relaxation time. However, the manuscript supplies a paraphrase, not an original excerpt. I cannot certify that both belong to Open Problem 4.48 rather than one being the neighboring question, or that the paraphrase is verbatim faithful. This is an unresolved bibliographic check, not a demonstrated misstatement.

The abstract's two answers and its limiting examples are supported by the theorems. It does not claim to identify the best C or the maximum of t_k/k over all k. The introduction also correctly limits its finite search to k≤60. The exception requiring clarification is “Both theorems hold … in discrete time” at line 81: the answers and ratio statements transfer, whereas the unscaled numerical values and limits in Theorem 1 do not. The rest of that same paragraph and section 2.3 give the correct scaling.

## 12. What Margin.lean proves — SOUND within its stated scope

Reading the entire source, its three theorem statements are:

1. `g_antitone` (lines 13–30 of the Lean file): for real 0≤s≤S, exp(−S)(1+S)≤exp(−s)(1+s).
2. `margin` (lines 33–40): for real 0<ε≤1/100, 3−exp(1)−ε(4+2exp(1)²)−4ε²>0.
3. `lower_bound_gt` (lines 43–76): for real 0<ε≤1/100 and 0≤t≤2, exp(−εt)−1+exp(−(1+ε)t)(1+(1+ε)t)>exp(−1).

The proofs use elementary exponential inequalities, an imported Mathlib bound on exp(1), and algebraic tactics. There is no `sorry`, additional axiom, or numerical oracle in this file. The accompanying log reports a successful Lean/Mathlib compilation; I have not independently reproduced that compilation and do not treat the log as an independent kernel check.

The third theorem is exactly the scalar inequality used after the probabilistic lower bound in Theorem 1(i). Thus it formalizes a statement used by the paper. It does not prove the Markov-chain comparison giving that lower bound, the stationary law, the Kemeny calculation, either limiting assertion, Theorem 2, the optimal stopping formula, or the bound 66. The paper's description at line 191 accurately limits its scope, and line 193 correctly says the computations are not part of the proofs. The ordinary written proof of the scalar inequality is sufficient without Lean.

## Independent programs, commands, and outputs

The two new programs are `audit_math.py` and `audit_structural.py`. They import no code from `code/`. The numerical calculations use mpmath 1.3.0 at 70 digits, or 65 digits in the structural script; the stopping-time optimization uses Python exact fractions. The commands to reproduce the saved outputs are:

```sh
python3 -B audit_math.py gamma > gamma_output.txt
python3 -B audit_math.py paths > paths_output.txt
python3 -B audit_math.py random > random_output.txt
python3 -B audit_math.py discrete > discrete_output.txt
python3 -B audit_math.py controls > controls_output.txt
python3 -B audit_structural.py > structural_output.txt
```

Each command has a 280-second wall-clock alarm. The actual runs took approximately 0.9, 5.6, 0.8, 0.6, 1.6, and 0.8 seconds, respectively. Peak measured resident memory was below 23 MB. Computations ran sequentially, without worker processes, other agents, browser use, or visible windows. The manuscript and authors' files were not modified.

### Three-state chain

The high-precision results are:

| ε | τ_0 | d̄(2) | τ_1 | τ_1/τ_0 |
|---|---|---|---|---|
| 0.01 | 1.999801999801999801999802 | 0.402400640424033289826173 | 2.133068661857253153374083 | 1.066639928387134361496615 |
| 0.001 | 1.999998001999998001999998 | 0.405644991834243063344513 | 2.144887094576618422509708 | 1.072444618660484324450869 |

`paths_output.txt` records these results. `eps_grid.csv` contains all 100 values ε=j/10000, j=1,…,100, with τ_0, d̄(2), τ_1, and the ratio. Every grid point satisfies τ_1>2>τ_0. `dbar_eps_100.csv` and `dbar_eps_10.csv` contain d̄(t) on t=0,0.25,…,4 at ε=0.01 and 0.001, computed by direct matrix exponential and checked against the independent polynomial spectral-projector formula.

The largest three-state matrix-exponential discrepancy was 1.91×10^(−70); the largest discrepancy between the closed form, spectral sum, and hitting-equation calculations of τ_0 was 6.71×10^(−69). Roots were bracketed by 145 bisection steps at 70-digit precision. These are numerical accuracy checks, not formally interval-certified matrix exponentials. The all-ε conclusion comes from the rational analytic certificate, not numerical interpolation.

`controls_output.txt` independently checks every probabilistic lower bound on t=0,0.001,…,2 at both ε values, including the absorbed-chain hitting distribution at t=0,0.05,…,2. The minimum scalar lower bounds are 0.3808181778487229006 and 0.4034667779147010135. It also verifies the manuscript's ε=0.05 control: f(ε)=−0.6671874383521103… and τ_1/τ_0=1.04213907512266084… .

### Gamma quantiles

`gamma_results.csv` contains all 60 quantiles and ratios to 60 printed significant digits, their negative crossing derivatives, and bisection bracket widths. Selected output:

| k | t_k | t_k/k |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2.146193220620582585237061 | 1.073096610310291292618531 |
| 3 | 3.258252468867040069126053 | 1.086084156289013356375351 |
| 4 | 4.351992687802341510134091 | 1.087998171950585377533523 |
| 5 | 5.434092747620628605094098 | 1.086818549524125721018820 |
| 60 | 62.310672279089120427489926 | 1.038511204651485340458165 |

The maximum over k=1,…,60 is at k=4. All the manuscript's quoted digit prefixes are correct. The largest bracket width is 1.211×10^(−55). The full textual output, including all 60 values, is `gamma_output.txt`. A second evaluation through the incomplete-gamma special-function API, rather than the recursively summed Poisson tail, gives maximum residual 2.57×10^(−57) over all 60 roots (`controls_output.txt`).

### Chains with k=3,4,5

All starting-state pairs were evaluated. `paths_output.txt` gives the full-precision results at ε=10^(−3),10^(−5),10^(−7). At the smallest ε:

| k | τ_0 | τ_1 | τ_1/τ_0 |
|---|---|---|---|
| 3 | 3.000000099999990000 | 3.258252375812823578 | 1.086084089068141844 |
| 4 | 4.000000200000000000 | 4.351992662486905814 | 1.087998111221820892 |
| 5 | 5.000000300000010000 | 5.434092803460228516 | 1.086818495482933801 |

These approach the asserted limits. For k=5 the threshold approaches t_5 from above; for k=3,4 it approaches from below. The theorem does not assert a direction. The largest direct-exponential check discrepancy in these tests was below 3.7×10^(−60).

`audit_structural.py` separately evaluates direct matrix exponentials for k=1,…,6, ε∈{0,0.001,0.01,0.5,1,2}, and t∈{0.01,0.5,2,5}. Endpoint maximization passes all 144 cases. At ε=0, the largest discrepancy from the Gamma survival identity is 2.38×10^(−66). It also prints exact rational edge-sum Kemeny values, including 20200/10101 for k=2, ε=0.01.

### Theorem 2 and exact optimal stationary stopping values

There are 15 independently generated rational reversible chains for each n=2,…,6, using seed 129845. Their stationary weights and symmetric conductances are positive rational numbers. The program checks the CT chains and the DT matrices obtained by uniformization. It computes the optimal stationary stopping mean exactly as a fraction; it also enumerates all possible vertices of the occupation-measure linear program independently of the fundamental-matrix inversion. For the DT chains it constructs a stopping rule and solves its mean and terminal probabilities exactly, not by simulation.

All 300 initial states pass these exact comparisons in each time convention. Relaxation eigenvalues and normalized eigenfunctions are computed at 70 digits, and both the statewise bound and maximum-over-states bound pass. Output ranges are:

| n | chains | minimum τ_1^(2)/τ_2 | maximum τ_1^(2)/τ_2 |
|---|---|---|---|
| 2 | 15 | 1 | 1 |
| 3 | 15 | 1.00808970871172875 | 1.40945159809744175 |
| 4 | 15 | 1.05137379053762787 | 1.29910150872395496 |
| 5 | 15 | 1.09235855095862187 | 1.43279855858755684 |
| 6 | 15 | 1.10669141105591217 | 1.52125305632654192 |

The tiny minimum two-state slack −1.82×10^(−71) is eigenvalue rounding at equality. Exact stopping values, all ratios, and the DT scaling parameters are in `random_results.csv`; `random_output.txt` summarizes them. The δ=0,0.01,0.25 two-state controls give stopping/relaxation values 1/2, 50/99, and 2/3, while the respective absolute relaxation times are infinite, 50, and 2.

### Discrete-time checks

`discrete_output.txt` checks ε=0.01 and 0.001 at c=1/(1+ε),0.1,0.01,0.001. Mean hitting times are solved from P−I independently of the scaling formula, and the integer threshold is bracketed by evaluating P^m on both adjacent integers.

| ε | c | τ_0(P) | own discrete threshold | comparison |
|---|---|---|---|---|
| 0.01 | 100/101 | 2.019800019800… | 2 | below τ_0(P) |
| 0.01 | 0.1 | 19.998019998020… | 21 | above τ_0(P) |
| 0.01 | 0.01 | 199.980199980200… | 213 | above τ_0(P) |
| 0.01 | 0.001 | 1999.801999801999… | 2133 | above τ_0(P) |
| 0.001 | 1000/1001 | 2.001998000002… | 2 | below τ_0(P) |
| 0.001 | 0.1 | 19.999980020000… | 21 | above τ_0(P) |
| 0.001 | 0.01 | 199.999800200000… | 214 | above τ_0(P) |
| 0.001 | 0.001 | 1999.998001999998… | 2145 | above τ_0(P) |

The continuized ratios in every row equal the corresponding CT ratio above. The distinction between these two thresholds is essential.

## Corrections and source checks

1. **Line 81, “Both theorems hold for chains in discrete time.”** Replace with: “Both answers remain valid in discrete time under the conventions below: the ratios in Theorem 1 are preserved by continuization, and Theorem 2 holds for integer-valued randomized stopping times.” If stating numerical limits for I+cQ at fixed c, write τ_0→k/c and τ_1→t_k/c. For example, at c=1/2 the unscaled limit τ_0→k is false. This is an ambiguity in the introductory summary; the detailed discrete-time section already gives the correct statements.
2. **Lines 47–51 and 214, attribution to Open Problem 4.48.** Verify the original numbering and wording before publication of a correction or further revision. The supplied folder does not let this audit decide whether both questions are part of 4.48 or one is adjacent. There is no evidence here warranting an asserted replacement number.
3. **Lines 45–47 and 69, C≤66.** Keep the distinction between the new lower bound and the cited upper bound explicit, for example: “Together with the cited Aldous–Fill bound τ_1≤66τ_0, this gives …”. Source verification should check the exact variation threshold, the averaging convention for τ_0, and the lemma number. No change to 66 is justified by this audit.

No corrections are required to the displayed formulas, quantile decimals, Theorem 2's |u(i)| factor, the integrability argument, or the descriptions of what the Lean file formalizes. No error was found in the numbered results.

Task: “You are refereeing a mathematical paper that has been posted” — 12 November 2026, first recorded clock sample 19:55:48 Asia/Tbilisi (15:55:48 UTC).
