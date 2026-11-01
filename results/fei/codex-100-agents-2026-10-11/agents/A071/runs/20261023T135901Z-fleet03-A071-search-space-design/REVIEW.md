# Independent analytic review of A075 whole-row signed drift, version 1

Source: A075 run 20261023T133516Z-fleet03-A075-search-to-theorem-bridge,
PROOF.md sections 1-6 and the exact CLAIMS.json statement/hypotheses.
Verdict: HOLDS UNCHANGED SCOPE, including the explicitly unpaid initial price.
No substantive repair was supplied; the prime-ball obstruction is separate.
No source executable was imported or run for this review.

Reconstruction: split the full Fourier index into a queried core's remaining
index T and the outside physical index W. Write the outer Boolean function
as A+z_j D, evaluated on the other cores. For T nonempty both paired full
coefficients are Dhat(W) times the queried inner pair. The entropy decrement
of a pair is homogeneous of degree two because the log-scale terms cancel
by conservation of the sum of squared coefficients. Parseval gives the
outside sum Dhat(W)^2=E D^2=q_j. All nonempty T rows cancel exactly against
q_j times the queried core's entropy decrement. For T empty the full pair
is (Ahat(W)+mu Dhat(W),t Dhat(W)); its inner counterpart is (mu,t).
Other cores' entropy weights have conserved means since q_k is affine in
the queried core's sign mean. This reconstructs the source exact identity
without occupied-set independence or division by a core variance.

For any real x,y, the paired decrement is Phi(x^2,y^2)+Jrow(x,y).
Both are nonnegative: Phi is unnormalized binary entropy; Jrow is a
concavity gap of eta. The elementary log estimate ln(1+s^2)<=s gives
Phi<=(2/ln2)|xy|. Write Jrow=(x^2+y^2)G(2xy/(x^2+y^2))/ln2.
Derivative comparison atanh(z)<=z/sqrt(1-z^2), starting at zero, gives
G(z)<=1-sqrt(1-z^2), including endpoints. Thus
Jrow<=(2/ln2)min(x^2,y^2). This proves the source bound on the entire row.
For the actual Boolean pair, conditional means mu+t and mu-t belong to
[-1,1], so |mu|+|t|<=1 and |t|<=Inf_i(g_j). Subtracting the nonnegative
full exceptional rows yields exactly the claimed 2/ln2 physical influence
bound. Zero derivative, constant cores and zero biases need no division.

Influence telescoping makes C+kappa I superharmonic; its complete-revelation
value is zero, proving nonnegativity by finite induction. Weighted hulls
are superharmonic because q_j is unchanged when core j is queried, while
all other q_k conserve their means. Majorization follows from rho_j>=
H(g_j)-K I(g_j) and exact influence composition, for every real K>=0.
If supplied a dominates U, child a_b=U_b+a-mean U_b is nonnegative and
mean-conserved. Positive a uses its common mean-one owner kernel; a=0
forces both child credits zero. For debit sum T>0, d_b/T preserves signed
labels; T=0 forces both d_b zero and kernel one preserves cancelling labels.
Thus all source accounting qualifications and zero-total cases are valid.
The rational potentials differ by exactly 3I, conditional on supplied stock;
this is no new or reusable donor. Singleton initialization remains H+kappa I.

The source auxiliary four-bit countercontrol checks independently as follows:
at mu=5/8,t=d=3/8, direct expansion gives
L-2d=37/16-(9/32)log2 3-(25/32)log2 5, positive iff
2^74>3^9*5^25. This controls the stronger exceptional-row guess only.
The separately frozen audit recomputes that integer inequality, source
canonical digest, whole-row identities on actual small Boolean functions,
and rejects altered artifacts. This author's independent review is not an
external review of the NEW prime-ball theorem, which still needs a peer.
