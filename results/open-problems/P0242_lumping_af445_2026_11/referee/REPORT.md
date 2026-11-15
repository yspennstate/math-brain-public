Independent referee report for PAPER.tex

The numbered mathematical results and their proofs are sound under the usual conventions supplied in the request: hitting times allow time zero, and auxiliary stopping-rule randomization is independent of future transitions. I found no counterexample to Theorem 1, Lemmas 2 and 4, or Propositions 2 and 5. Two local corrections are needed: restrict the opening sentence of Remark 6 to the Table 1 parameters, and require the set Z in Section 4 to be nonempty. Neither affects a proof of a principal result. Bibliographic accuracy and novelty have only the memory-based assessment requested here; they are not certified.

The following verdicts use the source line numbers in the unmodified PAPER.tex. “GAP” for an attribution means an explicit limit of verification, not a discovered mathematical gap. The qualified “WRONG” verdict concerns an unqualified reading of one sentence, with the counterexample below.

| Statement or step | Verdict | Reason |
|---|---|---|
| Network setup, 43–48 | CORRECT | Detailed balance is pi_x P_xy=w_xy/w; loops count once in vertex mass. |
| Induced-weight display, 50–57 | CORRECT | Fiber sums give the stated transition probabilities and stationary mass; total mass is preserved. |
| Contraction assertions, 72–75 | CORRECT | Commute follows from wR; the spectral variational quotient and Cheeger cuts restrict to fiber-constant objects. |
| Stopping-rule definition, 59–65 | CORRECT | Randomized stationary stopping is allowed, including time zero and periodic chains. |
| Formula (1), 66–68 | CORRECT | Independently derived by occupation flows and checked against three tiny-chain LPs. |
| Theorem 1 lower bound, 98–103 | CORRECT | Fixed-N comb limit gives N, identity gives 1, and chains have 2N+2 states. |
| Theorem 1 upper bound, 98–103 | CORRECT | All four inequalities in (2) are valid in discrete time. |
| Lemma 2 statement, 110–115 | CORRECT | Applies to a nonzero real eigenfunction; no positivity of the eigenvalue is required. |
| Normalization, 146 | CORRECT | Divide by nonzero g(i), including its sign. |
| Martingale display, 147–150 | CORRECT | Conditional increment equals Pg-lambda g=0. |
| Increment bound, 151 | CORRECT | In fact delta M=g(X_(t+1))-lambda g(X_t), so the sharper bound is 2. |
| Optional stopping, 151–152 | CORRECT | Stop at U wedge t; domination by 1+2U justifies passage to finite-mean U. |
| Mean-zero terminal eigenfunction, 152–154 | CORRECT | Stationarity gives pi g=lambda pi g, so E_i g(X_U)=pi g=0. |
| Final martingale display, 155–157 | CORRECT | The sum is bounded above by U and 1-lambda is positive. |
| “In particular,” 158 | CORRECT | Reversibility gives real lambda_2<1, including negative values and periodicity. |
| Two-state equality, 117 | CORRECT | With cross probabilities a,b, both times equal 1/(a+b). |
| Complete-graph equality, 117 | CORRECT | On K_m both times equal (m-1)/m. |
| (2), first inequality, 166–168 | CORRECT | Sample J independently from stationarity and stop at T_J; the mean is Kemeny's constant. |
| Random-target commute average, 170 | CORRECT | Average the starting-state-independent target sum and symmetrize. |
| Commute identity with loops, 170–171 | CORRECT | Commute=wR; loops affect the discrete-time clock through w, not resistance. |
| (2), second inequality, 169–171 | CORRECT | Expand induced masses into fibers, preserve w, and use pointwise resistance contraction. |
| (2), eigentime identity, 172 | CORRECT | tau_0=sum_(k>=2)(1-lambda_k)^(-1), without an aperiodicity hypothesis. |
| (2), third inequality, 172 | CORRECT | Each of the m-1 positive summands is at most tau_2. |
| (2), fourth inequality, 173 | CORRECT | Lemma 2 supplies the constant one. |
| One-state image, 173–174 | CORRECT | Its stopping time is zero; the original denominator is at least 1/2. |
| Remark 3 deduction, 178–184 | CORRECT | Conditional on the quoted estimate, both spectral contraction and hat_pi_*>=pi_* apply. |
| Remark 3 order statements, 185–187 | CORRECT | Bounded-degree pi_* is of order 1/n; comb log(1/pi_*) is Theta(N log t). |
| Lemma 4 statement, 193–197 | CORRECT | Removing the bridge isolates the stated side mass, including loops. |
| Lemma 4 restriction, 199–200 | CORRECT | Modify only y; all transitions before T_y remain the same. |
| Lemma 4 return-time argument, 200–201 | CORRECT | New pi_y=w_xy/(w(S)+w_xy), and return time is 1+H(x,y). |
| Comb definition, 204–215 | CORRECT | The weights, tooth holding probability and fiber map have the stated meanings. |
| Vertex weights, 228–229 | CORRECT | The formula for z_N includes its edge to c; w_c=r^N+ell. |
| Delta and (3), 230–234 | CORRECT | S_k=(1+delta)r^k-delta, including k=0. |
| Proposition 5(i), 236–237 | CORRECT | Bridge masses are S_k and w_yk; add along the path. |
| Centered hitting times, 239–240 | CORRECT | Formula (1) gives max_(x,j)d(x,j). |
| Median identity (4), 240–245 | CORRECT | The two strong-Markov decompositions cancel H(m,j). |
| Target c case, 246 | CORRECT | d(x,c)<=H(x,c)<=M. |
| Reverse spine and tooth crossings, 249–253 | CORRECT | Side masses are w-S_t and w-w_y_p. |
| Geometric bound (5), 250–252 | CORRECT | Extend the finite sum to infinity; r/(r-1)<=2. |
| Median at levels p>q, 254–256 | CORRECT | Both states at level p have median z_p and total mass C r^(p-1). |
| Number and cost of high levels, 255–256 | CORRECT | Exactly N-q levels; each costs at most C/(r-1)=1+delta. |
| States at levels <=q, 257–258 | CORRECT | Their full mass is S_q; baseline cost is at most 2(1+delta). |
| Tooth-target correction, 258–260 | CORRECT | Include j's H(c,z_q) baseline in S_q, then add at most h for the tooth edge. |
| Bound for d(c,j), 261–263 | CORRECT | Add the three contributions to obtain at most B. |
| Pairs x,j distinct from c, 265–270 | CORRECT | The median is not c, and H(c,m)>=H(c,z_N)=rho. |
| Proposition 5(ii), 221–222, 270 | CORRECT | The three cases give max(B,M+B-rho); rho>=M gives B. |
| Induced path weights, 272–273 | CORRECT | Each spine conductance becomes (1+alpha)r^k, and loops remain in vertex masses. |
| Proposition 5(iii), first display, 274–277 | CORRECT | Each of the first N side masses contains w_yk. |
| Proposition 5(iii), second display, 278–283 | CORRECT | Every summand is nonnegative; keep the c summand and use hat_pi_c=pi_c. |
| Lower-bound parameter choice, 291–292 | CORRECT | Delta<=1 and ell can enforce both rho>=M and pi_c>=1-1/t. |
| Lower-bound display and limit, 293–297 | CORRECT | For fixed N the displayed expression tends to N as t grows. |
| Table 1, 299–315 | CORRECT | All four exact recomputations round to the printed entries. |
| Remark 6 opening sentence, 318 | WRONG if unqualified | N=1,r=2,alpha=h=1,ell=0 has ratio 1, not below 1; the Table 1 reading is correct. |
| Remark 6 two fractions, 319–323 | CORRECT | Both recompute exactly. |
| Remark 6 maximizing pair and ratio, 324–325 | CORRECT | (1,0) is a maximizer in both chains; so is (0,1); the ratio is correct. |
| Domain of (6), 329 | GAP, minor | “Proper subset” should be “nonempty proper subset”; resistance to the empty set is not specified. |
| (6), occupation sum | CORRECT | Count each visit at times 0 through T_Z-1, including holding visits. |
| (6), hitting-probability factorization | CORRECT | Strong Markov at T_y, with T_y=0 at y. |
| (6), diagonal Green/resistance identity | CORRECT | Escape-before-return probability is 1/(w_y R(y,Z)), also with loops. |
| Rayleigh under fiber gluing, 339–342 | CORRECT | Shorting source fibers and other fibers cannot raise source-to-A resistance. |
| Section 4 display, first inequality, 344 | CORRECT | Replace every hitting probability by 1. |
| Section 4 display, fiber expansion, 345 | CORRECT | hat_w_b=sum_(y in fiber b)w_y, also for new loops. |
| Section 4 display, resistance inequality, 346 | CORRECT | Apply pointwise contraction with nonnegative coefficients w_y. |
| Section 4 display, Green equality, 346 | CORRECT | Use G_A(y,y)=w_y R(y,A). |
| Section 4 display, last inequality, 346 | CORRECT | A diagonal occupation count is at most total occupation before T_A. |
| Proposition 2 first statement, 129–133 | CORRECT | The display proves the first bound; count n-|A| summands for the second. |
| Proposition 2 second statement, 134–135, 348–353 | CORRECT | With singleton c and the comb scaling the hitting-time ratio tends to N. |
| Factor-of-about-two assertion, 36–38 | CORRECT | The universal factor is 2N+1 and the examples approach N. |
| Aldous–Fill exact labels and discrete-time quoted estimate | GAP in verification | The arguments are independently correct, but exact source statements were not available under the no-browsing rule. |
| Hermon–Peres historical description | CORRECT as far as recalled | Consistent with the known logarithmic bounded-degree sensitivity result; exact theorem/remark labels unverified. |
| Novelty and “Open Problem 4.48(b),” 105–108 | GAP in verification | I cannot independently certify this precise attribution or priority from memory. |

For clarity, there is no substantive missing step in the delicate low-level accounting. Write C=1+r+alpha+h alpha. At each level p>q the combined mass of z_p,y_(p-1) is C r^(p-1), and H(c,z_p)/w<=r^(1-p)/(r-1), so the contribution is at most C/(r-1)=1+delta. At levels <=q the *full* mass, including the target, is S_q. For a tooth target, allocate H(c,z_q) to the target in this baseline and add pi_j H(z_q,j)<=h afterwards. For x,j!=c, the path from c to their median includes the edge c,z_N; thus H(c,m)>=rho even when x=j or one is itself a tooth.

The stationary-stopping formula was checked without assuming it. Expected departure counts v solve v(I-P)=delta_i-pi, v>=0. All solutions differ by c pi. The minimum total mass is obtained when some v_j=0. For h_j(x)=H(x,j), (I-P)h_j=1-e_j/pi_j, so H(i,j)-E_pi T_j=sum_x v_x-v_j/pi_j. Maximizing over j gives the minimum total mass. The corresponding stopping policy at x stops with probability pi_x/(v_x+pi_x), realizing the minimizing occupation flow. This proof permits periodicity and external randomization.

The additional spectral contraction used in Remark 3 also has an independent variational proof: the induced Dirichlet form and variance equal the original ones on fiber-constant functions. The infimum defining the spectral gap is therefore over a smaller space, giving gap(hat_X)>=gap(X) and tau_2(hat_X)<=tau_2(X). This remains true for negative second eigenvalues. Similarly, induced Cheeger cuts are a subset of original cuts with the same masses and boundary flows. The statement about maximal commute times follows directly from the already checked pointwise wR contraction.

Numerical checks used independent code in referee.py. All chains were processed serially, with numerical threading restricted to one. No run lasted more than four seconds according to its own recorded elapsed time; all matrices have order at most 18. The attempted low-priority `nice` wrapper was refused by the sandbox (“setpriority: Operation not permitted”), so no claim is made that priority was lowered. No browsing, external state changes, other agents, pushes, or visible windows were used. PAPER.tex was not edited.

The three tiny-chain LPs used nonnegative occupation flows with equality constraint (I-P)^T v=delta_i-pi and objective sum v:

| Chain | Optimal means by starting state | tau_stop by (1) | LP agreement |
|---|---|---|---|
| Periodic two-state flip | 1/2, 1/2 | 1/2 | yes |
| P=[[1/2,1/2],[1/4,3/4]] | 4/3, 4/3 | 4/3 | yes |
| Periodic three-state path | 3/2, 1/2, 3/2 | 3/2 | yes |

Step 2 used four fixed-seed batches. Weights in the uneven ensemble range from 10^-20 to 9*10^20. All two-state chains and all uneven cases used rational hitting times, plus exact two-state spectral values or 110-decimal-digit symmetric eigensolving. Other cases were screened for poor conditioning and small gap. Eleven double-precision ratios slightly above one were rechecked with rational hitting times and 110-digit eigenvalues. None exceeded one at meaningful precision; the high-precision check tolerates only 10^-80. Every two-state chain attains the exact value one.

| Seed | Chains | Negative lambda_2 detected | Deliberately periodic | Rational/high-precision cases | Raw double maximum | Rechecked maximum |
|---|---:|---:|---:|---:|---:|---:|
| 742019 | 5250 | 1766 | 1314 | 1965 | 1.0000000000000002 | 1 |
| 742020 | 5250 | 1795 | 1314 | 1965 | 1.0000000000000002 | 1 |
| 742021 | 5250 | 1786 | 1314 | 1965 | 1.0000000000000004 | 1 |
| 742022 | 5250 | 1769 | 1314 | 1965 | 1.0000000000000002 | 1 |
| Total | 21000 | 7116 | 5256 | 7860 | 1.0000000000000004 | 1 |

There were 3,500 chains of each size 2 through 7. The ensemble counts were 5,256 dense, 5,256 periodic bipartite, 5,256 nearly equal complete-loopless, and 5,232 uneven-weight chains. The largest tau_2/tau_stop is **1**. These are tests of the formula and proof, not a substitute for the proof.

Step 6 tested every requested parameter label, with t instantiated at 2, 16 and 256. For each t and N there were 4^4=256 cases: r in {2,3,10,1+t^3}, alpha in {1/10,1,7,t}, h in {1,2,50,t}, ell in {0,1,r^N,10^100 r^N}. Repeated numerical values arising from different labels were retained. Thus 3,840 labeled cases were tested. The exact solver grounded the graph Laplacian at c, inverted it over fractions, reconstructed all hitting times, and checked every first-step Poisson equation. It did not use Lemma 4.

In the next table U=max(B,M+B-rho), L=N h alpha/(1+alpha). Each entry is the largest ratio in that row's 256 cases, so a violation would be an entry greater than one. Every exact parameter, max_x H(x,c), tau_stop(X), tau_stop(hat_X), H_hat(b_0,c), M,B,rho,U,L,pi_c L and the four comparison ratios is in comb_t2.csv, comb_t16.csv or comb_t256.csv. Maxima and witnesses are also saved in the corresponding JSON files.

| t | N | Cases | max H(x,c)/M | tau_stop(X)/U | L/H_hat(b_0,c) | pi_c L/tau_stop(hat_X) | Violations |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 256 | 0.965138946 | 0.933955449 | 0.786163522 | 0.786163522 | 0 |
| 2 | 2 | 256 | 0.966122818 | 0.935884526 | 0.826719577 | 0.826719577 | 0 |
| 2 | 3 | 256 | 0.967169323 | 0.937816965 | 0.843189279 | 0.843189279 | 0 |
| 2 | 4 | 256 | 0.968164354 | 0.939647256 | 0.851826486 | 0.851826486 | 0 |
| 2 | 5 | 256 | 0.969101937 | 0.941373945 | 0.857106731 | 0.857106731 | 0 |
| 16 | 1 | 256 | 0.980737172 | 0.962202440 | 0.973953808 | 0.973953808 | 0 |
| 16 | 2 | 256 | 0.981101216 | 0.962903518 | 0.986074971 | 0.986074971 | 0 |
| 16 | 3 | 256 | 0.981451755 | 0.963579063 | 0.990183002 | 0.990183002 | 0 |
| 16 | 4 | 256 | 0.981789527 | 0.964230443 | 0.992249880 | 0.992249880 | 0 |
| 16 | 5 | 256 | 0.982115218 | 0.964858933 | 0.993494153 | 0.993494153 | 0 |
| 256 | 1 | 256 | 0.996124025 | 0.992277980 | 0.996063412 | 0.996063412 | 0 |
| 256 | 2 | 256 | 0.996138990 | 0.992307680 | 0.998020195 | 0.998020195 | 0 |
| 256 | 3 | 256 | 0.996153840 | 0.992337152 | 0.998674166 | 0.998674166 | 0 |
| 256 | 4 | 256 | 0.996168576 | 0.992366400 | 0.999001473 | 0.999001473 | 0 |
| 256 | 5 | 256 | 0.996183200 | 0.992395425 | 0.999197960 | 0.999197960 | 0 |

Step 7 reproduced Table 1 at t=256, r=1+t^3, with D=1+(1+delta)(r^N-1), w_c=(N+2)t^2 D, and ell=w_c-r^N. Besides the Laplacian algorithm, a second exact algorithm formed directed edge-cut masses and added edge-crossing means along unique tree paths. Both algorithms gave the same entire hitting matrix in each original and induced chain.

| N | States | tau_stop(X) | tau_stop(hat_X) | Ratio | Printed rounding correct? |
|---:|---:|---:|---:|---:|---|
| 1 | 4 | 257.003911455 | 256.011693576 | 0.996139289 | yes |
| 2 | 6 | 258.007835626 | 511.019493475 | 1.980635558 | yes |
| 4 | 10 | 260.015681425 | 1021.035090734 | 3.926821202 | yes |
| 8 | 18 | 264.031369972 | 2041.066282206 | 7.730393106 | yes |

The exact rational values, without decimal rounding, are:

- N=1: tau_stop(X) = `14278506430873105859327/55557545214098407683`; tau_stop(hat_X) = `2031911605883309270126/7936792173442629669`; ratio = `14223381241183164890882/14278506430873105859327`.
- N=2: tau_stop(X) = `5379649389014732012908282356274039301/20850720971148473590868243431948805`; tau_stop(hat_X) = `10655124869261314665334069890891447562/20850720971148473590868243431948805`; ratio = `10655124869261314665334069890891447562/5379649389014732012908282356274039301`.
- N=4: tau_stop(X) = `58573115712199383577271001600215428707234685666590811926437680761/225267627671865918635276613362811834169411645005030507455411387`; tau_stop(hat_X) = `2530067679252933526403360050522030065317666685505322551657335092796/2477943904390525104988042746990930175863528095055335582009525257`; ratio = `843355893084311175467786683507343355105888895168440850552445030932/214768090944731073116660339200789905259860514110832977063604829457`.
- N=8: tau_stop(X) = `6844704163541055927907203217172217431584082727565832952849081156757596002242956142889441062431900002662183888202077810818695/25923829294479416344169313044503874881315902304216103982837695392815844712501355314208358929739171421470072221241535760401`; tau_stop(hat_X) = `52912253878631214261747089989469628601522237976597945407802554655291181522820328981036695338963765753417770898655767435271576/25923829294479416344169313044503874881315902304216103982837695392815844712501355314208358929739171421470072221241535760401`; ratio = `52912253878631214261747089989469628601522237976597945407802554655291181522820328981036695338963765753417770898655767435271576/6844704163541055927907203217172217431584082727565832952849081156757596002242956142889441062431900002662183888202077810818695`.

For Remark 6 the exact values are:

| Quantity | Recomputed value | Maximizing pairs |
|---|---|---|
| Original tau_stop | 149731115/63193903 = 2.369391790850456... | (0,1), (1,0) |
| Induced tau_stop | 346900/114917 = 3.018700453370694... | (0,1), (1,0) |
| Ratio | 419679620/329408453 = 1.274040226284054... | — |

The printed pairs need not be unique, and the paper does not claim uniqueness. However, the first sentence of the remark needs qualification: the N=1 comb at r=2,alpha=h=1,ell=0 has original and induced tau_stop both exactly 3/2. It is a loopless weighted star, and the gluing merges two leaves. This refutes “below one” for the full comb family, while the N=1 row of Table 1 is correct.

Step 8 used 600 random networks with random surjective partitions and nonempty proper target unions of fibers, seed 382947. All hitting-time comparisons and every intermediate Green/resistance comparison were exact. The matrix G was checked against its occupation Poisson equations. The probabilities P_x(T_y<T_A) were obtained from separate harmonic Dirichlet solves, not inferred from the factorization being tested.

| States | Networks | max hat_H / sum_y H_y | max sum_y H_y / ((n-|A|)max_y H_y) | Largest observed lumping factor | Violations |
|---:|---:|---:|---:|---:|---:|
| 3 | 150 | 1.000000000000 | 1.000000000000 | 1.000000000000 | 0 |
| 4 | 150 | 1.000000000000 | 1.000000000000 | 1.000001039967 | 0 |
| 5 | 150 | 1.000000000000 | 1.000000000000 | 1.339726633884 | 0 |
| 6 | 150 | 1.000000000000 | 1.000000000000 | 1.020035293083 | 0 |

The four ensembles contributed 152 dense, 152 periodic, 148 complete-loopless and 148 uneven networks. Some tests have only one original state outside A, explaining the equality maxima in the two bound columns. A one-state induced chain was separately checked to have tau_stop=0; Proposition 2 does not have a nonempty proper target in that degenerate image.

These are the commands that produced the numerical tables. Run them in order, one process at a time. The `nice` warning described above is harmless to execution but means priority lowering was unavailable. Thread settings include the LP's explicit HiGHS threads=1 setting. Exact raw results are retained in tiny_results.json, spectral_0.csv through spectral_3.csv and their JSON summaries, spectral_recheck.json, comb_t*.csv/json, published_examples.json, and set_results.csv/json.

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
nice -n 15 python3 referee.py tiny
nice -n 15 python3 referee.py random_spectral --batch 0
nice -n 15 python3 referee.py random_spectral --batch 1
nice -n 15 python3 referee.py random_spectral --batch 2
nice -n 15 python3 referee.py random_spectral --batch 3
nice -n 15 python3 referee.py spectral_recheck
nice -n 15 python3 referee.py comb_grid --t 2
nice -n 15 python3 referee.py comb_grid --t 16
nice -n 15 python3 referee.py comb_grid --t 256
nice -n 15 python3 referee.py published_examples
nice -n 15 python3 referee.py set_grid
python3 make_report.py
```

Typos and unclear wording noticed:

- Lines 47–48: explicitly define T_A=inf{t>=0:X_t in A}, and use T_y^+ for a return time. This removes a convention that matters to (1), the bridge proof and (6).
- Lines 63 and 150–151: make independence of auxiliary randomization from future transitions explicit. With ordinary randomized stopping times the proof is correct; arbitrary anticipatory enlargement of the filtration would not be legitimate.
- Lines 119–122: “the lower bound ... is attained along a family” can suggest a finite-parameter maximum. The proof gives ratios approaching N; “is approached along a family” is more precise.
- Line 151: the increment bound 4 is valid, but 2 follows immediately from the displayed martingale. This is a loose bound, not an error.
- Lines 255–256: “by the first equality in (5)” is an awkward reference because (5) starts with an inequality. Say “by the geometric-series bound in (5).”
- Lines 257–260: explicitly include j's baseline H(c,z_q) contribution in the S_q bound before adding the extra tooth-edge cost. The present sentence is reconstructible but makes the reader wonder where j was counted.
- Lines 286–288: qualify the informal rare-entry/about-h explanation by “in the parameter regime used below.” For general allowed alpha,r,h, tooth entry need not be rare.
- Line 318: restrict “gives ratios below one” to the preceding Table 1 parameter choice. It is false for the full N=1 comb family, as the exact ratio-one example shows.
- Line 329: insert “non-empty” before “proper subset Z.” Without it the resistance and finite Green formulas are outside the stated domain at Z empty.

No other definite typographical errors were noticed. The decimal strings in Remark 6 have ellipses and are valid truncations; they need not be rounded to four decimal places.

Attributions and novelty, from memory only:

The Lovasz–Winkler access-time formula is a known stationary-stopping result, and the paper states it correctly. I recall the broad Aldous–Fill contraction principle and the open lumping question; the precise proposition/problem labels, the exact four-vertex historical example, and the assertion that Open Problem 4.48(b) asks this exact constant-one question are not independently verified here. The quoted discrete-time Lemma 4.23 estimate was an assumption of the requested deduction check, and the deduction is correct. I have not confirmed that source's exact constants or hypotheses.

The account of Hermon–Peres is consistent with my recollection of their logarithmic bounded-degree mixing sensitivity result, with lazy total-variation times transferred to stationary-stopping times by the standard reversible-chain comparison. I cannot independently certify Theorem 3(c), Remark 1.8, their precise lumping construction, or the bibliographic pagination from memory. No source was consulted.

I do not know a reliable prior citation for exactly tau_2<=tau_stop with constant one in the conventions used here, nor for this exact application of the additive eigenfunction martingale to stationary stopping rules. The martingale itself is a standard additive/Dynkin martingale. Familiarity with that device is not evidence that the sharp comparison is new or old. I know the cited logarithmic bounded-degree result, but do not recall an existing linear-in-state-count lumping theorem for unrestricted reversible weighted networks. Absence from my recollection does not certify novelty.

Other limits of the check: the linked repositories and the author's earlier numerical program were not inspected; no such program was supplied locally. Author/agent provenance, funding, affiliations, conflicts, and external publication metadata cannot be established from this source alone. The continuous-time/total-variation equivalence and external bibliographic details were not independently reproved. There was no web or literature search. The exact tests are finite evidence, while the analytic arguments above establish the claimed general inequalities.

The final verdict concerns the main mathematics: the local wording and domain corrections above should be made before publication, and priority/attribution should be checked by someone with access to the cited sources. They do not expose a gap in a principal proof.

Task: “refereeing a short mathematical paper before it is made public” — 2026-11-12 02:51 +04.

Overall verdict: **SOUND**
