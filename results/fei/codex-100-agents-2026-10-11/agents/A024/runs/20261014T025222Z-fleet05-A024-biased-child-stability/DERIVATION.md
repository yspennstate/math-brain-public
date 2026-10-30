# Biased-child mixed-face derivation (unfinished stage 2 resumed in stage 4)

Physical inputs remain uniform. Use odd-face credit q_x(f)=I(f_0 f_1)/2 and event-boundary influence J(W)=I(1-2W), not the Fourier Dirichlet energy of a 0/1 indicator.

For disjoint F=A(z)+B(z)h(u), with AB=0,A^2+B^2=1 and W=B^2, t=E W, a query x inside h has

    F_0 F_1 = 1+W(h_0 h_1-1),
    q_x(F)=t q_x(h)+(Inf_x(h)/2) J(W).                 (1)

This is an actual Boolean activation of the disagreement product. Interior h edges contribute t I(h_0h_1), and z edges contribute Pr(h_0!=h_1) J(W). No independence of child spectra is required. The two blocks are physically disjoint.

More generally for F=g(f_1,...,f_k), define a_i=E(D_i g)^2 over other output means, and gamma_ij=Pr_{other outputs}[the four gate values in directions i,j multiply to -1]. Then

    Q(F)=sum_i a_i Q(f_i)+(1/2)sum_{i<j} gamma_ij I(f_i) I(f_j). (2)

Same-block faces preserve a child's oddness exactly when the gate is nonconstant in that output. A mixed face is odd precisely when both child physical edges flip and the gate face is odd. Equation (2) counts the faces by their actual two directions and has no normalization singularity at deterministic means. Mixed faces are spent on the first queried direction of that face; they are not a second influence reserve.

Frozen selector module c(s,x), x in {0,1}^4: b(x)=(-1)^(x0*x1+x2*x3), c(0,x)=b(x), c(1,x)=b(x) except the point x=0 is flipped. Let d=1/16, m=3/16, I(c)=37/16, and q_s(c)=4d=1/4. Its selector erasure is

    B_*=[10(10 log2(10)-9 log2(9))
          +6(26 log2(26)-25 log2(25))]/256 > 1/4=4d.   (3)

The sign in (3) will be certified with rational logarithm intervals; the exact spectrum has ten fibers (9,1)/256 and six fibers (25,1)/256.

Let G_L be the product of L independent copies of c. Let P_N be parity on N fresh bits. Define

    F_{L,N}=1-[(1+P_N)/2](1-G_L), L,N>=1.

The outer gate is a genuine disjoint two-input Boolean gate. Root influence is

    I(F_{L,N})=[(37/16)L+(1-(3/16)^L)N]/2.             (4)

Consider the fixed complete order: all L selectors first, then all module data, then the N parity bits. At any selector node before module data, the means of other modules are in {3/16,1/4,1/8}. Thus |M|<=3/16 and beta=-M/3 for the currently queried selector. The stage-1 bias residual is exactly

    R(M,beta)=[Lbin(1+M,beta)+Lbin(M-1,beta)]/4
                  -Lbin(M,beta)/2 >=0,
    Lbin(a,b)=(a^2+b^2)h2(b^2/(a^2+b^2)).              (5)

The inequality follows since |1+-M|>=|M| when |M|<=1/2 and Lbin increases in its first squared argument. Therefore B_s(F)=B_*/2+R>4(d/2): every one of those selector nodes is bad at K=4, despite its mean-log bank becoming exponentially small with L.

At each such node q_s(F)=d(4+N)/2, by (1), independent of the selected branch history. The selectors alone spend

    Q_bad >= L d(4+N)/2.

Taking N=L^2 gives

    Q_bad/I(F) >= [L d(4+L^2)]/[(37/16)L+(1-(3/16)^L)L^2]
                 >= L/53 -> infinity.                (6)

This disproves a uniform bound for EVERY tree, and in particular a core-first rule; it does not disprove the lead's SOME-tree localized bridge or FEI.

The mean bank is not the divergent bill. At every one of these selector nodes, beta^2<=16^(-(L+1)). Using Lbin(a,b)<=b^2[log2((a^2+b^2)/b^2)+log2(e)] and dropping only its negative subtraction yields

    0<=R<=(2L+4)16^(-(L+1)).                           (7)

Here (1+|M|)^2+beta^2<5, log2(5e)<4 (e<3), and u log(5e/u) is increasing on this tiny interval. Thus their total expected signed bias bank is at most L(2L+4)16^(-(L+1)). The scalar subtraction Lbin(M,beta)/2 remains in the exact ledger. Since beta=-M/3, R=(beta^2/2)log2(1/M^2)+O(beta^2) as M->0, so these are genuine log(1/mean) splits and they are bad, but the divergent bill is the mixed-face term dN/2.

Compare the complete order: all parity bits first, then selectors, then module data. For N>=2, the first N-1 parity reveals have B=0, because the two parity-support sectors remain distinguishable after erasing that one coordinate. The last parity reveal has d=(1-(3/16)^L)/2>=13/32, so B<=h2(d)<=1<4d. For N=1 this last-coordinate argument applies directly. Thus no parity reveal is bad. With probability 1/2, the parity leaf is constant; otherwise it is G_L. In G_L, erasure and selector credit tensorize. Its L selectors are bad with credit 1/4 each. After all selectors, every module is b or its one-point flip on four bits. Their first data-coordinate influence is 1/2 or 5/8; after that, any relevant function on <=3 bits has influence >=1/4. Hence B<=h2(d)<=4d at every module-data node (use h2(d)<=1 for d>=1/4). These nodes are good also inside the tensor product, since B and queried influence agree with the local module values.

Consequently the parity-first COMPLETE tree has exactly

    Q_bad=L/8,
    Q_bad/I(F)=[L/4]/[(37/16)L+(1-(3/16)^L)N]<=4/37.   (8)

The K=4 quantifier is essential: (6) refutes the assertion that EVERY complete tree has O(I) bad-node credit at this fixed K. It does not refute an every-tree assertion with a different threshold K, nor the lead's existence of some absolute K,K' and some tree for each function.

## Exact erasure reconstruction and endpoint safety

For F=A+B h, let a_Z,b_Z denote the Fourier coefficients of A,B on its physically disjoint block. Write m=E h and beta=(E h_0-E h_1)/2. At a fiber with no remaining h coordinates, the two Fourier coefficients in the queried direction are a_Z+m b_Z and beta b_Z. At a nonempty remaining-h fiber, both coefficients are multiplied by b_Z. Since Lbin is homogeneous of degree two, all nonempty h fibers contribute t times their h erasure, by Parseval sum_Z b_Z^2=t. Replacing the inner empty fiber by the outer empty fibers gives exactly

    B_x(F)=t B_x(h)+sum_Z Lbin(a_Z+m b_Z,beta b_Z)
                            -t Lbin(m,beta).

This reconstructs the used clause of A024-BIASED-CHILD-TRANSPORT@1 without assuming its independent acceptance. It uses physical uniform Fourier coefficients, not a fictitious biased physical restriction. Actual child means change the law seen by the outer gate. No division by 1-m^2 occurs, and deterministic children simply contribute zero queried influence.

The seed has a stronger certificate: B_*-Lbin(3/16,1/16)>1/4, equivalent to

    2^182 * 13^156 > 5^210 * 3^162.

Indeed 256 times its margin is 182+156 log2(13)-210 log2(5)-162 log2(3). Nonnegativity of every outer Lbin fiber therefore implies B_s(F)>4 Inf_s(F) in ANY disjoint outer composition using this seed nontrivially (t>0); if t=0 both quantities vanish. The other margin B_*-1/4 is certified by 2^192 * 13^156 > 5^200 * 3^180. Both are actual integer comparisons, not rounded logarithm evidence.

For the parity activation, A=(1-P_N)/2, B=(1+P_N)/2. Its empty and full-parity fibers are (a,b)=(1/2,1/2) and (-1/2,1/2). Substitution into the reconstructed formula yields (5), with t=1/2 and the negative inner empty fiber retained. In G_L, the other tensor factor has Fourier squared mass 1, hence selector erasure and queried influence equal those of its one module. This also justifies the tensor steps in (8).

## No FEI counterexample and retained normalization

The physical spectrum of F_{L,N} is supported on at most 2*32^L sets: the parity block is either empty or full. Thus H(F)<=5L+1 bits, while I(F)>=13N/32 by (4). For N=L^2, H/I<=(32/13)(5L+1)/L^2 tends to zero. These are actual Boolean witnesses against a fixed-order credit rule only.

Throughout, corrected FEI+ is Eplus_mu(g)=sum_{S nonempty} P_mu(S) log2(product_{i in S}(1-m_i^2)/P_mu(S)), with no output-variance numerator; on uniform physical inputs H(f)=Eplus(f)+e((E f)^2). This stage prices neither the full signed JS correction nor an arbitrary inherited terminal-core deficit. Both compared trees have constant leaves, so their terminal entropy is exactly zero. A partial tree would have to retain its actual terminal entropy.

For N=L^2 the ratio tends to zero, while (6) grows linearly. Each mixed face is allocated at a good parity reveal in this order. Terminal entropy is zero in both compared complete trees. The shortest open step is a history-measurable policy that moves these mixed faces to good nodes for general biased outer modules; identifying a cheap mean bank alone cannot supply that policy.
