ACCEPT

The partial claim is mathematically correct. I found no counterexample to A–E
and no missing argument that changes any of their conclusions. The proof works
with counting measure, uses positive resolvent parameters correctly, and does
not assume that every orientation field is irreducible. In particular, the
circulating field really is recurrent and supplies the requested recurrent
example for which the dyadic series converges.

This is an acceptance of a partial result. It does not solve Problem 3. The
resolvent machinery, bounded-stream recurrence, and Bosi's alternating/random
and sparse-perturbation results are predecessors. E is an elementary consequence
of Bosi, rather than an independent new transience theorem. I did not find A's
explicit comparison, B's unbounded deterministic criterion, C's full tail
classification, or D's simultaneous extension stated in the sources inspected.
That is a bounded literature finding, not a certification of priority.

The numbered error/gap list is as follows. Locations refer to
`claim_files/REPORT.md`, whose line numbering was checked directly.

1. No mathematical error or unfilled proof obligation was found in A–E,
   lines 31–459, including equations (1)–(16). No mathematical correction is
   required. Detailed checks appear below.
2. The literature investigation is explicitly incomplete at lines 540–548:
   Pène's 2020 survey and Brémont's separate 2016 paper were identified but
   not read. I independently encountered the same publisher/TLS obstacles.
   This is a limit on an exhaustive novelty judgment, not a gap in A–E.
   Fix before making a stronger priority claim: obtain those full texts and
   extend the citation search. The submission's existing qualification at
   lines 107–113 and 484–487 should remain.
3. A useful presentation addition at lines 418–423 is to define the single
   measurable probability-one event used in D. The argument is already valid;
   the explicit event and measurability justification below make its quantifier
   order completely transparent. This requires no change to the theorem.

The source question and the meaning of recurrence

The paper is Ahmed Bou-Rabee and Yuval Peres, *The randomly oriented Manhattan
lattice in 2D is transient*, **arXiv:2609.07621v1**, submitted 7 September 2026.
The independently downloaded v1 has 16 pages. Its Section 7, page 14, gives
the exact question in Problem 3:

> Which orientation fields give a recurrent walk, and which give a transient one?

The surrounding paragraph contrasts the iid environment with a stationary
ergodic recurrent law obtained by randomly translating the alternating field.
The following paragraph asks a related irrational-rotation question for a
model with bidirectional vertical edges. These are contextual examples; the
main question is not restricted to stationary fields. The submission interprets
the question correctly and distinguishes the two models.
([Source paper, §7](https://arxiv.org/abs/2609.07621v1).)

For a fixed field let (P) be the discrete transition kernel, with probability
(1/2) for each outgoing edge, and put

\[
G(o,o)=\sum_{n\geq0}P^n(o,o).
\]

A site is recurrent precisely when its positive-time return probability is
one, equivalently (G(o,o)=\infty). The number of returns otherwise has a
geometric tail, giving a finite diagonal Green function. These are statewise
facts for a countable Markov chain and require no irreducibility. The
submission's convention, recurrence at every starting site and transience at
every site, is consequently appropriate; it agrees with the sitewise form of
the source paper's transience theorem.

There is an additional safeguard in this particular model. (P^T) is also
stochastic and has the same diagonal powers as (P). A recurrent state is
therefore recurrent for the reversed walk too. Recurrence forces every outgoing
edge to have a return path; applying the same argument to (P^T) supplies paths
back across incoming edges. Starting at any recurrent state, all its lattice
neighbors communicate with it, and this propagates across the connected square
lattice. Thus a field with even one recurrent state is irreducible and recurrent
everywhere. In particular there is no overlooked mixture of recurrent and
transient sites in the claimed examples. None of the submitted proofs needs
this extra observation.

Verification of the proof

At lines 119–138, write the two directed shifts as

\[
Uu(x,y)=u(x+e_y,y),\qquad Vu(x,y)=u(x,y+f_x).
\]

Each shift is a permutation of the lattice and hence a unitary operator on
counting-measure (ell^2). Its inverse follows the same line in the opposite
direction. Therefore (L=U+V-2I) is bounded, and direct adjunction gives exactly
the submitted symmetric part (mathcal S) and antisymmetric part (A).
Multiplication by (e_y) commutes with horizontal translation; multiplication
by (f_x) commutes with vertical translation. This proves (A^*=-A) for every
allowed field. It would fail for general vertex-dependent orientations, which
are outside the claim.

Every vertex has one horizontal and one vertical incoming edge, as well as two
outgoing edges, each of rate one. Thus counting measure is invariant. More
formally, both (P) and (P^T) are stochastic, and Poissonization preserves
their row sums. There is no illegitimate use of the constant function as an
(ell^2) vector. The normalization
(mathcal E(u)=\frac12\sum_{\{z,w\}}(u(w)-u(z))^2), with unordered edges,
is correct.

At lines 141–189, for **each positive** (lambda), (H=lambda I-mathcal S)
is bounded and (H\geq\lambda I). With
(B=H^{-1/2}AH^{-1/2}), one has (B^*=-B). The operators (I\pm B) are
invertible and commute, and

\[
\tfrac12\big[(I-B)^{-1}+(I+B)^{-1}\big]=(I-B^2)^{-1}.
\]

Conjugation gives equation (1), with the **minus** sign in
(H-AH^{-1}A). Indeed

\[
\langle u,(H-AH^{-1}A)u\rangle
=\langle u,Hu\rangle+\langle Au,H^{-1}Au\rangle.
\]

This operator is positive and bounded below by (lambda I). Completing the
square proves equation (2); optimizing over scalar multiples of any test vector
gives (3). A real diagonal matrix element of the original resolvent equals
that of its symmetric part. Thus the formula is for the actual diagonal Green
function, not a substitute symmetric walk.

The domain is all of (ell^2) at positive (lambda). No inverse of
(-mathcal S) at zero is being asserted. The cutoff argument first fixes a
finite test function and then takes (lambda) small enough to control
(lambda\|u\|_2^2). The uniform estimate is only on the other terms, as it
should be. Finally,

\[
G_{A,\lambda}(o,o)=\int_0^\infty e^{-\lambda t}p_t(o,o)\,dt,
\qquad
\int_0^\infty p_t(o,o)\,dt=\tfrac12G(o,o).
\]

The factor (1/2) comes from total jump rate two. Nonnegativity of the kernel
allows monotone convergence in (lambda\downarrow0), even though (p_t(o,o))
need not itself be monotone in time. This settles the nonreversible and
reducible-chain issues in the resolvent step.

At lines 193–245, the face stream
(h(x,y)=[S(y)-T(x)]/2) has the correct signs: its upper-minus-lower difference
is (e_y/2), and its left-minus-right difference is (f_x/2). Regrouping edges
counterclockwise around faces gives (5) with no missing factor two. The stated
diagonal identity on each face also checks. The resulting bound

\[
|\langle u,Av\rangle|\leq4\sqrt{W_h(u)\mathcal E(v)}
\]

and duality give (langle Au,H^{-1}Au\rangle\leq16W_h(u)), equations (6)–(7).
The constants are conservative. For finitely supported (u), only finitely many
face gradients are nonzero, so an unbounded (h) causes no domain problem.
Approximation in (v) is legitimate because (A) and (mathcal S) are bounded.

For A, lines 248–278, let (widetilde A=A+D), and set
(K=64\|h_D\|_\infty^2). The bounded primitive differences give a bounded
stream (h_D) and
(|Du|_{-1,lambda}^2\leq K\mathcal E(u)). Hence

\[
Q_{\widetilde A,\lambda}(u)
\leq(2+2K)Q_{A,\lambda}(u).
\]

The same argument with (D) replaced by (-D) proves the reverse inequality.
Extending from finitely supported functions uses density separately at each
positive (lambda), and preserves the displayed constant. The homogeneous
version of (2) is
(G_{A,\lambda}(o,o)=\sup_{u\ne0}u(o)^2/Q_{A,\lambda}(u)).
It gives precisely the two-sided comparison (9). The constant is independent
of (lambda) and (o), although it depends on the size of the primitive
difference. Both assertions of uniformity are justified. Flipping finitely
many whole lines changes each primitive by a bounded function on both tails.

For B, lines 280–324, I checked the annuli independently, including their
boundaries. There are exactly (8k+4) undirected edges between square radii
(k) and (k+1), so the annulus from (2^m) to (2^{m+1}) has
(12\cdot4^m) edges with a potentially nonzero radial gradient. Each has
gradient (d_m/2^m). Its two incident face weights have sum at most
(M(2^{m+3})^2). Consequently the submitted equation (10) holds even with

\[
\mathcal E(u_N)+16W_h(u_N)
\leq\sum_{m=0}^N[6+192M(2^{m+3})^2]d_m^2.
\]

In particular the stated constant 4096 is ample. Assigning an edge to the
annulus of its smaller endpoint radius prevents double-counting at boundaries.
The minimizing choice (d_m=w_m^{-1}/\sum_{j\leq N}w_j^{-1}) gives energy at
most a constant divided by that sum. A fixed shift of the dyadic index cannot
change divergence. Translating a fixed starting site changes the envelopes
only by a fixed spatial shift and additive constant. This proves recurrence
at every site, and (M(2^m)^2=O(m)) proves B1. The paired sparse-defect example
at lines 319–324 also has the asserted (O(\sqrt{\log r})) envelope on both
tails.

For C, lines 326–414, take (e=g), (f=-g) and
(R=|x+1/2|+|y+1/2|). Direct counting gives (8r) edges between successive
(R)-levels, hence
(mathcal E(\phi(R))=4\sum_{r\geq1}r a_r^2). Substitution into (A) gives
exactly the four dipoles in (12). At ((r-1,0)), for example,
(Au=a_{r-1}/2); at its paired site ((r-1,-1)) the value is
(-a_{r-1}/2). The four central sites have (Au=0). The outer support boundary
also contributes precisely the dipoles already present in (12).

These dipoles use distinct edges. Their squared coefficients sum to
(sum a_r^2), while the sum of squared test-function differences over those
edges is at most (2\mathcal E(v)). Cauchy–Schwarz and duality give (13).
This does not assume that different dipoles are orthogonal in the
(H^{-1}) norm. With (a_r=-1/(r h_N)), equations (11)–(14) therefore give

\[
Q_{A,\lambda}(u_N)
\leq\lambda\|u_N\|_2^2+4/h_N+\pi^2/(3h_N^2).
\]

This tends to zero in the required order of limits and proves recurrence.
Every directed edge belongs to a directed rectangle with sides on opposite
sides of the central coordinate lines, providing a return path around that
rectangle. The graph is irreducible. Reflection (x\mapsto-1-x) proves the
opposite circulating arrangement recurrent too.

For the saddle (e=g,f=g), the northeast and southwest quadrants are closed
and point outward. Before reaching them, the other two quadrants have
monotone coordinates moving toward their boundaries. Thus no directed cycle
is possible; (P^n(o,o)=0) for every (n>0), at every site. The reflected
saddle is the same. If either orientation sequence is globally constant, a
return would require zero steps in its monotone coordinate; the other
coordinate then moves monotonically along a single fixed line. Again positive
time returns are impossible. These cover the twelve constant-sequence tail
patterns and the two saddles. The other two patterns circulate.

Replacing the middle finitely many lines of an eventually constant field by
the corresponding canonical tail pattern is exactly an instance of A.
Consequently arbitrary intermediate line configurations cannot change this
classification. To try to break the clause, I flipped vertical lines (-1,0)
in the saddle. A directed central four-cycle appears, with positive four-step
return probability, but the field remains transient by A. A local cycle is
not a recurrent trap. Independently, a finite closed class is impossible:
invariance forces the number of boundary edges entering a finite set to equal
the number leaving it; a closed finite set would have neither, contrary to
connectivity of the square lattice.

The requested recurrent example with convergent B-series is explicit. For
(g(k)=1) at (k\geq0) and (-1) otherwise, its normalized primitive is

\[
S(n)=n\quad(n\geq0),\qquad S(-n)=n-2\quad(n\geq1).
\]

The two C1 fields have vertical primitives (-S) and (S). Thus their absolute
primitive sequences agree exactly, and for every integer (r\geq1),

\[
M(r)^2=2r^2,\qquad
\sum_{m\geq1}\frac1{1+M(2^m)^2}
<\tfrac12\sum_{m\geq1}4^{-m}=\tfrac16.
\]

One is recurrent and the other transient. Convergence of the series is
therefore insufficient for transience, and even the full absolute primitive
sequences cannot determine the type.

For D, lines 418–423, fix (f^0_x=(-1)^x) and define

\[
E_0=\{e:\ \sum_{n\geq0}P_{e,f^0}^n(z,z)<\infty
\text{ for every }z\in\mathbb Z^2\}.
\]

Each finite-time return probability depends on finitely many signs, so (E_0)
is Borel. Bosi's Theorem 9(i) gives it probability one, with the usual
countable-site extension. One can also use that an iid horizontal field has
both signs arbitrarily far out on both tails, making the alternating-vertical
graph irreducible. For **each** (e\in E_0), A compares (f^0) with **every**
(f) having bounded primitive, because (T_f-T_{f^0}) is bounded. This is a
deterministic statement, including if (f) is selected after seeing (e).
There is no uncountable intersection of null-set complements. Indeed the set
where transience holds for every such (f) is exactly (E_0), since (f^0)
itself belongs to that class. This also settles the measurability concern.

For E, lines 425–453, Bosi's Theorem 9(iii) applies to the alternating vertical
field and independent replacements with (p_y=c|y|^{-\beta}) outside a
finite set. Choose this exact power, rather than an arbitrary comparable
sequence. Then

\[
\mathbb E e_y=(-1)^y(1-p_y),\qquad
\operatorname{Var}(e_y)=2p_y-p_y^2\leq2p_y.
\]

The mean partial sums are bounded by the alternating-series test. Centered
increments are independent. Kolmogorov's maximal inequality gives exactly
(16), with exponent (1-\beta-2a). For any (a>0), the interval
((\max(0,1-2a),1)) is nonempty; choosing (eta) there makes the dyadic
probabilities summable. Borel–Cantelli and dyadic interpolation give the
two-sided bound (S(k)=O(|k|^a)), including the separately checked negative
tail. Intersect this probability-one event with Bosi's transience event and
fix a realization. Its other primitive is bounded. Swapping coordinates treats
(b>0). Alternating/alternating fields supply recurrent members of every
nonnegative upper-bound class. This proves the stated “every member” iff
(a=b=0), without claiming prescribed exact powers or an effective algorithm
for selecting the transient example.

The supplementary periodic argument, lines 461–479, also checks: on the finite
period quotient every row and column is a directed cycle, the chain is
irreducible, and its invariant law is uniform. The martingale strong law and
finite-chain ergodic theorem give the displayed velocity. Nonzero velocity
implies transience; zero period sums give bounded primitives and hence
recurrence. No additional irreducibility assumption on arbitrary fields is
being imported from this special case.

Literature and citation audit

I fetched the papers below independently from the network. I did not use the
submission's source texts. Retrieval URLs, timestamps, versions visible in the
texts, and SHA-256 hashes are recorded in `sources/MANIFEST.txt` and
`sources/INDEX.txt`. PDFs were decoded in memory; only plain text was saved.
The paper-page references below are to these independently retrieved texts.
Where an arXiv manuscript and a published version differ, the version used for
the locator is specified.

| Source | Checked locator and result | Consequence for the submission |
| --- | --- | --- |
| [Bou-Rabee–Peres, 2609.07621v1](https://arxiv.org/abs/2609.07621v1) | Theorems 1.1–1.2, p.2; Proposition 6.2 and Problem 3, p.14. Iid transience and finite annealed Green function; the deterministic kernel bound alone is not integrable. | Correct citation and scope. It does not state A–E's deterministic classification. |
| [Gianluca Bosi, *Simple random walks on some partially directed planar graphs*, 2019](https://amsdottorato.unibo.it/id/eprint/8914/) | Appendix A, Theorem 9(i)–(iii), pp.72–73; replacement definition (2.12)–(2.13), p.40. Alternating vertical lines with iid, centered periodic, or sparse randomly perturbed horizontal lines. | Exactly the coupled model needed in D and E. No transfer from a bidirectional-vertical model is being assumed. The critical defect exponent 1 is excluded. |
| [Gaudillière–Landim, *A Dirichlet principle for non reversible Markov chains and some recurrence theorems*, 1111.2445v1](https://arxiv.org/abs/1111.2445v1) | Theorem 2.4, p.5, and Lemma 5.5, pp.25–26. The latter bounds capacities using face-stream second moments relative to symmetric conductances. | Bounded deterministic streams satisfy the lemma. The variational approach and this subcase of B are established. The lemma's stated hypothesis does not contain B's unbounded deterministic envelopes. |
| [Beaton–Holmes, 2023 author manuscript](https://researchers.ms.unimelb.edu.au/~mholmes1%40unimelb/Manhattan_short.pdf) | Theorem 1 and following discussion, p.2. The floor of the rescaled even-time walk is planar simple random walk in the alternating field. | Recurrence is an unnumbered observation attributed to Guillotin-Plantard; the submission locates it correctly. |
| [Campanino–Petritis, math/0111305v1](https://arxiv.org/abs/math/0111305v1) | Theorems 1.6–1.8, p.5. Alternating, half-plane, and iid horizontal orientations. | Correct. Vertical edges here are bidirectional; the half-plane transience theorem is not the circulating C1 example. |
| [Guillotin-Plantard–Le Ny, math/0601102; independent mp_arc copy](https://web.ma.utexas.edu/mp_arc/c/06/06-4.pdf) | Theorem 1, condition (2.3), p.4; rotation discussion, pp.13–14. Mean one-half generating probabilities and the stated integrability assumption. | Correct. A deterministic half-circle indicator fails that condition, so this result cannot be invoked to settle its recurrence. |
| [Guillotin-Plantard–Le Ny, 0705.3342v1](https://arxiv.org/abs/0705.3342v1), also published text | Theorem 2, published p.339 / PDF p.3. Joint scaling with exponents (3/4,1/2) and dependent limiting coordinates. | Correct citation. It supplies neither an independent-coordinate argument nor a local return theorem for Manhattan fields. |
| [Castell–Guillotin-Plantard–Pène–Schapira, 1002.1878v1](https://arxiv.org/abs/1002.1878v1), also published text | Theorem 20 and Remarks 21–22, published p.2106 / PDF p.28. Arithmetic conditions and the summable (n^{-5/4}) return scale in the Campanino–Petritis case. | Correct. This is a one-scenery model with an independent skeleton. |
| [Pène, *Transient random walk in Z² with stationary orientations*, 2009](https://www.numdam.org/item/10.1051/ps%3A2008019.pdf) | Theorem 1, p.418 / PDF p.2, includes covariance and fourth-moment/decorrelation conditions. Theorem 2, p.419 / PDF p.3, includes (sup n^6\alpha_n<\infty). | Correct. The submission does not replace these assumptions by stationarity and centering alone. |
| [Devulder–Pène, 1110.4865v2](https://arxiv.org/abs/1110.4865v2) | Theorem 1, p.2; Theorem 2, pp.3–4. Random nonconstant iid layer probabilities, the stated negative-moment condition, and fixed or random orientations. | Correct. Both vertical directions remain available; this is not a universal Manhattan transience theorem. |
| [Campanino–Petritis, 1204.5297v2](https://arxiv.org/abs/1204.5297v2) | Theorem 1.5 and Proposition 1.8, p.4. Defect-probability transition at exponent 1 and recurrence after finite defects of a balanced periodic field. | Correct, but a different model. The submission appropriately uses Bosi for E. |
| [Brémont, *Markov chains in a stratified environment*, ALEA 2017](https://alea.impa.br/articles/v14/14-36.pdf) | Theorem 2.4, p.754 / PDF p.4; Proposition 7.1, p.790 / PDF p.40. General stratified criterion and recurrence of the half-circle rotation model for almost every angle. | Correct. It addresses the related partially oriented question for almost every angle, rather than the fully coupled Problem 3. |
| [Brémont, *Planar random walk in a stratified quasi-periodic environment*, 2007.01573v2](https://arxiv.org/abs/2007.01573v2) | Proposition 3.1 and Theorem 3.2, p.4; Proposition 3.3, p.5. Periodic drift, a continued-fraction recurrence condition, and exceptional angles with transience for almost every phase. | The exact continued-fraction, parity, growth, and phase qualifications in the submission agree with the source. |
| [Brémont, *Random walk in a stratified independent random environment*, 1811.07562v1](https://arxiv.org/abs/1811.07562v1) | Theorem 1.3, p.3. Centered nonconstant iid vertical bias ratios, with exponentially small horizontal drift scales and specified exponent margins. | Correctly separated from the Manhattan model and from simple-walk vertical skeletons. |
| [Ledger–Tóth–Valkó, 1802.01558v2](https://arxiv.org/abs/1802.01558v2) | Theorem 1.1, p.2, explicitly time-averaged displacement bounds in dimensions two and three. | Correct. These are not diagonal Green-function estimates. |
| [Nguyen, 2608.21701v1](https://arxiv.org/abs/2608.21701v1) | Theorem 1.1, p.3. Three-dimensional displacement Laplace transform with square-root logarithmic growth and log-log factors. | Correct. It does not classify two-dimensional deterministic fields. |
| [Guillotin-Plantard–Pène–Watbled, 2504.08485v2](https://arxiv.org/abs/2504.08485v2) | Theorem 1.1, p.3. Iterated-scenery joint limit with the three scales recorded in the submission. | Correctly identified as a different three-dimensional model. |
| [Armstrong–Bou-Rabee–Kuusi, 2601.22142v2](https://arxiv.org/abs/2601.22142v2) | Theorem A, p.5. Continuum random incompressible flow in the specified small-exponent regime. | Correctly screened out as a classification theorem for lattice orientation fields. |
| [Gu–Hao, 2609.19498v1](https://arxiv.org/abs/2609.19498v1) | Theorems 1.1–1.2, p.2. A sufficient confinement criterion and finite-size nonmonotonicity in the Manhattan mirror model. | Correct. Given the mirrors, routes are fixed; these are not fresh fair choices at each visit. |
| [Bosi–Hu–Peres, 1807.03498v4](https://arxiv.org/abs/1807.03498v4) | Graph definitions, p.3; Theorem 4, p.5. Vertical edges away from the horizontal axis remain bidirectional. | Correctly distinguished from C1. The recurrence theorem for their (G_2) is not literally a theorem about the circulating field here. |

I also retrieved Armstrong–Bou-Rabee–Kuusi's
[2404.01115v3](https://arxiv.org/abs/2404.01115v3), a continuum predecessor
cited by the source paper, and checked its model. It provides further
variational background, not an orientation-field criterion. Two saved arXiv
API searches covered 2024–2026, one for Manhattan in math.PR and one for the
phrase “Manhattan lattice” across categories. The latter returned the source
paper, Nguyen, and Gu–Hao; the former also had two unrelated hits. Title-based
searches supplied the iterated-scenery and continuum works. These searches
cannot establish that no relevant paper exists under different terminology.

Two retrieval exceptions remain. The arXiv endpoint for math/0601102 returned
HTTP 500, so the same dated author manuscript was obtained from mp_arc.
No arXiv copy was located for Bosi's thesis or Pène's 2009 paper; their
university/journal copies were read instead. The
[Pène 2020 survey](https://doi.org/10.1051/proc/202068003) returned HTTP 403
even at the independently identified correct publisher PDF path. Brémont's
separate 2016 author manuscript failed TLS certificate verification. Neither
unavailable full text is represented as inspected. Their roles in the
submission are disclosed background/access limits; no proof of A–E depends
on a statement taken only from those unavailable texts.

The novelty finding is consequently specific. The inverse identity and
variational method are established potential theory. Bounded-primitive
recurrence is already covered by bounded streams. A is a direct bounded-sector
perturbation comparison, and B extends the known stream-energy argument using
annular weights. D's alternating/random base case and E's sparse transient
examples are Bosi's results; the uniform extension in D and the polynomial
upper-bound formulation in E are deductions. I found no verbatim theorem
covering A, B's unbounded condition, C, or the full simultaneous statement D
in the inspected sources. C is not supplied by the superficially similar
revolving-walk papers. The evidence supports potentially new formulations and
applications, not five independently new methods or an established priority
claim for every consequence.

Reproducibility and extent of the answer

`code/check_audit.py` is independent code written for this review. It checks
eight pairs of fields on a (6\times6) torus at three positive resolvent
parameters. It verifies counting invariance, antisymmetry, the symmetric
resolvent identity, the quadratic variational optimum, two-sided quadratic
form comparisons, and diagonal comparisons. Its largest inverse-identity
error was below (2.25\cdot10^{-14}), and its largest variational error below
(8.0\cdot10^{-15}). These are checks of algebra, not finite-volume proofs
of infinite-volume recurrence.

It also checks 30 exact rational face identities and sector inequalities, 24
exact rational radial profiles including central and outer support sites, the
dyadic edge counts, and the exact two-sided primitive/envelope of (g).
Exact unwrapped coin-word counts through time 64 give (G_{64}(0,0)) about
1.65474 for the circulating field and exactly 1 for the saddle. After the two
saddle-line flips described above, (P^4(0,0)=1/16), illustrating the local
cycle without challenging the analytic transience conclusion. No simulation
or finite return sum was used to infer a type. The submission's additional
Monte Carlo tables are not needed for any conclusion here.

Reproduce with `python3 code/check_audit.py`; outputs and source-hash checks
are in `checks.json`. The check runs with one numerical thread and inherited
nice 20, lower scheduling priority than nice 10. Its measured peak RSS was
under 34 MB. Fetches were sequential and retained only text. No language-model
helpers, large computation, publication, pushes, or changes to `claim_files/`
were used.

Exactly what survives is A–E as stated: stability under bounded two-sided
primitive differences; the sufficient dyadic recurrence test; the complete
eventually-constant-tail classification; simultaneous almost-sure transience
for iid/bounded-primitive mixed fields; and the universal polynomial
upper-bound obstruction. The matching-absolute-primitives pair is valid.
There is still no necessary-and-sufficient test for general fields, no sharp
logarithmic threshold, and no classification for specified exact sublinear
growth or general coupled quasi-periodic fields. The original problem remains
open beyond these partial classes.

Task: “You are an independent referee … Break it if it is wrong.” —
13 November 2026, about 21:34 Asia/Tbilisi (session start).
