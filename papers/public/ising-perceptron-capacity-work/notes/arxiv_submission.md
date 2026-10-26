# arXiv submission package (release-gated)

Upload `paper/main.tex`. It compiles standalone with `pdflatex`, uses no
figures, and contains its bibliography inline.

Title:
The storage capacity of the Ising perceptron: verification of the
outstanding numerical conditions

Categories: math.PR (primary); cs.CC, cond-mat.dis-nn (cross-list)

Comments field (reconfirm the page count after the final inventory build):
13 pages. Verification programs, source-bound canonical certificates, and
complete raw record trees at
https://github.com/yspennstate/ising-perceptron-capacity

Abstract (same as the paper's):

Krauth and M\'ezard (1989) predicted that the maximum number of storable
patterns in the Ising perceptron is $M_N=\alpha_\star N + o(N)$ for an explicit
constant $\alpha_\star \approx 0.833$. Ding and Sun proved the matching lower
bound, and Huang recently proved the matching upper bound; each result is
conditional on an outstanding global sign hypothesis about an explicit
low-dimensional variational problem. Those two hypotheses were supported by
ordinary floating-point computations. Huang separately used rigorous interval
arithmetic for the other numerical inputs, but inherited the Ding--Sun
parameter rectangle and left open the main Condition 1.3---the nonpositivity,
over the whole plane, of a two-variable rate function with a degenerate point
and slowly approaching tails. That unbounded optimization is the reason the
capacity upper bound remained conditional.

We verify both outstanding conditions in full. Reparametrizing Huang's functional into the
moment coordinates of the pair $(X,\tanh X)$ compresses the plane onto a
compact convex body and turns the entropy term into a per-cell linear
function by convex duality; certified sweeps then establish nonpositivity on
the whole body away from a star-shaped region around the distinguished
degenerate point. On the star itself no box enclosure can work---the tilted
covariance $\nabla^2\Phi$ is nearly singular and its inverse loses an
essential cancellation---so we certify concavity of a majorant along rays
from that point, bounding the entropy Hessian by a certified majorant of
$\mathbb E[ff^\top\max_{b\in L}\operatorname{sech}^2(b\cdot f)]$ over
sublevel-set localizations of the dual that are themselves certified by
one-dimensional sweeps; no interval enclosure of the nearly singular
covariance is inverted. The same machinery, in one variable, verifies the full
Ding--Sun Condition 1.2, including its strict-curvature clause at the
degenerate zero and its one-sided derivative clause at the singular endpoint,
and we re-establish the parameter rectangle
$(\alpha_\star,q_\star,\psi_\star)$ on which both papers rest. Together these
close the stated conditional reduction for the Krauth--M\'ezard prediction.

Final preflight before submitting:

- Freeze the exact final source commit containing all Block3a, Huang, and
  Block3bc certificates and raw record trees.
- On a clean machine, run `release_verification.py run` from that
  clean commit and retain the external Stage-A receipt. Require the nonzero
  unit inventory, paper-inventory pass, nine theorem `PASS` rows,
  `ALL CERTIFICATES PASS`, and exit code zero.
- Run `update_paper_counts.py --check`; compile `main.tex` twice; confirm the
  final page count; reject layout/reference warnings; render and visually
  inspect every page.
- On Windows, run `notes/finish.ps1` with the same commit and receipt. Retain
  its no-clobber package, exact checked receipt copy, and external release
  handoff. The handoff records the commit, receipt file/payload hashes, package
  hash, PDF hash, and page count; do not mutate the validated commit afterward.
- Read the funding and declarations section once; choose the arXiv license.
- Public repository promotion or tagging is separate and requires explicit
  owner authorization; the package/receipt gates do not publish. If promotion
  occurs, retain its public commit/tag and fresh-checkout transcript in a
  distinct external post-promotion record; never rewrite the release handoff.
