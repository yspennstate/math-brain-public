# C0048 independent route — w459

Recorded 2026-10-10 before reading any current core-lane proposed proof.

Provisional target: the nearest-neighbor ferromagnetic q-state Potts model on Z^d, integer q>=3, d>=3, has a discontinuous transition. Exact primary wording and which discontinuity (magnetization, energy, or both) must be recovered before treating this as the complete statement. Convention: Gibbs weight exp(beta sum_{<x,y>} 1{sigma_x=sigma_y}); FK p=1-exp(-beta).

Independent approach: use finite-volume relative entropy and the convex pressure as a bridge between ordered/disordered Gibbs states and an edge-density jump. Derive the bridge with explicit surface errors first. Then test whether a q>=3 entropy deficit or a local conditional identity can force distinct limiting energy slopes at criticality, without importing a contour expansion or taking a large-d/large-q limit. This approach does not assume that mean-field bistability survives finite dimension.

Hardest remaining gap at outset: prove, for every d>=3 and integer q>=3 including (d,q)=(3,3), two critical infinite-volume states whose nearest-neighbor agreement densities differ by a strictly positive amount. Convexity and a surface-order entropy bound alone do not supply that positive amount.

No openness or novelty claim yet. No peer proof has been read.

## Saved lemma L1: surface entropy bound (complete elementary proof; unreviewed)

Prior-attempt digest: C0048-A001 (2026-09-07) tried reflection positivity/chessboard/contour entropy, with an additional planar FK comparison. It recorded no result. Targeted ID/Potts searches found no separate H/I attempt. The Lean ranking has only attempted_un. Team O has no exact C0048 row. This route instead derives an entropy certificate and proves why product trial laws fail it. Basic finite-graph partition identities reused below are not critical FK coexistence computations.

Let G be a finite graph, Lambda its variable vertices, q>=2 integer, beta>=0, A(sigma) the number of agreeing edges internal to Lambda, and B_b(sigma) the number of agreeing edges from Lambda to a fixed exterior coloring b. Write m for the number of such crossing edges, gamma_f proportional to exp(beta A), and gamma_b proportional to exp(beta(A+B_b)). Then

    0 <= D(gamma_b || gamma_f) <= beta m,
    0 <= D(gamma_f || gamma_b) <= beta m.

Proof: 0<=B_b<=m, hence 0<=log Z_b-log Z_f<=beta m. The log density ratio is beta B_b-(log Z_b-log Z_f), so either relative entropy is at most beta m. Both are nonnegative by the log-sum inequality. For any mixture rho of the gamma_b, convexity of relative entropy in its first argument gives D(rho||gamma_f)<=beta m. Thus the marginal of any infinite-volume Potts DLR Gibbs state has this same bound. No independence of edges or spins was used.

For Lambda={1,...,n}^d: m=2d n^(d-1), so D(rho||gamma_f)/n^d <= 2d beta/n. This holds at every beta, not only a critical beta, and for every q>=2.

## Saved lemma L2: entropy-deficit certificate for an energy jump (complete proof; unreviewed)

Let P_n(t)=|Lambda_n|^(-1) log sum exp(t A_n), for growing boxes in a fixed nearest-neighbor integer-q Potts model. Assume P_n(t)->P(t) on an open interval containing beta_*. For each sign choose arbitrary probability laws rho_n^+ and rho_n^- (they need not be Gibbs). Put e_n^sign=E_rho A_n/|Lambda_n| and delta_n^sign=D(rho_n^sign||gamma_{n,beta_*}^f)/|Lambda_n|. If delta_n^sign->0, e_n^sign->e_sign, and e_+>e_-, then

    P'_+(beta_*) - P'_-(beta_*) >= e_+ - e_- > 0.

Proof: finite-volume Gibbs variational inequality log Z(t)>=S(rho)+t E_rho A, and its equality at gamma_{beta_*}, give P_n(beta_*+s)>=P_n(beta_*)+s e_n^sign-delta_n^sign for either sign and either sign of s. Taking n->infinity yields P(beta_*+s)>=P(beta_*)+s e_sign. For s>0 this implies P'_+(beta_*)>=e_sign; for s<0 it implies P'_-(beta_*)<=e_sign. Use plus on the first and minus on the second. Convexity ensures both one-sided derivatives exist. All limit orders are explicit: first n, then s->0.

The useful finite-volume version, for h>0, is

    [P_n(beta_*+h)-P_n(beta_*)]/h
      - [P_n(beta_*)-P_n(beta_*-h)]/h
    >= e_n^+ - e_n^- - (delta_n^+ + delta_n^-)/h.

L1 makes delta_n=O(1/n) for actual Gibbs marginals. It does not prove e_+>e_- or that beta_* is the critical point. Those are still missing. This certificate is a reduction, not a proof of C0048.

## Saved lemma L3: a product-law obstruction (complete elementary proof; unreviewed)

Let G=(V,E) be a finite simple graph with an induced matching of M edges: its selected endpoint pairs have no edges between distinct pairs. Let gamma_beta be the free, zero-field integer-q Potts law with unit bonds, beta>0, and let u be the uniform independent spin law. Then

    D(u || gamma_beta) >= M c_q(beta),
    c_q(beta) = log((exp(beta)+q-1)/q) - beta/q > 0.

Proof: write S for the selected endpoints and C=V\S. The chain rule for relative entropy, with the nonnegative C-marginal term discarded, gives

    D(u||gamma) >= E_{u_C} D(u_S || gamma(S|C)).

Conditioned on every spin in C, the Gibbs law on S factors over the selected pairs, because the induced-matching condition excludes every edge between distinct pairs. This is a derived conditional independence, not a product assumption on the full interacting model. A pair has law v(i,j)=exp(beta 1{i=j}+h_i+k_j)/Z(h,k), with fields produced by C. Its relative entropy against uniform product is

    D(u_pair||v)=log Z(h,k)-mean(h)-mean(k)-2 log q-beta/q.

The function log Z is convex in (h,k), and is invariant under simultaneous color permutations of h and k. Average over all color permutations and use Jensen: log Z(h,k)>=mean(h)+mean(k)+log(q(exp(beta)+q-1)). Substitute to obtain c_q(beta). Strict positivity follows from strict Jensen applied to exp(beta X), where X is Bernoulli(1/q), beta>0 and q>=2. Add the M conditional pair deficits.

On Lambda_n={1,...,n}^d, select pairs (x,x+e_1) with x_1=1,4,7,...<=n-1 and each x_j (j>=2) odd. Distinct pairs have no nearest-neighbor edge between them. Their number is ceil((n-1)/3)*ceil(n/2)^(d-1), and M/n^d->1/(3*2^(d-1)). Consequently

    liminf_n D(u_n||gamma_{n,beta})/n^d
      >= c_q(beta)/(3*2^(d-1)) > 0.

This rigorously excludes the uniform disordered product trial sequence from the vanishing-deficit hypothesis in L2 at every beta>0. In particular, mean-field coexistence cannot be inserted into L2 without controlling the extensive interaction/correlation correction.

Extension to any full-support independent one-site law pi: for a conditional pair v and two distinct colors i,j, v_ii v_jj/(v_ij v_ji)=exp(2 beta), whereas (pi_i pi_i)(pi_j pi_j)/(pi_i pi_j)^2=1. If a=(min_i pi_i)^2 and epsilon=TV(pi tensor pi,v)<a, each of these four cells differs by at most epsilon; hence exp(2 beta)<=((1+epsilon/a)/(1-epsilon/a))^2. Thus TV>=a tanh(beta/2), including epsilon>=a. Pinsker gives

    D(pi tensor pi || v) >= 2 (min pi)^4 tanh(beta/2)^2,
    liminf D(pi^Lambda_n||gamma_{n,beta})/n^d
      >= 2 (min pi)^4 tanh(beta/2)^2/(3*2^(d-1)) > 0.

The bound assumes full support; no conclusion from this formula is claimed when min pi=0. The uniform formula above is stronger in its case. These are supporting obstruction lemmas, not a discontinuity proof or a novelty claim.

## Saved lemma L4: sharper all-edge uniform obstruction (complete proof; unreviewed)

The uniform part of L3 improves to

    D(u || gamma_beta^free) >= |E| c_q(beta)

on every finite simple graph for integer q>=2 and beta>=0. Put v=exp(beta)-1>=0. Expand each factor exp(beta 1{sigma_x=sigma_y})=1+v 1{sigma_x=sigma_y}, then sum colors:

    Z_G(beta)=sum_{A subset E} v^|A| q^k(A),

where k(A) counts components including isolated vertices. Each added edge reduces k by at most one, so k(A)>=|V|-|A| and (q>=1)

    Z_G(beta)>=q^|V| (1+v/q)^|E|.

Since D(u||gamma)=log Z_G-|V| log q-beta |E|/q, subtraction gives the bound. This uses an exact expansion and a termwise inequality, not independence of edge agreements. Equality holds for forests; if G has a cycle, q>1 and beta>0, at least one subset has a strict termwise inequality, so the entropy bound is strict.

For lattice boxes |E|/|V|->d, therefore the limiting uniform-product entropy deficit is at least d c_q(beta)>0. At the mean-field coexistence value

    beta_MF=(q-1) log(q-1)/(d(q-2)), q>=3,

the uniform product law and the ordered product law with pi_1=(q-1)/q and pi_i=1/(q(q-1)) for i>1 have identical limiting variational score S(pi)+beta_MF*d*sum pi_i^2. Indeed their entropy difference is -(q-2)log(q-1)/q and their sum-of-squares difference is (q-2)^2/(q(q-1)). Their relative entropy deficits per vertex therefore have the same positive limit, bounded below by d c_q(beta_MF). Neither qualifies as a vanishing-deficit trial law for L2. This closes a specific false shortcut in this independent proof attempt, not the C0048 gap.

Pressure existence used in this last limit is elementary here. For beta>=0, tile an n-box by disjoint L-boxes plus leftover single vertices. Removing crossing edges changes log Z by a number between 0 and beta times the number removed. That number of edges is at most d*n^d/L+O(n^(d-1)*L); leftover volume is O(n^(d-1)*L). Fix L and let n grow: liminf P_n>=P_L and limsup P_n<=P_L+beta*d/L. Thus limsup P_n-liminf P_n<=beta*d/L for every L, giving existence as L tends to infinity. The expected internal agreement per vertex under a fixed product pi converges to d*sum pi_i^2, and its entropy per vertex is S(pi). The exact relative entropy identity then justifies both product-deficit limits.

Final checkpoint: the fresh resource gate refused numerical enumeration, and no numerical pass is asserted. Complete analytic proofs are frozen for independent review. The hardest target-specific piece remains constructing correlated critical trial laws with zero entropy deficit per vertex and a strictly positive limiting energy separation for q=d=3 (then for all q>=3,d>=3).
