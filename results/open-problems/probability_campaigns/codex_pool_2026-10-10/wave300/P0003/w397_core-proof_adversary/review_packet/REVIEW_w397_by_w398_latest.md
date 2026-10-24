# Independent referee verdict on w397.P0003.001

VERDICT: KEEP as a finite linear-algebra counterexample to the stated inference. It is not a counterexample to convergence of the genuine self-avoiding-walk observable and does not solve P0003.

I rederived the calculation from the definitions. Orient the six boundary edges of an interior hexagonal face as `d_j=v_(j+1)-v_j`, and put `H((v_j+v_(j+1))/2)=delta/d_j`, zero elsewhere. At `v_j`, the preceding edge contributes `(-d_(j-1)/2)(delta/d_(j-1))=-delta/2`, while the following edge contributes `(d_j/2)(delta/d_j)=+delta/2`. Hence the complex vertex residual is exactly zero at all vertices; it is trivially zero off the face. `|H|=1` on each face edge, and regular-hexagon successive edge directions differ by 60 degrees, so consecutive values differ by magnitude 1 while their midpoint separation is `sqrt(3)delta/2`. The fields on shrinking interior faces are bounded with zero boundary data but fail equicontinuity. The same calculation gives nonuniqueness after adding `cH` to any solution.

Scope: the claim concerns only the homogeneous vertex relation and boundary data. An extra property of the actual walk-sum observable could eliminate these circulation modes. The primary-source identity and the role it plays in a full scaling-limit proof remain to be checked. Reviewer: w398, 2026-10-10.

Primary context is now checked: Duminil-Copin–Smirnov [Lemma 1](https://arxiv.org/pdf/1007.0575#page=2) states exactly this vertex equation at `x=x_c`, spin `5/8`. The genuine observable is the weighted walk sum, which the abstract circulation field need not represent.

Additional verdicts on w397's later `ATTEMPT.md`:

- KEEP the face-contour calculation: each of the six terms `(v_(j+1)-v_j)H(p_j)` equals `delta`, so the total is `6delta`. If an edge field converges locally uniformly to a continuous `f`, subtract `f` at the face center and use the zero sum of edge increments; the contour sum is `o(delta)`. This is a necessary obstruction to compactness, not a sufficient regularity test.
- KEEP the avoidance discontinuity example: the horizontal segment at height `5/4+1/n` avoids the closed disk centered `(0,1)` with radius `1/4`; the limit at height `5/4` touches it. Vertical segments at `x=±2` stay away. The disk plus rectangle `[-1/4,1/4]×[0,1]` is boundary-attached in the stated rectangle, and the same example applies. A collar squeeze or zero boundary-event probability is needed to pass avoidance probabilities.
- KEEP the source-scope correction: [Grimmett Question 2.2](https://arxiv.org/pdf/2205.07318v1#page=3) is uniform fixed-length from the origin; the chordal critical-fugacity statement is a separate conjecture without an established ensemble bridge.
