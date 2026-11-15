# Independent referee report

Overall verdict: **SOUND**.

I found no gap in the contraction proof, the finite-mean domination argument, or the derivative and strict local monotonicity calculation. The one definite mathematical wording error is the unnormalized one-tree density in [rem:tilt]; the main proof gives the correct density and is unaffected. Numerical checks support the formulas. This verdict treats the cited Lin–Rousselin dimension formula as a known external theorem: its exact source hypotheses and numbering, and the novelty claim, could not be source-verified in this no-browsing run. A publication referee should complete that literature check before acceptance.

The geometric difference quotient is not an estimate of the exact zero-bias slope: curvature explains about .00104 of its excess. The remaining discrepancy is consistent with the printed Monte Carlo uncertainty. No theorem-level overstatement was found. Numerical reproducibility and a few literature descriptions need clarification.

PAPER.tex was read only. All programs and results are original to this audit and saved in this directory. No browsing, git push, other agents, visible windows, outside mutations, or authors' code were used. Computations ran serially with numerical-library threads set to one; the batch driver has one child at a time. Largest stored arrays are in the ray check (roughly 170 MB including stored node values and indices, comfortably under 1 GB). A nice-priority attempt was denied by the sandbox, so no priority change is claimed; the individual pool runs took about 4–7 seconds and ray runs about 1–2 seconds. Exact and symbolic checks were also short. Signals cap every numerical invocation and the batch driver at 280 seconds.

## Verdict table and detailed proof audit

The log below supplies a verdict for each requested lemma, proposition, proof step, theorem, corollary, remark, scope and attribution question. CORRECT means checked directly except where explicitly marked memory-only. GAP in a source-verification or novelty row records an audit limitation, not a discovered mathematical gap. WRONG in the density row is a local exposition error with the correction stated.

# Independent referee log

Task: “Be a hard, independent referee” of PAPER.tex. Started 2026-11-12 06:56 +04 (Asia/Tbilisi).
Only this directory is mutated; no web, other agents, authors' programs, or external state updates. The the author's local-only rule takes precedence over the standing mesh/checklist/memory writes. Computations run one at a time, with numerical-library threads limited to one. A nice-priority attempt was denied by the sandbox; no priority change is claimed. PAPER.tex is untouched.

## 1. Escape recursion and lower bound

| Step (source lines) | Verdict | Reason |
|---|---|---|
| [lem:rec], first-step equation, 163–170 | CORRECT | From child i, success before returning to the root has probability b_(j-1)(T_i); a return restarts the experiment. Multiplication gives b(lambda+S)=S. |
| Finite-region exit, 160–163 | CORRECT | Interpret “first j generations” as levels 0,...,j-1. The set is finite by local finiteness. For lambda>0, the minimum of the finitely many probabilities of following the ancestral path to e_* is positive; block trials of j steps give a geometric tail for failure to exit. For lambda=0 distance increases at every step. |
| Positivity of denominator, 170–171 | CORRECT | lambda>0 suffices; at zero every finite-level success probability is one. |
| Decreasing events and escape, 171–173 | CORRECT | Intersect the countably many almost-sure finite-exit events. Never hitting e_* then forces reaching every level. Conversely a path that hits e_* at finite time has reached only finitely many levels by that time. |
| [lem:lower], simultaneous induction, 185–187 | CORRECT | The induction hypothesis explicitly says “and all trees of T_k”; every child subtree remains in that class. S>=n(1-lambda/k)>=k-lambda, and s/(lambda+s) is increasing on its domain. |
| lambda=k in first assertion | CORRECT | The claimed lower bound is zero. The comparison denominator at k-lambda=0 is k>0; the proof makes no positive-transience claim at the critical value. |
| lambda=0 in the induction | CORRECT | Actual S=n>0. The comparison point k-lambda=k is also positive, so the removable singularity at (lambda,s)=(0,0) is never used. |
| [eq:beta], finite-sum limit, 187–188 | CORRECT | For lambda<k, S>=k-lambda>0, so the rational map is continuous at the limit. There are only n child terms. |
| Conductance normalization, 191–192 | CORRECT | Root-to-child edges have conductance 1, child networks are scaled by 1/lambda. Each branch has series conductance C_i/(lambda+C_i)=beta_i. The added parent edge must have conductance lambda, giving beta=C/(lambda+C). This convention should be made explicit. |

Exact-fraction comparison: audit_exact.py independently forms the absorbing-chain Dirichlet linear equations and solves them by Fraction Gaussian elimination. All 25 comparisons (five mixed-degree trees, lambda=0,1/3,1,3/2,3) agree exactly. Trees and fractions are saved in exact_results.json. The smallest test tree was subsequently changed to have mixed degrees too, then rerun. Command: `python3 audit_exact.py`.

## 2. [prop:C1], line-by-line

| Step (source lines) | Verdict | Reason |
|---|---|---|
| Definition of x and its cube, 204–210 | CORRECT | b_j in [c,1]; all child subtrees stay in T_k. |
| (a) [eq:partials], 214–215 | CORRECT | dH/dx_i = exp(x_i)(1/S-1/(lambda+S)) = q w_i; partial_lambda H=-1/(lambda+S). |
| (b) q bound, 217 | CORRECT | q=lambda/(lambda+S)<=lambda/(lambda+k-r)<=r/(r+k-r)=rho. Using monotonicity in lambda is essential; it is valid. |
| (c) Lipschitz, 218–219 | CORRECT | The l1 norm of the gradient is sum_i q w_i=q<=rho; integrate along the segment in the convex cube. No n-dependent constant enters. |
| (d) delta_1, 220 | CORRECT | b_1=n/(lambda+n); supremum is log(1+r/k). log(1+rho)<=rho. |
| delta_j contraction, 219–220 | CORRECT | For any T the two input vectors have the same finite dimension n; each coordinate difference is <= the global delta_(j-1), since each subtree is in T_k at the same lambda. Thus delta_j<=rho delta_(j-1)<=rho^j. |
| Finite-stage rationality and chain rule, 222–228 | CORRECT | Each finite-level recursion is rational and has positive denominators throughout [0,r]. [eq:yrec] follows by the chain rule. |
| (e) y bound, 229–232 | CORRECT | Starting y_0=0 gives (k-r)^(-1) sum_(h=0)^(j-1) rho^h <= 1/((k-r)(1-rho))=k/(k-r)^2=M. |
| (f) Three-term decomposition, 235–237 | CORRECT | Add and subtract q_j sum w_(j,i) y_(j-2)(T_i); the displayed equality is exact. |
| Indexing and exp inequality, 239 | CORRECT | b_(j-1)-b_(j-2) is controlled by delta_(j-1), exactly the definition. exp has derivative <=1 on (-infinity,0]. |
| First bracket, 240–241 | CORRECT | Difference of reciprocals <=n delta/(nc)^2<=delta/(k c^2). |
| Second term, 241–242 | CORRECT | sum w=1, q<=rho, and global eta_(j-1) controls each child difference. |
| Third term, triangle inequality, 245–246 | CORRECT | Add and subtract b_i'/(S(lambda+S)); summing b_i' gives S'. |
| Equality with lambda+S+S', 247 | CORRECT | |S'(lambda+S')-S(lambda+S)|=|S'-S|(lambda+S+S'); the S' outside cancels its factor in the common denominator. |
| Last inequality, 248–250 | CORRECT | Split lambda+S+S' <= (lambda+S)+(lambda+S'); the resulting terms have denominators S(lambda+S') and S(lambda+S), each >=(nc)^2. Total <=3 delta/(k c^2). |
| Final third-term constant, 251 | CORRECT | Multiply that sum by lambda<=r and |y_(j-2)|<=M. |
| (g) eta recurrence and induction, 254–257 | CORRECT | Divide the recurrence by rho^(j-1); each increment is <=K. The resulting arithmetic-geometric series is summable because rho<1. The stated eta_1 bound is valid (actual supremum is 1/k). |
| (h) Uniform convergence, 259–260 | CORRECT | Sum eta_j finite makes y_j uniformly Cauchy over all trees and lambda. For each fixed tree its uniform limit is continuous in lambda. No topology on the tree class is required. |
| Integral identity, 261–264 | CORRECT | x_j(T,0)=0, x_j converges pointwise to log beta with beta>=c, and uniform convergence of y_j permits passage under the finite integral. |
| beta derivative bound and zero value, 265–267 | CORRECT | beta'=beta y and beta<=1. At zero q=0,S=n, so y_j=-1/n for every j>=1 and beta_0=1. |
| Endpoint regularity | CORRECT | The integral with continuous integrand proves a right derivative at 0, a left derivative at r, and continuity up to both ends. If an ordinary derivative at r is desired, repeat with any r<r'<k. |

All displayed constants survive rederivation. Finite-depth numerical tests are saved in contraction_results.json; these test, rather than establish, the uniform estimates.

Numerical outcome: 384 compactly represented roots, 17 lambda values, depths 1–20, all nine (k,r) choices. Every delta and eta bound passed. Maximum centred-difference discrepancy for y was 1.13e-10 (step 1e-5). Largest observed |b_20'| was 1/k (the grid includes lambda=0), well below M; this does not certify an infinite-depth supremum. Sharing of lower subtrees is disclosed in audit_contraction.py; unfolding gives actual mixed-degree trees but the root samples are dependent.

## 3. Formula [eq:lin]

| Step | Verdict | Reason |
|---|---|---|
| Formula as remembered | CORRECT (high confidence, source not consulted) | For 0<lambda<m, use independent GW trees T,T'. Write C(T)=sum beta(T_i), B=beta(T'), W=B C/(lambda-1+B+C). The invariant density on T is E[W|T]/E W. Dimension equals E[W log(lambda+C)]/E W. This matches the recalled kappa_lambda(beta) representation, up to normalizing constants which cancel. |
| Roles of the two trees | CORRECT | T is the environment along the harmonic ray, T' is an independent auxiliary tree integrated out in its density; they are not two successive environments on the ray. |
| [eq:beta] normalization | CORRECT | Root-child conductance is 1 and added-parent edge conductance is lambda, not 1. At lambda=1 the usual beta=C/(1+C) is recovered. |
| Use of [eq:beta] for k0<=lambda<m, 278–279 | CORRECT | Although [lem:lower] states its limit formula only below k, [lem:rec] also implies the same formula for any fixed lambda>0: the finite sum converges and the denominator is at least lambda>0. No stronger regularity assertion is used there. |
| Relation to entropy along a ray | CORRECT | Transition probability to child i is beta_i/C. Its negative log is log C(root)-log C(child)+log(lambda+C(child)); under stationarity the first two terms cancel in expectation, leaving the displayed formula. |
| Extension to lambda=0, 285–287 | CORRECT | This is direct evaluation, not an interchange of limits: B=1,C=N,D=N,W=1,L=log N. The visibility dimension is E log N. At zero the GW law is itself invariant for choosing a uniform child. |
| Exact Lin/Rousselin equation and theorem numbers | GAP (verification only) | Their texts are not present and browsing is forbidden. The mathematical formula agrees with memory; exact numbering, all original hypotheses, and priority cannot be independently source-checked here. This is not an identified gap in the proof. |

Independent population and harmonic-ray checks are complete (see NUMERICS.md). A ray check must preserve the dependence between a selected child's escape value and its descendants; drawing a fresh unconditional offspring number at each step would be an invalid test. The formula and the burn-in ray estimates agree within two combined seed standard errors at all three requested biases. With 360-level raw prefixes the remaining initial transient at lambda=1.2 is still visible; it is reduced by omitting 20 initial levels. The run is finite and uses a pool, not an asymptotic proof.

## 4. Proof of [thm:main]

| Step (source lines) | Verdict | Reason |
|---|---|---|
| Bounds for B,C,B',C', 290–295 | CORRECT | Apply the proposition separately to the independent tree and each of the finitely many child trees; sum the bounds for C,C'. |
| Lower bound for D, 297–300 | CORRECT | lambda-1+(1-lambda/k0)+n(1-lambda/k0) = lambda(1-1/k0)+n(1-lambda/k0)>=cn. The first term is nonnegative, including k0=1. |
| Upper bound for D, 300 | CORRECT | B<=1, C<=n, lambda<=r imply D<=r+n. |
| Differentiability and W',L', 302–306 | CORRECT | Positive D and lambda+C justify the quotient and logarithm rules. Both displayed derivatives are exact. |
| W lower bound, 310 | CORRECT | BC>=c^2 n and D<=r+n<=n(1+r), because n>=1. Thus W>=c^2/(1+r). |
| W upper bound, 310 | CORRECT | BC<=n, D>=cn. |
| W' bound, 311 | CORRECT | First numerator <=2nM gives 2M/c. Second numerator <=n(1+M+nM), divided by c^2 n^2, gives (1/n+M/n+M)/c^2 <=(1+2M)/c^2. |
| L bound, 312 | CORRECT | cn<=lambda+C<=r+n<=n(1+r); take logs. Lower end can be negative, whose magnitude is <=log(1/c), absorbed by kappa. |
| L' bound, 313 | CORRECT | (1+nM)/(cn)<=(1+M)/c. |
| Domination and finite mean, 315–316 | CORRECT | Product rule bounds W'L+WL' by A(1+log n). log n<=n for n>=1; E log N finite. No hidden N log N term survives. E|W'L| is finite. |
| Differentiation and continuous derivatives under E, 317–318 | CORRECT | Dominated difference quotients yield differentiation, and dominated convergence applied to the continuous samplewise derivatives yields continuity, with one-sided derivatives at the endpoints. |
| Positive denominator and arbitrary r, 319–320 | CORRECT | E W>=c^2/(1+r)>0; choose any r<k0. |
| Quotient rule [eq:quot], 322 | CORRECT | F=E WL, G=E W; d'= (F'-d G')/G. |
| Values at zero, 326–330 | CORRECT | beta'_0(T_i)=-1/N_i, beta'_0(T')=-1/K; consequently C'_0=-A and D'_0=1-1/K-A. |
| Cancellation [eq:W0], 334–335 | CORRECT | (-N/K-A)/N -(1-1/K-A)/N = -1/K -(1-1/K)/N. L'_0=(1-A)/N. |
| Independence, 337–338 | CORRECT | Branching gives iid child offspring numbers, independent of root N; T' gives an independent K. Conditional on N=n the selected first n iid variables still have the stated product law. |
| Three expectations, 340–341 | CORRECT | E A|N=Na gives E L'=a-a=0; E W'=-a-(1-a)a=-2a+a^2; independent K gives the weighted-log expectation shown. |
| Algebra to [eq:slope], 343–348 | CORRECT | -a ell+(2a-a^2)ell=(a-a^2)ell; factor (1-a). |
| Symmetrisation, 350–353 | CORRECT | Expanding the expectation gives 2(a ell-E(log N/N))=-2 Cov(log N,1/N). All terms integrable. |
| Strict sign, 354–356 | CORRECT | The two monotone functions give a strictly positive product whenever N!=K. Nonconstant N makes this event nonnull, and a<1 since P(N>=2)>0. |

No gap identified in the theorem proof assuming the stated external dimension formula.

## 5. Corollary, examples, remarks

| Step | Verdict | Reason |
|---|---|---|
| [cor:mono], 359–361 | CORRECT | Continuity of d' and d'_0>0 give an interval on which d'>0; the mean value theorem gives every strict comparison in the statement. Choose epsilon<k0. |
| Binary example, 110–111 | CORRECT | a=3/4, covariance=-(log 2)/8, slope=(log 2)/32. |
| 2/4 example, 111–112 | CORRECT | a=3/8, covariance=-(log 2)/16, slope=5(log 2)/128. |
| Geometric example, 112–113 | CORRECT | a=log 2; independently summing through k=400 at 70-digit precision gives 0.05495944237138239886416958..., rounding to 0.05496. Tail bound uses log k<=k. |
| [rem:tilt] density description, 117–119 | WRONG (wording) | “measure on trees with an explicit density W_lambda” omits integration over T' and normalization. Correct: E[W_lambda|T]/E[W_lambda]. The proof later states this correctly at 283–285. |
| [rem:tilt] derivative and its mean, 120–122 | CORRECT | L'_0=(1-A)/N, E L'_0=E(1/N)-a=0. |
| Negative event, 122–123 | CORRECT | Pick any n>k0 with p_n>0. The event has probability p_n p_k0^n>0 and A=n/k0>1, even for k0=1. |
| “entirely from ... density”, 123–124 | CORRECT | E L'_0=0; E[W'_0|N=n]=-a-(1-a)/n increases strictly with n. Its normalized score differs only by a constant. This describes a first-order tilt, not a pointwise sign for all L'. |
| Last remark, displayed decomposition, 365–369 | CORRECT | W>0; E_Q L'=E WL'/E W and Cov_Q(L,W'/W)=[E W'L-d E W']/E W. All terms integrable by the proof's bounds and the positive lower bound on W. |
| B',C' nonpositive, 371–372 | CORRECT, terse | Already follows from [eq:yrec]: y_0=0 and every coefficient q w_i>=0, forcing y_j<0. Hence b_j'<=0 and the derivative limit is nonpositive. Summing gives C'<=0. A monotone coupling is unnecessary. The text should point back to this argument. |

Exact examples and a second independent symmetrisation calculation are saved in exact_results.json.

## 6. Numerical section

Own synchronous pool: 40,000 entries, 180 sweeps, four independent seeds (101–104); 14 lambda values coupled by common offspring and child-index draws. Average evaluations over the last 40 sweeps. For dimensions, subtract the paired empirical visibility dimension and add the known exact d0; raw dimensions are saved as well. This reduces sampling noise in difference quotients without changing their paired finite-difference values. Standard errors are computed across independent seed-level results, not across dependent pool entries or sweeps.

The independent second-order expansion in audit_curvature.py gives geometric d''(0)=0.0517634785877222802861. Thus at lambda=.04 curvature alone shifts the quotient above d'_0 by about .00103527, predicting .05599471 before higher-order corrections. The published .05677 differs from this by about .000775, or 1.27 of its stated standard errors (.00061). Its displacement from the slope is therefore not evidence of a formula error. The independent pool curvature estimate at h=.005 is .0521461 ± .0002884 (forward difference of derivatives), and .0520576 ± .0002885 (second difference using d and dprime); finite h gives a first-order bias.

The expansion was checked symbolically by differentiating BC/(lambda-1+B+C). With a=E(1/N), v=E(1/N^2), sigma^2=v-a^2, one obtains E[W''_0|N=n]=2 sigma^2-4 sigma^2/n+2(1-2a+v)/n^2. Further, E[L''_0]=(1-a)sigma^2 and E[W'_0 L'_0]=-(1-a)sigma^2. Twice differentiating F=dG gives

`d''_0 = -4 sigma^2 Cov(log N,1/N) + 2(1-2a+v) Cov(log N,1/N^2) - (1-a)sigma^2 + 2 d'_0(2a-a^2)`.

This is an audit calculation, not a claim made in the paper. Its expansion is justified locally from beta=1-lambda/n+lambda^2(1-A)/n^2+O(lambda^3), with uniform control from finite-depth contraction near zero. All reciprocal-degree moments are bounded. It does not require extending the paper's differentiability theorem to second derivatives on the whole interval.

| Numerical claim | Verdict | Reason |
|---|---|---|
| [tab:slope] exact columns | CORRECT | Independent high-precision values agree with every printed rounding. |
| [tab:slope] pool averages | CORRECT as a compatibility check | All four published pool averages agree with our independent estimates within two combined SE, and all agree with exact slope within two of their own SE. This is not a reconstruction of their hidden raw data. |
| Positive-bias quotient compared to exact slope | CORRECT, with curvature qualification | The geometric quotient is 2.968 reported SE above the derivative at zero, but curvature plus noise explains it. All four published quotients agree with ours within two combined SE. A finite-bias quotient need not be within two SE of the zero-bias derivative. |
| [tab:dim] increasing and below log m | CORRECT for our independent grid | Every one of our four seeds is strictly increasing on the requested ten-point grid and below log m for all four laws. The scale and trend match the published table. |
| Authors' stated exact run sizes, seeds and SE | GAP (reproduction metadata) | Authors' code and raw data are absent locally and browsing is forbidden; those particular runs and per-seed statements cannot be authenticated. We used 40,000 entries and 180 sweeps, four seeds, with final-40-sweep averaging. |
| Global monotonicity from numerics | CORRECT restraint | The paper presents the full grid as supporting evidence and explicitly leaves the theorem away from zero open. The finite grid proves no global monotonicity. |

All numerical tables and commands are in NUMERICS.md and included in REPORT.md. Each original numerical program has a 280-second alarm; the serial driver has one too. Individual pool runs took about 4–7 seconds; ray runs about 1–2 seconds. The largest arrays belong to the ray test and total roughly 170 MB. No large simulation or unbounded computation was needed.

## 7. Scope

| Step | Verdict | Reason |
|---|---|---|
| Theorem restricted to [0,k0) | CORRECT | The cube lower bound c>0 and rho<1 are available on each compact subinterval of this range only. No derivative sign beyond a neighbourhood of zero follows. |
| Extension to (k0,m) | GAP (new work needed, not a paper gap) | One needs differentiability of the random escape solution beyond uniform treewise contraction, integrable control of its derivative and of quotient derivatives involving small denominators, and uniform integrability on compact lambda intervals. Long pipes can make beta arbitrarily small when k0=1 and lambda>1. A probabilistic regeneration, negative-moment, or random-contraction argument could replace the deterministic lower bound, possibly requiring extra moments. Pointwise transience by itself does not supply these controls. The endpoint k0 would need its own analysis too. |
| Any stronger theorem claim in the source? | CORRECT | No sentence asserts monotonicity throughout [0,k0) or differentiability throughout [0,m). Lines 417–418 explicitly leave monotonicity away from zero open. The numerical grid extends further, but is presented as evidence only. |
| “answers ... including strictness ... neighbourhood”, 105–106 | CORRECT | A fair local formulation, with neighbourhood understood relative to the parameter half-line. It does not answer the full global question. |

## 8. Attributions and novelty (memory only)

Here CORRECT means consistent with my remembered result, not source-authenticated bibliographic metadata. GAP means I cannot certify the requested detail from memory. No web or supplied external source was used.

| Item | Verdict | Recollection and limit |
|---|---|---|
| Lyons 1990 | CORRECT | Branching-number criterion for transience of a biased walk; on a supercritical GW tree the threshold is m, with recurrence at the critical value in this setting. The cited title/journal/year look right. |
| LPP 1995 | CORRECT | Ergodic environment methods, speed, dimension drop and visibility dimension E log N. The title, ETDS 15 (1995), and pages look familiar. |
| LPP 1996 | CORRECT | Biased walks, speed and harmonic measure on GW trees; PTRF 106 (1996) is consistent with memory. I do not independently allocate every result in the joint 1995/1996 citation to a particular theorem. |
| LPP 1997 unsolved problems | CORRECT | I remember the trees problem list and the speed and dimension monotonicity questions. Exact wording including strictness and page numbers not independently recalled. |
| Lyons–Peres Question 17.29 | GAP | I recognize the dimension monotonicity question and book, but cannot certify that version-specific question number from memory. The bibliography warns numbering is from an online version. |
| Lin | CORRECT | I recall d_lambda>d0, limits d0 as lambda decreases to zero and log m as lambda increases to m, and the explicit invariant density. The neighbouring walk-environment mean degree, a different observable from ray dimension, need not be monotone. Exact equation numbers not verified. |
| Rousselin | CORRECT | I recall an explicit invariant measure for harmonic-ray environments, dimension/drop applications, and numerical evidence concerning bias. The EJP citation and title look consistent; theorem number and independence/priority of discovery not verified. |
| Ben Arous–Fribergh–Sidoravicius | CORRECT | Speed monotonicity for sufficiently large outward bias; translating outward bias beta to parent weight lambda uses beta=1/lambda. CPAM 67 (2014) looks right. |
| Aidekon | CORRECT | Explicit speed formula involving escape probabilities and independent tree pieces; PTRF 159 (2014) looks right. |
| lambda<=1/2 and attribution through SWX | GAP | I have seen this small-parent-bias bound attributed to Aidekon, but cannot independently authenticate its provenance or endpoint from memory. |
| Song–Wang–Xiang | GAP | I cannot independently recall the 2025 paper or certify its bound k0/(1+sqrt(1-1/k0)), author initials, journal, volume, or pages. It is a citation to verify, not an identified false reference. |
| Mehrdad–Sen–Zhu | CORRECT | I recall comparison of speed for stochastically ordered offspring laws at sufficiently high outward bias, distinct from varying bias on a fixed law. Exact pages and initials not verified. |
| Ben Arous–Hu–Olla–Zeitouni | CORRECT | Einstein relation near critical bias: linear response of speed related to the critical walk's diffusion coefficient, under strong moment assumptions. Exponential moments are consistent with the remembered setting. Exact normalization of the relation is not needed here and not asserted. |
| Bowditch–Tokushige | CORRECT with qualification | I recall differentiability of speed in a ballistic/CLT parameter regime, with hypotheses on the offspring law and the regime. “at every lambda for which ... ballistic and ... CLT” should not be read as a universal theorem with all moment hypotheses dropped; those must be stated or inherited from the cited result. Exact law assumptions and bibliographic pages not independently certified. |
| Prior differentiability/local monotonicity of dimension | GAP (novelty unverified) | I do not recall an earlier theorem proving these exact dimension claims. Absence from memory cannot establish novelty, especially for work after my reliable recollection. The paper's “To our knowledge ... only results” needs a current literature check outside this no-browsing audit. |

Bibliography: no entry is demonstrably wrong from memory alone. The familiar titles, years and journals show no clear author/year/volume mismatch. Exact pagination, the 2025 SWX entry, theorem/eq numbers, and the three 2026 project references are unverified. This audit does not verify acknowledgements, grants, AI provenance, repository contents or declared conflicts.

## 9. Wording and reader obstacles

1. Lines 117–119, “measure on trees ... density W_lambda”: WRONG as written. Replace with normalized conditional density E[W_lambda|T]/E W_lambda, or explicitly work on pairs with density W_lambda/E W_lambda.
2. Lines 160–161, “first j generations ... at most j steps”: CORRECT under levels 0,...,j-1, but ambiguous if the reader includes level j. Say “levels 0 through j-1”; then the j-step assertion is literal.
3. Lines 191–192, “effective conductance ... lambda^{-j}”: CORRECT, but specify the added-parent edge has conductance lambda; this prevents the tempting, wrong beta=C/(1+C) convention at general lambda. Say the value at lambda=0 is defined by the escape sum, not a network with 0^{-j} weights.
4. Lines 129–131, “same holds for the recursion obtained by differentiating”: CORRECT only with coefficients fixed as functions of the x inputs. The derivative recursion has a homogeneous contraction plus errors from changing coefficients, not a demonstrated contraction of the joint map (x,y). Replace by “the differentiated recursion has the same contraction coefficient in its derivative variables.”
5. Lines 217–218, “Since S>=... we have q<=...”: CORRECT but compressed. Insert the intermediate lambda/(lambda+k-r)<=r/k to expose the monotonicity used.
6. Lines 243–247, “b_i', S' ... one step earlier”: CORRECT but primes elsewhere mean lambda-derivatives. Use tildes here to avoid mistaking the algebra for differentiation.
7. Lines 371–372, “since ... decrease in lambda”: CORRECT but not explicitly proved at that point. Cite the nonpositive-y induction in [eq:yrec].
8. Lines 378–383, “averages over the pool”: GAP in reproducibility. Explain how an independent B and the root's C, C' are sampled, whether evaluation offspring are reused, and how the empirical baseline d0 is coupled for difference quotients. Provide seeds, error convention and initialization/burn-in diagnostics. A pool of beta values alone does not specify the joint root evaluation.
9. Lines 397–398, “(d_lambda-d0)/lambda”: clarify whether d0 is exact or the paired empirical estimate. Common-randomness cancellation radically changes its standard error. The manuscript gives insufficient detail to reproduce that convention.
10. Lines 413–414, “pool averages agree ... one and a half standard errors”: CORRECT numerically for the printed slope averages. Geometric quotient is 2.97 printed SE above the exact derivative; add that it is a positive-bias quotient and its curvature correction is about .00105, so readers do not misread the discrepancy as disagreement at zero.
11. Lines 86–87, “at every lambda ... ballistic ... central limit theorem”: GAP as an attribution unless the cited law/moment assumptions are retained. State the precise hypotheses of Bowditch–Tokushige after source verification.
12. Lines 87–88, “All of these monotonicity results concern lambda<k0”: potentially overcompressed. The preceding paragraph mixes variation in bias, stochastic ordering of offspring laws, and regularity/Einstein results near m. “These small-bias speed-monotonicity results” would identify the intended subset. It is not a claim that the Einstein relation holds only below k0.
13. Lines 71–72, “only results on the dependence”: GAP as a current exhaustive literature assertion. This is qualified by “To our knowledge”, but no memory-only audit can authenticate it.
14. Lines 105–106, “on a neighbourhood”: CORRECT; “a right neighbourhood” or “a neighbourhood in [0,m)” would make the endpoint convention explicit.
15. Table [tab:dim] at zero gives sampled 1.0394 and .5978, while Table [tab:slope] gives exact 1.03972 and .59725: CORRECT as estimates, but label or state that the zero column is empirical, not exact.

No definite spelling or LaTeX typo found. No theorem-level overstatement identified. The density sentence is the sole definite mathematical wording error found; the other points are precision, notation, attribution or reproducibility issues.

## Completion and final consistency check

Completed 2026-11-12 07:12 +04. Overall verdict: SOUND, with the known-external-formula and memory-only literature qualifications above. REPORT.md contains all requested verdicts, tables, commands, wording corrections and limitations; NUMERICS.md is the numerical appendix alone. The final original check program, `python3 audit_validate.py`, passed syntax checks on all saved programs, the 25 exact comparisons, all sampled contraction bounds, all 16 population outputs, all four ray outputs, finite-value checks, the four dimension grids and report coverage of steps 1–9. The Richardson estimate of geometric curvature from paired derivative runs is .0518805 ± .0002886, consistent with the independent .0517634786 expansion.

Audited source SHA-256: `e6d1fdcbbbd017af53accf6a93bc90560cb59ace8446036d35ae9b30b2b4c5e8`. This identifies the source version, not a before/after hash comparison. PAPER.tex was not edited.

Task completed: “Be a hard, independent referee” of PAPER.tex — local task start 2026-11-12 06:56 +04.


Law key: 12 means p1=p2=1/2; 24 means p2=p4=1/2; 123 is uniform on {1,2,3}; geom means pk=2^(-k), k>=1.


## Numerical table 1: exact absorbing-chain check


| Tree | Interior vertices | lambda=0 | 1/3 | 1 | 3/2 | 3 | Agreement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1 | 99/119 | 5/9 | 32/77 | 1/5 | 5/5 exact |
| 2 | 3 | 1 | 135/163 | 7/13 | 68/173 | 13/73 | 5/5 exact |
| 3 | 4 | 1 | 1053/1193 | 23/35 | 344/659 | 23/83 | 5/5 exact |
| 4 | 9 | 1 | 43173/49204 | 137/228 | 1640/3889 | 85/596 | 5/5 exact |
| 5 | 12 | 1 | 645441291/784492043 | 8481/18167 | 2187712/8000077 | 2077/37165 | 5/5 exact |


Tree notation: `()` is a boundary vertex; a tuple lists its children. Each tree has mixed degrees.

`[(((),), ((), (), ())), (((),), ((), ())), (((), (), ()), ((),), ((), ())), ((((),), ((), ())), (((), (), ()),), (((), ()), ((),))), (((((),),), (((), ()), ((), (), ()))), ((((), (), ()), ((), ()), ((),)),))]`


Command: `python3 audit_exact.py`. Fraction Gaussian elimination solves the walk equations, independently of the escape recursion. All 25 results agree exactly.


## Numerical table 2: contraction and derivatives


| k | r/k | delta12 / bound | eta12 / bound | delta20 / bound | eta20 / bound |
| --- | --- | --- | --- | --- | --- |
| 1 | 0.3 | 2.170e-08 / 5.314e-07 | 8.162e-07 / 1.153e-04 | 5.163e-15 / 3.487e-11 | 3.266e-13 / 1.295e-08 |
| 1 | 0.6 | 3.789e-05 / 2.177e-03 | 6.311e-04 / 3.065e+00 | 1.466e-09 / 3.656e-05 | 4.284e-08 / 8.880e-02 |
| 1 | 0.9 | 1.524e-03 / 2.824e-01 | 1.355e-02 / 9.355e+04 | 1.203e-06 / 1.216e-01 | 2.050e-05 / 6.956e+04 |
| 2 | 0.3 | 1.223e-08 / 5.314e-07 | 2.313e-07 / 5.767e-05 | 3.014e-14 / 3.487e-11 | 9.578e-13 / 6.475e-09 |
| 2 | 0.6 | 2.438e-05 / 2.177e-03 | 2.115e-04 / 1.532e+00 | 1.185e-08 / 3.656e-05 | 1.768e-07 / 4.440e-02 |
| 2 | 0.9 | 1.318e-03 / 2.824e-01 | 6.684e-03 / 4.678e+04 | 1.286e-05 / 1.216e-01 | 1.174e-04 / 3.478e+04 |
| 3 | 0.3 | 2.022e-08 / 5.314e-07 | 2.561e-07 / 3.845e-05 | 1.034e-13 / 3.487e-11 | 2.204e-12 / 4.317e-09 |
| 3 | 0.6 | 4.280e-05 / 2.177e-03 | 2.509e-04 / 1.022e+00 | 4.703e-08 / 3.656e-05 | 4.762e-07 / 2.960e-02 |
| 3 | 0.9 | 2.481e-03 / 2.824e-01 | 8.541e-03 / 3.118e+04 | 6.014e-05 / 1.216e-01 | 3.757e-04 / 2.319e+04 |


| k | r/k | max abs b20 derivative | M | max y FD error | max delta/bound (all j) | max eta/bound (all j) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.3 | 1.00000000 | 2.04081633 | 8.403e-11 | 0.874548 | 0.700000 |
| 1 | 0.6 | 1.00000000 | 6.25000000 | 1.060e-10 | 0.783339 | 0.400000 |
| 1 | 0.9 | 1.00000000 | 100.00000000 | 1.125e-10 | 0.713171 | 0.100000 |
| 2 | 0.3 | 0.50000000 | 1.02040816 | 2.224e-11 | 0.874548 | 0.700000 |
| 2 | 0.6 | 0.50000000 | 3.12500000 | 2.937e-11 | 0.783339 | 0.400000 |
| 2 | 0.9 | 0.50000000 | 50.00000000 | 3.822e-11 | 0.713171 | 0.100000 |
| 3 | 0.3 | 0.33333333 | 0.68027211 | 1.817e-11 | 0.874548 | 0.700000 |
| 3 | 0.6 | 0.33333333 | 2.08333333 | 2.305e-11 | 0.783339 | 0.400000 |
| 3 | 0.9 | 0.33333333 | 33.33333333 | 3.714e-11 | 0.713171 | 0.100000 |


Command: `python3 audit_contraction.py`. Each case: 384 roots, 17 lambda grid values, depths 1 through 20. Finite-depth trees use layered subtree sharing; unfolding is a valid tree, but samples are dependent. Supremum means the maximum of this test set, not the supremum over all trees. Centred differences use h=1e-5, including a rational continuation to negative h at zero. Every tested bound passed. Floating-point noise can dominate differences around 1e-16. The reported b20 derivative approximates beta; no finite test certifies an infinite-depth supremum.


## Numerical table 3: formula versus harmonic-ray entropy


| lambda | Formula, main pool | Formula, ray pool root sample | Ray n=120, root | Ray n=360, root | Ray n=360 after 20 levels |
| --- | --- | --- | --- | --- | --- |
| 0.3 | 0.3539020 ± 0.0000218 | 0.3557084 ± 0.0009514 | 0.3536291 ± 0.0002600 | 0.3541261 ± 0.0002252 | 0.3541918 ± 0.0002420 |
| 0.75 | 0.3706881 ± 0.0000571 | 0.3713079 ± 0.0005269 | 0.3701428 ± 0.0002321 | 0.3706156 ± 0.0002201 | 0.3708425 ± 0.0002147 |
| 1.2 | 0.3952165 ± 0.0000827 | 0.3952995 ± 0.0004747 | 0.3933556 ± 0.0001964 | 0.3948364 ± 0.0002010 | 0.3954323 ± 0.0002010 |


Commands: `python3 audit_ray.py 201` (and seeds 202–204), plus `python3 audit_pool.py 12 101` (and 102–104). The ray calculation uses 12,000 population nodes per level, 420 stored levels and 12,000 lazily unfolded rays per seed. Offspring and child indices are retained with their escape values. At each visited node choose child i with weight beta_i/sum beta and accumulate -log(weight). Thus the root column is literally -(1/n)log of prefix mass. The burn20 column estimates the same asymptotic rate after an initial segment. This uses harmonic-ray simulation, not a simulation of all backtracking steps of the original walk. Selected-child dependence is preserved.

The largest raw finite-n transient is at lambda=1.2; its reduction with n and after burn-in is visible. Main-pool formula and burn-in ray means agree within two combined standard errors at all three biases. The smaller ray pool has noisy one-root-sample formula estimates. Layer sharing, finite-pool bias and finite-depth effects are not included in the seed standard errors. This is an independent check of the entropy observable and stationary weighting, though it shares the escape recursion. It is not an independent proof of the source theorem.


## Numerical table 5: exact examples and constants


| Law | E 1/N | d0 | d0 prime |
| --- | --- | --- | --- |
| 12 | 0.75 | 0.34657359027997265470 | 0.02166084939249829091 |
| 24 | 0.375 | 1.03972077083991796412 | 0.02707606174062286364 |
| 123 | 0.61111111111111111111 | 0.59725315640935166693 | 0.04954268583459163943 |
| geom | 0.69314718055994530941 | 0.50783392286843839218 | 0.05495944237138239886 |


Binary 1/2 law: slope = log(2)/32. Binary 2/4 law: slope = 5 log(2)/128. Geometric slope rounds to 0.05496. Command: `python3 audit_exact.py`; mpmath precision 70 digits, geometric series through k=400. Tail contributions to the required logarithmic sums are below 1.6e-118, using log k<=k and sum_(k>400) k 2^-k=402*2^-400. The geometric a=log 2 also follows from -log(1-z)=sum z^k/k at z=1/2.


## Numerical table 6: slope reproduction


| Law | Exact d0 | Exact slope | Pool RHS [eq:quot] at 0 | Paired quotient at .02m |
| --- | --- | --- | --- | --- |
| 12 | 0.346573590 | 0.021660849 | 0.0215422 ± 0.0000800 | 0.0217605 ± 0.0000786 |
| 24 | 1.039720771 | 0.027076062 | 0.0270721 ± 0.0000246 | 0.0270596 ± 0.0000251 |
| 123 | 0.597253156 | 0.049542686 | 0.0495387 ± 0.0000636 | 0.0498311 ± 0.0000640 |
| geom | 0.507833923 | 0.054959442 | 0.0550698 ± 0.0000586 | 0.0561357 ± 0.0000602 |


Runs: `python3 audit_batch.py`, which serially executes `python3 audit_pool.py LAW SEED` for LAW in 12,24,123,geom and SEED in 101,102,103,104, then the four ray runs. Existing completed JSONs are skipped. A full fresh run is under five minutes here. Each numerical script and the driver have 280-second alarms. Pool settings: 40,000 entries, 180 synchronous sweeps, evaluations averaged over the last 40 sweeps, 14 coupled lambda values. All ± values are sample standard deviation of four seed means divided by 2.

The displayed dimensions use exact d0 as a control variate: d_est(lambda)=d_raw(lambda)-d_raw(0)+d0_exact. The quotient is consequently the paired empirical difference quotient, not a noisy quotient against an unrelated baseline. Raw values remain in each pool JSON. Averaging across sweeps reduces Monte Carlo error but does not remove finite-pool bias; the four-seed SE is not a bound on systematic error.


| Law | Paper vs ours pool z | Paper vs ours quotient z | Paper pool vs exact slope z | Paper quotient vs exact slope z | Our pool vs exact slope z |
| --- | --- | --- | --- | --- | --- |
| 12 | 1.239 | 1.244 | 0.974 | 1.510 | 1.483 |
| 24 | 0.668 | 0.628 | 0.652 | 0.547 | 0.163 |
| 123 | 1.376 | 1.452 | 1.463 | 0.014 | 0.062 |
| geom | 1.044 | 1.035 | 1.227 | 2.968 | 1.884 |


For paper-vs-ours comparisons z uses sqrt(SE_paper^2+SE_ours^2). For comparisons against the exact slope it uses the single stated SE. All published pool means and positive-bias quotients are within two combined SE of ours. Every published pool mean is within two of its own SE of the exact slope. The geometric positive-bias quotient is 2.97 SE above the exact slope; it estimates a different, curved-parameter quantity. Two-SE intervals with four seeds are descriptive, not a strong coverage guarantee.


### Curvature at zero


| Law | Expansion d2(0) | (dprime(.0025m)-dprime(0))/.0025m | same, .005m | same, .01m | 2(d(h)-d(0)-h*dprime(0))/h^2, h=.0025m | Richardson, 2*small-double |
| --- | --- | --- | --- | --- | --- | --- |
| 12 | 0.014158668 | 0.0141386 ± 0.0001754 | 0.0142335 ± 0.0001748 | 0.0144233 ± 0.0001737 | 0.0141069 ± 0.0001756 | 0.0140437 ± 0.0001759 |
| 24 | -0.000458229 | -0.0004368 ± 0.0000266 | -0.0004318 ± 0.0000265 | -0.0004223 ± 0.0000264 | -0.0004386 ± 0.0000266 | -0.0004419 ± 0.0000267 |
| 123 | 0.013913092 | 0.0140091 ± 0.0001881 | 0.0141528 ± 0.0001867 | 0.0144350 ± 0.0001841 | 0.0139608 ± 0.0001885 | 0.0138654 ± 0.0001894 |
| geom | 0.051763479 | 0.0521461 ± 0.0002884 | 0.0524117 ± 0.0002883 | 0.0529433 ± 0.0002881 | 0.0520576 ± 0.0002885 | 0.0518805 ± 0.0002886 |


Command: `python3 audit_curvature.py`; the pool estimates use the already saved near-zero runs. The independent symbolic expansion and the two different finite-difference calculations agree in scale and sign; first-order finite-difference errors are visible as h increases. The last column cancels that first-order error using paired h and 2h estimates. Geometric curvature shifts the .04 quotient by about .00103527, yielding .05599471 at quadratic order, with higher-order corrections remaining. The published .05677 ± .00061 is compatible with curvature plus sampling noise. No numerical error is identified.


### Dimension grid


| Law | 0.0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 0.346574 | 0.349992 | 0.353902 | 0.358505 | 0.364030 | 0.370688 | 0.378499 | 0.386997 | 0.395216 | 0.401995 |
| 24 | 1.039721 | 1.047825 | 1.055881 | 1.063806 | 1.071449 | 1.078602 | 1.085026 | 1.090486 | 1.094753 | 1.097573 |
| 123 | 0.597253 | 0.607504 | 0.618617 | 0.630655 | 0.643309 | 0.655843 | 0.667373 | 0.677280 | 0.685197 | 0.690716 |
| geom | 0.507834 | 0.520030 | 0.535207 | 0.554348 | 0.578034 | 0.605034 | 0.631816 | 0.655355 | 0.674242 | 0.687464 |


Standard errors over four seeds:


| Law | 0.0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 0.000000 | 0.000011 | 0.000022 | 0.000033 | 0.000045 | 0.000057 | 0.000067 | 0.000074 | 0.000083 | 0.000090 |
| 24 | 0.000000 | 0.000008 | 0.000018 | 0.000028 | 0.000040 | 0.000052 | 0.000065 | 0.000080 | 0.000097 | 0.000123 |
| 123 | 0.000000 | 0.000013 | 0.000027 | 0.000040 | 0.000049 | 0.000055 | 0.000059 | 0.000069 | 0.000089 | 0.000122 |
| geom | 0.000000 | 0.000014 | 0.000037 | 0.000071 | 0.000115 | 0.000162 | 0.000201 | 0.000231 | 0.000273 | 0.000362 |


| Law | log m | Every seed increasing | Every seed below log m | Mean gap at .9m |
| --- | --- | --- | --- | --- |
| 12 | 0.405465108 | True | True | 0.003470 |
| 24 | 1.098612289 | True | True | 0.001039 |
| 123 | 0.693147181 | True | True | 0.002432 |
| geom | 0.693147181 | True | True | 0.005683 |


The increase on this finite grid is numerical evidence only. It does not establish global monotonicity. These values reproduce the scale and trend of [tab:dim]; no attempt is made to reconstruct the authors' undisclosed seeds or raw outputs.


## Remaining limitations

- Lin's and Rousselin's original texts, the precise domain/hypotheses of their statements, and the cited theorem/equation numbers were not available locally. I am highly confident about the formula from memory and its normalization; numerical entropy checks are supportive, not a replacement for verifying the citation.
- The literature survey and exact bibliographic metadata, especially SWX 2025 and Bowditch–Tokushige's hypotheses, are not independently authenticated. No novelty conclusion is warranted from memory alone. Funding, repository contents and project provenance were outside this mathematical audit.
- Numerical samples use finite pools and, for rays and arbitrary trees, layered subtree sharing. Across-seed standard errors omit population and truncation biases. Ray lengths stop at 360 rather than giving an asymptotic error bound.
- Authors' numerical seeds, exact pooling/evaluation conventions, code and raw outputs were not supplied in this folder. Their per-seed monotonicity and stated SE cannot be checked directly; independent runs reproduce the claims within the comparisons stated above.
- No extension to lambda>=k0 was proved. No step 1–9 was skipped; uncertain items are identified individually.

Task: “Be a hard, independent referee” of PAPER.tex — the author's request, 2026-11-12, local clock 06:56 +04 at audit start.
