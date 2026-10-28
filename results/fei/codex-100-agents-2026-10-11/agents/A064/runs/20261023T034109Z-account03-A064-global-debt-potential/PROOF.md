# One actual intermediate reset and unrestricted continuation from the old allocation

All quantities are in bits. Uniform physical outcomes, rather than reference predictions, define the fair filtration. Every reference is normalized, supports the actual squared Fourier law, and uses the same coherent kernel as the source, extended by (1/2,1/2) on source-zero rows. All trees below are finite and reveal each physical coordinate at most once. No limit argument is used.

## 1. Generic continuation envelope, reconstructed

For any Boolean g and supporting Q put K=D(p_g||Q), M=sum_j h2(Inf_j(g)), TC=M-H(g). Erase coordinate i and write E=D(p||Q)-D(p^-i||Q^-i)>=0. On an erased row T of positive source mass the physical kernel is k_b(T)=p_(g_b)(T)/(2p^-i(T)). Reference-only rows retain their fair extension. Let r_b=sum_T Q^-i(T)k_b(T), Q_b=Q^-i k_b/r_b, and O=D(fair||r). Support and normalized Boolean child spectra imply r_b>0. Two finite KL chain rules give

    K=E+O+(K_0+K_1)/2.

For j!=i, direct physical edge partition gives d_j(g)=(d_j(g_0)+d_j(g_1))/2. Concavity of h2, including endpoints0,1, gives M>=mean M_b. Therefore V=K+M is nonnegative and V-mean V_b>=O. At a stop retain K, or convert ONCE and stop with TC; both are<=V. Thus every adaptive continuation from a supplied entry law obeys

    E T_tau + E sum_(queries before tau) O <= K_entry+M_entry.       (1)

Here T is the actual inherited KL or actual product TC, not zero. Adding E H(g_tau) to both sides retains the full terminal cross entropy. That entropy is not claimed paid by the extra reserve. This reconstructs A087's full-physical envelope at its stated scope without modifying its source.

## 2. Concrete entry, original account and admissible enlarged policy

Let l>=2, m=3l, q=2^l, and h(a,b,x)=psi(a)(1-2*1[x=ab]) on GF(q)^3, psi a nontrivial additive character. Write H_h=H(h), M_h=sum h2(Inf_j(h)). Define C_g(u,v,y)=(-1)^((u+v+L(y))*v)g(y), L the parity of all m ordinary physical coordinates. The selector s chooses G=C_1 or H=C_h. Supply its ORIGINAL already booked uniform product spectral reference Q_root (all original physical influences are1/2). The SAME original expected owner is

    Sbar=mean_s(4I(C_g)-H(C_g))=2m+2-H_h/2.

Assume unrelated earlier consumption 0<=omega<=Sbar/4. Existing pending allocation theta, if any, must be for a nested policy class with this SAME original reference and satisfy theta<=W=m+2. If W is already booked no extra allocation is made; otherwise top up ONCE by W-theta. Already consumed charges remain in omega. Availability is a hypothesis, not implied by Sbar's numerical value.

After the fixed selector each child may independently choose: (A) any adaptive physical continuation with at most one final conversion and stop, as in A087; or (B) query fresh v IMMEDIATELY, actually reset both children to their actual marginal product references, then take ANY adaptive physical continuation, with inherited-reference stops or one final product conversion and stop. Stops before selector or before v retain actual inherited KL. Mode B's reset is intermediate, and continuation may query the unused u as well as all ordinary coordinates. Mode is chosen at selector-child entry; switching to B after arbitrary later queries is NOT admitted. Randomized mixtures follow by conditioning. Earlier terminal conversion debits are not relabeled pending.

The inherited selector prediction is r_G=1/(2q), r_H=1-r_G, erasure credit0, and

    K_G=2l-1,
    K_H=m-H_h+log2(r_H),
    K_root=O_selector+(K_G+K_H)/2.                         (2)

These formulas retain reference-only rows. The core reference is R_G(T)=[1 at empty;0 on supp h;1/2 elsewhere]/(q^3 r_G), and R_H(T)=[0 at empty;1 on supp h;1/2 elsewhere]/(q^3 r_H). Lift with independent uniform bent spectrum and the same shear. The empty atom is outside supp h. The explicit field spectrum has one atom(1-2/q)^2 and(q-1)q^2 atoms4/q^4; this normalizes the formulas and gives H_h<=m, H_h=5 at l2.

## 3. Reset splice guard: no renewed full-M owner

At each selector child use P_b=K_b+W, where W=m+2 equals its actual full marginal entropy. Mode A is paid by section1. In mode B the inherited lifted reference has exact carrier-pair symmetry, including reference-only rows, so O_v=0. Its actual children are g and -chi_u chi_L g. Character multiplication only complements Fourier indicators; thus both have entropy H(g), marginal entropy M(g), and product KL TC(g)=M(g)-H(g). The extra unused u indicator is deterministic and contributes0. At the reset genuinely replace the inherited reference by the actual product and use the post-reset potential

    V_reset=TC(g)+M(g)=2M(g)-H(g).                       (3)

This is a remaining continuation liability, not a new owner. For G it is0. For H, the complete signed switch-and-continuation debit relative to incoming K_H is

    J_H=2M_h-H_h-K_H=2M_h-m-log2(r_H).

Since M_h<=m and r_H>=7/8>1/2,

    J_H<=m-log2(r_H)<m+1<W=m+2.                         (4)

The cut between the physical v query and reference replacement is also admitted. Erasing v in the lifted source/reference gives E_v=0; on each child's positive-source support the transported reference agrees with its original core R (or its character translate), while all reference-only mass remains. Thus EACH pre-reset child has inherited KL exactly K_b. At this cut use K_b+[2M(g)-H(g)-K_b]_+=max(K_b,2M(g)-H(g)). Its pending portion is [J_b]_+<=W, so it is paid before the physical v reveal, dominates both a stop in the inherited reference and the impending reset-plus-continuation, and passes to (3) without an increase. A stop that resets and ends immediately keeps TC, which is dominated by (3). No unobserved between-query cut is assigned zero debt.

For G, J_G=-K_G<=0<W. Thus P_b>=mean V_reset+O_v at this ACTUAL reference reset. It retains every incoming KL, and both reset child laws. After the reset use section1 with K=TC at entry; its M is the continuation portion already included in (3). No descendant receives additional original capacity. At any cut before reset retain P_b, after reset retain K_current+M_current, and at a stopping conversion retain actual TC. All are nonnegative. Branch potentials may grow, but fair conditional expectations satisfy the stated drift. The compensated process P_current+sum O is a supermartingale up to every admitted cut, even with different modes in the two selector branches.

At root P_root=K_root+W, and (2) gives exact drift O_selector. Consequently for every such enlarged tree

    E T_terminal+E sum_all_queries O <= K_root+W.         (5)

Full E H_terminal remains explicitly on both sides if (5) is written for cross entropy. Initial K_root=m-1-H_h/2 is already booked separately; (5) does not bound it by influence. Formula (4) is a signed splice, not a sum of a full pre-reset M allocation and a fresh post-reset M allocation. Reserving both independently would double charge the continuation.

## 4. Original balance, exact scope and remaining gap

The unchanged W=3l+2 satisfies W<5Sbar/7: l>=3 follows from Sbar>=9l/2+2 and (5/7)Sbar-W>=(3l-8)/14>0; l2 gives3/14. Hence the SAME balance, with the original old-quarter debit retained, is

    Sbar-omega-W>Sbar/28.

The old allocation supports the union of mode A and the new immediate-v-reset mode B, so if W was already booked the additional owner charge is exactly0. A smaller nested theta is topped up by W-theta once. This does not refund any conversion already performed in an earlier run, nor allow arbitrary late conversion, arbitrary reset loops, or a new allocation after reset.

The first unsupported universal line remains a signed influence-scale reserve for arbitrary inherited sparse histories, with an eligible unused original owner. Even within this fixture, allowing the first reset after an arbitrary adaptive prefix requires a new splice guard at that prefix; (4) uses the actual selector-entry K_H and cannot be reused there. A second intermediate reset followed by further continuation is also outside this theorem. These are real boundaries, not FEI counterexamples. The result advances reset continuation at a paid location rather than reopening the closed ordinary/carrier query classes.
