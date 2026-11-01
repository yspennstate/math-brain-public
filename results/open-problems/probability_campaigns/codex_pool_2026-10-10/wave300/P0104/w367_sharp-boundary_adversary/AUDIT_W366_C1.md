# w367 independent adversarial audit of w366-C1

Verdict: KEEP as a fixed-endpoint special case. Parent P0104 remains unresolved.
Named integrating referee: w368. This is one audit; other-login admission is not claimed.

Statement audited from w366/CLAIMS.jsonl and w366/LEMMAS.md: for iid finite
almost surely nonnegative nearest-neighbor weights on Z^2, n >= 1 and r > 0,
E[T(0,n e_1)^r] is finite exactly when E[M^r] is finite, where M is the
minimum of the four weights incident to the origin. The proposed bounds are
P(M>t) <= P(T>t) <= K P(M>t/L), L=n+8,
K=n(n+2)^2(n+8), for all t >= 0.

I independently reconstructed the four paths. In order they travel along row
0, along row 1 with vertical attachments, along row -1 with attachments, and
through (-1,0), (-1,2), (n+1,2), (n+1,0). Their lengths are n, n+2, n+2,
n+8. The last path uses x=-1 and x=n+1 for vertical attachments, so even
n=1 creates no shared undirected edge. Shared vertices do not spoil edge
independence. The exact check expands these segments at n=1,2,3,17 and
finds zero intersections for all six pairs at every checked n.

The hardest step is valid because these are deterministic paths. Put
q(s)=P(tau>s). Any connecting path starts with an origin edge, so T>=M,
even when the infimum is not attained. Also T<=min S_j. The event T>t
therefore implies every S_j>t. Those four sums depend on disjoint edge
sets and hence are independent. For each j, S_j>t forces at least one
edge above t/l_j, so P(S_j>t)<=l_j q(t/l_j)<=l_j q(t/L).
Multiplication now uses genuine independence and gives the stated bound.
Strict tail inequalities remain valid with atoms, including at zero.

Integrating r t^(r-1) times these inequalities, with infinities allowed,
gives E[M^r]<=E[T^r]<=K L^r E[M^r]. No limit in n or uniform constant
was used. This checks the proof rather than only the source or file identity.

Independent boundary rederivation: for the continuous Pareto(alpha) law on
[1,infinity), q(t)=t^(-alpha) for t>=1. Thus M has tail t^(-4alpha),
and its r-th moment is finite exactly when r<4alpha. Equality diverges
logarithmically. At alpha=1/2, E[M]=2, so E[T] is finite, while E[T^2]
is infinite. A finite mean cannot remove the infinite second moment by
centering, so Var(T)=infinity. This includes the critical endpoint claimed
in w366/STATEMENT.md. No additional premise is needed for this special case.

Scope that must stay attached: K L^r grows with n. This criterion neither
establishes a fluctuation exponent nor contradicts a KPZ assertion with
suitable moment assumptions. It rejects an extension to all finite-a.s.
iid laws if that extension requires finite variance. The Pareto endpoint
fails the bounded/exponential-moment hypotheses relevant to standard
concentration results.

Reproduction: python -X utf8 verify_boundaries.py; inspect
VERIFICATION.json.w366_fixed_path_checks. Arithmetic checks supplement the
proof; no formal certificate or new asymptotic theorem is claimed.
