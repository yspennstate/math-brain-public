# Primary-source and priority checkpoint for deterministic LTF FEI

Checked 2 October 2026. This checkpoint distinguishes the internally audited
mathematical proof from historical priority and external validation.

The proposed theorem is H(f)<=C I(f) for every deterministic linear threshold
function on the uniform Boolean cube, with one absolute constant, arbitrary
input weights and arbitrary threshold. The new largest-weight split proof
must be read in full with its independent audits; finite checks do not prove
that dimension-independent statement.

## Established analytic inputs

1. Klivans--O'Donnell--Servedio, *Learning Intersections and Thresholds of
   Halfspaces*, JCSS 68 (2004), 808--840. Theorem 18 of the
   [author-hosted journal manuscript](https://www.cs.columbia.edu/~rocco/Public/focs02.pdf)
   bounds Boolean-halfspace bit-flip noise by
   min(2p,20.5p sqrt(epsilon ln(1/p))). The root and independent reviewers
   checked the statement and noise convention. This is old input, not a
   new result of this continuation.
2. Keller--Klein, *Biased halfspaces, noise sensitivity, and local Chernoff
   inequalities*, Discrete Analysis 2019:13,
   [primary paper](https://arxiv.org/pdf/1710.07429v3).
   Theorem 1.4 gives maximal physical influence comparable to
   p min(1,tau sqrt(ln(1/p))) with normalized input weights and unrestricted
   threshold. The proof uses its lower bound. The preceding regular-weight
   corollary also uses Theorem 1.1. Constants are existential and absolute;
   no numerical value of their lower constant is certified here.
3. Uniform-cube hypercontractivity is classical. The specific consequence
   used here is Stab_(1/2)(B)<=alpha^(4/3) for an indicator of measure alpha.
   It follows from ||T_(1/sqrt(2))B||_2<=||B||_(3/2).
   An author-written statement and proof are in Ryan O'Donnell,
   [Lecture 16, Theorem 1.1](https://www.cs.cmu.edu/~odonnell/boolean-analysis/lecture16.pdf).
   It concerns the uniform cube; no biased-input extension is being assumed.

## Prior LTF claims and their actual scope

The old 2013 abstract of *Upper Bounds on Fourier Entropy* claimed FEI for
all LTFs. It is not safe to treat that abstract as the current theorem.
The [ECCC report and revision history](https://eccc.weizmann.ac.il/report/2013/052/)
show Revision 2, dated 13 September 2018, removing inaccuracies including
the previous Lemma 5.4 and Theorem 5.5. The
[full revised primary manuscript](https://eccc.weizmann.ac.il/report/2013/052/revision/2/download)
has Section 4 and Corollary 4.8 proving H(LTF)<=C sqrt(n), followed by
read-once-formula FEI in Section 5. It does not provide a valid universal
H(LTF)<=C I(LTF) statement there. The root inspected the actual revised
section, not just the old abstract. This matters because a search result
can otherwise make the present target appear already settled.

Chakraborty--Karmalkar--Kundu--Lokam--Saurabh,
*Fourier Entropy-Influence Conjecture for Random Linear Threshold Functions*,
[2019 arXiv primary manuscript](https://arxiv.org/abs/1903.11635) and
[author manuscript](https://iuuk.mff.cuni.cz/~koucky/LBCAD/papers/random-ltf.pdf),
explicitly state in the introduction and Section 3 that their methods do not
prove FEI for all LTFs. They prove random-weight results and a deterministic
regular corollary. Definition 9 includes the bias w0 in both normalization
and maximal-weight regularity; Corollary 10 assumes tau<=c/sqrt(n).
Thus that stated regular theorem does not cover every deterministic LTF.

Gonzalez--MacManus--Pereyra,
[*Further evidence towards the Fourier Entropy-Influence conjecture*, v2](https://arxiv.org/html/2606.00246v2),
revised 9 June 2026, develops the restriction-increment induction framework
for several other classes and still treats unrestricted FEI as conjectural.
It is relevant to the split framework, but does not by itself certify the
current status of every halfspace subclass. The exact split identity used
here includes its interference term; dropping that term would be wrong.

## Bounded current search and honest conclusion

Targeted searches on 2 October 2026 covered deterministic LTF/halfspace FEI,
regular and arbitrary-bias halfspaces, largest-weight entropy splitting,
slab noise stability, recent 2025/2026 FEI papers, and the older retracted
LTF claim. No earlier complete proof of this particular largest-weight
split theorem or of all deterministic-LTF FEI was located. This is negative
search evidence, not a certificate that no earlier proof exists.

The analytic proof and its audits can therefore be reported as a complete
internally verified theorem in their stated scope. It would settle the
deterministic-LTF subproblem described as open by the primary random-LTF
paper. A claim of historical novelty, definitive present-day priority, or
acceptance by the mathematical community requires an expert literature
review and external validation, neither of which has occurred. No one has
been contacted, and this work is being preserved only in the authorized
private repository.

Unrestricted Boolean FEI and biased-input-product FEI remain unproved here.
The earlier monotone maximum-influence counterexamples remain valid because
they need not be LTFs. The slab estimate uses the parallel-halfspace geometry
and the largest defining weight, beyond the failed separator-only condition.
