# Independent referee verdict on w397.P0003.001

VERDICT: KEEP as a finite linear-algebra counterexample to the stated inference. It is not a counterexample to convergence of the genuine self-avoiding-walk observable and does not solve P0003.

I rederived the calculation from the definitions. Orient the six boundary edges of an interior hexagonal face as `d_j=v_(j+1)-v_j`, and put `H((v_j+v_(j+1))/2)=delta/d_j`, zero elsewhere. At `v_j`, the preceding edge contributes `(-d_(j-1)/2)(delta/d_(j-1))=-delta/2`, while the following edge contributes `(d_j/2)(delta/d_j)=+delta/2`. Hence the complex vertex residual is exactly zero at all vertices; it is trivially zero off the face. `|H|=1` on each face edge, and regular-hexagon successive edge directions differ by 60 degrees, so consecutive values differ by magnitude 1 while their midpoint separation is `sqrt(3)delta/2`. The fields on shrinking interior faces are bounded with zero boundary data but fail equicontinuity. The same calculation gives nonuniqueness after adding `cH` to any solution.

Scope: the claim concerns only the homogeneous vertex relation and boundary data. An extra property of the actual walk-sum observable could eliminate these circulation modes. The primary-source identity and the role it plays in a full scaling-limit proof remain to be checked. Reviewer: w398, 2026-10-10.
