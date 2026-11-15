# C28 v1: independent sterile barriers close every fixed ordinary entry-cap family

Status: proof (unaudited). Kind: route-failure. Dossier target: 1.
This is a statement about a restricted lower family, not transience of the ordinary frog model on T3. Novelty has not been established.

## Precise model and claim

Fix an integer K >= 1, 1 <= k <= K, and 0 < p < 1/2. At each nonabsorbing vertex of a rooted ternary subtree, an ordinary frog steps to its parent with probability p and to each child with probability (1-p)/3. The parent of the subtree root u is absorbing. Initially k incoming frogs and the single resident at u are active; all other vertices have one sleeping resident.

Each child edge permits at most K awakening-enabled entrances from its parent. On any subsequent entrance the entering frog keeps its entire ordinary excursion but cannot wake residents anywhere during that excursion, until it returns across that edge. All motion, including motion during suppressed excursions, is retained. An entrance made during an already suppressed excursion cannot become awakening-enabled below the edge that started the suppression. At an awakening-enabled first visit the vertex's unique resident awakens. The rule never consults a sleeping resident's personal future walk. One can additionally suppress awakening below level h; denote the number of distinct frogs absorbed at the parent of u by R_h(k). An incoming frog is counted at most once, as is every resident.

Put beta = p/(1-p), delta = p^(K+1), and r = 3 beta (1-delta). Then

    E R_h(k) <= k beta + beta sum_{n=0}^h r^n.                 (1)

If r < 1, both the depth-h laws and any causal infinite-depth realization of this model have the uniform bound

    E R(k) <= k beta + beta/(1-r).                            (2)

In particular, at the ordinary T3 value p=1/4,

    sup_h E R_h(k) <= (k + 4^(K+1))/3.                        (3)

Consequently no fixed K in this ordinary suppressed-waking family can satisfy C27's positive escape criterion: there cannot exist epsilon > 0 such that, for every M, some finite height h has P(R_h(1) >= M) >= epsilon. This closes this lower family at p=1/4; it does not determine T127.

## Proof of the independent barriers

Use an equivalent instruction construction. At each vertex preassign an independent iid sequence of directions for awakening-enabled departures, with the ordinary probabilities above. All suppressed departures use separate independent instruction streams. In particular a suppressed visit does NOT consume an awakening-enabled instruction. A direction is drawn only when the next step is to be taken, and its stream is selected using the already known suppression flag. The unused direction remains independent of the past with the correct transition probabilities. Thus this construction gives the same joint law as independent ordinary personal frog walks with the specified causal suppression rule.

Let E_v be the event that the first K+1 awakening-enabled instructions at v all point to its parent. The events (E_v) over fixed vertices are independent, with probability delta. If E_v occurs, v's resident and the at most K awakening-enabled arrivals from its parent all leave immediately upward. Before any enabled departure to a child could occur, there could be neither an enabled arrival from a child nor an awakened descendant: both would require an earlier enabled departure from v to a child. A first such departure is therefore impossible. Suppressed visitors cannot wake a child or use an enabled instruction. This proves that E_v blocks all awakening strictly below v.

For any fixed vertex w at level n below u, awakening w requires the failure of E_v at each of its n strict ancestors in the subtree. This is a deterministic necessary condition on the instruction arrays. Independence of these FIXED vertex events therefore gives

    P(w awakens) <= (1-delta)^n.                              (4)

No independence between a random number of entrants or conditional return events is asserted or used.

## First moment using the same law in personal-walk coordinates

Return to the equivalent construction using an independent ordinary personal walk for every frog. A sleeping resident's awakening event is independent of its own entire personal walk: until first awakening that walk is not queried, so changing it cannot change whether the first awakening occurs. Conditional on awakening at level n, its subsequent motion is still its entire ordinary walk, with only its ability to wake others suppressed on selected excursions. The probability that such a walk ever hits the absorbing parent of u is beta^(n+1). To verify this probability, project to distance from that parent. Away from zero the distance decreases with probability p and increases with probability 1-p. The gambler's-ruin formula between 0 and L, followed by L -> infinity, gives (p/(1-p))^(n+1).

Hence the contribution of the resident at w to the mean absorbed count is exactly

    P(w awakens) beta^(n+1).

The barriers used to bound the first factor and the independence used for this factorization were established in two representations of the SAME probability law. There is no claim that the barrier events and personal future hit indicators are independent in one simultaneous coupling.

Each of the k initial incoming frogs has first-hit probability beta. There are 3^n possible residents at level n. Summing nonnegative indicators (Tonelli's theorem) and using (4) proves (1). The same sum over all levels proves (2) for an infinite-depth causal version whenever r < 1; this argument does not require interchanging a nonmonotone height construction with an infinite model. At p=1/4 one has beta=1/3, delta=4^(-(K+1)), and r=1-delta, proving (3).

Finally Markov's inequality gives

    sup_h P(R_h(1) >= M) <= (1+4^(K+1))/(3M) -> 0.

This contradicts the positive escape criterion for every epsilon > 0 and proves the route-failure claim.

## Scope, checks, and limitations

For k=1 the bounds are 17/3 (K=1), 65/3 (K=2), 1025/3 (K=4), and 262145/3 (K=8). The cap-4 barrier has probability 1/1024, so growth through heights 20--64 is entirely compatible with this finite, loose bound. The numerical data did not establish recurrence or a critical drift.

The proof requires the permanent finite budget on awakening-enabled entries and suppression of ALL waking throughout each overflow excursion. It does not cover a model that renews the budget, allows overflow frogs to wake deeper residents, or has unbounded/level-dependent caps. It also does not cover a nonbacktracking incoming frog: its first step may be forced away from the parent, invalidating the all-up barrier. An ordinary model that shares a vertex's enabled instruction stream with suppressed visits would need a different barrier proof; that sharing is unnecessary and is not the independent-direction representation used here.

For level-dependent finite caps K_j, the same necessary-condition argument instead bounds awakening at level n by product_{j=0}^{n-1}(1-p^(K_j+1)). This observation alone proves neither recurrence nor transience when the resulting weighted series diverges. It only identifies how a future family might evade the particular uniform-cap obstruction.

Prior sources: HJJ, arXiv:1404.6238, Section 2, supplies the comparison context; the fixed-cap barrier and its claimed consequence here are submitted as owner-own-work, proof unaudited. This is not claimed as a new literature result without a further novelty check.

Hardest remaining piece for T127: a lower comparison that can give positive escape at p=1/4 despite retaining arbitrarily many usable returns, or an independent upper comparison for the full model. This claim supplies neither.

Checks: computations/C28_EXACT_CHECKS.json (rational identities and scope checks). These checks verify algebra only; the probabilistic argument requires independent audit.
