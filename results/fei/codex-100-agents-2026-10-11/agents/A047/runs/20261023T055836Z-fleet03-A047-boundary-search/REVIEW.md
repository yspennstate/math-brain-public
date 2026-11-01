# Independent reconstruction of A036's point-factor invariant

Disposition: accept A036-NONPOSITIVE-COHERENT-SAME-PROFILE@1 and A036-ITERATED-POST-A-SAME-OWNER@1 unchanged at their stated scopes. Exact source statements/hashes are retained in CLAIMS.json. This is independent reconstruction, not a substantive repair. All quantities use bits. Full FEI remains OPEN.

## 1. Reconstruct the normalized compensation

Let the target point factor be v and the disjoint arbitrary Boolean spectator u. Write l=q_v/p_v and s=q_u/p_u, with l(0)=s(0)=1 at zero/zero rows. The outer source P has target marginal (delta_0+p_v)/2. Because the reference matches empty mass, P*l and P*l*s are normalized. This is an explicit normalization check, not a product claim for the entire activation spectrum.

After erasing the queried target frequency put B=P*l. At a child source-positive atom the old inherited reference is P_y*s*(Bbar/Pbar)/(2r_y); the fresh one is P_y*s*l_y. Thus log(old/fresh)=log(Bbar/Pbar)-log(2r_y)-log(l_y). Taking actual fair physical means proves

    sigma=(1/2)E_y D(p_vy||q_vy)-D(Pbar||Bbar)+D(fair||r).

The spectator ratio cancels atomwise. Its potential effect on r also cancels: on nonzero spectator frequencies the coherent kernel is spectator-independent and sum q_u(nonzero)=sum p_u(nonzero); at spectator zero its ratio is1. This is exactly where matching empty mass AND same support are used. No reference-only source-zero atom is silently discarded. The independent dense checker verifies the old/fresh likelihood equalities at EVERY positive child atom and separately verifies the equality of tilted/untitled spectator outcomes. Interval overlap is not the proof of this identity.

## 2. Reconstruct the point-specific gap

For width w>=3 let d=2^-w, beta=1-alpha, E=1-4d+8d^2, A=(1+E)/2. Coarsen erased laws onto the remaining target frequency. Source masses: A at zero and4d^2 at each nonzero target. Reference masses: A-2alpha*d^2 at zero, beta*4d^2+2alpha*d(1-d) at remaining-full, beta*4d^2 at the other targets. They normalize directly, with2^(w-1) target frequencies.

Log-sum bounds the actual erased divergence below by this coarse divergence. The inactive factor child is constant; the other is a width-(w-1) point defect. Subtract the coarse divergence from one quarter its fresh KL. All nonfull terms cancel, leaving exactly

    V=A log2(1-2alpha*d^2/A)
        +4d^2 log2(1+alpha*d/[alpha+(2-4alpha)d]).

Its denominators are positive since alpha+(2-4alpha)d=alpha(1-4d)+2d>0. Elementary log bounds give

    ln(2)*V <= -2alpha*d^2 +4alpha*d^3/[alpha+(2-4alpha)d]
              <= -4alpha^2*d^2/(1+2alpha)
              <= -(4/3)alpha^2*d^2.

The middle step follows because4d/[alpha+(2-4alpha)d] increases in d and is at most2/(1+2alpha) at d=1/8. This is an all-alpha/all-width argument. The Boolean generalization fails HERE: PROOF.md gives an actual full-support3bit factor for which the complete reset has the opposite sign.

## 3. Reconstruct the outcome payment and endpoints

At the inactive child's target-zero rows, Bbar=Pbar-alpha*d^2*p_u(U) for each controller frequency. Applying its actual coherent kernel gives r_0=(1-eta)/2, r_1=(1+eta)/2, where eta=alpha*d^2 sum_(c,U) p_u(U)P_0(c,0,U)/Pbar(c,0,U). The conditional density ratio is at most2 and the two controller frequencies give total spectator weight2, so0<=eta<=4alpha*d^2. Consequently

    ln(2)D(fair||r)=-log(1-eta^2)/2
       <=8alpha^2*d^4/(1-16alpha^2*d^4)
       <=(32/255)alpha^2*d^2.

Combining gives sigma<=-(308/255)alpha^2*d^2/ln2<0. For width2 both child references are exact, and data processing D(fair||r)<=D(Pbar||Bbar) proves sigma<=0. Characters have l=1, constants have no essential query. Alpha0 is the exact-law endpoint; alpha1 is excluded because domination can fail. Signed factors and constant/character spectators are included. The source's corrected wrong-spike control is outside its full-spike hypothesis, and does not contradict it.

## 4. Reconstruct arbitrary finite post-a histories

Use the original source/first reset already independently accepted by A047 stage8: M0>1+2t+3m*d0/10, actual sigma1<11m*d0/40, old omega<=1/4. These are SAME original quantities. Every subsequent actual query followed by its same-profile factor-only reset restores the invariant above; induction on any finite physical tree gives sigma_later<=0. Spectator references retain matching empty mass and source support because the other factors are unchanged; constant/character endpoints are exact. This induction needs the intermediate resets actually exercised and permits different physical policies in the two a signs. It does not price a no-reset multi-query gap or changed alpha.

For an activation J_epsilon(g), erasing its controller gives (delta_0+p_g)/2, hence H(J)<=2+H(g)/2. Physical pivots give I(J)=(1-epsilon*Eg)/2+I(g)/2. Therefore4I(J)-H(J)>=-2epsilon*Eg+(4I(g)-H(g))/2. Every point-tensor restriction has H<=4I. In each sign-conditioned finite data partition, E(Eg_leaf)=Eg_initial. Averaging both complete a signs cancels the signed means even with divergent policies. The retained b0 branch contributes1 globally, so complete S>=1.

Let A0 be the original source KL and e=H0-Hf-4(I0-If). Exact full-source bookkeeping gives

    S-[A0+e+sigma1+sigma_later]_+
       =min(S,M0-sigma1-sigma_later)>=1.

The old quarter is subtracted ONCE, leaving>=3/4. No child bank or released KL is renewed. Own history.py uses original A050 Q0, actually positive first resets, divergent a-sign query orders, every physical child and complementary terminal, and reconciles complete source+resets with all erasure/outcome/terminal KL.

## 5. Limits of acceptance

The acceptance is of A036's unchanged point-factor theorem and its original-source finite-history consequence. Own72 physical fixtures and four original-source histories are independent checks, not their infinite proof. No arbitrary-core supplier, changed-alpha conversion, arbitrary target-factor nonpositive rule, or full FEI conclusion follows. A050's separate two-full-reset gross budget remains a distinct source result, read for context and not newly independently accepted here. The new same-support counterexample does not refute any stated A036 hypothesis.
