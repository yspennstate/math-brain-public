# Pair interaction: exact retained-row localization and a realizable scalar obstruction

Uniform finite Boolean signs; normalized Walsh coefficients; entropy and KL in bits. This is a narrow critical-payment diagnostic, not a universal FEI bound.

## 1. Reconstruction of the new A005 payment interface

Let L_A=H(f)-E H(f|A), I_A=sum_(i in A) Inf_i, D=H-KI, and S_A=-E[H(child)-K I(child)]. Physical influence telescopes exactly: E I(child)=I-I_A. Thus D+S_A=L_A-KI_A, with actual signed reserves on arbitrary roots.

For the complete retained spectral row distribution on A, B_A=H(S_A|S_Ac) and J_A=L_A-B_A. A product Bernoulli reference rho=(1+2^(K-lambda))^-1 has log normalization r=log2(1+2^(lambda-K)). Direct expansion gives G_A=|A|r-B_A+(K-lambda)I_A. Therefore G_A+lambda I_A-J_A-|A|r=KI_A-L_A=-(D+S_A). Changing lambda does not create payment.

For disjoint A,B set Omega=L_(A union B)-L_A-L_B. Sequential physical restriction gives L_(A union B)=L_A+E L_B(child_A); hence 0<=L_A<=2|A| and |Omega|<=2min(|A|,|B|). Singleton L=B+J has each term at most one: B is a binary conditional entropy, J is mutual information about a fair physical query. The two-bit point defect gives Omega=-2; the three-bit sign (-1)^((xi xor xj)y) gives Omega=+2. Tensoring independent copies proves sharpness at either sign for equal block sizes. Adding irrelevant queried coordinates supplies unequal sizes without changing the smaller-side extremum. Also S_AB-S_A-S_B-D=Omega. On a genuine minimal K-violator, D>0 and S_A,S_B>=0, so a paid pair would require Omega<=-(2D+S_i+S_j). These are independently reconstructed A005 Sections1--2; this run does NOT independently accept the entire bundled rare/prime admission theorem or its N14 certificate.

## 2. An exact row representation retaining all phase information

Fix physical coordinates i,j and write the other Fourier index as T. For its real quartet a_T=(alpha,beta,gamma,delta), indexed 00,10,01,11, put q_T=||a_T||^2. Omit zero rows. Normalize by sqrt(q_T). Define ZZ to be the probability distribution of the squared entries; XZ,ZX are squared entries after the normalized two-point Walsh transform on respectively i,j; XX uses both transforms. Let

    omega(a)=H(XZ)+H(ZX)-H(ZZ)-H(XX).

Then, exactly for every Boolean root,

    Omega_ij = sum_T q_T omega(a_T).                         (R1)

Proof: the mixed-measurement probability on (physical i, Fourier j,T) is (alpha+/-beta)^2/2 and (gamma+/-delta)^2/2. Its physical marginal is fair because every physical slice is Boolean of L2 norm one. Its joint entropy is 1+E H(f|xi). The analogous expression holds for j. The double physical measurement has probability |Walsh_2 a|^2, marginal (i,j) uniform on four outcomes, and joint entropy 2+E H(f|xi,xj). The original joint entropy is H(f). Thus H(XZ,T)+H(ZX,T)-H(ZZ,T)-H(XX,T)=Omega. Each of the four distributions has identical T-marginal q by orthogonality. All four H(q) terms cancel, proving R1. The normalization and fair marginals are essential; arbitrary real roots need not have the same physical entropy constants.

In particular define d(a)=(beta^2+gamma^2+2delta^2)/q. Parseval gives Inf_i+Inf_j=sum_T q_T d(a_T). Thus a rowwise inequality omega(a)>=-c d(a) would imply the same whole-root inequality, without renewing a child bank. R1 is an analytic identity in every dimension, not inferred from a finite search.

## 3. The tempting rate-two row step fails inside actual Boolean spectra

Take a=(3,-3,-2,-2); q=26 and d=21/26. Its proposed rate-two margin is exactly

    omega(a)+2d = (29/13)log2(2)+(18/13)log2(3)-(25/13)log2(5)<0.       (R2)

An independent integer certificate is 2^29 3^18 < 5^25. The certified logarithm enclosure in out/ROW_CHECK.json gives the same strict sign. Thus a rate-two bound cannot be proved separately on all real retained quartets.

This is not merely a non-Boolean relaxation witness. Let f on five physical bits have the first two as the queried pair; on the remaining three-bit integer y, let its four physical pair slices equal -1 exactly for y<c_ab, with c=(6,1,2,1) in order 00,10,01,11. Their means are (-1/2,3/4,1/2,3/4). The T=empty quartet is (3/8,-3/8,-1/4,-1/4), exactly a/8, with row mass13/32. This realizes the failing row in an actual normalized Boolean spectrum.

The full Boolean pair nevertheless has

    I_pair=5/8,
    Omega=(1/2)log2(2)+(9/32)log2(3)-(25/32)log2(5).

Its other rows contribute to the rate-two margin exactly

    (27/32)log2(2)-(9/32)log2(3)>0,

whose sign follows from 2^3>3. The whole margin is positive, certified by 2^56 3^9 > 5^25. The actual row witness therefore refutes the proposed rowwise step and does NOT refute the whole-root rate-two inequality. The complete complement is retained in the certificate.

## 4. Even uniform physical query marginals do not repair the scalar step

The relaxation cannot be repaired merely by requiring globally fair physical query marginals. On two query bits x and two outside bits y, put

    F(x,y)=(2 a_y/sqrt(26)) (-1)^(x dot y),  a=(3,-3,-2,-2).

This real function has E_y F(x,y)^2=1 for each x. Thus every query slice has unit L2 norm, and the induced physical pair distribution is exactly uniform; its singleton physical marginals are fair as well. Its Fourier coefficients are

    Fhat(s,t)=a_s (-1)^(s dot t)/sqrt(104).

All four outside rows have q=1/4 and differ from a only by signs implementing physical outcome permutations. Hence every row has the same omega and d, and the whole normalized Fourier-entropy interaction obeys Omega+2I_pair=R2<0. Its values have squares36/26 or16/26, so F is explicitly NOT Boolean. This is an exact obstruction to deducing the rate-two inequality from real amplitudes plus every queried-slice normalization. It is not a Boolean counterexample and not a disproof of FEI. Pointwise Booleanity, or constraints obtained from it such as A051's selected signed cuts, must do additional work.

## 5. Exact finite scope and the live critical target

The checker exhausts all labelled n<=4 Boolean tables and all queried pairs, including irrelevant pairs. Every pair satisfies Omega>=-2(Inf_i+Inf_j), decided by exact prime-log expressions and proved outward rational log intervals. This is a finite census, not a theorem in arbitrary dimension. The 1200 quartets from integer entries -3..3 modulo global sign contain16 strict counterexamples to the corresponding row statement.

The surviving all-dimensional bound follows from the already reviewed one-bit channel inequality. Write Z=I(S_i;S_j|S_rest)>=0. Spectral chain rules give Omega=Z+J_pair-J_i-J_j. Therefore

    Omega >= Z-(2/ln2)(beta_i+beta_j),                       (R3)

where beta_i is the singleton minority mass and J_pair>=0. R3 is conditional here on the accepted channel interface; it does not assert an improved constant. On a critical witness, any selected payment requires

    2D+S_i+S_j+Z <= (2/ln2)(beta_i+beta_j).

This is a necessary filter, not a sufficient selection rule. A least-dimensional violating root cannot be treated as our five-bit fixture or as an admission wrapper. The new A051 finite maximal-deficit selection supplies simultaneous Boolean signed-vertex-cut constraints precisely where the scalar relaxation loses information.

FIRST UNSUPPORTED LINE: force sufficiently negative weighted row interaction from those Boolean variational constraints and the SAME full D+S_pair account on an actual minimal witness. A universal rate-two whole-root inequality, if established, would itself only control the available negative interaction; it would not force a paid pair. NEXT is a comparison of the cross-row compensation term in R1 with A051's signed cut potential, retaining the actual pair child reserve. Further standalone quartet bounds or cheap-prefix admissions cannot supply this resource.
