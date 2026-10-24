# Research worklog: unrestricted FEI continuation

20 September 2026. This is a scientific record of proved statements, tested proposals, and concrete failed routes, not a claim of a full proof. Full FEI was the target. No independent auditor or delegated agent was used.

## What actually advanced

The all-dimensional one-step derivative bound D_cross<=6M was sharpened to

    D_cross <= 2 lambda_* M < 5.394754 M,
    5.3947539099 < 2 lambda_* < 5.3947539100.

The scalar maximizer is proved unique, and its location and coefficient are certified by rational logarithm intervals, not by taking the largest value on a finite grid. The sharp universal Boolean one-step coefficient is consequently bracketed between 4 and 5.394754. The upper endpoint is not asserted optimal for Boolean spectra, and neither endpoint is being presented as a proved upper FEI constant for H/I.

The complete proof and a reconstruction of its inherited uncertainty input are in REPORT.md. The inherited nonsummability counterexample is preserved; changing 6 to 5.395 does not fix it.

## Attempt 1: sharpen the full-domain derivative inequality to four

The candidate was

    D_cross(f) <= 4 M(f) for every Boolean f.

`explore_derivative.py` exhausts truth tables modulo global negation through dimension four (32,906 representatives) and samples 150 tables per dimension from five through nine, with several negative densities. It computes M by greedy minimum-weight basis selection from the exact integer directional costs. Its entropy calculations use floating-point logarithms. The actual output is `derivative_exploration.txt`.

Every tested case had D/M<=4, up to the exploratory numerical arithmetic; the two-variable quadratic phase attains four. The separate exact checker confirms the candidate on 342 explicitly specified cases. No all-dimensional proof of the coefficient four was obtained. The finite maximum is not an optimality certificate outside its tested scope.

Optimizing the already-proved scalar route, rather than replacing it by this unproved numerical candidate, produced the rigorous upper coefficient in Theorem 1. The loss between four and 5.394754 is not proved necessary for Boolean spectra.

## Attempt 2: relax the two-copy argument to arbitrary real amplitudes

`explore_real.py` initially tested a real-amplitude relaxation, using NumPy and SciPy to search on the unit sphere. It found a one-coordinate violation of the coefficient four, recorded in `real_exploration.txt`. That floating-point witness was then replaced by the exact choice

    a_0=sqrt(119/120), a_1=sqrt(1/120).

The normalized two-copy output construction has a nonuniform shift marginal. With q=1/120 and t=4q(1-q), its corrected conditional-entropy deficit is

    D_real = 2 h_2(q) - (1+t)/2 * h_2(t/(1+t)).

The exact checker proves D_real-4q>48014467/250000000000. The inverse Walsh transform is not Boolean. This rules out the real-amplitude relaxation of the candidate; it does not refute the Boolean candidate or FEI. The per-shift normalization supplied by f^2=1 is essential.

No claim is made about the best constant for arbitrary real amplitudes. The optimizer stopped after this counterexample and did not complete all the dimensions specified in the loop.

## Attempt 3: exploit the full signed truth-table geometry

`explore_truth_entropy.py` computes the truth-table Fourier expansion of H in dimensions one through four. It found the alternating order signs and the positive order-six coefficient. A subsequent repository search recovered the identical coefficient formula in the September 16 report, credited there to the September 13 R32 archive. Accordingly this report explicitly labels the formula as inherited and does not count rediscovery as a new theorem.

The continuation reconstructs the formula in bits, derives the translation-orbit square representation for D_cross, and checks both identities exactly. The actual floating-point discovery output is `truth_entropy_exploration.json`; the exact comparisons are in `verification.json`.

Two consequences were made explicit for the attempted full proof:

1. On nondegenerate quadratic phases, the positive fourth-order contribution to D/M is at least (2^n-1)/(12 ln(2) n), whereas the complete signed ratio is exactly four. Thus even a single low-order positive contribution is not payable by a dimension-free influence budget. Negative higher-order credits must remain in the argument.
2. The exact positive sixth-order coefficient at {0,1,2,4,8,15} proves that H(fg) is not a conditionally negative definite kernel on Boolean truth tables. Therefore the proposed direct Hilbert-distance/negative-type proof does not work.

These are consequences of a known-in-the-repository signed expansion; no exhaustive priority review was performed. They do not establish a universal bound on the signed accumulated allocation.

## Additional exact obstruction to incomplete Boolean constraints

An attempted relaxation that retains only some of the convolution equations cannot suffice by itself. This follows without numerical testing.

Fix a nonzero omitted direction v. Let the only nonzero real Fourier amplitudes be

    a_0=sqrt(1-q), a_v=sqrt(q), 0<q<1.

Then

    sum_s a_s a_(s+u) = 1                 for u=0,
                       2 sqrt(q(1-q))    for u=v,
                       0                 for every other u.

Thus every Boolean convolution constraint except the one at v holds exactly. Nevertheless H=h_2(q), I=|v|q, and H/I tends to infinity as q tends to zero. The inverse transform is not Boolean. Even omitting a single nonzero constraint admits this obstruction. This rules out proving FEI for the full relaxed class using only that proper subset of equations; it does not exclude arguments that use additional inequalities valid only for Boolean functions.

The report does not claim priority for this elementary two-coefficient observation, and it does not count it as a Boolean counterexample.

## Other attempted closures and their precise status

The uncertainty reduction gives a bound on one step, while its iteration requires a summable resource. The existing one-point-defect calculation disproves a uniform bound on the discounted sum of M. It also prevents presenting the improved constant as the missing full proof.

A uniform fixed-coefficient affine-drift payment was not reinstated: the current entrypoint explicitly records its failure on the recovered majority family. A possible future adaptive, nonuniform-shift or high-entropy-excess argument would require a new proved selection/stability theorem. No such theorem was obtained in this continuation, and merely stating it would be a reformulation rather than progress.

The old weighted-erasure quantity and signed allocation quantity remain valid full-scope targets. The coefficient-four derivative proposal is a useful auxiliary question, but solving it alone would still leave the full accumulation problem unresolved.

## Actual execution and reproducibility

The exact checker ran successfully, including a complete replay after simplifying the JSON to shorter outward-rounded rational lower bounds. No floating-point tolerances were introduced into it. It checks 342 Boolean functions, exact entropy/translated-square identities, the certified scalar optimum, a positive sixth-order coefficient, the explicit quadratic fourth-order counts in dimensions 2,4,6,8, and the rational real-relaxation counterexample.

The exploratory code and raw outputs are archived separately. They require NumPy; `explore_real.py` also requires SciPy. They do not constitute proof or independent review. No massive truth-table enumeration in dimensions 6 or 8 was used to establish the quartic asymptotic: that result is analytical, with finite coefficient sums serving only as checks.

No schedule, ownership, native finite-dimension atlas metric, email delivery, Google Drive delivery, permission, repository visibility, or workflow was changed. GitHub delivery and actual future worker uptake are distinct.
