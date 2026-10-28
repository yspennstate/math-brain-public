# Protected-tag interleaving leaves exactly the seed stopping cost

Mathematical rung: complete derivation, with exact validation recorded separately.
Independent review is pending. This is a route obstruction and conditional
transport identity; it is not a new universal Booleanity inequality.

All coordinates are independent uniform signs. H is squared Fourier entropy
in bits, I is total physical influence, and Delta_i H(g) is H(g) minus the
average of the two complete Boolean child entropies. Fix any real C>=0.

## Complete Booleanity hierarchy and imported obstructions

For a real Fourier vector a, the hierarchy used here is the ENTIRE system

    sum_S a_S a_(S xor U) = 1{U=empty}, for every U.

Fourier inversion makes it equivalent to f(x)^2=1 at every physical point.
Equivalently, at every restriction and every next physical bit, write
f=A+x_i B. Then A B=0 and A^2+B^2=1 pointwise. Recursing retains the
complete pair identities, not only the range or granularity of derivatives.
For nonempty T, D_T f belongs to 2^(1-|T|) Z intersect [-1,1], on every
remaining point. This necessary derivative grid alone is not substituted
for the pair identities. For n>=1 all Walsh coefficients are in
2^(1-n) Z; keeping this arithmetic alone is also insufficient.

ROUTE_MAP_CURATED section 3 imports the fixed-order G_(K,w) obstruction
from BOOLEANITY_ORDER Theorem 2.1, K=4^k. Its norm is one; square-spectrum
coefficients through order 2w-1 vanish; I=w+3/4; and
B/I > [3/(4w+3)] log2(1+K/4), unbounded in K. Its coefficients are dyadic,
E G^4<3, and restrictions fixing at most 2w-1 coordinates have norm one.
The same source records vanishing-defect strengthenings. These are
non-Boolean controls, not counterexamples to FEI. Their original checker
is not rerun in this stage. The distinct fixed atom-cap cyclic obstruction
is imported only at the audited scope stated in the campaign plan:
every prescribed fixed cap prefix admits unbounded non-Boolean B/I.
The local curated source still does not give its complete construction
or original checker. Full source import of THAT family remains blocked;
no parameters or exact definition are invented here.

## Representation and exact whole-spectrum identities

Let A,B be ternary functions on a controller cube c, with A B=0 and
A^2+B^2=1 pointwise. Let h be ANY Boolean function on a disjoint seed cube y.
Introduce a physical balancing bit ell and set

    F(c,ell,y)=A(c)+B(c) ell h(y),   beta=E B^2.

F is Boolean by the complete pair identities. On any partial controller
restriction s let G_s(c,ell)=A_s(c)+B_s(c)ell and beta_s=E B_s^2.
On any partial seed restriction t let h_t be the complete remaining seed.
The tag ell remains unqueried throughout the theorem. Fourier inversion
gives two DISJOINT sectors:

    ell-frequency 0: Ahat_s(T) 1{seed-frequency=empty},
    ell-frequency 1: Bhat_s(T) hhat_t(V).

Thus, without a dropped normalizer or terminal sector,

    H(F_s,t)=H(G_s)+beta_s H(h_t),
    I(F_s,t)=I(G_s)+beta_s I(h_t).

The influence formula includes the balancing bit inside I(G_s). For a
controller query i, averaging over ell kills the cross term in physical
edge differences. Hence Inf_i(F_s,t)=Inf_i(G_s). For a seed query j,
Inf_j(F_s,t)=beta_s Inf_j(h_t). Also
beta_s=(beta_s,+ + beta_s,-)/2 under EVERY controller query. Consequently
the signed one-query debts d_C=Delta H-C Inf obey

    controller i: d_C(F_s,t;i)=d_C(G_s;i),
    seed j:       d_C(F_s,t;j)=beta_s d_C(h_t;j).

These statements allow arbitrary seed bias, deterministic coordinates,
beta=0 and beta=1. All complete child entropies remain in Delta H.

## Exact optimal stopping identity, including arbitrary interleavings

Let V_C(h) be the maximum, over finite adaptive physical seed stopping
trees, of sum_v reach(v) d_C(h_v;i_v); stopping immediately is permitted.
Let U_C(G_s) be the analogous maximum over controller-only trees for G_s,
with ell protected. All maxima exist: the coordinate sets are finite,
each query removes a bit, and there are finitely many such trees. The same
statement allows a fixed subset of controller coordinates as queries;
all other controller coordinates remain in the complete terminal spectrum.
This is the version used for A032's four u bits below.
Let W_C(F_s,t) allow arbitrary adaptive interleavings of controller and
seed queries, still protecting ell. Then the exact identity is

    W_C(F_s,t)=U_C(G_s)+beta_s V_C(h_t).                 (*)

Upper bound: induct on the total number of unqueried controller and seed
coordinates. The right side is nonnegative because U,V admit stopping.
For a controller query, its Bellman continuation equals

    d_C(G_s;i)+avg U_C(G_child)+avg beta_child V_C(h_t)
      <= U_C(G_s)+beta_s V_C(h_t).

For a seed query it equals

    U_C(G_s)+beta_s[d_C(h_t;j)+avg V_C(h_child)]
      <= U_C(G_s)+beta_s V_C(h_t),

using beta_s>=0. These are all available actions, proving the upper bound.
Lower bound: execute an optimal controller tree first. At EVERY resulting
controller leaf execute an optimal seed tree, unless beta_leaf=0 (where
any seed tree has zero cost). The controller cost is U_C(G_s), and the
seed cost is E beta_leaf V_C(h_t)=beta_s V_C(h_t) by conservation of beta.
This is an admissible mixed stopping tree, proving equality. In particular
query choices depending on the other branch history cannot improve (*).

No all-dimensional limiting argument or optional-stopping integrability
assumption is hidden here: every tree has depth at most the total number
of controller and seed coordinates. The policy/witness may depend on h,
C, s, and t, exactly as permitted by the maxima's quantifiers.

## Full Booleanity does not add a mixed seed constraint in this family

For arbitrary real h the exact defect factorization is

    F^2-1=B^2(h^2-1),
    E (F^2-1)^2=beta E (h^2-1)^2.

For beta>0, F is Boolean if and only if h is Boolean. For beta=0, F is
independent of h and no conclusion about h follows. This checks the one
denominator/positivity side condition; we never cancel beta at zero.
Thus the full signed hierarchy in the complementary seed is preserved,
rather than replaced by a fixed prefix or a small-defect relaxation.
The entropy/optimal-stopping identity (*) also holds for normalized real
seed amplitudes. It therefore does NOT pass B07's novelty test for a new
Booleanity inequality. Its legitimate use is to rule out an extra discount
from protected-tag interleaving; the remaining seed term is explicit.

For a normalized real non-Boolean seed, the construction remains non-Boolean
when beta>0. The three-bit point defect is an admissible seed; constants,
parities, ignored coordinates, and the pure-selector boundaries are also
admitted. Arbitrary spectators retain their ENTIRE seed entropy and cost.

## Application to the new A032/A079 dependency

Use A079's four-bit a and b=1-a^2 from run20261021T153136Z, and write

    A(u,z)=a(u), B(u,z)=z b(u), F=A+B ell h.

Both a and b are exact ternary rows with disjoint supports and beta=3/8.
If only u is queried among the controller coordinates, A032's
run20261021T215120Z gives U_4=1-(9/16)log2(3), in (1/10,1/8).
That source already paid ALL u-only histories from the original 1/8
structural reserve. Applying (*) now permits arbitrary adaptive queries
of the seed y INTERLEAVED with those u queries, without querying z or ell:

    W_4 = 1-(9/16)log2(3) + (3/8) V_4(h).

This is a conditional extension of the existing source theorem, not a
new certification of its 238145-tree enumeration. The universal theorem
(*) above has a self-contained proof and does not depend on that census.
The factor 3/8 and the one structural reserve never reset. The identity
also shows exactly when 1/8 alone suffices:

    V_4(h) <= (8/3)[1/8 - (1-(9/16)log2(3))].

There is no reason to assume this seed condition. No arbitrary seed
reference reset or general FEI payment has been obtained. If a prescribed
reference Q is supplied, its normalization and conversion cost need their
own transport identity; Shannon cancellation does not certify that step.

## What can fail, and the next unpaid step

The proof uses independence of the physical seed/controller inputs,
disjoint A/B support, normalization of h, beta>=0, exact conservation of
beta, and protection of ell. If ell is queried, its two complete children
are A_s +/- B_s h_t; their empty seed-frequency coefficients can interfere,
so the disjoint-sector argument used in (*) ends at that exact line.
Likewise, a seed-dependent prescribed reference is not covered merely by
the entropy identity. These are substantive exclusions, not bookkeeping.

This exclusion is necessary: with A=(1+c)/2, B=(1-c)/2, the tag query has
Inf_ell=1/2 and Delta_ell H=2 for h=1, but the SAME tag influence and
Delta_ell H=0 for h=y. Both are actual three-bit Boolean functions (one
has an irrelevant y coordinate). Thus tag-query cost depends on the
seed even though protected controller-query cost does not. Direct spectra
and both complete tag children are certified in out/tag_boundary.json.

The next action is to expose ell ONCE at an inherited mixed-history cut,
retain both full spectra A_s +/- B_s h_t, and price the resulting signed
empty-frequency interference from the SAME unused structural/seed owner
and the same incoming reference. The theorem above removes the possibility
that more protected-tag interleaving secretly supplies that payment.
