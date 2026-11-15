# T105 work log, round 5

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 2026-11-15 08:22:27 Asia/Tbilisi (04:22:27 UTC); prompt receipt time unavailable.

## Orientation and bounded literature check

Read the startup MEMORY.md and compute_state.json. The governor reports `warn`, `owner_away_open`, CPU saturation. No heavy computation is planned. The specific instruction to write only in this folder overrides shared checklist, mesh and brain writes; these systems are not mutated. No git or subagents are used.

Read the REPORT.md, LOG.md and PROOF.md files in the three preceding folders. The first folder has no PROOF.md. Directory listings show no scripts in any of the three folders. The first read/search command was not prefixed with nice; subsequent shell commands use `OMP_NUM_THREADS=1 nice -n 15`. The sandbox prints `nice: setpriority: Operation not permitted`, while the read commands exit 0. No numerical experiment has been launched.

Web `search_query`: `Berry Tabor flat tori nearest neighbour spacing distribution 2025 2026 conjecture`; `"flat tori" "long gaps" 2026`.

Opened primary sources:

- Christoph Aistleitner, Valentin Blomer, Maksym Radziwiłł, *Triple correlation and long gaps in the spectrum of flat tori*, https://arxiv.org/abs/1809.07881 and https://ems.press/content/serial-article-files/31432. The published PDF gives averaged triple correlation (Theorem 1), uniform over intervals in a fixed compact interval, and the density-point argument (Lemma 2, Section 5).
- Wooyeon Kim, Jens Marklof, Matthew Welsh, *Values of ternary quadratic forms at integers and the Berry-Tabor conjecture for 3-tori*, https://arxiv.org/html/2601.03209v2. The abstract and introduction concern pair correlation for three-dimensional Dirichlet boxes, not the full two-dimensional spacing law.

The check finished within five minutes. No solution of the stated target was found; no SOLVED_ELSEWHERE.md is warranted. This bounded search cannot certify absence of other work.

Read commands used `cat` on the three earlier REPORT.md/LOG.md/PROOF.md files and `ls -la` on all four task folders. Web `find` for `6. Proof` located the published density-point and long-gap arguments. No further literature search is planned; subsequent source reads concern that proof.

## Independent re-check of round 4

For A=0, B>=1, the residual in its integer certificate is (B-1)(B-2)>=0. For A>=1, T=A+B, the residual is ((T-2)(T-3)+B(B-1))/2>=0. At (0,0) it is zero. This covers all counts without bounded-support assumptions.

With a=1, t=5/4, b=1/4, the certificate gives F(1)+2F(5/4)>=27/16=81/48. The scalar extremizer gives 1/2+2(55/96)=79/48. The deficit is 1/24. Independently, equality in the scalar quadratic bound forces T in {0,2,3}; then P(A=0,T>0)=7/96 exceeds E[B(B-1)]/2=3/96 by 1/24. The main incompatibility holds.

The area/slope separation also checks: a 1-Lipschitz excess of height at least 1/72 has area at least 1/5184, and -D(G)<=3(G-G*)/8. Their quotient is 1/1944. The scope of that result is the stated moment relaxation.

## Chosen extension, before attempting it

Take the report's proposed next step: combine the finite-count joint certificate with the scalar long-gap inequalities, using only nonnegative weights on triple counts, and establish a common-subsequence upper bound from the published uniform averaged theorem. The aim is a conditional-on-published-theorems improvement for almost every torus, with every finite-count and averaging step proved. A joint moment relaxation alone does not justify that conclusion.

The proposed construction replaces small disjoint pieces of the scalar integral near 1 and 5/4 by the two-interval inequality. Pair correlation controls differences of gap CDF values inside those pieces. If the replacement has a positive exact gain and leaves all triple weights nonnegative, the density-point argument can be applied once to the entire sum. Constants and quantifiers will be checked independently before stating any torus conclusion.

## Analytic step 1: a positive replacement with no increment error

A simpler replacement uses monotonicity alone. Put w=1/32 and remove W1=[1,1+w] and W2=[5/4,5/4+2w] from the scalar integral. Since F_N is nondecreasing, its integral over these two windows is at least w(F_N(1)+2F_N(5/4)). The finite-count certificate therefore supplies a lower bound with triple terms -w/2 times each of T3((0,5/4],(0,5/4]) and T3((1,5/4],(1,5/4]). The remaining scalar triple coefficients stay nonpositive. This is exactly the sign needed for one nonnegative sum of triple counts.

Both windows lie inside [1,c(G)] for 2<=G<=109/54, because their upper endpoint 21/16 is less than sqrt(7)-1. On these windows H_G(s)=(4s-s^2)/6. Direct integration gives

integral_W H_G = w(79/48)+(2/3)w^2-(1/2)w^3.

The Poisson value of the replacement is w(81/48). Hence the gain is

eta=w/24-(2/3)w^2+(1/2)w^3=131/196608>0.

The initial symmetric-neighbourhood construction was unnecessary: right-hand windows use monotonicity and avoid a separate pair-increment estimate. Only the common-subsequence passage and the ordinary endpoint bound still require the published correlation input.

## Analytic step 2: common-subsequence lemma

Let Q_N>=0 be the entire weighted sum of triple counts, including both new atoms and the remaining integrated scalar terms. Uniform averaged convergence in the published Theorem 1 implies integral_R Q_N -> C mu_hyp(R) for every finite rectangle R, where C is its Poisson benchmark. Fatou gives integral_R liminf Q_N <= C mu_hyp(R). Equivalently, if liminf Q_N>C on a set of positive measure, take a positive-margin subset and then a sufficiently dense rectangle: its contribution alone exceeds C mu_hyp(R), a contradiction. Thus liminf Q_N<=C almost everywhere. This applies once to the sum, so no invalid intersection of separate subsequences occurs.

Source commands: web `open` on the published PDF around lines 2715 and 2945. Read Theorem 1 and the complete relevant portions of Sections 5 and 6. The published lemma has one fixed left endpoint; the Fatou/density proof above extends it to the nonnegative combination with the two different left endpoints needed here. No new correlation theorem is being assumed.

## Proof saved; boundary and quantifier audit

Saved PROOF.md with the finite inequalities, the common-subsequence lemma, the explicit combined functional, and its consequence for almost every flat 2-torus. No numerical computation or script was needed.

For an eventual bound G, with at most M exceptional early gaps, the endpoint inequality has the uniform correction (M+1)/N. The integrated identity is exact:

integral_0^G F_N = G(N-1)/N - (x_N-x_1)/N + sum_(i<N)(g_i-G)_+/N.

The last sum is eventually constant; hence the integral tends to G-1 by Weyl's law. The combined finite inequality loses at most (M+1)(G-c(G))/N. All other count inequalities are exact under truncation, including the last anchor. There is no passage of count moments through a weak limit.

Pair convergence is uniform on a compact interval by a rational mesh and monotonicity. The triple functional is one nonnegative sum; applying the averaging lemma once gives the required subsequence. To obtain a bound for a random torus rather than merely for one fixed G, intersect the full-measure sets for G=2 and rational G between 2 and G_dagger. This countable intersection rules out limsup gaps <G_dagger. The proof does not assert infinitely many gaps at or above the exact endpoint G_dagger.

The new necessary condition for eventual gap bound G is D(G)+eta<=0, where D is the previous scalar deficit. Its unique zero G_dagger lies in (G*,109/54). This proves a torus consequence beyond the previous ideal-moment relaxation.

## Independent arithmetic and attempts to break the proof

- Window gain, second calculation: with J(s)=s^2/3-s^3/18, the antiderivative differences for W1 and W2 are 9311/589824 and 21400/589824. Their sum is 10237/196608. The replacement is 27/512=10368/196608, and the difference is 131/196608. This checks the Taylor-integral computation independently.
- Ordered-count factors: the replacement pair benchmark is 2wt=5/64, and its triple benchmark is w(t^2+b^2)/2=13/512. Their difference is 27/512. Both atomic triple weights are w/2, not w. At one later point the integer certificate has residual 1 when A=1, and zero when A=0,B=1; at two later points with A>=1,B<=1 it is exact. The explicit residual formula checks all larger counts.
- Window endpoints: W1 ends at 33/32<5/4; W2 ends at 21/16<sqrt(7)-1 because 1369<1792. Thus the same quadratic branch is valid throughout both windows for the full endpoint range, with no omitted crossover case.
- The baseline area was checked by integrating its density: its mass is G-c/3-c^2/6=1, and its first moment is 1-D(G). This gives the same I(G)=G-1+D(G) as CDF integration.
- Endpoint signs were independently checked through R(c)=c^2(c-2)^2+24c-40: at c=5/3 it is 25/81, hence D(109/54)=-25/5832. At G=2 it is 148-56sqrt(7), hence 18D(2)=14sqrt(7)-37>0. The added eta is smaller than 25/5832 because 763992<4915200.
- Differentiation gives D'=c-G; matching the pieces before differentiation gives the same derivative because the moving-boundary terms cancel. The slope bound G-c<=3/8 gives G_dagger>=G*+131/73728. Its sign is correct: extra positive area requires a larger endpoint.
- Polynomial elimination gives R(c_dagger)=72eta=393/8192, independently of the square-root equation, which is the earlier equation plus 18eta=393/32768.
- Rational root bracket, without numerical computation: R(331/200)=73619921/1600000000<393/8192<R(53/32)=77745/1048576. The cross products in the first comparison are 603094392832<628800000000; the second compares 50304 with 77745. Hence 481961/240000<G_dagger<12345/6144. The lower endpoint exceeds 251/125=2.008 by 41/240000.
- Normalization: the full quadratic-form ellipse has area 2pi E/sqrt(Delta), and identifying global sign halves its leading count. The rescaled levels pi q/sqrt(Delta) therefore have unit density. This agrees with the normalization in the opened paper. Extra multiplicities occur on a countable union of proper parameter hyperplanes and do not affect the almost-everywhere statement.
- Tried replacing the common lemma by separate liminf bounds: that would not justify a shared subsequence. The proof instead applies Fatou to the full nonnegative functional. It does not use an upper bound on each triple statistic at the selected N.
- Tried dropping nonnegativity in the lemma: the density argument would fail through cancellation off the exceptional set. All coefficients in the actual Q_N are explicitly nonnegative.
- Tested the support assumption against early exceptional gaps and the last anchor: (15) has correction (M+1)/N, and (16) records the finite sum of excess early gaps. Thus the argument proves a limsup statement, not merely a contradiction for sequences bounded from their first gap.
- The literature search does not establish global novelty. The full published averaged-triple proof has not been independently reproved; it is the explicit external theorem used. No full Berry–Tabor statement, explicit-torus spacing law, or optimality claim follows.

Readback command: `OMP_NUM_THREADS=1 nice -n 15 /bin/cat PROOF.md`, exit 0 with the recurring priority warning. Corrected a stray literal plus sign in the countable-intersection paragraph. No mathematical correction was needed after the audit.

## Completion

Saved REPORT.md with the required verdict and exact threshold, scope, verification, limitations and next step. Read the round-4 LOG.md again in a separate untruncated call. Final checks: `OMP_NUM_THREADS=1 nice -n 15 /bin/cat REPORT.md LOG.md` and `OMP_NUM_THREADS=1 nice -n 15 rg -n 'null exceptional|131|393|251|481961|Q_N|VERDICT' PROOF.md REPORT.md`. Both exited 0; the priority warning persisted. The saved constants, signs and report verdict agree. Only LOG.md, PROOF.md and REPORT.md were authored here. The three previous folders remain untouched. Final recorded clock: 2026-11-15 08:30:49 Asia/Tbilisi (04:30:49 UTC).
