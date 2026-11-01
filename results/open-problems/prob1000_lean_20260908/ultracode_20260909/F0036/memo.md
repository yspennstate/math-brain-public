# F0036 - Potential most recent common ancestors in the Brownian net (Schertzer-Sun-Swart, Conjecture 8.3)

Date: 2026-09-09. Status: partial (a rigorous reduction, a corrected sub-claim from the earlier attempt, and a numerical test that comes out in favour of the conjecture). Not settled.

## 1. The problem as the source states it

Source: E. Schertzer, R. Sun, J. M. Swart, "The Brownian web, the Brownian net, and their universality", arXiv:1506.00724 (2015), Section 8.2, p. 72 of the PDF. Verbatim:

> Let M be the set of all meeting points of paths in W({0} x R), i.e.,
>
> M := { (x, t) in R^2 : t > 0, there exist pi, pi' in W({0} x R) s.t. pi(t) = x = pi'(t), pi < pi' on (0, t) }.   (8.3)
>
> Biologically, we can interpret a point z = (x, t) that is the first meeting point of paths pi(x,0) and pi(x',0) as the most recent common ancestor (MRCA) of x and x', that lived a time t in the past. It is easy to see that M is a locally finite subset of R x (0, infinity).
>
> Moving away from neutral evolution, one can interpret paths in the Brownian net as potential genealogies (cf. the biased voter model in Sec. 7.2.2), where in order to determine the true genealogy of an individual, one has to have information about what happens at selection events, which correspond to separation points. In this case, replacing W({0} x R) in (8.3) by N({0} x R), we can interpret the resulting set M as the set of potential most recent common ancestors (PMRCAs) of individuals living at time zero.
>
> **Conjecture 8.3 (Potential most recent common ancestors)** If we replace W({0} x R) in (8.3) by N({0} x R), then the set M is a locally finite subset of R x (0, infinity).
>
> The definition of a potential most recent common ancestor (PMRCA) is somewhat reminiscent of the definition of a (0, infinity)-relevant separation point, except that in order to determine wether a meeting point is a PMRCA, we have to follow forward paths backwards in time. This is similar to the definition of the map phi : M* -> S* and indeed, Conjecture 8.3 seems to be closely related to our previous two conjectures. In particular, meeting points that lie inside a bubble (properly defined w.r.t. the finite time horizon 0) can never be PMRCAs.

The ledger row (problems.jsonl, F0036) quotes this correctly: "pi < pi' on (0,t)" is a strict inequality at every time of the open interval, and the conclusion is local finiteness in R x (0, infinity) (nothing is claimed at t = 0, where the set is dense).

Notation below: N is the standard Brownian net, (W^l, W^r) the left-right web, l_z and r_z the left-most and right-most paths from z, xi_t = {pi(t) : pi in N({0} x R)} the branching-coalescing point set started from R at time 0, and M now always means the net version of (8.3).

## 2. Findings

Everything in this section is proved from the results quoted in the survey (Prop. 3.14 containment, Prop. 3.15 hopping, Prop. 3.18 density of xi_t, Thm. 3.24 classification) together with Theorem 1.12 of Schertzer-Sun-Swart, "Special points of the Brownian net", EJP 14 (2009) (arXiv:0806.2326). Two standard facts are used repeatedly:

(F1) Containment (Prop. 3.14): no pi in N and l in W^l with l(s) <= pi(s) and pi(t) < l(t) for some s < t; symmetrically for r in W^r. In words, a net path never crosses a left-most path from right to left, nor a right-most path from left to right. Crossing a left-most path from left to right is allowed and does happen (item 2.3 below).

(F2) A left path l and a right path r with l(s) <= r(s) satisfy l <= r on [s, infinity). This is (F1) applied to r restricted to [s, infinity), which is a net path.

### 2.1 Every PMRCA is a meeting point of type (pp, p)

If pi < pi' on (0, t) and pi(t) = pi'(t) = x, then pi and pi' enter z = (x, t) and are not equivalent as incoming paths (equivalence means pi(t_n) = pi'(t_n) along a sequence t_n up to t, which the strict inequality excludes). So z has at least two incoming equivalence classes of net paths. By Theorem 1.7 of SSS09 (Thm. 3.24 in the survey) together with Remark 1 there (n counts as a single incoming class) and Theorem 1.12(a) (the incoming relation is an equivalence relation on N_in(z)), the only type with two incoming classes is (pp, p). Hence

    M is contained in the set of meeting points of N, which is countable and dense.

By Theorem 1.12(a) the two classes carry (extended) pairs (l_1, r_1) and (l_2, r_2) with l_1 <= pi <= r_1 and l_2 <= pi' <= r_2 near t, and r_1 < l_2 on (t - eps, t). By (F2) and the fact that a left and a right path cross at most once, r_1 < l_2 on their whole common lifetime before t.

### 2.2 Pairs from a common starting point; the same-source part of M is locally finite

Let pi, pi' start at the same point z_0 = (y, 0). At a deterministic time all points are of type (o,p), (o,pp) or (p,p) (Thm. 3.24). If z_0 has a single outgoing class, every outgoing net path is squeezed between the equivalent pair (l_{z_0}, r_{z_0}) near time 0 (Thm. 1.12(b)), and since those two touch at times t_n down to 0, so do pi and pi'. So a same-source pair can only come from a point of type (o, pp), with pi in the left class (l_{z_0}, r_1) and pi' in the right class (l_2, r_{z_0}), r_1 < l_2 on (0, eps). By Thm. 1.12(b) and (F1), pi <= r_1 and pi' >= l_2 on all of [0, infinity). Hence pi and pi' cannot meet before the first meeting time T of r_1 and l_2, and (r_1, l_2) is itself an ordered pair from z_0 that meets at T. So

    the same-source pairs from z_0 contribute exactly one point of M: the top (r_1(T), T) of the mesh M(r_1, l_2) with bottom point z_0.

These mesh tops form a locally finite set. Proof. Fix a box [a, b] x [t_0, t_1] with t_0 > 0 and put s = t_0 / 2. Two such meshes with bottoms y < y' have l_2^{y} <= r_1^{y'} by (F2), so their cross-sections at time s are disjoint open intervals of positive length (positive because both meshes reach time t_0 > s). Their left endpoints r_1^{y}(s) are therefore distinct points of xi_s. Paths that reach [a, b] before time t_1 are confined: choose K with l_{(b+K,0)} > b and r_{(a-K,0)} < a on [0, t_1] (possible a.s.); by (F1) a net path from time 0 starting outside [a-K, b+K] stays outside [a, b] up to time t_1, and one starting inside stays between l_{(a-K,0)} and r_{(b+K,0)}, hence in a bounded interval [-L, L] on [0, t_1]. So the number of mesh tops in the box is at most the number of points of xi_s in [-L, L], which is a.s. finite by Prop. 3.18 (finite expectation). QED.

### 2.3 The earlier attempt's reduction is wrong: a pair of sources produces more than one PMRCA

Attempt F0036-A001 asserted that for sources y < y' the first meeting of any ordered pair (pi from y, pi' from y') is the meeting point Z_1 of r_y and l_{y'}. What is true is only the inequality: since pi <= r_y and pi' >= l_{y'} (containment), no ordered pair from (y, y') meets before tau := the first meeting time of r_y and l_{y'}, and (r_y, l_{y'}) is itself an ordered pair meeting at Z_1 = (r_y(tau), tau). So Z_1 is the earliest point of M coming from (y, y'), and it is the only one in R x (0, tau].

But it is not the only one. Take pi = l_y and pi' = r_{y'}. By (F2) l_y < r_{y'} until their first meeting time t_2, so Z_2 = (l_y(t_2), t_2) is in M. At time tau we have l_y(tau) <= r_y(tau) = l_{y'}(tau) <= r_{y'}(tau); whenever one of the two inequalities is strict, t_2 > tau and Z_2 is a different point from Z_1. The pair (l_y, r_y) from a deterministic point is a sticky pair whose set of coincidence times is nowhere dense with positive Lebesgue measure (SS08, Prop. 3.1, quoted in SSS09 p. 5), so l_y(tau) < r_y(tau) has positive probability, and then Z_2 is a second PMRCA from the same two sources. After tau the two tubes [l_y, r_y] and [l_{y'}, r_{y'}] overlap and the intermediate paths (obtained by hopping) generate further first-meeting points. The count of PMRCAs per pair of sources is therefore not one, and the finiteness question is exactly about how many such later points a pair of overlapping tubes produces. This is the whole difficulty and A001's argument does not address it.

Side remark on the survey's last sentence ("meeting points that lie inside a bubble ... can never be PMRCAs"). As literally read this needs a qualification: by (F1) a net path may cross a left-most path from left to right (r_y crosses l_{y'} at Z_1 and is strictly to its right at later times), so a bubble bounded by l_z on the left and r_z on the right can be entered from outside on both sides, and a pair entering from the two sides can meet inside the bubble without having touched. Presumably the authors have a definition of "inside" relative to N({0} x R) in mind; the reduction in 2.4 does not use this remark.

### 2.4 Reduction to pairs of points of xi_s, and the first step of the recursion

Fix a deterministic s > 0. Every path of N({0} x R) passes through a point of xi_s at time s, and xi_s is a.s. locally finite (Prop. 3.18). For p <= q in xi_s let M_s(p, q) be the set of first meeting points of pairs pi in N((p, s)), pi' in N((q, s)) with pi < pi' on (s, t). Then

    M restricted to R x (s, infinity) is contained in the union over p <= q in xi_s of M_s(p, q),

and by the confinement argument of 2.2 only finitely many pairs meet a given box. The diagonal terms M_s(p, p) are handled by 2.2 (empty or a single mesh top). So

    Conjecture 8.3 follows if, for every deterministic s > 0 and every pair p < q of points of xi_s, the set M_s(p, q) is locally finite in R x (s, infinity).

(This is a sufficient condition, not an equivalence: a pair ordered on (s, t) need not extend to a pair ordered on (0, t).)

For a fixed pair p < q, with tau_1 the first meeting time of r_p and l_q (the right-most path from (p, s) and the left-most from (q, s); if (p, s) is of type (o, pp) take the outer one), the argument of 2.3 gives

    M_s(p, q) restricted to R x (s, tau_1] = { Z_1 },   Z_1 = (r_p(tau_1), tau_1).

Moreover Z_1 is isolated in M_s(p, q) provided the point sets xi^{(p,s)}_{tau_1} and xi^{(q,s)}_{tau_1} (net paths from the two points, evaluated at the random time tau_1) are locally finite near r_p(tau_1) = l_q(tau_1): a pair meeting after tau_1 satisfies pi(tau_1) < r_p(tau_1) or pi'(tau_1) > l_q(tau_1), hence is separated by a positive distance delta at time tau_1, and equicontinuity of the compact set N gives a positive time before two paths delta apart can meet. Whether tau_1 can be one of the exceptional times at which the point set is not locally finite (SSS09 Prop. 3.14 shows such times form a dense set; R. Kou, arXiv:2512.10761, shows they have Hausdorff dimension 1/2) is not settled here; intuitively it is not, but I have no proof.

After tau_1 the two tubes overlap and every ordered pair (p_i, q_j) of points of xi^{(p,s)}_{tau_1} x xi^{(q,s)}_{tau_1} other than the coalesced one restarts the same recursion. The conjecture is therefore equivalent to the statement that this tree of restarts does not accumulate in a bounded region, which is what the next section tests numerically.

## 3. Numerical test (discrete branching-coalescing walks)

Script: pmrca_sim.py. Model: sites of Z^2_even, each site has a right arrow w.p. (1 - eps)/2, a left arrow w.p. (1 - eps)/2, both w.p. eps; all even sites at time 0 are occupied; diffusive scaling (space eps, time eps^2) converges to the Brownian net (Sun-Swart 2008). A discrete PMRCA is a site (x, s+1) with incoming arrows from (x-1, s) and (x+1, s) such that the pair (x-1, x+1) is "ordered-reachable" at time s: there are paths from time 0 to the two sites that are strictly ordered at every time 1..s. The DP keeps the boolean matrix of ordered-reachable pairs (O(L^2) per step). Counted in the continuum box x in [-2, 2], t in [0.25, 2]; strip half-width 10 (paths are killed at the strip boundary; paths from outside the strip reach the box with negligible probability). Controls:

* eps = 0 (coalescing walks, Brownian web): the expected number of MRCAs in the box is 2*XB*(1/sqrt(pi*T0) - 1/sqrt(pi*T1)) = 2.92 for XB = 2, T0 = 0.25, T1 = 2 (each meeting removes one particle from a coalescing point set of density 1/sqrt(pi t)). Measured at lattice spacing 0.1 over 20 seeds: 3.25 +- 0.38. Consistent.
* all meeting points with both incoming sides occupied by time-0 paths (ordering not required): these are dense in the continuum and must grow like 1/eps.
* the DP was checked against brute-force enumeration of all path pairs on 300 random small systems (bruteforce_check.py): 1028 PMRCA sites found by both, no mismatch.

Results (mean over seeds, standard error in brackets):

    eps      seeds   PMRCAs in box     all meetings     eps x all meetings
    0.1      2       50.5 (9.5)        144.0            14.4
    0.05     10      55.2 (5.0)        271.7            13.6
    0.025    6       50.0 (7.3)        525.0            13.1
    0.0125   abandoned: the run (strip 7, 12,800 steps on a 1120^2 pair matrix) got 10 CPU-seconds in 18 minutes on the shared machine and was killed

Second series, a cheaper window so that eps = 0.0125 fits the budget: box x in [-2, 2], t in [0.25, 1], strip half-width 6, run at all three eps for a like-for-like comparison (web control for this window: 2.26):

    eps      seeds   PMRCAs in box     all meetings     eps x all meetings
    0.05     6       34.0 (5.5)        126.3            6.3
    0.025    4       28.0 (4.6)        251.5            6.3
    0.0125   2       20.5 (0.5; the true spread is about 10 per seed, so read +-7)   414.5   5.2

In both series the count of all meeting points grows like 1/eps (the last ratio, 1.65 instead of 2, is within what two seeds and the narrower strip allow), as it must for a set that is dense in the limit. The PMRCA count never grows: 50, 55, 50 in the first window across a factor 4 in eps, and 34, 28, 20 in the second window across a factor 4 in eps, the latter if anything decreasing toward its limit. Within the resolution of this test (about +-15 to 30 percent per point) the discrete PMRCAs converge to a finite intensity (roughly 7 per unit space-time area in the first window, 5-7 in the second), which is what Conjecture 8.3 predicts. A logarithmic divergence of a few units per halving is excluded only at the level of these error bars; see Section 5.

## 4. What is not done

* No proof that M_s(p, q) is locally finite for a pair of points; the recursion after tau_1 is not controlled. This is the conjecture.
* The isolation of Z_1 is conditional on local finiteness of the two clouds at the random time tau_1.
* No Lean file: the load-bearing steps are topological and probabilistic (classification of special points, containment, compactness), not an algebraic identity or an inequality that Mathlib could certify. Nothing was compiled.
* No first-moment formula for E|M in A|. Such a formula would settle the conjecture; a plausible route is a characterisation of PMRCAs through the extremal pair (the left-most time-0 path entering the left class and the right-most one entering the right class), which I could not identify with a canonical left-right pair.

## 5. Checks, and the strongest case that this is wrong

The strongest case against the numerical conclusion: a slow divergence. If the true count grew like c log(1/eps), then c of order 5 would hide inside the error bars of three points spaced by factors of 2. The check that would confirm it is the eps = 0.0125 and 0.00625 points: a monotone rise of 5 or more per halving would contradict the conjecture's reading of the data. The eps = 0.0125 point was run in the second window (Section 3) and came out lower than the two coarser points, not higher; an eps = 0.00625 point (four times the cost) was not affordable on the shared machine tonight. A second caveat is structural: convergence of the discrete counts does not by itself prove local finiteness of the continuum set (strict ordering is not a closed condition, so the continuum M could in principle be larger than the limit of the discrete sets). The theoretical part (Sections 2.1-2.4) is independent of the simulation.

The strongest case against Section 2.3: that l_y(tau) = r_y(tau) and l_{y'}(tau) = r_{y'}(tau) almost surely, which would make Z_2 = Z_1 and rescue A001's claim for the extremal pair. This would require the random time tau (the hitting time of l_{y'} by r_y) to lie a.s. in the nowhere dense coincidence set of the sticky pair (l_y, r_y); given the SDE description (independent driving noises when the paths are apart) that has probability strictly less than one. Even if it held, the intermediate hopping paths after tau would still produce further first meetings, so the count per source pair would still not be one.

Checks actually run: web control (3.25 +- 0.38 vs 2.92); brute-force versus DP agreement (300 systems, 1028 = 1028 sites); 1/eps growth of the all-meeting control (eps x count = 14.4, 13.6, 13.1).

## 6. Prior art

Searched (WebSearch, 2026-09-09): "potential most recent common ancestors" Brownian net; "Brownian net" "most recent common ancestor" locally finite Schertzer Sun Swart; bubble hypothesis / Conjecture 8.1; Swart Brownian net 2020-2025 separation points meeting points. Fetched and read: Swart's talk "The Brownian net and its meshes" (Budapest, 31 March 2025), which still lists the bubble hypothesis and the bubble complexity hypothesis as open hypotheses and adds two open problems, with no mention of a proof; the Cambridge book version of the survey (Schertzer-Sun-Swart 2017, "The Brownian Web, the Brownian Net, and their Universality", Conjecture 6.8.3), which restates the conjecture unchanged; the Semantic Scholar citation list of arXiv:1506.00724 (59 citing works, none on meeting points, common ancestors or bubbles of the net); R. Kou, "Special times for the point set process of the Brownian Net", arXiv:2512.10761 (2025), which concerns exceptional times of xi_t (Hausdorff dimension 1/2) and does not touch the conjecture; Sun-Swart-Yu, "Universality of the Brownian net", arXiv:2401.09370, whose abstract does not touch it either. Nothing found that settles or attacks Conjecture 8.3; it is open as of the 2025 talk.

Files: memo.md (this), pmrca_sim.py (the DP), bruteforce_check.py (independent check), summarize.py (table), pmrca_eps*.jsonl (raw runs), run_eps0125.log.
