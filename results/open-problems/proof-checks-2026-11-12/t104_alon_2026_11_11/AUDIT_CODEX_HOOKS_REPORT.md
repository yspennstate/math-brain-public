# Referee report

11 November 2026. Sources are unchanged. `H` denotes HOOKS_AND_TWO_ROWS.md and `G` denotes GAP_STATE_FORM.md. Proposition 1 of N4_PROOF.md is accepted as permitted. No browsing, other agents, external code, pushes, or writes outside this folder were used.

The main representation identities and scalar algebra check out. The notes nevertheless contain false statements: the asserted spanning of V_22, the edge-vector interval for theta, and the equality classification for the leading terms. The covariance argument also omits normalization and a treatment of zero projected states. These issues do not supply a counterexample to Conjecture F or to Alon's conjecture. Neither conjecture is proved here for general n.

## Verdict table

Each numerical/conjectural statement is marked NOT A PROOF even when its numerical evidence agrees with mine. A GAP refers to the printed justification; repairs supplied below are distinguished from that justification.

| Statement | Verdict | Reason |
|---|---|---|
| H1: hook Specht module is exterior^k V | CORRECT | The hook polytabloid maps equivariantly to the wedge of its column differences; dimensions agree. |
| Lemma H: transposition rank-one argument | CORRECT | All wedge terms with two projection factors vanish. |
| Lemma H: spectrum and bottom eigenvalue | CORRECT | The derivation of a diagonal operator has the distinct-eigenvalue sums. |
| H1: hook ratio >= k/j | CORRECT | The next eigenvalues are at least the average of the first j; use the undivided inequality if the denominator vanishes. |
| H1: reported hook search ratios | NOT A PROOF | They agree with k/j; searches do not establish global sharpness. |
| H2: conjugation identity | CORRECT | The entire spectrum is reflected about W by tensoring with sign. |
| H2: reformulation for tau=[2,1^(n-2)] | CORRECT | Rearranging 2W-lambda_max(L)>=c(2W-lambda_max(mu)) gives exactly the displayed bound. |
| H2: hook mu permits c=1 | CORRECT | The largest k-term sum is at least the largest eigenvalue. |
| H3: matrix model and dimension | CORRECT | Zero-diagonal symmetric row-zero matrices give the [n-2,2] summand, of dimension n(n-3)/2. |
| H3: Rayleigh quotient | CORRECT | Counting the swapped entries gives the displayed unordered-edge quotient. |
| H3: orthogonal projection and norm | CORRECT | On trace-zero diagonals, diag(Pi diag(d) Pi)=(n-2)d/n. |
| H4: star minima and equivalence of the two F formulations | CORRECT | The star minima are n-2 and n-1, and conjugation gives the equivalence. |
| Conjecture F | NOT A PROOF | Explicitly conjectural; n=4 follows from the supplied Theorem 3, whose elementary argument checks. |
| H4: star and single-edge equality examples | CORRECT | At a single edge both original bottom eigenvalues vanish. |
| H4: random/search support for F | NOT A PROOF | Original outputs are absent; independent checks below give no contrary evidence. |
| H4: dual form | CORRECT | This is Proposition 1 after sign twist, with the stated edge norm. |
| H4: explicit star and edge measures | CORRECT | They satisfy the row constraints; their expected edge energies give the asserted tight edges. |
| H5: uniform construction's N and A_ij | CORRECT | Direct projected matrices reproduce both, for the homogeneous covariance state. |
| H5: exactness at star/edge and failure between | CORRECT | Both endpoint states match; the supplied intermediate vector gives negative slack, and so does the two-edge path. |
| H5: P(xy) spans V_22 for every x | WRONG | At the edge vector its image has dimension one, whereas dim V_22=2. |
| H5: formula (*) | CORRECT | It is (n-1) times the unnormalized slack; the normalized slack has an additional projected-trace denominator. |
| Reduction R, as justified by the asserted rho(x,C) | GAP | The note does not define its normalization or handle zero images; a density-matrix limit argument repairs the global reduction. |
| H5(a): omega trial and negative minima | NOT A PROOF | Explicitly an unsuccessful numerical trial; the quoted minima were not independently replicated. |
| H5(b): symmetry reduction to C(theta) and affine slacks | CORRECT | Averaging over permutations of the repeated block removes its cross covariance with the one-dimensional complement. |
| H5(b): circle scan and star singleton interval | NOT A PROOF | A grid is evidence only; the reported full circle scan was not rerun. |
| H5(b): edge interval [0,0.18] at n=5 | WRONG | Exact admissible interval is [0,1) for normalized nonzero states, or [0,1] for homogeneous inequalities. |
| H5(c): summing (*) gives M | CORRECT | Weighted pair sums give the stated quadratic form. |
| H5(c): one y with y^t M y>=0 certifies the graph | GAP | The argument needs A_x y nonzero; zero projected vectors give a vacuous zero inequality. |
| H5(c): M vanishes on the star/edge complement | CORRECT | Every nonzero projected image lies in the appropriate extremal star/edge eigenspace. |
| H5(c): spectral experiments | NOT A PROOF | The note correctly calls these searches; their original data are absent. |
| H5(d): covariance N/tau and Gval expansion | CORRECT | The covariance requires tau>0; the expansion equals tr(MN). |
| H5(d): Gval>=0 implies F through this state | GAP | A positive projected trace is required; N=0 and other zero-image cases need separate handling or a global continuity argument. |
| H5(d): star equality of the two expanded sides | CORRECT | Both equal n(n-1)(n-2)(n-3). |
| H5(d): negative Gval at n=4 | NOT A PROOF | Reported numerically; independently verified below by an exact rational example. |
| H5(d): nonnegative searches at n>=5 and proposed proof route | NOT A PROOF | Correctly left open; the proposed state inequality is stronger than the requested graph conclusion. |
| H6: five pairs remaining at n=5 | CORRECT | Direct enumeration after removing hook, sign and standard cases gives precisely the listed pairs. |
| H6: search minima | NOT A PROOF | Original search files are not in this folder. |
| Lemma U | CORRECT | Restriction to the Young subgroup gives tensor sums and hence the stated minimum. |
| H7: connected heavy-component/Pieri limit | CORRECT | Only its trivial representation survives; empty survivor sets mean +infinity. |
| H7: n=6, n=7, n=8 pair (4211,422) constructions | CORRECT | Their only four-box survivors are 211 and 22, respectively. |
| H7: other n=8 pairs under 'The same holds' | GAP | Different constructions are needed; a connected heavy graph on the other four vertices leaves no finite blocks. |
| H7: interpreting all listed pairs as having star ratio 1 | WRONG | Their exact ordinary-star minima include 5/6, 8/9, 6/9 and 7/9; only the two specified width-three/four pairs have ratio 1. |
| H7: search minima and counts | NOT A PROOF | The quoted output files are absent; valid examples explain the stated 2/3 values but do not prove lower bounds. |
| G: setting and converse construction | CORRECT | The entrywise condition makes lam Pi-N a nonnegative graph Laplacian and Nx=0 attains its top eigenvalue. |
| G: affine Gval identity and auxiliary pair identity | CORRECT | Substitution and N1=Nx=0 give the displayed expressions. |
| G: consequence 1, a>=0 | CORRECT | It is a positive multiple of a sum of squared projected norms. |
| G: consequence 2, complete-graph addition and boundary reduction | CORRECT | For fixed N,x the slope in lam is nonnegative; this reduces the sufficient Gval inequality. |
| G: leading-terms inequality | CORRECT | Both tr N^2 and tau^2/(n-2) are at most lam tau. |
| G: leading-term equality 'needs every g_k=lam' | WRONG | All gaps zero also give equality, for every equally weighted complete graph. |
| G: unit-star checks | CORRECT | Substitution gives the printed t, a lam and b. |
| G: two-eigenvalue Laplacian and nonnegativity bound | CORRECT | For g>=0 the weights are nonnegative exactly when lam>=g(1+nm); g=0 and lam=g are degenerate cases. |
| G: 'one other nonzero eigenvalue' including a single edge | WRONG | For a single edge lam-g=0; the intended formula is correct with 'nonzero' removed. |
| G: Gval=2g^2 Psi and intermediate identities | CORRECT | Direct matrices and the N expansion agree; the Q identities reduce to the stated moment expressions. |
| G: edge, star, padded-star and n=4 special values | CORRECT | Substitution gives the formulas, including the extra balanced n=4 zero. |
| G: numerical minimum of Psi | NOT A PROOF | Independent many-start minima agree; both edge and star are exact zeros. |
| G: Psi>=0 proves F 'on this family' | CORRECT | It covers the boundary graph and its complete-graph additions, not arbitrary graphs or every graph with two spectral levels. |
| G: first one-positive lower bound | CORRECT | The moment bounds have the required coefficient signs; symbolic substitution gives exactly the stated expression. |
| G: two open problems and n=4 warning | NOT A PROOF | Correctly labelled open; the n=4 warning is independently certified. |
| G: split of Psi | CORRECT | Exact expansion has zero residual. |
| G: signs of K,D and classification D=0 | CORRECT | K has the stated lower bound and D is a Cauchy-Schwarz defect. |
| G: easy region and two-valued classification | CORRECT | A non-star two-valued vector has both sign multiplicities at least two and m>=1/n. |
| G: explanation of loss in the one-positive bound | CORRECT | The replacements can be simultaneously tight only at the star; the stated interval of negativity follows. |
| G: subset-mean candidate and numerical remedy | NOT A PROOF | In fact max_A mu_A=m because two-element sets are allowed; this restates the original problem. |
| G: m>=M, equality conditions and denominator | CORRECT | Sum m>=x_i x_j with nonnegative factors (S-x_i)(S-x_j); the denominator is at least n-2. |
| G: n*den*Psi>=Phi' | CORRECT | The difference is exactly n(n-1)K*den*(m-M). |
| G: local minima of Phi' and proposed sufficiency | NOT A PROOF | The implication is exact, but Phi'>=0 is still unproved; independent local checks agree. |
| G: Hessian, determinant and strict concavity | CORRECT | The printed Hessian is negative definite in the stated range. |
| G: reduction to S, possibly -S, and at most three interior values | CORRECT | A supporting linear moment functional gives one cubic by constrained stationarity; singular constraints already have fewer values. |
| G: scan 1, probability relaxation fails | NOT A PROOF | Independently reproduced; it refutes the relaxation, not the genuine-vector inequality. |
| G: scan 2, integer three-valued grid | NOT A PROOF | Independently reproduced; a finite grid does not cover its intervening parameters. |
| G: 'both exact evaluations on a grid' | GAP | Exact arithmetic or interval certificates are not supplied; the independent calculations below use floating point. |
| G: final statement of what is proved and what remains | CORRECT | The comparison and value reduction hold; Phi'>=0 and the general Gval inequality remain open. |

## Errors and repairs

### Covariance states, their kernel, and theta

Write A_x y=P((xy^t+yx^t)/sqrt(2)), using the Frobenius inner product. For a PSD covariance C of trace one, put

    Z = tr(A_x C A_x^*) = 1 - (2n/(n-2)) kappa.
    rho = A_x C A_x^* / Z, provided Z>0.

This is equivalent to weighting normalized images by their squared norms. Normalizing every image first and then using the original uniform measure generally gives a different state. The formulas N,A_ij and (*) concern the homogeneous construction above. In particular (*) equals (n-1)Z times the normalized dual slack.

H lines 98–99 say: 'as it must: the vectors P(x.y) span V_22, so this is Theorem 3 again'. Take

    n=4, x=(1,-1,0,0)/sqrt(2), y=(1,1,-1,-1)/2.

Then y lies in {1,x}^perp but A_x y=0. A second independent direction has nonzero image, so rank A_x=1, not 2. The unrestricted existence theorem does not imply feasibility in a prescribed proper image.

The omission in R is repairable. A_x is injective at a star vector, so its Gram determinant is not identically zero. It is injective for a dense set of x. For such x every C of trace one has Z>0. Under R's hypothesis, construct the normalized states there and pass to a density-matrix subsequential limit at exceptional x. This proves the global reduction, although the printed pointwise state argument omits these steps. An analogous limit argument applies if a sufficient Gval inequality is proved for all graphs. A pointwise zero image alone does not certify an individual graph.

H lines 124–125 say the admissible theta interval 'is [0, 0.18] at the edge vector for n = 5'. This is false. At that vector take

    v=(3,3,-2,-2,-2)/sqrt(30), C(theta)=theta vv^t+(1-theta)Pi_B/2.

Here A_x v=0. Exact substitution in (*) gives

| Pair type | (*) |
|---|---|
| 12 | 0 |
| 1k or 2k, k>=3 | (3/2)(1-theta) |
| kl, k,l>=3 | 5(1-theta) |

Thus all theta in [0,1] pass the homogeneous inequalities. The endpoint theta=1 gives Z=0; all theta in [0,1) give the same valid normalized image state. These exact calculations are produced by `python3 referee.py exact`, with the full executable path given below.

### Leading-term equality

G line 45 says: 'Equality needs every g_k = lam, a single edge.' For lam>0 the actual equality alternatives are

    all g_k=0, or all n-2 gaps equal lam.

The first is an equally weighted complete graph. The second is a single edge: L=lam xx^t, and nonnegative weights forbid two positive or two negative nonzero coordinates of x. The zero graph is another degenerate equality case. The later phrase about 'both equality cases' is harmless if it means the two listed examples; it must not be read as an exhaustive classification of Gval zeros.

### Disjoint unions at n=8

A horizontal strip of size four needs four distinct columns. None can be removed from a width-two diagram. Thus a four-vertex star plus a connected heavy graph on the other four vertices cannot give finite 211/22 bottoms for the three width-two pairs in H lines 175–176. This is a missing distinction between the constructions, not evidence against the numerical ratio 2/3.

The accounts can be completed as follows. The arrow records the survivors after one heavy edge is removed by Pieri.

| Pair | Correct graph construction |
|---|---|
| (2211,222), n=6 | Four-vertex star plus one sufficiently heavy edge. |
| (3211,322), n=7 | Four-vertex star plus a connected heavy three-vertex graph. |
| (4211,422), n=8 | Four-vertex star plus a connected heavy four-vertex graph. |
| (22211,2222), n=8 | Four-vertex star plus two separate heavy edges: (22211,2222)->(2211,222)->(211,22). |
| (221111,2222), n=8 | Six-vertex star plus one heavy edge: (221111,2222)->(21111,222), with star bottoms 4 and 6. |
| (2111111,2222), n=8 | The ordinary eight-vertex star itself, with bottoms 6 and 9, as also stated in Theorem 4.5 of the supplied Alon text. |

Only (3211,322) and (4211,422) in this list have ordinary-star ratio 1. For example a four-vertex star plus h K_4 has, for (2111111,2222), bottoms 8h+6 and 6h+3 for large h; its ratio tends to 4/3, not 2/3. The branching and ordinary-star numbers are independently enumerated by `referee.py model`.

## The Gval algebra and its precise graph consequence

For the auxiliary pair identity, summing d_ij^2(N_ii+N_jj) over unordered pairs gives nt+tau. The remaining term -2 sum d_ij^2 N_ij vanishes by N1=Nx=0. Substituting L=lam Pi-N in tr(MN) then yields the printed affine expression. The slope a is nonnegative because

    tau - (2n/(n-2))t = sum_k g_k ||A_x y_k||_F^2.

For N=gQ the projected trace before dividing by tau is gK/(n-2). This is strictly positive for n>=5 and g>0. The identities for Q give exactly the printed Psi. Hence if Psi(x)>=0 for every unit sum-zero x, then F holds for every nonnegative graph of the form

    w_ij=(lam-g)/n-g x_i x_j,
    L=lam xx^t+(lam-g)Q,
    g>0, lam>=g(1+nm).

At lam=g(1+nm) these weights are g(m-x_i x_j). Larger lam adds a nonnegative multiple of K_n, and a>=0 preserves Gval>=0. The degenerate g=0 case is an equally weighted complete graph and satisfies F directly. This is the precise content of 'on this family' in G line 73, which is correctly qualified. It does not cover all graphs, nor graphs whose top Laplacian eigenvalue has arbitrary multiplicity.

For the power-sum bound, with den=n(n-1)S^2-1,

    n den Psi-Phi' = n(n-1)K den (m-M).

This is an exact identity. The concavity calculation is also correct. At fixed S a supporting nonzero linear form in the two moments gives an objective a sum y_i^3+b sum y_i^4. Its interior stationary coordinates satisfy one cubic. If constraint gradients are dependent, the interior coordinates already take just one value. Repeated endpoint values ±S have integer multiplicities. The reduction leaves continuous parameters among at most three interior values; it is not a finite list of vectors or an argument establishing Phi'>=0 between grid points.

The subset remedy does not change the problem: max over all sets A of size at least two of mu_A is exactly m. A mean cannot exceed the largest product it averages, and the maximizing pair is itself an allowed set A.

## Independent computations and commands

All commands were run in this folder with

    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3

The shell inherited nice=10. `referee.py` sets BLAS/Accelerate/OpenMP thread variables to one before imports and sets a 240-second alarm. NumPy, SciPy, mpmath and SymPy are installed; only these numerical packages were used. Peak resident memory was below 117 MB and the longest run, including superseded solver trials, took about 31 seconds. No process remained running at completion. Each completed block appends its command, result and resource figures to LOG.md. The final implementations and raw outputs are retained here.

### 6(a): Young orthogonal modules, written from scratch

Command:

    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py specht > specht_checked.out

Seed 20261111; 160 independent W=1 exponential-weight graphs at each n. All partitions were built, not just hooks, and the full spectra were compared. Dimensions range up to 16. Coxeter involution, braid and commuting relations were checked before using the matrices.

| n | Max Coxeter residual | Max hook-spectrum error | Max full conjugation-spectrum error | Min (hook ratio-k/j) |
|---|---:|---:|---:|---:|
| 5 | 1.1102230246251565e-16 | 2.220446049250313e-15 | 2.1094237467877974e-15 | 0.0504744848153269 |
| 6 | 1.1102230246251565e-16 | 2.4424906541753444e-15 | 2.4424906541753444e-15 | 0.0017534470869429164 |

The separate edge-permutation model uses the kernel of the vertex-edge incidence matrix, without using the Specht construction:

    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py model > model_checked.out

On 80 graphs at each n=5,6, its maximum spectrum errors against [n-2,2] were respectively 1.7763568394002505e-15 and 1.4432899320127035e-15. Projection-constraint errors were at most 1.4e-15; norm-identity errors were at most 7.2e-15. The output also records every four-box survivor and ordinary-star minimum used above.

### 6(b), 6(d): Psi, split, covariance algebra, m and Phi'

Command:

    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py algebra > algebra_checked.out

The first invocation prepended `nice -n 10`; the sandbox refused a further priority change, but the process ran at the inherited nice=10. The final run and reproduction use only the command above. Seed 20261111; 300 random unit sum-zero vectors at each n, independent random g in [.1,2], and separate random W=1 graphs for the general N identities.

| n | Max abs(Gval-2g^2 Psi) | Max split residual | Min(m-M) | Min(n den Psi-Phi') |
|---|---:|---:|---:|---:|
| 4 | 9.769962616701378e-15 | 2.220446049250313e-16 | 0.011408343995856773 | 0.007425987197142554 |
| 5 | 2.4868995751603507e-14 | 1.3322676295501878e-15 | 0.01360651560029856 | 20.839849623544257 |
| 6 | 5.684341886080802e-14 | 3.552713678800501e-15 | 0.028893558841178134 | 98.06059873376786 |
| 7 | 1.1368683772161603e-13 | 7.105427357601002e-15 | 0.03564875683315622 | 542.8398143023923 |
| 8 | 2.2737367544323206e-13 | 1.4210854715202004e-14 | 0.05989971804725272 | 2057.4957820170994 |
| 9 | 3.410605131648481e-13 | 1.4210854715202004e-14 | 0.050893947184497496 | 4034.3753242922776 |

These are absolute errors; Gval scales with g^2 and grows with n. The general affine identity had maximum error below 9.8e-15, the expanded H5(d) formula below 1.8e-14, and (*) below 1.8e-14. The intermediate Q identities had residuals below 8.4e-16. All sampled a were positive. The comparisons include exact equality at star/edge in addition to these generic random tests; their floating-point errors are recorded in the SPECIAL rows of algebra_checked.out. The Phi' comparison was also checked at n=4, where K>=0 still makes it valid.

The same command gives the total-weight-one path slacks, in H's N,A convention:

| n | Weighted slack | Exact value |
|---|---:|---:|
| 4 | -0.055555555555555414 | -1/18 |
| 5 | -0.08333333333333304 | -1/12 |
| 6 | -0.09999999999999909 | -1/10 |

The original expression 'two unit edges ... total weight 1' needs its implicit rescaling: the computation uses two weights 1/2.

### 6(c): minimise Psi from many starts

Command:

    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py optimize --starts 200 > optimize_scaled.out

This uses a smooth epigraph variable bounding every x_i x_j, analytic Jacobians, sum-zero and unit-norm constraints, bounded coordinates, and objective scaling by n^3. It uses the same seed as above, with star/edge starts, perturbed star/edge starts and random starts. All 200 solves reported success for every n. The listed objective is recomputed using the actual largest coordinate product after centering and normalizing the result.

| n | Smallest computed Psi | Location of this run's smallest value |
|---|---:|---|
| 5 | -1.1102230246251565e-15 | (4,-1,-1,-1,-1)/sqrt(20) |
| 6 | -2.220446049250313e-15 | (5,-1,-1,-1,-1,-1)/sqrt(30) |
| 7 | -4.440892098500626e-16 | (6,-1,-1,-1,-1,-1,-1)/sqrt(42) |
| 8 | 8.881784197001252e-16 | (1,-1,0,0,0,0,0,0)/sqrt(2) |

The exact values at both the star and the edge are zero for every n, including n=8. Permutations and overall sign changes preserve Psi. The numerical evidence therefore agrees with minimum zero and these two classes of minimizers. It neither proves global nonnegativity nor excludes further minimizers. Individual final vectors and solve results are saved in optimize_n5.json through optimize_n8.json. Earlier nonsmooth and unscaled attempts are retained but superseded because some solves failed.

A supplementary check of the note's Phi' local-minimum claim used:

    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py phiopt > phiopt.out

For 80 starts per n=5,6,7,8, the smallest values were respectively -2.1316282072803006e-14, -1.406874616804999e-13, -1.7053025658242404e-13, -4.547473508864641e-13, at star/edge vectors within rounding. Solver success counts were 75,79,73,72; failed solves are not certificates. This agrees with, but does not prove, the claimed nonnegativity.

### Exact identities, failures, and scans

Commands:

    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py exact > exact.out
    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py targeted > targeted.out
    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py n4search > n4search.out
    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py certificate > certificate_checked.out
    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py scans > scans.out

`exact` symbolically gives zero residual for the split and the Phi' comparison, and the Hessian and determinant printed in G. It also gives the zero projected matrix and the exact theta slacks above. `certificate` gives zero residual for the one-positive lower-bound substitution.

`targeted` normalizes the rounded intermediate vector supplied in H and finds slack -0.14025117089308015 on pair 14. It also checks the expanded unit-star sides for n=4..9, giving the integers 24,120,360,840,1680,3024 within rounding. A direct graph-weight search in that mode missed the negative n=4 gap example; `n4search` uses an independent orthonormal-frame parameterisation of N and finds Gval/W^2=-0.014715702538821294. Both searches, including the miss, are retained in the log.

An exact rational example from `certificate` removes dependence on a nearly repeated eigenvalue. In edge order 12,13,14,23,24,34 its weights are

    (9/83, 899917/1660000, 0, 9/83, 44/83, 0).

Its Laplacian eigenvalues are

    0, 16/83, 989917/830000, 99/83,

and its simple top eigenvector is (1,-10,1,8)/sqrt(166). Exact matrix multiplication gives

    Gval = -1390241124027/57178700000000
         = -0.024313968733584358,
    Gval/W^2 = -5560964496108/380077315651787
             = -0.014631140210437482.

This refutes the sufficient state inequality at n=4, as the note reports. It does not refute F. The earlier failed coarse rational approximation is retained in certificate.out and is not used as a counterexample.

For the integer scan, the other coordinates are derived from their required mean and variance for every multiplicity k and both signs. On 2001 equally spaced S^2 values in [1/n,(n-1)/n], the minima were:

| n | Minimum Phi' on grid |
|---|---:|
| 5 | -2.3314683517128287e-14 |
| 6 | -4.476419235288631e-14 |
| 7 | -5.684341886080802e-14 |
| 8 | 1.2180732613030286e-13 |
| 9 | 1.6786572132332377e-13 |
| 10 | 4.547473508864641e-13 |
| 11 | -1.4772183476452481e-12 |
| 12 | -9.094947017729282e-13 |

Only S^2=1/2 and (n-1)/n were numerical zeros. These reproduce scan 2's evidence. The inequalities remain unchecked between grid points.

For scan 1 the independent probability-measure parameterisation gives:

| n | Two interior atoms: min Phi' | Endpoint/interior family: min Phi' |
|---|---:|---:|
| 5 | -2.7913027859764767 | -2.778817507002067 |
| 16 | -2267.680214238837 | -2230.57106684927 |

For example the first n=5 value has S^2=.4405, interior atoms .05978806542705967 and -.6636526412636804, with probabilities .688 and .312. Both atoms satisfy the bound by S. The probability is not an empirical multiplicity divided by four. The n=16 two-atom value occurs at S^2=.4075 and probability .904. Different grid choices explain the modest difference from the note's quoted minima. Negative feasible relaxed values confirm that this relaxation cannot prove Phi'>=0.

## Labels needing correction and limits of the check

The conjectures F, Psi>=0, Phi'>=0 and general Gval>=0 are appropriately left unproved. The note does not falsely announce a proof of Alon's conjecture. The following asserted conclusions or justifications need correction:

1. The universal V_22 spanning assertion is false.
2. The edge theta interval is a false numerical conclusion; its correct interval follows exactly above.
3. The leading-term equality statement omits complete graphs.
4. The covariance reductions need normalized positive-trace states and treatment of exceptional kernels. R's global conclusion can be repaired by continuity.
5. The n=8 account needs the different graph constructions given above; its connected heavy-block explanation cannot be reused unchanged.
6. 'Nonzero' must be dropped for the lower eigenvalue in the single-edge degeneration.
7. The 'exact' label for the grids needs an arithmetic certificate or should be changed to 'numerical grid evaluations'.

I could not authenticate the original search outputs, seeds, minimization traces or source-code checks named in the notes: none of those files is supplied here. In particular I did not rerun the full circle scans, omega trials, SDP covariance searches, all pair-ratio searches, or the unbounded relaxed arc mentioned at G line 169. I checked the displayed mathematical reductions and supplied independent reproductions of the requested module, scalar, minimization, bound and boundary-grid tests. Numerical minima are not certified global minima. No counterexample to F or to Conjecture 1.5 was found, and no assertion for all n>=5 has been established by computation.

Overall verdict on the PROVED parts: **WRONG**.

Task: 'You are refereeing a mathematical working note' — 11 Nov 2026; the request's exact clock time was not exposed (first local check: 08:00:36 +04).
