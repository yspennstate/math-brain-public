# Shared-data point selectors: width-dependent full stopping payment

Entropy bits, eta(x)=x log2(1/x), eta(0)=0, b=log2(e). Let s be k>=1 shared physical coordinates, X,Y disjoint private cubes. Let G(s,X),H(s,Y) be arbitrary Boolean signs and A_r the indicator of one prescribed point on r>=1 fresh uniform bits, p=2^-r. The point controls occur in neither child. Define F=A_r G+(1-A_r)H and d=Pr(G!=H), computed on the actual union data cube. Stopping when the point test is decided leaves G with weight p and H with weight 1-p.

    Pi=H(F)-pH(G)-(1-p)H(H), Q=2rp d,
    I(F)=Q+pI(G)+(1-p)I(H).

Pi is the complete expected sum of SIGNED entropy increments of that physical control-first tree. Shared data influence is already included in the weighted child influence; it is not charged a second time. The theorem is

    Pi <= [4+(4k+6b+4b/e)/r] Q.                       (1)

In particular, if r>=k, Pi<=14Q. With certified terminal bounds H(G)<=L_G I(G), H(H)<=L_H I(H), full expected path plus terminal allowance is <=max(14,L_G,L_H)I(F). The no-shared-data case k=0 remains the earlier v3 bound71/8; it need not be weakened.

## 1. Exact collision and private-energy partition

Embed the Fourier coefficients in the union data cube. Let C be the N=2^k shared-only sets; a_T=Ghat(T), c_T=Hhat(T) on C. Write t_T=a_T-c_T, m_T=p a_T+(1-p)c_T, D=sum_C t_T^2. Let V_G,V_H be the true spectral masses outside C for each child. Private nonempty sets belong to a unique branch. Parseval gives the exact ownership identity

    V_G+V_H+D=4d.                                   (2)

Conditional private independence gives 2d=E_s[1-u(s)v(s)], u=E_X G,v=E_Y H in [-1,1]. Since |u-v|<=1-uv, every shared-only coefficient obeys

    |t_T|<=2d, lambda_T=t_T^2/4<=d^2,
    Delta=sum_C lambda_T<=min(d,N d^2).              (3)

No sign folding is used here: when r>1, changing the sign of H does NOT in general permute point-selector spectral sectors. The budget and amplitudes always belong to the original Boolean pair.

At a shared-only frequency the empty selector coefficient is m_T and each of the 1/p-1 nonempty selector coefficients has magnitude p|t_T|. Private G frequencies have coefficient magnitudes p times the child coefficient in all selector sectors. Private H frequencies have magnitude (1-p) times the child coefficient in the empty sector and p times it in each nonempty sector. Direct grouping therefore proves

    Pi=2rp[V_G+(1-p)V_H+(1-p)D]+V_H eta((1-p)^2)
       +sum_C[eta(m_T^2)-p eta(a_T^2)-(1-p)eta(c_T^2)]
       +p(1-p) sum_C t_T^2 log2(1/t_T^2).           (4)

The last summand is zero when t_T=0. All possibly colliding shared-only rows, including the empty row, are present. There is no unsigned replacement of coherent amplitudes.

## 2. A raw collision entropy bound, uniform in arbitrary private dimensions

Claim: for k>=1 the subprobability atoms in (3) obey

    sum_C eta(lambda_T) <= (2k+2b/e)d.              (5)

If d=0 this is immediate. In the rare regime 0<d<=1/N, each lambda_T<=d^2<=1/4. eta is increasing on [0,1/e], and e<3<4, so

    sum eta(lambda_T)<=N eta(d^2).

Set x=Nd<=1. Dividing by d yields 2x(k-log2 x)<=2k+2b/e, using x log2(1/x)<=b/e. In the other regime d>=1/N, the entropy maximum at fixed Delta is Delta log2(N/Delta). Since Delta<=d<=1 and N/d>=1,

    Delta log2(N/Delta)
      =Delta log2(N/d)+Delta log2(d/Delta)
      <=d log2(N/d)+(b/e)d <=(2k+b/e)d.

This proves (5), including Delta=0. The elementary e<3 bound follows from 1/j!<=1/2^(j-1) for j>=2, strict for j>=3. It is used only for the increasing-eta endpoint. Unlike the literal-selector binary-entropy bound of A095, (5) is a raw entropy bound needed for all nonempty sectors of a rare point selector.

Consequently

    sum t_T^2 log2(1/t_T^2)
       =4 sum eta(lambda_T)-8Delta
       <=(8k+8b/e)d.                               (6)

The negative -8Delta is kept in the exact identity, although dropped for the upper bound. No collision influence is reused in a second account.

## 3. Proof of full width-dependent payment

For psi(x)=eta(x^2) on [-1,1], psi''(x)=-4log2|x|-6b>=-6b away from zero. psi' extends continuously across zero, so psi(x)+3b x^2 is convex on the whole interval. Applied to each row,

    sum[psi(m_T)-p psi(a_T)-(1-p)psi(c_T)]
       <=3bp(1-p)D.

Also eta((1-p)^2)<=2bp(1-p). Combining these two terms, (2) gives

    bp(1-p)[2V_H+3D] <=3bp(V_H+D)<=12bp d.

The leading term in (4) is <=8rp d by (2). Add (6) to obtain

    Pi<=8rp d+12bp d+(8k+8b/e)p d,

which is (1). This is a complete signed path bill, not a bound merely on erasure, JS or one row. Constants and equal children are included; d=0 implies F=G=H on the union cube and Pi=Q=0.

For exact rational comparisons, ln2>=2/3+2/81+2/1215=842/1215>9/13 gives b<13/9, and e>8/3 gives 1/e<3/8. Hence 6b+4b/e<65/6. If r>=k>=2, the coefficient in (1) is <=8+65/12=161/12<14. If k=1 and r>=2 it is <=4+(4+65/6)/2=137/12<14.

The remaining endpoint k=r=1 is already paid by the literal shared-data mux interface. We independently reconstruct A012 v2's at-most-two-shared-bit entropy proof, which applies by padding this one-bit intersection: for r=1 only, fold to d*=min(d,1-d). Let Delta=sum_C(a-c)^2/4 after folding, so Delta<=min(d*,4d*^2), exact noncollision erasure B_out=2(d*-Delta), and collision erasure B_C<=h2(Delta). For d*<=1/4, monotonicity of q log2(e/q)-2q below1/4 yields B/d*<=2+x[b-2log2x]<=2+2b/sqrt(e)<4, x=4d*. For d*>=1/4, maximize h2(q)-2q at q=1/5 to get B<=2d*+log2(5/4)<4d*, since (5/4)^2<2. The coefficientwise scalar JS inequality gives J<=2bd*. Thus Pi=B+J<=(4+2b)d*<7d<=14Q, since Q=d here. This accepts only A012's stated entropy-increment subclaim; no blanket grammar/reference review is claimed. The zero-folded-distance endpoints have Pi=0.

## 4. One complete normalized reference and retained terminal debt

Given normalized finite-cost core references, calibrate each shared-only atom to its true child squared coefficient. Preserve the incoming conditional law on the entire private complement and rescale to its true mass. The CE reduction is exactly categorical KL on the shared atoms plus complementary cell; hence no debt is discarded. Denote the calibrated references R_G^c,R_H^c.

On C set root masses m_T^2 at empty selector and p^2 t_T^2 at every nonempty selector. At a private G frequency T use p^2 R_G^c(T) in every selector sector. At a private H frequency use (1-p)^2 R_H^c(T) in the empty sector and p^2 R_H^c(T) in every nonempty sector. Reference mass on off-target private frequencies is retained; shared-only off-target atoms are calibrated to zero. Mixed-private frequencies receive zero. Total mass is

    pV_G+(1-p)V_H+sum_C[m_T^2+p(1-p)t_T^2]=1.

Probability ratios in private sectors cancel their respective point coefficients. Consequently

    D(P_F||R_F)=pD(P_G||R_G^c)+(1-p)D(P_H||R_H^c),
    CE_F=pCE_G_cal+(1-p)CE_H_cal+Pi.                 (7)

Thus (1), and rate14 when r>=k, apply equally to this complete ideal spectral reference with both terminal debts retained. It does not encode the physical transcript or include integer prefix rounding. The reference identities are algebraic, not an empirical extrapolation. The executed finite job checks their true-spectrum specialization only.

## 5. Actual Boolean lower family: the k/r scale is necessary

This consumes the known bent/point-flip obstruction rather than presenting it again as a new literal-selector counterexample. The new parameter is arbitrary point-selector width r. For even k>=4 let G(s)=(-1)^(s1*s2+...+s_(k-1)*s_k) on binary s, H=G-2*1_{s=0}. Both are Boolean signs. Write epsilon=2^-k. All G Fourier coefficients are +/-sqrt(epsilon), all H coefficients are shifted by -2epsilon. Hence d=epsilon, V_G=V_H=0, D=4epsilon, and the last raw entropy in (4) is exactly8epsilon(k-1).

Along the interval between each pair of child coefficients, absolute value is at least sqrt(epsilon)/2 (k>=4). Therefore psi''<=2k+4; applying the ordinary upper-curvature Jensen bound rowwise gives

    sum[psi(m)-p psi(a)-(1-p)psi(c)]
       >=-(k+2)p(1-p)D.

Equation (4) now proves, for every r>=1,

    Pi/Q >=(1-p)[4+2(k-4)/r].                      (8)

For any sequence k/r->infinity with even k>=4 the actual point-selector-only payment ratio diverges. Thus r=Omega(k) is necessary in scale for a bound covering arbitrary shared children, and (1) makes it sufficient. The full FEI ratio does not diverge: the substantial weighted bent/edited-child influence is retained. It may fund an additional owned slack bank, but this stage does not assume that payment.

## 6. Stopping admission and the honest first unsupported line

A finite recursive certificate may use point-selector blocks with shared child-support intersection k and width r>=k, the v3 disjoint selector blocks, certified terminal functions, and disjoint products/signs. Applying (1) and (7) at each complete block gives depth-independent full entropy/reference rate max(14,terminal rates). Each shared physical data coordinate remains inside the actual weighted terminal influence. This supplies stopping trees ending in any supplied checked regular, bounded-overlap or threshold-formula class, without treating an arbitrary opaque seed as certified.

The width-domination condition is NOT preserved by every physical restriction: fixing active controls shrinks r while leaving k intact. A surviving partial point-test node may therefore fail the local coefficient, although the original whole-block payment is valid. No hereditary admission, arbitrary interleaving or all-coordinate good-step theorem follows. This is precisely where a nonlocal block stops past possibly expensive intermediate restrictions.

First unsupported universal line: when r<<k, the excess raw collision entropy in (4) is paid by one named UNUSED signed terminal-core reserve, transported through the actual control/data history without changing terminal weights or spending the shared influence twice. The lower family rules out replacing this reserve with a fixed selector-only allowance. General controller substitution and universal terminal FEI remain open.
