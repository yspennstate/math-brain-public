# C0023 referee proof attempt — 2026-10-10

## Exact target and status boundary

For each integer 3 <= d <= 10, nearest-neighbor Bernoulli bond percolation on Z^d has independent open edges of parameter p. Set theta_d(p)=P_p(|C(0)|=infinity) and p_c(d)=inf{p in [0,1]:theta_d(p)>0}. The target is theta_d(p_c(d))=0. Garban–Steif, Chapter XI, printed p. 134 (PDF p. 136), calls critical nonpercolation in the intermediate dimensions a major open question in its historical context. The 7 September intake used the later known d>=11 bound. The 24 September OpenAI primary manuscripts now report d=3 bond/site critical nonpercolation (Theorem 1.1 of the cubic paper) and bond critical nonpercolation on all quasi-transitive graphs with p_c<1 (Theorem 1.1 of the general paper). They therefore report a solution covering C0023, but I have not audited their complete proof or the formal solutions; the comparator challenge files with `sorry` are statement files. No new-solution or novelty claim is made here.

## One independent route, with its single open input

The w420 block route has a precise sufficient criterion. Let S_z be the seed box centered at L(z_1,z_2,0,...,0), h_z its lex-first vertex reaching the boundary of the M-box, and G_z(L,M) the finite compatible-anchor event defined in w420/ATTEMPT.md. Put H=M+L and R=floor(2H/L). The field of G_z is strongly R-dependent because each event only reads bonds in D_z(H). Its failure probability q_p(L,M) below delta_R=800^{-(R+1)^2} yields an infinite good coarse component by the checked bad-circuit count. The identical global anchor choices then make an infinite original open cluster. Because G_z uses finitely many bonds, a strict q_{p_c}<delta_R persists at some p<p_c and contradicts the definition of p_c. These are the independently checked steps L1–L3 in REVIEW_VERDICTS.jsonl.

The **single missing input G** in that route is: if theta_d(p_c)>0, prove that for at least one finite M>=L>=1, q_{p_c}(L,M)<800^{-(floor(2(M+L)/L)+1)^2}. The unique-infinite-cluster assumption yields only lim_{L->infinity} lim_{M->infinity} q_{p_c}(L,M)=0. At fixed L the five anchors stabilize, but R grows with M/L. The numerical family q_fake(L,M)=1 below M=L2^L and 2^{-L} afterwards has this iterated limit while missing the threshold for every pair. Thus no diagonal choice follows from the available limit. Proving a bounded-aspect-ratio block error estimate would close G; neither peer has done so. A KEEP on L1–L5 is not a proof of G.

## Attempt against the strongest finite comparison

The newer cubic manuscript states Proposition 2.1: for independent labelled hyperedges on a finite hypergraph, with arbitrary weights in [0,1], node o, nonempty relay set A and target set T,

    P(o↔A and o↔T) >= P(o↔A) min_{a in A} P(a↔T).

This is load-bearing in the paper's different route. I independently rederived two preliminaries. First, for A={a}, the events {o↔a} and {a↔T} are increasing; Harris/FKG gives P(both)>=P(o↔a)P(a↔T), and both imply o↔T. Second, conditioning on an exact finite cluster C(S)=W tests internal and crossing hyperedges but tests no hyperedge disjoint from W. Exterior hyperedge bits therefore retain their independent product law. These checks do not establish the many-relay comparison.

A direct first-relay argument cannot simply apply FKG after selecting a relay. On o--a2--b--a1 with three independent fair edges, order A=(a1,a2). The event that a2 is the first reached relay has probability 3/8, while its intersection with {a2↔b} has probability 1/8, so the conditional connection is 1/3 although each relay-to-b marginal is 1/2. The global comparison is still equality. The manuscript's Lemma 2.2 supplies nonnegative inverse-column coefficients through a conditioned-cluster induction, and this is the hardest unverified step in my external-proof audit. I checked its exact-cluster conditioning setup and the algebraic use of the lemma in Proposition 2.1, but I have not independently rederived the full cone induction or the later adaptive-exploration argument. The manuscript remains a **reported proof**, not a proof certified by this packet.

NEXT: Have an independent referee examine the conditioned-cluster cone induction and the all-dimensions manuscript's final lattice deduction before changing the math-brain problem card from historically open to verified solved.
