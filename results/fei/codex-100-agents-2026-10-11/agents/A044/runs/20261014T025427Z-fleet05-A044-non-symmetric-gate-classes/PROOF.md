# Shared-guard loss and coherent endpoint payment

Use natural corrected entropy E=(ln2)Hplus. Physical biases are independent, vi=4pi(1-pi), P(S)=vS cS^2, Delta=sum(|S|-1)P(S). All endpoint functions are contracted before normalizing.

The four-variable Boolean sign is positive on the mutually exclusive events
A={a=1,b=1,z=1}, B={a=0,c=1,z=1}, C={b=0,c=0}.
It is A043's mask56067 under least-significant-coordinate indexing, and equals
F=1-2b-2c+2bc+2zc+2zab-2zac.

For any law, exclusivity implies Var(F)=sum Var(fi)-8sum event-probability products. For the A/B derivative intersection, only the opposing a coordinate can contribute: its physical cross expectation is negative, with joint residual event probability p_b p_c p_z. The A/C and B/C pairs have one opposing literal and no agreeing common literal, so the covariance and influence cross contributions cancel. Therefore

    Delta(F)-sum Delta(fi)=-L,
    L=2v_a p_b p_c p_z(1-p_z).

This is reconstructed directly from physical derivatives, without borrowing A043's checker.

Fix p_a=p_z=1/2 and p_b=p_c=r=1-e, 0<e<=1/2. The normalized nonempty coefficients, with all absent entries zero, are

    c_z=r; c_b=c_c=1/4-e;
    c_ab=1/4, c_ac=-1/4, c_bz=c_cz=1/4, c_bc=1/2;
    c_abz=1/4, c_acz=-1/4.

The mean is -e+2e^2. Put v=4re. Squaring actual coefficients only after adding the events gives

    Delta=2re+4r^2e^2=2re(1+2re), L=r^2/2,
    L/Delta=r/[4e(1+2re)] ~ 1/(4e).

For e<=1/4, r>=3/4 and 1+2re<=3/2, hence L/Delta>=1/(8e). Thus no finite K pays L<=KDelta, even on this fixed four-input genuine prime and interior input laws. The sum of constituent deficits is Delta+L and also has unbounded ratio to Delta. The contradiction does not use an abstract non-Boolean profile.

Retaining amplitudes yields a fully paid entropy instead. With h(t)=t^2 ln(1/t^2), h(0)=0, the exact entropy is

    E=r^2 ln(1/r^2)+8re h(1/4-e)+(3/2)re ln16+4r^2e^2 ln4.

For 0<e<=1/2, |1/4-e|<=1/4; h is even and increasing on [0,1/4], so h(1/4-e)<=ln16/16. Also ln(1/r)<=e/r by ln x<=x-1. Consequently

    E<=2re+2re ln16+4r^2e^2 ln4
      <=(1+ln16)(2re+4r^2e^2)=(1+ln16)Delta.

As e decreases to zero, r^2 ln(1/r^2)/(2re) tends to 1, the second and third entropy terms together divided by 2re tend to ln16, and the last term divided by Delta tends to zero. The sharp corrected constant on this entire one-parameter slice is therefore

    sup Hplus/Delta = 4+1/ln2.

The supremum is a limit, not the quotient at the contracted literal e=0. For fixed e the law has only two biased data inputs and all four physical inputs remain independent. This is a narrow coherent repair of the existing shared-guard mechanism, not an all-four-bias theorem.

The actual unused singleton reserve is S=4Delta-2R-E_single, R=sum_{|S|>=3}(|S|-2)P(S)=re/2 here. It is nonnegative by the signed Boolean singleton identity, and S<=4Delta since E_single>=0. Consequently L cannot be paid by any fixed multiple of S (or of a nonnegative root reserve bounded by a fixed multiple of Delta). Removing singletons does not make the raw intersection a fundable positive cost. The exact coherent higher-degree cost is

    E_ge2=(3/2)re ln16+4r^2e^2 ln4 <= (3ln2)Delta.

All high-degree entropy vanishes as e tends to zero while L tends to1/2: the termwise component amplitudes cancel before squaring. A reference that retains only component deficits and demands a nonnegative debit for L has discarded the information required for this cancellation.

First unsupported line: for arbitrary four independent biases, an inherited signed quadratic reference must pay the full combined spectrum of prime56067 with one output/terminal reserve, rather than charge L separately. The one-parameter bound does not establish that line or universal FEI.
