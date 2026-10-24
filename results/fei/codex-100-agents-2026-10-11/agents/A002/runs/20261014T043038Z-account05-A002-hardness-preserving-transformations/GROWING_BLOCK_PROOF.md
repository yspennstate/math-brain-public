# Growing-block near-code admission, with actual child debt retained

Finite uniform physical cubes, Boolean signs, normalized Walsh coefficients, entropy in bits. For a physical block A, put L_A=H(F)-E_a H(F|A=a), I_A=sum_(i in A)Inf_i(F), and S_A=-E_a[H(child)-K I(child)]. At a retained Fourier row T, amplitudes indexed by U subset A are a_U, q=sum_U a_U^2, and w(x_A)=sum_U a_U chi_U(x_A). Define the actual row collision

    C_A=sum_T [E_(x_A) w_T(x_A)^4-q_T^2]/q_T,

with zero rows contributing zero. This equals the squared signed convolution over nonempty block frequencies, and for |A|=2 agrees with A052's quartet C_ij. It is nonnegative. No independent-child or minimality hypothesis is imposed on the transport theorem.

## 1. New code scale: minimum distance beyond growing blocks

Let D be the number of physical data bits and b>=1 the maximum block size. Suppose

    b<=D, r=ceil(2b log2(2D))<=D.

Initialize a list with the r standard basis vectors in F_2^r. Add D vectors ell_j deterministically: at step j choose the least nonnegative r-bit vector NOT expressible as the XOR of at most b-1 DISTINCT already listed vectors (the empty sum is included). At most

    sum_(h=0..b-1) binom(D+r-1,h) <= b(2D)^(b-1) <2^r

vectors are forbidden. Thus the greedy choice always exists. Initially the standard basis has no dependence; induction shows every at-most-b-element subset of the entire column list is independent in the weak sense that its XOR is nonzero. Repeated columns are allowed only when b=1. The systematic parity-check matrix (ell_1,...,ell_D | I_r) therefore has no nonzero kernel vector of weight <=b.

For ANY Boolean core g on D bits, define

    F(x,z)=g(x_1 xor <ell_1,z>,...,x_D xor <ell_D,z>).

Its spectral map U -> (U, xor_(j in U) ell_j) is injective and its image has distance at least b+1. H(F)=H(g), original coordinate influences are unchanged, and

    I(F)=I(g)+sum_a e_a,  e_a<=Var(g).

The variance refinement follows because an added spectral tag can occur only on a nonempty original frequency. No auxiliary physical influence is discarded. Every restriction of at most b coordinates is injective on the old support. For EVERY physical assignment its child therefore has H(child)=H(g) and I(child)=I(F)-I_A(F). This is physical child certification accounting, not an artificial spectral projection.

For any b_D with b_D log D=o(D), the displayed r=o(D) and r<=D eventually. The deterministic greedy recipe proves existence on every sufficiently large index; no growing-dimensional search is executed. Finitely many initial indices can be discarded.

## 2. Exact all-block single-edit collision formula

Let F be any distance-(b+1) coded Boolean sign on N bits and reverse its value at physical zero. Write E for the edited sign, p=2^-N, epsilon=2p, and eta=F(0). For a block A of size a<=b let M=2^a. Each retained old Fourier row has at most one occupied coefficient c (possibly c=0). After multiplying the partial row by its occupied character, its physical values are

    w(x_A)=c-eta M epsilon 1_(x_A=0),
    q=c^2-2 eta c epsilon+M epsilon^2.

Multiplying by a character preserves w^2 and does not affect the edit at zero. The exact row collision is

    R_M(c)=(M-1)epsilon^2(M epsilon-2 eta c)^2/q.          (1)

Indeed w^2 takes c^2 off zero and (c-eta M epsilon)^2 at zero; its variance is (M-1)epsilon^2(M epsilon-2 eta c)^2. This also covers previously empty rows.

Set u=c/(eta epsilon)-1. Weighted Cauchy--Schwarz gives

    (M-2-2u)^2/(u^2+M-1)
       <=4+(M-2)^2/(M-1)=M^2/(M-1).

Thus R_M(c)<=M^2 epsilon^2, and summing 2^(N-a) rows yields the uniform arbitrary-block estimate

    C_A(E)<=2^(a+2)p.                                  (2)

Consequently the TOTAL over every nonempty block of size at most b satisfies

    sum_(1<=|A|<=b) C_A(E)
       <=4p sum_(a=1..b) binom(N,a)2^a
       <=4b(2N)^b 2^-N.                               (3)

It tends to zero whenever b log N=o(N), even though the number of tested blocks grows superpolynomially. This extends A005/A053's singleton/pair surgery bound, not their already-proved pair refund classification. The exact row formula is also a regeneration certificate requiring only the uncoded seed spectrum, not an enumeration of 2^N rows: for support size J, add (2^(N-a)-J) copies of R_M(0) and one R_M(c) per old occupied coefficient.

For pairs the two A052 merging refunds remain nonnegative and their sum <=C_i+C_j<=16p. Their TOTAL over all pairs is <=16 binom(N,2)p. No new higher-arity refund identity is asserted.

## 3. Full support and physical primitivity

For each z, x -> x xor Lz is bijective, so the negative count of F is divisible by 2^r and hence even (r>=1). Editing one point makes it odd. For N>=2 every integer Walsh sum of E is then 2 modulo 4, hence nonzero; all physical coordinates are relevant.

A Boolean product across a nontrivial physical partition of sizes u,v>=1 has negative count 2^v a+2^u c-2ac, which is even. Therefore E has no nontrivial disjoint physical Boolean tensor factor. This is the same parity primitivity criterion consumed from A005; it is qualitative and supplies no quantitative product-distance reserve.

Every influence changes by at most 2p and squared-spectrum TV is at most 2sqrt(p). For v=2sqrt(p)<1/2, coupling gives entropy error <=h2(v)+Nv. Thus the edit error is O(N sqrt(p)) in entropy and <=2Np in total influence. These are rigorous asymptotic bounds, not floating comparisons.

## 4. Simultaneous rare, weak, full-support growing-block completeness

Fix ANY nonconstant seed h on n relevant bits, H_h and I_h>0. Let t->infinity, k_t=ceil(sqrt(t)), rho_t=2^-k_t, and let A_t be point activation of z times t disjoint copies of h, with k_t fresh controls and value +1 elsewhere. The old accepted activation ledger gives

    D_t=tn+1+k_t,
    H(A_t)=rho_t tH_h+2k_t rho_t(2-rho_t)+phi((1-rho_t)^2),
    I(A_t)=rho_t(tI_h+1+k_t),
    Var(A_t)=2rho_t-rho_t^2, max influence=rho_t,
    mean=1-rho_t.

Take

    b_t=max(1,floor(sqrt(t)/log2(2D_t))),
    r_t=ceil(2b_t log2(2D_t)), N_t=D_t+r_t.

Then b_t->infinity, r_t=O(sqrt(t)), r_t=o(t) and r_t<=D_t eventually. Apply the greedy code to A_t and edit physical zero to obtain E_t. The exact tag ledger gives

    I(coded A_t)<=rho_t(tI_h+1+k_t+2r_t),
    max influence(coded A_t)<=2rho_t.

The code preserves H and mean. Edit errors O(N_t 2^(-N_t/2)) and O(N_t 2^-N_t) are o(rho_t). Therefore

    I(E_t)->0, max influence(E_t)->0, mean(E_t)->1,
    H(E_t)/I(E_t)->H_h/I_h,
    sum_(1<=|A|<=b_t) C_A(E_t)->0,
    sum_(all pairs) [M_i+M_j](E_t)->0.                   (4)

The ratio limit uses the upper influence bound and the lower bound I(coded A_t)>=I(A_t), whose difference is at most2rho_t r_t. Full support and physical primitivity hold by section3. Thus every arbitrary seed survives a root endpoint with all these simultaneous restrictions AND total collision vanishing over an unbounded block scale. For fixed tau,eta,xi>0 and any fixed block floor L, the class with I,max influence<=tau, mean>=1-eta, total collision over all blocks through L <=xi, full support and primitivity has optimal H/I supremum equal to the universal one, allowing infinity.

There is also a single SEED-INDEPENDENT growing-order class: define q(N)=max(1,floor(cube_root(N))). Since N_t~nt and b_t~sqrt(t)/log2(2nt), b_t/q(N_t)->infinity for each fixed n. Eventually all blocks of size<=q(N_t) are covered by(3)-(4). The same optimal-constant equality therefore holds when the endpoint requires total collision through q(N) <=xi at its actual dimension N. The large-index threshold may depend on the seed, but the class definition and q are universal. The N12470 finite compressed recipe certifies b=4 only, not this eventual cube-root block scale. No claim is made about B/H tending to one: coding instead produces an almost erasure-free root, with the entire entropy unpaid at descendants.

## 5. Every small-block INDIVIDUAL child still violates the seed constant

Fix K>=0 and assume delta_h=H_h-KI_h>0. Activation positivity and the tag energy estimate give

    delta_K(coded A_t)/rho_t
        >=t delta_h-K(1+k_t+2r_t).                      (5)

This is positive and asymptotic to t delta_h. Every unedited child after removing a block A, 1<=|A|<=b_t, retains the same entropy and has influence I(coded A_t)-I_A, so its deficit is >=the root deficit.

Exactly one assignment per block agrees with the edited vertex. Its disagreement probability is 2^|A|p_t<=2^b_t p_t, p_t=2^-N_t. A uniform entropy error is O(N_t sqrt(2^b_t p_t)); influence error <=2N_t 2^b_t p_t. Because b_t=o(N_t) and N_t~nt, these errors are o(rho_t). Therefore EVERY INDIVIDUAL child of EVERY block of size <=b_t still violates FEI(K) for all sufficiently large t. The average child reserve S_A is strictly negative on all such blocks simultaneously.

This is the precise surviving exclusion: full support, physical primitivity, weak/rare influences and tiny TOTAL collision at growing block order do not imply same-K child certification. The family does not contradict A051/A052's critical comparison; it fails its actual physical-child premise on all small blocks. A proof using this root endpoint must retain the terminal seed deficit, not convert its tiny collision into a free stopping payment.

## 6. Reconstruction of the signed pair identity and scope boundary

For a quartet (alpha,beta,gamma,delta), let u=alpha^2+beta^2, v=gamma^2+delta^2. The weighted variance identity

    A^2/u+B^2/v-(A+B)^2/(u+v)=(Av-Bu)^2/[uv(u+v)]

with A=alpha beta and B=gamma delta proves A052's nonnegative merging refund and its exact squared formula, including zero-weight limits. The other orientation is identical. Thus C_ij=C_i+C_j+P-M_i-M_j with P=4(alpha delta+beta gamma)^2/q. The two Cauchy bounds P<=2(Inf_i+Inf_j) and C_i+C_j>=2 minority mass imply C_ij<=2(C_i+C_j)+2 orientation mass. These unconditional clauses are independently reconstructed and checked here. The critical A055/A051 reserve substitution is not independently accepted in full, because its entire row-phase chain is outside this stage's proof.

First unsupported universal line: on an actual least-dimensional K-violator, select a block whose signed collision AND retained phase/child cost can be funded below the root reserve from one unused physical influence account. Equations(1)-(5) close a stronger hardening/admission boundary, but do not supply such a selection. Since arbitrarily growing root block orders still retain arbitrary seed debt, NEXT must use genuine child certification and actual signed merging refunds, rather than enlarge a root-only collision census.

## 7. Independent A005 reconstruction and exact compressed controls

A005-SAME-C-VANISHING-PAIR-COLLISION-ADMISSION@1 is reconstructed at its exact scoped application: choose the least r with 2^r-r-1>=D and the first D distinct weight-at-least-two labels. No one or two columns of (L|I_r) sum to zero, so the old support has distance at least three. The entropy/tag-influence ledger, odd-negative-count primitivity, single-edit pair caps, total refunds and all-individual-child limit follow from sections1-3 and5 with b=2, WITHOUT depending on the pending A053 classification. This source uses the simpler unactivated tensor; its influence grows linearly and tags add at most r=O(log t), so the same-constant ratio preservation is immediate. No alteration of the A005 statement or repair is needed. A002 authored a prior general coding baseline; this is a separate reconstruction of A005's scoped application, not a claim of two independent complete major-candidate dependency-chain reviews.

For its N=200 example, regenerate the 192 eight-bit labels and count which of the64 point3 seed blocks each tag touches. The exact counts are [64,64,50,39,36,33,24,24], and each tag influence is (1-2^(-m))/2: a nonzero translation of point3 has autocorrelation1/2, and tensor autocorrelations multiply. Thus coded influence is strictly below52. The exact inequality 3^80<2^127 proves point3 deficit delta_(8/3)>137/640. Consequently the unedited root deficit exceeds91/30. For every root/singleton/pair exceptional edit the common conservative error is at most (200+98+3/2)2^-98+(8/3)*1600*2^-200<1/30. Every actual individual child deficit therefore exceeds3 bits. This independently certifies the source's compressed control without a 2^200 enumeration.

The NEW simultaneous rare/growing-block control uses the same seed, t=4096, k=64, D=12353, b=4, r=117 and N=12470. Integer tests 24706<=2^16, 24706^5>2^64 and 2^116<24706^8<=2^117 verify the precise b/r formula. The weaker 3^5<2^8 yields delta_(8/3)>1/5; (5) therefore gives root deficit/rho>328/15, rho=2^-64. The uniform all-block exceptional-child error is <=(12470+6232+3/2)2^-6232+(8/3)*2*12470*16*2^-12470<rho/2. Every individual child of every block through size4 has deficit >rho*641/30. Total influence is <2^-52; total collision through all four-coordinate blocks and total pair refunds are each <2^-12000. The actual greedy-code recipe is justified by its finite counting proof; its12470-bit table and huge code search are NOT materialized. out/COMPRESSED_CERTIFICATE.json records only exact integer/rational certificates and regeneration parameters.
