# P0340: deterministic core (proof, pending w347)

Let T be a finite rooted full binary tree. Let n(T) be its number of leaves, h(T) its height in edges, D(T) the sum of the depths of its leaves, and l(T) the minimal drawn length defined by l(leaf)=0 and l(T)=l(L)+l(R)+2+|h(L)-h(R)|. Write S(T)=sum_{v internal} h(T_v).

Then l(T)=S(T)+h(T) and 2(n(T)-1)<=l(T)<=D(T).

Proof. For a leaf all quantities are zero except n=1. At an internal root, h(T)=1+max(h(L),h(R)), so 2h(T)-h(L)-h(R)=2+|h(L)-h(R)|. Substituting the inductive identities into S(T)+h(T) proves the identity. The lower bound follows by summing the increment at least 2 over the n-1 internal vertices. Every full binary tree with k leaves has height at most k-1, by induction on its two children. Hence 2+|h(L)-h(R)|<=n(L)+n(R); combined with D(T)=D(L)+D(R)+n(L)+n(R), induction proves the upper bound.

Checks to run: enumerate all ordered full binary trees with up to 10 leaves; check the identity, both inequalities, height convention, the singleton, balanced trees, and combs. A numerical check is supplementary to this induction.

Scope. This is a deterministic lemma. To refute an expected n(log n)^4 rate it suffices additionally to verify the source's expected leaf-depth O((log n)^2) theorem. This lemma alone does not prove E[l(T_n)]=Theta(n). A linear upper bound needs an additional expected-clade-height estimate and a summable clade-size bound.

Prior-work lead: aldous_janson_op14_drawn_length_is_linear_not_n_log4_2026_09_08. The saved memory contains the recursion and an existing Lean-check claim. Both source correspondence and the formal-check receipt will be checked independently in this pass.

## Linear-expectation argument checked against the earlier proof

The prior campaign proof supplies the full linear-limit argument, not just the leaf-depth inequality. The load-bearing estimates can be proved as follows, with a tighter geometric exponential moment.

The split law is q_m(i)=m/[2 H_{m-1} i(m-i)], where H denotes a harmonic number. A uniformly tagged leaf has next-clade size j with probability 1/[H_{m-1}(m-j)]. Its conditional probability of halving the clade size is at least 1/(2 H_{m-1}). For a chain started at n, put p_n=1/(2 H_{n-1}) and b_n=ceil(log_2 n). Couple successful halvings from below by independent Bernoulli(p_n) trials. Every tagged leaf depth is dominated by the waiting time for b_n successes, a sum of b_n geometric(p_n) variables on {1,2,...}.

Set theta_n=-log(1-p_n/2). The geometric moment is exactly E exp(theta_n G)=2. A union bound in exponential-moment form over n leaf depths, followed by Jensen, gives

E height(T_n) <= [log n+b_n log 2]/theta_n <= 4 H_{n-1}[2 log n+log 2] = O((log n)^2).

No independence among leaves is used: pointwise exp(theta_n h(T_n)) is at most the sum of exp(theta_n d) over its leaves, whose expected sum is n times the moment of a uniformly tagged leaf. Thus E exp(theta_n h(T_n))<=n 2^b_n before applying Jensen. Compared with the earlier proof's moment bound 3 and integrated tail, this removes its extra factor and integration term.

Let a(n,m) be the probability the tagged descent chain visits m. In a dyadic block (b,2b], each step exits the block with conditional probability at least 1/(2 H_{2b-1}), and the chain never returns. Consequently sum_{m=b+1}^{2b} a(n,m)<=2 H_{2b-1}, uniformly in n. If h_m=E height(T_m), the block sum of a(n,m)h_m/m is at most C(1+log b)^3/b. Summing over dyadic b proves a uniform vanishing tail.

The Markov branching property and the exact clade identity E N_n(m)=n a(n,m)/m give E drawn(T_n)/n=sum_{m=2}^n a(n,m) h_m/m+h_n/n. The established pointwise occupation limit a(n,m)->a(m)=6 H_{m-1}/[pi^2(m-1)], finite-sum convergence, the uniform tail bound, and h_n/n->0 prove

E drawn(T_n)/n -> c=sum_{m=2}^infinity a(m)h_m/m, with 2<=c<infinity.

This is an author-checked proof candidate continuing the prior work. It requires audit of the source split law, pointwise occupation limit and subtree branching identity. The stochastic argument is not Lean-checked in this pass. The finite-tree theorem has an older Lean file; the current lean_check.py run returned SETUP_UNVERIFIED because the compute governor reports distress.
