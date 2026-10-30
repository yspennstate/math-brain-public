# The uniform-core bill diverges inside the positive-private-clause family

This strengthens the dummy-data majority control in CORE_FUSION.md to the
SAME physical clause class used by the paid two-core theorem, allowing its
core size to grow. No empty private block or vanishing activation limit is
needed. This is a reference-cost obstruction, not an FEI counterexample.

Let s=2m+1>=3. For every T subset[s] of size m+1 introduce s FRESH private
bits x_(T,1),...,x_(T,s). Define the actual monotone Boolean indicator

    F(z,x)=prod_(|T|=m+1) prod_(l=1)^s OR(z_T,x_(T,l)),
    f=2F-1, h(z)=Maj_s(z).

Every private block has width1, all are physically disjoint, and all core
anchors have size m+1. The number of private bits is s binom(s,m+1), finite
for each s. These are exactly shared-core OR clauses with nonempty private
blocks, not a surrogate formula on independent copies of the core.

Put delta=2^-s. If h=1, every anchor OR is true, so F=1. If the core has k
ones with k<=m, the number of false anchors is b=binom(s-k,m+1)>=1. The
residual is AND of exactly s*b independent private bits; hence

    Pr_x[F=1|z]=delta^b<=delta,
    D=Pr[f!=h]<=delta/2.                              (1)

The core conditional mean mu(z)=E_x f equals1 on the true-majority half
and equals-1+2delta^b on the false half. Consequently

    E mu^2>=1-2delta,  0<=E mu<=delta,
    N=Var_z(mu)>=1-2delta-delta^2>=1-3delta>=5/8.      (2)

N is precisely the ACTUAL core-only nonempty Fourier mass by Walsh/Parseval.
For each core coordinate, its pivotal indicator differs from that of h
only if f!=h at at least one endpoint. Uniformity of a bit flip gives

    I_core(f)<=I(h)+2sD<=I(h)+s delta.                (3)

Given a false-majority core, the residual private influence is
2s*b*delta^b. Since b delta^(b-1)<=1 for every integer b>=1 and delta<=1/8,
averaging over the false half gives I_private(f)<=s delta. This counts ALL
private coordinates; their huge number has not been multiplied by a loose
union bound. For example b<=2^(b-1) by induction implies the needed bound.
Thus

    I(f)<=I(h)+2s delta<=I(h)+1<=2I(h).               (4)

Here 2s/2^s<=1 for s>=3, and I(h)>=Var(h)=1.

Use EXACTLY the fixed Q from CORE_FUSION.md(1), now with this s-bit core.
The all-zero core slice has all private clauses present, ensuring qbar is
strictly positive; other nonconstant slices use their supported local mask
law. Every nonempty core-only set has probability1/[2(2^s-1)], independent
of qbar. Therefore its COMPLETE nonempty cost obeys

    C_Q(f)>=N[1+log2(2^s-1)]>=5s/8,
    C_Q(f)/I(f)>=(5/16)s/I(h)
                >=(5/16)sqrt(m+1) -> infinity.        (5)

The last inequality uses the central-binomial proof already given in
CORE_FUSION.md: I(h)=s binom(2m,m)/4^m. All remaining output costs are
nonnegative, and the full wrapper is nonnegative, so neither can repair
(5). No cost of one selected witness is confused with the entire output
law: the lower bound uses an actual spectral sector of the normalized Q.

This establishes the exact missing compression feature even within the
expanded clause class: one must compress a growing CORE Fourier set rather
than transmit it with a uniform s-bit tag. Paying local masks or refining
the slice mixture alone cannot repair the core-only debit. Equation(5)
does not prove H(f)/I(f) diverges; no FEI disproof is claimed.
