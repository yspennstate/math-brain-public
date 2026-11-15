# Referee of FLOW section 11

Audited source: FLOW_SNAPSHOT.md, SHA-256 in SOURCE_SHA256.txt. The snapshot is the full FLOW.md read on 10 November 2026; the earlier FEIB10, FEIB12, FEIB14 and FEIB17 proof files were also consulted. All claims below concern section 11 unless stated otherwise. Entropies are in bits.

11(a): PROVED. Cardinality is a function of the erased spectral set, so the level witness is an upper bound for erasure entropy.

11(b): PROVED. A uniform bound for that witness at a largest weight gives FEI by restriction induction inside the threshold class.

11(c): PROVED. The dyadic grouping, superadditivity direction and displayed constant are correct; the general hypothesis must include K=0.

11(e): PROVED for the noise reduction and its displayed inequalities. FALSE for the separate Gaussian illustration's assertion of delta^2/pi at every correlation and height; a computed counterexample is below.

11(i): PROVED. Every induction case closes with closed windows, including endpoint atoms and weights equal to a.

11(j): PROVED. The stopped remainder has the required conditional symmetry and variance bound, the 1/8 is valid, and the covering gives 16/3.

11(k): PROVED, with its unspecified concentration constant supplied here by an elementary proof giving K_0=3. Independence and conditioning are valid. M_cs=80 is admissible.

Final theorem: PROVED. An explicit coefficient is 3/ln(2)+4+2 log2(1+2*1019.13), which is below 30.316 and hence below 31. No proof step uses the false Gaussian illustration.

Setting and small dimensions: PROVED after the standard representation normalization described below. Zero weights and ties are harmless once treated explicitly.

## Setting

Input sign changes make weights nonnegative, and a permutation puts a largest weight first. These operations preserve squared Fourier coefficients up to relabeling, hence preserve entropy and influence. Delete zero-weight coordinates, which add zero influence and no spectral mass involving them. If all weights are zero, the Boolean function is constant.

Every sign convention at equality has a representation with no ties: the finite set of nonzero margins has a positive minimum, and a sufficiently small threshold shift in the direction prescribed by the tie value preserves the truth table. This includes restrictions encountered during induction. An identically zero affine form represents a constant and is handled separately. “No ties” means w.x differs from theta for every full cube point; equivalently the remaining-coordinate sum s(y) never equals either endpoint ±a of the slab. It does not exclude repeated weights or repeated subset sums.

For a nonconstant function a>0. The equations D_1 f=1_S and E_1 f=sgn(s)1_(S^c) follow by evaluating s+a and s-a. The value assigned to sgn(0) in the second expression is irrelevant when s=0 lies inside S.

To check “delta=0 implies constant,” suppose coordinate j of weight b<=a has a pivotal edge with x_1=e. With r the sum over all other coordinates minus theta, this says |r+ea|<b. Fix x_j=e instead. If e=1, r+b belongs to (-a,-a+2b), a subset of (-a,a). If e=-1, r-b belongs to (a-2b,a), also a subset of (-a,a). Thus coordinate 1 has a pivotal edge. Since any nonconstant cube function has some pivotal edge, delta cannot vanish.

For n=1, a nonconstant threshold is a signed dictator; delta=1 and all A levels vanish, so its entropy and level witness are zero. For n=2, the only positive level is K=1; the choice rho=1/2 applies directly. The computation includes both dimensions, constants, equal weights and zero weights. Restrictions may become constant, which is the induction base case rather than a division by zero.

## 11(a), the witness

Let X indicate whether coordinate 1 belongs to the spectral sample, and V be the erased spectral set. Then E_1=H(X|V). Conditioning on |V| gives H(X||V|)>=H(X|V), since |V| is determined by V. The two masses at level k are precisely A_k and B_k. Their contribution is Phi(A_k,B_k), including the continuous cases where one mass is zero. Normalization is sum(A+B)=1. The use of E_1 for the scalar erasure entropy must be distinguished from E_1 f for the function obtained by averaging over coordinate 1.

## 11(b), the induction

The entropy drop is erasure entropy plus Jensen-Shannon divergence of the restricted spectra. The former is at most L_1. The latter is at most (2/ln 2)Inf_1. PROOFS.md includes a scalar differentiation proof of this constant, so this report does not simply assume the numerical bound from section 7. Influences of the other coordinates average under restriction, while querying coordinate 1 consumes Inf_1. Both restrictions are threshold functions, and their largest weight may be selected afresh at the next induction step. There is no requirement that a fixed coordinate remain largest. The induction is on dimension and terminates at constants.

## 11(c), two sequences

The inequality A log2(1+B/A)<=B/ln 2 follows from ln(1+u)<=u; A=0 is taken by continuity. Put g(A,B)=B log2(1+A/B). This is the perspective of a concave logarithm and is 1-homogeneous. Concavity plus homogeneity gives g(sum A,sum B)>=sum g(A,B), the direction needed for an upper bound after grouping. It is increasing in each argument: the B derivative has the sign of ln(1+u)-u/(1+u), which is nonnegative.

The beta_k are nondecreasing and belong to [0,1]. The intervals (2^(-j-1),2^(-j)] partition (0,1], including all boundary powers of two exactly once. A nonempty group is consecutive in k, possibly including intervening levels with B_k=0. If k_j is its first index, A_G<=A_(>=k_j) and the hypothesis bounds this by M delta/beta_(k_j)<=2^(j+1)M delta. For its last index l_j, B_G<=B_(<=l_j)<=2^(-j)delta. These two bounds and monotonicity give exactly the displayed g estimate. The algebraic step uses 1+2^(2j+1)M<=2^(2j)(1+2M). Summing gives 4+2 log2(1+2M), and the earlier summand adds 1/ln 2. One harmless endpoint edit: the source writes a strict inequality when replacing 1/beta by 2^(j+1); if M=0 both sides are zero. Use <= there, or dispose of M=0 separately. The proof and constant then cover that case too.

Levels with beta_k=0 have B_k=0 and zero Phi contribution, regardless of A_k. They need not be assigned a group, and no division by zero occurs. The hypothesis at K=0 is genuinely needed for general sequences: A_0=N, B_0=1 and all other entries zero satisfy every K>=1 condition with M=0, but Phi(N,1) grows without bound. This is also a planted false variant in verification.json. For threshold levels, A_(>=0)B_0=(1-delta)delta^2<=delta^2. Thus replacing a product constant valid only for positive K by max(M,1) is enough; the final M used here already exceeds 1.

## 11(e), the noise reduction

Stab_rho(v)=sum_k rho^k W^k(v) for 0<rho<1. On k<=K, rho^k>=rho^K, proving the low-level bound. On k>=K, 1-rho^k>=1-rho^K, proving the high-level bound. These inequalities include the endpoint level K and require neither a Boolean v nor nonzero mean.

For K=1, rho=1/2 gives prefactor rho^(-K)/(1-rho^K)=4. For K>=2, rho=1-1/K lies strictly between 0 and 1, and rho^K lies between 1/4 and 1/e. Separate upper bounds give 4/(1-1/e)=6.327906827477306<6.33 (constants.json). This is deliberately loose; it is nevertheless an upper bound.

The exact identity follows from half the mean squared difference of f0 across the exchangeable pair. A mixed support pair contributes squared difference 1; the two orientations have the same probability, so their total after multiplication by 1/2 is P[y not in S,z in S]. Opposite nonzero values contribute squared difference 4 and hence 2 Cross. Thus the expression is also delta-Stay+2 Cross. In particular its first term is at most delta, and Stay<=delta. Multiplying and applying Cross-Stay gives 6.33(1+2 M_cs)delta^2. Every factor and orientation agrees with the definitions in the source. The same rho suffices throughout; the parenthetical suggestion of different noise rates is unnecessary.

The Gaussian sentence is false as written. Take independent standard normal X,Y, theta=0, and S={|X|<epsilon}. With delta=P(S), Stay=delta^2 and Cross=2[(1-delta)/2]^2. Therefore Cross Stay/delta^2=(1-delta)^2/2 tends to 1/2, rather than 1/pi. verification.json records epsilon=0.001 giving 0.49920243388195795, versus 1/pi=0.3183098861837907. This is a concrete counterexample to the illustrative formula, not to the inequality needed by the theorem. The smallest edit is to delete that formula or restrict it to a properly stated limiting regime. No such asymptotic is needed in PROOFS.md.

## 11(i), Lemma A

The induction may include the empty sum: a positive left mass there forces alpha=c=0. In a step R=R'+w eps, translating the target and window produces the two displayed inequalities. Proving each with factor 2 is sufficient after averaging; it does not compound the factor with dimension.

The plus translation has center c+w and left endpoint alpha+w. For the minus translation with c>=w, both endpoints decrease by w and remain in the allowed order with a nonnegative center. With c<w, e=w-c belongs to (0,a], beta=alpha-w>=-e, and symmetry changes the negative center -e to e.

All three remaining cases work. If beta>=e use induction. If e-a<=beta<e, the interval [beta,beta+a] lies within [e-a,e+a]. If -e<=beta<e-a, its upper piece [e-a,beta+a] lies in that window. Its lower piece [beta,e-a) reflects to (a-e,-beta], which lies there because e<=a gives a-e>=e-a, and beta>=-e gives -beta<=e. Reflection preserves mass. The split pieces are disjoint, so any atom at e-a is counted once; the two mass bounds yield factor 2. At equalities one of the adjacent cases applies and the inclusions still hold. The third case can be empty, which causes no difficulty.

Weights equal to a are allowed throughout, since the only bound used is e<=a. Zero steps can be removed. Conditioning on magnitudes extends the result to independent symmetric bounded summands, as the source remarks. An open denominator window is not a valid variant: R takes ±a, c=0, alpha=a, and the numerator mass is 1/2 while P(|R|<a)=0. The closed window is essential here; in 11(k), absence of endpoint atoms is what permits its use for an open slab.

## 11(j), Lemma B

Take a deterministic ordering of the steps; no assumption on descending order enters. At first passage above t+a, the previous sum is at most t+a and the new step is at most a, giving S_tau<=t+2a. Conditional on each stopping event and its past, the unused signs remain independent and symmetric. Their variance is at most the total sigma^2. For sigma>0, symmetry gives P[remainder>2sigma]=P[|remainder|>2sigma]/2<=1/8. For sigma=0, the empty-sum case is trivial and the division is avoided.

The one-sided Lévy inequality is valid with the strict tail used here, even with atoms: after any first passage the remaining sum is nonnegative with probability at least 1/2, implying the final sum remains strictly above t+a. Summing over stopping events gives P[tau finite]<=2P[R>t+a]. PROOFS.md proves this directly, with no external reference required.

The event R>t+a+(a+2sigma) forces the remainder after passage to exceed 2sigma. Multiplying 1/8 by the Lévy factor 2 gives 1/4. Subtracting this far tail leaves at least three quarters of the original tail in (t+a,t+a+L], giving 4/3. Covering by ceil(L/a)<=2+2sigma/a closed length-a intervals costs factor 2 from Lemma A. Their left endpoints are at least t. The product is (4/3)*2*(2+2sigma/a)=(16/3)(1+sigma/a). At shared endpoints the cover can overcount, which preserves the upper bound.

## 11(k), Cross-Stay and constants

The refresh construction gives E[y_j z_j]=rho, and all coordinate pairs are independent. The set T is drawn independently of the entire original y. Conditional on T and the unrefreshed signs, the two sums over T are independent identically distributed symmetric sums. Replacing those unrefreshed signs by their statistic A still gives this description, because their sum alone changes the common translation; the law of the refreshed sums is unchanged.

The expression 2 P[U>=a-A]P[U>=a+A] counts the two cross orientations and uses symmetry of the second sum. The larger of these two thresholds is a+|A|, so the product of probabilities is at most that upper-tail probability. Endpoint atoms are excluded by the no-ties hypothesis on the original full threshold, for every fixed unrefreshed assignment; the same holds on each fiber of A. Lemma B applies at t=|A|. Its window centered at |A| has the same mass as the window centered at -A by symmetry. That is precisely the conditional slab probability.

Averaging over A at fixed T gives delta, because T is independent of y. This justifies factoring out delta before averaging the scale factor 1+sigma_T/a. Jensen then bounds E sigma_T by sqrt(E sigma_T^2)=sqrt(1-rho) sigma. There is no assumption that the slab event is independent of the unrefreshed sum A.

For Stay, condition on (T,y). The chance that the new z lies in the slab is bounded by Q_T, a function of T only. Thus E[1_S(y) Q_T]=delta E Q_T, again by independence of T and y. Conditioning only on the amount of noise, or selecting T after seeing y, would not justify this identity. Empty T has sigma_T=0 and is handled by Q_T<=1.

The source's Kolmogorov–Rogozin invocation is qualitatively legitimate: an individual Bernoulli summand has concentration 1/2 at interval length w_j, since its two atoms are separated by 2w_j. It does not specify an admissible numerical constant. PROOFS.md supplies an independent triangular-Fourier-kernel proof of Q_T<=min(1,3a/sigma_T), including closed intervals. This establishes K_0=3 without citing an unspecified theorem constant. The elementary kernel bound is (24/23)^2 sqrt(2pi)<3; the exact rational check using pi<22/7 is in verify.py.

For the Chernoff step, Z=sigma_T^2/a^2 is a sum of independent terms in [0,1], with mean x^2. The convex-chord estimate for exp(-u Z_j), followed by Markov with u=ln 2, gives a lower-tail exponent (1-ln 2)x^2/2, stronger than x^2/8. The stated exponent is therefore safe. Splitting at sigma_T^2=x^2 a^2/2 yields the displayed Stay bound. At x=0, interpret the min term by continuity and use the trivial bound directly.

To bound the final supremum explicitly, set b=3 sqrt 2. The concentration term contributes at most 1+b, and the Gaussian exponential term contributes at most 1+2 exp(-1/2). Therefore the supremum is at most 2+3 sqrt 2+2 exp(-1/2)=7.455702006544552. Multiplication by 32/3 gives 79.52748806980856<80. These values are in constants.json. This proves M_cs=80. A floating numerical maximization in verification.json returns supremum about 5.795210950198137 at x=3 sqrt 2, corresponding to 61.815583468780126; this numerical optimization is not used as a certificate.

With M_cs=80, M=6.33*161=1019.13=101913/100. Applying 11(c), 11(a), then 11(b), gives C=30.315745145395 bits per unit influence, evaluated from the exact expression. The proved safe coefficients 30.316 and 31 follow. M>=1 also covers K=0. This completes the theorem rather than leaving an unresolved constant or a quoted concentration estimate.

## Computational audit and limits

RESULTS.md reports the final scopes and extremizers. Exact integer sums determine every truth value; half-integer thresholds remove ties. Integer Walsh numerators give exact dyadic Fourier masses in the dimensions tested. Logarithms, square roots, evaluations in rho and polynomial stationary roots use floating point. This is exact enumeration of cube points, not a claim of exact algebraic optimization over every real rho or every real weight vector.

Independent checks use full-function transforms, edge counting, direct bitwise noise averaging, and exact rational enumeration of small pair laws. The latter check does not reuse the Walsh noise identity. The endpoint false variants and clean controls in verification.json ensure that the test detects an open-window error and the omission of K=0. No model comparison or brain-versus-no-brain experiment was run; the test-rigor cards were read before constructing the audit.

No proved bound was exceeded. The new empirical L_1 and product maxima exceed those in 11(g); the older claims are explicitly scoped to the samples then run, so these are new observations, not counterexamples to those sample reports. The Gaussian formula is the only false mathematical assertion found in the requested material. The theorem's proof stands after that illustrative sentence is removed and its constants are made explicit.
