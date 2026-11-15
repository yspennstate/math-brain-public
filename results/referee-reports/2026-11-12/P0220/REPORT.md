Overall verdict: SOUND WITH GAPS

I found no counterexample to the stationary representation, the finite determinant, the convergence bound, or either corollary. Independent exact enumeration, Young-lattice propagation, mean calculations, and simulations of the actual dynamics support those claims. The gaps identified below are repairable: the infinite construction needs a local path argument, the last block determinant manipulation needs a sign conjugation, and the proof of Lemma 3.3 needs a separate treatment of zero time. None requires changing a displayed probability formula.

Line numbers refer to the supplied PAPER.tex. I read the authors' programs and Lean source but did not run or import their programs. All referee programs and outputs are in this directory. No browsing, external source retrieval, other agents, or visible windows were used.

## Theorem 1.1 — GAP in the infinite path construction; finite claims sound

Lines 51–61 and 118–188.

The change of variables is correct. The full Jacobian matrix is triangular with diagonal entries exp(-t), exp(t), so its determinant is one. The drift disappears, the order of particles is preserved, and the transformed Poisson intensity is one. Conversely, (y,u) maps to (yu,log u), again preserving area. There is no missing intensity factor.

The restriction property for R^y_u at line 144 is correct. An event above y cannot change the tops at or below y. At an event v≤y, replacing a top above y has the same restricted effect as adding v when no top lies in (v,y]. This is also the reason that restricting patience sorting to values below a threshold preserves precisely those pile tops below the threshold. Consequently (2.1), the count identity, and (2.2), its inverse, hold pathwise.

Local finiteness and positivity follow from finiteness of the Poisson count in (0,y]×(0,u]. Lemma 2.1 implies that the count tends to infinity with y almost surely: apply its bound with fixed m≥j and let y tend to infinity, then use monotonicity and intersect over j. Thus every Y_i(u) is positive and finite, and the positions tend to infinity with i.

There is a genuine formulation gap at line 152. The Poisson process on the whole quadrant has infinitely many points in every nonempty u-time interval. Its time projection cannot be listed as successive event times. In particular the whole infinite set S_u is not a globally piecewise constant process with a next event. The finite rectangle constructions alone do not justify that sentence as written.

Fix: for any u_0>0, localize the first k particles on [u_0,u_1] to the random finite rectangle

    (0,Y_k(u_0)] × (u_0,u_1].

Static positions only decrease. Events to the right of Y_k(u_0) cannot affect these k particles. The rectangle contains finitely many events, so the usual successive-event construction applies. Restriction consistency identifies its paths with the sets already constructed from the origin. Taking countably many k and rational positive time endpoints gives simultaneous locally well-defined paths for all particles. This proves the claimed infinite process without imposing a nonexistent ordering of all points in the quadrant.

With that repair, the stationary construction is valid. At u=1, enumerate the strip's points by first coordinate as (Gamma_n,U_n). The marking property gives an independent rate-one Poisson process and iid uniform marks. A chain inside the rectangle is exactly an increasing subsequence of its marks. Therefore

    X_i = inf{y : ell_{N(y)}≥i} = Gamma_{tau_i},
    X_i>s iff ell_{N(s)}≤i-1.

This is a simultaneous identity for every index and every threshold, including s=0. The strict inequality in the survival event is correct even when s is a Poisson location: at that location N(s) already includes its point. The marked construction gives consistency in k directly; it does not require a separate marginalization argument.

The convergence and uniqueness claims follow from Proposition 2.3, audited below. Choosing A=exp(t/2) meets A<x_1 exp(t) for all sufficiently large t for each fixed x_1>0. For an arbitrary initial probability law, integrate the pointwise total variation convergence using its bound by one. Any invariant law must therefore equal pi. No unproved recurrence or regeneration assumption is being used.

## Theorem 1.2 — GAP in the final sign justification; formula sound

Lines 69–83 and 227–273.

The index ranges, marker set, kernels, and block signs in (1.4) are correct. Here is the full check of the reduction to the determinant.

1. If d=0, all indices are one, and the last condition is N(T)=0. The answer is exp(-T). For d≥1, conjugating the Young diagrams turns a first-row bound m_a into a bound of m_a on the number of nonzero parts. The empty configuration in the position encoding is exactly b=(0,...,d-1). Thus the ranges 0≤i,j≤d-1 in all four blocks are essential and correct.

2. At an earlier time s_a, the required occupied positions are exactly 0,...,d-m_a-1. If m_a=d this list is empty; if m_a=0 it contains all d base positions and forces the empty diagram at that time. All marker positions lie between zero and d-1. There is no missing marker at T, since the final bound is already enforced by using d particles in the conjugate encoding.

3. Markers are ordered by nondecreasing time, with arbitrary order inside a tie. The inequality in Q must be strict. For sigma_alpha=sigma_beta, Q_alpha,beta is zero, including its diagonal. A single path cannot select two different positions at the same time. Simultaneous occupation by different paths is recovered by the determinant, not by inserting zero-time propagators into Q. Permuting tied markers permutes both a row and a column of the full block matrix, leaving its determinant unchanged. The referee computations explicitly reverse each tied group.

4. The chain weight (4.1) has the correct normalization. The terminal determinant with parameter one contributes f^(lambda^r)/n_r!, and each interval determinant contributes f^(lambda^a/lambda^(a-1)) Delta_a^h_a/h_a!. Transposing the diagrams preserves both straight and skew tableau counts. No extra factorial or power of T is missing.

5. The cutoff semigroup P_u P_v=P_(u+v) holds exactly on indices 0,...,Lambda. All contributing intermediate positions lie between the two endpoint positions, so the upper cutoff loses no term. Cauchy–Binet uses increasing subsets at every stage, hence introduces no ordering sign. The diagonal insertion D_a gives a factor 1+w_alpha exactly when its site is occupied. The full squarefree coefficient therefore imposes every required occupation. Along a nonzero chain, positions increase coordinatewise, so the cutoff is equivalent to max y^r≤Lambda.

6. Expansion of K gives the matrices with tildes exactly as printed. In particular tilde Q=Q^transpose is strictly lower triangular, including zero blocks at tied times. Consequently its weighted geometric series terminates. The identities involving W are valid as polynomial identities; no analytic convergence in the auxiliary variables is needed.

7. Invertibility of tilde A is justified. Its product with diag(T^j) is the weighted Gram matrix with weights T^y>0. The vectors 1/(y-i)! are independent already on y=0,...,d-1. The assumed Lambda≥d is sufficient; Lambda≥d-1 would also suffice. Sylvester's determinant identity, det(I-W tilde Q)=1, and row multilinearity yield the full coefficient det(tilde F tilde A^(-1) tilde G-tilde Q). The Schur-complement signs in the next display are correct.

8. Removing the cutoff is legitimate at the probability level by monotone convergence, and entrywise at the determinant level because only finitely many entries occur and their defining series converge. Directly,

       sum_y p_1(y,i)p_T(y,j) = E_T(j,i),
       sum_y p_1(y,i)p_u(y,z) = E_u(z,i).

   The transposes printed at line 269 are correct. They must not be removed by falsely treating E as symmetric.

The small gap is the passage at line 271. The limiting block matrix is not the literal transpose of the stated block matrix: both off-diagonal blocks have the opposite sign. Let

    B = [[A,F],[-G,-Q]],    S = diag(I_d,-I_q).

The limiting matrix is S B^transpose S. Its determinant equals det B because (det S)^2=1. This supplies the missing sign operation. The displayed determinant equality is true, but transposition alone does not explain it. The exact cutoff test in referee_algebra.py verifies the coefficient, occupied-subset sum, and block determinant with two simultaneous markers.

The Bessel representation of E has the correct power u^((b-a)/2). For a≥b this follows by extracting the usual Bessel power; for a<b one must shift the series index by b-a. The definition by series handles u=0. Finally q=sum_(a<r)(d-m_a)≤(r-1)d, so the stated size bound follows.

## Reduction after Theorem 1.2 — SOUND

Line 85.

Sorting thresholds, merging equal times using the smallest particle index, and replacing each k_a by the suffix minimum do preserve the event. For the last operation, any later constraint also bounds every earlier value of the nondecreasing L. Conversely the new constraint at a is at least as strong as its old one. Removing earlier equal indices is therefore valid. The remaining indices are strictly increasing, giving at most k positive thresholds and d≤k-1. The bound k(k-1) follows, including k=1 where the special exponential case needs no matrix.

Joint upper-orthant probabilities determine the law: arbitrary coordinate subfamilies can be represented by setting unwanted coordinate thresholds to zero, and inclusion–exclusion recovers rectangular distribution probabilities. No density assumption is required. The computations include repeated indices at different times before dropping them and obtain the same answers.

## Corollary 1.3 — SOUND

Lines 87–98 and 277–287.

For one threshold J is empty. Conjugating [E_T(i,j)] by diagonal powers of T removes T^((j-i)/2); shifting both index ranges from 0,...,d-1 to 1,...,d changes no difference i-j. This gives the stated Toeplitz determinant.

For d=1, the single-time formula is exp(-T) I_0(2 sqrt(T)). For indices (1,2) there is one marker (s,0); the printed 2×2 matrix and its sign give exp(-T) I_0(2 sqrt(T-s)). At s=0 the first condition is automatic. At s=T the first condition implies no points up to T, giving exp(-T), consistent with I_0(0)=1.

The direct decreasing-sequence proof is valid: conditional on n points in the remaining rectangle there is exactly one decreasing relative order among n! orders. Multiplying this probability by its Poisson probability produces (T-s)^n/(n!)^2. This argument does not use the block determinant. Independent permutation enumeration checks both endpoints and interior cases below.

## Corollary 1.4 — SOUND

Lines 100–108 and 289–291.

Set tau_0=Gamma_0=0. The exponential spacings of Gamma are independent of the uniform marks determining tau. Conditional on tau, the mean of the selected sum of spacings is tau_i-tau_(i-1). The number of summands is random; the sum itself is not asserted to be independent of tau.

The pathwise occupation identity is exactly

    tau_i-tau_(i-1) = sum_(n≥0) 1{ell_n=i-1}.

The endpoints are n=tau_(i-1),...,tau_i-1. In particular the i=1 case includes n=0 and gives one. The LIS can increase by at most one, so there are no skipped levels. Tonelli justifies the expectation identity even before proving finiteness.

A direct geometric bound fills out the brief finiteness sentence at line 290. Conditional on n points uniform in a square, if ell_n< i then at least m-i+1 diagonal cells in an m×m grid are empty. Therefore

    P(ell_n≤i-1) ≤ binom(m,m-i+1) [1-(m-i+1)/m^2]^n.

This proves summability without an inverse-Poissonization argument. For i=2, ell_n≤1 is the decreasing order, of probability 1/n!, including n=0. Hence E tau_2=sum_n 1/n!=e, and E X_2=e. Integrating the nonnegative single-coordinate survival probability yields the stated integral for every i≥2.

The identification of c(i) is mathematically justified by the series quoted in the text. It can also be recovered without trusting that quotation. At insertion step j, the new card's value-rank is uniform on 1,...,j. Conditional on rank n+1, the preceding n smaller cards have uniformly random relative order. The new card goes to pile i precisely when these cards have LIS i-1. Thus

    P(card j goes to pile i) = (1/j) sum_(n=0)^(j-1) P(ell_n=i-1).

Summing over j gives E S_N(i)=c(i) H_N+O(1)=c(i) log N+O(1); the error is bounded using the preceding geometric tail. This establishes that the same constant governs pile growth and mean gaps. It also checks the shift from the paper's sum over n≥0 to the quoted sum over k≥i. Exact bibliographic wording of AD99 was not independently checked because its text is not among the supplied files and browsing was prohibited.

## Remark 1.5 — SOUND

Lines 110–112.

Lemma 3.1 has the ascending Schur-process weight: the skew factors are Plancherel specializations with parameters Delta_a and the terminal straight factor has parameter one. The exponential normalizing factor is exp(-T). The statement about an extended discrete Bessel determinantal process is consistent with this weight; the usual signed modified Frobenius coordinates use the particle/hole form of that process. The paper does not use this remark to prove (1.4), and no Fredholm determinant assertion is needed in the finite proof.

## Lemma 2.1 — SOUND

Lines 127–136.

Points chosen from occupied diagonal cells form a strictly increasing chain. A chain bound j-1 forces at least m-j+1 empty cells. The area of any specified union of that many cells is (m-j+1)yw/m^2, so its void probability is exactly the exponential printed. The union bound gives the binomial factor, even when more than the specified number of cells are empty. Boundary coincidences have probability zero. The case m=j=1 is exact.

## Lemma 2.2 — SOUND

Lines 158–164.

The map (y,u)↦(exp(c)y,exp(-c)u) preserves intensity and chains. Inverting this map on a rectangle gives the rectangle and the identity for Y'_i(u) printed in the proof. Multiplication by exp(t) gives X'_i(t)=X_i(t+c) simultaneously in t. This proves stationarity of all finite time and particle marginals, once the local path construction described above is supplied. Setting u=1 gives the final formula.

## Proposition 2.3 — SOUND

Lines 167–178.

The coupling is valid and supplies total variation convergence, not merely weak convergence. It does not rely on the two initial configurations being ordered.

For any fixed y<x_1, the started process has no particle in (0,y] at u=1. Its restricted configuration is the smallest min(k,#T) elements of the unbounded-pile construction T in that rectangle. Each of the three update cases in the proof preserves this assertion, including the case where T already has at least k elements and an event lies to the right of its kth element. Events above y are irrelevant. Thus there is no missing influence from the particles outside the rectangle.

The exceptional past rectangle has area y_*=A/exp(t). Its void event D has complement probability 1-exp(-y_*). On D, the two restricted constructions use identical points. If the stationary kth particle is at most y_*, their first k particles coincide exactly. The union bound therefore gives

    P(coupling fails) ≤ 1-exp(-A exp(-t)) + P_pi(X_k>A)
                      ≤ A exp(-t) + P_pi(X_k>A).

No independence of D and the last event is assumed or needed. With the usual probability convention TV=sup_B|mu(B)-nu(B)|, this is the stated bound. A coupling at each fixed t suffices; eventual coalescence on one fixed event is not required. Finite processes are nonexplosive because X_k(t)≤x_k exp(t), which bounds their integrated relevant-event rate on every finite interval.

## Remark 2.4 and the comparison with AD93 (42) — SOUND with a necessary finite-rectangle reading

Lines 63 and 186–188.

The combinatorial explanation is correct as far as the stated definition of B(i) goes. It should be written using finite rectangles rather than literally ordering every point in an unbounded strip by its second coordinate; such an ordering has no first point.

Here is a precise version. Keep the n smallest first-coordinate labels. Read these n points in increasing second-coordinate order and perform patience sorting. Restricting a larger finite input to these labels preserves its pile tops with labels at most n. The number of these tops equals the LIS length of the restricted input. Exchanging the two coordinates inverts its permutation, preserving increasing chains and exchanging the insertion and recording tableaux. This works simultaneously for all n by compatible finite restrictions. It gives the claimed joint-in-n count identity, hence the joint law of all limiting top labels and the tau_i.

Matching a separate one-dimensional distribution for each n would not suffice; the restriction argument is what establishes the joint assertion. The existing construction supplies that argument after localization. The actual displayed equation (42) and the definitions in the original AD93 notes are not included locally, so I cannot certify their exact transcription. Under the definitions the paper states, the asserted equivalence is justified.

## Lemma 3.1 — SOUND

Lines 194–203.

The Poisson increment probabilities are exp(-T) product_a Delta_a^h_a/h_a!. Conditional on the total n_r, relative order of the uniform marks is a uniform permutation independent of those counts. Its RSK recording tableau restricted to entries at most n_a has the prefix shape lambda(n_a).

For fixed intermediate shapes, the recording-tableau count is the product of the skew tableau counts. The insertion tableau can be any of the f^(lambda^r) tableaux of the terminal shape. Division by n_r! is therefore correct. Equal consecutive shapes have h_a=0 and skew count one; no strict-containment assumption is needed. Transposing fillings in the following paragraph preserves both straight and skew counts, with the conjugation on nu correctly placed.

This uses the ordinary first-row theorem of Schensted and the RSK recording-tableau restriction property. Greene's theorem is not invoked anywhere in this paper and is not needed. In particular, the proof does not identify the full pile-size diagram of patience sorting with an RSK shape.

Independent RSK insertion on all permutations through seven letters reproduced every checkpoint/final-shape count tested; see referee_algebra.txt.

## Lemma 3.2 — SOUND

Lines 205–217.

The positions are strictly decreasing in the original row index and nonnegative. Reversing them gives an arbitrary increasing d-element subset of the nonnegative integers; conversely its descending elements satisfy y_i≥d-i and recover a partition by subtracting d-i.

When the last d-m parts vanish, their positions are exactly d-m-1,...,0. Conversely, if those positions are present, they must be the d-m smallest positions and force the last parts to vanish. The cases m=d and m=0 give respectively a vacuous condition and the empty partition. The exact tests include both endpoints.

## Lemma 3.3 — GAP at u=0 in the written proof; identity sound

Lines 219–225.

For u>0 the proof is correct. Reversing both orders changes the determinant sign twice. Each nonzero permutation term has total exponent |mu|-|nu|. Aitken's factorial determinant then gives f^(mu/nu)/h! for contained shapes.

For noncontained shapes, choose i with nu_i>mu_i. Rows i,...,d vanish in columns 1,...,i. There are d-i+1 such rows but only d-i other columns, so every determinant term vanishes. This block-zero argument does not require Aitken's formula outside its domain.

The stated domain includes u=0, but the proof factors u^h before separating the noncontained case. That expression need not be defined when h<0. Fix: first prove the argument for u>0 and extend by continuity of the polynomial entries p_u, or handle u=0 immediately. At zero the matrix is [1{y_i=z_j}], whose determinant is one for identical position sets and zero otherwise. This gives the asserted result, using the standard constant-term convention 0^0=1 when mu=nu. No counterexample to the lemma results.

## Section 4 — status of the complete determinant proof

Theorem 1.2's section above checks every stage: chain weight, finite cutoff, Cauchy–Binet, same-time markers, nilpotent expansion, extraction, Schur complement, and limit. The only algebraic repair is the explicit conjugation at line 271. There is no illicit interchange of an infinite signed sum with a determinant, since all Cauchy–Binet operations are first performed at finite cutoff. Invertibility is proved at the cutoff, and need not be assumed for an unexplained infinite matrix.

## Sections 5–6 and the Lean certificate

The corollary proofs are audited above. The reported deterministic numbers in Section 6 were reproduced independently, including all twelve enumeration cases and the tail bound for the integral beyond 400. The authors' simulation output is a record of one random run; my different simulation provides an independent distributional comparison, not reproduction of those particular random numbers.

The Lean source states exactly

    det [[A,F],[-G,-Q]] = det A * det(G * inverse(A) * F - Q)

over a commutative ring, assuming an invertible finite matrix A. Its proof specializes Mathlib's block Schur-complement theorem and simplifies the two minus signs. This is the correct identity. It does not formalize the stochastic model, RSK, Aitken's formula, Cauchy–Binet occupation extraction, kernel series, or convergence. Nor does it establish invertibility of the particular probabilistic A. The sentence at line 306 accurately limits its claim to sign bookkeeping; it does not overstate the certificate.

No Lean or lake executable is available in this environment, so I inspected the source and supplied compilation log but did not independently recompile it. The supplied log reports success and only the usual propext, Classical.choice, and Quot.sound axioms. It is not a substitute for the mathematical audit above.

## Independent checks: programs, methods, and outputs

All scripts use one computational process and single-thread numerical-library settings. The largest sample array is 180000×4 doubles, about 5.8 MB. No computation approached five minutes or one GB; the main recorded runs took approximately 0.1–3 seconds each. Dependencies and local time are recorded in environment_info.txt. Programs are run from this directory, for example:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 referee_numeric.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 referee_growth.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 referee_dynamics.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 referee_algebra.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 referee_reported.py
```

### Exact finite combinatorics and signs

[referee_algebra.py](referee_algebra.py), output [referee_algebra.txt](referee_algebra.txt):

```text
Lemma 3.1: all permutations through n=7, 84 checkpoint/final-shape pairs: PASS
Lemma 3.2: 390 occupancy tests, including m=0,d: PASS
Lemma 3.3: 2502 exact determinants, including u=0 and nonnested shapes: PASS
Section 4: 98 exact finite-cutoff semigroup tests: PASS
Section 4 cutoff extraction: coefficient=occupied Cauchy--Binet sum=block determinant=18959/9216: PASS
Section 4 final transpose: requires diag(I_d,-I_q) conjugation; determinant unchanged: PASS
```

The skew counts here are computed recursively by removing corners, independently of Aitken's determinant. The finite-cutoff extraction uses d=2, Lambda=3 and markers (1/4,0),(1/4,1),(1/2,0), so it tests simultaneous markers as well as the signs.

### Forty-digit determinants and permutation enumeration

[referee_numeric.py](referee_numeric.py), output [referee_numeric.txt](referee_numeric.txt), evaluates E from its defining series and evaluates the full block matrix. Times are exact rational decimals. LIS profiles use the quadratic subsequence recurrence, not patience sorting. Every permutation of n≤9 is enumerated. The interval counts are summed with exact rational Poisson coefficients before multiplying by exp(-T).

For an enumeration cutoff M, the omitted mass is at most

    exp(-T) T^(M+1)/(M+1)! / [1-T/(M+2)]

when T<M+2, by bounding successive Poisson-term ratios. For T=1 and M=9 this bound is 1.1151548×10^-7. Every tested determinant lies between the truncated result and that result plus its tail bound. For example:

| Conditions (s,k) | Matrix size | Determinant | Determinant minus n≤9 enumeration |
| --- | ---: | --- | ---: |
| (0.2,1),(1,2) | 2 | 0.7265459314230440882327331404262134790621 | 3.0196539e-15 |
| (0.4,2),(1,2) | 1 | 0.8386125671260258169907256002818549338536 | 2.8169477e-14 |
| (0.2,1),(1,4) | 6 | 0.8182803652842047098086245267728721164543 | 1.8370580e-9 |
| (0.2,1),(0.6,2),(1,3) | 5 | 0.7873082896910016124276581496844668085354 | 8.6779228e-12 |
| (0.2,1),(0.6,3),(1,4) | 7 | 0.8171786641057253296490229859130151994955 | 1.1399460e-9 |
| (0.2,2),(0.6,2),(1,4) | 7 | 0.9307176022742552747060490383691603594062 | 6.2819402e-10 |
| (0.2,1),(0.6,1),(1,4) | 9 | 0.5487901790320082367312724177901578495707 | 1.7554808e-12 |

The table's final digits use the guard-precision comparison described below. The full output also includes intermediate bounds equal to the final bound, d=0, and the Gessel examples (d,T)=(2,1.5),(3,2),(4,3). These give respectively 0.9465534613831550368571, 0.9854111029208532689355, and 0.9927365798408176356276. Their enumeration deficits are below the stated Poisson bounds. The large-T enumeration intervals are intentionally wider; printing forty digits by itself does not establish forty digits of accuracy.

For the two-particle closed form, independent enumeration gives:

| s | T | exp(-T) I_0(2 sqrt(T-s)) |
| ---: | ---: | --- |
| 0 | 1 | 0.8386125671260258169907256002818549338536 |
| 0.25 | 1 | 0.7000414286023533924571577751462880660068 |
| 1 | 1 | 0.3678794411714423215955237701614608674458 |
| 1.75 | 3.5 | 0.1111860588313470293554994632061334231982 |

All are inside their independent enumeration intervals. Reversing every same-time marker group changes none of the determinants to the arithmetic precision tested.

### Independent multitime growth computation

[referee_growth.py](referee_growth.py), output [referee_growth.txt](referee_growth.txt), does not use skew-tableau determinants or the block formula to compute its comparison probabilities. It traverses the Young lattice by single-box edges. For a shape lambda of size n, the transformed mass

    g(lambda,t)=exp(t) n! P(lambda(t)=lambda)/f^lambda

evolves by exp(Delta B), where B adds a box with coefficient one. The program sums that finite series on shapes of total size at most 40, applies the first-row bound at every observation, and transforms back using hook-length dimensions. It uses 50-digit arithmetic to provide guard digits for the requested forty-digit comparison.

For T=1 the omitted probability is at most

    exp(-1)/(41! [1-1/42]) < 1.126529×10^-50.

The ten cases include r=2, r=3, equal indices at distinct times, jumps of indices by more than one, simultaneous marker times, empty marker groups, and d=0. They agree with the block formula to forty digits. The largest observed absolute difference is about 4.01×10^-50, attributable to rounding at the working precision as well as truncation; the Poisson bound is a bound on omitted probability, not a certified floating-point error bound. No directed interval arithmetic is claimed.

### Means computed two ways

The two methods in referee_numeric.py are:

1. Numerical quadrature of exp(-s) times the Toeplitz determinant on [0,600]. The integrated tail bound from Lemma 2.1 is minimized over m. Quadrature uses 40-digit working precision; it is not a formal interval integration.
2. Exact integer sums of (f^lambda)^2 for every shape of size n≤180 with first row at most i-1, divided by n!, then summed over n. Dimensions come from the hook-length formula on conjugate shapes. Integer counts are accumulated over a common factorial denominator, giving an exact rational truncated expectation. Counts through n=9 are checked against literal permutation enumeration.

For the second method let q=P(ell_30≤i-1). If ell_n≤i-1, each disjoint block of 30 entries must also have LIS at most i-1. Thus P(ell_n≤i-1)≤q^floor(n/30), and the remainder after n=180 is bounded by 30 q^6/(1-q). This is a deterministic truncation bound, independent of the Toeplitz determinant.

| Mean | Hook-length series | Discrete omitted tail | Integral omitted tail beyond 600 |
| --- | --- | ---: | ---: |
| E X_2 | 2.7182818284590452353602874713526624978 | 8.614e-194 | 5.741e-65 |
| E X_3 | 5.0906787293171656229786777199074984380 | 2.656e-100 | 1.286e-31 |
| E X_4 | 8.0865085847435762374876977784407933621 | 2.874e-55 | 4.629e-20 |

The displayed series and quadrature values agree to all printed digits; the rigorous integral tail alone only certifies the corresponding shorter accuracy. The exact rational series has the much smaller stated remainder. The resulting mean gaps are

    c(1)=1,
    c(2)=1.71828182845904523536...,
    c(3)=2.37239690085812038762...,
    c(4)=2.99582985542641061451....

The independent Catalan series for c(3) gives 2.3723969008581203876183902485548359402. The reported Section 6 tail bounds beyond 400 are reproduced as 1.91517e-174, 2.97606e-43, 9.25800e-21, and 8.01177e-13. In particular the paper's 8.1e-13 bound is valid.

### Direct particle dynamics and separate LIS/Gamma sampling

[referee_dynamics.py](referee_dynamics.py), output [referee_dynamics.txt](referee_dynamics.txt), simulates the particles themselves. Between jumps X_k grows exponentially; the integrated relevant-event rate for a delay h is X_k(exp(h)-1). The code consumes an exponential hazard budget, including across observation times, then chooses the event location uniformly in the interval up to the current X_k and moves the nearest particle to its right. It uses neither the representation nor a determinant to generate this trajectory.

Each k uses 180000 observations, spacing 2, after burn-in 50; 90 consecutive batches estimate sampling errors. Observed time after burn-in is 359998. Initial positions are X_i=10^-5 i for k=2, X_i=100 i for k=3, and X_i=i for k=4. The respective runs contain 979694, 1834812, and 2915636 jumps. A separate 180000 iid sample uses quadratic LIS dynamic programming and independent exponential spacings until the LIS reaches four.

| Method | E X_2 estimate ± batch SE | E X_3 estimate ± batch SE | E X_4 estimate ± batch SE |
| --- | --- | --- | --- |
| dynamics k=2 | 2.721235882 ± 0.0048737 | — | — |
| dynamics k=3 | 2.717918513 ± 0.0047772 | 5.089716094 ± 0.0069845 | — |
| dynamics k=4 | 2.724332212 ± 0.0047750 | 5.096634919 ± 0.0073187 | 8.091005247 ± 0.0094126 |
| iid LIS/Gamma | 2.715214058 ± 0.0048731 | 5.090521925 ± 0.0073828 | 8.091478081 ± 0.0083735 |

Representative survival comparisons:

| Conditions | Formula | dynamics k=2 | dynamics k=3 | dynamics k=4 | iid LIS/Gamma |
| --- | ---: | ---: | ---: | ---: | ---: |
| X_2>2 | 0.57549311 | 0.57626667 | 0.57623889 | 0.57700000 | 0.57528333 |
| X_1>0.5, X_2>2 | 0.42841589 | 0.42951111 | 0.42904444 | 0.42967778 | 0.42813889 |
| X_3>3 | 0.75460472 | — | 0.75438889 | 0.75626667 | 0.75350556 |
| X_1>0.2, X_2>0.6, X_3>1 | 0.78730829 | — | 0.78799444 | 0.78953889 | 0.78660000 |
| X_1>0.5, X_2>1.5, X_3>3, X_4>5 | 0.41666966 | — | — | 0.41952778 | 0.41568333 |

Full batch errors and standardized deviations are in the output file. The largest standardized deviation among these dynamics checks and all means is 2.564, for E X_1 in the k=4 run. The largest dynamics survival deviation is 2.220. These correlated multiple comparisons provide no material evidence against the formulas. They are numerical checks, not proofs of stationarity or of the representation.

### Reproduction of the paper's printed calculations

[referee_reported.py](referee_reported.py), output [referee_reported.txt](referee_reported.txt), independently evaluates all twelve Section 6 enumeration families, all twelve small-case closed-form comparisons, the integral-tail bounds, and the Catalan series. The largest enumeration deficit is about 1.78e-8 and every tail is below 1.116e-7, confirming the rounded assertions at line 297. The output includes the matrix sizes, including 14 for the five-threshold example. None of these calculations imports code/checks.py.

## Corrections

1. **Line 152; infinite process construction supporting Theorem 1.1.** Replace the assertion that the whole S_u is constant between Poisson points by the localized first-k construction on (0,Y_k(u_0)]×(u_0,u_1]. State local finiteness of relevant events and compatibility across k and positive time intervals. The global process has no successive list of all event times. In the update sentence use the pre-event configuration S_(u-), since the definition of S_u already includes points at time u.

2. **Line 271; last displayed determinant passage in Section 4.** Insert S=diag(I_d,-I_q) and identify the limiting block matrix as S B^transpose S. Transposition alone leaves the wrong off-diagonal signs. The probability formula (1.4) itself needs no sign change.

3. **Lines 220 and 224; Lemma 3.3 at u=0.** Prove the factorial-power argument for u>0, then use continuity, or give the delta-matrix argument at zero. Do not factor an undefined 0^h when h<0. State the constant-term convention at h=0 if treating zero directly.

4. **Lines 63 and 186–188; AD93 comparison.** State that the time-order reading and the inverse-permutation argument take place in finite first-coordinate restrictions, followed by the compatible limit. A literal increasing-time enumeration of the entire unbounded strip is unavailable. Make the simultaneous-in-n restriction argument explicit; a separate marginal equality at each n would not establish (1.1).

5. **Line 290; finiteness explanation in Corollary 1.4.** The claim is correct. For a complete self-contained justification, give the conditional diagonal-cell geometric bound displayed above rather than leaving “after Poissonization, or directly” as an unspecified argument.

No correction to the stated constants, the ranges in J or A,F,G,Q, the strict time inequality in Q, the threshold reduction, or the scope of the Lean claim is indicated by this audit.

Task: “You are refereeing a mathematical paper that has been posted.” Local session start: 12 November 2026, 18:07, Asia/Tbilisi, recorded in codex.log.
