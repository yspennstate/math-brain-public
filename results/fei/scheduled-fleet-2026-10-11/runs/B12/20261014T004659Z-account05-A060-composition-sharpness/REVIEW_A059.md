# Scoped independent reconstruction of A059's signed DATA drift

Source: A059-INTERLEAVED-BIASED-STOPPING-RESERVE@1, run 20261013T235852Z-account05-A059-decomposition-depth, PROOF Sections 1-3. Verdict: ACCEPT_AT_STATED_SCOPE for its exact U,R controller/data identities and one-step signed DATA inequality (6). This review does not pay the remaining controller/terminal residual, issue blanket acceptance of all bundled claims or reopen A038's already established factor-2 sharpness. Source bytes and source claim statement are pinned in out/SOURCE_RECEIPTS.json. No repair is made, and A059 remains author of that claim.

Reconstruct the one-step identity directly. At a query in selected core j, separate nonempty core frequencies from the empty frequency. The former contribute q times their actual inner entropy decrement; the empty row replaces inner amplitudes (m,beta) by (a_T,beta c_T) in the independent auxiliary cube, where a=W+m C, c=C. Thus

    D_i H(F)=q[D_i H(u)-paird(m,beta)]+M(t)+N,
    t=beta^2,
    paird(m,beta)=eta(m^2)+eta(t)-E eta(m_child^2).

Since q is unchanged by data exposure, this is exactly

    D_i H(F)=U-E U_child+M(t)+N-q eta(t).

Conditional variance conservation supplies R-E R_child=q log2(1/q)t. Constants and zero selectors contribute zero; beta=0 gives a zero row contribution without a division.

For completeness reconstruct the analytic price without importing A059's checker. Homogeneous packet concavity and Parseval give M(V)<=h2(qV). For 0<t<=V, the scalar derivative of Phi(A,z)/z+log2(z) is [z-A ln(1+z/A)]/(z^2 ln2)>=0, so

    M(t)<=(t/V)M(V)+qt log2(V/t)
         <=qt log2(1/q)+qt/ln2+q eta(t).

The last step uses h2(x)<=x log2(e/x) and cancels log(V) exactly. At V=0 necessarily t=0.

The raw JS row with amplitudes a,b is (a^2+b^2) j(2ab/(a^2+b^2))/ln2, where j(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2. The inequality j(z)<=1-sqrt(1-z^2) follows from j'(z)=atanh(z)<=z/sqrt(1-z^2) for z>=0: their derivatives are respectively (1-z^2)^-1 and (1-z^2)^(-3/2), and both vanish at zero. Evenness and continuity handle the remaining endpoints. Consequently every row JS is <=2 min(a^2,b^2)/ln2, and N<=2qt/ln2 after Parseval on c. This proves

    D_i H(F)<=U+R-E(U_child+R_child)+(3/ln2)qt.

At a controller query cores do not change, U is a martingale, and R's scalar Jensen gap is exactly sum_j q_j V_j D_2(P(X|C_j)||fair)>=0. At a data query the variance loss above is exact. Summing on finite physical reach weights yields A059's reserve identity, including actual stopped R. Its full stopped entropy formula follows with the signed controller residual retained; no funding of that residual follows from this review. The elementary beta^2<=Inf_i(u) uses |beta|<=Inf_i(u)<=1.

The new family in PROOF.md independently verifies the signed cancellation at beta=1 and proves that 3/ln2 is best possible, with both terminal spectra reproduced by direct character sums as well as integer FWHT. This is a sharpness contribution to the local inequality, not a substantive repair of A059. Independent acceptance of A060's sharpness proof remains A091/A090's task.
