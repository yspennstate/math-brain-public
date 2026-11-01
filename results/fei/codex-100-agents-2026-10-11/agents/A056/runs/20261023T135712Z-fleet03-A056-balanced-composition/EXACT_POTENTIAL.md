# Exact mark-randomness potential and sharp total overhead

Continue DERIVATION.md with the same original-set witness, physical keep/reselect kernel, supporting references and complete terminal CE bills. All information is in bits. This sharpens equation10; it does not price the initial reference. Define, for integer d>=0,

    m(0)=m(1)=0; m(d)=sum_(j=2..d) log2(j-1)/j,
    M(P)=sum_S P(S)m(|S|).

The physical pair identity P_0(T)+P_1(T)=2(P(T)+P(T+i)) gives directly

    M(P)-average_t M(P_t)
       =sum_(i in S,|S|>=2) P(S)[m(|S|)-m(|S|-1)]
       =rho_i.                                             (11)

This equality includes singleton and empty atoms and does not use reference masses or a balancing assumption. Along every finite adaptive physical tree, induction and actual reach probabilities give

    sum reach*rho_i = M(P_root)-E M(P_leaf).                 (12)

Thus the ENTIRE extra mark-reselection randomness is determined by the original degree law and the retained terminal degree law. This is an exact potential, not a renewed bank per child. For complete trees ending in constant functions M(P_leaf)=0.

Set w(0)=w(1)=0 and w(d)=log2(d)+m(d) for d>=2. The lifted CE ledger in equation7 plus the explicitly charged mark-reselection entropy has the exact value

    total combined bill
       =CE(P_root,R_root)+E_(S~P_root)w(|S|)-E M(P_leaf).
                                                               (13)

Indeed the CE ledger is rootCE+L_root and (12) is the additional invoice. Its terminal CE already includes the terminal L; this explains why the last term is M_leaf, not L_leaf+M_leaf. The randomness of the original spectral outcome channel kappa and integer prefix-free code lengths are still excluded, exactly as in DERIVATION.md. No executable sampler is asserted.

There is a sharp universal pointwise bound w(d)<=c_* d for every nonnegative integer d, where

    c_* = [log2(5)+(1/4)log2(3)+11/15]/5
         =0.69030041068... <7/10.                            (14)

The decimal is orientation only. To prove the bound for ALL integers, write a_d=h2(1/d) for d>=2. Direct expansion gives

    w(d)-w(d-1)=log2(d)-(d-1)log2(d-1)/d=a_d.

The sequence a_d decreases for d>=2 because binary entropy increases on [0,1/2]. For b_d=(d-1)a_d-w(d-1),

    b_(d+1)-b_d=d(a_(d+1)-a_d)<0.

The sign of b_d is the sign of w(d)/d-w(d-1)/(d-1). Two exact integer comparisons locate its unique crossing:

    60 b_5=240log2(5)-524log2(2)-15log2(3)>0,
       because 5^240>2^524*3^15;
    -60 b_6=310log2(5)-285log2(3)-256log2(2)>0,
       because 5^310>3^285*2^256.

Consequently w(d)/d increases strictly up to d=5 and decreases strictly thereafter. Its unique maximum is w(5)/5=c_*. Finally c_*<7/10 is equivalent to 5^60*3^15<2^166. These comparisons are performed with exact integers in code/potential.py, not inferred from numerical logarithms.

Combining (13),(14) proves the sharpened conditional universal bridge

    total combined bill
        <=CE(P_root,R_root)+c_* I_root-E M(P_leaf)
        <=CE(P_root,R_root)+(7/10)I_root.                    (15)

The overhead coefficient c_* is optimal for THIS explicit kernel and accounting convention: take the actual Boolean function parity_5, whose spectrum is the single five-element set and whose influence is5. A complete physical restriction tree has L_root=log2(5), M_root=11/15+log2(3)/4, and M_leaf=0, so combined bill minus rootCE is exactly5c_*. This proves sharpness regardless of the supporting initial reference. It does not prove optimality among different witness kernels or different accounting conventions.

If a universal initial source CE(P,R)<=C I were supplied, (15) would give the combined conditional rate C+c_* (or C+7/10). That premise remains unpaid and is FEI-equivalent without additional Boolean structure. Neither the sharp transport constant nor its parity witness is a proof or disproof of full FEI.

FROZEN_POTENTIAL.json predates this extension's bounded job. code/potential.py checks the degree identities and maximum through64, the three exact integer guards, the exact potential drift on all physical coordinates of all256 three-bit functions (twice, once per stored reference tree), and total M_root against all512 previously stored complete-tree reselection bills. The all-integer maximum and all-dimensional adaptive-tree assertions are the analytic proofs above; the finite checks are supporting certificates, with author reconstruction only.
