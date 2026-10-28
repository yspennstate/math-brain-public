# Several edits: preserve their phase signatures

All entropies and cross-entropies below use bits. Let E=F_2^n label physical vertices and frequencies using the usual dot product. Let g be Boolean, with Fourier support in a supplied linear subspace V of E. Flip g on a set D={a_1,...,a_k} of distinct vertices to obtain the actual Boolean f. Empty D is permitted. Set W=span{a_j+a_1:2<=j<=k}; when k<=1 set W={0}. Put r=dim W<=k-1 for nonempty D. Neither V nor W is assumed coordinate-aligned.

Let G consist of all invertible linear maps T:E->E with T v=v for v in V and <T s,w>=<s,w> for all s in E,w in W. The G-orbits are the singleton frequencies in V and the nonempty cells

    C_z={s outside V: (<s,w_1>,...,<s,w_r>)=z}.

Here w_1,...,w_r is any basis of W. In particular there are at most 2^r outside profile cells, in addition to |V| singleton labels. This count is an algebraic profile count, not a paid code length or an influence bound.

Proof of the orbit assertion. Necessity follows from the definition. Given u,v outside V in the same cell, put d=u+v. Then d annihilates W. If d=0 use identity. Otherwise u is not in V+span(d): if u=a+d with a in V then v=a is in V. Thus there is a linear functional l with l(V)=0,l(d)=0,l(u)=1 (extend a basis). The map T(s)=s+l(s)d fixes V, preserves the W evaluations, sends u to v, and satisfies T^2=Id. This proves sufficiency, including V={0}, W={0}, empty cells, and cells of size one.

For s outside V, Fourier inversion gives

    fhat(s)=-2^(1-n) sum_j g(a_j)(-1)^<s,a_j>.

Factoring (-1)^<s,a_1> shows that p(s)=fhat(s)^2 depends only on the W signature. Therefore the ACTUAL squared spectrum is G-invariant, including the fixed core atoms. For any normalized current reference Q that is positive on supp(p), its G-average Qbar has complete invoice

    CE(p,Qbar)-CE(p,Q)
      = -sum_C p(C) D_KL(U_C || Q(.|C)) <= 0.

Only outside cells occur in this sum. Cells of zero actual mass contribute zero; positive-mass cells have Q(C)>0 and Q(s)>0 throughout the cell, because p is uniform and positive there. Jensen's inequality for log, on each finite cell, proves the formula and sign. Core masses and every cell mass are retained. No vacuum calibration, ghost deletion, source replacement from scratch, or new influence grant is used.

Physical heredity. At an arbitrary partial physical assignment alpha, surviving edits are precisely D intersect that face, projected onto the remaining coordinates. They remain distinct. The clean restriction g_alpha has Fourier support in pi_alpha(V): restriction sums coefficients over frequency fibers, so it cannot create frequencies outside this projection. The restricted Boolean f_alpha is exactly g_alpha with those surviving points flipped. Repeating the preceding construction with the actual surviving edit differences proves the same nonpositive current-reference invoice at EVERY node of EVERY adaptive physical tree. Use the actual surviving set: projecting differences from an edit that did not survive need not give the sharp minimal signature space. Using the larger projected original W is still valid, but may preserve unnecessary cells.

SAME original owner. Fix original A, all prior signed bookings U, any reach weights lambda_alpha, and the actual current full references Q_alpha. If the currently available amount is A-U-sum lambda_alpha CE(p_alpha,Q_alpha), conversion changes it by exactly minus the weighted invoices, hence cannot decrease it. Retain all full terminal references and all old bookings. A negative invoice is released once; it cannot be counted a second time at a descendant. This pays conversions only, not any K*Inf query bill, any initial core source, or a mandatory policy.

One-edit specialization and two-edit guard. For k<=1, W=0 and the outside is one orbit: this reconstructs the mathematical core of A068@3. For a two-edit dictator on three bits, unrefined V-only averaging costs 3/4 bits (the source Q=P control from A068). Adding the one difference functional separates the interference classes; p is constant on each class and Q=P is unchanged, so the new invoice is exactly zero. The changed group, rather than a new budget, removes that particular failure.

The first unpaid universal line is a useful proper V and a bounded-complexity phase-signature profile whose ORIGINAL complete source is O(I(f)), together with payment of a necessary physical query from the SAME remaining amount. Taking V=E or W=E makes the return identity and supplies no universal progress. An arbitrary Boolean function may require a full-rank W (or exponentially many edits). Thus the profile count alone proves no FEI bound.

Connection to the semigroup. With L chi_S=|S|chi_S, define J_f(t)=sum_{S nonempty}|S|p(S)e^(-2t|S|)ln(1/p(S)), with 0 ln(1/0)=0. Direct integration of this FINITE nonnegative sum yields 2 integral_0^infty J_f=ln(2)H(f)-p(empty)ln(1/p(empty)). For a fixed finite f, J_f(t)<=J_f(0) for t near zero and J_f(t)<=e^(-2t)J_f(0) for all t>=0, so both endpoints are integrable, including constant f. The source conversions above leave f and its heat integral unchanged; their released KL is a source correction, not heat dissipation. A universal integrated influence payment remains open. No interchange of a supremum over functions with time integration is made.

Rung: written proof, pending the recorded exact finite checks and independent review; no full-FEI conclusion and no full theorem Lean certification.
