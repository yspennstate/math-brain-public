# A lossless collision statistic for the conditional-edge refund

Uniform Boolean signs, normalized Fourier amplitudes, all entropy in bits.
For coordinate i write e=Inf_i, mu(T)=p_(T+i)/e and r(T)=p_T+p_(T+i).
The oriented erasure cost is M_i=e[log2(1/e)-D(mu||r)].
The entire r law is normalized; no off-support mass is discarded.

## 1. Scope of the general information interface

For any deterministic statistic C(T), the exact KL chain rule is
D(mu||r)=D(mu_C||r_C)+E_(mu_C)D(mu(.|C)||r(.|C)).
Equality with the coarse divergence holds iff mu(T)/r(T) is constant on
each occupied C-fiber (off-support rows remain in r_C).
These are GENERIC probability facts, not Booleanity-specific improvements.
The new test is whether a statistic fixed by the actual signed Boolean
factor expansion can satisfy this criterion without erasing the growing
positional refund identified by A090. An arbitrary function's exact
likelihood-ratio statistic is tautological and does not solve the problem.

## 2. Signed admission and the three-state witness

Take t disjoint blocks of width w, q=2^-w, s=1-q, and
f=2 product_b(1-A_w)-1, A_w the all-zero point indicator.
Every factor 1-A has signed Fourier coefficients s at empty and -q at
each nonempty label. Hence, BEFORE squaring, for nonempty S touching j
blocks a_S=2(-q)^j s^(t-j), while a_empty=c=2s^t-1.
This is an actual sign function: all signed convolution identities follow
by Fourier transforming f^2=1. Taking absolute values before this product
expansion would not justify the admission or its exceptional empty row.
Every coordinate has e=2q s^(t-1), also by direct pivotal counting.

For coordinate i in block b define a three-state statistic:
0: T empty; 1: T nonempty but avoids b minus {i};
2: T meets b minus {i}.
The EXACT derivative masses and complete residual masses are

 mu_C=(e, 2q-e, 1-2q),
 r_C=(c^2+e^2, e(2q-e)(s^2+q^2)/q^2, 2e(1-2q)).       (1)

In state2 both adjacent amplitudes are equal, so mu/r=1/(2e).
In state1 the two amplitudes have signed ratio -q/s; thus
mu/r=q^2/[e(s^2+q^2)]. In state0 the ratio is e/(c^2+e^2).
All ratios are constant inside their states, including the exceptional
empty amplitude c. Therefore

 D(mu||r)=D(mu_C||r_C),                                (2)
 M_i/e=e log2((c^2+e^2)/e^2)
       +(2q-e)log2((s^2+q^2)/q^2)+(1-2q).             (3)

These formulas hold for all integers w,t>=1, with zero states omitted by
continuity. They compress exponentially many Fourier rows to three states
WITHOUT discarding any conditional divergence. No witness-code length is
being substituted for an entropy price: both coarse laws are normalized,
and (2) is an exact reference identity.
The complete joint laws are P(i,z)=(e_i/I)mu_(C_i)(z) and
Q(i,z)=(e_i/I)r_(C_i)(z). Each has total one and coordinate marginal e_i/I.
Hence I D(P||Q)=sum_i e_i D(mu_i||r_i), and the one aggregate bill is
M=I[sum_i(e_i/I)log2(1/e_i)-D(P||Q)]. No separate whole I is spent per
state or degree. The physical block partition is an actual hypothesis,
not a cost-free universal representation selected after looking at f.
Adding degree to C is still lossless. Thus for the degree statistic L,
D(mu||r)-D(mu_L||r_L)=E_(mu_L)D(mu_(C|L)||r_(C|L)).
The positional refund lost by degree is completely carried by this
three-state collision flag on tribes, not by enumerating row addresses.

## 3. Quantitative repair of A090's degree-only obstruction

For w>=4 and t=2^w, s^(t-1)<=1/2 (binomial expansion of its reciprocal),
so e<=q<=1/16. Parseval gives c^2+e^2<=1, and s^2+q^2<=1.
Since x log2(1/x) increases for 0<x<=1/16,
the first term in (3) is at most 2e log2(1/e)<=2wq.
The second is at most 2q log2(1/q^2)=4wq; the third is <=1.
Consequently

    M/I=M_i/e<=1+6w2^-w<=5/2.                        (4)

The last sequence decreases for integer w>=4. This is payment of the
unchanged conditional-edge reference, not a new priority claim about
FEI for tribes. A090 already bounded M/I by6 via entropy and proved
D_degree<=3+log2(w+1/2). Combining the latter with (2)-(4),

 D_full-D_degree >= w-13/2-log2(w+1/2).               (5)

For w>=32 it is also at least w/2-5/2, using A090's M_degree/I>=w/2.
Thus a finite collision flag exactly recovers the growing within-degree
refund on this obstruction family. A090's no-go for degree alone survives.
The lower bound involving degree uses that scoped source theorem, not
a new derivation of its block-count tail argument.

## 4. Non-Boolean, tensor, and vacuous-embedding guards

For the normalized real product spectral vector on n=64 with squared
law Bernoulli(1/64)^tensor64, the inverse function is
product_i(sqrt(63/64)+sqrt(1/64)x_i). It is not a sign function;
its U={i} signed convolution is 2sqrt(63)/64, not zero.
For every i its derivative law equals its residual law, giving D=0,
M_i/e_i=log2 64=6 and M/I=6>5/2. Any fixed partition, including C,
is lossless here too. Thus lossless compression alone is generic and
cannot imply payment; the signed Boolean factor admission in (4) matters.

Tensoring f by any Boolean sign on fresh variables preserves e,D_i and
M_i/e_i for each OLD coordinate, since mu and r tensor with the SAME
normalized spectator spectrum. The old C can ignore spectators and
remains sufficient; (2) holds with an arbitrary terminal spectator.
Its entropy and influence have not disappeared: joint M and I are additive.
Constant spectators are dummy embeddings. The w=1,t=3 table is the
three-bit point defect up to sign/input flips and is in the checker.
No product conditional-law/address admission is imposed.

## 5. Arbitrary-terminal activation: one paid flag, unpaid seed remains

Let g be ANY actual Boolean terminal core, not necessarily tribes. Form
h=chi_Z g^tensor m with ell>=2 fresh parity bits. For k>=1 fresh point
controls, q0=2^-k and F=1+A_k(h-1), the signed coefficients are
a_empty=1-q0, a_purecontrol=-q0, a_(S,U)=q0 hhat(S) for S nonempty.
The mean and singleton coefficients of h vanish. On an OLD data row,
mu_i(F) is mu_i(h) tensored with uniform control labels; r_i(F) on its
support is q0 times r_i(h) tensored with that same law. Therefore

    D_i(F)=k+D_i(h), M_i(F)=q0 M_i(h).                (6)

The k refund is precisely the binary flag that the residual core label is
nonempty: its mu-probability is1 and its r-probability is q0. Conditional
on that flag, the normalized row pair is the original terminal pair
tensored with spectators. If a statistic is sufficient for the seed row,
this flag plus the seed statistic is sufficient for the activated data
row; otherwise its CONDITIONAL KL debt survives unchanged. Pure-control
rows and the exceptional empty amplitude remain in the complementary
reference event. No hidden renormalization to total q0 is made globally.

Thus for a tribes seed the one binary activation flag plus its three-state
collision witness is lossless on all original coordinates and retains
the paid seed price (4). For an arbitrary seed it only proves
M_data(F)=q0 mM(g); I(F)=q0[mI(g)+ell+k]. The first unsupported universal
line is a bound on M(g)/I(g), equivalently the remaining C018 erasure
refund. Activation and a sufficient-statistic declaration do not prove it.

The next mechanism must obtain a physically certified low-complexity
collision partition for genuinely overlapping derivative supports, with
one influence ledger and conditional/terminal KL debt still present.
