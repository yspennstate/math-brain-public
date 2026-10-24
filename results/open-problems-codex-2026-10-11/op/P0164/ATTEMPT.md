# P0164 - partial results, 2026-10-11

## Statement and scope

The source is Pritish Kamath, Ravi Kumar and Pasin Manurangsi, *When Majority Fails: Tight Bounds for Correlation Distillation Conjectures*, arXiv:2604.06590v1, 8 April 2026. Conjecture 1 on PDF p.4 says: for every odd n, unbiased linear threshold f:{-1,1}^n -> {-1,1}, and 0<rho<1,

    Stab_rho(f) >= (2/pi) arcsin(rho).

LITERATURE.md records its exact quotation and the search limitations. This is NOT the false comparison with finite-dimensional majority. The full conjecture is NOT proved here.

X is uniform on the cube. The coordinate pairs (Xi,Yi) are independent, with uniform marginals and E XiYi=rho. Stability is E[f(X)f(Y)]. The source defines thresholds as sign(sum wi xi). With a fixed sign at zero, balancedness rules out any zero weighted sums: nonzero sums cancel in antipodal pairs, while zero sums all receive the same output. Thus f(-x)=-f(x). Signed coordinate changes make the weights nonnegative and preserve stability. Adding unused coordinates preserves stability, so the odd-n restriction is harmless.

Standard affine balanced thresholds also have such a homogeneous representation. First perturb the affine threshold into a strict gap while preserving the finite truth table (possible under a constant sign convention). Half of the values of sum wi xi lie on either side. Symmetry makes the two middle order statistics negatives of each other. Strict separation excludes a zero middle value; the central gap contains zero and the homogeneous threshold has the same truth table. Input-dependent arbitrary rules for zero ties are excluded.

## 1. Fourier and influence identities

For S subset [n], let chi_S(x)=product_{i in S} xi and hat f(S)=2^(-n) sum_x f(x)chi_S(x). Orthogonality gives sum_S hat f(S)^2=1. Independence gives E chi_S(X)chi_T(Y)=0 when S differs from T, and rho^|S| when S=T. Therefore

    Stab_rho(f)=sum_k Wk rho^k,  Wk=sum_{|S|=k} hat f(S)^2.

Here Wk>=0, sum_k Wk=1, W0=0 for balanced f, and Wk=0 for even k when f is odd (substitute -x in its coefficient).

Let Inf_i=Pr[f(X) differs from f(X with bit i flipped)], and I=sum_i Inf_i. The squared value of (f(x)-f(x flipped at i))/2 is the change indicator. Its Fourier expansion retains exactly terms with i in S, so Inf_i=sum_{S containing i} hat f(S)^2 and I=sum_k k Wk. For monotone f, conditioning on the other bits gives E f(X)Xi=(f(xi=1)-f(xi=-1))/2 averaged over those bits, equal to Inf_i. Signed coordinate changes give the corresponding formulas for unate functions.

## 2. Explicit near-one regime in all dimensions

**Theorem A.** Let f be any unate Boolean function on odd n variables, and put

    m_n=n binom(n-1,(n-1)/2)/2^(n-1).

For 1-8/(pi^2 m_n^2) <= rho < 1, stability is at least (2/pi)arcsin(rho). In particular it suffices that 1-rho <= 8/(pi^2 n). Balancedness is unnecessary for this theorem.

**Proof.** Make f monotone by signed coordinate changes. Set T=sum_i Xi. Then

    I(f)=E[f(X)T] <= E|T|.

For odd n, sign(T)=Maj_n, so E|T|=E[Maj_n(X)T]=I(Maj_n). A bit is pivotal for majority exactly when the other n-1 bits sum to zero. Thus E|T|=m_n. Also E|T|<=sqrt(E T^2)=sqrt(n) by Cauchy-Schwarz.

Put delta=1-rho. For k>=1,

    1-rho^k=delta(1+rho+...+rho^(k-1)) <= k delta.

The degree-zero difference is zero. The Fourier identity consequently gives

    Stab_rho(f) >= 1-I(f)delta >= 1-m_n delta.

Let t=arccos(rho), between 0 and pi/2. Integrating sin(u)<=u yields 1-cos(t)<=t^2/2, hence t>=sqrt(2 delta). The assumed delta bound implies

    m_n delta <= (2/pi)sqrt(2 delta) <= (2/pi)t.

Thus stability is at least 1-(2/pi)arccos(rho)=(2/pi)arcsin(rho). Replacing m_n by sqrt(n) gives the simpler sufficient condition. QED.

Jensen also gives the global estimate Stab_rho(f)>=rho^I(f)>=rho^m_n: the function k -> rho^k is convex, and Wk are probability weights. This does not prove the full arcsine comparison.

## 3. Entire interval for at most five essential variables

**Theorem B.** Every odd unate Boolean function on at most five essential variables satisfies Stab_rho(f)>=(2/pi)arcsin(rho) for 0<=rho<=1. This includes the thresholds of the problem in these dimensions.

### Complete combinatorial classification

Pad to five bits and make f monotone. Identify x with its set A of positive coordinates; call A winning if f(x)=1. Exactly one of A and its complement wins, by oddness. Winning sets are closed under taking supersets, by monotonicity. The empty set loses and the full set wins.

If a singleton {i} wins, all sets containing i win, and all sets missing i lose because their complements contain i. This is a dictator.

Otherwise all singletons lose and all four-element sets win. The function is determined by its family E of winning pairs: a triple wins precisely when its complementary pair loses. Two winning pairs must intersect, since disjoint winning pairs A,B would imply B subset A^c and make both A and A^c winning.

An intersecting edge family is a star or a triangle. To prove this, choose two distinct edges {a,b},{a,c}. If every edge contains a, the family is a star. Otherwise an edge meeting both and missing a must be {b,c}. Any edge meeting all three edges of this triangle must itself be one of them: an edge with an outside vertex cannot meet the opposite edge. Therefore the complete list, up to permutations, is empty E, stars with 1,2,3,4 edges, a triangle, and a dictator. There are respectively 1,10,30,20,5,10,5 labelled functions, totaling 81.

Conversely each listed family defines a monotone odd function. The only nontrivial inclusion is a winning pair A contained in a triple B. If B lost, its complementary pair would win and be disjoint from A, impossible. All other inclusions follow from sizes and the losing singletons/winning quadruples. Thus the classification is complete independently of numerical enumeration.

### Exact spectra

The coefficients (64 W1,64 W3,64 W5) are:

| Type |64 W1|64 W3|64 W5|
|---|---:|---:|---:|
|empty E, majority of five|45|10|9|
|one pair|44|16|4|
|two-edge star|45|18|1|
|three-edge star|48|16|0|
|four-edge star|53|10|1|
|triangle|48|16|0|
|dictator|64|0|0|

Here is a complete exact calculation procedure. Encode positive-coordinate sets as masks x=0,...,31. For E, define f_E to be -1 on sizes at most 1, +1 on sizes at least 4, +1 on a pair exactly when it belongs to E, and +1 on a triple exactly when its complementary pair is not in E. For every mask s form

    N_s=sum_{x=0}^{31} f_E(x) (-1)^popcount(x AND s),
    Wk=sum_{popcount(s)=k} N_s^2 / 1024.

The mask character differs from product xi by the constant (-1)^|s|, which leaves squared coefficients unchanged. Representative families are [],[3],[3,5],[3,5,9],[3,5,9,17],[3,5,6]. This specifies every integer operation; the denominator is 32^2. Dictator has a single unit Fourier coefficient by inspection. `FiniteChecks.lean` checks the six nondictator spectra using `decide +kernel`; the final success/failure is recorded in lean_check.log. `verify_exact.py` independently checks the spectra and every labelled function using Python integers.

### Reduction to two stability polynomials

Set G(r)=(44r+16r^3+4r^5)/64 and M(r)=(45r+10r^3+9r^5)/64. All types except majority dominate G on [0,1], because their numerator differences from G are:

- two-edge star: r(1-r^2)(1+3r^2);
- three-edge star and triangle: 4r(1-r^2)(1+r^2);
- four-edge star: 3r(1-r^2)(3+r^2);
- dictator: 4r(1-r^2)(5+r^2).

These identities are also verified in Lean. Every factor is nonnegative. It remains to compare both G and M with A(r)=(2/pi)arcsin(r).

### Full analytic comparison

For P equal to G or M, set H(t)=(1-t)P'(sqrt(t))^2 on [0,1]. P' is positive. On 0<r<1, A'(r)=2/(pi sqrt(1-r^2)), so the sign of (P-A)' equals the sign of H(r^2)-4/pi^2.

For G,

    P'(r)=(11+12r^2+5r^4)/16,
    H'(t)=(11+12t+5t^2)(13-16t-25t^2)/256.

The second factor is strictly decreasing on [0,1], positive at zero and negative at one, so it has exactly one root. H increases then decreases. H(0)=121/256>4/pi^2: it suffices that pi>3 and 1089>1024. H(1)=0.

For M,

    P'(r)=(45+30r^2+45r^4)/64,
    H'(t)=(45+30t+45t^2)(15+90t-225t^2)/4096.

The quadratic has roots (90 +/- sqrt(21600))/450, one negative and one in (0,1). Thus again H increases then decreases. H(0)=2025/4096>4/pi^2, because pi>3 and 18225>16384; H(1)=0.

In both cases continuity and strict decrease after the sole maximum show that H crosses 4/pi^2 exactly once, at t=c^2 with 0<c<1. Therefore D=P-A increases from D(0)=0 to its maximum at c, then decreases to D(1)=0. On the decreasing portion use continuity at 1, rather than differentiability there: D(r)>=lim_{u->1} D(u)=0. Hence both P dominate A on [0,1], proving Theorem B. QED.

## 4. Exact random-partition reduction

For tie-free weights let q=(1-rho)/2 and sample a subset J by independent inclusion probability q. Conditional on J set U=sum_{i not in J} wiXi and V=sum_{i in J} wiXi; these sums are independent. The two noisy weighted sums are U+V and U-V, both nonzero. Therefore

    f(X)f(Y)=sign(U^2-V^2),
    Stab_rho(f)=1-2 E_J Pr(|V|>|U|).

Equality |U|=|V| cannot occur: it would force U+V=0 or U-V=0. The full conjecture is equivalent to

    E_J Pr(|sum_{i in J} wiXi|>|sum_{i not in J} wiXi|)
        <= (1/pi)arccos(rho).

The reduction is exact but does not estimate this probability for arbitrary weights.

## 5. Experiments

`experiment.py` uses seed 164, complete cube truth tables, the Walsh-Hadamard transform, and squared Fourier coefficients. It sampled 600,500,300,120 vectors at n=7,9,11,13, from exponential, lognormal, near-equal and integer-weight distributions. Cases with any absolute weighted sum below 1e-9 were skipped (67,66,41,13 cases). Each remaining vector was tested at 162 correlations: 160 equally spaced values between .001 and .99, then .999 and .9999. No violation was found; see random_search.json. This is float grid evidence only, not a proof. It misses unsampled weights and correlations between grid points.

The initial five-variable LP test in experiment.py is floating point and is not used in the proof. It is superseded by the exact classification and spectrum calculation.

## 6. Hostile referee audit

- Ties and centering: constant zero-sign convention and unbiasedness imply oddness and exclude ties. Arbitrary tie-breaking rules are excluded explicitly.
- Classification: handle a winning singleton separately; intersecting edge families are stars or triangles. This proves completeness without trusting the LP enumeration.
- Spectra: use denominator 1024 before reduction, and account for the mask-character sign. Independent exact Python checks and Lean kernel checks verify the finite arithmetic.
- Analytic signs: both derivatives being squared are positive, so the squared comparison preserves signs. The two quadratic root counts are established, and continuity handles the singular derivative at rho=1.
- Near-one bound: the geometric-sum inequality holds for all degrees, with degree zero handled separately. Total influence is bounded for all unate functions, not merely thresholds.
- Numerical limits: sampled float truth tables and a finite rho grid cannot exclude counterexamples.

## First-attempt remaining gap (superseded by section 7)

The comparison for arbitrary numbers of essential variables, six and more, outside Theorem A's interval remains unproved. The general consequence W1>=2/pi is also not proved here. No counterexample was found. No exact solution in print was identified in the bounded accessible search; rate limits prevent an exhaustive literature verdict. Theorem A, Theorem B and the partition identity are partial results; no novelty is asserted.


## 7. Second serious attempt: two new approaches (2026-10-11)

Approach C (stronger finite special case, selected): classify odd monotone functions on SIX variables by intersecting winning pairs and complementary triples. Unlike the earlier five-variable classification, triple choices are now free and introduce nonthreshold functions. Enumerate these choices using exact integer truth tables, group their degree-1/3/5 spectra, and try to dominate the Gaussian curve analytically. If all odd unate functions pass, this proves a stronger six-variable theorem without numerical LP classification. If some fail, separate thresholds from nonthresholds using exact feasibility certificates or expose a concrete obstruction. Degree at most five follows from oddness, even though the truth tables use six coordinates.

Approach D (different reduction, not previously tried): differentiate stability into pivotal-event correlations. For a monotone threshold, S'(rho)=sum_i E[D_i f(X) D_i f(Y)], where D_i f is the indicator that the weighted sum of the other coordinates lies in the pivotal slab for coordinate i. Compare the resulting sum of two-point small-ball probabilities with the Gaussian derivative 2/(pi sqrt(1-rho^2)), or with a single-crossing condition for the integrated difference. A pointwise lower derivative comparison cannot hold near rho=1 for finite functions, since the Gaussian derivative diverges but S'(1)=I(f) is finite; a signed-integral or single-crossing argument is necessary. This suggests neighbouring anti-concentration tools (Esseen, Kolmogorov-Rogozin) but has no ready sharp comparison.

The brain gap query was `Rademacher sums random partition absolute value noise stability arcsin linear threshold`. It returned the previous open-problem/weak rho/3 record, Rademacher/Hoeffding cards, invariance, and Petrov/Esseen concentration leads; none is a verdict. Approach C is selected because it directly addresses the first dimension left open and permits exact checking of every finite step. Approach D remains a lead, with its pointwise-derivative obstruction recorded above.


### Approach C: first result saved

The exact six-variable construction produced 192 intersecting winning-pair families and 2646 odd monotone truth tables, grouped into 21 exact spectra (six_spectra.json). Three spectra have W1<2/pi and therefore cannot satisfy the desired inequality near zero: (W1,W3,W5)=(2400,1600,96)/4096, (2496,1408,192)/4096 and (2528,1344,224)/4096. These account for 332 functions. Indeed these three W1 values are at most 79/128<7/11<2/pi, using the classical pi<22/7 bound; the derivative at rho=0 of their stability minus the arcsine curve is negative, so each violates the curve on a nonempty interval next to zero. This refutes the stronger *all odd unate functions* extension at dimension six, not P0164: threshold feasibility has not yet been checked. No failing truth table is claimed to be a threshold.


### Exact rejection certificates and analytic compression

Every one of the 332 functions in the three failing spectra has an exact positive combination of winning sign vectors equal to zero. The numerical LP was used only to find the combination; fractions were reconstructed and all six sums verified with integers. If such a function were a tie-free homogeneous threshold, dotting the zero combination with its weight vector would give a positive number, contradiction. The full integer certificates are saved in six_rejection_certificates.json; no threshold infeasibility conclusion relies on a solver's floating-point status.

All other 18 spectra satisfy a=W1>=41/64 and a-c=W1-W5>=36/64. Thus they dominate the single polynomial P(r)=(41r+18r^3+5r^5)/64: if alpha=a-41/64 and gamma=c-5/64, the difference is r(1-r^2)(alpha-gamma*r^2), which is nonnegative because alpha>=0 and alpha-gamma>=0. This exact observation reduces the remaining analytic proof to one polynomial.


### Full exact six-variable threshold classification saved

The follow-up classification certifies every one of the 2646 truth tables: 1684 have explicit rational/integer strictly separating weights, and 962 have a positive integer combination of winning sign vectors equal to zero. All witness inequalities and rejection equalities are tested with integers after LP rational reconstruction. `six_full_threshold_certificates.json` contains every certificate. Its first seven spectral classes are nonthreshold; its last fourteen are thresholds. The sharp degree-one threshold weight is W1=43/64. Each of the fourteen threshold spectra satisfies W1-W5>=36/64, so all threshold stabilities dominate P6(r)=(43r+14r^3+7r^5)/64. This polynomial itself occurs, hence it is the pointwise minimum over six-variable unbiased thresholds, not merely a lower estimate.

For this polynomial, P6'(r)=(43+42r^2+35r^4)/64 and H(t)=(1-t)P6'(sqrt(t))^2 has derivative

    H'(t)=(43+42t+35t^2)(41+14t-175t^2)/4096.

The quadratic has one negative and one positive root (constant positive, leading coefficient negative), and its positive root is in (0,1) because its value at 1 is negative. Thus H increases then decreases, H(0)=(43/64)^2>4/pi^2 (pi>3, 129>128), and H(1)=0. The same derivative sign argument as section 3 proves P6(r)>=(2/pi)arcsin(r). The proof requires exact verification of the classification and spectrum certificates; independent checks are in progress.


### Theorem C: full six-variable comparison, with complete proof

**Statement.** Every unbiased linear threshold function on at most six essential variables satisfies the Gaussian arcsine lower bound for every 0<=rho<=1. More precisely its stability is at least

    P6(rho)=(43 rho+14 rho^3+7 rho^5)/64.

This bound is sharp in the six-variable class, attained by weights (3,3,2,2,1,4). It implies the sharp degree-one minimum W1=43/64 in this class. The proof below is finite and computation-assisted; the general conjecture is still open in this attempt.

**Completeness of the finite construction.** Pad the function to six bits and change coordinate signs to make it monotone. By balancedness and the standard zero convention it is odd, as established in section 1. If a singleton wins, the function is a dictator. Otherwise sizes zero and one lose and sizes five and six win. Let E be the winning pairs. By the disjoint-pair argument in section 3, E is intersecting, hence empty, a star, or a triangle. On six labelled vertices the counts are 1,15,60,60,30,6 for empty/stars of sizes 1 through 5, and 20 triangles: in total 192.

Complement symmetry determines each quadruple from its complementary pair. The twenty triples form ten complementary pairs. If a triple contains a winning pair from E, it must win; if its complement contains a winning pair, it must lose. Both conditions cannot hold, since that would yield disjoint winning pairs. Every remaining complementary pair of triples has two independent choices.

Every assignment constructed this way is monotone. The only nontrivial inclusions are a winning pair in a triple, a winning pair in a quadruple, and a winning triple in a quadruple. The first is enforced. For the second, a losing quadruple has a winning complementary pair disjoint from the contained winning pair, impossible. For the third, if winning triple A were inside losing quadruple B, the winning pair B^c would lie inside losing triple A^c, contrary to the enforced first condition. All other inclusions follow from size or transitivity. Thus this construction gives exactly all odd monotone functions with no winning singleton; adding the six dictators gives the complete class.

`six_variables.py` implements the following fully specified finite loops: enumerate the 2^15 subsets E of pair masks, discard those with disjoint edges, enumerate the 2^k assignments to the k unforced complementary triple pairs, construct all 64 function values by the preceding rule, and add the six dictators. Masks encode positive coordinates and complements are 63-x. Exactly 2646 distinct functions result. `verify_six.py` reverses the order of the loops: start with each of the 1024 triple assignments, identify every pair whose containing triples all win, then enumerate its permitted winning-pair subsets. The resulting set of 2646 truth tables agrees exactly. This independently checks the finite construction.

**Certificates separating thresholds from other functions.** For each table, `six_thresholds.py` searches for weights w with w dot x>0 on every winning cube vector x. For successful cases its rational weights are converted to integers and every strict inequality is checked exactly. Oddness then gives w dot x<0 on losing vectors, proving that the whole function is a threshold.

For all other cases the saved certificate is a nonempty list of winning sign vectors x_1,...,x_k whose sum is zero (all multiplicities happen to equal one). If the function were a tie-free homogeneous threshold, every w dot x_j would be strictly positive, while their sum would be w dot 0=0, contradiction. This argument excludes arbitrary real weights; it does not rely on nonnegative weights or on a numerical infeasibility verdict. The integers are independently checked against the truth tables and each of six coordinate sums. The certificates partition all 2646 cases into 1684 thresholds and 962 nonthresholds, with no unresolved solver output. Thus the solver is a certificate finder, not a proof oracle.

**Exact spectra.** For each table define N_s=sum_{x=0}^{63} f(x)(-1)^popcount(x AND s). Then Wk=sum_{popcount(s)=k} N_s^2/4096. Oddness rules out the even degrees 0,2,4,6. All spectra are exact integers with denominator 4096. The full table is below; T means all functions in that spectral class have verified threshold witnesses, and N means all have verified zero-sum rejection certificates.

|4096 W1|4096 W3|4096 W5|Count|Class|
|---:|---:|---:|---:|:---:|
|2400|1600|96|12|N|
|2496|1408|192|140|N|
|2528|1344|224|180|N|
|2624|1152|320|180|N|
|2656|1088|352|180|N|
|2656|1344|96|90|N|
|2688|1280|128|180|N|
|2752|896|448|180|T|
|2784|832|480|140|T|
|2784|1088|224|360|T|
|2816|1024|256|300|T|
|2880|640|576|12|T|
|2880|1152|64|180|T|
|2912|832|352|30|T|
|2912|1088|96|240|T|
|3008|896|192|60|T|
|3072|1024|0|80|T|
|3168|832|96|60|T|
|3392|640|64|30|T|
|3680|320|96|6|T|
|4096|0|0|6|T|

`verify_six.py` calculates all Fourier coefficients directly from their 64-term definition, independently of the Walsh-Hadamard transform used in the first script. It validates every spectral class, certificate and truth table and proves the two finite inequalities needed for thresholds:

    W1 >= 43/64,  W1-W5 >= 36/64.

The second inequality also follows without computation: for an odd six-bit function, I=W1+3W3+5W5=3-2(W1-W5), while the influence proof of section 2 gives I<=E|sum_{i=1}^6 Xi|=15/8 (the binomial distribution directly gives this last value). Rearranging yields W1-W5>=9/16=36/64.

**Polynomial comparison.** Put a=W1, c=W5, alpha=a-43/64 and gamma=c-7/64. Because the weights sum to one,

    Stab_r(f)-P6(r)=r(1-r^2)(alpha-gamma r^2).

Here alpha>=0 and alpha-gamma=(a-c)-36/64>=0. For 0<=t<=1, alpha-gamma t=(1-t)alpha+t(alpha-gamma)>=0. Thus all threshold polynomials dominate P6. The listed integer weights (3,3,2,2,1,4) have total weight 15, so every signed sum is an odd integer and is nonzero; direct exact Fourier calculation gives (W1,W3,W5)=(43,14,7)/64. This proves sharpness.

To compare P6 with A(r)=(2/pi)arcsin(r), set H(t)=(1-t)(43+42t+35t^2)^2/4096. On 0<r<1 both P6' and A' are positive, and the sign of (P6-A)' is the sign of H(r^2)-4/pi^2. Differentiation gives

    H'(t)=(43+42t+35t^2)(41+14t-175t^2)/4096.

The quadratic has one positive and one negative root because the product of its roots is negative. It is positive at zero and negative at one, so its positive root lies in (0,1). The first factor is positive. Hence H strictly increases to one maximum and then strictly decreases to H(1)=0. H(0)=(43/64)^2>4/pi^2, since pi>3 and 43*3=129>128=64*2. Therefore H crosses 4/pi^2 exactly once. The difference P6-A increases from zero and then decreases to zero. Continuity at r=1 handles the singularity of A' there. Consequently P6>=A everywhere on [0,1]. This proves Theorem C. QED.

**Scope of formal checking.** The complete combinatorial argument and analytic comparison are written here; they are not fully formalized in Lean. The exact rejection certificates, the sharp example spectrum, and the polynomial factorization identities are checked in `SixChecks.lean`, with final outcome recorded in `six_lean_check.log`. Exhaustive enumeration and every direct Fourier sum are independently checked in exact Python integer arithmetic. No floating-point result is being promoted to a theorem without a subsequent exact certificate.

### Hostile-referee checks for the new result

- The six-variable case cannot use the five-variable star/triangle classification alone: the free triple choices are necessary, and the construction and reverse construction explicitly include them.
- Odd monotone functions are a broader class than thresholds. Three classes actually violate the conjectured bound near zero; rejecting them as thresholds is essential. All seven nonthreshold classes, not just those three, have exact zero-sum witnesses.
- A zero-sum rejection requires strictly positive scores on all winners. Balancedness permits a tie-free homogeneous representation, so a constant-sign tie convention cannot evade the argument. Arbitrary input-dependent tie rules remain excluded.
- Successful weights are verified on all winning vectors and oddness supplies the losing inequalities. Exact reconstruction is checked even though the finder is numerical.
- The two finite spectral inequalities have different roles: W1 has to be classified, but W1-W5 follows independently from total influence. Nonnegativity of the factored gap uses both, not just W1.
- The derivative comparison is valid only on (0,1); continuity supplies endpoints. H' has one turning point because its quadratic has roots of opposite signs, not because every coefficient is positive.
- The bound is attained by an explicit six-coordinate threshold, and it applies to all at most six essential coordinates by padding. Padding to odd dimension seven also makes this a special case of the source's precise statement.

### Approach D checked reduction and obstruction

Differentiate the finite Fourier polynomial. For D_i f(x_without_i)=(f(x_i=1)-f(x_i=-1))/2, its coefficients are hat f(S union {i}) indexed by S not containing i. Hence

    sum_i E[D_i f(X_without_i)D_i f(Y_without_i)]
      =sum_{S nonempty}|S| rho^(|S|-1)hat f(S)^2
      =Stab'_rho(f).

For a monotone tie-free threshold with w_i>0, D_i f is exactly the indicator that -w_i<sum_{j!=i}w_j x_j<w_i. For w_i=0 it is zero. Thus this is a sum of correlated pivotal-slab probabilities. The pointwise inequality Stab'_rho(f)>=2/(pi sqrt(1-rho^2)) is false near rho=1 for every finite threshold: the left side tends to its finite total influence and the right diverges. Standard Kolmogorov-Rogozin/Esseen cards give concentration upper bounds with unspecified constants; they do not establish the needed exact signed-integral or single-crossing comparison. No general result is claimed from this approach.

### Updated remaining gap after the second attempt

The full inequality remains unproved for thresholds with seven or more essential variables outside the previously proved near-one regime. We have advanced the entire-correlation finite case from at most five to at most six essential variables, and have obtained its exact lower stability polynomial and sharp W1 minimum. The arbitrary-dimensional W1>=2/pi consequence remains unproved. No P0164 counterexample has been found; the six-variable unate failures are rigorously NONthresholds. The existing literature search remains bounded and incomplete, and no novelty of this finite result is asserted.
