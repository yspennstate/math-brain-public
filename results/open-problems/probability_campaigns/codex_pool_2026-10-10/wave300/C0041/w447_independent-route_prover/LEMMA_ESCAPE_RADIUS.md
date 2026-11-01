# Finite escape radius controls one residence episode

Claim ER (proved by w447; awaiting w449).

Fix d >= 1 and 0 < kappa <= 1/(2d). Let omega be any nearest-neighbor transition kernel on Z^d with omega(x,e) >= kappa. There is no independence, stationarity, or transience assumption. For S a proper subset of Z^d define

r(S) = sup_{x in S} min_{y outside S} |y-x|_1.

Suppose r(S) <= r for an integer r >= 1. Let T_S = inf{n>=0: X_n outside S}. Then for every x in S and m>=0,

P_{x,omega}(T_S > mr) <= (1-kappa^r)^m,
E_{x,omega} T_S <= r kappa^(-r).

Proof. At any block time mr on {T_S>mr}, choose a shortest lattice path from X_mr to the complement of S; its length s is at most r. Every step has quenched conditional probability at least kappa, so the conditional probability to follow that path is at least kappa^s >= kappa^r. Exit occurs by (m+1)r on that event. The Markov property gives the conditional survival bound 1-kappa^r. Applying the tower property successively gives the displayed tail; we never assume independence between blocks. Sum the tail in blocks of r: E T_S = sum_{n>=0} P(T_S>n) <= r sum_{m>=0}(1-kappa^r)^m = r kappa^(-r).

The same proof works conditionally from a finite stopping time sigma for a set S chosen measurably at sigma, fixed thereafter, provided every realized S has r(S)<=r. Work quenched, with the full environment retained. Under an annealed law, condition first on omega and the history; the deterministic bound survives averaging. Conditioning on a future event such as never backtracking is not a stopping-time version of this argument.

Claim FV (proved consequence; awaiting w449).

If S is finite, nonempty, |S|=N, then r(S)^d <= d! N and

sup_{x in S} E_{x,omega} T_S <= R kappa^(-R),
where R = floor((d! N)^(1/d)).

Proof. At a maximizer x of the integer distance r(S), S contains every point x+z with z_i>=0 and sum_i z_i <= r(S)-1. Stars and bars counts binom(r(S)-1+d,d) such points. This number is r(S)(r(S)+1)...(r(S)+d-1)/d! >= r(S)^d/d!. Hence r(S)<=R. Apply ER with R.

For t sufficiently large that q = log(t)/(2 log(1/kappa)) > 1 and q < sqrt(t), any set with sup_x E T_S >= t must have r(S)>q, and therefore N>q^d/d!. Indeed r<=q would imply r kappa^(-r)<=q sqrt(t)<t. This is a necessary size condition for slow finite traps, not a probability estimate for their occurrence.

Exact limitation. These inequalities control continuous residence before a first exit. They do not bound occupation after returns, the number of explored regions, or the first directional regeneration time. Even singleton exit time is always 1 for a nearest-neighbor chain, whereas returns to that singleton can give arbitrarily large expected total occupation. Directional transience and spatial iid must enter through a further argument, not through the block product above.

Source: owner campaign derivation, w447, 2026-10-10. Original proof text; elementary result, no novelty asserted. No formal checker or independent mathematical keep yet.
