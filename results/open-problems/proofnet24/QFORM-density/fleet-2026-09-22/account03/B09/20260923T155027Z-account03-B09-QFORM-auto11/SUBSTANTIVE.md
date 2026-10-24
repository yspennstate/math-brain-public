SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T15:50:27Z.
attacking: near-rank-one localized hub-pair interpolation by compiling the anchored third volume into a residual one-anchor two-volume half-Riesz estimate before any reciprocal pair determinant.

# Substantive checkpoint: one-anchor two-volume half-Riesz bridge

Status: NEW SUPPORTING DERIVATION; full QFORM remains OPEN. Execution label: WITHOUT_VERIFIED_BRAIN.

The r35 obstruction was quantitative: an invertible indefinite physical pair estimate blows up as det(E)->0 even though the exact rank-one endpoint is finite. This checkpoint changes mechanism. Complete one ORIGINAL coordinate first, then pay the exact Schur residual with a one-anchor two-volume fractional estimate. No small quadratic coefficient is discarded.

## Lemma A: one-anchor selected two-volume half-Riesz

Let I,J be disjoint ORIGINAL-coordinate banks and

    R=F(X_I)+2 X_I^T M X_J+G(X_J),

where F,G are arbitrary measurable real functions finite a.s. Fix a physical row h in I, write a=M[h,:], and let Omega be a selected family of physical 2x2 minors, every selected row pair being {h,k}. Put

    Z=sum_{({h,k},C) in Omega} det M[{h,k},C]^2 >0,
    z_k=sum_{C:({h,k},C) in Omega} det M[{h,k},C]^2,
    alpha_k=z_k/Z.

Then

    H_{1/2}(R):=sup_s E|R-s|^{-1/2}
      <= max{ Cc Z^{-1/8}, Cd ||a||_2^{1/6} Z^{-1/6} },

with

    Cc=4*2^(5/8)*e^(1/4)=7.9209515909...,
    Cd=12*2^(-1/6)*e^(1/4)=13.7272391734....

Proof split.

(1) If some alpha_k>=1/2, retain the whole physical two-row cross matrix with rows h,k. Its squared two-volume is at least z_k. The rank-two grouped Plancherel calculation gives

    |phi_R(t)| <= pi e^(1/2) z_k^(-1/4)|t|^-1.

Using the proved fractional-Riesz identity H_{1/2}<=c int |t|^-1/2 |phi(t)|dt, c=1/sqrt(2pi), and integrating min(1,K/|t|),

    H_{1/2}(R)<=4 sqrt(2)e^(1/4) z_k^-1/8
               <=Cc Z^-1/8.

(2) If every alpha_k<1/2, use quadratic decoupling on the I-bank. With H(w)=|psi_h(2t<a,w>)| and L(w) the product of the remaining row factors,

    |phi_R(t)|^2 <= F(t),
    F(t)^2 <= F2(t) F0(t),

where F2 integrates H^2 L and F0 integrates L against the difference-coordinate product density.

For F2 use the selected 2-volume determinant weights. The anchor has exponent one and Plancherel norm

    int |psi_h(2ts)|^2 ds <= pi/|t|.

The remaining row exponents alpha_k sum to one; the cap-one characteristic-function Lp lemma and the BL determinant bound give, after exact entropy cancellation,

    F2(t) <= 2 pi^2 e Z^-1/2 |t|^-2.                 (A.1)

For F0 descend the selected two-volume to a selected one-volume on the low rows. Let m_k=M[k,:]. Since

    z_k <= ||a wedge m_k||^2 <= ||a||^2 ||m_k||^2,

put pi_k=z_k/Z and distribute pi_k among the physical entries of m_k proportionally to m_kj^2. Its determinant-weighted effective mass satisfies

    Z_eff=exp(sum_k pi_k log(||m_k||^2/pi_k)) >= Z/||a||^2.

The resulting one-volume row marginals are exactly alpha_k<1/2. The same BL/Hausdorff-Young computation gives

    F0(t) <= 2 pi e^(1/2) ||a|| Z^-1/2 |t|^-1.        (A.2)

From (A.1)-(A.2),

    |phi_R(t)| <= min(1,
      sqrt(2) pi^(3/4)e^(3/8)||a||^(1/4)Z^-1/4 |t|^-3/4).

For gamma=1/2 and b=3/4,

    int_R |t|^-1/2 min(1,K|t|^-3/4)dt =12 K^(2/3).

Since c_{1/2}=1/sqrt(2pi), this yields

    H_{1/2}(R)
      <=12*2^(-1/6)e^(1/4)||a||^(1/6)Z^-1/6,

as claimed. This has the correct scaling M->sM: both branches scale as |s|^-1/2.

## Lemma B: splice into the r35 localized pair without det(E)^-1

Use r35 notation. Let i,j be the localized physical hub pair and S,T the leaf partition. Write

    m_i=A[i,T], m_j=A[j,T], m_k=A[k,T] (k in S),
    Delta=||m_i wedge m_j||^2>0,
    V=sum_{k in S}||m_i wedge m_j wedge m_k||^2.

In r35, V=V_ij(S)>=27G_*/400.

Assume the physical scalar pivot alpha=A_ii is nonzero. Complete the square exactly in the ORIGINAL coordinate X_i. The residual Schur cross rows against T are

    c_j=m_j-(A_ij/alpha)m_i,
    c_k=m_k-(A_ik/alpha)m_i.

The wedge currency survives exactly:

    m_i wedge c_j = m_i wedge m_j,
    m_i wedge c_j wedge c_k = m_i wedge m_j wedge m_k.

Hence, with

    Z2=sum_{k in S}||c_j wedge c_k||^2,

one has

    Z2 >= (||c_j||^2/Delta) V.                       (B.1)

Indeed the triple volume is Delta times the squared component of c_k orthogonal to span(m_i,c_j), whereas ||c_j wedge c_k||^2 is ||c_j||^2 times the squared component orthogonal to c_j, which is at least the former component.

The dependence-safe square-peel inequality gives

    ||p_Q||_inf <= |alpha|^-1/2 H_{1/2}(R).

Apply Lemma A to the residual with anchor row c_j and selected two-volume equal to all minors contributing to Z2. Using (B.1),

    ||p_Q||_inf
      <= |alpha|^-1/2 max{
          7.921 Delta^(1/8)||c_j||^-1/4 V^-1/8,
          13.728 Delta^(1/6)||c_j||^-1/6 V^-1/6 }.

The identical coefficient multiplies every interval length. Essential boundedness follows. Continuity is NOT established by this fractional square-peel route.

This estimate contains no det(E)^-1 and no sigma_min(E)^-1. It therefore removes the artificial determinant blow-up as an invertible pair approaches a nonzero rank-one physical core, provided one physical diagonal pivot and the residual cross currency remain quantitative. The still-unpaid stratum is the genuinely near-zero pair core (both physical diagonals small), or degeneration of the residual anchor c_j; that must be joined to the zero-core / aggregate grouped-cross mechanisms rather than paid by reciprocal pair determinant.

## Target-valid regression

For eps>=0 take the six-coordinate matrix with physical pair

    E_eps=[[1,1],[1,1+eps]]

on coordinates i,j and cross edges i-t1=1, j-t2=1, k-t3=1, all other coefficients zero. At eps=0 the spectrum is

    {-1,-1,1-sqrt(2),1,1,1+sqrt(2)},

and for sufficiently small eps>0 it still has at least four eigenvalues of absolute value >=1. Here alpha=1, Delta=V=1, c_j=(-1,1,0), ||c_j||=sqrt(2), and Z2=2. The concentrated branch gives

    ||p_Q||_inf <= 4 sqrt(2)e^(1/4) 2^-1/8
                 =7.2635446349...,

uniformly as det(E_eps)=eps tends to zero. Thus the previous indefinite-pair reciprocal determinant blow-up is not intrinsic on this family.

The same regression has the literal physical cross block K=I_3 from rows {i,j,k} to {t1,t2,t3}. Applying the designated account04/B09 theorem gives the actual inequality

    ||p_Q||_inf <=3|det K|^-1/3=3,

with continuous density; this is an independent paid exit for the regression, not the proof of Lemma A/B.

Next step: eliminate the residual near-zero-core / small-c_j gap by combining the zero-core two-anchor coefficient-plane theorem with this new one-anchor half-Riesz bound at a scale chosen before scalar completion.
