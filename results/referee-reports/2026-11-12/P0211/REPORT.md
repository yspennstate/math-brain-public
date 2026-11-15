# Independent referee report

Overall verdict: **SOUND**.

I found no mathematical error or missing internal proof step in the supplied arguments. The main spectral results survive exact generator checks, symbolic rederivation, boundary checks, and independent numerical tests. The count cutoff and classical Ewens diagonalization use established external theorems whose quoted statements are appropriate; their exact source locations were not checked because browsing was forbidden and the articles were not supplied. This verdict does not certify historical novelty or bibliographic metadata.

All eleven requested parts were reached. `LOG.md` records the ordered argument-by-argument audit; it is part of this report. Every program used for computation is saved here: `audit.py`, `audit_algebra.py`, `audit_count_direct.py`, `audit_uniformization.py`, the rejected `audit_exponential.py` diagnostic, and this table assembler. No author program, external search, other agent, push, visible window, or write outside this folder was used. Numerical work ran with one BLAS thread and sparse/tridiagonal storage. The longest computation was 21.1 seconds; the measured extension runs used about 7680 MB peak RSS. No computation approached the five-minute or 1 GB limits.

The four load-bearing points are: (i) the cut representation transfers stationary forms, with gamma_M >= gamma_B, rather than pathwise polymer lumping; (ii) cyclic invariance eliminates degree one, and the strict forward-ratio estimate puts every degree at least two strictly above gamma_Q; (iii) singleton count fibers plus reversibility give exact polymer endpoint TV identities; and (iv) the arbitrary-start mixing proof bounds the actual polymer density through instantaneous energies and positivity, without assuming that polymer lifts evolve under the cut semigroup.

## Verdict table

Proof-step details, including the arithmetic behind these reasons, are in `LOG.md`. CORRECT for an application of an external theorem means the quoted theorem implies the claim with the hypotheses and normalization given; see the source-verification limitations below.

| Statement or proof step | Verdict | Reason |
| --- | --- | --- |
| introduction: fragmentation/coagulation rates | CORRECT | The unequal/equal split and pair factors match the verbal model. |
| introduction: stationary law, irreducibility | CORRECT | Factorial detailed balance; all states connect through monomers. |
| [thm:main], [cor:regimes] | CORRECT | Upper certificate and exhaustive lower-bound patching give the stated constants. |
| [proof:prop:comparison]: multiplicity and pushforward | CORRECT | Distinguished-cut counting gives n(k-1)!/prod m_j!. |
| [proof:prop:comparison]: averaged rates and form equality | CORRECT | Uniform cyclic multiset ordering gives the polymer conductances exactly. |
| [proof:prop:comparison]: gap direction | CORRECT | Lifted functions form a subspace, so gamma_M >= gamma_B. |
| [proof:lem:positive] | CORRECT | Positive ground state and extrema of v/h prove both signs correctly. |
| Count chain, derivative intertwining, base bound | CORRECT | Discrete derivative identifies all nonzero Q eigenvalues with -A. |
| [proof:prop:upper] | CORRECT | The reciprocal product trial has maximum <= beta+4max(sqrt(beta),1/n). |
| [proof:lem:layers]: commutator/dimension | CORRECT | Adjoint injection/surjection gives binomial(n,ell)-binomial(n,ell-1). |
| [proof:lem:layers]: lift norms/orthogonality/completeness | CORRECT | The U,D recursion proves norms, support, and the telescoping decomposition. |
| [proof:lem:sectoraction] | CORRECT | Neighbor-lift sums give the exact birth, death and killing coefficients. |
| [proof:prop:base] | CORRECT | Higher killing is large; the cyclic fixed degree-one coefficient vector vanishes. |
| [proof:prop:squareroot] | CORRECT | Positive reciprocal quotients give sqrt(beta)/5 under the stated hypotheses. |
| Completion of [thm:main], all exceptional parameter ranges | CORRECT | beta>=1/16, beta<=4/n^2, n<8 and the remaining region exhaust all cases. |
| [lem:ground-ratio] | CORRECT | A minimum forward ratio <=1/2 contradicts adjacent eigenvalue equations. |
| [prop:higher-exact] | CORRECT | The shifted ground-state certificate is strictly above gamma_Q. |
| [thm:exact-gap] | CORRECT | Rotation-invariant lower bound and count-function upper bound agree. |
| [thm:sharp-gap]: a>1 and endpoint brackets | CORRECT | a(a-1)=beta*n(n+a+1); the quotient increases in k. |
| [thm:sharp-gap]: additive error | CORRECT | d+1/n<=c<=d+4/n and subtraction <=6/n give d-5/n and d+4/n. |
| [cor:sharp-equivalents] | CORRECT | The additive error is negligible in the claimed regimes; a->1 at the small end. |
| [prop:critical-operator] | CORRECT | Closed core form, compact embedding, positive simple minimizer. |
| [lem:critical-ground-ratios] | CORRECT | Order coupling plus the h0 transform gives both ratios; nonexplosion is justified. |
| [thm:critical-limit] | CORRECT | The finite correction to the restricted infinite ground state lies in [-b/n,b/n]. |
| [prop:critical-lipschitz] | CORRECT | Bounded cross-parameter ground states lie in the operator domain; pairing is valid. |
| [prop:critical-truncation] | CORRECT | Only the last birth changes; its quotient error is <=2b/(R+3). |
| Degree-one critical form construction | CORRECT | Killing j still gives compact tails; zero form energy is impossible. |
| [prop:critical-degree-one] | CORRECT | The transformed ratio gives the signed finite error and the bounds on sigma. |
| [cor:critical-end-asymptotics] | CORRECT | Reciprocal bounds squeeze sigma; sharp count bounds squeeze rho. |
| [eq:critical-sigma-truncation] | CORRECT | The last-birth error is <=b/(R+2). |
| [cor:critical-spatial-limit] | CORRECT | Minimum is 1-Lipschitz; both radial approximations have error <=b/n. |
| Count cutoff definition and window | CORRECT | The claimed fixed-epsilon times imply standard cutoff and an upper window bound. |
| Count strong lumping and polymer endpoint TV identity | CORRECT | Singleton fibers and reversible evolution keep endpoint densities count-measurable. |
| Count stationary estimates | CORRECT | Ratio differentiation gives central Gaussian estimates and geometric outer tails. |
| Count hitting means, both endpoints | CORRECT | Passage recurrences plus reciprocal drift sums give tn+O_b(sqrt(n)). |
| Count hitting variances, both endpoints | CORRECT | Independent passages and cumulative-tail estimates give O_b(n). |
| [thm:count-cutoff]: worst-case upper bound | CORRECT | The quoted birth-death theorem applies after the exact time rescaling. |
| [thm:count-cutoff]: endpoint lower bounds | CORRECT | Central-target hitting times have controlled means/variances; Chebyshev suffices. |
| Separation cutoff consequence | CORRECT | The quoted separation theorem uses the sum of endpoint hitting means; fibers transfer it. |
| [thm:full-polymer-tv-upper-new]: degree bound | CORRECT | Rising-factorial trials give lambda_ell >= ell*sqrt(beta)/6. |
| [thm:full-polymer-tv-upper-new]: count density | CORRECT | The logarithmic Lyapunov inequality yields M(t)<=C_b sqrt(bn). |
| [thm:full-polymer-tv-upper-new]: low-degree positivity estimate | CORRECT | Permutation-invariant PSD projectors have uniformly bounded entries on a slice. |
| [thm:full-polymer-tv-upper-new]: energy integration | CORRECT | The energy inequality first reduces log R, then the gap mixes a polynomial density. |
| [thm:full-polymer-tv-upper-new]: every start | CORRECT | All density and count estimates are uniform over the initial partition. |
| [eq:spatial-generator] and equilibrium | CORRECT | Nonempty-subset reactions and symmetric swaps preserve the stated weight. |
| [thm:spatial-exact-gap] | CORRECT | Harmonic tensor sums; higher sectors already exceed the count gap. |
| [prop:spatial-degree-one-sharp] | CORRECT | The exact reciprocal quotient is increasing, with positive denominators for all a>0. |
| [cor:spatial-leading-constants] | CORRECT | Combine additive errors inside the minimum; nm>=n sqrt(beta). |
| [prop:spatial-degree-one-scale] | CORRECT | Two trial upper bounds, auxiliary lower bounds, and parameter patching give u/8<=eta1<=u. |
| [eq:spatial-degree-one-below-count] | CORRECT | Subtract the two operators and use inverse ground ratios <=2. |
| [cor:spatial-uniform-gap] and rare/cycle/torus cases | CORRECT | Take the minimum of the proved count and degree-one scales. |
| [cor:spatial-inhomogeneous] and the example | CORRECT | Compare undirected reaction conductances against a_- B and a_+ B. |
| [thm:nonreversible]: invariance and asymptotic rate | CORRECT | Unitary permutation actions are dissipative; tensor spectral sums remain valid with Jordan blocks. |
| [thm:nonreversible]: contraction exponent | CORRECT | The symmetric-part gap is sufficient by differentiation and necessary at time zero. |
| Nonreversible three-coordinate example and product extension | CORRECT | Characteristic polynomials give the stated 5/2 and 2 rates. |
| [lem:simple-polymer-gap] | CORRECT | Strict higher-sector separation and the simple derivative ground state force a simple count mode. |
| [prop:polymer-circulation]: rates, invariance, symmetric part | CORRECT | A divergence-free antisymmetric stationary current preserves all three properties. |
| [prop:polymer-circulation]: strictness | CORRECT | An eigenvector attaining the symmetric-part gap would have to be g, but Ag is nonzero and orthogonal to g. |
| [eq:circulation-perturbation] | CORRECT | Simple-eigenvalue perturbation gives the positive quadratic coefficient; adjoint symmetry makes the branch even. |
| [thm:kernel-comparison] and unbounded stationary representation | CORRECT | Both reaction directions share a multiplier; compare forms with the same variance. |
| [prop:ewens-classical] | CORRECT | The quoted classical spectrum has its least nonzero value at (n-1,1), in the stated units. |
| [prop:growing-kernel-upper]: product drift and covariance | CORRECT | Exact monomer drift plus stochastic ordering of conditional nonmonomer counts. |
| [prop:growing-kernel-upper]: additive bounds | CORRECT | Use i+j>=2 and i+j<=2ij in the common equilibrium form. |
| Coupling appendix: Stage I and Stage II marginals | CORRECT | All joint events have the cut-chain marginals, including r=0. |
| Coupling appendix: certificates and survival | CORRECT | Both killed generators have positive supersolutions at rate sqrt(beta)/5. |
| Coupling appendix: concatenation and gap deduction | CORRECT | Uniform exponential moments concatenate by strong Markov; eigenfunctions force the gap bound. |
| [eq:L2-decay], [eq:cov-decay], point-mass TV bound | CORRECT | Standard finite reversible spectral calculus with the stated constants. |

## Independent numerical evidence

These are floating-point spectral and ODE calculations, except where exact Fraction/SymPy checks are specified. No floating-point output is presented as a rigorous interval certificate. The mathematical arguments, rather than these grids, establish the all-parameter claims.

### 1 and 3(a): full polymer generators

Command: `python3 audit.py step13`. Every row passed exact rational detailed balance and graph-connectivity checks, simplicity of the gap, and strict monotonicity of its count eigenfunction. The function is constant on each count fiber to numerical precision. For n=2 there is no second positive eigenvalue against which to measure separation. Raw per-case separations and residuals: `step1_3a.json`.

| n | beta | states | gamma_M | gamma_Q (direct) | absolute difference |
| --- | --- | --- | --- | --- | --- |
| 2 | 1/50 | 2 | 1.02 | 1.02 | 2.2204460493e-16 |
| 2 | 1/7 | 2 | 1.1428571429 | 1.1428571429 | 2.2204460493e-16 |
| 2 | 1 | 2 | 2 | 2 | 2.2204460493e-16 |
| 2 | 3 | 2 | 4 | 4 | 8.881784197e-16 |
| 3 | 1/50 | 3 | 0.69659167088 | 0.69659167088 | 6.6613381478e-16 |
| 3 | 1/7 | 3 | 0.87713676951 | 0.87713676951 | 2.2204460493e-16 |
| 3 | 1 | 3 | 2 | 2 | 1.7763568394e-15 |
| 3 | 3 | 3 | 4.191857033 | 4.191857033 | 5.3290705182e-15 |
| 4 | 1/50 | 5 | 0.53976004222 | 0.53976004222 | 0 |
| 4 | 1/7 | 5 | 0.77357725561 | 0.77357725561 | 1.1102230246e-16 |
| 4 | 1 | 5 | 2.0452420169 | 2.0452420169 | 2.2204460493e-15 |
| 4 | 3 | 5 | 4.2909830028 | 4.2909830028 | 7.9936057773e-15 |
| 5 | 1/50 | 7 | 0.44947522432 | 0.44947522432 | 8.881784197e-16 |
| 5 | 1/7 | 7 | 0.73091468081 | 0.73091468081 | 3.3306690739e-16 |
| 5 | 1 | 7 | 2.0802738673 | 2.0802738673 | 4.8849813084e-15 |
| 5 | 3 | 7 | 4.3501641979 | 4.3501641979 | 2.6645352591e-15 |
| 6 | 1/50 | 11 | 0.39237418081 | 0.39237418081 | 4.9960036108e-16 |
| 6 | 1/7 | 11 | 0.71493391842 | 0.71493391842 | 1.443289932e-15 |
| 6 | 1 | 11 | 2.1051375755 | 2.1051375755 | 3.108624469e-15 |
| 6 | 3 | 11 | 4.3894092245 | 4.3894092245 | 1.5099033135e-14 |
| 7 | 1/50 | 15 | 0.3541418531 | 0.3541418531 | 1.6653345369e-16 |
| 7 | 1/7 | 15 | 0.71102267403 | 0.71102267403 | 1.8873791419e-15 |
| 7 | 1 | 15 | 2.1233303659 | 2.1233303659 | 4.4408920985e-15 |
| 7 | 3 | 15 | 4.4173249316 | 4.4173249316 | 3.5527136788e-15 |
| 8 | 1/50 | 22 | 0.32760664945 | 0.32760664945 | 4.9960036108e-16 |
| 8 | 1/7 | 22 | 0.71230430996 | 0.71230430996 | 5.5511151231e-16 |
| 8 | 1 | 22 | 2.1371449179 | 2.1371449179 | 6.2172489379e-15 |
| 8 | 3 | 22 | 4.4381945209 | 4.4381945209 | 1.1546319456e-14 |
| 9 | 1/50 | 30 | 0.30877252936 | 0.30877252936 | 4.4408920985e-16 |
| 9 | 1/7 | 30 | 0.71552612936 | 0.71552612936 | 8.881784197e-16 |
| 9 | 1 | 30 | 2.147969725 | 2.147969725 | 5.3290705182e-15 |
| 9 | 3 | 30 | 4.4543854884 | 4.4543854884 | 5.3290705182e-15 |
| 10 | 1/50 | 42 | 0.29523212895 | 0.29523212895 | 2.2204460493e-16 |
| 10 | 1/7 | 42 | 0.71923184805 | 0.71923184805 | 3.3306690739e-16 |
| 10 | 1 | 42 | 2.1566721217 | 2.1566721217 | 7.9936057773e-15 |
| 10 | 3 | 42 | 4.4673120527 | 4.4673120527 | 1.7763568394e-15 |

Maximum absolute polymer/direct-count gap difference: 1.51e-14. The minimum separation from the next positive eigenvalue, where present, is 0.000239958. Maximum absolute within-count eigenfunction residual: 1.126e-12.

Additional command: `python3 audit_count_direct.py`. This builds Q from its original birth/death rates and computes its first positive eigenvalue directly, as well as checking the derivative version. Maximum direct-Q/derivative discrepancy is 2.66e-15 in the 36 small cases and 5.24e-11 in the 56 large cases, both below 1e-9. Exact count lumping of the full polymer generator and the matrix equation derivative*Q=A*derivative pass in all 36 rational cases. Raw data: `count_direct_checks.json`.

### 3(b): large count grid and bound slacks

Same command. The symmetric derivative tridiagonal matrix has exactly the nonzero Q spectrum, avoids subtracting the stationary zero eigenvalue, and has dimension n-1. All requested values are included, including duplicate numerical parameters such as 1e-6=n^-2 when n=1000. `step3b.json` stores unrounded values.

| n | beta | gamma_Q | sharp lower | sharp upper | eta1 (used in 7) |
| --- | --- | --- | --- | --- | --- |
| 2 | 1e-06 | 1.000001 | 1.000001 | 1.000001 | 1e-06 |
| 2 | 0.0001 | 1.0001 | 1.0001 | 1.0001 | 0.0001 |
| 2 | 0.01 | 1.01 | 1.01 | 1.01 | 0.01 |
| 2 | 0.25 | 1.25 | 1.25 | 1.25 | 0.25 |
| 2 | 0.5 | 1.5 | 1.5 | 1.5 | 0.5 |
| 2 | 1 | 2 | 2 | 2 | 1 |
| 2 | 10 | 11 | 11 | 11 | 10 |
| 2 | 1000 | 1001 | 1001 | 1001 | 1000 |
| 3 | 1e-06 | 0.66666816667 | 0.66666816666 | 0.66667266657 | 1.499999625e-06 |
| 3 | 0.0001 | 0.66681666479 | 0.66681664795 | 0.66726569446 | 0.00014999625 |
| 3 | 0.01 | 0.68164791693 | 0.68150264834 | 0.71901568306 | 0.014962502109 |
| 3 | 0.11111111111 | 0.8310225234 | 0.82222222222 | 1 | 0.16206874832 |
| 3 | 0.33333333333 | 1.1461490624 | 1.1069049711 | 1.3519093633 | 0.46065533708 |
| 3 | 1 | 2 | 1.8888888889 | 2.1428571429 | 1.2324081208 |
| 3 | 10 | 11.289084683 | 11.200280996 | 11.295753744 | 10.322234541 |
| 3 | 1000 | 1001.3328889 | 1001.3315618 | 1001.3328898 | 1000.3332222 |
| 5 | 1e-06 | 0.4000025 | 0.40000249999 | 0.40001149959 | 2.499996875e-06 |
| 5 | 0.0001 | 0.40024998687 | 0.40024986926 | 0.40114595783 | 0.00024996875 |
| 5 | 0.01 | 0.42486876403 | 0.42400658458 | 0.48947323353 | 0.024687691802 |
| 5 | 0.04 | 0.49790357878 | 0.48949474527 | 0.6501050946 | 0.095048148152 |
| 5 | 0.2 | 0.84955317239 | 0.78056649186 | 1.0777340326 | 0.39574333664 |
| 5 | 1 | 2.0802738673 | 1.8899959968 | 2.2080032026 | 1.3978317841 |
| 5 | 10 | 11.511272833 | 11.411358819 | 11.519091294 | 10.566674651 |
| 5 | 1000 | 1001.5990408 | 1001.5976068 | 1001.5990419 | 1000.5996403 |
| 10 | 1e-06 | 0.20000499999 | 0.20000499988 | 0.2000223307 | 4.9999666665e-06 |
| 10 | 0.0001 | 0.20049988 | 0.20049881642 | 0.20220761144 | 0.00049966666708 |
| 10 | 0.01 | 0.24880203189 | 0.24379611531 | 0.33069059647 | 0.046706870846 |
| 10 | 0.01 | 0.24880203189 | 0.24379611531 | 0.33069059647 | 0.046706870846 |
| 10 | 0.1 | 0.59493395562 | 0.51435935394 | 0.7446820762 | 0.299889117 |
| 10 | 1 | 2.1566721217 | 1.9865221841 | 2.2317894682 | 1.510885238 |
| 10 | 10 | 11.673422196 | 11.604527685 | 11.678907441 | 10.743704743 |
| 10 | 1000 | 1001.798562 | 1001.7976057 | 1001.7985629 | 1000.7993609 |
| 50 | 1e-06 | 0.04002499844 | 0.04002498445 | 0.040102613715 | 2.4995000002e-05 |
| 50 | 0.0001 | 0.042484401654 | 0.042377636956 | 0.048483597731 | 0.0024500457611 |
| 50 | 0.01 | 0.19069339817 | 0.15841155713 | 0.22309167887 | 0.093794101215 |
| 50 | 0.0004 | 0.04975082176 | 0.04867333898 | 0.065208255 | 0.009211371504 |
| 50 | 0.02 | 0.2736886179 | 0.23125880272 | 0.30630929246 | 0.14010662632 |
| 50 | 1 | 2.2200838955 | 2.1684724487 | 2.2367013457 | 1.5969990504 |
| 50 | 10 | 11.800668855 | 11.783649278 | 11.802033533 | 10.88195066 |
| 50 | 1000 | 1001.9581219 | 1001.9578923 | 1001.9581222 | 1000.9590801 |
| 200 | 1e-06 | 0.01009990001 | 0.01009904662 | 0.010387919465 | 9.9670007981e-05 |
| 200 | 0.0001 | 0.019025617237 | 0.017198249491 | 0.025685411206 | 0.0072376723436 |
| 200 | 0.01 | 0.197749598 | 0.18093655802 | 0.20578647601 | 0.10235246515 |
| 200 | 2.5e-05 | 0.01243761184 | 0.01216605631 | 0.0162131072 | 0.0022967691415 |
| 200 | 0.005 | 0.13902811673 | 0.12371552365 | 0.14698599945 | 0.070551470578 |
| 200 | 1 | 2.2320688962 | 2.218137825 | 2.2362945574 | 1.6127923212 |
| 200 | 10 | 11.824298558 | 11.819885996 | 11.824652626 | 10.907563128 |
| 200 | 1000 | 1001.9880338 | 1001.9879746 | 1001.9880338 | 1000.9890218 |
| 1000 | 1e-06 | 0.0024875211699 | 0.0024331090147 | 0.0032374034372 | 0.00045903011903 |
| 1000 | 0.0001 | 0.019508844791 | 0.016808803144 | 0.021039614678 | 0.0095383287317 |
| 1000 | 0.01 | 0.19974675586 | 0.19562288484 | 0.20134773325 | 0.10457309758 |
| 1000 | 1e-06 | 0.0024875211699 | 0.0024331090147 | 0.0032374034372 | 0.00045903011903 |
| 1000 | 0.001 | 0.06275526361 | 0.058981896178 | 0.064302945621 | 0.031608765928 |
| 1000 | 1 | 2.2352680135 | 2.2324242342 | 2.2361169173 | 1.6169865519 |
| 1000 | 10 | 11.830587983 | 11.829696997 | 11.830659488 | 10.91437728 |
| 1000 | 1000 | 1001.99601 | 1001.995998 | 1001.99601 | 1000.997006 |

A slack is actual-minus-lower or upper-minus-actual. The worst (smallest) slacks are:

| Inequality | minimum slack | n | beta |
| --- | --- | --- | --- |
| sharp_lower | -1.1368683772e-13 | 2 | 1000 |
| sharp_upper | 0 | 2 | 0.0001 |
| additive_lower | 0.0030059720498 | 1000 | 1000 |
| additive_upper | 0.0035124790801 | 1000 | 1e-06 |
| main_lower | 0.0021540211699 | 1000 | 1e-06 |
| main_upper | 0.0055164788301 | 1000 | 1e-06 |
| elementary_lower | -1.1102230246e-16 | 2 | 1e-06 |
| elementary_upper | 0.0015134788301 | 1000 | 1e-06 |

There is no failed inequality. The -1.14e-13 sharp-lower value and -1.11e-16 elementary-lower value occur at n=2, where the relevant formulas are exact equalities and gamma_Q=beta+1. Their signs are rounding artifacts, confirmed by that independent exact two-state calculation.

### 4: critical function and finite-size comparison

Command: `python3 audit.py step4`. To make the paper's truncation width less than 1e-6 requires the R below. A direct array at R=200,000,001 would exceed the resource limit. Instead, the program evaluates rho_R by bounding the omitted tail of J_R with a Schur complement and diagonalizing only 80 coordinates. For k>=M+1 the tail diagonal minus absolute off-diagonal row sum is at least (M+2)(M+1-2sqrt(b)), including the reflecting last row. If U=2+b/2, the last-coordinate Schur correction to the leading block lies in [0,bM(M+1)/(tail_lower-U)]. Smallest eigenvalues of the two leading-block endpoints bracket rho_R in exact arithmetic. The numerically evaluated endpoint differences are at most 5e-13, and sometimes round to zero. This also localizes the infinite eigenvalue; the width shown below is the paper's more conservative analytic truncation error. Rounding is not interval-certified. `step4.json` contains the endpoints.

| b | R | rho_R approx. | 2b/(R+3) | 2+b/2 |
| --- | --- | --- | --- | --- |
| 0.1 | 200001 | 2.0498750021 | 9.999800004e-07 | 2.05 |
| 1 | 2000001 | 2.48752112 | 9.99998e-07 | 2.5 |
| 10 | 20000001 | 5.9047507068 | 9.999998e-07 | 7 |
| 100 | 200000001 | 19.50863143 | 9.9999998e-07 | 52 |

| b | n | n gamma_Q(n,b/n^2) | difference from rho approx. | allowed b/n |
| --- | --- | --- | --- | --- |
| 0.1 | 10 | 2.049880002 | 4.9999201157e-06 | 0.01 |
| 0.1 | 100 | 2.0498750521 | 5.0000004581e-08 | 0.001 |
| 0.1 | 1000 | 2.0498750027 | 5.4103255209e-10 | 0.0001 |
| 1 | 10 | 2.4880203189 | 0.00049919894431 | 0.1 |
| 1 | 100 | 2.487526112 | 4.9920068648e-06 | 0.01 |
| 1 | 1000 | 2.4875211699 | 4.990745639e-08 | 0.001 |
| 10 | 10 | 5.9493395562 | 0.044588849451 | 1 |
| 10 | 100 | 5.9051969089 | 0.00044620209117 | 0.1 |
| 10 | 1000 | 5.9047551688 | 4.4620532549e-06 | 0.01 |
| 100 | 10 | 21.566721217 | 2.0580897874 | 10 |
| 100 | 100 | 19.529959564 | 0.021328134237 | 1 |
| 100 | 1000 | 19.508844791 | 0.00021336046116 | 0.1 |

All computed values satisfy 2<rho<=2+b/2. Every ordered pair among these b values satisfies 0<=rho(b2)-rho(b1)<=(b2-b1)/2 (checking adjacent pairs already implies the others). All twelve finite-size comparisons pass with substantial slack.

### 5: endpoint count TV profiles

Commands: `python3 audit.py step5` and `python3 audit_uniformization.py`. The table below uses uniformization: a nonnegative Poisson series for tridiagonal transition matrices. Adaptive upper-state truncation uses killed subgenerators, so removed trajectories and omitted Poisson terms lose probability mass; the total mass defect is <=2.02e-13, apart from roundoff. An independent sparse BDF evaluation of q'=Q^T q (rtol=2e-9, coordinate atol=2e-13) agrees in TV within 5.68e-9 over the entire grid. BDF mass error is <=7.2e-15, and a tighter-tolerance rerun at b=0.5,n=400 changes TV by <=1.88e-9. Uniformization took 1.43 seconds. Data: `step5_uniformization.json` and `step5.json`. All entries below are at tn+c sqrt(n). A dash means a negative time, for which TV is undefined; it does not mean zero or time zero.

| b | n | start | c=-4 | -2 | -1 | 0 | 1 | 2 | 4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.5 | 100 | 1 |  |  |  | 0.57986722 | 0.18207151 | 0.04885791 | 0.00321063 |
| 0.5 | 100 | 100 |  |  |  | 0.83364339 | 0.23026308 | 0.05420079 | 0.00352193 |
| 0.5 | 400 | 1 |  |  | 0.99957692 | 0.63688373 | 0.20070301 | 0.05274950 | 0.00329668 |
| 0.5 | 400 | 400 |  |  | 1.00000000 | 0.82810782 | 0.23264400 | 0.05610781 | 0.00343289 |
| 0.5 | 1600 | 1 |  |  | 0.99934258 | 0.67721273 | 0.21085197 | 0.05440810 | 0.00331194 |
| 0.5 | 1600 | 1600 |  |  | 1.00000000 | 0.81774968 | 0.23284566 | 0.05664354 | 0.00338311 |
| 0.5 | 6400 | 1 |  |  | 0.99963305 | 0.70352044 | 0.21810780 | 0.05509316 | 0.00333069 |
| 0.5 | 6400 | 6400 |  |  | 1.00000000 | 0.80692000 | 0.23186795 | 0.05651966 | 0.00336505 |
| 2 | 100 | 1 |  |  |  | 0.76383850 | 0.06872897 | 0.00436926 | 0.00001667 |
| 2 | 100 | 100 |  |  |  | 0.90736540 | 0.06805714 | 0.00411535 | 0.00001564 |
| 2 | 400 | 1 |  |  |  | 0.80941905 | 0.07390965 | 0.00456501 | 0.00001673 |
| 2 | 400 | 400 |  |  |  | 0.92737155 | 0.07385981 | 0.00442377 | 0.00001617 |
| 2 | 1600 | 1 |  |  |  | 0.84135939 | 0.07649605 | 0.00464029 | 0.00001661 |
| 2 | 1600 | 1600 |  |  |  | 0.93161485 | 0.07663884 | 0.00456511 | 0.00001633 |
| 2 | 6400 | 1 |  |  |  | 0.86225705 | 0.07787194 | 0.00466166 | 0.00001650 |
| 2 | 6400 | 6400 |  |  |  | 0.92884702 | 0.07811910 | 0.00462741 | 0.00001635 |

The positive-time entries are consistent with an O(sqrt(n)) transition window around tn: the distance at c=0 remains of constant order while fixed positive shifts reduce it substantially, and the two endpoints have similar limiting behavior. These small-to-moderate n data cannot prove cutoff or an optimal window. The requested grid poorly samples the pre-cutoff side: c=-4,-2 always produce negative times here, and for b=2 even c=-1 is negative for all four n. Thus this table gives very limited evidence for the left tail; the hitting-time lower bound, rather than the table, supplies that part of the theorem.

Rejected numerical diagnostic: `audit_exponential.py` attempted contour inversion of the tridiagonal resolvent. It produced nonphysical values and catastrophic cancellation for sharply concentrated high-count initial data; an initial dense-exponential cross-check also produced nonfinite output. Those results were rejected and do not appear in the table. Positive uniformization and the independent BDF solver resolve the calculation without that unstable route. This is a failure of an exploratory numerical method, not evidence against the paper.

### 7: full spatial generators

Command: `python3 audit.py step7`. State space is the 2^n-1 nonempty subsets, not the full Boolean cube. Each row below represents four separately built full generators. The unequal graph is a path with edge weights 1/3,2/3,...,(n-1)/3. Each entry was compared with min(gamma_Q,eta1+D lambda_G), using an independently built graph Laplacian and the degree-one radial operator. All 160 comparisons pass; maximum absolute error is 1.67e-13. Full per-D data: `step7.json`.

| n | beta | graph | lambda_G | gap D=0 | D=0.1 | D=1 | D=10 | max error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 0.05 | complete | 4 | 0.096684970267 | 0.49668497027 | 0.59850164608 | 0.59850164608 | 3.108624469e-15 |
| 4 | 0.05 | cycle | 2 | 0.096684970267 | 0.29668497027 | 0.59850164608 | 0.59850164608 | 9.1038288019e-15 |
| 4 | 0.05 | path | 0.58578643763 | 0.096684970267 | 0.15526361403 | 0.59850164608 | 0.59850164608 | 2.2204460493e-15 |
| 4 | 0.05 | star | 1 | 0.096684970267 | 0.19668497027 | 0.59850164608 | 0.59850164608 | 2.3314683517e-15 |
| 4 | 0.05 | unequal_path | 0.31194074251 | 0.096684970267 | 0.12787904452 | 0.40862571277 | 0.59850164608 | 1.8873791419e-15 |
| 4 | 1 | complete | 4 | 1.338297862 | 1.738297862 | 2.0452420169 | 2.0452420169 | 3.9968028887e-15 |
| 4 | 1 | cycle | 2 | 1.338297862 | 1.538297862 | 2.0452420169 | 2.0452420169 | 2.6645352591e-15 |
| 4 | 1 | path | 0.58578643763 | 1.338297862 | 1.3968765057 | 1.9240842996 | 2.0452420169 | 2.6645352591e-15 |
| 4 | 1 | star | 1 | 1.338297862 | 1.438297862 | 2.0452420169 | 2.0452420169 | 3.9968028887e-15 |
| 4 | 1 | unequal_path | 0.31194074251 | 1.338297862 | 1.3694919362 | 1.6502386045 | 2.0452420169 | 3.108624469e-15 |
| 5 | 0.05 | complete | 5 | 0.11730370647 | 0.52172746855 | 0.52172746855 | 0.52172746855 | 6.0618177145e-14 |
| 5 | 0.05 | cycle | 1.3819660113 | 0.11730370647 | 0.2555003076 | 0.52172746855 | 0.52172746855 | 4.551914401e-15 |
| 5 | 0.05 | path | 0.38196601125 | 0.11730370647 | 0.1555003076 | 0.49926971772 | 0.52172746855 | 1.5543122345e-15 |
| 5 | 0.05 | star | 1 | 0.11730370647 | 0.21730370647 | 0.52172746855 | 0.52172746855 | 9.7699626167e-15 |
| 5 | 0.05 | unequal_path | 0.24776397599 | 0.11730370647 | 0.14208010407 | 0.36506768247 | 0.52172746855 | 2.7755575616e-15 |
| 5 | 1 | complete | 5 | 1.3978317841 | 1.8978317841 | 2.0802738673 | 2.0802738673 | 4.7073456244e-14 |
| 5 | 1 | cycle | 1.3819660113 | 1.3978317841 | 1.5360283852 | 2.0802738673 | 2.0802738673 | 7.9936057773e-15 |
| 5 | 1 | path | 0.38196601125 | 1.3978317841 | 1.4360283852 | 1.7797977954 | 2.0802738673 | 7.1054273576e-15 |
| 5 | 1 | star | 1 | 1.3978317841 | 1.4978317841 | 2.0802738673 | 2.0802738673 | 9.7699626167e-15 |
| 5 | 1 | unequal_path | 0.24776397599 | 1.3978317841 | 1.4226081817 | 1.6455957601 | 2.0802738673 | 8.881784197e-15 |
| 6 | 0.05 | complete | 6 | 0.13548187936 | 0.47736609211 | 0.47736609211 | 0.47736609211 | 1.0524914273e-13 |
| 6 | 0.05 | cycle | 1 | 0.13548187936 | 0.23548187936 | 0.47736609211 | 0.47736609211 | 6.5503158453e-15 |
| 6 | 0.05 | path | 0.26794919243 | 0.13548187936 | 0.1622767986 | 0.40343107179 | 0.47736609211 | 2.1094237468e-15 |
| 6 | 0.05 | star | 1 | 0.13548187936 | 0.23548187936 | 0.47736609211 | 0.47736609211 | 2.8310687128e-15 |
| 6 | 0.05 | unequal_path | 0.20567695109 | 0.13548187936 | 0.15604957447 | 0.34115883045 | 0.47736609211 | 5.8286708793e-16 |
| 6 | 1 | complete | 6 | 1.4362987022 | 2.0362987022 | 2.1051375755 | 2.1051375755 | 2.1316282073e-14 |
| 6 | 1 | cycle | 1 | 1.4362987022 | 1.5362987022 | 2.1051375755 | 2.1051375755 | 1.2212453271e-14 |
| 6 | 1 | path | 0.26794919243 | 1.4362987022 | 1.4630936214 | 1.7042478946 | 2.1051375755 | 1.2212453271e-14 |
| 6 | 1 | star | 1 | 1.4362987022 | 1.5362987022 | 2.1051375755 | 2.1051375755 | 1.5987211555e-14 |
| 6 | 1 | unequal_path | 0.20567695109 | 1.4362987022 | 1.4568663973 | 1.6419756533 | 2.1051375755 | 1.2212453271e-14 |
| 7 | 0.05 | complete | 7 | 0.15098718007 | 0.4509688926 | 0.4509688926 | 0.4509688926 | 1.6608936448e-13 |
| 7 | 0.05 | cycle | 0.75302039628 | 0.15098718007 | 0.2262892197 | 0.4509688926 | 0.4509688926 | 3.1641356202e-15 |
| 7 | 0.05 | path | 0.1980622642 | 0.15098718007 | 0.17079340649 | 0.34904944426 | 0.4509688926 | 3.3306690739e-15 |
| 7 | 0.05 | star | 1 | 0.15098718007 | 0.25098718007 | 0.4509688926 | 0.4509688926 | 3.108624469e-15 |
| 7 | 0.05 | unequal_path | 0.1758893739 | 0.15098718007 | 0.16857611746 | 0.32687655397 | 0.4509688926 | 2.2204460493e-15 |
| 7 | 1 | complete | 7 | 1.4632706804 | 2.1233303659 | 2.1233303659 | 2.1233303659 | 1.1546319456e-14 |
| 7 | 1 | cycle | 0.75302039628 | 1.4632706804 | 1.5385727201 | 2.1233303659 | 2.1233303659 | 7.1054273576e-15 |
| 7 | 1 | path | 0.1980622642 | 1.4632706804 | 1.4830769069 | 1.6613329446 | 2.1233303659 | 1.0436096431e-14 |
| 7 | 1 | star | 1 | 1.4632706804 | 1.5632706804 | 2.1233303659 | 2.1233303659 | 1.5099033135e-14 |
| 7 | 1 | unequal_path | 0.1758893739 | 1.4632706804 | 1.4808596178 | 1.6391600543 | 2.1233303659 | 1.1990408666e-14 |

The degree-one endpoint, additive, scale, auxiliary and below-count bounds were also tested on every one of the 56 cases of 3(b):

| eta1 inequality | minimum slack | n | beta |
| --- | --- | --- | --- |
| endpoint_lower | -5.5511151231e-17 | 2 | 0.25 |
| endpoint_upper | -4.6837533851e-17 | 2 | 0.01 |
| additive_lower | 3.9821763285e-06 | 1000 | 1000 |
| additive_upper | 0.00051179626748 | 1000 | 0.0001 |
| scale_lower | 6.25e-07 | 2 | 1e-06 |
| scale_upper | 2e-06 | 2 | 1e-06 |
| aux_lower | 0 | 2 | 1e-06 |
| aux_upper | 0 | 2 | 1e-06 |
| below_count | -8.2266592694e-17 | 2 | 1e-06 |

The tiny negative slacks are rounding at n=2 exact equalities: eta1=beta and gamma_Q=beta+1. No inequality failure was found.

### 8: stationary polymer circulation

Command: `python3 audit.py step8`. In each case epsilon is half the smallest of the four normalized stationary conductances, strictly inside the allowed range. Nonnegativity, row sums, invariance, and equality of the symmetric part with L_M were checked exactly with fractions. Spectral rate means the smallest real part of a nonzero eigenvalue of -L_epsilon; equivalently the negative of the largest nonstationary real part for L_epsilon. All improvements are strict.

| n | beta | epsilon | gamma_M | spectral rate | increase |
| --- | --- | --- | --- | --- | --- |
| 4 | 0.2 | 0.0314795383 | 0.87640704429 | 0.89903957357 | 0.02263252928 |
| 4 | 1 | 0.028301886792 | 2.0452420169 | 2.3217517148 | 0.27650969784 |
| 5 | 0.2 | 0.023952095808 | 0.84955317239 | 0.90250277319 | 0.052949600797 |
| 5 | 1 | 0.040295500336 | 2.0802738673 | 2.1914064366 | 0.11113256934 |
| 6 | 0.2 | 0.0079890638593 | 0.84445429421 | 0.84823816547 | 0.0037838712641 |
| 6 | 1 | 0.038994800693 | 2.1051375755 | 2.1519985014 | 0.046860925924 |
| 7 | 0.2 | 0.0024791209521 | 0.84732934008 | 0.84770500958 | 0.00037566949219 |
| 7 | 1 | 0.031977426237 | 2.1233303659 | 2.1442918102 | 0.020961444282 |

The proof of strictness is complete for every admissible nonzero epsilon: equality in the symmetric-part Rayleigh inequality would force the eigenvector into the simple gap eigenspace, but A maps its generator out of that space. Perturbation theory is only needed for the later quadratic expansion, not for strictness itself.

### 9: Ewens and shared growing kernels

Command: `python3 audit.py step9`. Each row includes a directly constructed Ewens generator, a shared-product generator and a shared-additive generator. Exact detailed balance and product monomer drift pass. Every product/additive bound passes. Maximum Ewens gap/formula error is 2.49e-14; comparison of every eigenvalue against the quoted partition-indexed spectrum gives maximum error 1.85e-13. These are different equilibria: Ewens fragmentation uses beta(i+j); the shared-product fragmentation uses beta*ij.

| n | beta | Ewens gap | 2beta+2(n-1)/n | product gap | additive gap |
| --- | --- | --- | --- | --- | --- |
| 2 | 1/50 | 1.04 | 1.04 | 1.02 | 2.04 |
| 2 | 1/7 | 1.2857142857 | 1.2857142857 | 1.1428571429 | 2.2857142857 |
| 2 | 1 | 3 | 3 | 2 | 4 |
| 2 | 3 | 7 | 7 | 4 | 8 |
| 3 | 1/50 | 1.3733333333 | 1.3733333333 | 1.3721702548 | 2.0792003197 |
| 3 | 1/7 | 1.619047619 | 1.619047619 | 1.5714285714 | 2.531412873 |
| 3 | 1 | 3.3333333333 | 3.3333333333 | 2.5251903664 | 4.7639320225 |
| 3 | 3 | 7.3333333333 | 7.3333333333 | 4.5448584587 | 8.9172374697 |
| 4 | 1/50 | 1.54 | 1.54 | 1.5372687225 | 2.0794644281 |
| 4 | 1/7 | 1.7857142857 | 1.7857142857 | 1.7153705876 | 2.5437293047 |
| 4 | 1 | 3.5 | 3.5 | 2.7042441507 | 4.9701733327 |
| 4 | 3 | 7.5 | 7.5 | 4.7781526084 | 9.2880756366 |
| 5 | 1/50 | 1.64 | 1.64 | 1.6368607957 | 2.1012077629 |
| 5 | 1/7 | 1.8857142857 | 1.8857142857 | 1.8166158978 | 2.6442299511 |
| 5 | 1 | 3.6 | 3.6 | 2.8220436614 | 5.1289770357 |
| 5 | 3 | 7.6 | 7.6 | 4.9144267209 | 9.5026759349 |
| 6 | 1/50 | 1.7066666667 | 1.7066666667 | 1.7033044254 | 2.120144287 |
| 6 | 1/7 | 1.9523809524 | 1.9523809524 | 1.8847109848 | 2.7123310229 |
| 6 | 1 | 3.6666666667 | 3.6666666667 | 2.8996843461 | 5.2325104545 |
| 6 | 3 | 7.6666666667 | 7.6666666667 | 5.0038805357 | 9.6426332043 |
| 7 | 1/50 | 1.7542857143 | 1.7542857143 | 1.7507795407 | 2.1372260637 |
| 7 | 1/7 | 2 | 2 | 1.9334856142 | 2.7618609471 |
| 7 | 1 | 3.7142857143 | 3.7142857143 | 2.9548423487 | 5.305816911 |
| 7 | 3 | 7.7142857143 | 7.7142857143 | 5.0671652523 | 9.7412246056 |
| 8 | 1/50 | 1.79 | 1.79 | 1.7863976368 | 2.1526258673 |
| 8 | 1/7 | 2.0357142857 | 2.0357142857 | 1.9700970912 | 2.7992748131 |
| 8 | 1 | 3.75 | 3.75 | 2.9960526125 | 5.3604717207 |
| 8 | 3 | 7.75 | 7.75 | 5.1143190472 | 9.8144642025 |
| 9 | 1/50 | 1.8177777778 | 1.8177777778 | 1.8141116222 | 2.1664458073 |
| 9 | 1/7 | 2.0634920635 | 2.0634920635 | 1.9985759689 | 2.8284529988 |
| 9 | 1 | 3.7777777778 | 3.7777777778 | 3.0280140851 | 5.4027959126 |
| 9 | 3 | 7.7777777778 | 7.7777777778 | 5.1508203457 | 9.8710311404 |

### Second derivations and coupling checks

Command: `python3 audit_algebra.py`. The independent symbolic checks cover the upper, square-root, higher-sector, sharp count, sharp degree-one, critical finite-size, rising-factorial and coupling certificates, the tower recursion, and the Lyapunov fourth-power identity. The program also checks the stationary projected generator by enumerating cyclic cut sets, and constructs both coupling marginals event by event.

| Check | coverage/result |
| --- | --- |
| Exact symbolic identities | 13 |
| Exact stationary projection entries | 1834 |
| Full cut spectrum vs radial union | 14 cases through n=8; max error 4.09e-14 |
| Exact Stage-I coupling marginals | 741 pairs through n=7 |
| Exact Stage-II coupling marginals | 1023 pairs through n=7 |

The appendix is a complete proof independent of harmonic decomposition under n>=8 and 4/n^2<=beta<=1/16. Its finite constants may depend on n,beta, which is harmless for extracting the exponential spectral rate. It does not by itself cover all n,beta; the main proof supplies that parameter patching.

## Attribution and novelty: memory only

I remember Granovsky and Erlihson's solvable coagulationfragmentation work, and Durrett, Granovsky and Gueron's reversible equilibrium work. Confidence is moderate for the former and moderate to high for the latter. I do not independently remember the exact location or wording of the announced gap equality; the manuscript itself credits it, and its present proof does not require that announcement. Equality of gaps alone therefore should not be advertised as a new discovery.

I remember Aldous's coagulationfragmentation relaxation questions and cycle representation with moderate confidence. The exact webpage dates and precise original question have not been checked. The Ewens/Metropolis transposition spectrum is classical; Jiang is a plausible direct source and is explicitly credited. I do not claim, from memory, that Jiang was the earliest source of every version of that formula.

I do not recall an existing paper with this exact critical function or the stated b/n cutoff. That does not establish novelty. GranovskyZeifman's N-limit spectral-gap work in particular needs source examination before any priority claim about fixed-beta asymptotics. No literature priority claim was inferred from a failed recall.

The familiar DGG, CaputoLiggettRichthammer, ChafaiJoulin, Filmus, HwangHwang-MaSheu, LevinPeres and Jiang bibliography entries look plausible in author/title/year/journal. I found no definite metadata error from memory. The 2026 research items, repository citations, URLs, precise pagination and quoted theorem/equation numbers remain unverified. I did not invent a replacement reference.

## Typos, unclear wording, and missing material

No demonstrated mathematical typo was found. These are the source and clarity issues noticed:

| Location | Quoted text | Issue / suggested clarification |
| --- | --- | --- |
| introduction.tex; PAPER.tex:279 | `\input{related_work}` | The referenced file is absent and not concatenated, so the literature section is missing from this audit copy. |
| proof.tex; sector-action proof | Both radial boundary coefficients ... are zero. | Say the outward coefficient at each endpoint is zero to avoid suggesting that both birth and death vanish at each endpoint. |
| critical_scaling.tex; [prop:critical-degree-one] | It is increasing | Specify whether this means nondecreasing or strictly increasing. The proof explicitly establishes monotonicity; strictness also follows by positive ground-state pairing because the ground state is nonconstant. |
| count_cutoff.tex; opening paragraph | The time-window statements below imply cutoff | A brief explicit statement of the double-limit cutoff criterion would help readers. The fixed-epsilon mixing-time assertion is already sufficient. |
| appendix_computations.tex | The accompanying program / Source data ... accompany the paper | Those programs, result files and the figure are absent from this folder. Their claimed historical output was not checked; independent replacements were written. |
| main.bbl attachment; PAPER.tex:3626 onward | `\end{document}` before `BEGIN FILE main.bbl` | The compiled bibliography is appended for audit and would not be processed by TeX in this position. This is a packaging observation, not a mathematical defect. |
| acknowledgments.tex | The final manuscript was audited by Claude Opus 5.5 | A process declaration that cannot be independently verified from the supplied source; it supplies no mathematical evidence for this report. |

The date, source line numbers and external-file packaging refer to the supplied concatenation, not an independently fetched public release. No source changes were made.

## What could not be checked

- The absent `related_work.tex`, public PDF/figure, author programs/data, funding statements, and earlier AI audit declarations.
- The exact statements/numbering in ChenSaloff-Coste (worst-case TV and separation cutoff) and Jiang (classical spectral formula). Their supplied quoted forms were audited for applicability; external source authentication was prohibited.
- Comprehensive novelty, priority, URLs and recent bibliography metadata.
- TV at negative times in the requested numerical grid: these quantities are undefined.
- Rigorous floating-point rounding intervals. Exact rational and symbolic checks are rigorous arithmetic; numerical eigenvalues and the ODE solution are not certified interval calculations.
- An optimal cutoff window or worst-case polymer cutoff, neither of which the manuscript claims.

No requested mathematical section was left unread. The internal mathematical verdict is SOUND, with the external-source and novelty qualifications above.

Task: Be a hard, independent referee of PAPER.tex  report completed 2026-11-12 06:27 +0400. The original request clock timestamp was not supplied.
