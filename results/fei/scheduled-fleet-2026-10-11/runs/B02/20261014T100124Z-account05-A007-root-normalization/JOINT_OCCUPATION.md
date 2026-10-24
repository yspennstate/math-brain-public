# Exact occupation with the old roots in the same sum

Bits, gamma=6/5. Fix an ACTUAL old partition forest rho, with used gates V, owned sizes s_l, selected intersections kappa_l, old roots R and c=|R|. Let a(l) be the root of the actual TREE component containing l. It is not the source SCC containing l. Set pi_a to the old root rarity. Fix selected common-core size u>=1 and global label scaling beta. The original conditional surrogate posterior eta_T is unchanged.

For this fixed u define the truncated series, through degree u,

    f_l(z)=sum_(v=0)^u w_l(v) z^v/v!,
    w_l(v)=((s_l+v)/(kappa_l+u))^(gamma(s_l+v))
                         /(s_l/kappa_l)^(gamma s_l).

If c=1 the exact rank-stripped distributed multiplier for rho is

    G_rho(u)=beta^|V| u! [z^u] product_l f_l(z).

If c>=2 it is

    G_rho(u)=beta^|V| (u+1)_(c-2) u! / product_(a in R)pi_a
          *[z^u] sum_l pi_(a(l)) z f_l'(z) product_(h!=l)f_h(z).

Here (x)_j is rising factorial; (x)_0=1. These are EQUALITIES for the selected distributed family, not the full activated forest mass. In particular

    J_dist,U(T)=E_(rho~eta_T) G_rho(|U|).

No new conditioning, posterior, fractional reference, actual queue probability or optimization per T is introduced.

Proof: with gate occupation counts v_l, the number of labelled owner maps is u!/product v_l!. For c>=2 the exact rooted component-tree count is m_a=u_a (u+1)_(c-2), where u_a=sum_(l in component a)v_l. Multiply by pi_a/product_R pi before summing. The derivative z f_l' supplies the factor v_l, and the coefficient supplies the labelled-map multiplicity. This proves the formula. For c=1 the count is one for every map, irrespective of the location of its owner in the old tree; its root ratio is one. This explains why the c>=2 formula cannot be used by substituting c=1. The chronological order and old-event injection are those of the independently accepted distributed-lift theorem; no factorial moment of separate SCC factors is taken.

The coefficient can be computed with a two-register convolution: initialize P=1,Q=0. On adjoining gate l, replace (P,Q) by (P f_l, Q f_l+pi_(a(l)) P z f_l'), using OLD P,Q in both updates and truncating at degree u. This is O(|V|u^2) real arithmetic and O(u) coefficient storage for a GIVEN rho. It does not provide an efficient sum over all old rho or a polynomial-time Boolean algorithm. With gamma=6/5, each w is an exact rational base to power 6/5, so rational fifth-root intervals can certify numerical evaluations; our finite checks instead keep each rational base power formal.

## Exact one-control susceptibility and the first correlation obstruction

For u=1 write

    A=product_l (kappa_l/(kappa_l+1))^(gamma s_l),
    t_l=(s_l+1)^(gamma(s_l+1)) /
                                  [s_l^(gamma s_l)(kappa_l+1)^gamma].

Then Z_tau(1)=A sum_l t_l. For c>=2,

    G_rho(1)=beta^|V| (c-1)! A
                               *sum_l pi_(a(l)) t_l / product_R pi_a.

Thus the exact extra rarity credit beyond min-root rarity is the weighted arithmetic mean of pi_(a(l)) under q_l=t_l/sum_h t_h. The previous minimum-root inequality is valid since this mean is >=min_R pi. However replacing q by the owned-size law s_l/s is NOT a valid lower bound in general. This is the first unsupported line in a tempting stronger joint refund, and it fails even on overlapping prime supports.

Actual Boolean witness: B is the OR of clauses R_0={0,1,4} and R_1={2,3,4,5}; these are exactly its monotone prime implicants. They share coordinate 4. Take T={0,1,2}, ownership A_0={0,1}, A_1={2}. The base selected incidence graph is edgeless, so both gates are roots; s=(2,1), kappa=(2,1), pi=(1/8,1/16). This assignment and root set are forced by T, so eta_T is a point mass. For g=2B-1, T has nonzero Fourier coefficient -1/32: in 2h_0+2h_1-2h_0h_1-1 only the product term contains T, and its six-variable cell coefficient is 1/64. Feasible original lambda=(1/2,1/2) and beta=1 retain one globally fixed reference, also feasible at the fresh core.

Here t_0=(9/4)^gamma, t_1=2^gamma, so t_0/t_1=(9/8)^gamma<2, proved exactly by 9^6<2^5*8^6. Consequently q_0<2/3=s_0/s and, since pi_0>pi_1,

    sum_l q_l pi_l < sum_l (s_l/s)pi_l=5/48.

The proposed bound G>=beta^2 Z*(1!)*(5/48)/(pi_0*pi_1) is strictly false for this actual, positive-spectral-mass overlapping prime-table record. The exact formula and old min-root credit remain valid. This refutes an additional occupation/root factorization, not an existing claim, not the prior general budget, and not FEI. It pinpoints why the root rarity must be tilted by occupation susceptibility before crediting it. Uniform-root families conceal this obstruction.

For this SAME witness the exact coupled multiplier is

    J_dist,1(T)=16*2^(-6/5)+8*(4/9)^(6/5)>8.

The two terms correspond to the two surviving root choices, not separately optimized references. The sign follows from 2^(-6/5)>3/8 and (4/9)^(6/5)>1/4, checked by 512>243 and 4^11>9^6. Thus old rarity removal pays congestion and leaves MORE than three bits of credit on this shared-support record. Also lambda=(1/2,1/2), beta=1, p=1/2 give D=49/512, D'=97/2048 and D'/(pD)=97/98<1. The negative normalization is retained in the full ledger, rather than discarded before examining this refund. This sector has positive spectral weight 1/1024; it is not a payment assertion for the other 62 nonempty data sectors or inherited base cost.

## Complete signed ledger and the remaining line

For the inherited distributed transfer, p=2^-r, L_0(T)=E_eta beta^|V|, D=product(1+lambda*pi)-1 and D'=product(1+p beta lambda*pi)-1. Keep

    Psi=p Var(g)log[D'/(pD)]
        -p sum_(T!=empty)P_g(T)
              [p log L_0(T)+2^-r sum_(U!=empty)log E_eta G_rho(|U|)].

This now has an exact occupation/root numerator for every selected sector; there is no separate H(a) or K_tau approximation. All r+1 occupation sizes, empty-core labels, root conditioning, original posterior and inherited pR_g remain. Together with the prior rank-payment transfer this is an upper bound on the activated residual, not its equality and not an actual queue-output code length. The universal unsupported line is still a dimension-independent influence payment of this whole signed ledger AND its inherited base residual for an appropriate one-time feasible reference. Exact coefficients alone do not pay it. NEXT should price this exact mixed-root numerator under the same old determinant/factorial posterior, rather than multiply independently averaged root and occupation credits.
