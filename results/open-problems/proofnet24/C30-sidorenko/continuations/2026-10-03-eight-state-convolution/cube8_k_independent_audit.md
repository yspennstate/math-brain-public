# Independent audit: ML10 on all nonnegative eight-state Boolean convolution hosts

2 October 2026. **PASS within the stated host family.** I read the entire stable
proof and every exact generator on which it depends, reconstructed the analytic
argument, and independently regenerated both its chamber coverage and its full
positive polynomial certificate. No mathematical gap was found. This is an
independent agent audit of a finite, reproducible proof, not a certification of
historical novelty or a human peer-review decision.

The audited statement is precisely

\[
G=\mathbf F_2^3,\qquad \mu(x)=1/8,\qquad
W(x,y)=8p_{x+y},\quad p_g\geq0,
\qquad t(\mathrm{ML}_{10},W)\geq\Bigl(\sum_g p_g\Bigr)^{15}.
\]

It permits signed Fourier eigenvalues. It does not prove ML10 Sidorenko for
arbitrary regular eight-state kernels, unequal state measures, larger Boolean
groups, all finite abelian groups, or all graphons. The unrestricted ML10 problem
is not resolved by this audit.

The audited proof is
[`continuation_20261002_cube8_sidorenko_proof.md`](continuation_20261002_cube8_sidorenko_proof.md).
Its SHA-256 at this audit is
`afdf5b08071d973dafe62f6039ab7dc746251a8b19b954efdaa0f892375ba0b4`.
All relevant author and independent inputs are identified by content hashes in
[`cube8_k_independent_audit_manifest.json`](cube8_k_independent_audit_manifest.json).
The author's files were not edited during this audit.

## 1. Source graph and normalization

The source has left and right indices in \(\mathbf Z/5\mathbf Z\), with edges
\(j-i\in\{0,1,-1\}\). It has ten vertices, fifteen edges, is connected and
bipartite, and is the usual ten-vertex Möbius ladder. An explicit isomorphism
to a ten-cycle with five diameter edges sends left vertex \(i\) to
\(4i\pmod {10}\) and right vertex \(j\) to \(4j+5\pmod {10}\).
My independent generator checks this edge-set identity exactly.

Writing \(s=\sum_g p_g\), uniform averaging gives
\(t(K_2,W)=s\). Every Fourier character \(\chi\) is an integral-operator
eigenfunction with eigenvalue \(r_\chi=\sum_g p_g\chi(g)\). In particular the
trivial eigenvalue is \(s\); there is no missing factor of eight.

The root-fixed vertex expansion is also correctly normalized:

\[
F(p)=8^{-10}8^{15}\sum_{x\in G^{10}}\prod_{uv\in E}p_{x_u+x_v}
     =8^6\sum_{x\in G^9\text{ with one label }0}\prod_{uv\in E}p_{x_u+x_v}.
\]

The simultaneous translation \(x_v\mapsto x_v+b\) preserves each edge color
because \(b+b=0\). Its orbits have exactly eight elements and each orbit has
exactly one labeling with the chosen root equal to zero. Consequently the
integer TSV in the vertex generator stores rooted counts, and multiplying by
\(8^6=2^{18}\) gives the normalized density coefficients. The independent
reconstructed host polynomial has coefficient sum
\(8^{15}=35\,184\,372\,088\,832\), as it must when every \(p_g=1\).

## 2. Affine invariance and the averaging lemma

For an invertible linear \(A\) and a vector \(b\), replacing \(p_g\) by
\(p_{Ag+b}\) preserves the density of every bipartite source graph. Relabel
one source part by \(x\mapsto Ax\), and the other by \(y\mapsto Ay+b\).
These are independent measure-preserving bijections and their edge sum is
\(A(x+y)+b\). This is an AGL invariance, not an arbitrary permutation
invariance of the eight host colors. It also preserves \(s\).

After an affine alignment, write \(G=\mathbf F_2\times\mathbf F_2^2\) and
\(p(t,u)=a(u)+(-1)^t b(u)\), with \(a,b\geq0\). In the expansion of an edge
product, choosing its \(b\)-term contributes the sign
\((-1)^{t_x+t_y}\). Independently averaging each source vertex bit annihilates
the term unless every selected-edge degree is even. Thus the complete
expression is a sum over even-degree edge subsets, each having nonnegative
weight

\[
\mathbb E_{u_v}\prod_{xy\in S}8b(u_x+u_y)
                       \prod_{xy\notin S}8a(u_x+u_y).
\]

The empty subset is exactly the density after pair averaging; deleting the
other nonnegative terms proves the needed inequality. This expansion itself
does not require a bipartite source. The affine translation used to obtain
the alignment does require bipartiteness.

The pair-averaged kernel is constant in its first coordinate. Its quotient
has four uniform states and weights \(q_u=p(0,u)+p(1,u)=2a(u)\), because
\(8a(u+v)=4q_{u+v}\). Its edge density is still \(s\). This checks the quotient
normalization, including the multiplicity of the collapsed coordinate.

The qualitative four-state step does not require the earlier quantitative
Klein4 certificate. For two pairs, every orientation function
\(f:\mathbf F_2\to\mathbf F_2\) is affine. The affine shear
\((t,u)\mapsto(t+f(u),u)\) therefore puts the larger element first in both
pairs. Average, then orient the remaining two-state host by a translation
and average it. The final kernel is constant \(s\). This proves the stated
qualitative inequality for any bipartite source on a Klein4 convolution
host. The proof uses nonnegative host weights throughout and makes no
assumption on their Fourier signs.

## 3. Orientation parity and the complete domain coverage

For a nonzero direction \(a\), the chosen transversal is a linear complement
to \(\langle a\rangle\). Its four pair orientations form a function
\(f:\mathbf F_2^2\to\mathbf F_2\). In its unique multilinear expansion

\[
f(u,v)=c+\alpha u+\beta v+\gamma uv,
\]

the XOR of its four values equals \(\gamma\). Thus it is affine exactly when
the pair-orientation parity is even. With strictly distinct weights, this is
equivalent to the sign product \(\epsilon_a=+1\). In that case the affine
shear aligns every pair, so Section 2 covers the whole corresponding order
chamber, rather than just one sample vector.

Two linear transversals differ by a linear function of the quotient variable.
Its truth table has zero or two ones. Translated transversals differ by an
affine function whose table has zero, two or four ones. Hence changing the
representatives flips an even number of signs. Linear changes of coordinates
carry the seven directions bijectively to themselves. These facts justify
using a fixed convenient transversal and later transporting chambers by AGL.

I independently regenerated all strict-order coverage. The author builds
linear maps from their three matrix columns. Instead, my script starts with
all \(8!\) permutations \(A\) and retains precisely those satisfying

\[
A(x+y)=A(x)+A(y)+A(0)\quad\text{for every }x,y\in G.
\]

This condition says that \(A(x)+A(0)\) is linear, and the existing permutation
condition makes it invertible. It therefore generates exactly AGL(3,2), with
1344 elements, without relying on the author's matrix enumeration. For the
sign test I independently choose the numerically smaller member of each
pair, corresponding to a highest-pivot transversal; the author uses a
lowest-pivot transversal.

For all 40320 distinct rank assignments, the counts of positive directions
are exactly

\[
(1344,4032,6720,8064,8064,6720,4032,1344).
\]

The complete set of 1344 assignments with no positive direction, not only its
cardinality, equals the AGL orbit of
\((0,1,2,7,3,6,5,4)\). Since its ranks are distinct, any affine map fixing this
assignment fixes every group element and is the identity; the orbit is
faithful. Its descending color order is
\((3,5,6,7,4,2,1,0)\). There is consequently exactly one remaining chamber
up to the proved density symmetry. No S8 symmetry is used.

The independent coverage code and results are
[`cube8_k_independent_verify.py`](cube8_k_independent_verify.py) and
[`cube8_k_independent_coverage.json`](cube8_k_independent_coverage.json).

## 4. A third entire-density reconstruction

The author's primary density enumerator tests all \(8^9\) rooted labelings.
Its distinct check enumerates all binary even-degree subsets in the source
graph and applies a forward Walsh transform to the vertex polynomial. I
used a further route which does not call either author's generator.

In the ten-cycle-plus-diameters labeling, take the path
\(0,1,\ldots,9\) as spanning tree. Each of the six non-tree edges closes a
fundamental cycle. Their binary masks, with cycle edges first and then
diameters, are

\[
1023,\ 1055,\ 2110,\ 4220,\ 8440,\ 16880.
\]

Each has a different non-tree edge as its only non-tree coordinate, so these
six masks are independent. Every binary circulation is uniquely their XOR:
subtract these cycles to remove every non-tree edge, after which an
even-degree subset of a tree must be empty. The resulting cycle space has
exactly 64 elements. The independent code additionally verifies even degree
at all ten vertices for every resulting mask.

Fourier expansion of \(W\) is
\(W(x,y)=\sum_\chi r_\chi\chi(x)\chi(y)\). Averaging at each source vertex
retains precisely character-valued flows with zero sum there. On
\(\mathbf F_2^3\), these are three independently chosen binary circulations.
I enumerate all \(64^3=262144\) choices from the fundamental-cycle basis,
giving the full 3964-term Fourier polynomial. Every coefficient matches both
the author's flow JSON and the author's complete forward-Walsh TSV.

I then independently substitute \(r=Hp\), where \(H\) is the eight-variable
Hadamard matrix, to reconstruct the entire normalized host polynomial from
the Fourier polynomial. This inverse route starts with the character-flow
counts, not with the rooted-label polynomial. Its butterflies run in the
opposite bit order from the author's forward transform; the signs are
calculated by repeated convolution with \((1,1)\) and \((1,-1)\), rather than
the author's signed-binomial formula. Its exponent packing has five-bit
fields, rather than the author's four-bit fields.

All 89168 resulting density coefficients equal \(8^6\) times the author's
rooted counts, coefficient by coefficient. All are positive and their total
degree is fifteen. This independently establishes the exact density used in
the final chamber calculation. No optimizer, approximate integration or
floating-point operation participates in these comparisons.

The independent flow generator, C++ inverse transform, and records are
[`cube8_k_independent_verify.py`](cube8_k_independent_verify.py),
[`cube8_k_independent_polynomial.cpp`](cube8_k_independent_polynomial.cpp),
[`cube8_k_independent_flow_checks.json`](cube8_k_independent_flow_checks.json), and
[`cube8_k_independent_polynomial_checks.json`](cube8_k_independent_polynomial_checks.json).

## 5. Exceptional-chamber certificate and boundary cases

Let \(o=(3,5,6,7,4,2,1,0)\). The substitution
\(p_{o_i}=d_i+\cdots+d_7\), with \(d_i\geq0\), parametrizes the whole closed
exceptional chamber uniquely. The edge density becomes
\(s=\sum_{i=0}^7(i+1)d_i\). Remapping the independently reconstructed density
by \(o\), then applying the seven shears in increasing index order, gives
exactly this substitution. The order matters: for example the first two
shears turn the first variable into \(d_0+d_1+d_2\), rather than merely
\(d_0+d_1\).

Subtracting the full multinomial expansion of \(s^{15}\) gives the complete
170406-term polynomial \(P=F-s^{15}\), with exactly 367 negative
coefficients. My entire raw polynomial matches the author's JSON. It would
be incorrect to assert coefficient positivity of this raw gap.

For \(L=d_0+\cdots+d_6\), I multiply the independent raw gap directly by

\[
L^2=\sum_{i=0}^6d_i^2+2\sum_{0\leq i<j\leq6}d_id_j.
\]

This is different from the author's two successive \(L\)-multiplications.
All 345312 nonzero coefficients of the resulting homogeneous degree-17
polynomial are strictly positive. Every one matches both the Python
certificate and the separate author's C++ regeneration. The minimum and
maximum are respectively

\[
262143,\qquad 166970267349065400320.
\]

The seven pure coefficients \([d_i^{17}]L^2P\), \(0\leq i\leq6\), are

\[
(262143,134184960,1134628245,3221225472,
60175070835,118091317248,72749439945).
\]

Consequently \(L^2P\geq0\) throughout the nonnegative orthant. When \(L>0\),
division proves \(P\geq0\); indeed one of these pure terms makes \(P>0\).
When \(L=0\), every \(p_g=d_7\), so \(F=(8d_7)^{15}=s^{15}\) directly.
There is no division at this boundary. The distinction between \(d_7\) and
the seven genuine order gaps is handled correctly.

The union of the smoothing chambers and the exceptional affine orbit covers
every strictly ordered nonnegative vector. Every nonnegative vector,
including all ties and zeros, is a limit of positive strictly ordered
vectors. Polynomial continuity proves the desired inequality at all those
boundaries. This last step proves non-strict inequality globally; the
exceptional-chamber strictness is not a global equality classification.

## 6. Static arithmetic and code audit

I read the complete coverage, rooted-label, forward-Walsh, Fourier-flow,
chamber, Python multiplier and C++ multiplier generators. Their loops,
graph edges, exponent remapping, multinomial coefficients and normalizations
agree with the formulas above. The full polynomial comparisons, rather than
only stored term counts or extrema, were checked again by my independent
code. The flow file's subsequent numerical searches are excluded from the
proof.

There is sufficient room in all fixed-width representations:

- Rooted counts sum to \(8^9=2^{27}\). Fifteen-edge exponents fit four-bit
  fields without carrying between packed coordinates.
- During the author's forward Walsh substitution, the total absolute mass
  of fully expanded coefficients is at most
  \(8^{15}\cdot8^{15}=2^{90}\). This bounds partial accumulations as well.
- My inverse Walsh route starts with total mass \(2^{18}\), hence its
  intermediate absolute-mass bound is \(2^{18}8^{15}=2^{63}\).
- The ordered substitution has absolute mass at most \(2^{90}\); the
  subtracted mean expansion has mass \(36^{15}\). Multiplication by \(L^2\)
  costs at most a factor \(49\). Therefore all relevant signed arithmetic is
  bounded by \(49(2^{90}+36^{15})<10^{30}<2^{127}\), safely within signed
  128-bit integers. No overflow is used as part of a certificate.
- In the multinomial routine the product of partial factorial denominators
  is at most \(15!\); the binomial tables have degree at most fifteen.
  These unsigned and ordinary integer intermediates are safe too.
- Author multiplier fields have six bits and my fields five bits; degree
  seventeen fits both. Direct exponent shifts cannot carry into adjacent
  fields.

The compiled independent regenerator exited zero. Reproducible commands from
the research-directory parent are:

```bash
python sidorenko_attempt/cube8_k_independent_verify.py generate
g++ -O3 -std=c++17 sidorenko_attempt/cube8_k_independent_polynomial.cpp -o sidorenko_attempt/cube8_k_independent_polynomial
sidorenko_attempt/cube8_k_independent_polynomial sidorenko_attempt/cube8_k_independent_flow.tsv sidorenko_attempt/cube8_k_independent
python sidorenko_attempt/cube8_k_independent_verify.py compare
```

The comparisons reported PASS for the entire Fourier, host-weight, raw-gap,
and multiplier coefficient maps. The generated TSV files are reproducible
intermediate artifacts; the source and compact JSON records identify the
verification route explicitly.

## 7. Prior-art and scope check

I reopened the primary September 2025 Fox–Himwich–Mani–Zhou article,
*A note on directed analogues of the Sidorenko and forcing conjectures*,
EJC 32(3), #P3.38, DOI
[10.37236/11675](https://doi.org/10.37236/11675). Its introduction identifies
the ten-vertex Möbius ladder, also described as \(K_{5,5}\) minus a ten-cycle,
as a small open case of unrestricted Sidorenko. This supports the source
problem's importance; it does not itself claim that the present restricted
host theorem was previously unknown.

Yuqi Zhao's July 2025 primary preprint
[*Sidorenko-Type Inequalities for Even Subdivisions over Finite Abelian Groups*](https://arxiv.org/abs/2507.15723)
concerns sources obtained by replacing each edge with an even-length path in
abelian Cayley hosts. ML10 has degree three at all ten vertices and has no
degree-two subdivision vertices, so that source theorem does not apply.

I also reopened Zhao's June 2026 primary preprint
[*Sidorenko Inequalities for Two-Sided Group Correlation Kernels*](https://arxiv.org/pdf/2606.23018).
Its Theorem 1.1 concerns kernels
\(C_f(x,y)=\mathbb E_z f(x^{-1}z)f(zy^{-1})\). On the present Boolean group,
these have nonnegative Fourier eigenvalues \(\widehat f(\chi)^2\), unlike an
arbitrary nonnegative \(p\). Its equivalent product-Cayley statement concerns
directed 1-subdivisions, which again does not turn ML10 into a subdivision.
For an explicit spectral distinction, take \(p_0=0\) and \(p_g=1\) for
\(g\ne0\): all seven nontrivial Fourier eigenvalues are \(-1\). A translation
cannot make all of them nonnegative, because the product of their translation
signs is \(+1\), whereas the original seven signs have product \(-1\).

The elementary averaging argument, character-flow identity, and positive
multiplier method should not be individually represented as invented here.
The finite complete coefficient identity and full order-coverage calculation
do establish this particular restricted statement mathematically. A bounded
primary-source check is insufficient to certify its historical novelty.
Human review and a broader literature check remain appropriate before any
publication claim. No implication to the full ML10 graphon conjecture has
been used anywhere in this audit.

**Verdict:** the analytic reduction and the exact finite certificate jointly
prove the displayed eight-state Boolean convolution theorem. All mathematical
and computational obligations of that restricted claim passed this independent
audit; novelty and unrestricted generalization remain unasserted.
