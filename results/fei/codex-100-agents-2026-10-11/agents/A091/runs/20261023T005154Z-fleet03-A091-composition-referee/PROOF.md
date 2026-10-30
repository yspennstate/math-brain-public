# Later private point query before A/Y are resolved

Rung: independent reconstruction of A057-LATER-PRIVATE-SHARED-Y-PAYMENT@1; source comparison below. Exact tests are supporting finite certificates, not the all-dimensional proof. The scalar packet inequality and physical-channel inequality are imported from the previously audited A091 stage6/C005 chain. Full FEI OPEN.

Let Y be a fresh fair bit, A ANY indicator on a finite uniform private block, and B=P(1+x)/2 where P is ANY indicator on another private block and x a fresh fair sign. Set q=EP/2 in [0,1/2]. Point events on r>=1 bits give q=2^-r as a special case. Boolean signs u,v,G occupy disjoint data blocks independent of A,P,x,Y. There is ONE actual G, repeated in the two inactive histories. All means, including constants, are allowed. Define

    F=(1-Y)G+Y[A u+(1-A)(B v+(1-B)G)],
    a=EA, c=1-a, m=Eu, n=Ev, z=EG,
    delta=n-z, M=1-nz, Vv=1-n^2, VG=1-z^2.

For each remaining B coordinate i, its actual influence is

    d=q c M/2.                                           (1)

Indeed its derivative is the product Y(1-A)B_rest(v-G)/2, and E(v-G)^2=2M. The theorem is

    B_i(F)<=(8+8a)d<=16d,
    D_i H(F)<= (8+8a+2/ln2)d <(11+8a)d when d>0.         (2)

For a<=1/2 this is B_i<=12d and D_i<=(12+2/ln2)d. The stage17 earlier-A bound is unchanged. The initial weaker16d reconstruction came from dropping a<=1 in two sectors; retaining a recovers A057's exact source constant, not a changed physical influence.

## Exact frequency partition

Set

    Pq=Phi((1-q)^2,q^2), H=(1-q)z+qn,
    K=a m+c H, w=q c delta,
    RG=[Phi((1+c(1-q))^2,q^2 c^2)
          +Phi((1-c(1-q))^2,q^2 c^2)]/4,
    R0=[Phi((z+K)^2,w^2)+Phi((K-z)^2,w^2)]/4,
    RM=Phi((m-z-q delta)^2,q^2 delta^2).

With Phi(x,y)=eta(x)+eta(y)-eta(x+y), eta(x)=-x log2 x and eta(0)=0, the complete exact identity is

    B_i=(q-2q^2)cM+q^2 c Vv
          +(ac VG/2)Pq+VG RG+(ac/2)RM+R0.               (3)

Derivation: expand around B as F=K_phys+B E_phys(v-G), where E_phys=Y(1-A), K_phys=G+YA(u-G). At nonempty P frequencies both queried amplitudes have equal squared magnitude. Their total erasure is [sum_nonempty Phat(T)^2/2]||E_phys(v-G)||_2^2=(EP-(EP)^2)cM/2=(q-2q^2)cM. At empty P frequency, the paired amplitudes are K_phys+q E_phys(v-G) and q E_phys(v-G). Thus no flatness or point geometry of P is used.

Nonempty u-data frequencies have odd queried amplitude zero and hence no erasure. Nonempty v-data frequencies have identical even/odd queried squared amplitudes, totaling 2q^2 E[E_phys^2]Vv=q^2 c Vv. For nonempty G-data frequencies and nonempty A frequencies the even/odd multipliers are -(1-q)Ahat(T)/2 and -q Ahat(T)/2 at either Y frequency; summing Ahat(T)^2=ac gives (ac VG/2)P. At empty A frequency, those two Y packets give VG RG. The empty-data, nonempty-A sector has even/odd multipliers (m-z-q delta)Ahat(T)/2 and -q delta Ahat(T)/2 at either Y frequency, yielding (ac/2)RM. Finally the empty-data/empty-A sector yields R0. These sectors exhaust the physical Fourier basis, without creating a second G. Only indicator Parseval is used for A, so A's width and internal geometry are arbitrary.

## Dimension-free charge and side conditions

The imported scalar bound Phi(s^2,t^2)<=2|st| holds in bits, including zeros. All sectors in (3) are nonnegative, because 0<q<=1/2. For independent signs with means n,z in [-1,1],

    Vv<=2M, VG<=2M, |delta|<=M, M>=0.                  (4)

The variance inequalities follow from 2M-Vv=(n-z)^2+VG and its symmetric counterpart. For the last inequality, M^2-delta^2=Vv VG>=0 and M>=0; no division is used. Since H is a convex combination of z,n and K of m,H, both have absolute value<=1, and |m-H|<=2.

Group the first two terms of (3):

    (q-2q^2)cM+q^2 c Vv <=qcM=2d.                    (5)

The nonempty-A G sector obeys

    (ac VG/2)Pq <=ac q(1-q)VG <=aqc VG<=2aqcM=4ad.   (6)

The empty-A G sector uses 0<=c(1-q)<=1 and
|1+x|+|1-x|=2 there, hence RG<=qc. Thus

    VG RG<=qc VG<=4d.                                (7)

The nonempty-A mean sector obeys

    (ac/2)RM <=ac q |m-H| |delta|
               <=2acq |delta|<=2aqcM=4ad.            (8)

For the last mean sector, |z+K|+|K-z|=2max(|z|,|K|), so

    R0<=|w|max(|z|,|K|)<=qc|delta|<=qcM=2d.          (9)

Adding (5)-(9) gives 2+4a+4+4a+2=8+8a. The actual physical child-channel identity D_i=B_i+J_i, with J_i<=2d/ln2, proves (2). This uses no unused child surplus, tiny-influence normalization or discarded terminal. If a=1 then c=0 and every sector is zero, regardless of u/G. If M=0 then v and G are equal constants and all sectors again vanish, even with nonconstant u. If q=0 all sectors vanish directly. The cases a=0, q=1/2, all constant-core signs, and arbitrary prior physical DATA restrictions preserving the disjoint-block representation are included. With B already failed, the putative query is irrelevant and has zero charge; with B resolved there is no remaining B coordinate to query.

## Original fine reserve, old debits and both terminals

Let G have an original fine selector on independent private blocks with fine-core probabilities t_l and variances V_l. Set ZG=sum t_l V_l; take ZG=VG when G is one core. In the physically MERGED fine label law, u has mass a/2, v has mass cq/2 and each G-core has mass t_l s, where

    s=(1+c(1-q))/2,
    s0=(1+c)/2,
    s1=(1+c(1-2q))/2.

The original reserve R=sum eta(label mass) Var(label core) has release

    kappa=R-(R0_child+R1_child)/2
          =cq Vv/2+[eta(s)-(eta(s0)+eta(s1))/2]ZG >=0. (10)

All log(t_l) factors cancel because s=(s0+s1)/2, and concavity proves the sign, including zero masses by eta(0)=0. The u-label contribution is unchanged. The inherited U=sum label_mass[H(core)-eta(mean(core)^2)] is harmonic at this controller reveal. Consequently

    (H-U-R)_parent - E(H-U-R)_child
       =D_i-kappa <=(8+8a+2/ln2)d.                  (11)

Equation (11) retains the two actual child H-U-R quantities in full and spends no additional ancestor reserve. Previous debits are neither erased nor reissued. G's inactive-Y and active-failure occurrences are merged BEFORE entropy, not treated as independent copies. Terminal U funding and unresolved fine G entropy remain obligations; constant current cores alone do not resolve an unqueried controller. No FEI-certified universal terminal is asserted.

## Version and remaining universal step

This independently validates A057's adjacent later-B interface while preserving the earlier-A theorem unchanged. It creates no new broad candidate. Source A057 PROOF.md uses an L1 overlap bound for K_phys,D_phys. The reconstruction above instead partitions every actual erasure packet into data/controller sectors, with a separate direct-character implementation. Both derive the same coefficient for arbitrary P and A. The original exact claim/hash is preserved in the review record. The A057 stopped extension Section5 remains conditional on its imported DATA and after-Y theorems; reviewing Sections1-4 alone does not independently accept that entire dependency chain.

First unsupported line: for a point query after an arbitrary-length earlier priority prefix while Y is hidden, the complete coherent earlier-profile packets are bounded at a dimension- and prefix-length-independent rate with the SAME merged fallback law and both terminals. The direct |m-H|<=2 bound above concerns one earlier selected core; summing it over all earlier labels would risk a prefix-length factor. The shortest continuation is to combine the actual repeated-G packet with A059's last-nonempty-block log-moment mechanism, preserving original ownership rather than enumerating a third fixed-width class.
