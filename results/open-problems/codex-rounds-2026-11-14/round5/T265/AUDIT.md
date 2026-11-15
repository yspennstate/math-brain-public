# Checks and scope

The round 4 result was re-derived before the extension. Its hyperplane
jump lower bound and the zonotope clipping argument hold for arbitrary
finite representations, including extra lines. The new recheck.py
independently attains the explicit example's norms with exact rational
baseline allocations and checks the lower bound by summing local
gradient-jump norms with 70-digit arithmetic. The reported norms and
the separate integer certificate 144>81 agree.

For the extension, the critical restriction comes directly from both
per-neuron stationarity equations. Taking the input-weight equation's
inner product with that weight gives balance; dividing the output
equation by its norm gives D(u)=sign(a). Thus cancellations on one
orientation cannot be hidden by splitting coefficients. This does not
assume minimal intrinsic cost or global margin optimality.

An endpoint neuron has no zero sample preactivation. Its full signed
active sum must be sign(a) times its unit normal. Evaluating that same
linear sum at the center gives a number strictly between -1 and 1.
This excludes a center neuron on the same orientation even if its
own zero derivative is arbitrary. Only the two opposite-center edge
orientation patterns survive. audit.py enumerates all 27 nonempty
orientation supports independently and obtains exactly those two.

The angular condition was checked by two methods: exact differences
of squared edge lengths and determinants, and independently by
differences of cosines of arctangent angles. Ninety-digit checks include
half-width 10^(-8), where ordinary floating point would lose some of
the small defect. The proof uses an exact nonzero identity and does
not depend on numerical distinguishability.

The strongest attempted overgeneralization fails: a zero-centered,
angularly symmetric tent can have a margin-stationary representation.
Section 5 of PROOF.md gives a complete rational certificate. Its
balanced objective is exactly 10, independently equal to the sum of
its positive multipliers. The audit checks twelve such certificates,
including their margins, full input/output stationarity equations,
admissible center derivatives, and score identities. Therefore the
nonzero-center condition cannot be removed for arbitrary baselines.

The Gaussian statement is almost sure for each finite n,d, using a
nonzero residual polynomial and absolute continuity. It is not a
probabilistic estimate on an approximately stationary GD iterate.
Near-symmetric directions and tiny widths may make the exact
obstruction arbitrarily small. No uniform approximation or dynamical
claim has been proved. Alternative angularly symmetric interpolants
remain a possible route for the next worker.

Both final scripts use only the standard library, one process, fixed
small data, 60-second CPU/wall guards, and verified inherited niceness
20. The unsupported macOS virtual-memory limit caused the first
recheck to stop before mathematics; removing that guard allowed both
final runs to finish in less than one second with peak RSS below
17 MB. No mathematical assertion failed in either final run.
