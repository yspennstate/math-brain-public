# Averaged prefixes need cleanup, even with every outcome retained

Use precisely the one-balanced hierarchy and original references of A019 stage19 and A018 stage20. Write rho=2^-k, g3=-1 at000 and +1 elsewhere, G=product of m independent g3 seeds, A=point_k*(1-G)/2. Query q. On q1, leave seed0 and all padding live. For each other seed query its bits until the first1 or until all three bits are0. Stop querying that seed immediately when physically constant; leave its remaining irrelevant bits unqueried. Retain every outcome and process all m-1 such seeds. This is a finite adaptive physical prefix, with no renewed influence or reference.

Here p=Pr(A) is event density; the actual neighboring disagreement Pr(h0!=h1) is p/2, and the activated selector influence is p/4. Both tend to0 on the stated diagonals.

Each processed seed has four outcomes: first1 with probability1/2 and two ghost bits, 01 with probability1/4 and one ghost bit, 001 and000 each with probability1/8 and no ghosts. Its ORIGINAL projected seed law has empty mass5/8,3/4,1,1 respectively. Thus the expected retained ghost log-debt per processed seed is

lambda=(1/2)log2(8/5)+(1/4)log2(4/3)=2-(1/4)log2(75)>3/8,

the strict inequality following from75^2<2^13. For a full leaf let r be the product of these empty masses and epsilon the product of the constant seed signs. The remaining true seed is epsilon*g3, while the ORIGINAL reference still retains r. Both signs and every physical leaf remain present.

For every nonempty frequency of the live seed, on supported ghost-empty rows, each padding/u row has true core mass rho^2 P_g3(T)/4 and original marginal Q1 mass rho^2 P_g3(T)*r/8. There are2^(k+1) padding/u rows. Hence this sector has total true core mass M=(rho/2)*(1-(3/4)^2)=7rho/32, independent of epsilon and every ghost outcome. Its original code-to-true ratio is exactly r/2. With the complete actual activation conditional, the corresponding outer sector has mass M/2=7rho/64 and the same ratio r/2. Therefore the averaged q1 full cross-entropy is at least(7rho/64)*(m-1)*lambda. The untouched q0 branch gives the global lower bound

C_frontier >= (7rho/128)*(m-1)*lambda > 21rho(m-1)/1024.

The EXACT part of the averaged full-reference cleanup release on this sector, at original physical reaches, is (7rho/128)*(m-1)*lambda. All other literal marginal-code release terms are nonnegative; replacing gate conditionals by actual child conditionals adds nonnegative KL. Thus complete ghost cleanup releases at least this amount. No discarded sibling or support renormalization is used.

After this prefix the q1 true core is h1=u+(1-u)point_k*(1-epsilon*g3)/2. Put a=rho*(1-3epsilon/4)/2. Its full activated influence is exactly4I=6+3rho/4+(2k-3)*a. Averaging all leaves gives E[a]=p=rho*(1-(3/4)^m)/2, since E[epsilon]=(3/4)^(m-1). Together with q0, the exact remaining physical influence is

4I_frontier=6+3rho/8+(2k-3)*p/2 <=6+(14k-15)*rho/16   (k>=2).

Consequently the complete averaged signed reserve, with ANY old U>=0, obeys

E[4I-CE]-U <6+(14k-15)*rho/16-21rho(m-1)/1024.

For EVERY k>=8 choose m=2^(k+9)+1. The last negative term is21/2 and (14k-15)*2^-k/16 decreases from97/4096<1/2. Therefore the complete averaged frontier reserve is<-4. The original source is genuinely eligible: the stage19 tensor proof gives both original cores rate4 eligible and root surplus>B+5/8 for k8 and every m; its remainder estimates extend to every k>=8 since(2k+7/2)2^-k decreases, so |r_H|<3, |r_c|<4 and B>3/4 persist. Initial p<=rho/2 tends to0; the counterexample concerns inherited reference reserve, not FEI. At these prefixes the actual remaining entropy/influence stay bounded, while original reference divergence has the displayed ghost component. Taking m faster makes the averaged reserve arbitrarily negative.

Retire original event influence once: initial J=rho*3m/4+2kp, final averaged J=rho*3/4+2kp. Thus the q1 full influence retirement is3rho(m-1)/4, or3rho(m-1)/8 at global reach. Its ownership was already in B; it is not a new credit. Exact physical telescoping uses CE release with a positive sign and this influence with a negative sign, in agreement with A018. The result refutes an EVERY-prefix invariant even in this fixed tensor family, strengthening a local bad-history obstruction to a complete physical partition with q0 retained. It does not refute A020's cleanup-complete theorem or A018's all-coordinate endpoint.

First unsupported universal line: stopping/admission rules must bundle physically irrelevant reference cleanup, or explicitly charge its ghost debt before applying an averaged prefix invariant. Whether such a bundle can be paid for interacting arbitrary cores from a universal initial source remains open.

## Sharp full-cost coefficient, not merely a lower bound

Every supported nonempty-live-seed core row has mass rho^2/64. Its outer activated row has mass rho^2/1024 and reference ratio r/2. Thus the EXACT averaged complete cross-entropy of this sector, including the untouched q0 reach, is

C_active=(7rho/128)*(2k+11+(m-1)*lambda).

For m>=4 the remaining cost is uniformly bounded independently of m. Indeed the original core marginal on every supported seed-empty row has the positive vacuum term rho^2*(1-2mu)/8, where mu=(3/4)^m<=81/256. It is therefore at least rho^2/32; positive principal and empty atoms only increase it. On a nonempty outer data row the reference is Qcore/16, at least rho^2/512, so its code length is at most2k+9. The unique empty outer data pair has reference marginal at least1/2 and actual conditional code; its total cross-entropy is at most2 by h2<=1. Hence the q1 cost outside the active sector is at most2k+11. Untouched q0 has cost<7/2. Therefore, writing D=(7rho/128)*(m-1)*lambda,

0 <= C_frontier-D < (7rho/128)*(2k+11)+k+8    (m>=4).

This controls the FULL inherited-reference cost with its exact linear ghost coefficient and an explicit dimension-independent-in-m remainder. The averaged actual entropy is at most k+7: each terminal depends on at most u,k padding bits,one3-bit seed,two mask bits and one gate. Thus the averaged KL divergence also differs from D by at most an explicit O(k) bound. On the diagonal m=2^(2k+1)+1 the ghost term grows exponentially in k while p tends to0. These are reference/divergence debts, not an FEI entropy violation. The exact active-sector formula is checked by complete outer arrays in the same frozen small fixtures; the upper remainder is the displayed all-m vacuum argument.

## Original eligibility, with the all-k extension made explicit

Let H0=4-9log2(3)/8, so2<H0<3 by2^8<3^9<2^16. Set mu=(3/4)^m,beta=(1-mu)/2,p=rho*beta, eta(t)=-tlog2t. The actual indicator spectral entropy is HB=eta(beta^2)+(mH0-eta(mu^2))/4+(1-mu^2)/2. Direct Fourier expansion gives H1=eta((1-p)^2)-eta(p^2)+4kp+2rho*HB=rho*m*H0/2+rH. The elementary bound eta<=1 yields |rH|<2+(2k+7/2)rho<3 for every k>=8, since the positive sequence(2k+7/2)2^-k decreases. Original contaminated-code KL lies in[0,1], so c1=rho*m*H0/2+rc,|rc|<4. With J=3rho*m/4+2kp, the exact original bank becomes B=rho*m*(3-H0)/8+7/4+(k-1)p-rc/4>3/4. Hence4I(h1)-c1=4B-3>0; h0 is also eligible.

For the actual initial activated root, root activation KL<=1/2 by the original complete-mixture code, and Hp=H1/2+Delta(p), with Delta(p)<=15p/4 as in the independently accepted stage19 derivation. Consequently Wroot-B>=3/4+p/2+(c1-H1)/4-Delta(p)/2>=3/4-11p/8>5/8 since p<=2^-9. These inequalities prove source eligibility for every k>=8 and every m without discovering or recrediting a new owner. All later retirement is the same original influence.
