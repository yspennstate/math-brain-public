MINOR

The counterexample claim survives this audit. Theorems A, B and C are correct with the qualifications actually stated in CLAIM.md. In particular, the bounded case really covers every norm in the survey's Definition 5, including infinite-valued and non-Fatou functionals. The nonsymmetric n=4 example and the smooth examples also work. Independent rational calculations certify the continuous examples; floating-point grid checks are unnecessary.

The required revisions concern attribution, a small indexing omission, and reproducibility paths. Several auxiliary results are already in print, including Proposition 5 essentially verbatim in an equivalent formulation. The defensible contribution is the particular norm reduction and the explicit counterexamples with additional regularity, subject to the novelty qualifications below. This is a negative answer to the unrestricted converse and to several proposed regularity assumptions, not a full characterization of the additional hypotheses in Open Problem 4.

1. **Proposition 5 is an unattributed reformulation of a published theorem.** Location: CLAIM.md:249–262; also the summary at lines 27 and 528. Puccetti–Wang–Wang (2012), Theorem 3.2(b), characterizes discrete n-CM laws as countable mixtures of empirical laws of n points with the same mean. Wang's survey explicitly recalls this result in §2.3 and states the more general integral representation in Theorem 2. On finite support, the empirical probability vector is precisely k/n, so the submitted convex-hull criterion is exactly that specialization. The countable-support statement at line 260 is covered too. Required fix: identify Proposition 5 as this known theorem in count-vector coordinates and cite the original result. An independent proof does not make the characterization new. [Original theorem](https://www.math.uwaterloo.ca/~wang/papers/2012Puccetti-Wang-Wang-JAP.pdf), [survey](https://arxiv.org/abs/1411.6190).

2. **The novelty accounting for the discrete and n=2 results needs explicit prior attribution.** Location: CLAIM.md:23–27, 221–235, 528, and the literature table. Wang–Wang (2011), Proposition 2.3(2), already states 2-CM iff symmetry, and Proposition 2.3(3) and its proof construct Bernoulli(k/n) complete mixes. Mao–Wang (2015), Example 3.1, gives the entire Bernoulli aggregation set, which immediately yields the integer criterion in Theorem C. Bellini–Karaşan–Pınar (2016), Theorem 1, credited there to Haus, gives the related binary-matrix divisibility criterion. Required fix: add these references at the results and distinguish the norm-inequality part of C from its known mixability part. The submitted table omits the particularly relevant Mao–Wang and Bellini papers. The 2026 Mohammed citation is accurate but is much too late to establish priority for the integer criterion. [Wang–Wang](https://www.math.uwaterloo.ca/~wang/papers/2011Wang-Wang-JMVA.pdf), [Mao–Wang](https://www.math.uwaterloo.ca/~wang/papers/2015Mao-Wang-JMVA.pdf), [Bellini et al.](https://repository.bilkent.edu.tr/bitstreams/4e7bc6f3-b404-426a-b768-29db24e9fecd/download).

3. **Specify the starting index in the non-Fatou construction.** Location: CLAIM.md:142. Write k=1,2,… . The displayed average h_k is correct only when the interval lies in the nonzero part of v. If k=0 were included, L_0=1 and I_0 lies outside that part, so the asserted average would be wrong. With k≥1 every subsequent calculation is valid. This is a small specification omission, not a failure of Proposition 2.

4. **The reproduction instructions and source inventory do not match the delivered directory layout.** Location: CLAIM.md:33, 500–522. The commands refer to code/ and data/ beneath the current directory, but the delivered files are in claim_files/code/ and claim_files/data/. The listed source PDFs are absent from the delivered claim_files/sources/ directory; extracted text files are present. Required fix: say to change into claim_files/ before those commands, fix the relative source links, and either include the PDFs or accurately describe the text-only source bundle. This audit independently downloaded the primary sources and did not need the missing PDFs.

No other mathematical error or proof gap was found. In particular, I do not count the explicitly unproved converse for arbitrary unbounded laws and arbitrary non-Fatou norms as a gap in the theorem: the report carefully states only the implications it proves.

Verification of Theorem A, following the proof in order:

- **Definition and ambient space, lines 57–67.** I read Definition 5 in the survey itself. Its exact mathematical requirements are N:L⁰→[0,∞], with (i) N(aX)=|a|N(X); (ii) N(X+Y)≤N(X)+N(Y); (iii) N(X)=0⇒X=0 a.s.; (iv) X=ᵈY⇒N(X)=N(Y); (v) 0≤X≤Y⇒N(X)≤N(Y). There is no absolute-value axiom, completeness requirement, finiteness requirement on bounded variables, or Fatou axiom. The survey assumes an atomless probability space. Working on the probability interval is legitimate for these law-based assertions. In particular, a discrete *law* is still realized on an atomless space. [Definition 5](https://arxiv.org/html/1411.6190v3#S2.SS4).

- **Weak submajorization and the stop-loss identities, lines 59–96.** For nonnegative integrable Z, K_Z(a)=∫₀ᵃZ*(u)du has the two conjugate representations in (8). Taking infima or suprema proves the claimed equivalence of K order and stop-loss order, including the mean inequality at a=1. The z≥0 restriction is sufficient because these variables are nonnegative. At a=0 the infimum is zero by integrability. T_a is an admissible extended-valued norm for each a>0: its dual formula proves the triangle inequality and monotone convergence proves Fatou. Definiteness and law invariance hold. These norms detect every violation of weak submajorization. Testing only a selection of Lᵖ norms would not justify this conclusion.

- **Absolute extension, lines 98–104.** Replacing N by ν(Z)=N(|Z|) is legitimate because every argument in the inequalities is nonnegative. The positive monotonicity axiom and |Z+W|≤|Z|+|W| prove subadditivity of ν. No unjustified assertion N(Z)=N(|Z|) is used. If ν(V)=∞ there is nothing to prove, including when ν(U)=∞. If V=0, submajorization forces U=0. Otherwise finiteness of ν(V) implies finiteness of an indicator norm; finitely many equidistributed indicators cover 1 on the atomless interval. Thus 0<ν(1)<∞. Equation (10) then follows from monotonicity and the triangle inequality. The exceptional norm assigning infinity to every nonzero positive variable has therefore not been overlooked.

- **Conditional averaging, lines 106–125.** On each partition cell the conditional quantile is bounded and monotone. Its m equally spaced cyclic samples have average within M/m of its integral, uniformly apart from null endpoint choices. Every constructed V_j has the unconditional law of V. Subadditivity and (10) consequently give ν(E[V|P])≤ν(V). Strassen's increasing-convex-order coupling has U≤E[V|U]. Conditioning on the finite range partition of U gives the displayed comparison for U_δ; uniform convergence of U_δ to U finishes the argument. This is a valid proof for bounded variables with no Fatou or completeness assumption. Law invariance lets the coupling be realized on the interval without changing norm values.

- **Unbounded Fatou step, lines 127–131.** W_j=E[V∧j|U] is bounded and W_j≤cxV∧j by conditional Jensen. Hence the bounded result applies before any limit is taken. The sequence increases to E[V|U], and the positive Fatou property gives the desired comparison, with infinite limits permitted. This proves precisely the stated extension to integrable U,V for Fatou norms.

- **Non-Fatou counterexample, lines 135–183.** With the index correction above, v is decreasing, ∫v=1/3, and the disjoint I_k have integral 1/(2L_k). Thus h_k is their average, and U is a conditional expectation of V. The domain D is solid and law invariant. Its linearity follows from the rearrangement inequality at t/2 and replacing the two dilation indices by 2max(m₁,m₂). It contains V and all bounded variables and is contained in L¹. Consequently (14), with the stated convention at zero, satisfies all five axioms. On a positive-measure interval [t_k/2,t_k], U*/v(t/m) tends to infinity for every fixed m. In fact the first displayed ratio divided by L_k tends to 1/(4m), providing an independent asymptotic check. Thus U∉D, while V∈D. Truncating U demonstrates failure of Fatou. This is a valid example in the very broad definition being used; silently assuming a Banach function space would exclude it.

- **Scope of that counterexample.** It separates general unbounded submajorization from comparison in all Definition 5 norms. It does not produce a single integrable X for which X≤cxnμ−(n−1)X but an original hinge inequality fails. The submission expressly acknowledges this at lines 178–183 and 534. Neither the stronger converse nor its failure has been established here.

- **Threshold reduction, lines 188–212.** With c=n−1 and s=(nμ−t)/c, (Y−t)₊=c(X−s)₋ and (Y−t)₋=c(X−s)₊ pointwise. The first L¹ inequality for all real t is exactly the call-function criterion for X≤cxY, since the means agree. Conversely, composing either hinge with an increasing convex function gives the two increasing-convex orders in (17). Lemma 1 then supplies the required norms. The lower-quantile integrals on the right of the first line of (18), and upper-quantile integrals on the right of the second, have the correct orientations. Boundedness is used for the norm comparison, not for the elementary hinge identities.

- **n=2, lines 221–227.** Reflection preserves convex order. Applying reflection to X≤cx2μ−X gives the reverse comparison, hence equality in law. The call function's right derivative is −P(X>t), so atoms cause no difficulty. Symmetry supplies the explicit complete mix (X,2μ−X), and the two hinge laws match at complementary thresholds. Every norm inequality is then equality, even if both sides are infinite. This part holds for arbitrary integrable X without a Fatou restriction.

The extra discussion in §7 is consistent with this audit. The signed example N_α demonstrates why “law determined” must not be silently replaced by “absolute rearrangement invariant.” For the nondegenerate absolute Fatou norms, the usual associate-dual representation and completeness argument are appropriate. Proposition 2 blocks extending that representation to all Definition 5 functionals. The norm definition in the downloaded Wang–Wang (2016) author manuscript has four axioms, whereas the survey's Definition 5 also has positive monotonicity; the submission correctly uses the survey definition.

Verification of Theorem B:

All call gaps below were reconstructed from integrals of the densities, using rational coefficients. For each piece I independently computed C_Y(t) both directly as ∫(nμ−(n−1)x−t)₊f(x)dx and by put-call parity. The two expressions agree identically. A polynomial with nonnegative Bernstein coefficients on an interval is nonnegative throughout that interval, since the Bernstein basis functions are nonnegative and sum to one. The certificate file contains every interval, polynomial, and coefficient. This certifies a continuum of thresholds, not a grid.

For any law supported on [0,1] with the stated mean, checking D(t)=C_Y(t)−C_X(t) on [0,1] suffices: for t≤0, C_X(t)=μ−t and Jensen gives C_Y(t)≥μ−t; for t≥1, C_X(t)=0. Equality of means supplies convex order.

For density (2), direct integration gives mass 1, mean 1/2, and

\[
D(t)=-\frac{63}{80}t^4+\frac{63}{40}t^3
      -\frac{193}{160}t^2+\frac{67}{160}t+\frac{161}{1280},\qquad0\leq t\leq1.
\]

Its degree-four Bernstein coefficients on [0,1] are

\[
\left(\frac{161}{1280},\frac{59}{256},\frac{103}{768},
             \frac{59}{256},\frac{161}{1280}\right).
\]

All are positive. This is an explicit independent analytic certificate for the required convex order. There is also the simpler independent argument: any centered symmetric integrable Z satisfies Z≤cx cZ for c≥1, and cZ has the law of −cZ. Convexity and Jensen prove the scaling comparison, as in (19). The density has floor 1/10 and maximum 14/5 on the interval.

The non-3-CM argument is valid. If three centered values z_i=2x_i−1 all lie outside [−1/2,1/2], two share a sign and their sum has absolute value greater than 1, beyond the third value's ability to cancel. Hence every sum-3/2 triple contains a point in [1/4,3/4]. Integration gives central mass 13/80, both from a polynomial antiderivative and from 1/20+(9/10)(1/2)³. The expected number of coordinates in the central interval would be 39/80<1, which is impossible if that number is always at least one. Strictly speaking the deterministic statement uses the closed interval: (1/4,1/4,1) is a boundary exception to an open-interval assertion. CLAIM.md correctly uses the closed interval; absence of atoms at its endpoints gives the same probability for the open interval mentioned in the audit request.

For the nonsymmetric n=4 construction, I obtain ∫h₄=1, μ=81/200, and C_H(t)=(1−t)²(81−38t)/200. Re-expansion of D_H reproduces equation (26) exactly, and its Bernstein coefficients reproduce all four fractions in (27). In particular D_H≥5374873/56250000>0 on [0,1]. The endpoint law G₄ has the same mean, and independent addition of a uniform to the Bernoulli component preserves the centered convex order. Mixing G₄ and H₄ at this common mean also preserves the order. The density floor 43/1000 is valid. This example is nonsymmetric: its essential support is [0,1] and its mean is not 1/2.

The following bounds were obtained independently from exact interval sums and density integrals. They agree with every corresponding bound in the submission. Here d is distance from nμ to the n-fold sum of the indicated core, and q is probability outside the core.

| Law | n | Mean | d | q | Lower bound for E(S−nμ)² |
|---|---:|---:|---:|---:|---:|
| G₃ | 3 | 1/2 | 3/10 | 0 | 9/100 |
| F₃ | 3 | 1/2 | 3/10 | 2/25 | 171/2500 |
| G₄ | 4 | 81/200 | 7/25 | 0 | 49/625 |
| F₄ | 4 | 81/200 | 7/25 | 9/100 | 784/15625 |
| Density (2), core [0,1/5]∪[4/5,1] | 3 | 1/2 | 1/10 | 159/625 | 37/15625 |

For example, the core sum intervals adjacent to the n=4 target 81/50 end at 23/20 and begin at 19/10. Their distances to the target are 47/100 and 7/25, respectively. The smaller is indeed 7/25. The union bound gives P(all coordinates in the core)≥1−nq; on that event the squared deviation is at least d². Every listed bound is strictly positive and therefore rules out a complete mix. This argument holds for every coupling and needs no solver.

For Corollary 10, convolving with the prescribed independent symmetric bump preserves centered convex order by conditioning, and yields a globally C∞ density positive throughout the enlarged support interior. The G_n component, of probability 9/10, stays in the enlarged core. Adding n variables in [−η,η] can reduce the sum gap by at most nη. With η=1/100 the pre-normalization gaps remain at least 27/100 and 6/25. After the final affine map to [0,1], they are at least 9/34 and 4/17. Using q≤1/10 gives the additional certified bounds

\[
E(S-3\mu')^2\geq\frac{567}{11560}>0,\qquad
E(S-4\mu')^2\geq\frac{48}{1445}>0.
\]

Thus both smooth counterexamples work. The n=4 mean becomes 83/204, so it remains nonsymmetric. The smooth densities tend to zero at the endpoints; the theorem does not incorrectly claim a global compactly supported C∞ density with a positive endpoint floor. The distinct positive-floor examples are densities on the closed interval. The quantitative sufficient bound 3/[n(b−a)] in Puccetti–Wang–Wang (2013), Theorem 3.4, is not contradicted. [Density-floor theorem](https://www.math.uwaterloo.ca/~wang/papers/2013Puccetti-Wang-Wang-IME.pdf).

Verification of Theorem C and Proposition 5:

For 0<p<1, Y=np−(n−1)B has lower endpoint l=np−(n−1) and upper endpoint h=np. Convex order B≤cxY forces l≤0 and h≥1, giving 1/n≤p≤1−1/n. Conversely those endpoint inequalities place B inside [l,h]. The chord of any convex function through l,h dominates it on that interval; equal means make the chord expectations agree. This proves convex order and, by A, every original norm inequality. The two boundary values of p are included. The excluded degenerate laws p=0,1 pass and are CM, as the proof says.

For complete mixability the sum is an integer with expectation np, so its constant value must be an integer. If np=k, uniformly permuting a vector with k ones gives the required mix. This also exhibits counterexamples for every n≥3 by choosing an interior p with np nonintegral. For n=2 the permissible interior parameter reduces to 1/2, consistent with A.

For finite support, symmetrization gives an admissible count vector K with EK=np. Conversely a distribution on admissible count vectors, followed by a uniform coordinate permutation, realizes exactly the desired marginals. This proves (21), with no rationality assumption on atom locations or probabilities. The empty admissible set correctly gives impossibility. On countable support the analogous probability distribution on finite-count vectors is the right condition; an unqualified closure operation is not a substitute.

In the submitted three-atom example, my enumeration gives exactly (k₀,k₁,k₂)=(1,1,1) and (0,3,0). Thus every admissible triple contains at least one occurrence of 1, requiring p₁≥1/3, whereas p₁=1/50. This is an exact separating linear inequality for the convex hull. The target is reachable, and all atoms occur in an admissible triple; the example really defeats reachability alone. Symmetry about 1 independently verifies its norm condition.

Independent implementation and limits of the audit:

The implementation is [referee_code/check_exact.py](referee_code/check_exact.py), with output in [exact_run.log](referee_code/exact_run.log) and the rational certificates in [exact_results.json](referee_code/exact_results.json). It imports or executes nothing from claim_files/. Run from this directory:

```sh
python3 referee_code/check_exact.py
```

It certifies the call gaps of density (2), G₃, G₄, H₄, F₃ and F₄ by exact integration and Bernstein coefficients, verifies their masses and means, all the tabulated obstruction bounds, the smoothing margins, and the heavy-tail integral/asymptotic calculation. As a separate finite-law check it tests 2,700 rational Bernoulli cases with n=2,…,10 and denominators 2,…,25. Those comparisons check every support knot of the call-gap function, which suffices for each finite law because the intervening pieces are linear. The general statements are proved above; the finite sweep is a diagnostic, not an induction over p or n.

The final run used SymPy 1.13.1, one process, numerical-thread environment limits of one, and peak RSS 65,732,608 bytes, below 4 GB. No helper agents were started. I did not reproduce the submitted rearrangement heuristics, peak-memory claim, or every floating-point LP optimum; none is needed for the conclusions, and this report does not certify those numerical performance tables. The rounding-band LP described in §8 is a legitimate necessary relaxation: rounding changes a sum by at most n/(2M). Its infeasibility would be meaningful if certified, whereas exact midpoint-sum infeasibility without a band would not be.

Literature result, checked independently through 13 November 2026:

Primary PDFs and extracted text are in referee_sources/, with URLs and SHA-256 hashes in [manifest.json](referee_sources/manifest.json). They were downloaded independently by [fetch_sources.py](referee_code/fetch_sources.py). I searched the exact norm terminology and Open Problem 4, and combinations of complete mixability with convex order, counterexamples, smooth/positive densities and the named authors; I also checked Wang's publication and working-paper lists. The result is a qualified priority assessment, not a proof that no unindexed paper exists.

| Source | Relevant result and implication for novelty |
|---|---|
| [Wang, Probability Surveys 12 (2015)](https://arxiv.org/abs/1411.6190), §2.3–2.4 | Theorem 2 and the recalled PWW decomposition already contain Proposition 5. Definition 5 and Theorem 5 are the actual objects under audit. Open Problem 4 also asks for additional sufficient assumptions. |
| [Wang–Wang (2011)](https://www.math.uwaterloo.ca/~wang/papers/2011Wang-Wang-JMVA.pdf), Proposition 2.3, Theorem 2.4 and Corollary 2.9 | Symmetry iff 2-CM, Bernoulli/binomial constructions, and the monotone-density mean criterion are established results. The positive-class statement in §6 is not new. |
| [Puccetti–Wang–Wang (2012)](https://www.math.uwaterloo.ca/~wang/papers/2012Puccetti-Wang-Wang-JAP.pdf), Theorem 3.2(b), Theorem 4.2 | The discrete mixture characterization gives Proposition 5; the concave-density class is another known sufficient class. |
| [Puccetti–Wang–Wang (2013)](https://www.math.uwaterloo.ca/~wang/papers/2013Puccetti-Wang-Wang-IME.pdf), Theorem 3.4 | Supplies the stated quantitative density floor. An unspecified smaller positive floor has no such implication. |
| [Wang–Wang (2016)](https://www.math.uwaterloo.ca/~wang/papers/2015Wang-Wang-MOR.pdf), Theorem 2.1 and §3 | Necessary norm polygon inequalities and sufficiency for particular families. These do not establish A's equivalence for the threshold-family condition, or general n-CM from reflected convex order. |
| [Mao–Wang (2015)](https://www.math.uwaterloo.ca/~wang/papers/2015Mao-Wang-JMVA.pdf), Example 3.1 and §3 | Describes Bernoulli sums exactly and distinguishes aggregation sets from convex-order relaxations. Its Bernoulli result already implies the CM half of C. Its convex-order comparison is an aggregation-set statement, not A. |
| [Bellini–Karaşan–Pınar (2016)](https://repository.bilkent.edu.tr/bitstreams/4e7bc6f3-b404-426a-b768-29db24e9fecd/download), Theorem 1 and §2 | The binary-matrix criterion, attributed to Haus, is the finite rational analogue of the integer-sum obstruction. It is not an all-density norm converse. |
| [Yin–Zhu, arXiv:1706.05499v4](https://arxiv.org/abs/1706.05499), Examples 2.1 and 2.3 | Contains the odd-dimensional mass obstruction and the symmetric polynomial example. Equation (2) is its r=1 polynomial after an affine transformation and addition of a 1/10 uniform component. The obstruction and its basic shape are not new. |
| [Mao–Wang–Wang (2019)](https://www.math.uwaterloo.ca/~wang/papers/2019Mao-Wang-Wang-JAP.pdf), Theorem 5 | Characterizes sums of at least three uniform marginals by domination by the comonotonic sum. This is a convex-order characterization with specified uniform marginals, not one for arbitrary repeated marginals. |
| [Komisarski–Labuschagne (2024; online 2023)](https://doi.org/10.1007/s10959-023-01277-2), §1 and §3 | Reviews the known classes and extends necessary restrictions on possible averages/centers; its main results concern attainable distributions of averages. It does not establish the proposed norm converse. |
| [Koike–Lin–Wang (2024)](https://www.math.uwaterloo.ca/~wang/papers/2024Koike-Lin-Wang-MOR.pdf), Theorem 3 and Proposition 4 | Gives decompositions of joint mixes, including an exchangeable orbit-mixture representation. This is further prior context for Proposition 5, not a converse of the norm tests. |
| [Mutti–Semeraro, arXiv:2309.17346](https://arxiv.org/abs/2309.17346), revised 2025; JMVA 212 (2026), 105545 | Treats minimal convex sums of symmetric Bernoulli vectors and explicitly records failure of joint mixability in odd dimension. The odd Bernoulli obstruction is established background. |
| [Mohammed, arXiv:2604.17490v4](https://arxiv.org/abs/2604.17490), 29 October 2026, §4.4 | Explicitly recalls Bernoulli joint mixability iff the sum of the parameters is integral. This confirms the report's citation but is not the earliest source. |

The cited Yin–Zhu Proposition 3.1 really does state variance-only sufficiency for arbitrary finite-variance marginals. It is false: three Bernoulli(1/2) marginals satisfy its standard-deviation polygon inequality, but their integer-valued sum cannot equal 3/2. This is a defect in that source, not in the submitted counterexample. I used only the independently verified mass obstruction from it. Its claimed solution of a different large-n problem is not needed here. [Yin–Zhu v4](https://arxiv.org/html/1706.05499v4).

Two further 2026 search hits do not alter this assessment. Chaudhary–Khandelwal's October preprint concerns attainable sums of two uniform marginals via joint tail bounds; Martinevski's October preprint concerns attainment of characteristic-function bounds with prescribed marginals. Neither states the survey's all-norm threshold converse in its problem statement. I checked those statements, not all their proofs, and do not use their claims as established theorems. [Two-uniform preprint](https://arxiv.org/abs/2610.24197), [characteristic-function preprint](https://math.a-martinevski.com/publications/P02/).

Precisely, I found no earlier explicit statement of A's bounded all-Definition-5 equivalence, with its treatment of infinite-valued norms and the unbounded caveat, in the primary sources examined. Its ingredients are classical majorization, conditional averaging and Strassen coupling; those ingredients are not new. The link to the exact threshold family is the potential contribution. The n=2 mixability characterization is already known; its equivalence to this norm family is a short consequence of that reduction.

For B, the symmetric polynomial obstruction is prior work. The explicit positive-floor polynomial (2), the nonsymmetric four-summand positive-floor construction, and the quantified smoothing argument are valid refinements for which I found no exact predecessor in the checked sources. They should be described as explicit strengthened counterexamples built from known obstructions, rather than a new obstruction principle. For C, the mixability half and its arithmetic mechanism are old; the interval characterizing the norm tests is a simple application of A and the two-point chord argument, not a new Bernoulli mixability theorem. Proposition 5 is wholly a reformulation of prior work. The full additional-condition question in Open Problem 4 remains broader than these results.

Task: “You are a hard, independent referee for a probability journal … Write REPORT.md.” — 13 November 2026, approximately 03:14 Asia/Tbilisi.
