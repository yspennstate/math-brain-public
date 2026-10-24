# An exact thick-point optimization that does not determine d_gamma

Saved 2026-10-10 by w520. This continuation derives a deterministic algebraic obstruction, distinct from w519's subpower-normalization lemma. It is awaiting w521's independent check.

Let 0 < gamma < 2 and xi > 0. Set Q = 2/gamma + gamma/2 and, for -2 <= alpha <= 2, define

F(alpha) = (2 - alpha^2/2) / (xi*(Q-alpha)).

Q > 2, so every denominator is positive, including both endpoints. A direct completed-square identity gives

gamma/xi - F(alpha) = (alpha-gamma)^2 / (2*xi*(Q-alpha)).

Proof: multiply both sides by xi*(Q-alpha); the numerator on the left is gamma*Q - gamma*alpha - 2 + alpha^2/2 = (alpha-gamma)^2/2 because gamma*Q = 2 + gamma^2/2. Thus F has the unique maximum gamma/xi at alpha=gamma. The endpoints have F(-2)=F(2)=0. This identity holds for every admissible deterministic triple (gamma,xi,alpha); no independence, limit interchange or numerical experiment enters its proof.

Interpretation. Gwynne-Pfeffer, arXiv:1905.11790v3, Theorem 1.5/(1.12), gives this profile for the metric dimension of a deterministic (or field-independent random) full-Euclidean-dimension Borel set intersected with the alpha-thick points of a whole-plane GFF. Its parameter xi is already gamma/d_gamma. Substitution gives max F = d_gamma, reproducing the existing implicit parameter relation. It supplies no independent equation for xi and no exact evaluation of d_gamma.

The theorem's statement is for each alpha almost surely. Our algebra does not exchange that order with one common almost-sure event over all alpha. Nor does it infer the dimension of an uncountable union from the supremum of its pieces: [0,1] is an uncountable union of dimension-zero singletons but has dimension one. The dimension of the whole metric plane is established separately in the cited paper. A candidate proof relying on such an interchange must justify it rather than cite this identity.

At gamma=2 the denominator for alpha=2 vanishes; this argument is explicitly subcritical. The elementary identity remains valid for alpha<2 in that case, but the endpoint and critical metric require their own formulation. At gamma=0 neither Q nor the stated parametrization is defined. Neither boundary is included here.

The same obstruction appears in metric KPZ: if q is the metric Hausdorff dimension of the whole plane, then 2 = xi*Q*q - xi^2*q^2/2. On the physical branch xi*q <= Q, solving gives xi*q = Q-sqrt(Q^2-4)=gamma. This again identifies q=gamma/xi, not xi. The other quadratic root equals 4/gamma and is outside that branch when gamma<2.

Single hardest unresolved piece: prove an independent exact LFPP crossing exponent lambda(xi)=lim log(a_epsilon)/log(epsilon), where a_epsilon is the median of left-right crossing length in the unit square for heat-kernel-mollified whole-plane GFF. The established relation is lambda=1-xi*Q(xi); the dependence of Q on xi is the open input. A reformulated identity involving that same unknown is not a new estimate.

NEXT: w521 checks the completed-square identity, parameter domain and route-scoped interpretation; further proof work should target an independent exact crossing estimate.
