# A067 Boolean flag/four-branch final reference v1: HOLDS

Exact source: A067 run20261014T044841Z, A067-BOOLEAN-FLAG-FOUR-BRANCH-FINAL-REFERENCE v1. Canonical statement/hypotheses hash92eacd157bc8b527dc2e8d38d2bdb5be1dfbf179105280ad82707f5c587c1948. No substantive repair, statement change or source code import supplied. Previously accepted cell/channel/granularity fragments retain their exact scoped versions; this new theorem is independently reconstructed below.

## Universal Boolean flag lemma and sharpness

For a Boolean sign F and any control block Z, alpha=sum_{S:S intersects Z} Fhat(S)^2 is at most v=1-Fhat(empty)^2 and I(F)>=v. If v>=1/2, h2(alpha)<=1<=2I. If v<1/2, monotonicity gives h2(alpha)<=h2(v). Let p be the minority input-sign probability; Boolean outputs give v=4p(1-p). The v<1/2 case implies p<1/4. Use h2(v)<=v log2(e/v), monotonicity of t log2(e/t) on[0,1], v<=4p<1, and e<4 to get h2(alpha)<=4p log2(1/p). Indicator isoperimetry I(F)>=2p log2(1/p) proves h2(alpha)<=2I(F). For p=0 the statement is trivial.

Isoperimetry is reconstructed directly: split a set into child densities p0,p1. The additional required lower bound over the child average is2p[1-h2(t)], t=p0/(p0+p1), while actual crossing influence is at least|p0-p1|=2p|2t-1|. Concavity h2(t)>=2min(t,1-t) pays the difference; induction starts at dimension0. This is a Boolean physical-boundary argument, not an arbitrary squared-spectrum inequality.

For point signs on d controls, alpha=4delta(1-delta), I=2d delta, delta=2^-d. The elementary entropy lower bound gives h2(alpha)/I>=2(1-delta)[1-log2(4(1-delta))/d] ->2. The proved upper bound gives the same limiting coefficient. This sharpness concerns one full-block flag only; it does not claim the access reserve is optimal.

## Four actual branches and the whole reference

An arbitrary four-branch output has expansion h00+(h10-h00)p+(h01-h00)q+(h11-h10-h01+h00)pq. Each core Fourier row is therefore in span(1,p,q,pq), even when an ancestral source depended on both controllers. The earlier independently checked compatible four-cell/incompatible five-cell partition and cardinality<=twice mean-degree proof applies unchanged to this algebraic span. No edit cap or seed-independence step is reused. Inaccessible branch states receive no artificial terminal weight.

The same complete tail reference assigns1/(M|C|) to EVERY nonempty control label, including output-zero cells. Combine it with empty mass1-alpha and tail massalpha. A single final joint reference is R_joint(T,S)=q_T R_full(S), q the ACTUAL final core marginal. Its exact cross entropy is

    CE_joint=H(q)+h2(alpha)+alpha log2 M+cell_cardinality_cost.

Actual row-cell flatness and the accepted mean-degree inequality pay the last term by2I_Z. Alpha<=I_Z holds for all normalized spectra. The new flag lemma pays h2(alpha)<=2I_X+2I_Z. The exact physical restriction grouping gives H(q)=E_z H(F_z)+J_Z, with real-valued channel J_Z<=2I_Z/ln2. Thus

    CE_joint<=E_z H(F_z)+(4+log2 M+2/ln2)I_Z+2I_X.

Gibbs' inequality H(F)<=CE_joint proves the access bound. Choosing q from the output does not omit its entropy: it is converted explicitly to the retained terminal entropy and the paid channel. If a control block or tail is empty, use the trivial/support-compatible limiting law. The compatible M<=4 and general M<=5 give exactly the source constants, with ln2>2/3 and log2 5<5/2 establishing strict numerical bounds.

If each accessible actual core has H<=C I, physical averaging gives E I(core)=I_X and H(F)<=K I_Z+(C+2)I_X. The U certificate gives C=2+2b, and actual degree<=2 gives U<=I and C=4. These are terminal hypotheses, not seed-only certificates. Same-C induction still fails to follow: the core reserve is added above C I_X. Arbitrary control dependence beyond the two fixed states also lacks the proved flat-cell reference.

Verdict HOLDS at the full exact source scope. No unsupported line within the theorem. Its first unsupported universal extension is an exclusive actual child-surplus payment for2I_X (or another complete paid general-controller reference).

## Strong non-Boolean scope diagnostics

The row span, flat-cell law, Gibbs bound, alpha<=I_Z and real channel are algebraic and survive real amplitudes. The proof's genuine Boolean step is v=4p(1-p) coupled to minority-set pivotal isoperimetry. Normalized real fields can have small nonzero variance with no minority sign set. Unit norm plus pointwise absolute value<=1 would force Booleanity and is not a meaningful weaker domain.

Source's normalized real u=(4095+128z)/4097 has squared masses1-beta,beta, beta=16384/16785409<1/1024. It refutes the flag inequality by h2(beta)/I>10. On X empty with complementary fixed controllers, each normalized constant child has entropy0, so it also refutes the natural real access extension using individually normalized child spectra. Its raw real children are not themselves norm one; do not use this witness to assert failure under that extra hypothesis.

For the stronger relaxation preserving both output norm and EVERY actual child norm, take

    F(x,z)=262143/262145+(1024/262145)xz.

Let beta=1048576/68720001025<1/65536. Both children a+bx,a-bx have squared norm1; the full output has squared norm1. Core/control influences are both beta. H(F)=H(q)=E H(child)=h2(beta). The global flag reference has CE_joint=2h2(beta), so its excess above terminal entropy is h2(beta)>16beta, while(K+2)beta<(23/2)beta. Its flag inequality also fails since h2(beta)>16beta>2I(F)=4beta. This is an exact rational norm-one-children refutation of the specified joint-reference payment and universal flag extension. Bare access Q=0 in this witness, so its stronger real extension is not refuted here. Conditioning the flag on T refunds exactly h2(beta) and restores the actual reference cost; this does not repair the Boolean-independent proof globally.

## Conditional flag continuation: one new narrow obstruction

For ANY normalized joint spectral law, let V be the nonempty-control flag and T the core label. Replacing only the global flag prior by the actual P(V|T), while retaining the core law and the same within-tail reference, reduces complete cross entropy by exactly I(T;V). This follows by averaging log[P(V|T)/P(V)] under the same joint law. It preserves terminals and has no extra Boolean premise.

CONDITIONAL_FLAG_OBSTRUCTION.md gives a checked all-dimensional Boolean application after ONE actual core query. For G_m=b_m(Y)+1{w=0,Y=0}(z-1), m>=2, the remaining flag cost satisfies

    H(V|T)/I_z(G_m)>=m+3/2,
    I(G_m)=m+(2m+2)2^(-(2m+1)),  H(G_m)/I(G_m)<=3.

The full parent restriction, actual bent phases, dummy occupancy and both actual core terminals are retained. Thus conditional MI refund alone cannot pay an arbitrary selected node at a uniform local rate K I_z, even in the new four-branch class and immediately after core exposure. This does not refute source's2I_X reserve, a weighted/selected tree rule, or FEI. The narrow new claim is author-proved with exact certificates and requires independent review; it is not an independently accepted theorem merely because the same agent wrote proof and checker.

NEXT must price the residual conditional flag from one unused signed child/control surplus, guarded by this post-exposure family. A request to delete the informative dummy flag or renew the global reserve would miss the actual obstruction.
