# Spectral-center FEI for every parallel slab and its arbitrary character modulations

2 October 2026. Complete proposed analytic derivation; independent audit
requested. No external review or historical novelty claim is made. This
builds beyond the completed [parallel-slab proof](../2026-10-02-parallel-slabs/stripe_extension_parallel_slabs_proof.md).
It does not use a false comparison between I−Var and the spectral-center
budget. The strengthened [slab deficit proof](../2026-10-02-slab-deficit-composition/universal_split_deficit_and_slab_composition_proof.md)
was inspected, but the argument below only requires ordinary FEI on the
restrictions of a slab.

On the uniform cube define H(f) as full Fourier entropy with base-2
logarithms, a_i(f)=I_i(f) as physical flip probability, and

J(f)=Σ_i min(a_i(f),1−a_i(f)).

For χ_T=Π_{i∈T}x_i, the exact character shift gives H(χ_Tf)=H(f) and
I(χ_Tf)=Σ_{i outside T}a_i+Σ_{i inside T}(1−a_i). Consequently J(f)
is the minimum influence over the entire character orbit. It is realized
by T={i:a_i>1/2}; equality influences may be left unflipped.

**Proposed theorem.** Every Boolean parallel-slab gate g, with arbitrary
real weights and endpoint conventions, satisfies

H(g)≤(C_slab+60)J(g),

where C_slab is the universal constant in the completed ordinary slab
theorem. Therefore every χ_Tg satisfies ordinary FEI with the same
constant C_slab+60, for arbitrary T, including overlapping coordinates
and |T| growing with dimension.

The proof has two independent elementary ingredients: a generic
bounded-coordinate gluing estimate, and a bound of 15 on the number of
slab influences strictly larger than one half.

## 1. Universal entropy gluing over a bounded set of coordinates

For any Boolean f split on input i, write f=A+x_iB. For a coefficient
pair a=Ahat(S), b=Bhat(S), P=a²+b²>0, put q=b²/P and
r=(a+b)²/(2P). Its full spectral entropy is −P log₂P+P h₂(q).
The average of the two restricted coefficient entropies is
−P log₂(2P)+P h₂(r), since the restricted coefficients are a+b,a−b.
Consequently the exact pair formula is

Δ_iH(f)=Σ_S P_S[1+h₂(q_S)−h₂(r_S)].

The elementary inequality h₂(t)≥4t(1−t), together with
r(1−r)=(1−2q)²/4, gives 1−h₂(r)≤4q(1−q)≤h₂(q).
For a complete verification of the binary inequality, expand
1−h₂((1+x)/2)=(1/ln 2)Σ_{j≥1}x^(2j)/[(2j)(2j−1)].
Its coefficients are positive and sum to one; on |x|≤1 the series
is at most x². This proves the asserted inequality, with endpoints
following by continuity. Thus the pair formula gives

Δ_i H(f)≤2Σ_S P_S h₂(q_S),

where P_S=Ahat(S)²+Bhat(S)², q_S=Bhat(S)²/P_S, and f=A+x_iB.
P is a probability law and Σ_S P_Sq_S=EB²=a_i(f). Concavity of binary
entropy therefore gives the universal bound

Δ_i H(f)≤2h₂(a_i(f)).

We claim that, for every Boolean f and every coordinate,

h₂(a_i(f))≤2I(f).                                           (G1)

Here is a proof, including the rare-output case. Let p≤1/2 be the minority
output density. A pivotal edge has one minority endpoint, so a_i≤2p.
The standard uniform-cube edge isoperimetric inequality is

I(f)≥2p log₂(1/p).

It follows directly from |∂E|≥|E|log₂(2^n/|E|) for the minority set E,
using I(f)=2^(1−n)|∂E|. This is established edge isoperimetry, not a new
assumption about biased inputs. Here is its complete elementary induction
to make the input explicit. Split E into two (n−1)-cube sections E_0,E_1
with sizes a_0,a_1 and total a. The internal edge boundaries satisfy the
induction hypothesis, and the cross boundary is |E_0 symmetric-difference
E_1|≥|a_0−a_1|. With q=min(a_0,a_1)/a≤1/2, their sum is at least

a log₂(2^(n−1)/a)+a h₂(q)+a(1−2q)
≥a log₂(2^n/a),

because concavity of h₂ between 0 and 1/2 gives h₂(q)≥2q. The empty
set uses the zero-log convention, and the 0-dimensional base consists
of an empty or full singleton cube, both with boundary zero. This proves
the asserted edge bound for every set and dimension.

If 0<p≤1/4, then a_i≤2p≤1/2, so monotonicity of h₂ on [0,1/2] and
−(1−u)ln(1−u)≤u give

h₂(a_i)≤h₂(2p)
≤2p[log₂(1/(2p))+log₂ e]
≤2p[log₂(1/p)+log₂ e].

Since log₂(1/p)≥2>log₂ e, this is at most
4p log₂(1/p)≤2I(f). If 1/4≤p≤1/2, concavity of p log₂(1/p) shows
2p log₂(1/p)≥1 on this interval. Thus h₂(a_i)≤1≤I(f).
Constants have a_i=H=0 and are handled directly. This proves (G1) and
therefore

Δ_i H(f)≤4I(f).                                             (G2)

Let U be any fixed set of b coordinates. Restrict them successively,
averaging uniformly over the choices at each stage. The exact influence
decomposition gives

E I(f restricted at depth t)≤I(f)

for every depth: the mean influence after splitting equals the previous
influence minus the pivot influence. Telescoping entropy with (G2) yields

H(f)≤E_{assignments to U} H(f|U)+4b I(f).                    (G3)

If all terminal restrictions satisfy ordinary FEI with constant C, then
E H(f|U)≤C E I(f|U)≤C I(f). Hence

H(f)≤(C+4b)I(f).                                           (G4)

This is a generic bounded-coordinate gluing principle. It does not give
unrestricted FEI with a uniform constant if b grows with dimension.

## 2. There are at most 15 high-influence coordinates in a slab

First remove zero weights and flip input signs to make all weights
positive; these transformations preserve every influence. Endpoint ties
can be represented by moving the two endpoints into finite attained-score
gaps, as in the completed slab proof. Empty, full and singleton-score
intervals are handled by the same representation; infinite endpoints
give one crossing.

A two-crossing slab changes on an input edge only if at least one of its
two crossing halfspaces changes. Let h_1,h_2 be those monotone sign-valued
halfspaces. Coordinatewise,

a_i(g)≤a_i(h_1)+a_i(h_2).

For a monotone Boolean halfspace, the standard Chow identity is
hhat_r({i})=a_i(h_r). Parseval then gives

Σ_i a_i(h_r)²≤Var(h_r)≤1.

Thus, without requiring influence additivity between crossings,

Σ_i a_i(g)²
≤2Σ_i[a_i(h_1)²+a_i(h_2)²]≤4.                              (S1)

Any coordinate with a_i(g)>1/2 contributes strictly more than 1/4 to
this sum. Therefore their number b is strictly less than 16, hence
b≤15. A one-crossing gate has the stronger one-halfspace bound; a
constant has no high influences. These cases are included in b≤15.

No claim that a slab is unate is made. For example, the four-variable
middle-layer gate has all four influences 3/4. Inequality (S1) permits
that example and is compatible with cancellations between its crossings.

## 3. Apply gluing to the minimizing character

Let U={i:a_i(g)>1/2}, b=|U|≤15, and define h=χ_Ug. Then

H(h)=H(g), I(h)=J(g).

After assigning all U coordinates, χ_U is just a constant output sign.
The restricted g is still one interval indicator in the remaining weighted
linear form. Thus each terminal restriction of h is a slab or its
complement, and satisfies ordinary FEI with C_slab. The generic gluing
bound (G4) gives

H(g)=H(h)≤(C_slab+4b)I(h)≤(C_slab+60)J(g).

For any other character T, I(χ_Tg)≥J(g) and entropy is unchanged, which
proves the arbitrary-character corollary. This handles J=0 without a
division: the centering character makes h constant by Poincaré, and
therefore H(g)=0. The gluing proof itself also covers it directly.

## 4. Generic restriction-class closure and finite-crossing version

More generally, let a restriction-closed Boolean class have ordinary FEI
constant C, and suppose each member has at most b coordinates with
influence greater than 1/2, uniformly in dimension. The same centering
character and b-coordinate gluing prove H(g)≤(C+4b)J(g). Its arbitrary
character orbit therefore satisfies ordinary FEI with C+4b. Only the
base class must be restriction closed: after all center coordinates are
assigned, the restricted centered function is an output sign of a base
restriction. No assumption that character-modulated intermediate nodes
belong to that base class is made or needed.

This conditional closure is broader than the slab application. The
previously completed parity-LTF theorem has a sharper same-constant
argument using the strong deficit budget and is not claimed as a new
achievement here.

If g has at most m actual sign crossings in one linear form, with no
additional isolated point anomalies, the same union bound gives
a_i(g)≤Σ_{r=1}^m a_i(h_r). By Cauchy–Schwarz and Chow/Parseval,

Σ_i a_i(g)²≤mΣ_r Σ_i a_i(h_r)²≤m².

Thus b=|{i:a_i(g)>1/2}|<4m², so b≤4m²−1 for m≥1. If a
restriction-closed class of these gates has ordinary FEI constant C_m,
the identical gluing argument gives

H(g)≤[C_m+4(4m²−1)]J(g).

In particular the completed strictly separated m-crossing class has
this property. No new FEI theorem is inferred for arbitrary nearby
m-crossing functions: their ordinary FEI input is still unproved.

There is a further already proved class to which this applies, not limited
to strict separation of every crossing. Let the negative set be the union
of at most r ordered parallel intervals/rays, with each gap between
successive components strictly wider than twice the largest input weight.
Each component's width may be arbitrarily narrow. The completed
[disjoint-union proof](../2026-10-02-parallel-slabs/stripe_extension_union_proof.md) supplies ordinary
FEI with constant C_union=r C_slab+log₂(e)(1+1/e). Restriction translates
the same intervals/rays and only decreases the largest remaining weight,
so the wide-gap hypothesis persists. Out-of-range components may disappear.

There are at most 2r endpoint crossings. The previous Chow-square bound
therefore gives at most 16r²−1 influences greater than 1/2. Character
closure gives

H(g)≤[C_union+4(16r²−1)]J(g),

and ordinary FEI with that same constant for every character modulation.
The same conclusion holds when the positive set instead admits this
wide-gap description, by output complementation. This corollary requires
wide *separating gaps* for one chosen label; it places no lower bound on
component interval widths. It therefore goes beyond the strict-separated
crossing class, but does not cover an arbitrary nearby-crossing function
whose neither label admits the stated wide-gap decomposition. Empty or
full negative sets give constants and need no r≥1 argument.

## 5. Failures and limits kept explicit

The previous I−Var budget does not compare to J for slabs. The two-bit
parity is a parallel slab: its negative set is the middle layer. It has
I−Var=1 and J=0. Thus no finite factor can compare those two budgets
on the entire slab class. Its entropy is zero, so it does not contradict
the spectral-center result.

Nor does (G2) assert Δ_iH≤C a_i or Δ_iH≤C min(a_i,1−a_i). It charges
the local increment to the *total* influence of that particular function.
Only the bounded number of peeled coordinates keeps the final constant
dimension independent. A full [local-minimum obstruction](parity_slab_local_minimum_obstruction.md)
shows that the latter local bound fails even for slabs: multiplying the
previous three-crossing rare-point/majority obstruction by its pivot gives
a two-crossing slab with influence 1−2^(−N) and the same entropy increment.
Its increment divided by min(I_i,1−I_i) diverges. This is not an
assumption or a gap in the positive global proof.

No arbitrary shared-input slab circuit, arbitrary polynomial threshold
function, full Boolean FEI, or nonuniform product-input theorem is proved.
Standard edge isoperimetry, character shifts, Chow identity and Parseval
are prior facts. The new derived argument here combines them with the
completed slab theorem and the bounded-coordinate gluing estimate.
Research priority and outside specialist review remain unverified.
