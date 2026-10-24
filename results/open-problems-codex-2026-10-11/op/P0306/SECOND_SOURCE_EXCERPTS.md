# Continuation source excerpts (not a solution theorem)

## second_lead_1102.4177.txt, PDF page 8

```text
2
DISCRETE AND CONTINUOUS CACTUSES
8
where the supremum is over all choices of the subdivision 0 = t0 < t1 < · · · < tk = T of [0, T].
Obviously L(γ) ≥d(γ(0), γ(T)).
We say that (E, d) is a geodesic space if for every a, b ∈E there exists a continuous curve
γ : [0, d(a, b)] −→E such that γ(0) = a, γ(d(a, b)) = b and d(γ(s), γ(t)) = t −s for every
0 ≤s ≤t ≤d(a, b). Such a curve γ is then called a geodesic from a to b in E. Obviously,
L(γ) = d(a, b). A pointed geodesic metric space is a geodesic space with a distinguished point
ρ.
Let E = (E, d, ρ) be a pointed geodesic compact metric space. We deﬁne the (continuous)
cactus associated with (E, d, ρ) in a way very similar to what we did in the discrete setting. We
ﬁrst deﬁne for every a, b ∈E,
dE
Kac(a, b) = d(ρ, a) + d(ρ, b) −2 sup
γ:a→b

min
0≤t≤1 d(ρ, γ(t))

,
where the supremum is over all continuous curves γ : [0, 1] −→E such that γ(0) = a and
γ(1) = b.
The next proposition is then analogous to Proposition 2.1.
Proposition 2.4. The mapping (a, b) −→dE
Kac(a, b) is a pseudo-distance on E. Furthermore,
for every a, b ∈E,
dE
Kac(a, b) ≤d(a, b)
and
dE
Kac(ρ, a) = d(ρ, a).
The proof is exactly similar to that of Proposition 2.1, and we leave the details to the reader.
Note that in the proof of the bound dE
Kac(a, b) ≤d(a, b) we use the existence of a geodesic from
a to b.
If a, b ∈E, we put a
E≍b if dE
Kac(a, b) = 0. We deﬁne the cactus of (E, d, ρ) as the quotient
space Kac(E) := E /
E≍, which is equipped with the quotient distance dE
Kac. Then Kac(E) is a
compact metric space, which is pointed at the equivalence class of ρ.
Remark 2.5. It is natural to ask whether the supremum in the deﬁnition of dE
Kac(a, b) is
achieved, or equivalently whether there is a continuous path γ from a to b such that
dE
Kac(a, b) = d(ρ, a) + d(ρ, b) −2 min
0≤t≤1 d(ρ, γ(t)).
We will return to this question later.
2.3
Continuity properties of the cactus
Let us start by recalling the deﬁnition of the Gromov-Hausdorﬀdistance between two pointed
compact metric spaces (see [12] and [7, Section 7.4] for more details).
Recall that if A and B are two compact subsets of a metric space (E, d), the Hausdorﬀ
distance between A and B is
dE
H(A, B) := inf{ε > 0 : A ⊂Bε and B ⊂Aε},
where Xε := {x ∈E : d(x, X) ≤ε} denotes the ε-neighborhood of a subset X of E.


```

## second_lead_2006.11050.txt, PDF page 4

```text
We denote the set of all snake trajectories by S.
If ω ∈S, we often write Ws(ω) = ωs and
ζs(ω) = ζ(ωs) for every s ≥0. The set S is equipped with the distance
dS(ω, ω′) = |σ(ω) −σ(ω′)| + sup
s≥0
dW(Ws(ω), Ws(ω′)).
It is not hard to verify that a snake trajectory ω is completely determined by the knowledge of the
lifetime function s 7→ζs(ω) and of the tip function s 7→c
Ws(ω) (see [2, Proposition 8]).
Let ω ∈S be a snake trajectory. The lifetime function s 7→ζs(ω) codes a compact R-tree, which
will be denoted by T(ω). This R-tree is the quotient space T(ω) := [0, σ(ω)]/∼of the interval [0, σ(ω)]
for the equivalence relation
s ∼s′ if and only if ζs(ω) = ζs′(ω) =
min
s∧s′≤r≤s∨s′ ζr(ω),
and T(ω) is equipped with the distance induced by
d(ω)(s, s′) = ζs(ω) + ζs′(ω) −2
min
s∧s′≤r≤s∨s′ ζr(ω).
(see e.g. [18, Section 3] for more information about the coding of R-trees by continuous functions). We
write p(ω) : [0, σ(ω)] −→T(ω) for the canonical projection. By convention, T(ω) is rooted at the point
ρ(ω) := p(ω)(0), and the volume measure on T(ω) is deﬁned as the pushforward of Lebesgue measure
on [0, σ(ω)] under p(ω).
By property (ii) in the deﬁnition of a snake trajectory, the condition p(ω)(s) = p(ω)(s′) implies that
Ws(ω) = Ws′(ω). So the mapping s 7→Ws(ω) can be viewed as deﬁned on the quotient space T(ω).
For u ∈T(ω), we set ℓu(ω) := c
Ws(ω), for any s ∈[0, σ(ω)] such that u = p(ω)(s). We interpret ℓu(ω)
as a “label” assigned to the “vertex” u of T(ω). Notice that the mapping u 7→ℓu(ω) is continuous on
T(ω). We set W∗(ω) := min{ℓu(ω) : u ∈T(ω)} and W ∗(ω) := max{ℓu(ω) : u ∈T(ω)}, for ω ∈S.
We now introduce a σ-ﬁnite measure on S that plays an important role in the present work.
Deﬁnition 2. The Brownian snake excursion measure N0 is the σ-ﬁnite measure on S that is char-
acterized by the following two properties:
(i) The distribution of the lifetime function (ζs)s≥0 under N0 is the Itô measure of positive excursions
of linear Brownian motion, normalized so that, for every ε > 0,
N0

sup
s≥0
ζs > ε

= 1
2ε.
(ii) Under N0 and conditionally on (ζs)s≥0, the tip function (c
Ws)s≥0 is a centered Gaussian process
with covariance function
K(s, s′) :=
min
s∧s′≤r≤s∨s′ ζr.
Informally, property (ii) says that, under N0 and conditionally on (ζs)s≥0, the labels (ℓu)u∈T(ω) are
distributed as Brownian motion indexed by T(ω). The measure N0 can be interpreted as the excursion
measure away from 0 for the Markov process in W called the Brownian snake (we refer to [16] for
a detailed study of the Brownian snake and its excursion measures). For our purposes, it will be
important to know the distribution of the minimum W∗under N0: For every y < 0, we have
N0(W∗≤y) =
3
2y2 .
(2)
See e.g. [16, Section VI.1] for a proof.
The following scaling property is often useful. For λ > 0, for every ω ∈S, we deﬁne Θλ(ω) ∈S by
Θλ(ω) := ω′, with
ω′
s(t) :=
√
λ ωs/λ2(t/λ) ,
for s ≥0 and 0 ≤t ≤ζ′
s := λζs/λ2.
4


```

## second_lead_2006.11050.txt, PDF page 23

```text
Proof. Let F be a bounded continuous function on M•, and assume that 0 ≤F ≤1. Then,
E[F(D•) | D(v∗, ∂D•) ≤ε] = E[F(D•) 1{D(v∗,∂D•)≤ε}]
P(D(v∗, ∂D•) ≤ε)
,
(44)
and we know from (31) that
lim
ε→0 ε−2 P(D(v∗, ∂D•) ≤ε) = 1.
On the other hand, (42) gives
E
h
F(D•) 1{D(v∗,∂D•)≤ε}
i
= E
h Z
D
Vol(dx) F([D, x]) 1{D(x,∂D)≤ε}
i
.
(45)
From Theorem 9 (and the continuity of the mapping x 7→[D, x]), we have
ε−2
Z
D
Vol(dx) F([D, x]) 1{D(x,∂D)≤ε}
a.s.
−→
ε→0
Z
µ(dy) F([D, y]).
The desired convergence of E[F(D•)|D(v∗, ∂D•) ≤ε] to E[
R µ(dy)F([D, y])] will follow from (44) and
(45) if we can prove that the convergence in the last display also holds for expected values. Arguing
along a sequence of values of ε tending to 0, Fatou’s lemma gives
lim inf
ε→0 ε−2E
h Z
D
Vol(dx) F([D, x]) 1{D(x,∂D•)≤ε}
i
≥E
h Z
µ(dy) F([D, y])
i
.
(46)
By the case F = 1 of (45), we have
ε−2E
h Z
D
Vol(dx) 1{D(x,∂D)≤ε}
i
= ε−2P(D(v∗, ∂D•) ≤ε) −→
ε→0 1.
Replacing F by 1 −F in (46), we get the corresponding upper bound for the limsup, and we conclude
that we have
lim
ε→0 ε−2E
h Z
D
Vol(dx) F([D, x]) 1{D(x,∂D•)≤ε}
i
= E
h Z
µ(dy) F([D, y])
i
.
This completes the proof.
We will now combine Proposition 4 and Proposition 14 to get our construction of the free Brownian
disk with perimeter 1 pointed at a uniform boundary point. We start from a pair (b, N ′), where b =
(bt)0≤t≤1 is a ﬁve-dimensional Bessel bridge from 0 to 0 over the time interval [0, 1] and, conditionally
on b, N ′(dtdω) is a Poisson measure on [0, 1] × S with intensity
2 1{W∗(ω)≥−
√
3 bt} dt N0(dω).
We write
N ′ =
X
j∈J
δ(t′
j,ω′
j),
and Σ′ := P
j∈J σ(ω′
j). From N ′, we can deﬁne a compact measure metric space H′, and the associated
cyclic exploration (E′
s)s∈[0,Σ′], in exactly the same way as H and (Es)s∈[0,Σ] were deﬁned from N at the
beginning of Section 4. Intervals in H′ are deﬁned as previously from the exploration (E′
s)s∈[0,Σ′], and
we now specify labels (Λ′
u)u∈H′ by setting Λ′
t :=
√
3 bt for t ∈[0, 1], and for u ∈T(ω′
j), j ∈J,
Λ′
u :=
√
3 bt′
j + ℓu(ω′
j).
A fundamental diﬀerence is now that Λ′
u ≥0 for every u ∈H′ (because by construction W∗(ω′
j) ≥
−
√
3 bt′
j for every j ∈J). Furthermore 0 is the unique element of H′ with zero label.
We use the analogs of (28) and (29), with Λu replaced by Λ′
u, to deﬁne D′◦(u, v) and D′(u, v) for
u, v ∈H′. Then D′(u, v) is a pseudo-metric on H′. Furthermore, it is immediate that D′(0, u) = Λ′
u
for every u ∈H′, and that the bound |Λ′
u −Λ′
v| ≤D′(u, v) holds for every u, v.
23


```

## second_lead_2006.11050.txt, PDF page 24

```text
Theorem 15. The quotient space D′ := H′/{D′ = 0} equipped with the metric induced by D′, with
the volume measure which is the pushforward of the volume measure on H′, and with the distinguished
point which is the equivalence class of 0, is a free Brownian disk with perimeter 1 pointed at a uniform
boundary point.
We write Π′ for the canonical projection from H′ onto D′. As previously, we can deﬁne the label
Λ′
x of x ∈D′ by setting Λ′
x := Λ′
u, for any u ∈H′ such that Π′(u) = x. In a way similar to the formula
D(v∗, u) = Λu −Λ∗for the free pointed Brownian disk, labels Λ′
x exactly correspond to distances from
the distinguished point 0 lying on the boundary.
Proof. Thanks to Proposition 14, it is enough to verify that the (pointed measure metric) space D•
conditioned on the event {D(v∗, ∂D•) ≤ε} converges in distribution to D′ as ε →0, in the sense of the
pointed Gromov-Hausdorﬀ-Prokhorov topology. For the sake of simplicity, we will content ourselves
with proving the pointed Gromov-Hausdorﬀconvergence (a few additional technicalities, using Lemma
4 in [19], yield the stronger Gromov-Hausdorﬀ-Prokhorov convergence).
Let N be as previously a Poisson point measure on [0, 1] × S with intensity 2 dt N0(dω). Let us ﬁx
η > 0 and α > 0. We ﬁrst choose δ ∈(0, 1/2) small enough so that
P

sup
t∈[0,δ]∪[1−δ,1]
√
3 bt < α

> 1 −η,
(47)
and
P

W ∗(ω) ≤α for every atom (t, ω) of N such that t ∈[0, δ] ∪[1 −δ, 1]

≥1 −η.
(48)
For every ε > 0, let eε be distributed as in Proposition 4. Thanks to (47) and to the convergence in
distribution in the latter proposition, we can ﬁnd ε0 > 0 such that, for every ε ∈(0, ε0], we have also
P

sup
t∈[0,δ]∪[1−δ,1]
√
3 eε
t < α

> 1 −η.
(49)
Furthermore, we can also ﬁx ε1 ∈(0, ε0) such that, for every ε ∈(0, ε1], the total variation distance
between the distribution of (eε
t + ε)δ≤t≤1−δ and the distribution of (bt)δ≤t≤1−δ is smaller than η.
Let us ﬁx ε ∈(0, ε1 ∧(α/
√
3)]. On a suitable probability space, we can construct both b and eε
so that
P

ε + eε
t = bt for every t ∈[δ, 1 −δ]

> 1 −η.
(50)
We may also assume that the Poisson point measure N is deﬁned on the same probability space, and
is independent of the pair (b, eε). We then deﬁne two other random point measures N ′ and Nε by
N ′(dtdω) := 1{W∗(ω)≥−
√
3 bt} N(dtdω)
and
Nε(dtdω) := 1{W∗(ω)≥−
√
3(ε+eε
t )} N(dtdω).
Note that the pair (b, N ′) has the same distribution as described before the statement of the theorem,
and so we may assume that the pointed metric space D′ is constructed from this pair as explained
above.
Similarly, we claim that the pair (eε, Nε) has the conditional distribution of the pair (e, N) intro-
duced in Section 4 to construct the free pointed Brownian disk, given the event {Λ∗≥−ε
√
3}. Let us
brieﬂy explain this. Noting that {Λ∗≥−ε
√
3} = {W∗(ω) ≥−
√
3(et + ε) for every atom (t, ω) of N},
we get, using (2),
P(Λ∗≥−ε
√
3 | e) = exp

−
Z 1
0
dt
(ε + et)2

.
Then, conditionally on e, the law of N given the event {Λ∗≥ε
√
3} is the law P(ε,e) of a Poisson
point measure with intensity 2 1{W∗(ω)≥−
√
3(et+ε)} dt N0(dω). Hence, for any nonnegative measurable
function G on Mp([0, 1] × S),
E[G(N) 1{Λ∗≥−ε
√
3} | e ]
P(Λ∗≥−ε
√
3 | e)
=
Z
P(ε,e)(dγ) G(γ).
24


```
