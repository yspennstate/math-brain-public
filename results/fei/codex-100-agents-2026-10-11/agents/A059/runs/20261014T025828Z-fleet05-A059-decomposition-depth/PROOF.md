# Fine-state control payment under a shared point gate

All entropies and KL divergences are bits. Let an arbitrary finite internal
controller partition its cube into states C_j, with Boolean outputs u_j on
disjoint independent data cubes. Constant states are allowed. Define
P=sum_j C_j u_j. Put p_j=E C_j, m_j=E u_j, V_j=1-m_j^2,

    M=E P=sum p_j m_j,
    Vbar=sum p_j V_j,
    L=sum p_j(m_j-M)^2=Var(P)-Vbar.

An independent r-bit point gate activates this WHOLE controller:

    F=1+A_r(P-1).

The fine exclusive states of F are A_r C_j plus the inactive constant +1 state.
At any actual cylinder after arbitrary internal-control and data restrictions,
and after successful outer point controls, s>=1 outer gate bits remain,
q=2^-s. All quantities below refer to those ACTUAL restricted functions.
Failed gate branches are constant +1 and have zero charges. Bias endpoints,
empty states and constant cores are included.

## 1. Exact fine/coarse release correction

Use the A059 reserve R=sum eta(q_j)V_j, eta(x)=x log2(1/x).
At an outer gate query the active fine probability p_j q doubles on the success
slice and vanishes on failure. Constant states have V=0, including merged
inactive/active +1 labels. Hence the actual fine release is

    kappa_fine=q Vbar.

Treating P as ONE Boolean core would instead release kappa_coarse=q Var(P).
Thus the exact missing release is

    kappa_coarse-kappa_fine=q L>=0.                          (1)

This is the law-of-total-variance merging correction. It must be included;
the single-core residual formula cannot be applied with kappa_fine unchanged.
No entropy or influence assumption is made on the arbitrary internal P.

## 2. The same residual constant pays the correction

Set a=1-M and z=qa. Actual queried influence is z. Splitting physical Fourier
pairs of the queried outer bit into nonempty P-frequencies, nonempty remaining
outer frequencies with empty P-frequency, and the fully empty pair gives

    B_outer-kappa_fine
      =(q-2q^2)a^2+qL+Phi((1-z)^2,z^2),                    (2)
    Phi(A,B)=(A+B)h2(B/(A+B)).

The q Var(P) contribution of nonempty P-frequencies is the only place that
the fine/coarse distinction enters. Multiplicities of equal point-indicator
coefficients give the other terms. Since q<=1/2, all terms in (2) are
nonnegative. Crucially L<=Var(P)=2a-a^2, so

    (q-2q^2)a^2+qL<=2qa-2q^2a^2=2z(1-z).

The existing scalar packet bound

    2z(1-z)+Phi((1-z)^2,z^2)<=3z, 0<=z<=1                 (3)

therefore absorbs the entire merging correction with NO increased constant.
For clarity, (3) follows as follows. On [1/4,1/2], Phi(A,B)<=2sqrt(AB)
gives the bound 4z(1-z)<=3z. On (0,1/4], Phi<=B log2(e(A+B)/B) and A+B<=1
give b(z)/z<=2(1-z)+z[2log2(1/z)+1/ln2], increasing up to an endpoint
5/2+1/(4ln2)<3. On [1/2,1], symmetry uses the already bounded 1-z. The
Phi<=2sqrt(AB) inequality is the homogeneous binary entropy inequality
h2(t)<=2sqrt(t(1-t)); it can also be derived from the two-point scalar bound.
This scalar is reconstructed from A091, not claimed as a new optimization.

The actual physical child-channel gap J obeys 0<=J<=2z/ln2, by the
JS-Hellinger scalar inequality on the normalized full Fourier law. Therefore

    0<=D_outer-kappa_fine<=(3+2/ln2) Inf_outer.             (4)

Equation (4) remains valid after ANY internal-controller/data interleaving.
It prices the fine-state residual at the same rate as A091's single-core point
payment. It is not a price for arbitrary internal controller coordinates.

## 3. Exact terminal conversion under grouping

Let U_P=sum p_j[H(u_j)-eta(m_j^2)] and R_P=sum eta(p_j)V_j.
Let T_P=H(P)-U_P-R_P, the actual unresolved internal terminal profile. At F,

    U_fine=q U_P,
    R_fine=q s Vbar+q R_P,
    U_coarse=q[H(P)-eta(M^2)],
    R_coarse=q s Var(P).

Consequently the terminal correction T=H-U-R satisfies the exact conversion

    T_fine(F)-T_coarse(F)
       =q[T_P-eta(M^2)+sL].                               (5)

Here T_P-eta(M^2)>=0, by the empty-data profile coefficient factorization
reviewed from A091: the removed coefficient is exactly the completely empty
mean-profile coefficient, and every remaining raw term is nonnegative.
Thus a merged-core terminal cannot silently replace the finer actual frontier.
If the internal state is resolved, L=0 and T_P=eta(M^2), so the conversion
vanishes. If only the outer gate is resolved, the internal T_P remains.

In the priority example P=A u+(1-A)[1+B(v-1)], the three active probabilities
are p, (1-p)b and (1-p)(1-b), and the active means are m_u,m_v,1. A shared
fair outer bit is s=1. Formulas (1)-(5) explicitly pay the mixed shared-bit
debit sought by A091 without substituting the wrong one-core release.

## 4. Stopped ledger with the internal residual still visible

On any finite adaptive physical tree distinguish outer point-gate queries,
internal controller queries, and actual data queries. Keep the ORIGINAL fine
U,R throughout. The previously reviewed A059 data inequality and (4) give

    H(F_root)<=U_root+R_root+(3/ln2)T_data
              +(3+2/ln2)Pi_outer
              +sum_internal-controller w(D-kappa_fine)
              +E[H_leaf-U_leaf-R_leaf].                   (6)

T_data=sum_data w q_j beta_j^2<=Pi_data. On the same physical tree
I_root=Pi_data+Pi_outer+Pi_internal+E I_leaf. The fine reserve retains its
exact conservation identity; it is NOT funded a second time when grouping P.
If the actual full controller labels are resolved at leaves, the final profile
is eta(m_leaf^2)<=I_leaf/ln2, as independently reviewed from A091.

The new result is the merging correction, its unchanged local residual price,
and the exact unresolved-terminal conversion (5). The internal-controller
sum, inherited arbitrary U_root and unresolved terminal T are not paid here.
Setting all cores to constants still allows P to be an arbitrary Boolean
controller, which explains the remaining universal gap.

## 5. A trap for repeatedly reopening the merging potential

The apparent merging potential A=s q L is not a supermartingale under DATA
queries. For a query in core j with squared singleton t,

    E L_child-L=p_j(1-p_j)t,
    E A_child-A=s q p_j(1-p_j)t.                           (7)

Actual queried influence of F is q p_j Inf_i(u_j). No fixed constant bounds
the increase in (7) by that influence, even for independent literal cores.
Take P to select two independent balanced literals equiprobably by one fair
internal controller bit. Initially L=0. Query the first literal: t=d=1,
E L_child=1/4, and the increase/influence ratio is s/2, tending to infinity.
This is an actual Boolean growing-depth family of dimension s+3. It disproves
the LOCAL helper, not the original fine reserve or (4).

The joint R_fine+A has nonnegative expected data loss
q[s p_j^2+p_j log2(1/p_j)]t; this algebra does not license replacing the
larger fine data charge by that smaller loss. Formula (4) bypasses reopening
A: its entire qL correction is absorbed by the physical scalar packet bound.
Do not repeatedly charge a new coarse-core variance at each reveal.

## Provenance reconciliation and universal gap

After completing this reconstruction, A087's 20261014T020842Z source was
read in full: its killed-child theorem already subsumes the mixed outer
gate price. That price is therefore a consumed baseline, not a novel claim.
The exact terminal grouping and mean-migration counterexample remain useful
ancillary calculations. PRIORITY_PROOF.md advances A087's explicit next
gap: a private point test interrupted by data while both children reuse the
same fallback. Arbitrary-controller/full FEI remains open.
