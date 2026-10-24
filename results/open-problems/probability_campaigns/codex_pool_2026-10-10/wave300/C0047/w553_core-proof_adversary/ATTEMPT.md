# C0047 independent adversarial checkpoint (2026-10-10)

This checkpoint was written before reading any w552 proof. It is an independent derivation, not a resolution of C0047. Referee: w554; no independent KEEP yet. Served-model identity has not been verified.

The target is Bernoulli bond percolation on every Cayley graph Cay(Gamma,S), where Gamma is infinite and finitely generated and S is any finite symmetric generating set: pc < pu if and only if Gamma is nonamenable. The original Benjamini-Schramm 1996 paper states the broader quasi-transitive positive-Cheeger implication as Conjecture 6 (page 76). Its surrounding definitions use site percolation, so the bond version must be stated explicitly rather than silently attributed as the original model. The amenable converse follows from the established uniqueness theorem. Recent public openai/math result 214 claims a full bond result; current mathematical validation remains UNKNOWN pending its proof/assumption audit.

## Hardest input for this route

Let tau_p(x,y)=P_p(x is connected to y), and T_p its kernel on l2(V), with counting measure. The sufficient input is a finite graph-dependent bound M_G=||T_pc||_(2->2) for every nonamenable Cayley graph with its ORIGINAL generating set. This input is stronger than the target. Replacing S by a favorable larger generating set proves a different quantified statement. Nonamenability alone has not been turned into this bound here.

## Independent reduction: a quantitative sprinkling lemma

Suppose G is a countable simple graph of maximum degree D<infinity, 0<=p<1, and T_p is bounded on l2 with norm M. Set p'=p+(1-p)epsilon, where 0<=epsilon<1/(DM) (the edgeless case is immediate). Then

tau_p'(x,y) <= sum_{n>=0} epsilon^n [T_p (A T_p)^n](x,y),

and ||T_p'||_(2->2) <= M/(1-epsilon D M).

Proof: Couple p' percolation as the union of independent p-bonds and epsilon-bonds. Every connection has a finite simple witnessing path. Mark precisely its edges that are not p-open; these are distinct epsilon-open edges. Between successive marked edges are disjoint p-open path segments (zero-length segments are allowed). For fixed ordered oriented marked edges (a_i,b_i), apply the multi-event BK inequality to the p-segment connection events. Independence between the epsilon field and the entire p field then gives an upper bound epsilon^n tau_p(x,a_1) tau_p(b_1,a_2)...tau_p(b_n,y). This multiplication uses disjoint witnesses for BK; the segment events are not asserted to be independent. Sum over marked-edge sequences and drop the distinctness constraints to obtain the kernel series. Finite-volume exhaustion justifies BK for connection events using finite paths; monotone convergence handles the countable sums. ||A||<=D and epsilon D M<1 give norm convergence of the series. Entrywise domination by its nonnegative kernel bounds the operator on finitely supported f via |T_p'f|<=S|f|, and density extends it to l2.

Consequently, boundedness at pc<1 gives boundedness at p1=pc+(1-pc)/(2DM)>pc. Monotonicity of tau preserves boundedness for every q<=p1.

## Independent reduction: bounded kernel excludes uniqueness

On an infinite transitive graph, if there is almost surely exactly one infinite cluster and theta(p)>0, then tau_p(x,y)>=theta(p)^2 for every x,y. Indeed both increasing events {x connects to infinity} and {y connects to infinity} have probability theta(p), FKG bounds their intersection, and uniqueness puts x,y in the same cluster there. Thus T_p delta_x has infinitely many entries >=theta(p)^2 and cannot be in l2. On a quasi-transitive connected graph the same argument uses the positive minimum of theta over its finitely many vertex orbits.

Applying this at every q in (pc,p1] excludes uniqueness throughout that interval. For q<pc there is no infinite cluster. Uniqueness at q=pc would force bounded T_pc to be unbounded by the same argument (positive probability of existence gives positive theta on some orbit). Hence no q<=p1 belongs to the defining uniqueness set, and pu>=p1>pc. This threshold argument does not rely on an unjustified inference from nonuniqueness at one isolated p to an interval.

## Exact obstruction: exponential decay is insufficient for l2 boundedness

Let G be the 4-regular tree, a Cayley graph of the free group on two generators. For bond percolation, tau_p(o,x)=p^dist(o,x), since the connecting path is unique. There are 4*3^(n-1) vertices at distance n>=1. Therefore

sum_{dist(o,x)<=R} tau_p(o,x)^2 = 1 + 4 p^2 sum_{j=0}^{R-1}(3p^2)^j.

This diverges as R->infinity whenever p>=1/sqrt(3), even though tau_p decays exponentially in distance for EVERY p<1. At p=3/4 the sum is exactly 1+(36/11)*[(27/16)^R-1]. Thus pointwise exponential decay with an unspecified positive decay rate does not prove a finite l2 operator norm, even on a nonamenable Cayley graph. This does not disprove C0047 or the critical bound: pc=1/3 for this tree.

## Dependency control

For two simple paths on this tree that share L edges and have lengths m,n, their simultaneous openness probability is p^(m+n-L), while multiplying marginals gives p^(m+n). Shared edges forbid an independence shortcut. The sprinkling reduction above instead uses edge-disjoint BK witnesses and independent fields.

## A weaker target-aligned missing input

One does not need the stronger critical operator conjecture to finish the target. It suffices to establish, for each prescribed nonamenable Cayley graph, ONE p1>pc with inf_{x,y} tau_p1(x,y)=0. More concretely, a sequence of pairs with tau_p1(x_n,y_n)->0 suffices; uniform exponential decay at this strictly supercritical parameter would supply it.

Proof of the sufficient reduction: entrywise monotonicity gives inf_{x,y} tau_q(x,y)=0 for every q<=p1. Almost-sure uniqueness at any such q would give a strictly positive uniform lower bound on every entry by the preceding FKG argument, a contradiction. Thus no q<=p1 lies in the uniqueness set, and pu>=p1>pc. This uses monotonicity of the connectivity kernel, not a claim that the number of infinite clusters is monotone.

This is a weaker input than boundedness of T_p1: at p1=3/4 on the 4-regular tree the zero-infimum criterion holds while the l2 kernel is unbounded. Accordingly, O01 only refutes a decay-to-l2 inference; exponential connectivity decay at a strictly supercritical parameter IS enough for pc<pu. The unresolved target-aligned lemma is to produce those separated pairs above pc on every nonamenable Cayley graph in its original generating set. No such general derivation is established here.

NEXT: Audit the actual critical-operator step in w552's proof and the recent public claimed resolution; test whether it supplies a volume-uniform bound rather than pointwise decay, and send the exact reduction and obstruction to w554.
