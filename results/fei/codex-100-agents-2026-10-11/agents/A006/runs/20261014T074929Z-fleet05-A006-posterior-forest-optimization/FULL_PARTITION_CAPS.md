# Full partition star mass and incidence-aware joint certificate

Fix the original nonempty-root-conditioned queue, every positive width-two prime gate of the indicated graph, both endpoint orders, and globally fixed positive packing-feasible weights. All coefficients below include the selected-size, subset, child-count, multiset, chronological labels and root rarity. Cost C is the complete actual reference cross-entropy in bits, already minimized over distributions on DISTINCT actual partition runs. This is different from the surrogate forest residual R.

## Exact full partition formula, every star size

For f_m=x_0 AND OR(x_1,...,x_m), m>=2, label its edges by their leaves and put s=sum lambda_i<=1, D=product_i(1+lambda_i/4)-1. For a nonempty leaf subset B of size k, write lambda_B=product_(i in B)lambda_i and lambda_out=sum_(i not in B)lambda_i. Define

    a_k=(k-1)!/[3*8^k*k*(k+1)],
    b_k=k!/[16*8^k*(k+1)*(k+2)].

The COMPLETE full-partition numerator, not a selected-family lower mass, is

    W_B=lambda_B/32^k                     (hub absent),
    W_{0}=s/32,
    W_{0 union B}=lambda_B(a_k+b_k lambda_out).

Proof of exhaustiveness: each present leaf has a unique eligible owner, its own edge. If the hub is absent, the used edges have no ownership arcs and each is a root. If the hub is present, either an edge in B owns the pair, or an edge outside B owns the singleton hub. These exhaust every coordinate assignment. In either case the hub-owning edge is the unique source component, and every other used edge must be its direct child, connected through the hub. No additional parent choice is possible, since a singleton leaf owned by another edge is not in the child's support. For hub-only outputs each of the m possible singleton hub owners gives one root run.

For a pair owner there are k choices. Its root factor is lambda_i/4, its pair-subset factor 1/6, its child count factor 1/[k(k+1)], and its multiset factor 1/k. Each singleton child supplies lambda_j/8, including zero children. The (k-1)! different child sequences give DISTINCT chronological queue runs. Summing k owners gives a_k. A singleton hub owner outside B has root/subset factor lambda_i/16, child count 1/[(k+1)(k+2)], multiset factor one, and k! child sequences. This gives b_k. For a singleton isolated root the additional zero-child factor 1/2 yields lambda_i/32. Every run uniquely determines its owner blocks, roots and chronological child sequence; no abstract description is counted twice. Consequently Q_A=W_A/D is exactly the full partition output mass.

Normalizing the actual event probabilities within each A gives the optimizing posterior. The identity E_eta[-log q_run]-H(eta)=-log Q_A+KL(eta||q_run/Q_A) explicitly retains posterior witness entropy; no uniform description prior is substituted.

## Exact cardinality LP without restricting the physical infimum

At lambda_i=1/m put delta=4^-m, P_h=(1-2^-m)^2, v=1-delta and I=1+(m-1)2^-m. Every nonempty leaf-only or hub-plus-leaf set has spectral probability delta; only the hub singleton has P_h. These identities follow directly from f=x_0/2*(1+OR_m)+(OR_m-1)/2 in sign notation, or from the point-indicator expansion of OR_m. (Equivalently f=2*1[x_0=1]*(1-1[all leaves=-1])-1.)

Let K_AT be the coefficient of lambda_T in W_A divided by 4^-|T|, and h_T=sum_A P_A K_AT/Q_A. By leaf-permutation symmetry h_T depends only on t=|T|. The exact value is

    h_t=delta D (4m)^t
       +delta D 4^t m^t a_t/[a_t+b_t(m-t)/m]
       +t delta D 4^t m^(t-1) b_(t-1)/[a_(t-1)+b_(t-1)(m-t+1)/m], t>=2.

For t=1 replace the last line by 4 D P_h. The three lines correspond to leaf-only output, hub-plus-same-T output, and hub-plus-one-fewer-leaf output. The singleton-hub line is separate.

Every physical root law obeys p_lambda(T)<=u_t=4^(1-t)/t^t, since D>=s_T/4, product_T lambda_i<=(s_T/t)^t and s_T<=1. Define U_t=binom(m,t)u_t. The exact capped tangent LP is

    L=max sum_t h_t z_t,  z_t>=0, sum_t z_t=1, z_t<=U_t.

This cardinality reduction is EXACT for the relaxation: averaging any feasible p over leaf permutations preserves its objective and caps; conversely distributing z_t uniformly over all t-subsets lifts any feasible z. It does NOT assume that the optimizer of the physical all-weight problem is symmetric. The fixed uniform physical root law lies in this relaxation, and sum_T p_lambda(T)h_T=v. Sorting h_t and filling caps gives a rational optimal primal; if the last filled level has value theta, the dual value is theta+sum_t U_t max(h_t-theta,0). Their equality certifies the optimum exactly. Let Gamma_cap=L-v>=0.

The supporting inequality for G=-sum P ln Q is G(p)>=G(p0)+v-h dot p. Therefore, for the SAME full partition table/orders/family,

    C(lambda0)-Gamma_cap/ln2 <= inf_(all feasible positive lambda, all actual posteriors) C <= C(lambda0).

In particular the bit gap is <=2 Gamma_cap. Root coordinates are an algebraic reindexing of used-gate monomials; K is not asserted stochastic, and relaxed p need not define a physical queue.

## All-dimensional certificate payment on the full partition star family

Separate the singleton-hub contribution: it contributes at most 4 D P_h to h dot p since the total singleton-root mass is at most one. For all remaining nonnegative contributions, use p_T<=u_|T| and sum caps times gradient entries, even if that overcounts the total mass. Leaf-only and same-T hub outputs each contribute at most

    4 delta D sum_(k=1)^m binom(m,k)(m/k)^k
       <=4 delta D binom(2m,m).

Here binom(m,k)=product_(j=0)^(k-1)(m-j)/(k-j)>=(m/k)^k, and sum_k binom(m,k)^2=binom(2m,m). For the additional outside hub owners, with k<m, b_k/[a_k+b_k(m-k)/m]<=m/(m-k). Summing the m-k possible outside edges and using u_(k+1) bounds their contribution by

    4 delta D sum_(k=1)^(m-1) binom(m,k)(m/(k+1))^(k+1)
       <=4 delta D binom(2m,m-1).

The last inequality uses (m/t)^t<=binom(m,t) and the adjacent-binomial Vandermonde identity. Thus

    Gamma_cap<=4D[P_h+4^-m(2 binom(2m,m)+binom(2m,m-1))]-v.

For m>=2, c_m=4^-m binom(2m,m)<=3/8 since c_2=3/8 and c_(m+1)/c_m=(2m+1)/(2m+2)<1. The adjacent binomial is no larger. Also D=(1+1/(4m))^m-1<1/3: expand the binomial and bound each term by (1/4)^j, retaining strictness. Hence L<4/3*(1+9/8)=17/6, and v>=15/16. It follows that

    Gamma_cap<91/48,
    C(lambda0)-inf C <91/24 <=(91/24)I.

This is an all-m bound for a joint optimization CERTIFICATE, not an assertion of an optimal weight, a new FEI theorem for stars, or a universal graph payment. Stars were already influence-paid by a selected family; the new result closes the full-event-family and unbounded-size certificate quantifiers.

## Transferable incidence caps, arbitrary finite width-two graph

For any nonempty used/root-index subset T of k edges, let L_T be any certified upper bound on sum_(e in T) lambda_e under graph packing. A feasible nonnegative vertex-price vector y with y_u+y_v>=1 for every edge uv in T supplies L_T=sum_v y_v by summing the packing inequalities. Then, for ANY complete partition event family,

    p_lambda(T)<=min(1,4^(1-k) L_T^(k-1)/k^k).

Indeed D>=sum_T lambda/4, and AM-GM and the certified sum bound apply exactly as above. A feasible fractional matching whose sum equals L_T certifies the best such sum bound by weak duality; rational equality suffices. These caps depend only on physical root packing, not on which forests were selected. Applying the cap LP to h recomputed from the FULL family therefore provides a valid all-weight/all-posterior global certificate on shared/leafless graphs. Selected-family h cannot be substituted. Computing all root subsets can still be exponential.

## First unsupported line

The remaining universal C020/PI-J line is an influence-paid COMPLETE coding cost (or the forest-target surrogate with its retained constants) for every Boolean prime table. Even for arbitrary graph spectra, this stage does not prove C(lambda0)<=K I or Gamma_cap<=K I in all dimensions. A small optimization gap compares two costs and cannot pay either. NEXT is a full-family cap/occupation calculation at the first adjacent shared high-degree incidence, with actual spectral row probabilities and one full numerator; the cap interface now applies there without an invalid selected-family lower transfer.
