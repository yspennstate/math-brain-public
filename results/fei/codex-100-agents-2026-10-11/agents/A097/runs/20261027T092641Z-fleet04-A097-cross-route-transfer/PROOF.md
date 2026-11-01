# Affine moment calibration pays its complete fee; moments do not pay a query

All entropies, cross entropies and divergences are in bits. Full FEI remains open.

## 1. A096's calibration identity, with a direct finite proof

Let p be a probability law on a finite set, q a normalized reference covering p, and A the intersection of the probability simplex with closed affine moment equalities satisfied by p. Let u minimize D(v||q) over v in A with support contained in supp(q). The feasible set is compact and nonempty; D is continuous there, so a minimizer exists. Strict convexity gives a unique minimizing law.

Every atom positive under p is positive under u. Otherwise mix u with p by a small positive t: the new positive atoms contribute a negative multiple of t log(1/t), while changes at positive u atoms are O(t). This decreases the objective, a contradiction. This argument also shows that u contains the support of any feasible law. Zeros of q may be omitted because p and all finite-divergence feasible laws vanish there.

The direction p-u is feasible with both signs for sufficiently small t, since p vanishes wherever u vanishes and there are finitely many positive u atoms. Differentiate D(u+t(p-u)||q) at zero. The derivative is zero, so

    sum_s (p_s-u_s) log2(u_s/q_s) = 0.

The constant derivative term cancels by normalization. Therefore

    D(p||q)-D(p||u) = D(u||q).                         (1)

All summands are finite on their relevant support. No limit is interchanged with an infinite sum. For a subprobability reference Q=s q, 0<s<=1, replace it by s u: the entire scalar penalty -log2(s) remains, and the CE decrease is still D(u||q). In particular A096 section 2 holds for vacuum and total influence, including extreme feasible moments and constant functions. This reconstruction accepts that identity only; it does not newly review A096's separate atom-count theorem.

## 2. Exact substitution into A012's projection-history ledger

Let f be ANY Boolean function on a finite uniform cube, P its squared Fourier law, and Q a supplied normalized covering reference. At a physical query i both children inherit pi_i Q, where pi_i deletes i from a spectral set. Write P'=pi_i P, Q'=pi_i Q, and

    L_i=D(P||Q)-D(P'||Q') >= 0,
    J_i=average_b D(P_b||P').

Actual child Fourier coefficients give P'=average_b P_b. Hence

    average_b D(P_b||Q')-D(P||Q)=J_i-L_i.              (2)

The two-point bound is J_i<=(2/ln 2) Inf_i(f). A012 DERIVATION section 2 proves it from j''(t)<=4, with absolute values taken before the scalar argument and endpoints handled by continuity. The physical influence identity is I(f)=Inf_i(f)+average_b I(f_b).

At any node one may now perform ANY finite sequence of the affine projections in section 1, choosing the constraints from the actual current history, provided the current true law is feasible. Charge the FULL fee F=D(u||q) at each update. By (1),

    D_after-D_before+F=0.                             (3)

Thus this operation substitutes exactly for A012's nonpositive update bracket in its equations (5)--(6). Constraints may include the vacuum, total influence, every individual influence, or higher inclusion moments; they need not be a partition profile. Any of A012's paid partial-profile updates may also remain in the policy, since their bracket is nonpositive.

For ANY finite adaptive physical tree, actual reaches w_v, BOTH full terminal laws, and unchanged old bills U, telescoping (2)--(3) gives

    E D_terminal + sum_queries w_v L_v + sum_updates w_v F_v
       <= D_root + (2/ln 2) I(f).                     (4)

Each coordinate is queried at most once on a physical path. All choices may depend on that path; finiteness suffices. Adding the signed entropy increments and full terminal CE gives the complete bill

    Bill <= U + CE(P,Q) + (2/ln 2) I(f).              (5)

An ORIGINAL owner B with U+CE(P,Q)+(2/ln 2)I(f)<=B therefore pays the entire policy. If CE(P,Q)<=C0 I(f), the rate is C0+2/ln 2, plus old U. No terminal is replaced by a fresh source, no old charge is removed, and the fee is not also booked as a second refund. Scalar subprobability mass may equally be retained unchanged along the tree: its CE penalty is constant in each query and calibration identity. Projection inheritance is essential; this is not an uncharged replacement for A011's prescribed true-kernel inheritance.

## 3. Actual Boolean references defeat even very high moment matching

For every even n>=4 put f_n=product_{j=1}^{n/2} h(x_{2j-1},x_{2j}), where h is -1 only at (+,+). Its four Walsh coefficients have absolute value 1/2. Thus P_n is uniform on all 2^n spectral sets, H(f_n)=n, I(f_n)=n/2 and Inf_i(f_n)=1/2 for every i.

Fix 2<=k<=n-1. Let T={k+1}, let p0=2^-n, and define a spectral face F={T union V: V subset [k]}. Outside F set Q(S)=p0. On F set

    Q(T union V)=p0 [1+(1-epsilon)(-1)^|V|],
    a=2^(k-1-n), m=n*2^(n-k+1), epsilon=2^-m.

This is a strictly positive normalized rational reference. Exactly 2^(k-1) atoms have mass p0*epsilon, the same number have mass p0*(2-epsilon), and all others have mass p0. The vacuum is outside F, so Q(empty)=P_n(empty).

For EVERY coordinate set U of size <=k-1, the perturbation in the inclusion moment Pr[U subset S] vanishes. If U requires a coordinate fixed absent on F it is zero. Otherwise at least one of the k free coordinates is not in U, and summing its parity gives zero. All marginals on <=k-1 coordinates consequently agree, by inclusion-exclusion. In particular all individual influences and their sum agree.

For EVERY i in [k], the two perturbations on each pi_i fiber cancel. Therefore pi_i Q=pi_i P_n and

    L_i=D(P_n||Q)=a log2(1/[epsilon(2-epsilon)])
                    =n-a log2(2-epsilon).

Since 0<epsilon<1,

    n-a < L_i < n,  CE(P_n,Q)=n+L_i<2n=4 I(f_n).     (6)

Choose k=n-1. Then a=1/4, m=4n. The reference matches the vacuum AND EVERY marginal of order at most n-2, yet

    2n-1/2 < L_i/Inf_i(f_n) < 2n,
    2-1/(2n) < L_i/I(f_n) < 2.                       (7)

Thus no dimension-independent query-local bound L_i<=K Inf_i follows from those matching conditions, even with the ORIGINAL complete rate-4 source. This is not an FEI counterexample: H/I=2 exactly. All initial mismatch is lost at this first projection, so it cannot also be reused as unused reserve elsewhere.

Any affine calibration imposing only these already matched moments leaves Q unchanged: it is feasible and D(Q||Q)=0 is the unique minimum. Its actual release is zero. Section 2 still pays the full L_i from the original D_root; (7) explains why replacing that payment by a local influence charge is invalid. The n2 boundary cannot use this construction with k>=2 and a nonempty fixed tail.

## 4. Corrections to the immutable stage21 proof text

The signed-floor STATEMENT remains unchanged, as reconstructed by A004/A083/A085/A093/A098. Its displayed derivative omitted a factor t: the correct derivative of a log2(b/z)+(t-a)log2((t-b)/(t-z)) is t(z-a)/(z(t-z)ln 2). The minimizer and all stated signs remain unchanged because t>0.

The generic sentence asserting inherited CE increment=-D_occ also needs its reference convention and entropy term. For the explicit projection convention of section 2 the exact full-child change is

    average_b CE(P_b,pi_i Q)-CE(P,Q)=-B_i(P)-L_i,
    B_i(P)=H(P)-H(pi_i P).

It is not merely minus a KL contraction. This follows because average child CE equals CE(pi_i P,pi_i Q). Stage21's terminal conversion identity M_new=M_old-sum_h rho_h beta_h Delta_h is unaffected: it is direct full-law subtraction at fixed terminals. No old immutable report is overwritten.

## 5. Remaining universal line and proof rung

The all-dimensional statements above have finite analytic proofs; exact checks test their algebra and boundaries. They await independent review. A Lean check, if admitted and successful, concerns only the displayed ledger rearrangement and cannot certify the entropy or Boolean claims.

FIRST UNPAID UNIVERSAL LINE: supply a noncircular useful original complete reference with CE<=C0 I for arbitrary Boolean cores, or pay an actual necessary conversion into a productive interface from the SAME remaining original account. High-order moment matching alone cannot replace the query-KL payment. The exact constant transferred in (5) is unchanged, 2/ln 2; no universal FEI constant improves.
