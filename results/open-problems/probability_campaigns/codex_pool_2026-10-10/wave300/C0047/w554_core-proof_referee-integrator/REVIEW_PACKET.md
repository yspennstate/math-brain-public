# C0047 referee packet — 2026-10-10

Scope: Bernoulli bond percolation on a fixed infinite, locally finite Cayley graph. These are checks of the named peer lemmas, not a proof of C0047. Reviewer: w554. Final served-model identity is unavailable in this session; no GPT-6 Sol identity is asserted. A separate model/account gate remains for final promotion.

## Source and current status

Benjamini–Schramm (1996), *Percolation Beyond Z^d*, Conjecture 6, p. 76, states the positive-Cheeger implication for connected almost transitive graphs. Definitions on pp. 72–73 use site percolation, and the authors say that the nonplanar questions also apply to bond percolation. The assigned C0047 bond/Cayley form is a specialization, with the amenable converse known. [Original paper](https://emis.de/ft/41630), PDF lines 50–89 and 255–276.

The 2026-09-07 intake calls current resolution unverified. A September 24, 2026 [paper](https://github.com/openai/math/blob/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf) claims a full bond result (Theorem 1.1 and Corollary 1.2). Local copy SHA256: `46A78D044D2713E48CB3FAA9B0B9D22DA9480193E2202FE63D8E0DAA7D8A3DBB`. Its accompanying comparator statements in `BenjaminiSchramm.lean` and `CayleyPercolation.lean` end with `sorry`. This is not a formal proof receipt for the displayed theorems; the paper remains mathematically unaudited here. **Current open status: UNKNOWN.**

## Peer verdicts

| Peer row | Verdict | Reproduction and scope | Unresolved input |
|---|---|---|---|
| w552 L1 | KEEP | For each configuration on finite F, the connectivity matrix is a sum of cluster indicator outer products, hence positive semidefinite. Along an induced finite exhaustion every finite open connecting path eventually occurs, so entries converge upward. Uniform finite norms bound all finite-support quadratic forms. Conversely, finite connectivity is entrywise below full connectivity; taking absolute values of test vectors bounds each finite norm by the full norm. | No gap in this lemma. It supplies no uniform critical bound. |
| w552 L2 | KEEP | Russo's formula on F gives a pivotal sum. With pivotal edge e removed, the x-to-u and v-to-y connections occur in disjoint components and have edge-disjoint witnesses. BK gives the two endpoint products. The finite positive connectivity matrix has a positive simple Perron eigenvector for 0<p<1; applying the entrywise derivative bound to that vector gives m'≤αm². Integrating (1/m)'≥−α yields the stated denominator. No extra 1/(1−p) is needed in this formulation. | No gap in the finite graph lemma. It cannot bound m_F(p_c) uniformly in F. |
| w552 L3 | KEEP, conditional | Set η=min((1−p_c)/2,1/(2αM)). L2 gives all finite norms ≤2M up to p_c+η and L1 passes to the full kernel. If a unique infinite cluster existed almost surely, FKG gives τ_p(x,y)≥θ_p² on a transitive graph; unit vectors on n vertices then have quadratic form ≥nθ_p², contradicting boundedness. This excludes every p≤p_c+η from the uniqueness set, so p_u≥p_c+η. | The hypothesis M=sup_F||T^F_pc||<∞ is strictly stronger than C0047 and is unproved in this packet. |
| w552 CORR1 | KEEP | For SRW P=A/d on a nonamenable d-regular Cayley graph, ρ=||P||<1, so p_c<1/ρ is automatic when p_c<1. The path-sum norm condition is p_c||A||=p_c dρ<1. On the 3-regular tree p_c=1/2 and ||A||=2√2, giving √2>1, while the critical kernel is bounded. The 1996 Theorem 4 explicitly includes the degree factor k in kρp. | Sufficient spectral regime only; not a route for all Cayley graphs. |
| w553 L01 | KEEP, conditional | In the independent p/ε union coupling, mark p-closed edges on a finite simple p'-open witness. The intervening p-open segments have edge-disjoint witnesses, so multievent BK bounds their joint probability; ε edges are independent of the p field. Sum over marked edge sequences to obtain ∑ ε^n T_p(AT_p)^n, whose norm is ≤M/(1−εDM). A bounded kernel excludes unique infinite clusters by FKG and positive θ. | This proves only `bounded T_pc ⇒ p_c<p_u`; no general critical bound is supplied. |
| w553 O01 | KEEP | On the 4-regular tree, τ_p(o,x)=p^dist and sphere n has 4·3^(n−1) vertices. The squared row through radius R is 1+4p²∑_{j=0}^{R−1}(3p²)^j. At p=3/4 this is 1+(36/11)((27/16)^R−1), so pointwise exponential decay does not imply an ℓ² row. | This does not challenge boundedness at p_c=1/3 or C0047 itself. |
| w553 S01 and w552 source checkpoint | KEEP as status cautions | Both correctly refuse to infer current openness or proof validity from the dated ranking. The recent claimed result strengthens the need for a specific mathematical audit. | Verify the recent paper or independent final proof before any solved/retired label. |

## The load-bearing open input

The peer reductions agree: a graph-dependent bound on the **infinite-volume critical connection operator** for every fixed nonamenable Cayley graph would imply C0047. No such bound is proved by the peers. The recent claimed paper puts its hardest new work in Section 4, especially Lemma 4.8's second-moment estimate for a switched endpoint load. Its disjoint nonadjacent case depends on joint injectivity of two inverse switching codes (paper pp. 24–25, extracted lines 1538–1623). I checked that the next truncation step follows algebraically from its asserted E[L²]≤Q u^(2k) and E[L]≥c u^k: at threshold b=CQ u^k, E[L 1_{L>b}]≤E[L²]/b≤u^k/C≤E[L]/4 for C≥4/c. This does **not** check the joint injection or establish the second-moment bound. That exact input is the next adversarial target.

## Reproduction sources

- w552: `~/brain_workers/w552/ATTEMPT.md`, rows `w552-C0047-L1`, `L2`, `L3`, `CORR1`.
- w553: `~/brain_workers/w553/ATTEMPT.md`, rows `C0047-w553-L01`, `O01`.
- Original Theorem 4 (site model; kρp criterion): [1996 paper](https://emis.de/ft/41630), PDF p. 76–77, lines 272–276.
- Claimed 2026 paper: `claimed_2026_paper.pdf` and extracted text in this folder. Read exact PDF mathematical symbols when auditing; `pdftotext` drops subscripts and inequalities.

NEXT: Independently reconstruct the joint inverse-code injection in the claimed paper's Lemma 4.8; test every dependency on the restored root cluster and the fixed seeds.
