Overall verdict: ACCEPT

I found no mathematical gap or counterexample in the argument as written. In particular, the signed estimate is valid under the common-uniform coupling, including flat pieces; sufficiency uses a valid approximation argument rather than mistaking a bounded moment for tightness; and necessity establishes Gaussianity in the correct Banach space before invoking Fernique. There is even a shorter proof of the signed estimate, with a better constant, given below.

This verdict concerns mathematical correctness, assuming the cited external theorems have the stated hypotheses and conclusions. No cited source text is supplied in this folder. In accordance with the instructions, I did not browse, fetch sources, or use the authors' code. Consequently, agreement with my recollection and correct use of the statements quoted in the manuscript must be distinguished from checking the exact wording, numbering, and versions against those sources. In particular, this report does not certify the source-verification assertion in the acknowledgements. The source-use audit at the end records this limitation explicitly.

All line references are to the supplied PAPER.tex, SHA256 `e5a894142d0911c941b99157f09d4efed1542ecef5958fd3f9ebd18120055664`. The input was not changed. The audit covered the definitions, all proofs, and the mathematical claims in the introduction and examples.

## Theorem 1.1 — SOUND (`thm:main`, lines 78–90; proof 349–351)

The equivalence follows from Theorems 4.1 and 5.1 without an additional hidden assumption. On this finite measure interval, the moment requirement in (a) is exactly the requirement that the displayed processes be L^p-valued: every finite real sample produces a bounded Q_n, and Q_n−Q belongs to L^p exactly when Q does. Thus the interpretation in line 90, which omits a separately imposed moment assumption, is correct. It is not claiming convergence of objects outside L^p.

The sign is consistent with inversion of the uniform empirical process. Changing −qB to qB changes no law. The mean identity is justified by Tonelli, not by convergence of empirical moments. No empirical uniform integrability is assumed in the statement or needed for this identity.

The point mass case has q=0, J_p=0, and an identically zero process, and is included. Arbitrarily placed atoms are not automatically allowed: atoms combined with support gaps may fail local absolute continuity. The theorem makes exactly this distinction.

## Lemma 2.1 — SOUND (`lem:measurability`, lines 112–118)

The inverse-transform identity Q(U)≤x iff U≤F(x) is valid for the specified generalized inverse, without continuity or strict increase. It proves the moment identity for extended nonnegative integrals as well as finite ones.

Sorting is a continuous map on R^n, including at ties. Sending the sorted coordinates to a step function on the deterministic cells ((k−1)/n,k/n] is continuous into L^p for every finite p. Translation by fixed Q and multiplication by sqrt(n) preserve Borel measurability. This establishes ordinary Banach-valued measurability and avoids an empirical-process outer-probability issue.

If the moment is infinite, boundedness of Q_n and the vector space property of L^p imply that Q_n−Q cannot belong to L^p, for every finite real sample. Endpoint values of step functions are irrelevant to L^p.

## Lemma 2.2 — SOUND (`lem:hardy`, lines 120–138)

The integration by parts takes place on [epsilon,1/2], where G is finite and absolutely continuous. The lower boundary term is −epsilon G(epsilon)^p and has the correct sign. It is discarded; there is no unjustified assertion that it vanishes at zero.

For p>1 the displayed Hölder estimate gives A≤p H^(1/p) A^((p−1)/p), with A finite on this compact interval. Division when A>0 gives A≤p^p H; the A=0 case is dealt with. For p=1 the direct integration argument is valid. Monotone convergence removes epsilon. The comparison t^p≤[t(1−t)]^(p/2) is correct on the left half, and reflection gives the right half. Adding does not create another factor of 2. Adding the finite constant h(1/2) then proves h∈L^p.

This lemma is important twice: it supplies the original law's moment in sufficiency and supplies finite moments for both monotone pieces in Proposition 3.1. There is no endpoint boundedness or finite total variation assumption hidden here.

## Lemma 2.3 — SOUND (`lem:monotone`, lines 152–169)

Part (i) is a deterministic order-statistic identity. A nondecreasing map preserves weak ordering, so the sorted transformed sample is a(U_(1)),…,a(U_(n)), whether or not values coincide. Strict increase and an atomless transformed law are unnecessary. Even continuity is unnecessary for part (i).

Part (ii) needs the stated continuity. For x<a(t), the sublevel set is an initial interval of length s≤t. If s=t>0, continuity at t would imply a(t)≤x, a contradiction. Thus its probability is strictly below t, whereas P(a(U)≤a(t))≥t. This proves that the specified left generalized inverse is exactly a(t), including endpoints of flat intervals. An empty sublevel set gives s=0 and causes no exception.

Continuity cannot simply be dropped from (ii): a jump can make the canonical quantile take the left value at a jump level when the chosen representative of a takes the right value. The manuscript does not drop it. In its applications a and b are locally absolutely continuous and hence continuous.

The use with the original Q invokes only (i), so it is valid even when Q itself is discontinuous. It gives the required coupling of empirical laws for arbitrary P.

## Proposition 2.4 — SOUND, subject to the stated source-verification limit (`prop:BL`, lines 175–182)

What I recall of Bobkov–Ledoux's estimate is

    E W_p^p(mu_n,mu) <= (5p/sqrt(n+2))^p J_p(mu),   p >= 1,

with J_p written in the spatial/density form involving [F(x)(1−F(x))]^(p/2)/f(x)^(p−1). Thus 5p, n+2, and the full real range p≥1 in this proposition agree with my recollection. I do not recall a restriction to integer p or to p≥2. This is a recollection, not a source quotation or verification of the cited theorem number.

The proposition is a quantile-form specialization of that statement, not a verbatim statement in its original notation. Under local absolute continuity of u, the cited change-of-variables identity gives

    J_p(nu) = integral_0^1 |u'(t)|^p [t(1−t)]^(p/2) dt.

On a monotone quantile u this is D_p(u). It is not legitimate to identify the spatial functional with the almost-everywhere derivative of an arbitrary discontinuous quantile: a Bernoulli quantile has zero derivative almost everywhere, but nonzero empirical error. The proposition's absolute continuity hypothesis excludes precisely that misuse. No direct application of the external theorem to a signed h is made.

The factor (n/(n+2))^(p/2) in Proposition 3.1 is not an additional premise of the external estimate. It results from multiplying this estimate by n^(p/2). The constant (5p)^p and this factor have each been multiplied exactly once.

The finite p-th moment assumption is supplied before each nontrivial application. When D_p is infinite the upper bound is merely infinite. When it is finite, local absolute continuity suffices, even if one were to interpret an external auxiliary inequality as initially requiring absolute continuity up to the endpoints: clip u at epsilon and 1−epsilon. The clipped function is globally absolutely continuous, has D_p no larger than D_p(u), and tends pointwise to u. For fixed n, its empirical transformed sample tends to the original sample, too. Fatou, first for the t integral and then for expectation, transfers the same bound. Thus unbounded endpoint behavior creates no missing extension step.

For mixed laws, an absolutely continuous quantile need not arise from a law having a Lebesgue density. Atoms produce flat pieces of u, on which u'=0. The proof uses the density of the absolutely continuous part only through the cited identity, not as an unstated assumption that the entire law is absolutely continuous. Whether Corollary A.22 and the exact source conventions say precisely what line 182 reports remains an unavailable-source check; I found no mathematical contradiction in that report.

## Proposition 2.5 — SOUND (`prop:uniform`, lines 186–193)

The statement allows a triangular array with independent uniforms within each row. It does not require independence of different rows. This distinction is essential: one cannot use nested ordinary samples or mutually independent rows and expect almost sure convergence to one fixed bridge. The special coupling in the proposition is sufficient for the distributional use in Theorem 4.1.

Independently of the precise Shorack–Wellner theorem number, the inverse step can be checked explicitly. Write alpha_n(x)=sqrt(n)(F_n(x)−x), beta_n(t)=sqrt(n)(V_n(t)−t). With no ties,

    beta_n(t) = −alpha_n(V_n(t)) + r_n(t),   0 <= r_n(t) <= 1/sqrt(n).

On any special construction with ||alpha_n−B||_infinity→0 almost surely, one has ||V_n−id||_infinity→0 and hence

    ||beta_n+B||_infinity
      <= ||alpha_n−B||_infinity
         + omega_B(||V_n−id||_infinity) + 1/sqrt(n) -> 0.

Continuity of B gives the last step. This confirms the sign and shows that there is no endpoint inversion problem. Alternatively, the needed distributional convergence follows from the uniform empirical functional CLT and inversion, with a separable interpolation for the representation.

For each n the supremum in the proposition is measurable: on each deterministic cell the expression is continuous, with one-sided limits at the cell boundaries, so a countable dense set and boundary limits determine the supremum. This does not require treating a nonseparable l^infinity process as an ordinary Borel random element.

## Lemma 2.6 — SOUND (`lem:gausslimit`, lines 197–203)

Convergence in probability implies convergence of characteristic functions. Unbounded variances would have a subsequence tending to infinity and force a characteristic function equal to zero away from zero, contradicting continuity at zero. A convergent subsequence of the bounded variances identifies the limiting characteristic function as exp(−sigma^2 s^2/2). A single such subsequence suffices to identify the already existing limit law. Variance zero is correctly included. There is no moment-convergence assumption.

## Lemma 2.7 — SOUND (`lem:gaussfunctional`, lines 205–211)

The weighted L^1 condition makes the pathwise absolute integral finite almost surely by Tonelli. Compactly supported continuous approximation in L^1(w_1 dt) follows by truncating the endpoints and values, then using ordinary L^1 approximation; the bound w_1≤1/2 transfers the approximation error. Continuous bridge paths turn the compactly supported integrals into limits of Gaussian Riemann sums, and the weighted error estimate gives convergence in L^1 of probability, hence in probability. Lemma 2.6 applies at both limiting steps.

As a separate check, bridge covariance obeys

    |min(s,t)−st| <= sqrt(s(1−s)) sqrt(t(1−t)).

Thus the double covariance integral is absolutely convergent and its absolute value is bounded by (integral |psi| w_1)^2. This also validates finite variance of the resulting Gaussian integral. Neither bounded psi nor integrable psi without its weight is needed. Compact support permits the usual zero extension at endpoints in the Riemann sums.

## Lemma 2.8 — SOUND (`lem:weightedbridge`, lines 213–222)

Joint measurability and the one-dimensional Gaussian moment formula give the equality of nonnegative extended integrals by Tonelli. The assumed finite right side then proves almost sure L^p membership; it is not inferred from membership alone.

For bounded r_k the multiplication map C[0,1]→L^p is bounded linear. On the measurable full-probability event Omega_0, dominated convergence gives norm convergence to rB. Restrict the maps to Omega_0 and extend the limit by zero, as specified in the statement; equivalently take the everywhere pointwise limit of 1_(Omega_0) r_kB. This explicitly verifies Borel measurability on the original probability space, without requiring it to be complete.

The lemma does not assert that an almost surely finite arbitrary Banach norm has finite expectation. Here the weighted assumption and Tonelli provide the expectation directly.

## Lemma 2.9 — SOUND (`lem:lawsL1`, lines 228–236)

Equality of L^1 laws gives equality of every finite vector of bounded test-function integrals. The cylinder sets are a pi-system. For finite p>1, separability of L^(p') supplies a countable norming set of bounded functions in its unit ball; bounded functions are dense there by truncation and, if necessary, normalization. Including all signs in that dense ball makes the supremum without an absolute value correct.

Every translated closed L^p ball is therefore measurable in the cylinder sigma-field. Separability of L^p implies that open sets are countable unions of closed balls contained in the open set, using dense centers and rational radii. The cylinder sigma-field consequently contains the Borel sigma-field; the reverse containment follows from continuity of the functionals. Equality of the L^p laws follows. For p=1 the inclusion is the identity. No claim that the inverse inclusion is continuous is made.

## Proposition 3.1 — SOUND (`prop:signed`, lines 242–266)

With oriented integrals, a and b may be negative to the left of 1/2; they are nevertheless nondecreasing because a'=g^+≥0 and b'=g^−≥0. They are finite at every interior point, continuous, locally absolutely continuous, and zero at 1/2. The fundamental theorem on each compact interval gives h=h(1/2)+a−b pointwise. Also D_p(a)+D_p(b)=D_p(h), including p=1. Lemma 2.2 gives the finite moments needed for the laws of a(U) and b(U).

The empirical quantiles for those two laws are a(V_n) and b(V_n). Flat portions create ties, but do not reorder any ranks; Lemma 2.3 explicitly covers them. Both samples are individually iid because each is a fixed transformation of the iid uniforms. The two transformed samples need not be independent of each other, and the external moment estimate never requires that independence.

For this fixed V_n,

    A_n(h_1+h_2)(t) = A_n h_1(t) + A_n h_2(t)

holds pointwise by algebra. Consequently A_nh=A_na−A_nb. This is linearity of composition with a fixed random map and subtraction of the original function. It is not the false assertion that sorting a sum or difference of arbitrary samples is linear. In particular, the proof never claims that h(V_n) is the empirical quantile of h(U_i) when h is nonmonotone.

Applying Proposition 2.4 separately and then |x−y|^p≤2^(p−1)(|x|^p+|y|^p) proves the displayed estimate with its stated constant. For nondecreasing h, g^−=0 almost everywhere and b is identically zero, so the sharper stated special case is correct.

An independent proof avoids even this decomposition. Define

    c(t) = integral_(1/2)^t |h'(r)| dr.

Then c is nondecreasing and locally absolutely continuous, D_p(c)=D_p(h), and c∈L^p by Lemma 2.2. Absolute continuity gives, for every s,t∈(0,1),

    |h(s)−h(t)| <= |c(s)−c(t)|.

Use s=V_n(t), integrate, and apply Proposition 2.4 to c. This proves the proposition with the factor 2^(p−1) omitted even for signed h. The manuscript's weaker bound is therefore sound. This strengthening is optional, not a required correction.

The preliminary definition of A_n uses actual Borel functions, which is adequate here. If one instead regards its input as an L^p equivalence class, changing a representative changes h(U_i) only on a null event for each fixed input; none of the proof uses simultaneous samplewise evaluation of every equivalence class.

## Theorem 4.1 — SOUND (`thm:sufficiency`, lines 270–307)

The first assertions use Lemmas 2.2 and 2.8 with their hypotheses satisfied. Coupling by Q(U_i) reproduces the law of the original sample, including atoms. No relation between the auxiliary bridge and these uniforms is needed for comparing marginal laws.

Step 1 is a valid weighted approximation. The bounded, interior-supported f_k tends to q almost everywhere and its weighted error tends to zero by dominated convergence. Extend f_k by zero before mollification. For sufficiently large k and delta<1/(2k), the mollification is smooth and compactly supported inside (0,1). Ordinary L^p convergence implies weighted convergence because w_p≤1. The error allocations 2^(−p)/m and the factor 2^(p−1) yield total error at most 1/m, as claimed. Values at a null exceptional set of the derivative do not affect this argument.

Integrating g_m gives a smooth Q_m constant near both endpoints. It need not be a quantile; A_n is already defined for all these functions. The locally absolutely continuous difference Q−Q_m has derivative q−g_m, so Proposition 3.1 gives a uniform-in-n bound on its entire empirical error. This controls the endpoint effects as well as the interior approximation. In particular, it controls cases in which an order statistic from one region is evaluated in another; it does not incorrectly identify endpoint error with a pointwise tail bound. Markov gives, for every epsilon>0,

    sup_n P(||A_nQ−A_nQ_m||_p > epsilon)
      <= C_p / (m epsilon^p) -> 0.

Lemma 2.8 gives the corresponding approximation of the bridge limits.

Step 2 applies the special construction only to compute the law for fixed m; it does not replace the original common-uniform coupling across different m. The Taylor remainder is bounded by ||g_m'||_infinity times sqrt(n)||V_n−id||_infinity^2/2. The special construction makes sqrt(n)||V_n−id||_infinity bounded almost surely, so this remainder is O(n^(−1/2)) along the coupling. Multiplication of the uniform quantile limit by bounded g_m gives convergence in L^p. This proves convergence of the approximants as random functions, rather than relying on point evaluations as continuous L^p functionals (they are not).

Step 3's triangle inequality is legitimate on the original space: it uses only couplings within Z_n,Z_(n,m) and within Y_m,Y. The middle comparison concerns marginal distributions and is supplied by Step 2. Hölder converts the two p-th moment errors into first moment errors. Take n→infinity for each fixed m, then m→infinity; there is no unsupported interchange of two limits.

Step 4 correctly scales to all bounded Lipschitz functions and uses the closed-set approximations max(0,1−k dist(z,C)). Their monotone decrease and boundedness give the closed-set portmanteau inequality. Thus full weak convergence, and consequently tightness, are proved. No separate finite-dimensional argument is missing. For p=1 every estimate remains valid.

## Remark 4.2 — SOUND (`rem:tightness`, lines 309–311)

A uniform p-th moment bound alone does not yield tightness in an infinite-dimensional L^p space. The remark correctly identifies the approximation bound as the additional ingredient. Its assertion about endpoint control refers to the small weighted-derivative approximation error, not to an unjustified compactness of a norm ball.

## Theorem 5.1 — SOUND (`thm:necessity`, lines 315–345)

Step 1 uses the continuous inclusion L^p→L^1 on a measure-one domain, and the assumed moment gives Q∈L^1. The random elements have the requisite Borel measurability.

Step 2 applies the two Beare–Kaji statements exactly as quoted: necessity first supplies local absolute continuity and J_1<infinity; sufficiency then identifies the L^1 limit law as −qB. Equality of the Stieltjes integral and integral q w_1 follows on compact subintervals from local absolute continuity, and then on (0,1) by monotone convergence of nonnegative measures. The step is not assuming J_p in order to identify the L^1 limit. For p=1 this completes the condition and limit identification; the mean follows directly by Tonelli.

Step 3 is the central point. Equality of L^1 laws gives centered Gaussian integrals against every bounded phi by Lemma 2.7 and J_1<infinity. For p>1, bounded truncations are norm dense in L^(p'), with p'<infinity. Hölder gives almost sure convergence of their pairings with the given L^p-valued Y. Lemma 2.6 then shows that every continuous linear functional of Y is centered Gaussian. This is the definition of a Gaussian Banach-valued random element. It proves Gaussianity of Y before assuming qB is L^p-valued. There is no circular invocation of Fernique and no illicit use of point evaluation on L^p. The p=1 case does not need this density argument.

Step 4 applies Fernique to a Borel Gaussian random element of the separable Banach space L^p. Degenerate Gaussian measures are included. The exponential moment of ||Y||_p^2 implies the p-th norm moment for every fixed finite p. Weak convergence alone would not provide this moment; Gaussianity is what provides it here.

Step 5 makes the transfer of that moment fully measurable. The scalar function min(|x|^p,M) is globally Lipschitz with constant p M^((p−1)/p), so its integral is continuous on L^1. Taking integer M→infinity makes N_p Borel, even on L^1 functions whose p-th integral is infinite. Equality of the L^1 laws therefore transfers the distribution and expectation of this nonnegative extended functional. Joint measurability of q(t)B(t) and Tonelli give

    E||Y||_p^p = E N_p(−qB) = c_p J_p(Q).

The left side is finite by Fernique. Since c_p>0, J_p is finite. This argument does not confuse almost sure L^p membership of qB with integrability of its norm; that otherwise serious gap is explicitly avoided.

Step 6 first invokes Lemma 2.8 only now that J_p is known to be finite. Lemma 2.9 then transfers equality of laws back to L^p. The stated alternative using sufficiency and uniqueness is also valid and is not circular, because sufficiency was proved without necessity.

Coverage of exceptional-looking laws is complete. Atoms become flat quantile intervals and cause no problem. Support gaps give quantile jumps, so are excluded by Beare–Kaji's local absolute continuity conclusion. Singular non-absolutely-continuous variation of the quantile is excluded by that same conclusion, not by pretending its a.e. derivative captures all variation. Unbounded support is handled on compact subintervals and by the endpoint integrals; no finite endpoint values of Q are used. A singular component of P can coexist with an absolutely continuous Q, and the proof imposes no prohibition on it.

## Corollary 6.1 — SOUND (`cor:wasserstein`, lines 353–363)

The moment hypothesis required by the one-dimensional transport formula has already been proved. The norm raised to the p-th power is continuous on L^p, so the continuous mapping theorem gives exactly the asserted convergence. The mean stated is the mean of the limit. The corollary does not incorrectly claim convergence of empirical moments from weak convergence alone.

## Remark 6.2 — SOUND (`rem:largep`, lines 365–371)

For p>2, p'=p/(p−1)<2. Writing q=(q sqrt(t(1−t))) [t(1−t)]^(−1/2) gives exactly the displayed Hölder bound. The second factor is integrable near both endpoints precisely when p'<2, so q is integrable there and Q has finite endpoint limits. This forces bounded support.

For Q(t)=(1−t)^(−beta),

    q^p w_p = beta^p t^(p/2) (1−t)^(−p beta−p/2).

The upper endpoint is integrable iff beta<1/p−1/2. The lower endpoint is harmless. This verifies the example and the strict inequality. At p=2 the Hölder endpoint test is inconclusive; the remark does not claim that all unbounded laws fail at p=2. Some sufficiently light unbounded tails can satisfy J_2<infinity.

## Example 6.3 — SOUND (`ex:laws`, lines 373–375)

1. Uniform: q=1 and J_p is a finite beta integral for every finite p.
2. Exponential: the upper-end integrand has exponent −p/2, so the strict condition is p<2. At p=2 the divergence is logarithmic.
3. Normal: Mills' asymptotic gives the displayed q and weight. At p=2 the endpoint integral is proportional to integral dt/[t log(1/t)], which diverges. For p<2 the power is integrable; for p>2 it is not. Thus the failure of L^2 process convergence follows from necessity. There is no claim that its unscaled Wasserstein distance fails to tend to zero.
4. Atom plus uniform: the quantile is continuous and piecewise linear, with derivative zero below theta and 1/(1−theta) above. It is locally absolutely continuous, has a finite derivative jump rather than a quantile jump, and has finite J_p for every finite p. Saying this law has no density means that the entire probability law has no Lebesgue density; it does have an absolutely continuous component. In context the distinction is clear.
5. Two atoms: the formula n^(p/2)|theta_n−theta| is exact up to null sets in t. The binomial CLT makes it n^((p−1)/2) times a variable converging to a nondegenerate absolute normal, so for p>1 the norms are not tight. At p=1 the norms can converge while the processes fail to be tight in L^1: the mass concentrates on intervals whose lengths tend to zero, violating the uniform absolute continuity of integrals required of L^1 compact sets. This is consistent with both the theorem and the W_1 norm result quoted in the introduction. The example restricts its direct non-tightness assertion to p>1, correctly.

## Independent computational checks

Programs: `referee_checks.py` and `referee_inventory.py`, written for this audit. Results: `referee_checks_output.txt` and `referee_checks_output.json`. No author program was read or executed.

The completed numerical run used one Python process, one numerical thread, batches of 24 samples, 89.84 seconds wall time, and 135.00 MiB peak resident memory. It spawned no workers. All saved artifacts are small; no computation approached 200 MB of writes or 1 GB RAM. Every program run is saved here. Preliminary script errors were corrected before the completed run; no estimates below come from a failed run.

The exact arithmetic check used h(t)=t(1−t), with

    a(t)=−(t−1/2)^2 for t<1/2, and 0 otherwise;
    b(t)=0 for t<=1/2, and (t−1/2)^2 otherwise.

These have flat portions and h=1/4+a−b. Exhausting 1,715 samples of sizes 1 through 6 from a seven-point rational grid, including repeated values, verified both transformed sorting identities and the signed increment identity with Fractions. This tests the precise coupling used in Proposition 3.1, not a false linearity of sorting h itself.

For simulation I used p=3/2, seed 20261114, and 3,000 independent samples at each n. The same uniforms generate the three laws within a replication; this creates dependence between columns, but does not affect their individual Monte Carlo standard errors. Samples at different replications are independent. Values shown as SE are estimated standard errors of the means, not confidence bounds or discretization errors.

The three distributions are:

- Atom: P=0.35 delta_0+0.65 Unif[0,1]. The cell integrals of |Q_n−Q|^p are evaluated analytically, including the cell crossing the atom level.
- Critical Pareto: Q(t)=(1−t)^(−1/6), a Pareto law on [1,infinity) with tail index 6. This is exactly the integral threshold for p=3/2; J_p diverges logarithmically.
- Beyond: Q(t)=(1−t)^(−1/5), tail index 5. This is just on the heavier-tail side; its derivative integrand has exponent −1.05 at the upper endpoint.

Both Pareto distributions have finite p-th moments, since p beta is 1/4 and 3/10, respectively. Thus every finite-n expected loss is finite, despite their infinite candidate bridge moments.

For the atom law, two independent integrations, an incomplete beta formula and adaptive quadrature of the derivative integrand, give

    c_(3/2) = 0.860039987325,
    J_(3/2) = 0.341407418931,
    E||qB||_(3/2)^(3/2) = 0.293624032250.

The Monte Carlo estimates are of E||sqrt(n)(Q_n−Q)||_p^p:

| n | Atom mean | SE | Critical Pareto mean | SE | Beyond mean | SE |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 0.279952888 | 0.003777 | 0.340427640 | 0.005408 | 0.545704255 | 0.01003 |
| 128 | 0.287736400 | 0.003896 | 0.427490030 | 0.006001 | 0.710104182 | 0.01146 |
| 512 | 0.293482241 | 0.003980 | 0.505101611 | 0.005571 | 0.867028909 | 0.01096 |
| 2048 | 0.291220563 | 0.003984 | 0.574605162 | 0.005951 | 1.024677000 | 0.01269 |
| 8192 | 0.292591766 | 0.003938 | 0.653411937 | 0.005620 | 1.203404230 | 0.01133 |

For the atom law the sharper monotone BL bound is (5p)^p (n/(n+2))^(p/2) J_p, not the signed bound with an unnecessary factor sqrt(2):

| n | BL upper bound | Bridge mean |
|---:|---:|---:|
| 32 | 6.70066869 | 0.293624032 |
| 128 | 6.93130185 | 0.293624032 |
| 512 | 6.99189634 | 0.293624032 |
| 2048 | 7.00723880 | 0.293624032 |
| 8192 | 7.01108670 | 0.293624032 |

There is no observed conflict with the bound; it is very loose. The atom estimates are compatible with the bridge mean.

For each Pareto law, the full BL bound is infinity and E integral |qB|^p is infinity. Reporting a finite upper bound obtained by silently truncating this integral would be incorrect. As a diagnostic only, the program also computes c_p integral_0^(1−1/n) q^p w_p:

| n | Critical truncated bridge integral | Beyond truncated bridge integral |
|---:|---:|---:|
| 32 | 0.155923876 | 0.226758812 |
| 128 | 0.236016301 | 0.356417812 |
| 512 | 0.316882585 | 0.496715013 |
| 2048 | 0.397941887 | 0.647437945 |
| 8192 | 0.479049416 | 0.809074148 |

These truncated quantities are neither the full bridge means nor asserted finite-n bounds or equalities. The entire endpoint cell is included in the empirical loss calculation. Critical growth of the diagnostic is proportional to log(n); beyond-critical growth has the power n^(p beta+p/2−1)=n^0.05. A separate scaling check of the last quantile cell gives the same power: M_n is of size n^beta and that cell's contribution is n^(p/2) n^(p beta)/n. The finite simulations show increasing moments, but moment growth alone would not prove failure of weak convergence; the necessity proof supplies that conclusion.

Pareto numerical integration uses s=1−t=v^12 and splits every cell at the zero of Q_n−Q. It therefore avoids both endpoint truncation and integrating across an interior absolute-power cusp. A 24-point Gauss rule was used for the reported means. Checks on three independent n=31 samples per Pareto law against a separate adaptive integrator gave:

    beta=1/6: max relative error, 16 nodes 8.44e−6;
              24 nodes 1.12e−6; 48 nodes 3.61e−8.
    beta=1/5: max relative error, 16 nodes 1.18e−5;
              24 nodes 1.58e−6; 48 nodes 5.06e−8.

These are validation cases, not a proven global quadrature error bound. Their errors are much smaller than the simulation uncertainty. As a check independent of the fractional-power integrator's main use, switching to p=2 and n=1 gives the analytic cell formula x^2−2x/(1−beta)+1/(1−2beta); the maximum absolute error for x=1,2,10 and beta=1/5 was 8.1e−13. Averaging that formula over an independent Pareto observation gives 2 Var(X)=0.208333333333, consistent with the separate elementary variance calculation.

The inventory program independently recovered all 17 numbered environments and their source lines, checked the unchanged input hash, checked the 15 saved simulation rows and finite BL comparisons, and checks that this report includes every result label.

## Corrections and outstanding checks

Required mathematical corrections: none found. There are no results marked GAP or ERROR.

No stylistic changes are requested. In particular, the switch between qB and −qB is harmless equality in law, the phrase permitting atoms is not contradicted by the two-atom example, and the extra moment hypothesis is explained correctly.

The following are precise checks or optional proof simplifications, not findings of false statements:

1. **Lines 175–182:** verify Theorem 5.3 and Corollary A.22 against the actual Bobkov–Ledoux source, including its conventions for mixed laws. The constant, n+2, and range agree with my recollection, and the local-endpoint extension can be justified by clipping as above. This audit could not perform the requested source-text comparison without a local copy or browsing.
2. **Lines 186–193:** verify the exact Shorack–Wellner theorem number. The proposition itself is correct; independence is within rows. If the authors intend independence across rows as well, that would be a false stronger statement and must be removed. The actual wording does not impose it.
3. **Lines 324 and 95:** verify the stated Beare–Kaji theorem numbers and version against the source. The two quoted statements are sufficient for every use here, and agree with my understanding of their result. The version/date and theorem numbering cannot be certified from a bibliography entry alone.
4. **Lines 242–265:** optionally replace the signed decomposition estimate by the total-variation primitive c above. It proves the stronger constant without 2^(p−1). Retaining the existing valid estimate requires no correction.

## Use of cited results

No external source below was available for direct inspection. “Consistent” means that the mathematical conclusion quoted in the manuscript is used with the hypotheses shown in the manuscript; it does not certify the exact source statement or a literature-priority claim.

| Citation and location | What the paper uses | Assessment |
|---|---|---|
| Bobkov–Ledoux, Theorem 2.10; lines 173, 257, 362 | One-dimensional W_p^p equals the L^p quantile difference | Consistent with the standard formula. Finite p-th moments are supplied before use. No assumption of a density is needed for this formula. |
| Bobkov–Ledoux, Theorem 5.3; lines 99–103, 175–182 | Expected empirical W_p^p upper bound with 5p/sqrt(n+2) | Consistent with my recollection and used only for continuous nondecreasing quantiles with finite p-th moment. The signed extension is proved separately. Exact source check outstanding. |
| Bobkov–Ledoux, Corollary A.22; line 182 | Spatial functional equals weighted quantile derivative integral | Applied only under local absolute continuity. This restriction is essential and is respected. Exact mixed-law/source conventions outstanding. |
| Bobkov–Ledoux, Proposition A.17; lines 92, 182 | Characterization of absolutely continuous quantiles by interval support and Lebesgue domination; local convention | The stated characterization is mathematically consistent: domination excludes gaps and singular-only support, while allowing atoms and singular components alongside a sufficient absolutely continuous part. Not needed as an extra premise in the proof. Exact citation not verified. |
| Bobkov–Ledoux, Theorem 4.6 and Proposition B.13; line 182 | Description of the proof behind the moment inequality | These are explanatory citations, not separately invoked lemmas in the new proof. The beta/order-statistic description and an absolutely continuous-function inequality are consistent with the claimed use; their wording was not checked. |
| Bobkov–Ledoux, Theorems 5.6 and 5.9; line 103 | Prior moment-rate necessity/lower bounds | Background only. The new necessity argument does not infer moments from convergence using these results. Exact descriptions unverified. |
| Bobkov–Ledoux, Theorem 5.2; line 97 | Restatement of earlier smooth-density L^2 theory | Background only; no new proof step depends on it. Exact assumptions unverified. |
| Beare–Kaji, Theorem 3.2; lines 95, 324 | L^1 convergence forces Property Q | The paper supplies Q∈L^1, an L^1-valued Borel limit and norm-topology convergence. It uses the asserted full necessity theorem, not merely a sufficient condition. Correct if quoted as stated. |
| Beare–Kaji, Theorem 3.1; lines 95, 324 | Property Q gives the L^1 limit −qB | Used after establishing Property Q, and only to identify the L^1 law. It is not misapplied to assert L^p membership. |
| Shorack–Wellner, Theorem 3.1.1; line 193 | Special almost sure uniform coupling for uniform empirical/inverse processes | The needed triangular-array form is mathematically sound. The inverse identity above checks the passage and the sign independently. Exact numbering/source wording unverified. |
| Csorgo (1983) and Vervaat (1972); line 193 | Supporting references for quantile approximation and inversion | No stronger assumptions are introduced through a separate application. The elementary inverse verification suffices once uniform empirical coupling is available. |
| Fernique (1970), Bogachev Theorem 2.8.5; line 336 | Gaussian Banach-valued exponential norm integrability | Correct standard use. Gaussianity, Borel measurability and separability have been established for Y in L^p first. No non-Gaussian or merely cylindrical object is substituted. Exact theorem numbering unverified. |
| Billingsley, Section 2; line 306 | Closed-set portmanteau criterion | Correct standard use in a metric space, with the required measurable random elements. The paper derives the inequality explicitly. |
| del Barrio–Gine–Matran (1999); line 95 | Criterion for the scalar sqrt(n) W_1 limit | Used only for background about the norm. It does not assert an L^1 process CLT from this norm statement. The distinction matters for two-point laws and is respected. |
| del Barrio–Gine–Utzet (2005), Mason (1984), Csorgo–Revesz (1978); lines 97, 374 | Earlier weighted/smooth-density theory and divergent normal L^2 case | Background and context, not load-bearing. The mathematical examples are checked independently above. Exact source hypotheses and the scope of the priority assertion cannot be verified here. |
| del Barrio–Gonzalez-Sanz–Loubes–Rodriguez-Vitores (2025), Theorem 2.4 and Section 7 Problem 2; line 97 | Prior sufficient conditions and the open question | The theorem proved here supplies the necessary and sufficient conditions described in the question. The precise wording, scope and version of the cited problem are unavailable, so the historical “answers Problem 2” assertion is not independently source-certified. |
| Math Brain paper, Math Brain repository, Brain framework repository; lines 380, 386 | Project/provenance statements | Not mathematical inputs to any argument. No correctness claim is inferred from them, and they were not accessed. |

Task: “You are refereeing a mathematical paper that has been posted” — request received 14 November 2026, approximately 01:08 Asia/Tbilisi (first local clock reading 01:08:58; an exact user-message timestamp was not exposed).
