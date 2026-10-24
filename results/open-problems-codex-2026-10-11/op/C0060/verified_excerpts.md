# Primary-source excerpts

## source: PDF page 81

10.3. NOTES
81
With this choice of u, the right hand sides of both (10.2.8) and (10.2.9) tend to 0 as L0 →∞.
Thus, for large enough L0 and u = u(L0) as in (10.2.10), the inequalities in (10.2.6) are satisﬁed,
and (10.2.3) follows. The proof of Proposition 10.5 is complete.
10.3
Notes
The phase transition of the vacant set Vu is the central topic of the theory of random interlace-
ments. Let us now give a historical overview of the results presented in this section as well as
brief outline of other, related results.
The ﬁniteness of u∗for d ≥3 and the positivity of u∗for d ≥7 were proved in [S10, Theorems
3.5, 4.3], and the latter result was extended to all dimensions d ≥3 in [SidSz09, Theorem 3.4].
In contrast to the percolation phase transition of the vacant set Vu, the graph spanned by
random interlacements Iu at level u is almost surely connected for any u > 0, as we have
already discussed in Section 6.4.
The main result of [T09a] is that for any u < u∗, the inﬁnite component of Vu is almost surely
unique. The proof is a non-trivial adaptation of the Burton-Keane argument, because the law
of Vu does not satisfy the so-called ﬁnite energy property, see [S10, Remark 2.2 (3)].
As alluded to in Section 6.4 already, one can deﬁne random interlacements on more general
transient graphs than Zd, d ≥3, which can lead to interesting open questions on the non-
triviality of u∗. As an example, in the case of random interlacements on the graph G × Z,
where G is the discrete skeleton of the Sierpinski gasket, it is still not known whether the
corresponding parameter u∗is strictly positive; see [S12a] for more details of the construction
of random interlacements on such G × Z, and in particular Remark 5.6 (2) therein.
The ﬁrst version of the deﬁnition of u∗∗appeared in [S09b, (0.6)], and a stretched exponential
upper bound on the connectivity function of Vu for u > u∗∗was ﬁrst proved in [SidSz10, Theorem
0.1]. The deﬁnition of u∗∗has been subsequently weakened multiple times. Our deﬁnition of
u∗∗is a special case of deﬁnition [S12a, (0.10)] and our proof of Proposition 10.3 is a special
case of [S12a, Theorem 4.1], because the results of [S12a] are about random interlacements on a
large class of graphs of form G × Z, while our results are only about the special case G = Zd−1.
Currently, the weakest deﬁnition of u∗∗on Zd is [PT13, (3.6)], and the strongest subcriticality
result is an exponential upper bound (with logarithmic corrections if d = 3) on the connectivity
function of Vu for u > u∗∗, see [PT13, Theorem 3.1].
The question u∗
?= u∗∗is currently still open for random interlacements on Zd, but u∗= u∗∗does
hold (and the value of u∗is explicitly known) if the underlying graph is a regular tree, see [T09b,
Section 5]. The exact value of u∗on Zd is not known and probably there is no simple formula
for it. However, the following high-dimensional asymptotics are calculated in [Sz11a, Sz11b]:
lim
d→∞
u∗(d)
ln(d) = lim
d→∞
u∗∗(d)
ln(d) = 1.
The supercritical phase u < u∗of interlacement percolation has also received some attention. It
is known that for any u < u∗, the inﬁnite connected component of Vu is almost surely unique
(see [T09a]). One might wonder if the inﬁnite component is locally unique in large boxes. In
[T11] (for d ≥5) and in [DRS12a] (for d ≥3) it is proved (among other local uniqueness results)
that for small enough values of u we have
P[0
Vu
←→B(L)c | 0
Vu
̸↔∞] ≤κ · e−L1/κ.


## resolution: PDF page 3

important open question from [57], see the final Remark 5.6(2) therein and our second
main result, Theorem 1.2 below.
We now describe our results more precisely, and refer to Section 2 for the details of
our setup. We consider an infinite, connected, locally finite graph G endowed with a
positive and symmetric weight function λ on the edges. To the data (G, λ), we asso-
ciate a canonical discrete-time random walk, which is the Markov chain with transition
probabilities given by px,y = λx,y/λx, where λx = P
y∈G λx,y. It is characterized by the
generator
(1.2)
Lf(x) = 1
λx
X
y∈G
λx,y(f(y) −f(x)), for x ∈G,
for f : G →R with finite support.
We assume that the transition probabilities of
this walk are uniformly bounded from below, see (p0) in Section 2, and writing g(x, y),
x, y ∈G, for the corresponding Green density, see (2.4) below, that
there exist parameters α and β with 2 ≤β < α
such that, for some distance function d(·, ·) on G,
λ(B(x, L)) ≍Lα and g(x, y) ≍(d(x, y) ∨1)−(α−β), for x, y ∈G,
(1.3)
where ≍means that the quotient is uniformly bounded from above and below by positive
constants, B(x, L) is the closed ball of radius L in the metric d(·, ·) and λ(A) = P
x∈A λx
is the measure of A ⊂G, see (Vα) and (Gβ) in Section 2 for the precise formulation of
(1.3). The exponent β in (1.3) reflects the diffusive (when β = 2) or sub-diffusive (when
β > 2) behavior of the walk on G, cf. Proposition 3.3 below. Note that the condition on
g(·, ·) in (1.3) implies in particular that G is transient for the walk. For more background
on why condition (1.3) is natural, we refer to [24], [25] as well as Remarks 2.2 and 3.4
below regarding its relation to heat kernel estimates. As will further become apparent in
Section 3, see in particular Proposition 3.5 and Corollary 3.9, choosing d to be the graph
distance on G is not necessarily a canonical choice, for instance when G has a product
structure.
Apart from (p0), (Vα) and (Gβ), we will often make one additional geometric assump-
tion (WSI) on G, introduced in Section 2. Roughly speaking, this hypothesis ensures
a (weak) sectional isoperimetry of various large subsets of G, which allows for certain
contour arguments. Rather than explaining this in more detail, we single out the follow-
ing representative examples of graphs, which satisfy all four aforementioned assumptions
(p0), (Vα), (Gβ) and (WSI), cf. Corollary 3.9 below:
G1 = Zd, with d ≥3,
G2 = G′ × Z, with G′ the discrete skeleton of the Sierpinski gasket,
G3 = the standard d-dimensional graphical Sierpinski carpet for d ≥3,
G4 = a Cayley graph of a finitely generated group Γ = ⟨S⟩with S = S−1
having polynomial volume growth of order α > 2
(1.4)
(see e.g. [6], pp.6–7 for definitions of G′ and G3, the latter corresponds to V (d) in the
notation of [6]), all endowed with unit weights and a suitable distance function d (see
Remark 2.1 and Section 3).
The graph G2 is a benchmark case for various aspects
2


## resolution: PDF page 4

of [57], to which we will return in Theorem 1.2 below. The case G3 underlines the fact
that even in the fractal context a product structure is not necessarily required. The case
G4 subsumes G1 of course, which is but a starting point for the current article, and it
contains many interesting examples, for instance the (2n + 1)-dimensional Heisenberg
group H2n+1(Z), for n = 1, 2, . . .
Figure 1: A graph of the form G2 = G′ × Z, with G′ the discrete Sierpinski gasket.
The fact that (WSI) holds in cases G2, G3 and G4 is not evident, and will follow by
expanding on results of [68], see Section 3. In the case of G4, (WSI) crucially relies on
Gromov’s deep structural result [27]. The reader may choose to focus on (1.4), or even
G1, for the purpose of this introduction.
Our first main result deals with the Gaussian free field Φ on the weighted graph
(G, λ). Its canonical law PG is the unique probability measure on RG such that (Φx)x∈G
is a mean zero Gaussian field with covariance function
(1.5)
EG[ΦxΦy] = g(x, y), for any x, y ∈G.
On account of (1.3), Φ exhibits (strong) algebraically decaying correlations with respect
to the distance d, captured by the exponent
(1.6)
ν
def.
= α −β (> 0).
We study the geometry of Φ in terms of its level sets
(1.7)
E≥h def.
= {y ∈G; Φx ≥h}, h ∈R.
The random set E≥h decomposes into connected components, also referred to as clusters:
two points belong to the same cluster of E≥h if they can be joined by a path of edges
whose endpoints all lie inside E≥h. Finite clusters are sometimes called islands.
As h varies, the onset of a supercritical phase in E≥h is characterized by a critical
parameter h∗= h∗(G), which records the emergence of infinite clusters,
(1.8)
h∗
def.
= inf

h ∈R; PG  there exists an infinite cluster in E≥h
= 0
	
(with the convention inf ∅= ∞). The existence of a nontrivial phase transition, i.e.,
the statement −∞< h∗< ∞, was initially investigated in [12], and even in the case
G = G1 = Zd with d ≥3, has only been completely resolved recently in [47]. It was
further shown in Corollary 2 of [12] that h∗≥0 on Zd, and this proof can actually be
adapted to any locally finite transient and connected weighted graph, see the Appendix
of [1], or [33] for a different proof.
3


## resolution: PDF page 7

GN = (Z/NZ)d with tN ≍N d. The finiteness of u∗, i.e. the existence of a subcritical
phase for Vu, and even a phase of stretched exponential decay for the connectivity func-
tion of Vu at large values of u, can be obtained by adapting classical techniques, once
certain decoupling inequalities are available. As a consequence of Theorem 2.4 below, see
Remark 7.2, 1) and Corollary 7.3, such a phase is exhibited for any graph G satisfying
(p0), (Vα) and (Gβ) as in (1.12).
On the contrary, the existence of a supercritical phase is much less clear in general.
It was proved in [57] that u∗> 0 for graphs of the type G = G′ × Z, endowed with some
distance d such that (1.3) holds, see (1.8) and (1.11) in [57] (note that the exponent α
from (1.3) actually corresponds to α + β/2 in [57], see (1.9) therein). However, in this
source the condition ν ≥1 was required, cf. (1.6), excluding for instance the case G = G2
in which ν = log 9−log 5
log 4
< 1, see [30] and [2], as well as the case G = G3 in dimension three
(which was anyway not of the type G′×Z), see Remark 3.10, 1). As a consequence of the
following result, we settle the question about the positivity of u∗affirmatively under our
assumptions. This solves a principal open problem from [57], see Remark 5.6(2) therein,
and implies the existence of a phase transition for the percolation of the vacant set Vu of
random interlacements on such graphs. We remind the reader of the convention (1.12)
regarding conditions (Vα), (Gβ) and (WSI), which is in force in the following:
Theorem 1.2. Suppose G satisfies (p0), (Vα), (Gβ) and (WSI). Then there exists eu > 0
and for every u ∈(0, eu], a probability space (Ωu, Fu, Qu) governing three random subsets
I, V and K of G with the following properties:
i) I, resp. V, have the law of Iu, resp. Vu, under PI.
ii) K is independent of I.
iii) Qu-a.s., I ∩K contains an infinite cluster, and (I ∩K) ⊂V.
(1.17)
A fortiori, u∗≥eu(> 0).
Thus, our construction of an infinite cluster of Vu for small u > 0, and hence our
resolution of the conjecture in [57], proceeds by stochastically embedding a large part
of its complement, Iu ∩K inside Vu. The law of the set K can be given explicitly, see
Remark 9.4, 2), and K could also be chosen independent of V instead of I, see Remark
9.4, 3).
Let us now elaborate shortly on the important case G = G′ × Z considered in [57].
In this setting, the conclusions of Theorem 1.2 hold under the mere assumptions that
(p0) holds and G′ satisfies the upper and lower heat kernel estimates (UHK(α, β)) and
(LHK(α, β)), see Remark 2.2, with respect to d = dG′, the graph distance on G′, for
some α > 1 and β ∈[2, 1 + α); for instance, if G = G2 from (1.4), then α = log 3
log 2 and
β = log 5
log 2, see [7, 30]. This (and more) will follow from Propositions 3.5 and 3.7 below;
see also Remark 3.10 for further examples. Incidentally, let us note that Theorem 1.2 is
also expected to provide further insights into the disconnection of cylinders GN × Z by a
simple random walk trace, for GN a large finite graph, for instance when GN is a ball of
radius N in the discrete skeleton of the Sierpinski gasket (corresponding to G2 of (1.4)),
cf. Remark 5.1 in [52].
Theorem 1.2 is true on more general product graphs G = G′ × G′′, see Section 3,
but in fact also on graphs which are not product graphs, such as the graphs G3 and G4
from (1.4). Our proof still requires certain useful geometric features which are trivially
6


## resolution: PDF page 28

In particular, if G is either a product of infinite graphs G1 × G2 or the d-dimensional
Sierpinski carpet, d ⩾3, taking Oe such that Oe \ {e} only contains two connected
edges of E for each e ∈E+ \ E, we get that the external boundary of every finite and
∗-connected subset A of G is ∗-connected since G++ = G+.
2) Proposition 3.7 provides us with a stronger result than Lemma 2 in [68] even when
G = Zd, d ⩾3. Indeed, Zd = Zd−1 × Z and thus the external boundary of every
finite and connected (or even ∗-connected) subset of Zd is ∗-connected in the sense of
product graphs previously defined, i.e., it is connected in Zd∪{{(x, n), (y, n+1)}; n ∈
Z, x ∼y ∈Zd−1}.
3) An example of a graph G for which we cannot apply Proposition 3.7, and in fact
where we can find a finite and connected set whose boundary is not ∗-connected, and
where (WSI) does not hold, but where (Gβ) and (Vα) hold, is the Menger sponge. It is
defined as the graph associated to the following generalized 3-dimensional Sierpinski
carpet, see Section 2 of [6]: split [0, 1]3 into 27 cubes of size length 1/3, remove the
central cube of each face as well as the central cube of [0, 1]3, and iterate this process
for each remaining cube. It is easy to show that G endowed with the graph distance
verifies (Vα) with α =
log(20)
log(3) , and (Gβ) follows from Theorem 5.3 in [6] since the
random walk on the Menger sponge is transient, see p.741 of [5]. One can then easily
check that taking An = (3n/2, 5 × 3n/2)3 ∩G, where we see G as a subset of R3, then
∂extA is not ∗-connected. In fact for each p < n, there exists x ∈∂extAn such that
there is no 3p-path between x and B(x, 2 × 3p)c, and thus (WSI) does not hold.
We can now conclude that our main results apply to the examples mentioned in the
introduction.
Corollary 3.9. The graphs in (1.4) (endowed with unit weights) satisfy (p0), (Vα), (Gβ),
for some α > 2, β ∈[2, α) and (WSI), with respect to a suitable distance function d(·, ·).
In particular, the conclusions of Theorems 1.1 and 1.2 hold for these graphs.
Proof. Condition (p0) holds plainly in all cases since all graphs in (1.4) have unit weights
and uniformly bounded degree. For G1, we classically have α = d, β = 2 and (WSI)
follows e.g. from Proposition 3.7 with d = dG (or even the ℓ∞-norm) since Zd = Zd−1×Z.
The case of G2 is an application of Propositions 3.5 and 3.7: it is known [7, 30] that G′,
the discrete skeleton of the Sierpinski gasket, satisfies (Vα2) and (Gβ2) with α2 = log 3
log 2 and
β2 = log 5
log 2, whence (Vα), (Gβ), hold for G2 with respect to d in (3.22), for α = log 45
2 log 2 and
β = log 5
log 2 as given by (3.22) with α1 = 1, β1 = 2 (note that α2 > 1 so (3.21) holds), and
it is easy to see that any ∗-connected path is also a 1-path for d in (3.22), hence (WSI)
holds. Regarding G3, the standard d dimensional graphical Sierpinski carpet endowed
with the graph distance, with d ≥3 (cf. p.6 of [6]), α = log(3d −1)/ log(3) (with d = dG)
and (Gβ) then follows from Theorem 5.3 in [6] since the random walk on G3 is transient
for d ≥3, see p.741 of [5]. We refer to Remark 3.10, 1) below for bounds on the value of
β. Moreover, (WSI) on G3 follows from Proposition 3.7 since any ∗-connected path in
G3 is also a 2-path.
Finally, G4 endowed with the graph distance d = dG4 satisfies (Vα) for some α > 2
by assumption and (Gβ) holds with β = 2 by Theorem 5.1 in [29]. To see that (WSI)
holds, we first observe that the group Γ = ⟨S⟩which has G4 as a Cayley graph is
27
