# C021 v1: Poisson Palm kernel retaining both boundary histories

Status: proof (unaudited), auxiliary identity for target 3. This specifies an ideal tree kernel; it is not yet a conditional law for finite G(n,c/n).

Let H be a finite history alphabet, Q a probability law on H, and ell:H->{0,1,2,3} a terminal-message map. Let Psi map finite multisets of H deterministically to H. Assume that Psi is the desired history update, including any deterministic initial message. Write N for a Poisson multiset with independent counts of means c Q_z, and P_d=Pr(Psi(N)=d). Only types with P_d>0 are used. Let M be the monotone terminal-message update from C005. Write ell(N) for the multiset of terminal messages of N.

A parent type is (A,b,d), where A in H is the incoming boundary history, a=ell(A), 0<=b<a, and d is the outgoing reverse history. Its other incoming histories have law N conditional on Psi(N)=d. For each occurrence z in N, remove that occurrence to obtain N-z. Define

    A' = Psi(N-z+{A}),
    u  = M(ell(N-z)+{a}),
    v  = M(ell(N-z)+{b}).

If u>v, that occurrence produces a child of type (A',u,v,z). Here the child type explicitly includes both its incoming parent history A' and the updated terminal pair (u,v). The incoming history's own terminal value need not equal u: u and v are the two fresh updates being compared. Thus for a closed type space use the general type (A,a,b,d), with a>b, rather than requiring a=ell(A) at every subsequent step. For a general parent (A,a,b,d), use A in the history formula and a,b in the two terminal formulas. Initial compatible types can impose a=ell(A); invariance of that compatibility is a separate statement and is not presumed.

For the general type space, the column mean is exactly

 T_H[(A',u,v,z),(A,a,b,d)]
   = c Q_z/P_d * Pr(
         Psi(N+{z})=d,
         Psi(N+{A})=A',
         M(ell(N)+{a})=u,
         M(ell(N)+{b})=v).

Proof. For any nonnegative function f of a residual multiset, the Poisson identity is

    E[N_z f(N-z)] = c Q_z E[f(N)].

It follows by shifting the absolutely convergent nonnegative Poisson series in its z coordinate. In the definition of a child, multiply the corresponding indicator by 1{Psi(N)=d}, sum over occurrences of z, and divide by P_d. Applying the identity gives precisely the four conditions displayed above. No independence of sibling counts is asserted or needed for this mean identity. Counts are unbounded, but all their first moments are finite, and the calculation uses no numerical truncation.

The formula is consistent with the stationary C009 mean: if histories are just terminal states, Psi=M, and compatible parent histories A=a, then the event A'=u is automatic. The child has compatible incoming history u. Summing over A' gives C009's matrix with P_d in its denominator; at a fixed point P_d=pi_d. This consistency check does not justify deleting A' from general full-history types.

For actual length-t histories started from top, Psi appends the deterministic initial state followed by updates of the previous time coordinates; hence the terminal Psi uses incoming time t-1, while the fresh terminal comparison uses time t. This is the reason the compatibility gate above is explicit. Unstable baseline outputs must be seeded or charged before identifying these ideal responses with actual message changes.

Relation to the primary source: Cooley--Lee--Ravelomanana, arXiv:2111.15577, Definition 3.4, PDF pp8-9, generates independent vertex in-compilations and matches full story pairs, not terminal states alone. Proposition 7.6, PDF p25, is the comparison point that a finite-graph application must justify. This identity concerns the ideal Poisson template law before matching; it does not prove that a vertex sampled adaptively from the matched finite graph has that conditional law.

Remaining obligations: (i) choose compatible, baseline-consistent types that actually represent monotone late changes; (ii) prove subcriticality of their full-history kernel or an integrable weighted refinement, rather than assume it from terminal marginals; (iii) supply finite-history inventory and conditional matching bounds, and exceptional/multiple-hit budgets. C020 applies only once its conditional sampling hypotheses hold.
