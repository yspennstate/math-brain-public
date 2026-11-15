MINOR

The two formally stated negative results are correct. I found no hidden assumption of fair colors, no use of negative observation times, and no failure of the measurable-estimator argument. They have limited value as progress on F0126: Theorem A removes an explicit hypothesis of the question; Theorem B exposes an inadequate equivalence group for a sheared simple walk. Its kernel-symmetry mechanism is already printed in a closely related model. I would retain the results as elementary clarifications, with the corrections below, rather than describe them as substantive new progress toward reconstruction modulo all walk-kernel symmetries.

The claimed upper bound of 1/2 is valid. In fact the same walk admits a stronger upper bound of **1/4**, proved below. This strengthens the submitted statement; it does not refute it. The claim correctly says that its obstruction disappears when the equivalence includes all kernel symmetries. No resolution of that general reconstruction question was found in the literature checked through 13 November 2026.

Errors, omissions, and necessary qualifications follow. Locations refer to the submitted files in `claim_files/`.

1. **Missing qualifications in the summary of statement (1).** `REPORT.md:7` must say nondegenerate finite i.i.d. scenery and a walk confined to a proper reachable subgroup, with a fixed countable family of spatial bijections. For constant scenery, full reconstruction is trivial. Simply declining to assume irreducibility does not make every walk nonreconstructible. Theorem A at `REPORT.md:61` has the necessary hypotheses and its proof is correct. Fix the headline to match it. A family may be any fixed countable family of bijections; group closure is unnecessary.

2. **The bridge from nonirreducibility to a proper subgroup is implicit.** `REPORT.md:61–73` proves the proper-subgroup result, rather than explicitly proving the general nonirreducible recurrent-walk formulation suggested by the summary. The missing bridge is elementary: recurrence forces every support increment to have an admissible return path to zero, so the reachable semigroup is a subgroup. A proof is given below. Without recurrence the reachable semigroup need not be a subgroup. This is a small scope clarification, not a defect in Theorem A.

3. **Separate the printed question from its repaired interpretation.** `REPORT.md:9–11,128,163–167` reasonably distinguishes Euclidean equivalence from kernel equivalence. However, the survey itself specifies “translation or reflection”; it does not define this as all walk-kernel automorphisms. For ordinary Euclidean reflections, Theorem B really is a negative example to the literal higher-dimensional formulation, even after irreducibility is imposed. Calling the formulation with all kernel symmetries the authors' intended question is an interpretation, not a quotation or a documented attribution of intent. Fix by explicitly labeling the enlarged quotient a natural repaired formulation. The submitted caveat is mathematically right.

4. **A printed precedent for the mechanism is omitted.** `LITERATURE.md:43` mentions Finucane–Tamuz–Yaari (2014) only for Fourier criteria. Add their §3.2 and Lemma 3.2 as a precedent for the automorphism coupling in Theorem B; details appear below. No first-in-print claim for either exact formulation is justified by this search. [Primary text](https://arxiv.org/pdf/1105.5569).

5. **Incorrect branching-paper citation.** `LITERATURE.md:42` gives AAP 27(2) (2017), 877–897. The correct pages are **651–685**, and the published author order is **Heinrich Matzinger, Angelica Pachon, Serguei Popov**. The model description is correct. Fix the bibliography. The IMS issue contents put this article at 651 and the next at 686. [IMS issue contents](https://www.imstat.org/publications/aap/aap_27_2/AAP_27_2.pdf).

No other mathematical error was found in the submitted proofs. The bound 1/2 being nonoptimal is not an error, and the report does not claim it is sharp. The finite-cycle experiment is expressly identified as a surrogate; it cannot establish an infinite-lattice theorem and is not presented as doing so. I did not rerun or reuse the submitted computational code.

The source and its exact mathematical formulation

The complete 13-page arXiv text is independently extracted in [sources/survey_2006.txt](sources/survey_2006.txt), with PDF-page markers. Its PDF-byte SHA256 is `5827a0d7f0d9c7a45bdfe2c58c25352c4a1625af1eb37b4fe049d76e199407c8`. Only text was saved. The following preserves the mathematical quantifiers; only question 7 and the short equivalence phrase are quoted verbatim. [Published survey](https://arxiv.org/pdf/math/0608219).

Section 1, printed pp.53–54 / PDF pp.1–2:

\[
 d\in\mathbb N,\quad d\ge1,\qquad F\subseteq\mathbb Z^d
 \quad\text{(possibly infinite)},
\]
\[
 X=(X_n)_{n\in\mathbb Z}\sim m_F^{\otimes\mathbb Z},\quad
 \operatorname{supp}m_F=F,\quad S_0=0,\quad S_n-S_{n-1}=X_n,
\]
\[
 \forall x\in\mathbb Z^d\ \exists n\in\mathbb N,
 \ x_1,\ldots,x_n\in F:\quad x_1+\cdots+x_n=x.
\]

The last condition is semigroup generation, hence irreducibility. Also

\[
 |G|<\infty,\quad \operatorname{supp}m_G=G,\quad
 C\sim m_G^{\otimes\mathbb Z^d},\quad C\perp X,\quad Y_n=C_{S_n}.
\]

The default is fair binary scenery unless stated otherwise. These standing assumptions impose neither bounded jumps, symmetry, moments, nor aperiodicity. They do not restrict the paper to dimension one.

Section 3, printed pp.61–62 / PDF pp.9–10, uses

\[
 Y^+=(Y_n)_{n\in\mathbb N_0},\qquad
 \mathcal A:G^{\mathbb N_0}\longrightarrow G^{\mathbb Z^d}
 \ \text{measurable},\qquad
 \mathbb P\{\mathcal A(Y^+)\sim C\}=1.
\]

Its equivalence is “translation or reflection.” In dimension one this is exactly

\[
 c'\sim c\iff \exists a\in\mathbb Z,\ \epsilon\in\{-1,1\}\quad
 \forall x\in\mathbb Z:\ c'(x)=c(a+\epsilon x).
\]

Section 4, question 7, printed p.63 / PDF p.11, is exactly:

> Is scenery reconstruction possible for an arbitrary recurrent random walk with i.i.d. increments and an arbitrary i.i.d. random scenery?

Theorem 3.3, printed p.62 / PDF p.10, has

\[
 F\supsetneq\{-1,0,+1\},\qquad |G|=2,
\]

under the paragraph's one-dimensional, uniform-law setting. The submitted reading of the strict-superset sign is correct. The cited bounded-jump papers supply additional context; this shorthand is not a theorem about every infinite or drifting superset.

My interpretation of the source is therefore as follows. Irreducibility is part of question 7's inherited setting. General dimension is allowed. The observations contain neither walk increments nor positions. A successful rule must be one measurable map, rather than a different test for each known pair. Giving the output the larger Euclidean lattice-isometry quotient makes Theorem B's impossibility stronger than required for any smaller ordinary translation/reflection quotient. Enlarging further to kernel symmetries changes the question.

Verification of statement (1)

For a fixed proper subgroup H of Z^d, the complement H^c is infinite. If H is infinite, a coset x+H with x outside H already gives infinitely many omitted sites. If H is finite, H={0}, and d>=1 gives the same conclusion. Every path with increments in H remains in H.

Let U be an independent private seed if the estimator is randomized, and condition on

\[
 \mathscr H=\sigma(C|_H,S,U).
\]

The output D=\mathcal A(Y^+,U) is fixed conditionally on this sigma-field, while the coordinates C(y), y outside H, remain independent with their original law. For a fixed spatial bijection gamma and distinct y_1,...,y_k outside H, the event D=C composed with gamma forces

\[
 C(y_i)=D(\gamma^{-1}y_i)\quad(1\le i\le k).
\]

Consequently, with p_max=max_g m_G(g)<1,

\[
 \mathbb P(D=C\circ\gamma\mid\mathscr H)\le p_{\max}^k
 \quad\text{for every }k,
\]

and the conditional probability is zero. Taking a countable union and integrating proves exactly the claimed probability-zero result. Constraints involving visited coordinates can only further reduce the probability. There is no unjustified independence between the estimator and the visited scenery.

Measurability is straightforward but worth making explicit: the scenery and path spaces carry their product sigma-fields; evaluation C(S_n) is measurable on a countable lattice. For fixed gamma,

\[
 \{D=C\circ\gamma\}
 =\bigcap_{x\in\mathbb Z^d}\{D(x)=C(\gamma x)\}
\]

is measurable. A countable union over gamma is measurable too. No selection theorem or measurable choice of an orbit representative is used. This argument does not assert a uniform result over an uncountable, scenery-dependent family of transformations.

Here is the scope bridge. Let M be the reachable semigroup of a recurrent i.i.d.-increment walk. For each x in its increment support, the walk can make first step x with positive probability. Recurrence of zero and the Markov property imply that, from x, a return to zero is possible. At least one finite return path has positive probability, so some finite sum of support increments equals -x. Thus M contains the inverses of its generators and is the subgroup H generated by the support. If the walk is nonirreducible, H is proper and the theorem applies. Conversely, recurrent irreducibility makes every site visited almost surely, so this particular obstruction is unavailable. One can see this by repeated excursions from zero, each having a fixed positive chance to hit a specified accessible site, followed by a countable intersection over sites.

Thus (1) is an elementary consequence of unobserved independent coordinates. Its example, increments ±2 in dimension one, is recurrent but explicitly excluded by the survey. Under the survey's own assumptions there is no counterexample here. Time period two does not imply an unvisited parity class when every observation time is retained: the ±1 walk is the immediate counterexample to that mistaken inference.

Verification of statement (2), in the order of the submitted proof

Write u=(1,0), v=(1,1), and let the increments be uniform on {u,-u,v,-v}. I use M for the symmetry matrix and \mathcal A for an estimator to avoid the submission's overloaded A.

1. **Walk and irreducibility (`REPORT.md:77–92`).** With

   \[
   B=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
   B^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix},
   \]

   S=BT for ordinary planar simple symmetric T. The columns of B are u and v, and det B=1. In particular e_1=u and e_2=v-u are semigroup-reachable because both signs of both generators occur. Every lattice site communicates with zero. Period two causes no problem.

2. **Recurrence (`REPORT.md:94–102`).** For T=(U,V), each increment of (U+V,U-V) is one of the four sign pairs with probability 1/4. These are two independent one-dimensional simple walks. Therefore

   \[
   \mathbb P(S_{2n}=0)=\mathbb P(T_{2n}=0)
      =\binom{2n}{n}^{\!2}/16^n.
   \]

   For b_n=binom(2n,n)/4^n, the submitted ratio inequality is correct: after clearing positive denominators its squared comparison has numerator difference 1. Since b_1=1/2, it gives b_n>=1/(2 sqrt(n)). The Green sum diverges. If the probability of another return were r<1, the total number of visits, including time zero, would have expectation 1/(1-r), a contradiction. Thus the recurrence proof is valid. Independent integer spatial recursion verified the return counts through time 24, without relying on the ratio inequality.

3. **Symmetry (`REPORT.md:105–112`).** Direct multiplication gives

   \[
   M=BRB^{-1}=\begin{pmatrix}1&-2\\1&-1\end{pmatrix},\quad
   R=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
   M^{-1}=\begin{pmatrix}-1&2\\-1&1\end{pmatrix}.
   \]

   Its action cycles u,v,-u,-v. It preserves the entire probability kernel, not just its support. Also det M=1, M^2=-I, and

   \[
   M^\mathsf TM=\begin{pmatrix}2&-3\\-3&5\end{pmatrix}\ne I.
   \]

   Thus this is a lattice automorphism fixing the root and not a Euclidean isometry.

4. **Observation equality (`REPORT.md:108–112`).** For every deterministic c define c^M(x)=c(M^{-1}x). Coupling S'=MS gives

   \[
   c^M(S'_n)=c(S_n)\qquad\text{for every }n\ge0.
   \]

   The transformed increments remain independent and identically distributed with the same law. Equality of the full forward observation laws follows, including the time-zero observation. No averaging over scenery is needed for this step. Either M or M^{-1} can be used in the phrase “composed with the symmetry,” provided the walk is transformed in the matching direction.

5. **Different Euclidean classes (`REPORT.md:114–120`).** The affine-invariance lemma is right. A nonidentity affine lattice bijection moves infinitely many sites. From these one can greedily select infinitely many disjoint pairs {x,Tx}; excluding finitely many endpoints excludes only finitely many additional choices and preimages. On k such pairs the required equalities have probability rho^k, where rho=sum_g m_G(g)^2<1. Hence C=C composed with T has probability zero. This conclusion would be false for some finitely supported permutations, but the submission correctly restricts this lemma to affine maps.

   If C^M=C composed with h, h(x)=Qx+b a Euclidean lattice isometry, substituting x=Mu yields C=C composed with hM. The affine map hM cannot be the identity, since that would force b=0 and M=Q^{-1} orthogonal. Each h has probability-zero equality, and there are only countably many h. Thus C^M and C have different Euclidean orbits almost surely.

6. **Joint invariance and every estimator (`REPORT.md:122–126`).** On the product space, Theta(C,S,U)=(C^M,MS,U) preserves the joint law. Spatial permutation preserves any i.i.d. color law; there is no permutation of color labels. Independence is preserved because each transformed component depends only on its own original component. Theta fixes Y^+ and U. The two success indicators

   \[
   I_0=1\{\mathcal A(Y^+,U)\sim_E C\},\qquad
   I_1=1\{\mathcal A(Y^+,U)\sim_E C^M\}
   \]

   have equal expectations and satisfy I_0+I_1<=1 almost surely. Therefore each expectation is at most 1/2. The events need not be independent, and Theta need not be an involution. The countable-coordinate formulation used above proves measurability of these events. This covers all measurable deterministic rules and independently randomized rules. It does not give a rule access to C through its random seed.

The result is therefore an annealed success bound for the specified nondegenerate finite i.i.d. scenery law, and an almost-everywhere ambiguity statement about scenery. It is not a claim that every single deterministic scenery is ambiguous modulo Euclidean isometries: constant sceneries, for example, are not.

There is an easy stronger bound. The linear kernel group is G=B D_4 B^{-1}, of order eight. Its intersection with the orthogonal lattice group is {I,-I}. Both facts were checked by exhaustively choosing the images of the basis u,v from the four possible increments. Four representatives of its Euclidean classes are

\[
 I,\quad M,\quad
 D=\begin{pmatrix}1&-2\\0&-1\end{pmatrix},\quad
 MD=\begin{pmatrix}1&0\\1&-1\end{pmatrix}.
\]

For distinct representatives g,h, the ratio h g^{-1} is nonorthogonal. The preceding affine lemma, including translations, implies that C^g and C^h have distinct Euclidean orbits almost surely. There are only six pairs to exclude. Each of the four product-space transformations preserves the joint law and fixes the record. Their four success indicators have common expectation p and sum at most one. Hence 4p<=1. No sharpness or achievability assertion is made here.

Once the output equivalence includes these kernel symmetries, all these transformed sceneries belong to the same class. For sufficiently many uniform colors, the positive planar simple-walk reconstruction result transports through B and reconstructs this particular sheared example modulo the conjugated lattice symmetries. This makes its nature especially transparent: it is simple walk in a nonorthogonal integer coordinate system.

Independent computation and its limits

The independent implementation is [code/independent_check.py](code/independent_check.py). It imports no submitted code, uses only the Python standard library, and fixes all seeds. Run:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 code/independent_check.py
```

Full histograms, exact integer path counts, seeds, matrix checks, and resource measurements are in [data/independent_check.json](data/independent_check.json). The program verifies the kernel permutation, determinant and inverse, conjugation, nonorthogonality, all eight linear kernel automorphisms, the four representatives above, and exact return counts through time 24.

For each experiment it first draws a fixed i.i.d. scenery on a box covering every queried coordinate. It compares that same scenery with its pullback by M^{-1}, without redrawing colors or wrapping the box. At seven increments it independently enumerates every one of the 4^7=16,384 hidden paths for each scenery. The full length-eight record histograms agree as integers. It then generates 120,000 independently sampled forward records from each scenery, using different path seeds. Thus the Monte Carlo comparison is conditional on a fixed scenery, not an automatically equal comparison after averaging two fresh i.i.d. sceneries.

| Scenery law | Exact TV, length-eight records | Empirical TV between independent samples | TV after breaking kernel symmetry |
|---|---:|---:|---:|
| (0.8, 0.2) | 0 | 0.01488333 | 0.4160318 |
| (0.7, 0.2, 0.1) | 0 | 0.01580000 | 0.3443191 |

The last column uses increment probabilities (0.4,0.1,0.3,0.2) on the same ordered support and exact weighted enumeration. This is a negative control, not a recurrent-walk counterexample. The nonzero values show the comparison can detect a broken kernel symmetry. The maximal Monte Carlo cell errors are below simultaneous Hoeffding tolerances with failure bound 10^-6 per experiment. The program also checks 10,000 coupled length-thirteen forward records per scenery, with exact equality at each time.

Simulation is not proof of equality at infinite time or of nonreconstruction. Those conclusions follow from the coupling and orbit arguments above. Finite calculations test their concrete implementation. The initial run used one thread, nice 10, 2.89 seconds and 20,611,072 bytes peak RSS on this Mac. The final run, which adds the four-representative assertions, also passes; its measurements are retained in the JSON. Neither run approached 4 GB. No PDF, page image, or scan was saved, and nothing was published or pushed.

Literature result and value

The closest explicit predecessor is **Finucane, Tamuz and Yaari, SPA 124(8) (2014), 2754–2770**, §3.2, preprint p.4, and Lemma 3.2, p.5. Their Z/7Z walk has support {1,2,4}; multiplication by 2 preserves its kernel. Coupling v_2=2v_1 and transforming the scenery yields identical records. Their finite model starts uniformly, unlike the rooted infinite model here, but explicitly prints the non-geometric automorphism mechanism. Kernel symmetries being unobservable is standard identifiability reasoning. The estimator bound is an elementary consequence of equal-law, disjoint success events. I did not locate the exact planar matrix example in print. [Full primary text](https://arxiv.org/pdf/1105.5569).

For Theorem A, I did not find the precise fixed-countable-family formulation as a separately named theorem. Its underlying unvisited-coordinate obstruction is elementary. Adding the p_max^k estimate and a countable union makes the almost-sure statement precise; it does not address the irreducible question.

The following checks prevent misclassifying earlier results as either counterexamples or a full solution:

- **Lindenstrauss (1999), Indistinguishable Sceneries, RSA 14(1), 71–86.** I fetched the author's PostScript into memory only and checked the abstract and Theorem 2.1 on preprint p.6 from its text strings. It constructs continuum many indistinguishable sceneries using a rapidly growing odometer construction. I did not verify final journal pagination of that theorem. This exceptional constructed family is not a typical-i.i.d. negative theorem. Indistinguishability there concerns the inability to distinguish almost surely; it must not automatically be upgraded to equality of rooted observation laws. [Author's primary preprint]((author's home page)).
- **Benjamini–Kesten (1996), J. Anal. Math. 69, 97–135.** The original publisher abstract confirms distinction of each fixed scenery from almost every random one for simple walks on Z and Z^2. A test depending on two known candidates does not supply a universal reconstruction rule. Full original theorem numbering was not accessible. [Publisher abstract](https://link.springer.com/article/10.1007/BF02787104).
- **Kesten (1996, 1998) and Howard (1996, 1997).** These cover single defects, periodic scenery and distinction/orthogonality questions. Kesten's 1998 chapter is DIMACS 41, 75–83. Howard's 1997 heavy-tail result concerns renewal spacings in the scenery, not heavy-tailed jumps. I checked bibliographies in the downloaded primary papers and the original Benjamini–Kesten references; some originals remained inaccessible, so I do not assert their exact theorem numbers or resolve inconsistent four/five-color thresholds in later accounts. None of these sources located a full arbitrary-increment theorem. [Kesten volume](https://archive.dimacs.rutgers.edu/Volumes/Vol41.html), [Finucane–Tamuz–Yaari bibliography](https://arxiv.org/pdf/1105.5569).
- **Matzinger (1999, 2005).** Three-color simple-walk reconstruction and fair binary simple-walk reconstruction are established special cases. The independent download of the EURANDOM binary preprint contains its explicit measurable-map Theorem 1, preprint p.2 / PDF p.4. The final binary paper is AAP 15(1B) (2005), 778–819. This is positive typical reconstruction, compatible with Lindenstrauss's exceptional examples. [Binary paper record](https://arxiv.org/abs/math/0503517).
- **Löwe–Matzinger–Merkl (2004), EJP 9, 436–507.** Theorem 1.1, p.438 / PDF p.3, proves reconstruction for finite increment support M, mean zero, gcd(M)=1, and more uniform colors than increment types. The increment probabilities need not be symmetric or uniform. This is not an arbitrary-law theorem. [Full text](https://emis.de/ft/42290).
- **Lember–Matzinger (2002 reports; 2008 publication).** I independently read the 2002 piece-reconstruction report, §§1.1–1.3, and the 2008 EJP paper, §§1.2–1.3 and Theorem 1.1, p.399. They concern symmetric irreducible bounded jumps and fair binary scenery. The EJP theorem recovers a fingerprint conditionally on a crossing endpoint; the companion report extends a seed using localization information. The submitted distinctions between these components and the survey's full-reconstruction statement are correct. In particular, the symmetric uniform five-step binary example is not a newly identified positive class. [Piece report](https://pure.tue.nl/ws/files/2870763/562518.pdf), [2008 primary text](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/491/491-1603-1-PB.pdf).
- **Löwe–Matzinger (2002), AAP 12(4), 1322–1347.** The independently downloaded earlier primary preprint, Theorem 1.1, preprint p.2 / PDF p.4, proves planar simple-walk reconstruction for sufficiently many uniform colors. It transfers to the sheared walk after conjugating the equivalence group. It is not a result for arbitrary colors or arbitrary planar kernels. [Primary preprint](https://pure.tue.nl/ws/files/3017578/526077.pdf).
- **Hart–Machado–Matzinger (2015), MPRF 21(4), 939–970.** Theorem 1.1, arXiv p.4, assumes five uniform colors, a symmetric walk sufficiently close to nearest-neighbor, sufficiently fast exponential tails, and holding. This really allows unbounded jumps; it is far from all recurrent increments. Matzinger–Pachon Pinzon (ALEA 9 (2012), 85–99), §1.1, explains a four-color improvement via localization. Both primary texts were downloaded and checked. [Exponential-tail paper](https://arxiv.org/pdf/1110.6853), [ALEA paper](https://alea.impa.br/articles/v9/09-04.pdf).
- **Popov–Pachon (2011) and Matzinger–Pachon–Popov (2017).** The former observes fixed windows along a branching walk. The latter, Theorem 2.1, arXiv p.4, uses all branching-particle records and at least 2d+1 uniform colors. These observation models provide more data than one unobserved walk. They do not resolve this question. [2011 publisher](https://www.tandfonline.com/doi/abs/10.1080/17442508.2010.544973), [2017 primary text](https://arxiv.org/pdf/1511.00973).
- **Lakrec (2022), Israel J. Math. 248, 149–200.** The arXiv text, pp.1–5, explicitly retains directions as well as colors and studies adversarial corruption. Its use of the phrase scenery reconstruction does not mean it solves color-only reconstruction. [Primary text](https://arxiv.org/pdf/1909.07470).
- **Gross (2024), SPA 167, 104233.** The continuous torus reconstruction result uses Fourier conditions and discusses symmetry. Its state space and scenery class differ from i.i.d. finite-color scenery on Z^d. The arXiv preprint was downloaded; theorem numbering differs from the journal version. [Primary preprint](https://arxiv.org/pdf/2011.14153).

The search included the requested names, the exact survey question, automorphism and kernel-symmetry obstructions, unbounded and heavy-tailed increments, and year-specific searches through 2026. I found no general affirmative theorem and no negative theorem modulo all spatial automorphisms preserving the walk kernel for the entire recurrent irreducible finite-alphabet i.i.d. setting. That repaired formulation remains open in the literature I could verify; neither the submitted work nor the finite-group predecessor settles it. Search coverage and access limitations are recorded in [sources/reading_notes.txt](sources/reading_notes.txt) and [LOG.md](LOG.md), rather than treated as a proof of exhaustive absence.

Exactly what survives the audit is: full reconstruction modulo any fixed countable family of spatial bijections has success probability zero when an infinite deterministic set of independent nondegenerate scenery coordinates is never observed; and the explicit irreducible recurrent sheared planar simple walk cannot reconstruct typical finite i.i.d. scenery modulo Euclidean lattice isometries, with success at most 1/2 as claimed, indeed at most 1/4. These are correct elementary obstructions. They give a useful warning about hypotheses and quotients, with no demonstrated substantive novelty and no solution of the question after quotienting by all kernel symmetries.

Task: “Break it if it is wrong” — independent referee audit of F0126. Received 2026-11-13 approximately 10:02 +04 (Asia/Tbilisi).
