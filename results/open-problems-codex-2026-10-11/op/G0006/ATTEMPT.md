# G0006 — attempt and referee record

Date: 2026-10-11. Verdict: PARTIAL; the requested strict inequality is not proved.

## 1. Exact target and conventions

For every integer d >= 2, consider the nearest-neighbor contact process on Z^d. Recovery rate is 1 and infection rate is lambda PER EDGE. Write k = 2d, lambda_c = lambda_1, and nu_lambda for the upper invariant measure. The target is lambda_c(d) < lambda_p(d), where lambda_p is the supremum of rates for which a sample from nu_lambda has no infinite nearest-neighbor infected component. This is a statement about every d, not merely large d. Source: Fernley--Jacob, arXiv:2609.09972, PDF pp. 1--3. The tree theorem is not an answer to this problem.

In the graphical construction, let X_lambda consist of vertices v whose singleton infection survives forever, all evaluated in the SAME future graphical environment. Then X_lambda has law nu_lambda. To justify the joint law, for every finite A, additivity says the process started from A is the union of its singleton processes. It dies out iff all these finitely many singleton processes die out (their extinction times have a finite maximum). By contact-process duality this extinction probability equals nu_lambda(all vertices in A are healthy). These finite void probabilities determine the law by inclusion-exclusion. Thus simultaneous singleton survival may be used below without claiming the singleton processes independent.

## 2. A rigorous product upper comparison and a lower bound

Proposition 1. On any graph of constant finite degree k,

    nu_lambda <=st Ber(p)^{tensor V},    p = k*lambda/(1 + k*lambda).

Proof. For each v let T_v be the first recovery mark at v after time 0, and let S_v be the first outgoing arrow from v after time 0. If S_v >= T_v, a process begun with only v infected dies before giving birth; hence v not in X_lambda. Define B_v = 1{S_v < T_v}. The recovery process at v and the k outgoing arrow processes have disjoint labels from the processes used for B_w when w != v. In particular the two oppositely directed arrows on an undirected edge are independent processes. Consequently (B_v) are iid. Competing exponentials of rates 1 and k*lambda give P(B_v=1)=p. The graphical coupling has X_lambda subset {v:B_v=1}, establishing the stochastic upper bound. QED.

Corollary 1. If p_c = p_c^site(Z^d), then

    lambda_p(d) >= p_c / [2d*(1-p_c)].

Proof. For each lambda strictly below the displayed bound, p < p_c. Independent p-site percolation has no infinite component by the definition of p_c, and neither does its coupled subset X_lambda. Taking the supremum of these rates yields the bound. No assertion about behavior at equality is needed. QED.

This is an elementary bound, not a claimed new theorem, and it has not been shown to exceed lambda_c in any dimension. It does NOT settle the strict inequality. Product domination from below by a parameter less than p_c proves nothing about nonpercolation.

## 3. Stationary pair identity and why its apparent shortcut fails

Proposition 2. For lambda > lambda_c, let rho = nu_lambda(eta(0)=1)>0, and D_0 = sum_{y~0} eta(y). Then

    E_nu[D_0 | eta(0)=1] = k - 1/lambda.

Proof. For f(eta)=eta(0), its bounded local generator is

    Lf = -eta(0) + lambda*(1-eta(0))*sum_{y~0}eta(y).

Stationarity implies E[Lf]=0 (the local martingale identity is integrable since |Lf| <= 1+k*lambda). Translation invariance gives E sum eta(y)=k*rho. Put a=E[eta(0)*D_0]. The identity is 0=-rho+lambda*(k*rho-a), so a=(k-1/lambda)*rho. Divide by rho. QED.

In particular, this is an exact lattice identity, not an independence approximation. It does NOT imply nonpercolation whenever k-1/lambda<2. Finite occupied components can dilute the occupied-site mean degree while an infinite component remains.

Proposition 3 (explicit obstruction, not a contact-process counterexample). On Z^2 there exist translation-invariant, translation-ergodic, positively associated percolating laws with arbitrarily small density and occupied-site mean degree strictly below 2.

Proof. Let (B_j)_{j in Z} be iid Bernoulli(p) and (C_{i,j})_{(i,j) in Z^2} independent iid Bernoulli(q), independent of the B's, where p=q^2 and 0<q<1. Define

    eta(i,j) = B_j OR C_{i,j}.

Every row with B_j=1 is completely occupied. Almost surely there is at least one such row: the probability that B_j=0 for |j|<=N is (1-p)^(2N+1), tending to zero. Hence eta percolates a.s. Its density is r=p+(1-p)q=q+q^2-q^3, tending to zero as q decreases to zero.

Its distribution is translation invariant. To see ergodicity without assuming it, package each row as the random element (B_j,(C_{i,j})_{i in Z}); these random elements are iid over j. Events depending on finitely many rows are independent of their sufficiently distant vertical translates. General events can be approximated in probability by events in finitely many rows, so this vertical shift is mixing and therefore ergodic: for an invariant event A, mixing gives P(A)=lim P(A intersect shift^n A)=P(A)^2. Any event invariant under all lattice translations is vertically invariant, so has probability 0 or 1. The factor eta inherits this property.

Positive association follows because eta is a coordinatewise increasing function of independent Bernoulli variables. For completeness, association of a finite product follows by induction on the number of inputs: covariance decomposes into the mean of the conditional covariances plus the covariance of the two conditional means; the first term is nonnegative by induction and the second by the one-variable inequality for increasing functions. Cylinder observables suffice and bounded increasing observables follow by approximation.

For a horizontal neighbor the joint occupied probability is h=p+(1-p)q^2. For a vertical neighbor the two row inputs are independent, so the joint occupied probability is r^2. Thus

    E[D_0 | eta(0)=1] = (2*h+2*r^2)/r = 2*h/r + 2*r.

When p=q^2, h=2q^2-q^4. This conditional mean tends to zero with q. At q=1/10, p=1/100, we have r=109/1000, h=199/10000, and 2*h/r+2*r<2. These exact rational statements are separately kernel-checked in CertificateChecks.lean; lean_check.txt reports exit 0. QED.

This law is NOT invariant for contact-process dynamics and is NOT a counterexample to the target. It specifically refutes arguments using only translation invariance, ergodicity, association, small density, or the unconditional occupied-site mean-degree test. It also is not asserted to have the contact process's conditional finite-energy properties.

## 4. Finite local exit events give a valid criterion

For integer R>=0 let Q_R(v)={x: ||x-v||_infinity<=R}. Run the graphical contact process from {v}, using infections inside this finite box and arrows leaving it. Let E_v(R) be the event that it makes an infection path out of the box before becoming empty, and let

    q_R(lambda)=P(E_0(R)).

Only recovery processes at source vertices in Q_R(v) and outgoing arrow processes whose source lies in Q_R(v) are used. No recovery process outside the box is needed to determine the first exit. Thus disjoint source boxes give independent E events, even if some outgoing arrows have heads in the other box; the directed source labels are different.

Lemma 4. A finite-box contact process without exits dies out almost surely, uniformly over its initial state.

Proof. In any unit time interval require no outgoing arrows from any of the finitely many vertices and at least one recovery at every vertex. The probability is a positive constant c, independent of the initial infection state. On this event the infection is empty at the end. Independent graphical time intervals give P(not extinct by time n) <= (1-c)^n. QED.

Thus v in X_lambda implies E_v(R) almost surely: a process surviving without ever leaving the box contradicts Lemma 4. This implication holds simultaneously for the countably many v and R after discarding a null event.

Proposition 4 (conditional nonpercolation criterion). Let m=(2R+1)^d. If

    (2d-1)*q_R(lambda)^(1/m) < 1,

then nu_lambda does not percolate.

Proof. Color lattice vertices by the d coordinate residues modulo 2R+1, using m colors (for R=0 there is one color). Distinct centers with the same color have disjoint Q_R boxes. Along a self-avoiding path of n EDGES, at least (n+1)/m of its vertices have some common color. If all its vertices belong to X_lambda, all their E events occur. Restrict to that color class; independence implies a probability at most q_R^ceil((n+1)/m), and thus at most q_R^((n+1)/m). The color selected can depend on the deterministic path, not on the random environment, so no random selection assumption is used.

There are at most k*(k-1)^(n-1) self-avoiding n-edge paths from a specified root: k choices for the first step and at most k-1 afterward, since immediate backtracking is prohibited. The union bound yields

    P(root connected through X_lambda by an n-edge self-avoiding path)
        <= k*(k-1)^(n-1)*q_R^((n+1)/m).

Under the displayed condition the right side tends to zero. An infinite component in a locally finite graph contains arbitrarily long self-avoiding paths from each of its vertices (otherwise it lies in a finite-radius ball); hence the root has zero probability of an infinite component. The lattice is countable, so the probability of any infinite component is zero. QED.

For fixed R this q_R is a finite-state absorbing Markov-chain hitting probability, continuous in lambda>=0. One direct justification is to write the linear system for absorption in the nonempty box states. The finite-box recovery event used in Lemma 4 ensures absorption, uniformly when lambda ranges over a compact set; so the transient generator is invertible and its inverse is continuous. Alternatively finite-time continuity plus this uniform geometric tail proves the same assertion.

If the criterion were strict at lambda_c, continuity would yield a rate lambda_c+epsilon satisfying it, which would solve the target for that dimension. The following proposition shows why this particular crude criterion cannot achieve that.

## 5. A proved barrier: the criterion fails throughout the survival regime

Proposition 5. For every d>=2, every R>=0, and every lambda>=1/(2d),

    q_R(lambda) >= (2d-1)^(-(2R+1)^d).

Consequently Proposition 4's strict criterion can never apply there, and in particular cannot prove a gap above lambda_c.

Proof for R>=1. Put k=2d. Follow the prescribed directed path

    0, e_1, 2e_1, ..., (R+1)e_1,

the last site being outside Q_R(0). Track one infection along this path; at each stage suppress all births except to the next vertex and discard the old infection after its successful birth. This artificial process only removes possible infection paths from the graphical construction. At each handoff the current infection's next designated arrow has rate lambda and its recovery has rate 1. Independent increments and the memoryless property give success probability lambda/(1+lambda) at every step. The path visits distinct vertices, and its arrival time at a new source is measurable with respect to previously used sources, so these future clocks are also independent of the previously exposed clocks. If all R+1 races succeed, there is an exit infection path. Therefore

    q_R(lambda) >= [lambda/(1+lambda)]^(R+1)
                  >= (k+1)^(-(R+1))
                  >= (k-1)^(-2*(R+1)).

The last inequality uses k+1 <= (k-1)^2 for k>=4; its difference is k*(k-3)>=0. Also, for R>=1 and d>=2,

    (2R+1)^d >= (2R+1)^2 > 2*(R+1),

since the difference is 4R^2+2R-1>0. As k-1>1, we obtain the STRICT bound

    q_R(lambda) > (k-1)^(-(2R+1)^d).

For R=0 the exact one-vertex race gives q_0=k*lambda/(1+k*lambda)>=1/2, whereas the criterion would require q_0<1/(k-1)<=1/3. This proves all cases. QED.

Why lambda_c>=1/k, including the boundary: dominate the number of infected particles by a branching birth-death process in which each particle births at rate k*lambda and dies at rate 1, ignoring collisions. When k*lambda<1 its expected population from one particle is exp((k*lambda-1)t); hence its probability of being alive tends to zero. At equality the embedded population chain is simple symmetric random walk on the nonnegative integers, absorbed at zero. From 1 the probability to hit M before 0 is 1/M (solve the finite gambler's-ruin difference equation). Staying forever in any finite set without hitting 0 has probability zero: in blocks of M steps there is a uniform positive probability of successive downward jumps leading to 0. Consequently survival requires hitting each M before 0 and has probability <=1/M for all M, hence zero. The branching process is nonexplosive since its total rates are linear in its population. Domination proves extinction of the contact process for lambda<=1/k, hence lambda_c>=1/k. QED.

This barrier is about this sufficient criterion, with its box coloring and elementary self-avoiding-path count. It does NOT preclude all local criteria, sharper geometric path counts, multi-scale renormalization, or more refined graphical estimates.

## 6. Exact computations and hostile-referee checks

CertificateChecks.lean records the polynomial inequalities in Proposition 5 and the exact rational row-model check in Proposition 3. The probabilistic statements are human proofs, NOT Lean formalizations. No sorry or native_decide is used; decidable rational checks use decide +kernel. The run in lean_check.txt exited 0 in 99.820 seconds. An initial BOM-related parser failure is preserved in lean_check_first.txt; it was fixed by saving the Lean source as UTF-8 without a BOM, then rerunning. All five displayed lemmas passed.

The finite-state computation in compute_exit.py uses the five-site l1-radius-one star on Z^2, rather than Q_1's nine-site cube. It lumps the nonempty states into the nine classes (c,l), where c is the center occupancy and l is the number of infected leaves. This lumping is exact: center recovery has rate c, leaf recovery rate l, center birth rate (1-c)*lambda*l, leaf birth rate c*lambda*(4-l), and successful exit rate 3*lambda*l. All rates depend only on (c,l), so these counts form a Markov chain. Its transient generator determines the exit probabilities uniquely by Lemma 4. The script solves that nine-state rational linear system exactly. This is a diagnostic, not a thermodynamic simulation. The star has five independent-color classes for centers colored x+2y mod 5; distinct centers of one class have l1 distance at least 3, hence disjoint source stars. The same proof as Proposition 4 yields criterion q_star<3^(-5). It also fails near any possible survival rate: the two-step prescribed path gives q_star>=(lambda/(1+lambda))^2>=1/25>1/243 for lambda>=1/4. Thus finite computations merely cross-check the barrier and do not estimate lambda_p.

Referee checklist:

1. Direction of comparison: upper product bound proves nonpercolation; lower comparison proves percolation only when its parameter exceeds p_c. Checked against the original source and corrected earlier ledger.
2. Graph and normalization: k=2d on the lattice. Rath--Valesin's lambda is TOTAL attempted infection rate, not this per-edge rate; moreover its spread-out graph has additional edges.
3. Simultaneous survival: uses the correct joint law via finite void probabilities and additivity, not independent singleton survival.
4. Local independence: uses directed arrows labeled by SOURCE and disjoint source boxes; absence of target recoveries in exit events is essential.
5. Infinite versus finite time: confined finite-box survival is ruled out separately by Lemma 4.
6. Self-avoiding versus all walks: the count k*(k-1)^(n-1) is an upper bound, not equality on Z^d.
7. Parameter continuity at criticality alone does not establish a uniform spatial connectivity bound. The fixed-box criterion might have implied such a gap, but Proposition 5 defeats it.
8. Counterexample scope: the row-plus-noise law is not claimed to be a contact-process invariant law. It invalidates shortcuts, not the requested inequality.
9. No finite-torus Monte Carlo is promoted to a statement about nu_lambda: finite contact processes have only the empty stationary state.

## 7. Remaining gap, stated precisely

No proof or counterexample for lambda_c(d)<lambda_p(d) has been obtained, even for d=2. What is still needed is a valid upper estimate on spatial infected connectivity for some lambda>lambda_c, not just small marginal density or fixed low-order moments. For example, it would suffice to prove for such a lambda that the probability of a specified self-avoiding n-edge path being entirely infected is <= C*a^n uniformly over its shapes with a<1/(2d-1). Alternatively a rigorously quantified multi-scale decoupling and a small crossing probability could supply a different nonpercolation certificate. Neither estimate is proved here. The local exit construction's easily independent boxes cannot supply the indicated exponential estimate, by Proposition 5.

The literature searches have rate-limit and unavailable-PDF coverage gaps recorded in LITERATURE.md; they support only 'no exact solution found in this search', not an exhaustive assertion of current openness.

Exact computation outputs: q_star(1/8)=212317/1809007; q_star(1/4)=174699/592418; q_star(2/5)=3285432/7123727; q_star(1/2)=11906/21991. In all four cases the exact residual is zero, all nine state probabilities lie in (0,1), and the prescribed two-step lower bound holds. Memory use is negligible (a 9-by-9 rational matrix). No thermodynamic claim follows from these finite values.


## 8. User-requested second attempt, 2026-10-11

A further serious attempt is fully recorded in SECOND_ATTEMPT.md. Two new routes were identified: finite stationary boxes with infected boundaries and buffered annulus crossings; and whole-cluster split-and-merge stationarity. The first was pursued through a complete reduction and small-case checks.

New proved results: Theorem 6 gives a finite stationary crossing certificate in every dimension; Lemma 7 supplies a quantitative buffered comparison at a fixed supercritical rate in d=2; Theorem 8 proves that lambda_c<lambda_p on Z^2 is equivalent to the existence of L with b_L(lambda_c)<3^(-25), using van den Berg's verified sharpness and temporal-convergence theorems. Lemma 9 proves the criterion eventually passes below 1/(2d), with an explicit certificate at d=2, lambda=1/8, L=25. A restricted three-site immigration chain proves the buffered L=1 certificate fails throughout the survival regime in d=2. Proposition 10 gives an exact finite-cluster split-and-merge stationarity identity for the other route.

These are reductions and special cases, not a proof of the requested strict inequality. Larger buffered boxes were explored using exact-CTMC numerical simulations, but no critical-rate certificate was proved. The remaining gap is now concretely the existence of a sufficiently small stationary buffered crossing probability at lambda_c (equivalent to the target in d=2), or an alternative upper estimate above lambda_c. The final verdict remains PARTIAL.
