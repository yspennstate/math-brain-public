# Completed terminal-inclusive optimization

This is a scoped continuation of the interrupted 20261012 stage, not a new universal candidate. TREE_TARGET.md is copied unchanged with its provenance hash. Its compensated physical-restriction identity gives, in bits,

    C(T;f)=sum_h w_h B_i(f_h)+E_leaf H(f_leaf)
          =H(f)-sum_h w_h JS_i(f_h),
    B_i=H(S_i|S_-i)=h2(Inf_i)-I_P(S_i;S_-i).

Physical children interfere through signed Fourier amplitudes; the JS here is the actual two-child mixture information. Completing a stopping leaf costs an additional B_i but removes H(parent)-average H(child)=B_i+JS_i from its terminal bill, so it decreases C by JS_i>=0. An optimum therefore exists among complete trees and satisfies the Bellman equation in TREE_TARGET. Every alternative is an actual coordinate query. Randomized policies cannot improve a minimum of deterministic policies. Under the established common spectral lift, this minimum is min_T H(S_root|transcript(T)). Constant physical leaves do not make this root posterior entropy vanish.

## All-dimensional point-defect optimum

Let f_m=1-2*1_{x=0} on m binary coordinates. Its spectrum has empty coefficient 1-a and every nonempty coefficient -a, a=2^(1-m). All queries are symmetric, with one constant child and one f_(m-1) child, up to coordinate names and signs. Thus every complete adaptive tree has the same cost. At an active m-node, pairing the spectral sets differing at the queried bit gives

    B_m=phi((1-a)^2,a^2)+(2^(m-1)-1)*2a^2,
    phi(x,y)=(x+y)log2(x+y)-x log2(x)-y log2(y),
    V_1=0,  V_m=B_m+V_(m-1)/2
             =sum_(j=2)^m 2^(-(m-j)) B_j.

Zero terms use 0 log 0=0. This formula proves the optimum for every integer m>=1, including stopping trees with their actual terminal entropy. Influence is I_m=m a_m. Dividing by a_m yields

    V_m/a_m=2(m-1)+sum_(j=2)^m [-2a_j+phi((1-a_j)^2,a_j^2)/a_j].

For m>=2, x=(1-a)^2, y=a^2, x+y<=1. The inequalities ln(1+y/x)<=y/x and phi>=0 give

    0<=phi(x,y)<=y log2(e/y),
    phi(x,y)/a<=a [2(j-1)+log2(e)].

Here x>0; m=1 was already separated. Since sum_(j>=2) a_j=1 and sum_(j>=2) (j-1)a_j=2, the negative terms give V_m/a_m>=2m-4, while the nonnegative upper summands 2(j-2)a_j+log2(e)a_j sum to 2+log2(e). Therefore, for all m>=1,

    2-4/m <= V_m/I_m <= 2+log2(e)/m,
    lim_(m->infinity) V_m/I_m=2.

This is an optimum of the assigned debt-minus-credit tree objective, not another proof of the already retired H(f_m)<=4I(f_m) calibration. check_and.py validates the finite log formula for m=1,...,16 and independently reconstructs all actual query debts and the optimum from full truth tables for m<=6. Its interval tests use the weaker rational upper bound 2+2/m; the sharper log2(e) coefficient comes from the displayed proof.

## Exact B05 roots and descendant order obstruction

Use the actual quadratic b(x)=(-1)^(x_0 x_1+...+x_(k-2)x_(k-1)), the point flip b'=b-2*1_0, and selector y choosing b when y=0 and b' when y=1. Set F=b_y when all r controls are zero and F=1 otherwise. The frozen roots are k=2,r=4 and k=4,r=8. The exhaustive D/P state and action classification, including the exceptional empty Fourier fiber, is proved in TREE_TARGET.md. Integer Walsh coefficients give exact probabilities with denominator 2^(2N), N=3k+1. Bellman cost coefficients have denominator 2^(3N).

The certificates list every descendant value, every alternative action gap, and rigorous prime-log intervals. Backward induction on remaining dimension proves every stored value is the true minimum: constants cost zero; the candidate is the actual B plus the mean certified child minima; every alternative gap is either the zero prime-log map or has strictly positive lower enclosure. Distinct prime-log maps cannot be exact zero, by unique factorization after exponentiation. No floating comparison chooses a query.

For k=2, the root's optimal orbit is control, I=19/64 and V/I is in [1.836014211380,1.836014211381]. For k=4, it is again uniquely control, I=141/4096 and V/I is in [1.956704604624,1.956704604625]. In both cases a policy querying remaining controls first, then following the optimum on the core, has exactly the same cost. These statements include the complete terminal account. They do not assert this root policy is optimal at every descendant.

Indeed, D(1,1,2,r) for each frozen r=4,5,6,7,8 has one intact quadratic pair, one singleton variable left by fixing a partner zero, and an unfixed selector. It is reached from the k=4 root by a zero data query and appropriate active control restrictions. In explicit coordinates its core is

    g(u,v,w,y)=(-1)^(u v)-2*1_{u=v=w=0,y=1}.

There are r all-zero activation controls. The only optimal physical query coordinates are u,v. A control query followed by optimal children has strictly larger cost, with certified gaps in bits respectively:

| r | control-query gap lower | control-query gap upper |
|---|---|---|
|4|0.000187542886|0.000187542887|
|5|0.000076488129|0.000076488130|
|6|0.000019161179|0.000019161180|
|7|0.000004792650|0.000004792651|
|8|0.000001198306|0.000001198307|

Exact coefficient maps and denominators are in INDEPENDENT_K4.json. Consequently a hereditary rule 'query controls while any remain' fails on actual descendants of this family, even though it minimizes the cost at the two certified original roots. No claim is made for r outside the frozen domain.

## Independent representation check and scope

verify_tree.py constructs every canonical state's full Boolean truth table from its sign formula, drops only physically irrelevant coordinates, and recursively examines every actual coordinate. Its Walsh implementation recursively separates even and odd truth entries, independently of the compressed solver's iterative transform and activated-spectrum formula. It uses neither the compressed transitions nor the compressed spectrum formulas. The common trusted component is the previously certified rational log helper and exact prime factorization arithmetic. The independent solver agrees with all 35 k=2 and 162 k=4 canonical values, and checks all saved log bounds. It reconstructs 32 and 165 full truth-function states, respectively, with 115 and 1167 actual-coordinate alternatives. Internal alternative implementation is not external independent review.

The all-m AND statement is analytic; B05 optimality is finite only. A097 already pays a control-first B05 reference-transfer class and has an all-even-k erasure bound: our finite optimality result does not replace or extend that class FEI result. A038's selector reserve and A097's compatible-reference kappa remain different accounts from this objective and from B08 queried-bit mutual information. The first unsupported universal line is V(f)<=K I(f) for every Boolean sign with one finite absolute K, or a paid transfer of prescribed leaf references through the same overlapping history. Neither follows from a root-optimal ordering or these exact finite certificates.
