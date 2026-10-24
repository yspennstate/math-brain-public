# Full-activity matching-edge certificate with arbitrarily many twins

## Theorem and scope

Let `m≥4` terminal vertices each join all three core vertices by edges of one common activity `a>0`. The core-edge activities are arbitrary `p,q,r≥0`; setting them to zero allows missing core edges. Add the two marked edges joining terminal pairs `(0,1)` and `(2,3)`. There are no other edges between terminals.

For the weighted forest polynomial `Z=Σ_{F acyclic} ∏_{h∈F} z_h`, the marked Rayleigh difference `R=Z_eZ_f-ZZ_ef` is strictly positive at every activity choice of this form. The marked-edge activities themselves may be arbitrary positive numbers, since `R` is independent of them. Under the forest probability measure proportional to the same product of activities,

\[
\Pr(e\in F)\Pr(f\in F)-\Pr(e,f\in F)=\frac{z_ez_f}{Z^2}R>0.
\]

Parallel core edges may be aggregated by adding their activities, because an acyclic set can select at most one edge from a parallel class. This gives the same result for a three-vertex multigraph core after aggregation.

Put

\[
d=1+3a,\quad X=p+q+r,\quad t=pq+pr+qr,
\quad L=3+2X,\quad S=1+X+t.
\]

The exact certificate is

\[
\boxed{
R=4a^4d^{2m-8}
\left[
d^2(L^2-6S)+6ad(1+ma)L+9a^2+30ma^3+18m^2a^4
\right].}
\]

Indeed,

\[
L^2-6S=3+6X+4(p^2+q^2+r^2)+2(pq+pr+qr)>0.
\]

Thus every term in the certificate is positive or nonnegative. This is a full finite-activity result for an unbounded graph family, with arbitrary weights on the three-vertex core. It does not establish the arbitrary-core forest Rayleigh conjecture. No historical novelty claim is made.

## Exact terminal transfer

Condition on a forest of the three core vertices, and record its connectivity partition. There are five possible partitions. Adding one terminal chooses zero, one, two, or three incident spokes. Zero or one spoke leaves core connectivity unchanged, giving scalar `d=1+3a`. Two spokes are allowed exactly when their endpoints are in distinct components; let `P` count these choices and merge their components. Three spokes are allowed exactly when all three core vertices are in distinct components; let `Q` merge all three.

Therefore the connectivity transfer is

\[
T(a)=dI+a^2P+a^3Q.
\]

The exact multiplication rules are

\[
P^2=6Q,\qquad PQ=QP=Q^2=0.
\]

For `P²`, starting from three components, the first merge chooses one of three pairs; the second merge can join either vertex of that pair to the remaining vertex, giving six possibilities. Starting from fewer components, two such merges are impossible. All other products displayed would merge an already merged set and are forbidden by acyclicity.

Let the row vector of initial core-forest weights be `r`, and let `1` be the column vector of ones. Direct enumeration of the core gives

\[
r1=S,\qquad rP1=L,\qquad rQ1=1.
\]

The core forests have zero-edge weight one, one-edge total weight `X`, and two-edge total weight `t`. A first pair merge has three choices from the empty core and two from each one-edge forest; a triple merge is possible only from the empty core. These facts give the three identities.

Since every transfer is a polynomial in the same nilpotent operators, the order of the terminals is irrelevant. The power formula is

\[
T(a)^k=d^kI+kd^{k-1}a^2P+
\big[kd^{k-1}a^3+3k(k-1)d^{k-2}a^4\big]Q.
\]

## Marked-edge contraction

Write `Z=A+z_e B_e+z_f B_f+z_ez_f C`. Terminal symmetry gives `B_e=B_f=B`, so `R=B²-AC`.

Including a marked edge contracts its two terminals. Their two parallel spokes to each core vertex aggregate to activity `2a`; no forest can contain both parallel edges. Thus each contracted terminal contributes `T(2a)`, and

\[
A=rT(a)^m1,\quad
B=rT(2a)T(a)^{m-2}1,\quad
C=rT(2a)^2T(a)^{m-4}1.
\]

Put `h=1+6a` and

\[
u=\frac{a^2}{d},\quad v=\frac{a^3}{d},\quad
w=\frac{4a^2}{h},\quad z=\frac{8a^3}{h}.
\]

The normalized quantities are

\[
U_A=\frac A{d^m}=S+muL+mv+3m(m-1)u^2,
\]

\[
U_B=\frac B{hd^{m-2}}=
S+[(m-2)u+w]L+(m-2)v+z
+3(m-2)(m-3)u^2+6(m-2)uw,
\]

\[
U_C=\frac C{h^2d^{m-4}}=
S+[(m-4)u+2w]L+(m-4)v+2z
+3(m-4)(m-5)u^2+12(m-4)uw+6w^2.
\]

These formulas remain valid at `m=4`, because terms multiplying a zero factor vanish.

## Cancellation producing the positive certificate

Define

\[
\delta=w-2u=\frac{2a^2}{dh},\qquad
\kappa=\frac{6a^3(1+2ma)}{d^2h},\qquad
\eta=6\delta^2=\frac{24a^4}{d^2h^2}.
\]

Direct subtraction of the preceding exact expressions gives

\[
U_B-U_A=\delta L+\kappa,\qquad
U_C-2U_B+U_A=\eta.
\]

Consequently,

\[
U_B^2-U_AU_C=(\delta L+\kappa)^2-\eta U_A.
\]

This is an algebraic identity; the negative term has not been discarded. Substitute `U_A` and clear the common denominator to obtain

\[
U_B^2-U_AU_C=
\frac{4a^4}{d^4h^2}
\left[d^2(L^2-6S)+6ad(1+ma)L+9a^2+30ma^3+18m^2a^4\right].
\]

Finally, `R=h²d^(2m-4)(U_B²-U_AU_C)`, which proves the boxed formula.

## Verification

The proof above is symbolic for all integer `m≥4`; finite checks are not used to extend its range. The companion `twin_matching_core3_all_terminal_counts.py` nevertheless independently enumerates subsets of the original uncontracted graph for three cases, testing acyclicity before and after adding each marked edge. It verifies the exact `A,B_e,B_f,C` values and the certificate. Additional exact rational transfer checks cover several terminal counts up to `m=100`. See the companion results file.

The three directly checked cases include nonuniform positive core weights and a missing core edge. The direct subset checker does not use the nilpotent transfer to calculate the four forest coefficients.
