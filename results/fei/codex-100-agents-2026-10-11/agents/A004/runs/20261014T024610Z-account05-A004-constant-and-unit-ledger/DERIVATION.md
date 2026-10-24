# One owner for the partner-KL and unlocked-shadow bills

All functions below are actual Boolean signs on disjoint uniform physical cubes. Entropy and KL are in bits; influence is ordinary flip probability. No conditional spectral law is assumed to be a Boolean spectrum.

## 1. Independent review of A096's partner ownership

Let g(z,y)=A(y)+zD(y), with actual children g_+,g_- and delta=I_z(g)=E D^2. Its squared Fourier row has entries a_T=Ahat(T)^2, b_T=Dhat(T)^2; sum a=1-delta, sum b=delta. Define

    B_z=sum_T Phi(a_T,b_T),
    M_z=sum_(b_T>0) b_T log2((a_T+b_T)/b_T),
    C_z=sum_(a_T>0) a_T log2((a_T+b_T)/a_T).

For delta>0 the complete reference r_T=a_T+b_T and derivative mu_T=b_T/delta both normalize to one. Direct expansion gives M_z=delta[log2(1/delta)-D(mu||r)]. No conditioning of r on derivative support occurs. Zero terms are continuous; delta=0 gives B=M=C=0.

Replace z by u v physically. Character expansion gives only two occupied types in the duplicated u row: reference a_T at partner absent, b_T at partner present; derivative has only b_T/delta at partner present. Hence its full KL is log2(1/delta), its M_u=0, and B_u=0. Marginalizing partner occupancy gives exactly the original complete r and mu, so its influence-weighted KL loss is precisely M_z. In the opposite quotient, keeping only partner occupancy gives derivative (0,1) and reference (1-delta,delta). Its KL remains log2(1/delta), hence zero loss. The derivative-free reference mass is retained.

This representation proves the whole partial-substitution formula for an arbitrary J: H is preserved by injective spectral embedding; duplicated bits each have influence e_i; unduplicated rows are deterministically relabelled. Therefore I_new=I_old+sum_J e_i and M_new=M_old-sum_J M_i. Summing both duplicated partner losses gives 2sum_J M_i. If every coordinate is duplicated, division by I_new=2I_old yields M_old/I_old. Independent common spectator factors cancel in the KL ratio; they do not change the binary quotient. This independently reconstructs A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1 without repair.

For A096's witness, d even, delta=2^-d, b(y)=(-1)^(sum y_(2j-1)y_(2j)), g(s,y)=b(y)-1_(y=0)+s1_(y=0). Tensoring the quadratic two-bit spectrum gives b_hat=epsilon sqrt(delta). Thus a_T=(epsilon sqrt(delta)-delta)^2, b_T=delta^2, r_T=delta[1-2epsilon sqrt(delta)+2delta]. For sqrt(delta)<=1/2, the bracket is >=1/2, so M_s>=delta(d-1). Nonnegative KL gives M_s<=delta d. Both signs epsilon occur, making partner/core correlation genuine. Every data bit has influence 1/2+delta because the flipped child adds one previously nonpivotal edge at the origin. Consequently G(u,v,y)=g(uv,y) has I=d/2+(d+2)delta and H<=d+1, hence H/I<=3. These are all-dimensional proofs; the finite cases are corroboration. No FEI counterfamily is asserted.

## 2. The two accounts differ by exactly one reverse-row correction

The elementary packet identity gives

    B_z=M_z+C_z,      0<=C_z<=delta/ln2.             (1)

Indeed a ln(1+b/a)<=b, summed over a>0; terms with a=0 contribute zero C. Thus this correction is a single physical influence price. It is not a second independent copy of M_z.

Now choose any fresh balanced Boolean encoder h(x), and construct the actual function

    F(x,u,y)=g(u h(x),y).

Query the physical partner u first, then resolve the encoder with any complete physical policy, leaving y untouched. The auxiliary initial uniform shadow f(z,u,y)=g(zu,y) has B_z=0 by parity embedding. After u is revealed, its two shadows are g(z,y),g(-z,y), both with B_z(g). With Var(h_root)=1 and Var(h_leaf)=0, the variance martingale gives the total A026/A003 encoder shadow charge

    Q_shadow=sum_nodes w gamma_node^2 B_z(g)=B_z(g).

The signed data debit of the u query is -B_z(g). The corresponding A096 loss on the parity-pair shadow is L_partner=M_z(g). Therefore

    Q_shadow-L_partner=C_z(g),
    L_partner<=Q_shadow<=L_partner+delta/ln2.        (2)

This compares named source bills at the SAME original seed row. It does not identify L_partner with a new marginalization of the already encoded F row. For encoded F its derivative contains the encoder spectrum, so that distinction is essential. Nor does (2) assign a physical query to the auxiliary z.

For any balanced h, the actual unlocking query u has zero erasure and zero JS: inactive Fourier support has empty encoder index, whereas active support has nonempty encoder index. The physical influence of u is delta. After u, the signed shift changes no squared coefficients while h is balanced, so actual child entropy equals root entropy. Direct separated spectrum and physical flips give

    H(F)=H(g)+delta H(h),
    I(F)=I(g)+delta I(h).

These are used as checks of actual reach weights and terminal law, not claimed as new activation/selector baseline theorems. Complete encoder resolution and balanced h give actual terminal children g_+,g_- with weights 1/2 each, regardless of encoder policy. Their mean influence is I(g)-delta. Every terminal entropy is retained.

## 3. Exact conditional surplus criterion

Write J_z(g)=H(g)-[H(g_+)+H(g_-)]/2-B_z(g), the ordinary nonnegative JS, with J_z<=2delta/ln2. Let K be any chosen bit-entropy price per unit physical influence, and define the actual terminal surplus

    T_K=E_leaf[K I(g_leaf)-H(g_leaf)]
       =K[I(g)-delta]-[H(g_+)+H(g_-)]/2.

Let E_h be cumulative inherited encoder erasure on the complete encoder policy (on h itself, with its actual fair weights). Then the bank presented by the shadow interface is Q_shadow+delta E_h=B_z+delta E_h. Using Delta_z H=B_z+J_z gives the exact identity

    T_K-[B_z+delta E_h]
       =[K I(g)-H(g)]+J_z-(K+E_h)delta.            (3)

For the partner-KL version of the bank,

    T_K-[M_z+delta E_h]
       =[K I(g)-H(g)]+J_z+C_z-(K+E_h)delta.        (4)

Thus a single explicitly assigned terminal surplus pays the WHOLE shadow-plus-inherited bank iff the RHS of (3) is nonnegative. The KL bank passes the weaker criterion (4); transferring its success to the shadow bank requires retaining C_z exactly once. Neither nonnegative child surplus nor a positive seed surplus automatically supplies the required amount. These are tests of this particular exclusive terminal payment mechanism, not necessary conditions for FEI or for another physical stopping policy.

For h=Maj3, E_h=1 under every complete adaptive encoder policy. The first query has erasure zero; the remaining two-bit slices each have erasure one at their next query; their final one-bit or constant spectra have erasure zero. Also H(h)=2, I(h)=3/2, so spent unlocking-plus-encoder influence is (5/2)delta. Equations (3)-(4) become seed surplus + J_z -(K+1)delta and the same plus C_z.

## 4. Exact AND2 boundary: a constant-free substitution fails

Take g on two physical bits with one positive vertex and three negative vertices; choose either coordinate as z. This is the sign version of AND2 up to sign/orientation. Its four squared Fourier masses are 1/4, so H(g)=2, I(g)=1, delta=1/2, B_z=1, M_z=1/2, C_z=1/2, J_z=1. The actual terminal children are a constant and a dictator. Both satisfy H<=2I individually, and their mean K=2 terminal surplus is T_2=1.

For Maj3 the inherited bill is delta E_h=1/2. Hence

    T_2-[M_z+delta]=0,
    T_2-[B_z+delta]=-1/2.                          (5)

This actual Boolean certificate rules out replacing the partner-KL bank by the unlocked-shadow bank at an unchanged terminal allowance, even when every terminal child is K=2-certified. The difference is exactly C_z. The root F has H=3 and I=7/4, so H/I=12/7: the failed exclusive reserve is not a failed FEI inequality. No claim that A003 made this false substitution is implied; its report explicitly leaves arbitrary-seed reserve sufficiency open.

For A003's bent-flip control at every even d>=4, the actual terminal S2>=2d delta since each child entropy is <=d. Also B_z<=h2(delta)<=delta[d+log2(e)], so B_z+delta<2d delta. Consequently the same terminal owner pays both versions, and their difference remains the single C_z correction. This reconstructs the control's payment and shows why its favorable margin cannot be extrapolated to all child-certified seeds.

## 5. Units and endpoint guards

In natural logs, (1) is 0<=C_nat<=delta, (2) has one nat per influence as its safe additive price, and E_h(Maj3)=ln2. If K is now in nats, the RHS of (3) is K I(g)-H_nat(g)+J_nat-(K+ln2)delta. The AND2 shortage is (ln2)/2 nats. Converting an existing bit K to nats multiplies K by ln2; physical pivotal influence stays fixed. Indicator unnormalized Dirichlet energy is a quarter of the sign energy, so an RHS coefficient using that energy is four times the pivotal coefficient. Indicator raw squared masses still are not a normalized spectral law.

At constants delta=0, both bills and the inherited contribution vanish. At a distinguished dictator or parity coordinate, delta=1, B=M=C=J=0; entropy resides in actual descendants as appropriate, and the inherited encoder charge may still be positive. For nearly constant seeds, all formulas are exact with arbitrarily small positive delta; there is no division by variance or omission of the empty spectral atom. Actual terminal H is h2(v)+vH(R), and any B/DTC split must retain their opposite T0 corrections at identical leaf laws and weights. The proof and checker use full normalized law H throughout.

## 6. First unsupported universal line

No proof supplies nonnegative RHS (3), or an alternative owned amount covering its negative part, under a universal constructive physical query policy and one unused influence reserve. AND2 shows mere child certification is insufficient for this exclusive terminal-only mechanism. The partner KL loss, shadow debit, inherited encoder erasure, actual data erasure, and complete terminal entropy must remain in one signed account. Full FEI, C018 and C019 remain open. NEXT is to derive a policy-dependent remainder from actual certified child slack after the first outer-data exposure, rather than dropping C_z or charging the same terminal surplus twice.
