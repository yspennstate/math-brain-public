# A leafless family keeps the remaining scale charge large

For m>=2 take the exact monotone prime table R_ij={x_i,y_j}, 1<=i,j<=m.
Its Boolean union is B_m=OR_i x_i AND OR_j y_j; use g_m=2B_m-1 and independent
uniform bits (literal 1 means satisfied). Every variable lies in m primes;
there are no private leaves. The primes are EXACT: a positive implicant must
force a satisfied literal on both sides, and their minimal choices are pairs.
Negative literals cannot help a monotone implicant become minimal.

The single fixed feasible vector lambda_ij=1/m saturates every physical
packing row. It has Lambda=sum lambda=m, so a fresh common control requires
beta<=1/m if this table and scale are retained. This is an assertion about
the fixed weight vector, not about every possible reference on these primes.

Let a=2^-m. Expansion g_m=1-2A-2B+2AB, where A and B indicate all-zero
left/right blocks, gives these EXACT magnitudes of nonempty Fourier coefficients:

    |ghat(T)|=2a(1-a) if T is nonempty and lies on one side;
    |ghat(T)|=2a^2    if T meets both sides.

Physical pivot counting independently gives I_g=4ma(1-a), since one input
is pivotal exactly when its other m-1 side bits are zero and the opposite
side is nonzero. Both computations include all 2m physical coordinates.

For EVERY within-side selected set T, each edge prime contains at most one
selected coordinate. Each nonempty owned block therefore has size one and
EVERY eligible partition uses exactly k=|T| gates. This remains true for every
old actual forest, every posterior on those forests and every positive feasible
weight vector. In particular it holds for the original posterior used in the
one-control transfer; root choice or chronological reweighting cannot change it.

For the SAME M=sum_(T!=empty)P_g(T) E_eta(k-1) used in ONE_CONTROL.md,
nonnegativity on cross sectors and the within-side coefficients imply

    M >= 8a^2(1-a)^2 [m2^(m-1)-(2^m-1)]
       = 4a(1-a)^2(m-2+2a).

Since M<=I_g-Var(g)<=I_g and I_g>0,

    1 >= M/I_g >= (1-a)(m-2+2a)/m -> 1.

These are uniform bounds over the old posterior, so the limiting statement
does not exchange a limit with any unknown posterior sum. In particular, at
the fixed uniform vector and beta=1/m, m>=4 gives

    [M log(1/beta)]/I_g >= (15/32)log m -> infinity.

This refutes the proposed auxiliary payment M log Lambda <= K I_g for every
feasible original reference, even on leafless actual Boolean prime tables.
It does NOT lower-bound the actual signed correction Psi: (6) is an upper
bound, and old root/factorial credits were deliberately bounded below by one.
It does NOT refute the infimum over fixed references, the complete witness
mechanism, or FEI. The underlying Boolean function is a read-once AND of two
OR gates. A grouped representation removes the graph-edge label issue.

The compression still missing at this leafless boundary is a COUPLED payment
of scaling and inherited reference cost using the actual root/factorial
numerator, or a single replacement reference whose complete cost is paid.
Neither an ownership tail nor a standalone excess-gate scale budget suffices.

## The complete signed transferred bill also diverges at this fixed vector

The preceding standalone-term obstruction can be strengthened without discarding
other sectors. Keep lambda=1/m, beta=1/m, the SAME old posterior and the EXACT
one-control distributed correction Psi of ONE_CONTROL.md. For a within-side
T with s=|T|, every owned size and selected intersection is one. There are no
selected incidence edges, hence c=k=s and all used gates are roots. All pi=1/4.
Consequently, for EVERY old record and therefore also its exact posterior,

    L0(T)=m^-s,
    J1(T)=s! m^-s 2^(4(s-1)/5).

Both root rarity and chronological factorial credit are included here. Since
s!<=m^s, -log J1(T)>=-4(s-1)/5. The within-side contribution to Psi is thus at least

    (I_g/4)(1-a)log m - I_g/5.                              (7)

The remaining nonempty data sets meet both sides. Their total squared Fourier
mass is exactly W_cross=4a^2(1-a)^2. For any such record s_l<=kappa_l<=2.
Each ratio w_l(0) is <=1, and w_l(1) is one for (s_l,kappa_l)=(1,1),(2,2),
and (8/9)^gamma for (1,2). Thus Z<=k, and the exact root multiplier is at most
(k-1)!4^(k-1). It follows that

    J1(T)<=k!4^(k-1) averaged over k<=2m <= (8m)^(2m).

This upper bound survives the SAME posterior because it is uniform recordwise.
Moreover L0<=1. The total cross contribution to Psi is therefore at least

    -(I_g/2)a(1-a)log(8m) >= -(5/32) I_g,                 (8)

where m>=4 uses log(8m)<=m+1 and (m+1)2^-m<=5/16.
The first follows from 8m<=2^(m+1) at m=4 and the adjacent ratio (m+1)/m<=2;
the second follows from its adjacent ratio (m+2)/(2(m+1))<=1.

Finally the EXACT normalizers are

    D=(1+1/(4m))^(m^2)-1,
    D'=(1+1/(8m^2))^(m^2)-1.

Bernoulli gives D'>=1/8 and log D<=m log(e)/4. Since v<=8a,

    (v/2)log(2D'/D) >= -8a-ma log(e) >= -I_g             (9)

for m>=4: dividing the positive magnitudes by I_g gives
[2/m+log(e)/4]/(1-a)<=[1/2+3/8]/(15/16)=14/15<1.
No unknown-sign normalization term is omitted in this lower bound.

Combining (7)--(9), all sectors and both exact posterior coefficients are accounted for:

    Psi/I_g >= (15/64)log m - 217/160
             >= (15/64)log m - 3/2 -> infinity.           (10)

This is an all-dimensional obstruction to influence payment of this COMPLETE
signed transferred surrogate correction at the fixed uniform edge reference.
It is stronger than divergence of a discarded positive term. It is still NOT
a lower bound on actual optimal code cost or the variational infimum: the
source transfer is an upper-bound mechanism, and other feasible scales or
grouped references may work. The inherited base residual remains a separate
term; no inference about cancellation with it or a lower bound on final output
cost is made. The exact missing transfer feature is now visible in L0:
chronological/root credits refund the nonempty-control labels, whereas empty-
control data sets retain m^-s. A repair must price that sector jointly with
the inherited base reference, or replace the fixed reference once for all sets.
