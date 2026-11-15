# Literature and attribution check

Checked 10 November 2026 through primary papers below. The mathematical claims
proved in PROOFS.md stand on their arguments; this check does not establish that
any local inequality is new. No novelty claim is made for bounded-width or
read-once FEI, the hidden maximum-influence counterexample, or the old PM tower.

1. O'Donnell, Wright and Zhou, *The Fourier Entropy--Influence Conjecture for
certain classes of Boolean functions*, 2011,
[author PDF](https://www.cs.cmu.edu/~jswright/papers/fei.pdf), Theorems 1--3 and
Introduction. They prove Shannon FEI for symmetric functions, with constant
12.04, for d-part-symmetric functions with constant 12.04+log2 d, and for
read-once decision trees with constant 4.88. They explicitly explain that
KKL plus fhat({i})=Inf_i gives monotone Fourier min-entropy/influence.
These results do not establish all monotone FEI. Coordinate transitivity is
much weaker than full permutation symmetry; graph properties and the PM tower
are not covered by the symmetric-functions theorem just because all their
coordinates are equivalent.

2. Chakraborty, Kulkarni, Lokam and Saurabh, *Upper bounds on Fourier entropy*,
Theoretical Computer Science 654 (2016),
[revised author report](https://eccc.weizmann.ac.il/report/2013/052/revision/2/download/),
Section 5, Theorems 5.8 and 5.11. They prove FEI for read-once formulas over
AND, OR, XOR and NOT. Theorem 5.11 implies H<=10 I, since its bias correction
kappa(p) is nonpositive. Their proof uses a 0/1 entropy potential and disjoint
composition. This is established Shannon FEI for read-once formulas, not a
new class to claim here. Their O(sqrt n) entropy bound for LTFs should not be
read as a universal H/I bound for every LTF: not every LTF has influence
Theta(sqrt n).

3. O'Donnell and Tan, *A composition theorem for the Fourier Entropy--Influence
conjecture*, 2013,
[paper](https://arxiv.org/html/1304.1347), Theorem 1 and Corollary 4.2.
Their strengthened biased inequality composes. In particular they establish
FEI for read-once formulas over arbitrary gates of bounded arity. Biased
Fourier analysis of the outer gate is essential when the inner functions
are biased. Their theorem supports the known class result; the precise
one-coordinate recurrence used here is rederived in PROOFS.md and audited
against full truth tables, rather than inferred from a general FEI theorem.

4. Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes*,
[arXiv:1806.03646v2](https://arxiv.org/html/1806.03646v2), Introduction and
Theorems 3--9. The paper explicitly says that FEI for monotone functions is
open and distinguishes it from monotone FMEI, which follows from KKL.
It treats exponentially low influence, entropy linear in dimension, bounded
spectral norm, improved read-k decision trees, and regular read-k DNF
min-entropy. Its exponentially low-influence regime is very different from
I<=K sqrt(log n). It does not give the good-coordinate bound sought here.

5. Kelman, Kindler, Lifshitz, Minzer and Safra, *Towards a Proof of the
Fourier--Entropy Conjecture?*,
[arXiv:1911.10579v2](https://arxiv.org/html/1911.10579), Theorems 1.1--1.3.
Their Shannon estimate has the extra spectral-degree logarithm,
H<=O(I+sum_S |S| log(|S|+1) mu(S)). Their concentration result and improved
sharp-threshold bounds do not remove this factor for arbitrary monotone
functions. In their 0/1 notation the normalized influence is I/Var;
normalizations must be tracked before using their min-entropy statement.
Nothing in these theorems proves a constant upper bound on min_i E_i/Inf_i.

6. Arunachalam, Chakraborty, Koucky, Saurabh and de Wolf, *Improved bounds on
Fourier entropy and Min-entropy*,
[arXiv:1809.09819v2](https://arxiv.org/html/1809.09819), Introduction and
Theorems 1.6, 1.8 and 1.9. They prove H<=2 aUC^xor, and min-entropy bounds
from approximate spectral norm and minimum parity-certificate complexity.
For read-k DNFs their min-entropy factor is O(log k). Their introduction
attributes monotone FMEI to KKL and the singleton identity. The result is
about the largest squared Fourier coefficient; it does not control Shannon
entropy, erasure entropy, or the best-coordinate ratio. The paper does not
claim all unate Shannon FEI.

7. The search also surfaced a paper submitted 4 November 2026:
Paraashar and Saurabh, *Fourier Entropy Bounds via Approximations*,
[arXiv:2611.06451](https://arxiv.org/html/2611.06451), abstract and Sections
1.1--1.3. It states approximation spectral-norm and one-sided decomposition
bounds for Shannon entropy. Its hypotheses are description/approximation
costs, rather than a universal bound by influence. The checked sections do
not settle all monotone FEI or Question M. This is an additional current
literature check, not a validation of every proof in that preprint.

Unate and monotone classes have the same Fourier entropy, influences, and
one-coordinate erasure ratios after complementing suitable input coordinates:
that operation multiplies Fourier coefficients by signs. Thus an all-unate
Shannon FEI theorem would also solve the monotone case. Monotone/unate
min-entropy being easy does not mean Shannon FEI is known.

8. Gonzalez, MacManus and Pereyra, *Further evidence towards the Fourier
Entropy--Influence conjecture*,
[arXiv:2606.00246](https://arxiv.org/html/2606.00246), Introduction,
Theorems 5.3, 6.3 and 6.8. They treat delta-tribes, semi-separated functions,
and monotone functions with the tribe separation property through stopping
decision trees. These are proper structural classes. Their introduction
explicitly leaves arbitrary monotone functions open. A DNF with overlapping
terms does not automatically satisfy their separation hypothesis.

9. The the author's *Read-once formulas and a question of Han on the Fourier
entropy-influence conjecture* is indexed with its abstract at
[aiXiv:2611.00789](https://aixiv.online/abs/2611.00789), pointing to
[Zenodo 24064349](https://zenodo.org/records/24064349). The primary Zenodo
record was unavailable through the web tool, so the abstract is a locator,
not independent proof evidence. The local memories and T021/DOSSIER.md
identify its earlier public repository and the full-split bound 5+ln 4 nats
per influence. The local FEI19 PROOF.md and FEI21 referee report subsequently
prove the sharp per-leaf full-split constant pi^2/2 nats. They were read
directly. PROOFS.md Section 3 adapts that same potential to the erasure
kernel, obtaining pi nats, and credits the source. The two kernels differ.
Han's square-root overlap criterion is false even for monotone read-once
formulas; this does not refute the erasure question.

Within the fleet, FLOW 12(v) and the September memory
`fei_monotone_downset_bounded_width_dnf_2026_09_24.md` already record
bounded-width DNF bounds, relative-step bounds and the maximum-influence
counterexample. They are useful internal prior work, not a substitute for
published attribution. Section 2 of PROOFS.md improves an additive constant
in that local argument but introduces no new class. Section 3 proves a
per-leaf erasure bound, by the existing selector potential, rather than
claiming read-once FEI or a new class for the first time.

The boundedness of Question M is exactly the still-unresolved monotone FEI
problem up to an additive 2/ln 2 in optimal constants (PROOFS.md Section 1).
I found no theorem in the checked sources that resolves it. This is a
bounded literature review, not a proof of absence from all literature.
