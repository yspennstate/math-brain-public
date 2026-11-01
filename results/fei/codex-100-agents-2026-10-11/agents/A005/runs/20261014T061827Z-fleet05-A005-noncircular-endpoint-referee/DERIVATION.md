# Gibbs exhaustion referee: exact payment, sharp interaction and a hard paid prefix

Actual Boolean signs, finite uniform cubes, normalized squared Fourier spectra, all entropies/KL in bits. For a physical block A, L_A=H(f)-E_a H(f|A=a), I_A=sum_(i in A) Inf_i. The actual child reserve at fixed K is S_A=-E_a[H(f|A=a)-K I(f|A=a)], and D_K=H-KI. All formulas below retain signed S_A on arbitrary roots. References use lambda>=2/ln2, rho=(1+2^(K-lambda))^-1 and r=log2(1+2^(lambda-K)).

## 1. Independent reconstruction of A052's exact bank

For the retained row law nu_t on A define G_A=sum_t q_t KL(nu_t||Ber(rho)^tensor |A|), B_A=H(S_A|S_Ac) and J_A=L_A-B_A. Expanding the complete normalized reference gives

    G_A=|A|r-B_A+(K-lambda)I_A.

Consequently the proposed exhaustion quantity satisfies EXACTLY

    Psi_A:=G_A+lambda I_A-J_A
          =|A|r+K I_A-L_A,
    Psi_A-|A|r=K I_A-L_A=-(D_K+S_A).             (1)

The reference parameter lambda cancels from the surplus, on every root and every block. Selection Psi_A>=|A|r is exactly L_A<=K I_A, the original physical decrement payment. It is not an additional independent upper bound or a new source of child funding. A052 states its bank as an identity and leaves selection open; (1) does not refute that theorem. It identifies what a proposed proof of selection must actually establish.

The channel bound used in this review can be checked without FEI: product entropy tensorization follows from H(P)>=sum_i H_P(X_i|X_others), by the Shannon chain rule and conditioning. On one bit, after normalizing E w^2=1 and replacing w by |w|, put w^2=(1+u,1-u). The difference between E(s-t)^2/2 and Ent(w^2) has derivative u/sqrt(1-u^2)-artanh(u)>=0, since its derivative is (1-u^2)^(-3/2)-(1-u^2)^(-1)>=0. At u=0 the difference is zero; continuity handles u=1. Tensorization and Walsh Parseval give (ln2)J_A<=2I_A. Applying the same estimate to a singleton with the smaller Fourier amplitude as its derivative gives (ln2)J_i<=2 beta_i. Thus lambda>=2/ln2 makes every recentering slack nonnegative. For the collision cap, each singleton row has 4xy/(x+y)<=4min(x,y); the signed quartet parity term is <=2 times its queried influence by two Cauchy--Schwarz bounds, while merging refunds are nonnegative by weighted Cauchy--Schwarz. Consequently C_pair<=C_i+C_j+P_pair<=4(beta_i+beta_j)+2I_pair<=6I_pair. These independent elementary reconstructions cover the analytic dependencies needed for A052's stated claim, without assuming a pending FEI upper bound.

For singleton minority masses beta_i, orientation O_i=d_i-beta_i, minority Gibbs KL Lambda_i and recentring slack A_i=lambda beta_i-J_i, the scalar Gibbs expansion gives D+S_i+K O_i+Lambda_i+A_i=r. Reflecting a conditional inclusion p>1/2 to1-p changes KL by (K-lambda)(2p-1). The two full conditional KLs of a pair add to G_pair plus conditional mutual information Z. This independently yields A052's compatible pair identity and its whole-pair bank. Nonnegativity of every displayed reserve is used only on actual minimal witnesses. The singleton entropy bound h2(d)/d<log2(1/d)+1/ln2 and J_i<=2d_i/ln2 prove its critical max-influence bound exp(3)2^-R; d=1 cannot be positive-ratio critical. The block channel bound follows from the two-point entropy inequality and tensorization, as reconstructed in A052's proof. Thus A052-CRITICAL-WEAK-INFLUENCE-GIBBS-BANK@1 holds at its stated scope, with no repair. Its tail mass restriction is the increasing binary-KL bound for u>rho, and C_pair<=6I_pair yields its12exp(3)2^-K cap. No critical selection is proved by these necessary identities.

## 2. Sharp finite-block interaction, without a false sign assumption

For disjoint nonempty A,B define

    Omega_(A,B)=L_(A union B)-L_A-L_B.

Physical entropy telescoping gives Omega=E_a L_B(f|A=a)-L_B(f). Each singleton has L_i=B_i+J_i in[0,2]: both the binary spectral conditional entropy and the binary physical-channel information are at most one. Querying all coordinates of B telescopes, so 0<=L_B<=2|B| on every actual child. Reversing A,B gives the SHARP universal bound

    -2 min(|A|,|B|)<=Omega_(A,B)<=2 min(|A|,|B|).       (2)

For a pair i,j, conditional spectral chain rules give the alternative exact form

    Omega_ij=Z_ij+J_ij-J_i-J_j.

Let h=+1 except -1 at physical00 on two bits. Its H=2,I=1; L_i=L_j=2,L_ij=2, so Omega=-2. For g(x_i,x_j,y)=(-1)^((x_i xor x_j)y), H=2, L_i=L_j=0 and L_ij=2, so Omega=+2. Tensor m disjoint copies and query the first coordinate of each factor as A, second as B; entropy/decrements add and give equality +/-2m in (2). These are actual Boolean sharpness certificates, not arbitrary real row examples.

In Gibbs form, the pair's surplus minus the two singleton surpluses is -Omega_ij. The actual child reserves obey

    S_ij-S_i-S_j-D_K=Omega_ij.                       (3)

Hence one cannot infer pair payment by adding two nominal singleton r budgets and dropping their channel interaction. For a genuine minimal K-violator, singleton residuals L_i-Kd_i=D+S_i are positive. A paid pair requires Omega_ij<=-(2D+S_i+S_j), which is precisely the missing reserve-relative interaction estimate. The absolute bound(2) gives no such payment when D and the reserves may be arbitrarily small. Both interaction signs occur, so neither a submodularity nor a supermodularity shortcut is valid.

## 3. An arbitrary seed has an exactly exhausted, entropy-bearing paid pair

Fix any nonconstant seed f on n relevant coordinates. Form h_t=f^tensor t, multiply by the two-bit sign h above, and call this unactivated tensor M_t. Query the two gadget bits A. They are relevant with influences1/2 each; every physical child is +/-h_t. Thus

    H(M_t)=tH(f)+2, I(M_t)=tI(f)+1,
    L_A=2, I_A=1, J_A=0, C_A=0,
    Psi_A-2r=K-2.

All gadget retained rows have uniform four-atom squared Fourier law; their actual physical row is a scalar multiple of the Boolean two-bit sign. The ratio tends to the arbitrary seed ratio. For EVERY K>=2 this entropy-bearing proper pair is paid and its Gibbs bank exhausted, yet its complete terminal cost is tH(f). If delta_f=H(f)-KI(f)>0, its child reserve is exactly -t delta_f, which is negative. A cheap root block cannot certify its arbitrary terminal.

## 4. Simultaneous rare/weak admission with the same paid pair

For rarity also multiply M_t by a fresh balancing literal z. Let core_t=z h h_t, so H(core)=tH(f)+2 and I(core)=tI(f)+2; every gadget child remains balanced. Activate core at one point of k_t=ceil(sqrt(t)) controls, with value+1 elsewhere, probability p_t=2^-k_t. Call the Boolean root A_t. The existing balanced activation ledger supplies

    H(A_t)=p_t[tH(f)+2]+R_k,
    I(A_t)=p_t[tI(f)+2+k_t],
    R_k=2k_t p_t(2-p_t)+phi((1-p_t)^2).

For clarity, this ledger can be reconstructed directly: the balanced core has zero empty coefficient. Its nonempty coefficient u becomes p*u on each of the 2^k control characters; these rows contribute p H(core)+2kp. The wrapper has empty coefficient1-p and coefficient-p on each of the 2^k-1 other control characters, contributing phi((1-p)^2)+2k(p-p^2). Summing gives R_k as displayed. Every core coordinate has influence p times its core influence, and every control has influence p because the core is balanced. In the pair retained rows, wrapper modes have gadget weight only at the empty character, while core modes have all four gadget amplitudes of equal magnitude from the AND2 Fourier law. Each physical row therefore has constant squared density, proving J_A=C_A=0 directly, rather than assuming it from a conditional nonnegative bank.

All gadget children have the same wrapper term R_k and core entropy tH(f), so

    L_A(A_t)=2p_t, I_A(A_t)=p_t, J_A=C_A=0,
    Psi_A-2r=(K-2)p_t.                              (4)

The paid-pair rate is exactly2 independently of the seed, at every t,k. Meanwhile I and every influence tend to zero, mean tends to1, and H/I tends to H(f)/I(f). Each gadget child has deficit p_t t delta_f+R_k-Kp_t(1+k_t), asymptotic to p_t t delta_f for a positive fixed seed gap. All four are eventually violating, with S_A<0. No inactive or complete terminal weight is omitted.

Append two dummy bits and flip ONE inactive-control vertex. The resulting E_t has odd negative count, hence full Fourier support, all inputs relevant and no disjoint coordinate tensor factor. Its dimension N_t=tn+2+1+k_t+2. Entropy and influence edits are O(N_t 2^(-N_t/2)) and O(N_t2^-N_t). The four gadget children have edit probability at most4*2^-N_t, so their uniform errors are of the same exponentially small orders. Dividing by p_t shows these errors are o(1), also o(p_t) before division. Consequently the pair rate tends to2 and H/I tends to the seed ratio. For every fixed K>2 it is eventually strictly paid; the boundary K=2 is not inferred after surgery from a limit alone.

The parity and error claims have elementary certificates. Padding multiplies the old negative count by four, and one flip makes it odd. Every Walsh numerator equals 2^N at the empty character minus twice a signed sum of that odd count, or just the latter sum at a nonempty character, so it is nonzero for N>=2. A factorization over a nontrivial physical partition with both sides nonconstant would have negative count r*2^b+s*2^a-2rs, even; an irrelevant coordinate would likewise make that count even. Thus the edited function is prime and all coordinates are relevant. If the edit probability is epsilon, Fourier L2 distance is 2sqrt(epsilon), whence spectral total variation <=2sqrt(epsilon) by Cauchy--Schwarz. Entropy continuity gives error <=TV*log2(2^N-1)+h2(TV)=O(N sqrt(epsilon)); changing one physical vertex alters each influence by at most2epsilon. On a queried pair child epsilon is at most4*2^-N, which proves the uniform estimates. Since N=tn+O(sqrt(t)) and p=2^-ceil(sqrt(t)), both errors divided by p vanish exponentially. R_k/p=O(k), so dividing the activation ratio by pt yields the seed H/I limit. No limit is being inferred from the finite certificate.

Thus for fixed K>2 and fixed positive rarity/weak-influence thresholds, the class of prime full-support Boolean roots with an affordable relevant proper pair (equivalently exhausted pair Gibbs bank) still has exactly the universal extended-real optimal H/I constant. The exact pre-surgery K=2 class is already same-constant FEI-hard. These are admission theorems, not proofs that every Boolean root has a paid pair or that such roots can stop in a certified class.

## 5. Fixed strict certificate and the first unsupported line

The finite fixture takes the three-bit point defect, t=2, two gadget bits, balancing bit, k=3 controls, then two dummy bits and the inactive zero-data vertex with first control bit1 flipped: N=14. At K=lambda=3, rho=1/2 and r=1, all references are rational. Direct spectra and all four physical pair children certify a positive root K-deficit, max influence<1/4, full support/odd negative count, pair rate<3, and Psi_A>2. Each gadget child violates K=3, so the actually retained reserve is negative. The seed itself need not violate3 for this finite example; it is a root/terminal counterexample to treating paid-prefix exhaustion as certified induction. The arbitrary-seed positive-gap asymptotic proof is separate.

FIRST UNSUPPORTED UNIVERSAL LINE: prove a selected block's surplus from independently controlled signed physical interaction on a genuinely least-dimensional K-violator, retaining its full nonnegative child reserve, or complete the affordable prefix with a paid terminal class. Equation(1) cannot create that resource by changing lambda, and examples(2)--(4) cannot be assigned critical reserve signs. NEXT is the actual reserve-relative interaction/terminal payment; further root-only code or Gibbs-normalizer admissions would merely repackage the already-embedded arbitrary seed.
