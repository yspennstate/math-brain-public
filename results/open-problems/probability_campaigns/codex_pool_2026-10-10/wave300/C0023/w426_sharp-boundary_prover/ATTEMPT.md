# C0023 sharp boundary proof packet

Author: w426. Date: 2026-10-10. Referee: w428; adversary: w427. All results below are author proofs awaiting independent audit. No lattice solution, novelty claim, or formal-check receipt is asserted.

The exact target and quantifiers are in STATEMENT.md. The model here is independent nearest-neighbor BOND percolation. The intake's less specific phrase "Bernoulli percolation" must not be used to identify bond and site problems. Current openness is UNKNOWN: recent secondary material claims an all-dimensions formal proof, but this worker has not obtained and checked its primary theorem, definitions, dependency assumptions and trusted axioms. The retrieved public repository listing does not establish that claim. It also does not establish that no proof exists.

## Prior attempt digest and chosen boundary

The exact 2026-09-07 C0023 intake records attempted_unsolved, duplicates C0094, and gives Garban-Steif Chapter XI Section 1 p.136 plus Duminil-Copin survey locators. Its search was dated, bounded and unreviewed. That row is not a proof of current openness. C0023-A001 tried to bootstrap half-space nonpercolation using uniqueness and finite energy. Its sound caution is that the intersection of a full-space cluster with a half-space need not be a connected half-space cluster: paths can leave and reenter. Its purported further reduction still required an unproved hyperplane gluing lemma and an unverified half-space susceptibility assertion, so this packet does not promote it to a theorem. The G0001 attempt splits a site-percolation finite-cluster-tail conjecture into the supercritical case and the unresolved critical case. Even if that reduction is valid, a supercritical estimate does not automatically cover p=p_c; it is a different model from the bond-gluing route used here. H/I searches and owner/store source checks are recorded separately in SOURCE_STATUS.json; absent ID matches must not be advertised as an exhaustive prior-work audit.

The primary Kozma-Nitzan paper arXiv:2401.12397v1 conjectures product gluing on arbitrary finite weighted graphs (Conjecture 1), a stronger joint-event version (Conjecture 2), and a uniform near-one version (Conjecture 3). Theorem 6 proves Conjecture 3 would imply critical nonpercolation on Z^d for d>=2. It proves some small-relay and near-origin cases but does not supply a general proof. Our lane is a structural forest/separator subfamily and failures of stronger selection bridges, disjoint from w427's finite-strip limit lane.

The named brain scar perceptron_proof_open_gaps_fleet_2026_07_12 distinguishes a locally verified fix from closing the entire proof. Here the missing arbitrary-graph gluing step remains explicit even when every finite check passes.

## L1: a deterministic separator witness

Let G be a finite undirected graph, o,b vertices, A nonempty, v a vertex, and a_star in A. Assume every path from o to any member of A contains v, and every path from a_star to b contains v. These are properties of G fixed before revealing edge states.

On H={o connects to A}, choose an open path from o to a member of A. Its o-to-v segment is open. On K={a_star connects to b}, an open path supplies an open v-to-b segment. On H intersect K, concatenating these segments gives an open walk from o to b, hence an open path. Thus H intersect K is contained in {o connects to b} intersect H, pointwise for every edge configuration and every law on configurations.

Under independent Bernoulli edge states with any edge probabilities in [0,1], H and K are increasing events. Harris positive association therefore gives

P(o connects to b) >= P(H intersect K) >= P(H) P(K) >= P(H) min_{a in A}P(a connects to b).

No conditional relay estimate is used. Degenerate probabilities 0 and 1 follow directly; no division is needed.

## L2: arbitrary many relays in a finite forest

Suppose first that o,b and all relays lie in one tree. Let P be its unique o-to-b path. For a relay a, define pi(a) as the unique attachment vertex of the a-to-P path; equivalently it is the median of o,b,a. Choose a_star whose pi(a_star)=v is nearest o along P. Every o-to-a path enters P's relay attachment at pi(a), which is v or beyond v when moving from o toward b, so every such path contains v. The a_star-to-b path contains v by definition. Apply L1.

For a forest, if some relay lies outside b's deterministic graph component, min_a P(a connects to b)=0 and the product assertion is trivial; that relay also gives a vacuous pointwise witness. Otherwise all relays lie in b's component. If o lies outside that component, H is impossible. The remaining case is the tree case above. This covers disconnected forests, overlapping terminals and relays, o=b, and endpoint edge probabilities.

The pre-FKG assertion is also obtained:

P(o connects to b, H) >= min_{a in A}P(H, a connects to b).

It follows from the pointwise witness, without independence. The product assertion requires positive association, supplied here by the stated product measure.

Sharpness: on the path o--a--b with A={a}, independent edge probabilities r,t in (0,1), the probabilities are rt, r and t, so the product inequality is equality. A multiplicative coefficient exceeding 1 cannot hold uniformly.

## L3: exact near-one modulus in the forest subfamily

Fix epsilon in (0,1). Set delta_star=1-sqrt(1-epsilon). In a forest, if H has probability greater than 1-delta_star and every relay-to-b probability is greater than 1-delta_star, L2 gives terminal probability strictly greater than (1-delta_star)^2=1-epsilon. Thus the near-one implication holds for forests with this modulus, independently of the number of relays.

No larger delta in (0,1] can work uniformly even for two-edge paths: for delta>delta_star choose x strictly between max(0,1-delta) and sqrt(1-epsilon), and give each edge of o--a--b probability x. Then P(H)=P(a connects to b)=x>1-delta while P(o connects to b)=x^2<1-epsilon. Consequently delta_star is the largest admissible forest modulus and is a necessary upper bound for any proposed modulus for all finite graphs. This is not a proof of a uniform modulus for cyclic graphs.

## B1: selected relay conditioning can destroy a terminal route

Take the path o--a2--a1--b, with independent probabilities r,s,t in (0,1) on successive edges, and order A as (a1,a2). The first reached relay I equals a1 when the first two edges are open, and equals a2 when the first is open and the middle is closed. Hence

P(I=a1)=rs; P(I=a2)=r(1-s); P(a1 connects to b)=t; P(a2 connects to b)=st.

The event I=a2 forces the middle edge closed, so P(a2 connects to b | I=a2)=0, although the unconditional probability is st>0. The actual terminal probability is rst. Substituting unconditional terminal probabilities into the relay sum gives

sum_a P(I=a)P(a connects to b)=rs*t+r(1-s)*st=rst(2-s),

which exceeds the actual probability by rst(1-s)>0. For r=s=t=1/2 this is 3/16 versus 1/8, an overstatement of 1/16 or 50%. At r=s=t=99/100 the conditional probability still equals zero while the unconditional a2-to-b probability is 9801/10000. Thus even near-one marginal terminal probabilities do not justify a conditional estimate for an arbitrarily ordered chosen relay.

The product gluing inequality is equality in this example: P(H)=r and min_a P(a connects to b)=st, giving rst. The relay order here is decreasing in terminal marginal probability. A result explicitly ordering relays by nondecreasing marginals is outside this counterexample's scope. Nor does this refute Kozma-Nitzan's uniform gluing conjecture or the lattice target.

## B2: the forest's pointwise witness does not extend across a square

Let G have edges o-a1, a1-v, o-a2, a2-v, v-b, and A={a1,a2}. For candidate a_star=a1, open exactly o-a2, a1-v, v-b; then H and a1-to-b hold, but o-to-b fails. For candidate a_star=a2, interchange a1,a2. Thus neither relay is a fixed pointwise witness on this five-edge graph. With all edge probabilities in (0,1), both configurations have positive probability.

With every edge probability 1/2, exact reliability gives P(o connects to b)=7/32, P(H)=3/4 and min_a P(a connects to b)=9/32. The product bound still holds, with margin 1/128. This refutes the proposed universal pointwise-witness bridge, not probabilistic gluing itself. The distinction rules out a deterministic replacement for the forest projection while leaving a probabilistic proof possible.

## The single hardest remaining piece

For arbitrary finite weighted graphs, derive a near-one gluing modulus independent of |A| while retaining the actual conditional law after exploration/relay selection. The present deterministic witness is unavailable on cyclic lattice windows, already on a square. Unconditional edge independence before exploration does not restore independence after choosing a relay. Proving only the forest inequality or passing exact finite examples leaves this arbitrary-graph, uniform-in-relay-count step open in this packet.

NEXT: w428 checks L1-L3 and B1-B2 against the exact enumeration receipt, then the validating coordinator may ingest only the audited special cases and refuted routes; any continuation must supply a conditioning-safe gluing argument for cyclic windows.
