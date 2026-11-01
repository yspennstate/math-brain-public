C0047 independent boundary derivation — w559, 2026-10-10

This derivation was saved before reading w558's proof. It is an author proof of a special case and a counterexample to a stronger auxiliary inequality, pending independent review by w560. No novelty or full-conjecture claim is made.

The precise target is Bernoulli bond percolation on G = Cay(Gamma,S), where Gamma is an infinite finitely generated nonamenable group and S is an arbitrary prescribed finite symmetric generating set, with the identity omitted and repeated edges identified. The target is p_c(G) < p_u(G) for every such S. Here p_c = inf{p: P_p(|C(o)|=infinity)>0} and p_u = inf{p: P_p(exactly one infinite cluster)=1}. The amenable direction is the known uniqueness implication. The original 1996 paper discusses site percolation and explicitly transfers its nonplanar results/questions to bond percolation; Conjecture 6 is the broader locally finite connected almost-transitive positive-Cheeger statement. The current full-result status is UNKNOWN: a September 2026 public paper advertises a solution, and its linked comparator file contains admitted placeholders rather than a check receipt. This observation does not assess the underlying paper's proof.

Independent special case

Let Gamma = C_2 * C_3 = <a,b | a^2=b^3=1>, S={a,b,b^{-1}}, and let G be its simple undirected Cayley graph. G has degree 3. The b-edges form disjoint triangles, and every vertex has one a-edge. Contracting each triangle gives the 3-regular tree: free-product normal forms rule out any cycle of distinct triangle blocks. Each a-edge is therefore a bridge. This block-tree geometry is the essential extra premise used below.

1. Nonamenability with an exact edge expansion constant.
For a finite nonempty vertex set F, put N=|F|, c=the number of components of G[F], and t=the number of full triangles in F. Every cycle of G[F] is a triangle, and these triangles are disjoint, so |E(G[F])|=N-c+t and t<=N/3. Consequently |partial_E F|=3N-2|E(G[F])|=N+2c-2t >= N/3+2c. Thus h_E=inf_F |partial_E F|/|F| >=1/3. Conversely take all 3k vertices of any connected k-block subtree. Its boundary consists of k+2 a-edges, giving ratio (k+2)/(3k) ->1/3. Hence h_E=1/3; normalized conductance is h_E/3=1/9. The vertex Cheeger constant is at least h_E/3=1/9, so this is a nonamenable Cayley graph.

2. Exact branching reduction, with the independence premise explicit.
Enter a triangle at a vertex through its parent a-edge. Let K be the number (0,1,2) of the other two triangle vertices connected to the entry by open triangle edges. For each of the K vertices test its outward a-edge, and let X be the number of open outward edges. Conditional on K, X is Binomial(K,p). Direct triangle connectivity gives P(K=0)=(1-p)^2, P(K=1)=2p(1-p)^2, P(K=2)=3p^2-2p^3. In particular E K=2(p+p^2-p^3), E X=M(p)=2p^2+2p^3-2p^4, and P(X=2)=D(p)=3p^4-2p^5.

Different processed triangles and their two outward bridges use disjoint edge sets. The contracted graph is a tree, so different offspring lead to disjoint untouched descendant blocks. Thus the reproduction variables really are iid; no product of dependent triangle-connection events is used. The forward cluster is exactly a Galton-Watson process with offspring X. The root has at most three outward edges; this finite initial modification changes neither the threshold nor critical extinction. At p<=q all forward trees die out, and each fixed root cluster is finite almost surely; countability excludes any infinite cluster anywhere. At p>q a root has positive probability of reaching a surviving forward tree. Therefore p_c=q, the unique root in (0,1) of M(q)=1, equivalently 2q^4-2q^3-2q^2+1=0.

Uniqueness of the root follows from M'(p)=2p(2+3p-4p^2)>0 on (0,1); the parenthesis is a concave polynomial with endpoint values 2 and 1. M(1/2)=5/8<1, M(2/3)=88/81>1. The sharper rational bracket M(63/100)=0.97883478<1<M(64/100)=1.00794368 gives 0.63<q<0.64. Critical extinction follows from the nondegenerate bounded-offspring critical branching process (P(X=0)>0 and P(X=2)>0).

The quadratic offspring generating function also gives the exact forward survival probability s(p)=(M(p)-1)/D(p) when q<p<=1. Indeed its fixed-point roots are 1 and P(X=0)/P(X=2). At p=2/3, D=80/243, M-1=21/243, and s=21/80.

3. Exact uniqueness threshold and all boundary values.
Fix q<p<1 and a deterministic ray in the contracted tree. At every interior block of the ray choose its off-ray branch. These branch half-graphs are disjoint. The event that its attaching a-edge is closed and its forward root survives has probability (1-p)s(p)>0. These events depend on pairwise disjoint edge sets and are independent. Infinitely many occur almost surely: the probability that none occurs after a fixed index is lim_n (1-(1-p)s(p))^n=0, and take a countable union over the index. Each occurrence supplies an infinite open cluster separated from every other selected branch by its closed bridge. Thus infinitely many infinite clusters exist almost surely for every fixed p in (q,1). At p<=q none exists; at p=1 the entire connected graph is open and is the unique infinite cluster. Hence p_u=1 and p_c=q<p_u. At p=2/3 the independent isolated-branch event has exact probability 7/80.

4. Counterexample to the universal spectral bridge and to a reversed tree bound.
Let A be the adjacency operator and rho=||A||/3 the simple-random-walk spectral radius. A vector equal to 1 on one triangle and 0 elsewhere has Rayleigh quotient <f,Af>/<f,f>=6/3=2. Hence ||A||>=2 and 3 rho p_c=||A|| q>=2q>1.26>1. This nonamenable Cayley graph has p_c<p_u but fails the sufficient Benjamini-Schramm criterion 3 rho p_c<1. Nonamenability alone therefore cannot imply that criterion for the prescribed generating set. The inequality p_c<=1/(degree-1) is also false here: q>1/2. The usual universal tree comparison runs in the opposite direction.

The 2026-09-07 C0047-A001 intake attempt mistakenly writes the criterion as p_c<1/rho with rho the simple-random-walk spectral radius. For nonamenable graphs rho<1 and p_c<=1, so that displayed condition is automatic and loses the factor degree. Benjamini-Schramm 1996, Theorem 4, p.76, uses rho(G) k p<1; Juschenko-Nagnibeda 2015, Theorem 2, records rho(Gamma,S) p_c(Gamma,S)|S|<1. The present example independently proves that repairing the normalization leaves a genuinely stronger hypothesis, which is not a universal consequence of nonamenability.

Hardest remaining piece

To solve C0047 by this route, show nonuniqueness near p_c for an arbitrary prescribed Cayley graph without assuming a block tree, finite bridge separators, or ||A||p_c<1. The branching and separated-branch arguments above rely on bridges and are unavailable on a general one-ended Cayley graph. A counterexample to the spectral bridge is not a refutation of C0047.

Primary sources

- Benjamini and Schramm (1996), Percolation Beyond Z^d, Many Questions And a Few Answers, sections 2 and 4, Conjecture 6 and Theorem 4: https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/978/978-3321-1-PB.pdf
- Juschenko and Nagnibeda (2015), Small spectral radius and percolation constants on non-amenable Cayley graphs, Conjecture 1, Theorems 2 and 4: https://arxiv.org/html/1206.2183v3
- Local prior attempt: ~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl, line 37, C0047-A001.
- Recall timed out at 60 seconds; the named fallback scar perceptron_proof_open_gaps_fleet_2026_07_12 was read directly. It requires checking the hardest proof gap instead of treating a completion banner as proof.

NEXT: Give this independently saved block-tree derivation to w560, then read w558's proof and audit its principal bridge with this explicit example.
