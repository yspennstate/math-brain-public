# Same-constant admission into the vanishing-pair-collision endpoint

All functions are actual Boolean signs on finite uniform cubes. Entropy is in bits. The normalized Fourier law is fhat(S)^2. Fix a nonconstant seed h on n relevant inputs, H=H(h), I=I(h)>0. Known tensor/systematic-code ledgers are consumed from A002; the new application is to A053's distance-three collision/refund endpoint, removing the triple-parity construction's factor-three loss. It does not alter the optimal constant of the particular triple-parity-only family.

## 1. An explicit logarithmic-redundancy distance-three code

For t>=1 let D=tn and let r be the smallest integer with 2^r-r-1>=D. Choose the first D distinct nonzero r-bit vectors of weight at least two, in increasing integer order, and call them l_1,...,l_D. On D+r independent physical bits x,z define

    F_t(x,z)=h^tensor t(x_1 xor <l_1,z>,...,x_D xor <l_D,z>).

Here h^tensor t is evaluated blockwise; xor is only a physical coordinate representation of the uniform sign cube. Its Fourier index map is S -> (S, xor_(j in S) l_j), which is injective. Distinct code indices differ in at least three coordinates: a one-data-bit difference has tag weight>=2; a two-data-bit difference has nonzero tag because the labels are distinct; three or more data differences already suffice. Thus all singleton and pair retained Fourier rows of F_t contain at most one occupied coefficient.

The exact previously known ledgers give

    H(F_t)=tH,
    I(F_t)=tI+sum_(a=1)^r e_a,     0<=e_a<=1,

where e_a is the probability that tag a belongs to the coded spectral index. For D>=2, r<=ceil(log2 D)+2: 2^(ceil(log2 D)+2) is at least 4D and r+1<=3D. Therefore r=O(log t) for fixed n and H(F_t)/I(F_t)->H/I. No auxiliary physical influence is discarded. Tags may be irrelevant before surgery; the final function has no irrelevant inputs.

## 2. One physical edit, full support and primitivity

Flip F_t at physical zero, obtaining G_t on N=D+r bits; p=2^-N. For each fixed z, x -> x xor Lz is bijective. The negative count of F_t is therefore divisible by 2^r and is even. A single flip makes it odd. When N>=2 all integer Walsh sums of G_t are 2 modulo 4: for nonempty frequencies they are -2 times an odd signed sum over negative inputs; at the empty frequency they are 2^N minus twice the odd negative count. Hence every coefficient is nonzero and every physical coordinate is relevant.

A Boolean product across any nontrivial coordinate partition has even negative count, since its negative count is 2^b u+2^a v-2uv for a,b>=1. Thus G_t is prime with respect to every coordinate partition. Equivalently its multiplicative-plaquette interaction graph is connected: a disconnected graph would force the Boolean exponent to split as a sum across graph components, and hence the sign to factor. This is qualitative primitivity, not a bound on distance from products.

Each influence changes by at most 2p, so |I(G_t)-I(F_t)|<=2Np. The squared Fourier laws have total variation at most 2sqrt(p). Coupling gives |H(G_t)-H(F_t)|<=h2(v)+Nv for sufficiently large N, v=2sqrt(p). These errors tend to zero, while I(F_t) is linear in t. Consequently

    H(G_t)/I(G_t) -> H(h)/I(h).                          (1)

## 3. All-pair prices and the endpoint's exact constant

A053-REFUND-ZEROS-AND-SPARSE-CODE-SURGERY@1 Sections 2--3 applies to ANY distance-three Boolean seed. Its proof is independently reconstructed here at the required subset scope. In a singleton row the edited previously zero amplitude has magnitude 2p. Then 4a^2 b^2/(a^2+b^2)<=4(2p)^2; summing 2^(N-1) rows gives C_i<=8p. For each pair, the nonnegative total merging refunds obey M_i+M_j<=C_i+C_j<=16p. Shift the old occupied coefficient to the empty corner by a Fourier character. The other three amplitudes have magnitude 2p; weighted Cauchy--Schwarz bounds that row's pair collision by 16(2p)^2, giving C_ij<=16p after summing 2^(N-2) rows.

Thus both the sum of all pair collisions and the sum of both refunds over all pairs are at most

    16 binom(N,2) 2^-N ->0.                            (2)

Conditional off-anchor spectral mass for a pair is 3p. Hence B_A<=h2(3p)+3p log2 3. Its physical restriction divergence is at most C_A/ln2; this follows rowwise from the order-two divergence bound and averaging over the actual child law. Therefore the decrement L_A satisfies

    L_A<=h2(3p)+3p log2 3+16p/ln2 <(3N+29)p.          (3)

Let C_* be the extended-real supremum of H/I over all nonconstant Boolean signs. For any fixed epsilon>0, the class of prime, full-Fourier-support signs for which both total quantities in (2) are at most epsilon has optimal FEI constant exactly C_*. Indeed (1),(2) admit each fixed arbitrary seed with its ratio preserved, and inclusion gives the opposite inequality. A bound H<=C I on the systematic-code-and-edit family itself also gives universal FEI(C) at the same C. This is a new endpoint application of known ledgers; no universal upper bound is proved. The factor-three loss belongs to A053's particular triple substitution, not to its qualitative vanishing-refund endpoint.

## 4. Exact obstruction to critical-witness admission

Fix K>=0 and assume the arbitrary seed has delta_h=H(h)-K I(h)>0. Then

    delta_K(G_t) >= t delta_h-K r-o(1),

which grows linearly with t. For every pair A, define the actual average physical child reserve S_A=-E_a[H(G_t|A=a)-K I(G_t|A=a)]. The exact restriction identity is

    S_A=L_A-K I_A-delta_K(G_t).

Using (3), for every pair simultaneously,

    S_A <= (3N+29)2^-N-delta_K(G_t) <0                 (4)

for all sufficiently large t. No healthy lower bound on query influence or positive lower bound on the root gap is assumed; the tensor root gap itself pays for the exclusion. The same conclusion holds for every singleton using L_i<(2N+13)p. Thus these admitted roots have uncertified average children on EVERY pair and singleton, not merely on a special auxiliary direction. They cannot be least-essential-dimension K-violators. The precise blocking hypothesis is genuine fixed-K physical-child certification, which root primitivity, full support and tiny pair collision/refunds do not supply.

In fact every individual child also violates K eventually. Removing any block A of size at most two is injective on the old distance-three support. For EVERY assignment a, the unedited child has H=tH(h) and I=I(F_t)-I_A(F_t), so its deficit is delta_K(F_t)+K I_A>=delta_K(F_t). Exactly one assignment agrees with the flipped vertex and is edited; its disagreement probability is 2^|A| p<=4p, its entropy error is O(N sqrt(p)), and its influence error is O(Np). Both tend to zero uniformly over all blocks and assignments. Thus every actual singleton and pair child retains the positive linear seed deficit. The compressed N=200 certificate records the uniform exceptional-child lower bound as well as (4); it is not an enumeration of 2^200 inputs.

FIRST UNSUPPORTED UNIVERSAL LINE: select/pay a pair or larger block on a genuinely least-dimensional K-violator, using its actual nonnegative S_A and one owned influence account. The A051/A052 phase and signed-parity banks are necessary conditions; the admission above proves neither their missing selection nor a universal positive refund floor. Request a proof of that actual critical selection, not a root-only primitivity or small-refund assertion.

## 5. Independent reconstruction of A002 same-C completeness

A002-SIGNED-PRICE-SAME-C-COMPLETENESS@1 is reconstructed without a repair. For a tensor, each physical child changes only one seed factor, so sigma_i(f^tensor t)=sigma_i(f)-(t-1)delta. Since B_i and JS_i are unchanged, q_C,i=max(B_i/d_i,C+(t delta-JS_i)/d_i). Taking a minimum over finitely many seed directions yields Q_C/t->delta/d_max for delta>0. FEI(C) gives sigma>=0 and Q_C<=B/I<=C; the tensor lower bound forbids a sublinear dimension envelope if a violating seed exists. This proves the exact same-C dichotomy.

The restricted rare/full-support branch is also valid: balance t copies, activate at k=ceil(sqrt(t)) fresh controls, p_t=2^-k. The largest influence is p_t and delta/p_t>=t delta_h-C(1+k). After two dummy bits and a point edit, dimension N_t=tn+k+3, entropy error O(N_t 2^(-N_t/2)) and influence error O(N_t 2^-N_t) are o(p_t). Hence liminf Q_C/N_t>=delta_h/n. The rare/weak/full-support restrictions do not remove the debt. This review uses a direct physical-child reconstruction and independent exact small spectra; A005 authored an earlier dependency but supplies no repair or contribution to A002's new version. No acceptance is claimed for unrelated A061 multi-quantity assertions.
