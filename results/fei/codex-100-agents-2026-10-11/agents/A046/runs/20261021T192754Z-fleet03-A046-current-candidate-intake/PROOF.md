# A fixed continuation releases one unused separator reserve

All entropy and cross-entropy units are bits. Influences are physical flip probabilities on the uniform cube. No universal rate-four FEI assertion is assumed.

Let S,W,U,V be four independent fair event bits and

    A = WUV OR S(U OR V),  F(g) = 1+A(g-1).

The independent three-bit core, in increasing binary input order, is

    g = (-1,-1,-1,+1,+1,+1,+1,+1).

Query core bit 0 first. Its children are g0=(-1,-1,+1,+1) and g1=(-1,+1,+1,+1), both nonconstant. In each child prescribe S as the next query and then stop separator accounting. No further core query precedes S. This priority is essential to the scope below.

## The unchanged incoming account

Use exactly the A046 v3 reserve

    U(g) = [(7/8)(1-Eg)+(5/8)I(g)]/2.

It has values U(g)=23/32, U(g0)=3/4, U(g1)=17/32. The already booked core release is 5/64, because Inf_0(g)=1/4. These are not newly created funds.

At the root put P=Fhat^2 and Q=the product of its spectral marginals. Erase the queried core coordinate from both laws to get p,q. Transport the SAME actual physical restriction kernel

    k_b(t)=P_b(t)/(2p(t)), with k_b(t)=1/2 when p(t)=0,
    z_b=sum_t q(t)k_b(t), Q_b(t)=q(t)k_b(t)/z_b.

All source-zero reference rows remain. Every normalizer is positive in the exact certificate. A single explicit reset changes Q_b to R_b, the full product of the actual child spectral marginals. Put

    K=mean_b D(P_b||Q_b), T=mean_b D(P_b||R_b), sigma=T-K.

The actual reset increases mean terminal cross-entropy by sigma. No erasure credit is spent to offset this increase. Two finite KL chain rules also yield D(P||Q)=E+O+K, where E is conditional-erasure KL and O=D((1/2,1/2)||(z0,z1)); the certificate checks this independently, retaining source-only and reference-only support conditions.

Define the previously proposed full child account and the actual core remainder by

    B_new=mean_b [4I(F_b)-H(F_b)-D(P_b||R_b)-U(g_b)],
    R=D_0 F-(7/16)D_0 g-[U(g)-mean_b U(g_b)].

Independent direct character sums and rational logarithm intervals reproduce A040's obstruction:

    R > 41/1000, B_new < -67/1000,
    sigma > 3/50, sigma-E < -47/1000.

Thus the favorable net root reset sign still does not make this child bank eligible. Keeping B_new unchanged cannot pay R.

## What can actually be retired

For both children the sole actual S query has erasure B_S<4 Inf_S. Since there are no more separator queries after it, there is no positive bad-separator liability under this prescribed continuation. In particular the reserved U(g1)=17/32 need not remain earmarked for bad separator queries. Retire only this branch's reserve, at its ORIGINAL reach 1/2. This gives t=17/64. Keep the entire U(g0)=3/4 on the other branch, at original reach 1/2, so its held reserve is 3/8.

The original reserve conservation is exactly

    23/32 = 5/64 + 17/64 + 3/8.

Retirement does not count the booked release twice. It removes an unnecessary earmark from the existing account. The signed payment certificate is

    B_new + 17/64 - R > 5/32.

Both branches separately retain a positive account after the stated held reserves: branch 0 has 4I-CE-U(g0)>3/8; branch 1 has 4I-CE>1/100. The root-reach debit R can be drawn solely from branch 0: its required conditional withdrawal is 2R<9/100, below its certified >3/8 account. The other child is retained in full.

The value B_new+17/64-R is about .1563239326; the decimal has no role in the certificate. The rational interval comparison supplies the sign and the stated margin. This isolated remainder payment is not yet a complete source admission, as the next section shows.

## Full original-source admission requires more retirement

The original root account, with its complete original Q and the entire U, is

    S_old=4I(F)-H(P)-D(P||Q)-U(g) < -21/50.

It is about -.420582723. Consequently t=17/64 does not by itself establish full source affordability. This is the first failed admission check; it must not disappear behind the positive isolated-remainder margin above.

For the final transaction retire 5/16 of branch 0's U and the entire 17/32 of branch 1's U, at their ORIGINAL reaches 1/2. Total retirement is t=27/64. Keep U0'=7/16 and U1'=0, whose mean is 7/32. Then

    U(g) = 5/64 + 27/64 + 7/32,
    U_eff(root)=U(g)-27/64=19/64,
    U_eff(root)-mean U_b'=5/64.

Thus the booked core release remains exactly unchanged. The exact certificate gives

    S_new=S_old+27/64 > 1/800,
    C_new=B_new+27/64,
    C_new-R > 5/16.

To check the COMPLETE physical query rather than only its R component, put

    DCE_new=CE(P,Q)-mean_b CE(P_b,R_b),
    L=DCE_new+5/64-4 Inf_0(F).

Here L>7/20 is the actual signed query debit including the reset and the booked reserve release, after the physical query influence price. The finite identity is

    C_new-L=S_new>1/800.

This pays the whole node from the same two complete child accounts. R is a component of this full accounting; the assertions C_new>=R and C_new>=L are two views of the transaction, NOT two simultaneous withdrawals. Retained child source banks and the complete S continuations below are positive; no root bank, physical influence account or reset credit is renewed. The improvement is a prescribed-policy release of an unnecessarily held liability. It is not a general permission to lower U on arbitrary histories.

## Complete continuation costs, including the guard that fails

Retiring a bad-erasure reserve is not by itself a full-reference query bound. To keep every other bill visible, carry each R_b through its actual S kernel to normalized full terminal references R_bc, with the same fair fallback on source-zero rows and no further reset. Let

    CE_b=H(P_b)+D(P_b||R_b),
    CE_bc=H(P_bc)+D(P_bc||R_bc),
    DCE_b=CE_b-mean_c CE_bc,
    L_b=mean_c[4I(F_bc)-CE_bc].

The exact physical influence split gives the finite identity

    4I(F_b)-CE_b = [4 Inf_S(F_b)-DCE_b]+L_b.

The certificate keeps all four full terminal laws, reference laws, normalizers, influences and cross-entropies. Both first terms on the right are NEGATIVE, about -.270948 and -.335066. Thus erasure-goodness does not imply full-reference goodness, even here. They are paid from their corresponding terminal accounts L0 about 1.406496 and L1 about .345695, with the exact signed difference retained. These L_b accounts are not spent again as additional funds in B_new. B_new already uses the left side of this identity.

This is also why an arbitrary mixed-history assertion is not justified: another core query before S might create a new bad separator liability. A continuation that permits this cannot retire U on the evidence above. A future theorem must either prove the same no-liability admission for its actual continuation or keep and pay the liability.

## Independent reconstruction of the consumed A040 statement

For any independent Boolean activation A and core g, put pi=EA, a=1-Eg, phi(x)=-x log2 x, L_A=sum_T phi(Ahat(T)^2). The coefficients with nonempty core set V are Ahat(T)ghat(V). Their entropy is

    pi[H(g)-phi((1-a)^2)]+(2a-a^2)L_A.

The empty-core row consists of 1-a pi at the empty control set and -a Ahat(T) at nonempty sets. Its entropy is

    phi((1-a pi)^2)+a^2[L_A-phi(pi^2)]
       -(pi-pi^2)a^2 log2(a^2).

Adding gives H(F)=pi H(g)+2a L_A+Psi_pi(a), with Psi exactly as in A040 v1. Across a fair core query, a=mean a_b cancels the linear term. A^2=A supplies sum Ahat^2=pi; independence supplies the factorization. All sums are finite; no denominator is cancelled at pi=0, pi=1 or a=0, and x log x is extended continuously at zero. The endpoints give F=1, F=g, or a constant core as appropriate. The code1 and dictator fixtures independently reproduce A040's contrasting full-reference signs. This review changes no mathematical clause of A040 v1.

## Verification rung and exact open line

The main certificate uses direct integer character sums, not the source's FWHT. Rational atanh bounds use 32 positive terms after range reduction to [1,2], with z=(x-1)/(x+1) in [0,1/3] and tail at most 2z^65/[65(1-z^2)]. Division by the positive ln2 enclosure uses ordered endpoints. Rounding occurs outward on a 2^-110 grid. Every sign is a rational interval test. Parseval and influence are checked by a separate physical edge count.

Rung: exact finite certificate plus a finite accounting derivation; independent review of this new retirement transaction remains pending. A formal check, if it returns, certifies only the stated rational conservation identity, not entropy, policy admission or FEI. Full FEI remains OPEN. The next unpaid line is a history-stable sufficient condition allowing the same unused-reserve release before a further active core query, while retaining the original reference, all prior debits and both full terminals. Existing earlier-history debits beyond the explicitly booked release are not supplied in this fixture and are not assumed absent in a universal argument.
