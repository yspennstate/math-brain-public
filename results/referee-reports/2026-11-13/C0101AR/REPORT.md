MINOR

The qualified mathematical claim survives this audit. The displayed matrix is an irrational, non-isolated maximal element for the ordinary Loewner order, in every dimension at least three, after the stated normalization shift. The zero-coordinate argument rules out every positive semidefinite improvement, including improvements involving the added coordinates. I found no fatal algebraic or analytic error.

Its value needs the qualification already present in the claim: it gives negative answers to the two literal yes/no questions in problem (4), and corrects an omission in the survey's description of dimension two. It does not describe all higher-dimensional maximal elements or settle a suitably defined question about the distinguished cone vertices analogous to the packing circles. The survey never formally defines a different notion of maximality. Calling that different notion its intention is an inference from context.

The following are the errors or gaps I found, with locations in the supplied claim report.

1. **The definition bridge is incomplete.** At claim_files/REPORT.md:19 and :44–51, the LPS class defined by an asymptotic equality is identified with the lower-obstacle class used in the new proof. The explanation establishes the inclusion from asymptotic representatives to lower obstacles, but not the reverse inclusion. Fix: supply the short argument using the geometric alternative in the proof of LPS Theorem 1.1 and the function maximality in Theorem 1.2. That argument is given below. This is a repairable omission, not a counterexample to the theorem.

2. **The survey normalization bridge is asserted too quickly.** At claim_files/REPORT.md:25–30, equality with the closed stabilization class needs both least action and an explanation of why the affine lower obstacle is harmless. Fix: explicitly pass from a stabilizer to an integer majorant, and from an affine majorant for A to a stabilizer for A−εI. Then use closure. The integer polynomial p_S does have Laplacian four; the claimed shift is correct. For the statement in all dimensions, one can explicitly use S_d=diag(d−1,1,…,1), of trace 2d−2.

3. **The stronger interpretation has no formal definition.** At claim_files/REPORT.md:5, :36 and :298, “cone peak” and the survey's apparent intention should not be treated as an already specified alternative problem. The report appropriately says “apparently,” but an exact remaining conjecture would need an intrinsic definition of its selected vertices. Fix: retain the statement about the ordinary order as a theorem, describe the proposed peak interpretation as an interpretation, and distinguish answering the two literal yes/no questions from classifying all maximal elements. Do not define a peak to mean an isolated maximal element and then present isolation of such peaks as a further conjecture.

The source history also deserves explicit mention: the earliest LPS theorem omits the residual contribution altogether, and the GAFA preprint's displayed closed-set formula likewise omits it. Those formulations must not be substituted for the corrected v4 theorem. This is context missing from the supplied report, rather than a defect in its use of v4.

I verified the mathematics as follows.

The survey's own language is: “the maximal elements of Γ(Z²) correspond to the circles in the Apollonian band packing of R².” This is open problem (4), preprint p.27. It then infers rationality in dimension two and asks for a description, isolation, and rationality in higher dimensions. Section 6, pp.21–22, defines Γ(Z^d) as the Euclidean closure of matrices whose rounded-quadratic sandpiles stabilize locally. Its figure describes cones associated with packing circles. It does not define “maximal,” restrict that word to positive-trace points, or exclude residual limits. [Survey](https://arxiv.org/abs/1611.00411); [downloaded text](sources/survey_1611.00411.txt).

Thus the natural mathematical reading of the printed words is ordinary maximality in the positive semidefinite order. That is also the order explicitly used in the cited LPS paper. A reader following the survey's geometric explanation would probably picture the circle vertices; the survey conflates that picture with the full set of order maxima. The literal reading answered by the claim is legitimate, not an artificial replacement of an explicitly different definition. The assertion about intended peaks is nevertheless contextual inference, not a quotation of a definition.

For the principal LPS source, I read Theorems 1.1 and 1.2, the paragraph following Theorem 1.1, and Lemma 3.4 and its proof, in v4. The theorem gives, in its Δg≤1 convention,

\[
\Gamma_{\mathrm{LPS}}=
\{A:\operatorname{tr}A\le0\}\ \cup\!
\bigcup_{C\in\mathcal B}\{A:A\preceq A_C\},\qquad
A_C=\frac12\begin{pmatrix}r_C+a_C&b_C\\b_C&r_C-a_C\end{pmatrix}.
\]

The following paragraph explicitly discusses trace-zero residual matrices in the closure of the union of downsets but outside that union. Theorem 1.2 constructs representatives of A_C that are periodic after subtraction of a quadratic and an affine function. It also says that any integer function lying above such a representative, and satisfying the same Laplacian bound, can differ from it only by a bounded function. Lemma 3.4 establishes topological closure by contact normalization and compactness. [LPS v4](https://arxiv.org/abs/1309.3267v4); [text](sources/LPS_1309.3267v4.txt).

In the earliest version served at the v1 URL, Theorem 1.1 gives only the circle downsets; there is no residual half-space. The published Annals Theorem 1.1 instead includes a half-space with trace at most 2, and the adjacent residual discussion also prints 2. V4 has 0 in both places. This is an acknowledged typo correction: the arXiv revision comment records the change from 2 to 0. It is not an alternative choice of the Δg≤1 normalization. For example, the printed trace-two half-space would admit the identity matrix, contradicting the universal bound tr A≤1 in that normalization. [Earliest version](https://arxiv.org/abs/1309.3267v1), [text](sources/LPS_1309.3267v1.txt); [published article](https://annals.math.princeton.edu/2017/186-1/p01), [text](sources/LPS_Annals_published.txt).

I also read the relevant introduction and normalization in arXiv:1208.4839. There the stable threshold is three, circle matrices have their trace shifted by two, and the displayed Theorem 1.2 identifies the closed class with the circle downsets alone. Read literally, that older closed-set formula has the same missing-residual issue. It does not invalidate the subsequent corrected characterization or the construction under review. [GAFA source](https://arxiv.org/abs/1208.4839); [text](sources/LPS_1208.4839.txt).

For completeness, write E_K^d for the matrices with an integer function g satisfying Δg≤K and a global lower obstacle q_A+b·x+c. An approximate minimum of g−q_A−b·x can be translated to the origin; subtracting its integer value and an integer linear function gives

\[
h(0)=0,\qquad h(x)\ge q_A(x)+\beta\cdot x-\varepsilon,
\qquad |\beta_i|\le\tfrac12.
\]

For matrices in a bounded set these inequalities give uniform lower bounds on each finite ball. From Δh≤K, an upper bound at one vertex and lower bounds at its other neighbors give an upper bound at any specified neighbor. Propagating from h(0)=0 gives upper bounds on every finite ball. Integer-valuedness and a diagonal subsequence then prove E_K^d closed. The slopes have a convergent subsequence as well. This argument works in arbitrary dimension and requires no periodicity.

An asymptotic LPS representative gives a lower obstacle for A−εI, so closure gives Γ_LPS⊆E_1^2. Conversely, let A∈E_1^2. If tr A≤0, LPS Theorem 1.1 puts it in Γ_LPS. If tr A>0 and A is not below a circle matrix, the circle-packing alternative used in LPS's proof gives A_C≺A for some circle C, with positive definite difference. The lower-obstacle representative for A, plus an integer constant, then lies everywhere above the periodic representative g_C, and its difference from g_C is unbounded. This contradicts Theorem 1.2. Therefore A is below a circle matrix and belongs to Γ_LPS. This supplies the missing reverse inclusion.

For the survey, a local stabilization of Δ⌈q_A⌉ gives a finite nonnegative integer toppling function u and hence an integer majorant g=⌈q_A⌉+u satisfying Δg≤2d−1. Conversely, if g has an affine lower obstacle q_A+b·x+c, then for each ε>0 the quantity b·x+c+ε|x|²/2 is bounded below. Adding an integer constant to g makes it majorize ⌈q_(A−εI)⌉. Its nonnegative difference from that rounded quadratic is a stabilizing upper bound by least action. Closure therefore gives exactly Γ_survey=E_(2d−1)^d.

For any integer diagonal S with trace 2d−2,

\[
p_S(x)=\sum_i S_{ii}\binom{x_i}{2}
\]

is integer-valued, has Hessian S and Δp_S=2d−2. Adding and subtracting p_S proves Γ_survey=S+E_1^d. In dimension three S=diag(2,1,1) is valid and Δp_S=4, so it translates the bound one into the stable bound five. This translation preserves the order, rationality, and isolation in the set of maximal elements. No division by 2d or change to an averaged Laplacian is involved.

Residual trace-zero matrices really are maximal. Let R=M(a,b,0) be outside every circle downset. If B−R is nonzero PSD, then tr B>0. If B were admissible, the corrected theorem would give B≼A_C for some C; transitivity would give R≼A_C, a contradiction. Hence R is maximal. Consequently the survey's dimension-two assertion is already false if it means *all* ordinary Loewner maxima. LPS explicitly describes the residual matrices; it does not explicitly call them maximal in that paragraph. Their maximality is the immediate argument just given. Its later discussion calls the circle matrices maximal in the semidefinite order, which is true for those matrices and does not remove the residual ones.

The explicit algebraic point checks independently. I wrote [independent_check.py](independent_check.py), without reading, importing, or executing any code in claim_files/code. Its exact calculations use Q[t]/(t⁴+4t²−1), which equals the requested Q(√5,t), since √5=t²+2. A separate numerical computation evaluates the defining radicals directly at 150 decimal digits.

The polynomial f(t)=t⁴+4t²−1 is irreducible. Independently of the computer check, t²=√5−2 has norm −1 from Q(√5), whereas a square in that field has a rational-square norm. Thus adjoining t has degree four. With a=1−t and b=t³+4t−1,

\[
(b+1)^2=t^2+4=\sqrt5+2,
\qquad a^2+b^2=6-10t+2t^2-2t^3.
\]

The positive embedding gives the proposed square-root expression for b. In the basis (1,t,t²,t³), the columns for 1,a,b,a²+b² are

\[
\begin{pmatrix}
1&1&-1&6\\
0&-1&4&-10\\
0&0&0&2\\
0&0&1&-2
\end{pmatrix},\qquad\det=2.
\]

Hence no rational equation of a circle can vanish at (a,b). Also a and b are individually irrational. This excludes circle boundaries; by itself it would not exclude interiors.

To exclude interiors, I independently derived the three insertion matrices from the Descartes rule and multiplied them. The product and characteristic polynomial agree with the claim:

\[
T=\begin{pmatrix}2&2&2&-1\\3&6&6&-2\\10&15&18&-6\\0&0&1&0\end{pmatrix},
\quad p(z)=z^4-26z^3+46z^2-26z+1.
\]

Putting y=z+z⁻¹ gives y²−26y+44=0. Its roots are 13±5√5. The larger produces λ=24.13891300137765… and its reciprocal; the smaller lies strictly between −2 and 2 and produces the two unit-modulus roots. Thus λ is the unique dominant root. Exact reduction verifies

\[
\lambda=(23+5t^2+47t+11t^3)/2.
\]

Rather than assuming the claim's supplied left eigenvector, I used the adjugate of zI−T. For every row, its dominant projection on the curvature column is nonzero, and the ratios of projections on the two center-coordinate columns are exactly a and b. Thus all three subsequences of inserted centers converge to the proposed point and their radii tend to zero.

The starting circles and line belong to the band packing. Successive insertions fill nested gaps, so they are distinct proper packing circles. Any fixed packing disk has interior disjoint from all the distinct disks in this sequence, apart from a possible equality with one of them. Passing to the limit shows that (a,b) lies outside its interior. The field calculation then excludes equality on its boundary. This proves that (a,b) is in the residual set outside *every closed proper packing disk*, not just outside a finite sample. Since

\[
M(a,b,0)\preceq A_C
\quad\Longleftrightarrow\quad
(a-a_C)^2+(b-b_C)^2\le r_C^2,
\]

the two-dimensional matrix C_*=M(a,b,0) is an irrational maximal element.

As a separate check, my fresh branching recursion fills both gaps between consecutive unit disks in one band period. It produced 9,834 distinct circles of curvature at most 3,000. All 150-digit distance-minus-radius values were positive. The minimum was approximately 0.00003511224453482841147, for curvature-center triple (2337,1201,2472). The 180th circle of the deep cyclic sequence had radius approximately 2.71509109156×10⁻⁸⁴ and center error approximately 2.93784949964×10⁻⁸⁴. These are checks, not a substitute for the preceding all-circles proof. Exact identities, numeric values, and resource measurements are in [independent_results.json](independent_results.json).

The higher-dimensional proof passes line by line. First, the ceiling bound is valid for E_1^d:

\[
\sum_i\lceil A_{ii}\rceil\le1.
\]

Indeed, subtract p_K with K_ii=⌈A_ii⌉ and s=tr K. The new obstacle Hessian D=A−K has diagonal entries in (−1,0]. Normalize an approximate contact as above. For sufficiently small ε,

\[
h(\pm e_i)\ge\tfrac12D_{ii}\pm\beta_i-\varepsilon>-1.
\]

These integer neighbor values are nonnegative. If s≥2, the inequality Δh≤1−s<0 contradicts h(0)=0. Off-diagonal entries do not enter this argument.

Now suppose ∑⌈C_ii⌉=1. Constant extension of a lower-obstacle representative proves C⊕0∈E_1^d whenever C∈E_1^k. For the converse, subtract the integer quadratic of Laplacian one. At an approximate contact the same neighbor argument gives h(±e_i)=0, since Δh≤0 and every neighbor value is nonnegative. For an added coordinate with zero quadratic coefficient, the obstacle inequality therefore gives |β_j|≤ε. Take a contact subsequence with ε→0. The compactness argument above leaves an integer h(x,z) with Δh≤0 and a lower bound independent of z.

For each x, the nonempty set of integer values {h(x,z):z∈Z^(d−k)} is bounded below, so it has an attained minimum H(x). At a minimizing z,

\[
\Delta_z h(x,z)\ge0,\qquad
\Delta_x H(x)\le\Delta_x h(x,z),
\]

so ΔH≤0. Adding back p_K proves C∈E_1^k. The elimination of the added affine slopes is essential; the claim correctly performs it before taking the minimum.

Finally let B=C⊕0+P be admissible with P PSD. In the old coordinates, ⌈B_ii⌉≥⌈C_ii⌉. Any positive added P_jj would contribute at least one extra unit to the ceiling sum and violate the bound. Thus P_jj=0 in all added coordinates. The PSD inequality |P_ij|²≤P_ii P_jj makes every corresponding row and column zero, including all mixed entries. Hence B=C'⊕0 with C'≽C and ceiling sum one. The reduction just proved makes C' admissible in dimension k; maximality of C forces C'=C. This covers every PSD improvement, rather than only block-diagonal or tested rank-one improvements.

For C_*, 0<a<1 gives ⌈a/2⌉+⌈−a/2⌉=1. Thus

\[
A_*^{(d)}=\frac12\begin{pmatrix}a&b\\b&-a\end{pmatrix}\oplus0_{d-2}
\]

is admissible and maximal for all d≥3. Its irrational entries persist under zero extension and the integer shift. Every proper circle matrix has positive trace and ceiling sum one: membership gives the upper bound one and positive trace gives the lower bound one. Such a circle matrix is maximal because one proper packing disk cannot contain another. The same lifting proof therefore applies to every approximating circle matrix. Their distinct rational lifts converge to A_*^(d). This proves non-isolation *among maximal elements*, as required.

I also checked the ancillary structural assertions rather than treating the saved searches as proofs. The separable convex approximation in §3.2 gives the stated exact diagonal slice. The trace bound proves maximality of integer symmetric trace-one matrices. In §3.4, expansion along a positive eigendirection and completing the square gives the claimed lower bound −5dδ−(2d+1)ε on the bounded-width path and its neighbors; propagation of zero is valid. Thus the claimed local isolation radius 1/(10d) for that integer family is supported. These results do not classify the remaining higher-dimensional vertices.

My separate [certificate verifier](check_certificates.py) uses only the saved data and fresh exact evaluation of the quadratic, affine term, and periodic correction. It verified all 190 positive certificates on 180,704 torus sites, the integrality of lattice increments, and the mean-Laplacian identities. Results are in [certificate_results.json](certificate_results.json). Fixed-period failures remain fixed-period failures; no finite search certifies the irrational example or proves a global exclusion. No code under claim_files/code was executed.

The literature audit found no printed resolution of the cubic-lattice classification or of a precisely formulated higher-dimensional analogue of the distinguished rational circle vertices, through 13 November 2026. This is a bounded search result, not proof that no such work exists. The survey citation list returned 33 records and the LPS list 45, including duplicates and older preprint dates; 30 and 36 respectively carried years 2017–2026. I screened these lists, searched the requested terminology and author combinations, and followed the plausible candidates to primary texts. The responses and search record are retained in [sources/LITERATURE.txt](sources/LITERATURE.txt).

| Work | What it establishes; relevance to this question |
|---|---|
| Pegden–Smart, *Stability of patterns in the Abelian sandpile*, Ann. Henri Poincaré 21 (2020), 1383–1399, [1708.09432](https://arxiv.org/abs/1708.09432) | Pattern convergence and stability using the two-dimensional structure theory. Not a classification in d≥3. |
| Bou-Rabee, *Convergence of the random Abelian sandpile*, Ann. Probab. 49 (2021), 3168–3196, [1909.07849](https://arxiv.org/abs/1909.07849) | Scaling limits for random initial configurations in general dimension. The effective sandpile operator remains implicit. |
| Bou-Rabee, *Dynamic dimensional reduction in the Abelian sandpile*, CMP 390 (2022), 933–958, [2009.05968](https://arxiv.org/abs/2009.05968) | Dimensional reduction for specified hypercube evolutions. Not the matrix reduction or full maximality problem considered here. |
| Bou-Rabee, *A shape theorem for exploding sandpiles*, Ann. Appl. Probab. 34 (2024), [2102.04422](https://arxiv.org/abs/2102.04422) | Limit shapes in an explosive regime. Its shape theorem does not identify Γ(Z³). |
| Bou-Rabee, *Integer superharmonic matrices on the F-lattice*, Adv. Math. 436 (2024), 109400, [2110.07556](https://arxiv.org/abs/2110.07556) | A complete matrix characterization on a different directed planar graph. Irrational boundary points on its hyperbolas are dominated by cone vertices; being on a boundary alone is not ordinary maximality. |
| Kalinin, *Sandpile solitons in higher dimensions*, Arnold Math. J. 9 (2023), 435–454, [2212.03717](https://arxiv.org/abs/2212.03717) | Piecewise-affine husking and solitons. Its introduction explicitly notes the missing higher-dimensional quadratic-form pattern classification. |
| Aliev–Kalinin, *Convergence of a sandpile on a triangular lattice under rescaling*, [primary journal page](https://doi.org/10.4213/sm9789e) | Extends convergence to the triangular lattice, rather than classifying cubic-lattice peaks. |
| Granin–Kalinin–Saakyan, *Sandpile patterns on a regular graph of degree eight*, Chebyshevskii Sb. 25(3) (2024), 47–69, [journal page](https://www.mathnet.ru/php/archive.phtml?jrnid=cheb&option_lang=eng&paperid=1445&wshow=paper) | Studies the planar graph with eight neighbors, not nearest-neighbor Z³; its pattern results do not settle (4). |
| Kim–Wang, *A stochastic variant of the abelian sandpile model*, J. Stat. Phys. (2019), [1906.01107](https://arxiv.org/abs/1906.01107) | Stochastic topplings and steady states, motivated by lattice reduction. This changes the model, not the deterministic matrix set. |
| Selig–Zhu, *Asymptotics of the single-source stochastic sandpile model*, [2208.10202](https://arxiv.org/abs/2208.10202) | Radius and avalanche asymptotics for a Kim–Wang variant in dimension two. Not a theorem about Γ(Z³). |
| Kalinin–Shkolnikov, *Tropical curves in sandpile models*, [1502.06284](https://arxiv.org/abs/1502.06284), [2026 journal record](https://doi.org/10.1016/j.aim.2026.111127) | Small perturbations of the planar maximal stable state and tropical scaling limits. Not a higher-dimensional quadratic classification. |
| Alevy–Mkrtchyan, *The Limit Shape of the Leaky Abelian Sandpile Model*, [2010.01946](https://arxiv.org/abs/2010.01946) | Shape results for a dissipative modification. The leakage parameter is not the lattice dimension, and the result does not solve the conservative cubic-lattice problem. |

The newer citation records concerning centrally excited walks, rotor walks, comb lattices, internal DLA, divisible sandpiles, activated random walk, and two-dimensional height probabilities did not supply a candidate solution to (4). Author publication lists and searches for “sandpile shapes,” “integer superharmonic matrices” with three/higher dimensions or cubic lattice, and Kim–Wang yielded no additional such theorem. Search-engine indexing dates were not treated as publication dates.

What remains is an intrinsic higher-dimensional description of the admissible set and its maximal elements, including genuinely higher-dimensional distinguished vertices. If the intended question is whether the analogues of the rational circle vertices form an isolated rational family generating the closed set after appropriate limits, that interpretation still needs to be specified and is not settled by this claim or by the literature found here. Isolation of every ordinary maximal element and rationality of every ordinary maximal element, in contrast, are disproved by the construction just checked. This is a valid partial answer to the literal printed problem, with its main relevance being the distinction between residual maxima and circle vertices; it is not a complete resolution of the structural open problem.

All new source files are plain text. PDFs were downloaded only into memory for extraction; none were saved, and no page images or scans were made. Computation used one numerical thread, nice 15, and less than 0.1 GB peak RSS per checking process. Work stayed in this directory; there were no subagents, pushes, or publication.

Task: “Break it if it is wrong.” — received 2026-11-13, approximately 06:51 +04.
