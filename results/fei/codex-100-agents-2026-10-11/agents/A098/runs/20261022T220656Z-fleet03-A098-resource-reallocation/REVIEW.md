# A098 reconstruction of the dummy-data extension

Verdict: the new LOCAL dummy marginal/likelihood/envelope argument holds analytically. Finite independent validation and compute admission are recorded separately. The all-history consequence is conditional on the exact imported A096 active-reset and A097 control-reset versions, whose whole dependency chains are not independently recertified here.

Let a,b,r be integers with a,b,r>=1, n=a+b, s=2^-a, t=2^-n, e=2^(1-n-r), mu=1-2s. Let g=1-2A_a, F=g+2A_(n+r). Supply any normalized reference R on data spectral labels, finite on the source support, calibrated so R(0)=mu^2. Put c=CE(P_g,R). Define R_e=(1-e/s)R+(e/s)mu delta_0+2e U_n and Q(T,U)=R_e(T)P_F(T,U)/M(T), where M is the actual data marginal. Entropies and CE are in bits. The reference Q is complete and normalized, rather than a signed amplitude lift. Each M(T)>0 since a nonempty control label has amplitude e. All weights and denominators used below are positive where required.

Delete any physical dummy label j. The unchanged off-child is g with unused variables; its inherited reference is the complete marginal Q_-j, not a new source reference. The on-child has parameters a,b-1,r,2e. Let V=R_-j and recalibrate it at mu^2 to obtain Rbar. For every occupied nonempty source label T, V(T)>=R(T), V(0)>=mu^2, and

    Rbar(T)=V(T)(1-mu^2)/(1-V(0))>=R(T).

Finite source cost forces V(0)<1: an active singleton has positive true mass and positive reference mass even when a=1. At the vacuum Rbar(0)=R(0). Consequently cbar<=c pointwise on true support. The zero-probability vacuum at a=1 is omitted, not logged.

For an occupied nonempty source label, one term of Q_-j(T,0) is

    R_e(T)*(2s-e)^2/(4s^2-4se+2te).

The other deleted-label term is nonnegative and is retained in the actual CE. Let h=e/s. Since b,r>=1, h<=1/2, t<=s/2 and e<=t. The inverse of the displayed likelihood multiplier is

    1+(2te-e^2)/(2s-e)^2 <= 1+h/2.

Indeed its numerator is nonnegative and at most se, while (2s-e)^2>=9s^2/4>=2s^2. Also R_e(T)>=(1-h)R(T). At the vacuum, calibration gives Q(0,0)=(mu+e)^2>=mu^2, so deleting j cannot worsen that atom. Thus, with v=4s(1-s)<=4s,

    c_off-c <= v[-log2(1-h)+log2(1+h/2)]
              <= (8+2/ln 2)e < 11e.

Here -log2(1-h)<=2h follows from convexity and its chord between 0 and 1/2, and ln(1+x)<=x supplies the other term. These are signed complete likelihood costs, including reference-only atoms and the actual conditional control normalizer.

The actual Boolean Fourier amplitudes are ghat(T)+e when the control label is empty and e otherwise. Pairing any non-active coordinate and counting all labels gives

    sum_pairs |alpha beta|=e(4-4s+2e-2e/s)<=4e.

For nonzero alpha,beta, apply ln(1+z^2)<=z separately with z=|beta/alpha| and its reciprocal. This proves phi(alpha^2,beta^2)<=2|alpha beta|/ln 2; zero endpoints follow directly. Therefore B_j<=8e/ln 2<12e. The estimate ln 2>2/3 follows from its positive atanh series (first term is 2/3).

The imported root floor estimate gives the specified new on-child envelope W_on=cbar+20e(n+r-1). With W=c+10e(n+r), the entire substitution obeys

    B_j+(c_off+W_on)/2 < W+(15/2)e < W+8e.

No prior erasure debit or opposite terminal disappears in this comparison. All occupied atoms have strictly positive denominators; balanced a=1, b=1 and r=1 obey the same local argument. A non-point source would not satisfy the two-level coefficient calculation, so the result asserts nothing about it. Neither marginalization nor this estimate is a proof that an arbitrary source has influence-priced CE.

Conditional global synthesis: assuming the pinned A096 active/final-boundary and A097 control local substitutions, each surviving on-step halves physical reach and doubles e. Thus reach*e=e_root, every non-active step spends at most 8e_root, and there are at most d-1 such steps, d=b_root+r_root. All retained off-branches admit no-reset continuation by the complete-reference chain rule. From c_cal<=C0 Ig, K=2C0+10, I(F)=Ig+e(d-a), and E=ae with E/Ig=2^-d<=1/4,

    K I(F)-W_root >= (C0+10)(Ig-2E)+2C0 de >=5Ig
                       =5a 2^d e_root.

For integer d>=2, 5*2^d-8(d-1)>=12: equality holds at d=2 and the increment is 5*2^d-8>0. Thus the claimed all-eligible-history reserve follows CONDITIONALLY at unchanged rate18 for structural C0=4. This checks the new substitution and the algebraic assembly, but does not independently certify the upstream active theorem at its full scope.

The next unpaid transaction is a prescribed reference reset in a previously retained off-branch after inherited debits. It must retain both complete terminal costs and use the diminished original bank. Local influence pricing, reinitializing a floor, or an unrelated terminal surplus does not establish it.
