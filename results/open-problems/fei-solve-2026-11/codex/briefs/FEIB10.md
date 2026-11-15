disk: small

Read ~/fei_solve_agent/NOTES.md and ~/fei_solve_agent/FLOW.md first
(section 5(g) of FLOW.md states this task; sections 2, 3 and 3b are the background).
The check scripts are in ~/fei_solve_agent/code (check_p.py, check_flow.py, check_feib09.py); write your own.

Task: decide whether containment follows from the hypercontractive size statements alone.
Setting: mu is a probability measure on finite subsets of [n]. up(R) = mu{U : U contains R}, I = E|U|.
Axiom (C_a,b,c): for every set R and every integer k >= 0,
    mu{U contains R, |U - R| <= k} <= a^k b^|R| up(R)^(1+c).
For the spectral measure of a Boolean function this holds with a = 3, b = 2 (or 4; work out the exact constant from
||D_R f||_{4/3}^2 <= up(R) p(R)^(1/2), p(R) >= up(R), and granularity |D_R f| >= 2^(1-|R|) on its support) and c = 1/2.
Containment: E_{S~mu} log2(1/up(S)) <= C I, with C depending only on a, b, c.

1. State and prove the exact axiom the Boolean spectral measure satisfies (constants explicit), and check it by
   exhaustive computation on all 4-variable Boolean functions and a sample of 6-variable ones.
2. Either prove containment from (C) alone, or construct an abstract measure mu (not necessarily a spectral
   measure) satisfying (C) with E log(1/up(S)) / I unbounded. Search numerically first: an LP or a direct
   optimisation over measures on subsets of [n], n <= 6 (64 sets), and over structured families (two-scale measures:
   N small sets of size s plus a few large sets; nested chains; block designs; products of small measures).
   Report sup of E log(1/up(S))/I under (C) for each n and each family, and how it grows.
3. If a counter-measure exists, find which further property of Boolean spectral measures it violates. Candidates,
   each to be stated as an inequality on mu and tested: the level-1 theorem of FLOW section 2 applied to every
   derivative; the same axiom with up replaced by p(R) (needs functions, so say what the measure-level analogue is);
   closure of the class under restriction (the thinned law tau_rho of FLOW 5(c) must again satisfy the axiom with
   the same constants); Parseval for each derivative D_R f (sum over U containing R of mu(U) = up(R) is automatic,
   but the squares (D_R f)^2 <= 1 give sum_R-type constraints: find them).
4. If containment does follow from (C), run the same question for the cancellation half:
   B = E log2(up(S)/mu(S)) <= C I, which needs an axiom on mu(S)/up(S); propose the right one and test it.

Deliverables: PROOFS.md, scripts with outputs, RESULTS.md (tables of the sup ratios found, the extremal measures
written out explicitly), REPORT.md with a verdict line per numbered item. Label every statement PROVED, CHECKED
(numerically, with scope) or OPEN. A counter-measure must be given explicitly with a script that verifies (C) on it.
Memory: each process under 3 GiB, at most 2 threads, nice 10.
