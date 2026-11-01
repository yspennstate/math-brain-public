# Newman-Piza 1995, the log-variance lower bound, transcribed exactly
# 2026-08-12 pass 85. Discharges the REF-CORE item-2 flag ("the record
# should say folklore/NP95-shaped, untranscribed"). Source read directly: Ann. Probab. 23(3)
# 1995, 977-1005 (JSTOR 2244860), pages 981-988 of the journal PDF.

## The statement the campaign has been citing as "Var >= c log n (LOG 409)"

NP95 THEOREM 2, verbatim (p. 984): "Consider undirected first-passage percolation on Z^d
with i.i.d. passage times such that E(tau(e)^2) < infinity and var(tau(e)) > 0. Assume in
addition that one of the following two conditions is satisfied:
  (2.12)  lambda = 0  and  P(tau(e) = 0) < p_c(d),
  (2.13)  lambda > 0  and  P(tau(e) = lambda) < p_c^dir(d).
If d = 2, then there exists a constant B > 0 such that
  (2.14)  var(T_n(xhat)) >= B log(n)
for n >= 1 and all unit vectors xhat in R^2."

Definitions consumed (p. 983): lambda = inf{x : P(tau(e) <= x) > 0} (2.11); p_c(d) =
critical value for undirected nearest-neighbor bond percolation on Z^d; p_c^dir(d) = the
directed critical value. T_n(xhat) = T(0, v(n, xhat)), v(n, xhat) the lattice point closest
to n xhat (2.3).

## Scope notes that matter for us

1. DIRECTION-UNIFORM. The log bound holds for ALL unit directions, with B independent of
   direction (section 3, p. 988: "The constant B may depend on the value of p but not on
   the unit vector xhat"). The flat-edge/curvature machinery is NOT a hypothesis here.
2. WHERE CURVATURE LIVES: the power-law results (Theorems 5-7: chi >= 1/8, xi <= 3/4) need
   TWO extra hypotheses (p. 981): (i) exponential moments E[exp(beta tau)] < infinity, and
   (ii) xhat a direction of curvature for B_0 - and the paper itself stresses (p. 981) that
   directions of curvature are known to EXIST (>= 4 by symmetry, Lemma 5, nonconstructive)
   but NO explicit direction (e.g. a coordinate axis) is provably one. Any campaign use of
   chi >= 1/8 inherits that nonconstructiveness; the log bound (Theorem 2) does not.
3. THE ATOM CONDITION IS THE REAL HYPOTHESIS. (2.12)/(2.13) exclude percolation of
   minimal-weight edges; when P(tau = lambda) > p_c^dir the asymptotic shape has the
   Durrett-Liggett FLAT EDGE (p. 979, display (1.1)) and the theorem's route fails there.
   Whoever consumes c log n must check, for the campaign's weight class: continuous weights
   satisfy (2.12)/(2.13) trivially (atom mass 0); Bernoulli-type or atom-at-minimum weights
   need the explicit threshold check. E(tau^2) < infinity is automatic for the bounded-
   weights baseline; var > 0 is nondegeneracy.
4. NUMBERING TRAP. The Auffinger-Damron-Hanson survey ("50 years", 1511.03262) states this
   as its Theorem 3.7; web digests attribute "Theorem 3.7" to NP95. In NP95 it is THEOREM 2.
   Cite "NP95 Theorem 2 (= ADH survey Thm 3.7)".
5. Related in the same paper: Theorem 3 = directed model, same conclusion under (2.15)
   P(tau = lambda) < p_c^dir alone; Theorem 4 = d=2 Ising FPP, var >= D(J,h) log n in the
   interior of the nonpercolating regime. Pemantle-Peres 1994 proved the exponential-weights
   special case by different methods (p. 984 remark).
6. The published CORRECTION (Ann. Probab. 23(4) 1995, 2057) was READ same day (fire 86,
   Euclid PDF): it is a single editorial line — "This article should have appeared as a
   SPECIAL INVITED PAPER. — The Editor." No mathematical content; no theorem, constant, or
   proof affected. Caveat permanently discharged; the July-1995 text stands as printed.

## Consequence for the standing record

The campaign's uses of "Var >= c log n" (LOG 409, the sandwich note, the referee checklist
items 1-2) are all ADVERSARIAL (the bound's smallness drives beta_cert ~ n/log^2 n), so the
atom condition's failure would only STRENGTHEN those conclusions (smaller certified L). Any
future POSITIVE use now has the exact statement + conditions here and no excuse.
