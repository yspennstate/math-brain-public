# A094 stage 3 proof-chain audit

Target selected: A086-DISJOINT-SELECTOR-PRESCRIBED-REFERENCE@1 and the source-complete continuation A097-ONE-SHARED-DATA-COLLISION-TRANSFER@1. Verdict: HOLDS at the exact stated scopes. Independent completed validation records 35,162 exact assertions in out/EXACT_RESULTS.json; the interrupted original larger shared check contributes none. Neither states or proves universal reference admission. Full FEI OPEN. All entropies, CE and divergences are bits.

## 1. Full dependency chain reconstructed

For arbitrary actual Boolean children G,H and fresh selector z, write their real Fourier coefficients a_T,b_T on the same union cube. The parent coefficients are u_T=(a_T+b_T)/2 and v_T=(a_T-b_T)/2. Hence m_T=u_T^2+v_T^2=(a_T^2+b_T^2)/2 and the actual conditional selector kernel is K_T=(u_T^2,v_T^2)/m_T. On m_T=0 choose the fixed selector-absent kernel, including fibers with positive reference mass. Given normalized full child references R_G,R_H, r_T=(R_G(T)+R_H(T))/2 and Q(T,U)=r_T K_T(U) preserve total mass and support. No latent child label is transmitted or charged twice.

Let k_P(j|T)=P_j(T)/(2m_T), k_R(j|T)=R_j(T)/(2r_T). Factor the joint likelihood ratio of (j,T) in both directions to obtain

    [D(P_G||R_G)+D(P_H||R_H)]/2 = D(m||r) + kappa,
    kappa = sum_T m_T D(k_P(.|T)||k_R(.|T)) >= 0.

Because the parent true and reference distributions use the same K, D(P_F||Q)=D(m||r). With B=H(U|T) and J=H(m)-[H(P_G)+H(P_H)]/2,

    CE(P_F,Q) = [c_G+c_H]/2 + B + J - kappa.

This reconstructs the exact one-node portion of A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER@1 directly. No stopping-tree or universal payment hypothesis is imported. Exact leaf references give kappa=0; no free history refund arises from this identity.

## 2. Calibration and the A086 disjoint interface

For a finite partition of each child's subset space into the collision atoms and their complement, calibrate each atom to the corresponding true mass and retain the original reference conditional distribution on the complement. If that complement has zero true mass, its calibrated mass is zero; otherwise its original reference mass is positive by finite-cost support positivity. Calibration preserves normalization and support and changes cost by exactly the categorical KL between the true partition masses and the original reference partition masses. Thus cost cannot increase. This is an instance-level fixed reference, not a choice depending on the sampled subset.

Disjoint physical blocks collide only at empty. Calibrate both empty atoms. On the empty fiber the child posteriors agree, and on each nonempty supported fiber the active child is unique. Off-support reference mass uses the fixed normalized K and is retained. Hence kappa=0 and

    D(P_F||Q) = [D(P_G||R_G^0)+D(P_H||R_H^0)]/2.

Conditioning on z gives every physical data influence as the average child influence; the fresh selector has d=(1-mu nu)/2 where mu=EG, nu=EH. In particular I(F)=[I(G)+I(H)]/2+d, including constant children and zero packets.

All nonempty data packets have fair selector membership, so their total conditional erasure is [(1-mu^2)+(1-nu^2)]/2 <= 2d. For any binary unnormalized packet A,B, Jensen applied to sqrt(1/p) gives phi(A,B) <= 2sqrt(AB)/ln2. For the empty packet A=(mu+nu)^2/4, B=(mu-nu)^2/4. The identity (1-mu nu)^2-(mu-nu)^2=(1-mu^2)(1-nu^2)>=0 and |mu+nu|<=2 imply sqrt(AB)<=d. Thus B<=2d+2d/ln2.

For completeness rederive J rather than assuming a campaign lemma. A fiber has child masses (u+v)^2,(u-v)^2 and m=u^2+v^2. Its contribution is m D(t)/ln2 with t=2|uv|/m and D(t)=[(1+t)ln(1+t)+(1-t)ln(1-t)]/2. Since D'(t)=atanh(t)<=t/sqrt(1-t^2), integration gives D(t)<=1-sqrt(1-t^2), hence the contribution is <=2min(u^2,v^2)/ln2. Summing and using sum v^2=d gives J<=2d/ln2, including endpoints by continuity. Therefore B+J<=(2+4/ln2)d. The exact retained-deficit identity and calibrated cost decrease give precisely the whole A086 claim, with constant max(K_G,K_H,2+4/ln2) under the stated supplied child-cost hypotheses. No unsupported line occurs in that claim.

## 3. The one-shared-data continuation and all larger-block clauses

For G(s,X),H(s,Y), private blocks X,Y are independent conditional on s. Their embedded supports intersect only on C={empty,{s}}. Calibrate BOTH atoms separately and the remaining complement as above. Posteriors then agree on C; outside C any true nonzero fiber identifies its child. Thus kappa=0 exactly, not merely bounded or discarded. The average entire calibrated seed deficit is retained.

Let a,b be the two Fourier coefficient vectors of the conditional means m_G(s)=E_X G(s,X), m_H(s)=E_Y H(s,Y). Their l1 norms equal max(|m_j(+)|,|m_j(-)|), hence are at most one. Independence gives d=(1-<a,b>)/2. Also |x-y|<=1-xy on [-1,1], so for EACH shared coefficient

    |a_T-b_T| <= E_s |m_G-m_H| <= E_s(1-m_G m_H) = 2d.

The noncollision erasure is (v_G+v_H)/2 with v_j=1-||a_j||_2^2, and is <=2d by ||a-b||_2^2>=0. On a collision fiber, the packet estimate gives phi <= |a_T^2-b_T^2|/(2ln2). Summing,

    sum_C |a_T^2-b_T^2| <= ||a-b||_infinity ||a+b||_1 <= 4d.

Thus B_C<=2d/ln2 and the SAME selector coefficient 2+4/ln2 applies. Conditioning on z again owns each physical data influence once, including s. This proves the entire one-bit reference-transfer clause independently of the author checker.

For t shared bits the conditional-mean argument and max coefficient difference still hold. The original constant follows if BOTH l1 norms are <=1. Without that admission, Parseval and Cauchy-Schwarz give ||a+b||_1 <=2*2^(t/2), yielding the stated dimension-dependent coefficient 2+(2*2^(t/2)+2)/ln2. Calibrate every shared-only atom and retain the complement. The general references may require actual coefficient information; no algorithmic efficiency or arbitrary low-cost core reference is claimed. When everything is shared, calibration can simply replace the whole seed reference by its exact spectrum: this does not prove its cost is influence-paid.

## 4. Actual Boolean boundary: reconstruct the infinite family

On even k>=4 binary fair coordinates, b(x)=(-1)^(x_1 x_2+...+x_(k-1)x_k), and b'=b-2*1_zero are Boolean signs. Each two-bit factor has transform (+1,+1,+1,-1)/2, so b_hat(T)=sigma_T e with e=2^(-k/2); the flip subtracts 2delta at every T, delta=2^-k. The plus/minus sign counts are (2^k +/- 2^(k/2))/2, since summing the transform recovers b(0)=1.

Let M be the fresh fair selector of b,b'. Its selector influence is exactly delta. At each residual fiber the actual parent squared masses are A=(sigma_T e-delta)^2 and B=delta^2. Since e>=4delta, A>=9delta/16. For positive A,B,

    phi(A,B)=B log2(A/B)+(A+B)log2(1+B/A) >= B log2(A/B).

There are 2^k fibers. Thus B_z(M)/delta>=k-log2(16/9), and Delta/delta>=[k-log2(16/9)] since J>=0. This proves the entire A097 unrestricted selector-only no-go at the stated scope. Exact child references already have zero mismatch; the no-go is not a dictionary-choice penalty or an unpriced stopping label. No FEI counterexample follows.

Independent physical edge accounting strengthens the scope check: each coordinate of b has influence 1/2. The flipped zero was originally a nonpivotal edge to every unit vector, so each influence of b' is 1/2+2delta. Consequently I(M)=k/2+(k+1)delta. The entropy is at most k+1 by the finite support size 2^(k+1), and H(M)/I(M)<5/2 for even k>=4. An unbounded selector increment ratio is compatible with uniformly bounded full H/I.

## 5. Additional adversarial embedding: balanced children and arbitrary retained cores

For ANY Boolean q on an independent fresh block Y, define G_q=q(Y)b(x), H_q=q(Y)b'(x), M_q=q(Y)M(x,z). Every Y coordinate is shared by the two physical children. Fourier tensor factorization gives

    H(M_q)=H(q)+H(M), I(M_q)=I(q)+I(M),
    [H(G_q)+H(H_q)]/2=H(q)+[H(b)+H(b')]/2,
    Inf_z(M_q)=delta, Delta(M_q)=Delta(M).

For any normalized complete supplied reference R_q and complete normalized reference Q_M, use the fixed product R_q tensor Q_M. Its cost and deficit retain the FULL terminal bill:

    CE(P_Mq,R_q tensor Q_M)=CE(P_q,R_q)+CE(P_M,Q_M),
    D(P_Mq||R_q tensor Q_M)=D(P_q||R_q)+D(P_M||Q_M).

This is a scoped tensor statement; it does not infer a core bound. Taking q to be one fresh shared fair character makes BOTH children and the root balanced, sets both empty Fourier coefficients to zero, preserves Delta/delta>=k-log2(16/9), adds exactly one physical influence, and adds no entropy. Now H(M_q)/I(M_q)<2 for every even k>=4 because H(M_q)<=k+1 and I(M_q)>k/2+1. Thus neither balancing nor removing the empty spectral atom can justify an absolute selector-only extension; the coherent collision just moves to nonempty tagged frequencies. This added balanced/terminal-inclusive boundary is author-proved here and awaits an independent review. A086/A097 claims are accepted without supplying a repair, so their reviews remain independent.

## 6. First unsupported universal line and next action

No line is missing from the scoped A086 or A097 proof chains reconstructed above. The first unsupported universal extension is: influence-pay the excess shared collision erasure outside the l1-admitted regime from one specified, nonreused terminal core reserve, while retaining both complete seed reference bills. Replacing those bills by unproved low-cost exact references, borrowing their entire influence after already charging it to terminal CE, or paying only the selector violates the tested ledger. The shortest next target is a signed seed-slack payment tested on the balanced bent/flip tensor, with arbitrary terminal R_q retained. Do not repeat the now-paid one-shared-bit or common-spine classes.
