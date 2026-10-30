# Actual shared bent/spike collision and the selected-coordinate guard

All physical bits are independent and uniform. Entropy, erasure B and retained Q are in bits. For a physical query write f=u+(-1)^x v and Inf_x=E v^2. Phi(p,q)=(p+q)log2(p+q)-p log2 p-q log2 q, with zero continuity. L_x=6 sum |uhat|^(1/2)|vhat|^(3/2) is the previous A078 universal majorant of Q_x.

## 1. An actual Boolean family and its full influence

For every even k>=2 let s be k shared bits, x a private bit, z a fresh selector, N=2^k, a=1/N, b=1/sqrt(N)=2^(-k/2). Define

    G(s,x)=1-2*1{s=0,x=0},
    H(s)=(-1)^(s_1 s_2+...+s_(k-1) s_k),
    F(s,x,z)=G(s,x) if z=0, and H(s) if z=1.

No spectral law is postulated: these formulas give every truth value. G is a point defect on k+1 actual coordinates. H is a tensor of two-bit quadratic signs. Each quadratic pair has all four Walsh coefficients of magnitude1/2, so Hhat(C) has magnitude b at every C and Hhat(empty)=b. The x-query of G has uhat(empty)=1-a, uhat(C)=-a otherwise, and vhat(C)=-a for every shared C. This follows directly from its single physical exceptional vertex.

Every influence of G is a, every shared influence of H is1/2, and E(GH)=b-a. Thus

    Inf_x(F)=a/2,
    Inf_sj(F)=(a+1/2)/2,
    Inf_z(F)=(1-b+a)/2,
    I(F)=k/4+(k+1)/(2N)+(1-b+a)/2.                 (1)

All added shared and selector influences are counted. In particular Inf_z>=1/4. H(G)<=4I(G) follows from the point-defect spectrum, proved in the prior CORE_TRANSPORT_PROOF section4. The exact selector decrement H(F)-[H(G)+H(H)]/2 is at most2 since B_z<=1 and JS_z<=1. H(H)=k, so

    H(F)<=2(k+1)/N+k/2+2 <4 I(F).                 (2)

The difference between the right side4I(F) and the displayed upper bound is k/2-2b+2a>0 for k>=2. This family is not an FEI counterexample.

## 2. The newly unpaid private-query collision

At x, each shared Fourier row has actual pair ((u_C+h_C)/2,d_C/2) at z-frequency0 and ((u_C-h_C)/2,d_C/2) at z-frequency1. Consequently

    B_x(F)=B_x(G)/2+D_k,
    D_k=(N-1) S(-a,a;b)+S(1-a,a;b),
    S(u,d;h)=[Phi((u+h)^2,d^2)+Phi((u-h)^2,d^2)]/4
               -Phi(u^2,d^2)/2.                    (3)

This is A077's exact private-row identity with all common frequencies retained; signs of h_C do not affect S. It extends the identity, not its one-shared-bit constant. This data-query obstruction differs from A097's bent/singleton-flip example for selector-only entropy pricing.

For positive p,q, Phi(p,q)>=q log2(p/q). Since Phi(a^2,a^2)=2a^2, the nonempty comparison gives

    S(-a,a;b)>= (a^2/2)log2(N-1)-a^2.

The empty row is at least -Phi((1-a)^2,a^2)/2. Its negative magnitude is at most a^2(k+3/4): write Phi(p,q)=qlog2((p+q)/q)+plog2(1+q/p), use p+q<=1, ln(1+t)<=t, and1/ln2<=3/2. Therefore, for every even k>=4,

    D_k/Inf_x(F)
      >=(1-1/N)log2(N-1)-2(1-1/N)-(2k+3/2)/N
      >=k-3-(3k-3/2)/N >=k-4.                       (4)

Here log2(N-1)>=k-1 and3k/2^k<=1 for k>=4 (the latter decreases thereafter). This is an all-parameter proof of an actual Boolean failure of any constant |D_x|<=C Inf_x under unrestricted shared data. The finite exact certificate also gives D_4>2 Inf_x, already defeating the literal one-bit price2 at four shared bits. It does not refute A077's at-most-one-shared-bit theorem.

Since B_x<=Q_x+M_x/ln2 and M_x<=Inf_x, (4) also yields Q_x/Inf_x>=k-11/2. Thus a fixed price at every physical coordinate is false for Q itself, not just for its upper surrogate.

## 3. Quarter-profile overcharge is stronger, and a paid pivot survives

For each nonempty shared row, its contribution to P=L/6 is

    (a^(3/2)/4)[sqrt(b+a)+sqrt(b-a)].

For k>=2, a<=b/2, so it is at least (a^(3/2)/2)sqrt(b/2). Keeping the N-1 nonempty rows proves

    L_x(F)/Inf_x(F)
       >=(6/sqrt(2))(1-1/N)N^(1/4)
       >=3*2^(k/4).                                 (5)

This records why the quarter surrogate can overcharge a deliberately rare query exponentially more than retained Q; it does not invalidate its universal majorization or the earlier conditional antichain/degree-transport theorem.

The same actual root has a paid selector coordinate. Holder and Parseval universally give P_z<= (1-alpha)^(1/4)alpha^(3/4), alpha=Inf_z. Since alpha>=1/4,

    L_z(F)<=6*3^(1/4) Inf_z <8 Inf_z,                (6)
    Q_z(F)<=B_z(F)<=1<=4 Inf_z.

Thus this family does not defeat selected-coordinate admission, let alone every-coordinate admission at the root. Querying z first retains the complete G and H leaf entropy in (2). The large correction at x cannot be charged only to that rare removed influence; it must be avoided or paid from a named shared-core reserve. No reserve is invented or spent twice here.

## 4. Exact universal frontier

The old scoped quarter theorem remains valid; this stage adds its explicit adverse shared-padding test. Arbitrary multi-shared data prefixes cannot inherit A077's factor2 without an additional exclusive source reserve. Selected-coordinate Q payment for arbitrary Boolean roots, hereditary paid selection, and all terminal core entropy remain open. NEXT must select or own the shared-core reserve at bad rare queries; another bounded-H/I class scan cannot address this gap.
