# Terminal-inclusive conditional-edge refund audit

All logarithms are base two. Let p_S=hat f(S)^2, e_i=Inf_i(f), I=sum_i e_i. For e_i>0 and T not containing i define mu_i(T)=p_(T+i)/e_i and r_i(T)=p_T+p_(T+i). Both are probability laws. Define

    D_i=D(mu_i||r_i),
    M_i=sum_T p_(T+i) log(r_i(T)/p_(T+i)), M=sum_i M_i.

The normalized joint laws P(i,T)=p_(T+i)/I and Q(i,T)=(e_i/I)r_i(T) have identical coordinate marginals e_i/I. Consequently

    I D(P||Q)=sum_i e_i D_i,
    M=sum_i e_i log(1/e_i)-I D(P||Q).                 (1)

These are retained-KL baselines from A001, not claimed as fresh progress. They preserve actual Boolean endpoints and the complete joint normalizer. Moreover M<=B<=M+I/ln(2), since each edge contributes M's upper term plus x log(1+y/x)<=y/ln(2), and sum of upper masses is exactly I. Zero terms have continuous conventions.

## Exact new audit: the refund preserves the arbitrary terminal core

Take any nonconstant Boolean seed f on n>=1 coordinates, m>=1 disjoint copies and ell>=2 fresh parity coordinates Z. Set h=chi_Z product_(b=1..m) f_b, J=I(h)=mI(f)+ell. The occupied Fourier sets of h contain all Z, so its mean and singleton coefficients vanish. Product structure gives

    M(h)=mM(f), sum_i Inf_i(h) D_i(h)=mI(f)D(P_f||Q_f). (2)

For an original coordinate in block b, its derivative and residual marginal are mu_i(f) and r_i(f), each tensored with the SAME complete Fourier laws of the other blocks and the parity support. Thus D_i(h)=D_i(f). For a fresh parity coordinate r_i=mu_i and D_i(h)=M_i(h)=0; its influence is one. These statements hold also for irrelevant seed coordinates, which are omitted from the joint laws.

Activate h with k>=1 fresh point-indicator controls A_k, q=2^-k:

    F=1+A_k(h-1), d=(1-q)^2+q^2.

Its constant coefficient is 1-q, nonempty pure-control coefficients have magnitude q, and every nonempty core coefficient in every control slice is q times its h coefficient. Hence I(F)=q(J+k).

For each relevant core coordinate, mu_i(F) is mu_i(h) times the uniform control-subset law. On its support, r_i(F) is q times r_i(h) times that same law. The exceptional constant endpoint is outside this support because h has no singleton coefficients. Therefore

    D_i(F)=D_i(h)+k,  M_i(F)=qM_i(h).               (3)

This is a literal likelihood-ratio identity, not an entropy upper bound. All k activation bits' rarity are refunded in each terminal data derivative; no terminal data entropy was discarded.

For a control coordinate the exceptional residual atom has derivative probability q and residual marginal d. Every other occupied atom has likelihood ratio 1/(2q), and their total derivative probability is 1-q. Therefore, independently of f,m,ell,

    D_control=(1-q)(k-1)+q log(q/d),
    M_control=q(1-q)+q^2 log(d/q^2).                (4)

The normalization is exact: the exceptional derivative mass is q, the remaining mass is 1-q; the residual marginal sums to one even though the core spectrum is arbitrary.

Writing D_f=D(P_f||Q_f) and D_F=D(P_F||Q_F), the complete joint refund is

    I(F)D_F=q[mI(f)D_f+kJ+kD_control],
    M(F)=q mM(f)+k[q(1-q)+q^2 log(d/q^2)].          (5)

Equation (5) is the substantive audit result. It explicitly retains the original seed divergence, with the single physical ledger I(F)=q[mI(f)+ell+k]. Activation supplies a refund for its own rarity and does not supply the missing seed payment.

Let M_ge2 retain only edges whose lower endpoint has size at least two. Every occupied core edge of positive M-cost contains Z, hence lies in this tail. Each control coordinate contributes q/2 from nonempty core sets. Pure-control lower sets of size at least two contribute q^2[2^(k-1)-k]. Thus

    M_ge2(F)=q mM(f)+kq(1-kq).                      (6)

This oriented-cost identity is distinct from A090's erasure identity B_ge2(F)=q mB(f)+2kq(1-kq). The latter follows independently by doubling equal-mass regular control edges; the exceptional control edge lies in the root layer. More generally B_geell(F)=qmB(f)+kq+2kq^2 sum_(r=ell..k-1) binom(k-1,r), with an empty sum zero. For each parity coordinate, removing it from a core support leaves ell-1>=1 parity bits and no adjacent occupied lower coefficient, while the empty-frequency exception has no singleton coefficient. Thus B_z(F)=0 and Inf_z(F)=q>0. This independently reconstructs A090's entire finite-parameter formula and its zero selected-coordinate ratio, without using the T12 theorem.

## Quantifier consequence: low-influence refund completeness

Let K_M=sup_(I(f)>0) M(f)/I(f) in the extended reals. For any finite nonnegative s(N)=o(N), and every fixed ell>=2, the supremum of M_geell/I over Boolean signs with 0<I<=2^-s(N) equals K_M. This statement does not assert K_M finite.

For completeness, take eta_m=sup_(N>=mn) s(N)/N, which is finite and tends to zero. Set k_m=ceil[4(n+1)m sqrt(eta_m)+2sqrt(m)]. Then k_m=o(m). Eventually N_m=mn+ell+k_m<=(n+2)m and

    s(N_m)<=eta_m(n+2)m<=4(n+1)m sqrt(eta_m),
    k_m-s(N_m)>=2sqrt(m)>log(mI(f)+ell+k_m).

Thus the actual activated Boolean F_m is in the cutoff class. All core M-cost is in M_geell, so M_geell(F_m)/I(F_m)>=mM(f)/(mI(f)+ell+k_m), tending to M(f)/I(f). The reverse supremum inequality follows from M_geell<=M. For K_M infinite apply the same argument to each finite seed ratio; no exchange of an unknown supremum and a limit is needed. For ell=2, (6) gives the exact finite-parameter cost, and (4) bounds M_control/q<=1+2kq<=2, so M(F_m)/I(F_m) also tends to the seed ratio.

Equivalently, activation's large known divergence in (5) does NOT establish the necessary universal inequality

    D(P_f||Q_f)>=sum_i (e_i/I)log(1/e_i)-K          (OPEN)

for an arbitrary terminal seed and one finite K. That is the first unsupported line. Uniform M payment implies uniform B payment with the explicit I/ln(2) overhead, so this is a full C018 obligation, not a small-influence class theorem. No FEI disproof is claimed.

## Scope and review

The normalizer/refund transport is a scoped audit of the A001-requested function-specific reference, not a proposal to pay full FEI or another broad candidate. A090's B-tail completeness is independently reconstructed: the same cutoff argument above with B replacing M, homogeneity, the exact doubled control tail, and B_geell<=B proves its full supremum statement. A096 supplies no correction to that version and can act as independent reviewer. The new M-refund formulas require separate A001/A073 review.
