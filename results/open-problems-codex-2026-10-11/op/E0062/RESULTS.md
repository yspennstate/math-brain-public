# E0062: final mathematical scope

Verdict: PARTIAL. No general necessary-and-sufficient condition for
arbitrary matrices with zero entries has been established in this attempt.

For A skew-symmetric with |a_ij|≤1, write
V_A(x)_i=x_i(1+Σ_j a_ij x_j). The property at issue is convergence of
n^(-1)Σ_{k<n}V_A^k(x) for every point of the closed simplex.

The proved results, with complete proofs in ATTEMPT.md, are:

| Matrix class | Result | Proof |
| --- | --- | --- |
| Acyclic graph i→j iff a_ij>0, including zeros | Every trajectory converges | §1 |
| All off-diagonal entries nonzero | The every-point ergodic property holds iff the sign tournament is acyclic | §§2–3; published three-species obstruction is a dependency |
| Chordless four-cycle, 0<a,b,c,d≤1, a−b−ab≥0 and c−d−cd≥0 | Every trajectory converges | §§5–5a |
| Chordless four-cycle, 0<a,b,c,d≤1 and ac=bd | Every nonfixed interior point has a nonconvergent Cesàro-average vector; boundary trajectories converge | §§12–14 |
| Independent blocks from the certified convergence classes | Every trajectory converges in any finite dimension | §7 |

The four-cycle matrix in these statements is

    A(a,b,c,d) = [[ 0, a, 0,-d],
                  [-a, 0, b, 0],
                  [ 0,-b, 0, c],
                  [ d, 0,-c, 0]].

An exact counterexample to any sign-only criterion:

- A(1/2,1/2,1/2,1/2) fails the every-point property. The interior point
  (1/10,2/10,3/10,4/10) is nonfixed and has a nonconvergent average vector.
- A(9/10,1/10,9/10,1/10) has convergent trajectories from every initial
  point, because both sufficient inequalities have gap 71/100.

These matrices have exactly the same signs and zero positions.

The remaining gap includes unbalanced four-cycles outside the sufficient
convergence bounds, such as a=c=1/2,b=d=2/5, and general matrices with
interacting cyclic components. The boundaries of the sufficient parameter
region have not been proved necessary. The literature search found no
verified full solution; its coverage is bounded and novelty is not claimed.

REFEREE.md records the second mathematical rereading. VERIFICATION.md and
lean_check_result.json distinguish the finite Lean verification from the
ordinary analytic proofs. The exact rational check counts are 2,187 for
prefix/cut algebra and 24,024 for product bounds. Numerical trajectories
are supporting evidence only.
The Lean compiler outcome is unrecovered after the interrupted shared-slot
wait; the supplied formalization is not credited as checked.
