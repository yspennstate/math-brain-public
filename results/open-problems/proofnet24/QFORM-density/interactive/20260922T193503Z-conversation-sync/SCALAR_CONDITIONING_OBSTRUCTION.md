# Scalar remainder conditioning does not give a uniform conditional density bound

Programme: QFORM-DENSITY-3EIG-20260922. Interactive record: 20260922T193503Z-conversation-sync.

Status: an explicit counterexample to an intermediate proposed proof criterion, NOT a counterexample to the original independent-input bounded-density conjecture. The full conjecture is not proved by this note. No independent review or literature-wide novelty claim is asserted.

## 1. The statement being tested

The shared owner-side outline at yspennstate/math-research-brain commit 8b508713b9edf3ae1c92824be781da39a8c0d948, scheduled_tasks/README.md, blob 959f0834db9124c916fecaa37092d3123f338092, control revision 2026-09-22.13, suggests conditioning on the SCALAR remaining quadratic contribution Q' rather than the entire remaining spectral vector. Its proposed sufficient gate is an essential supremum over b of the conditional density norm of the three-large-direction component Q3 given Q'=b.

A uniform conditional density bound would indeed be sufficient for the full output. However, the gate itself is false, even for bounded independent uniform coordinates, a full-rank matrix, and flat large eigenvectors. This note tests the displayed uniform conditional supremum, not every possible scalar-conditioning method or an appropriately weighted integral retaining the target level.

The shared edits are not authenticated here as Claude-authored. Attribution of the mathematical proposal is to the exact repository source above, not to a guessed agent identity.

## 2. An exact admissible construction

Take n=128 and X_i independent Uniform[-1/2,1/2]. Partition the indices into four equal groups. Define three vectors by repeating the following signs across those groups, then dividing every entry by sqrt(n):

u1 = (+,+,-,-)/sqrt(n),
u2 = (+,-,+,-)/sqrt(n),
u3 = (+,-,-,+)/sqrt(n).

Each displayed sign denotes an entire group of n/4 coordinates. The three vectors are orthonormal and orthogonal to the all-ones vector. Write P=sum_j u_j u_j^T and epsilon=1/128. Define

Q3 = (u1^T X)^2 + (u2^T X)^2 - (u3^T X)^2,
Q' = epsilon * ||(I-P)X||_2^2,
A = u1*u1^T + u2*u2^T - u3*u3^T + epsilon*(I-P).

Then X^T A X=Q3+Q'. The eigenvalues of A are 1,1,-1 and epsilon repeated n-3 times. Thus A satisfies exactly the original spectral assumption and is full rank. The input densities equal one on their intervals. Moreover P_ii=3/n=3/128<1/32: even the high spectral window is diffuse.

## 3. Conditional concentration near the maximum of Q'

For every point in the input cube, ||X||_2^2<=n/4. Orthogonality gives

||PX||_2^2 = ||X||_2^2 - Q'/epsilon <= n/4 - Q'/epsilon.

Also |Q3|<=||PX||_2^2. Consequently, on the event

E_eta = { Q' > epsilon*(n/4-eta) },

we have |Q3|<eta.

For every eta>0 the event E_eta has positive probability. Indeed the cube vertex v=(1/2,...,1/2) lies in ker(P), so Q'(v)=epsilon*n/4. Continuity of Q' gives a neighborhood of v inside the cube on which Q'>epsilon*(n/4-eta); that neighborhood has positive n-dimensional volume. The argument uses only a positive-measure neighborhood, not positive probability at the vertex itself.

Suppose a finite C bounded the conditional density of Q3 given Q'=b for almost every b with respect to the law of Q'. Conditional on such b, the probability of any interval J would be at most C*|J|. Averaging this inequality over the positive-probability event E_eta yields

P( |Q3|<=eta | E_eta ) <= 2*C*eta.

The left side is one. Choosing eta<1/(2C) is a contradiction. Therefore no such finite C exists, even for this one fixed n, A and product input law.

Equivalently, wherever conditional densities exist, their essential supremum in b is infinite. A pointwise lower bound is 1/[2*(n/4-b/epsilon)] for almost every relevant b below epsilon*n/4. The probability argument above avoids any need to assign a density on exceptional conditioning values.

If desired, joint absolute continuity of (Q3,Q') follows from the rank-two derivative criterion outside a null set: their gradients lie in the orthogonal spaces range(P) and ker(P), respectively, and each is nonzero outside its proper linear kernel. This extra observation is not needed for the contradiction to the proposed uniformly bounded conditional densities.

## 4. Interpretation for the full problem

The conditional law concentrates because an extreme value of the residual energy leaves almost no energy in the three-dimensional component. These conditioning events may be very rare. Replacing a weighted conditioning integral by its worst conditional density discards precisely that rarity.

The example does not imply that the density of Q3+Q' is large, let alone unbounded. In fact it satisfies the geometric hypotheses of the earlier spectral-window supporting result. It only rules out the proposed uniform-in-b conditional-density gate. A successful scalar-conditioning method must retain the distribution of b and the level t-b together; an unweighted essential supremum is insufficient.

Claim ID: QFORM-SCALAR-REMAINDER-CONDITIONAL-SUP-FALSE-v1.

Preserve the original owner-side outline and prior reports. Do not relabel the arbitrary rank-three conjecture as solved using an arbitrary-joint-density coarea bound, and do not replace the previously refuted vector-conditioning moment by this equally false uniform scalar-conditioning gate. The exclusive target remains the original independent-coordinate theorem, with arbitrary signs, dimension, laws and remaining spectrum.
