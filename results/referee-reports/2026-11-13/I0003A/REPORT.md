PARTIAL

# I0003: recurrence, transience, and what partial-sum growth misses

The full characterization in Bou-Rabee–Peres, Section 7, Problem 3, remains
unsettled by this work. The results below give a deterministic recurrence
criterion, a classification of all fields eventually constant in their four tails,
and a larger mixed random/balanced class. They also disprove a classification
based only on the magnitudes of the two partial sums.

Throughout, “recurrent” means recurrence of every starting site, equivalently
infinite diagonal Green functions. For a reducible field, “transient” means finite
diagonal Green functions at every site.

## Statements

Normalize the two-sided primitives by

\[
 S(0)=T(0)=0,\qquad S(k)-S(k-1)=e_k,\quad T(k)-T(k-1)=f_k,
 \qquad k\in\mathbb Z.
\]

Thus, for example, \(S(n)=\sum_{k=1}^n e_k\) for positive \(n\), and
\(S(-n)=-\sum_{k=-n+1}^{0}e_k\). Bounds below concern both tails. Define

\[
 M(r)^2=\max_{|k|\le r}|S(k)|^2+\max_{|k|\le r}|T(k)|^2.
\]

**A. Bounded primitive changes preserve type.** Suppose two fields satisfy

\[
 \sup_{k\in\mathbb Z}|S(k)-\widetilde S(k)|+
 \sup_{k\in\mathbb Z}|T(k)-\widetilde T(k)|<\infty.
 \tag{A}
\]

Their diagonal Green functions are finite at exactly the same sites. In
particular, changing the orientations of finitely many whole lines preserves type.
There is a uniform multiplicative comparison of their diagonal resolvents.

**B. A deterministic recurrence criterion.** Every field satisfying

\[
 \sum_{m=1}^{\infty}\frac{1}{1+M(2^m)^2}=\infty
 \tag{B}
\]

is recurrent. In particular, this holds if both primitives are bounded, or if

\[
 |S(k)|+|T(k)|=O\bigl(\sqrt{\log(2+|k|)}\bigr).
 \tag{B1}
\]

More generally the displayed logarithmic bound can be replaced by
\(O((\log(2+|k|))^c)\) with \(c\le 1/2\). The value \(1/2\) is a
sufficient logarithmic exponent from this proof, not a proved sharp boundary.
A necessary condition for transience is the convergence of the series in (B).
Its convergence is not sufficient.

**C. Complete classification for eventually constant tails.** Suppose
\(e_y=e_+\) for all sufficiently large positive \(y\),
\(e_y=e_-\) for all sufficiently negative \(y\), and similarly
\(f_x=f_+\), respectively \(f_-\), on the two tails. Then the walk is
recurrent if and only if

\[
 e_-=-e_+,\qquad f_-=-f_+,\qquad e_+f_+=-1.
 \tag{C}
\]

All other such fields are transient. Thus the two circulating tail arrangements
are recurrent; the other fourteen choices of four tail signs are transient.
Finite arbitrary configurations of lines between the tails do not affect this test.

For the explicit recurrent and transient pair, put \(g(k)=1\) for \(k\ge0\)
and \(g(k)=-1\) for \(k<0\). Then

\[
 (e_y,f_x)=(g(y),-g(x))\quad\hbox{is recurrent},\qquad
 (e_y,f_x)=(g(y),g(x))\quad\hbox{is transient}.
 \tag{C1}
\]

The two fields have exactly the same functions \(|S(k)|\) and \(|T(k)|\).
In each tail these are asymptotic to \(|k|\). Consequently even pointwise
lower bounds larger than \(n^{1/2}\) in both directions do not imply transience
for arbitrary deterministic fields. Any criterion using only these absolute
primitive sequences, including their exponents, necessarily loses information.

**D. Mixed random/balanced fields.** If \((e_y)\) is iid symmetric signs, then
on a single event of probability one, the walk is transient for every vertical
field \((f_x)\) with bounded two-sided primitive. The same holds after interchanging
horizontal and vertical. This extends the alternating/random case already proved
by Bosi, Theorem 9(i), using A.

**E. The sharp universal polynomial upper-bound statement.** For \(a,b\ge0\),
consider the class of fields with \(S(k)=O(|k|^a)\), \(T(k)=O(|k|^b)\)
on both tails. Every member is recurrent if and only if \(a=b=0\).
For every other pair the class contains both recurrent and transient fields.
This is a statement about upper-bound classes, not an exact-power phase diagram.
The transient examples follow from Bosi's sparse random perturbations and an
elementary maximal inequality, as shown below.

A–C are proved here directly. Their tools are standard nonreversible potential
theory; the bounded-stream predecessor is Gaudillière–Landim, Lemma 5.5.
I did not locate the unbounded criterion (B), the tail classification (C), or
extension (D) stated in the reviewed sources. This is not a claim of exhaustive
priority verification. The original problem, general two-frequency rotation
fields, and a classification with specified exact sublinear power asymptotics
remain open in this report.

## Proof

### 1. The resolvent test

Use continuous time with rate one along each of the two outgoing edges. This
has the same recurrence type as the discrete walk. On real \(\ell^2(\mathbb Z^2)\),
its bounded generator is \(L=\mathcal S+A\), where

\[
 \begin{split}
 \mathcal S u(z)&=\tfrac12\sum_{i=1}^2
       [u(z+\mathbf e_i)+u(z-\mathbf e_i)-2u(z)],\\
 Au(x,y)&=\tfrac12e_y[u(x+1,y)-u(x-1,y)]
          +\tfrac12f_x[u(x,y+1)-u(x,y-1)].
 \end{split}
\]

The symmetric part \(\mathcal S\) is the same for every field, and \(A^*=-A\).
The latter uses precisely that each orientation is constant along its own line.
Counting measure is invariant. Write

\[
 \mathcal E(u)=\langle u,-\mathcal S u\rangle
       =\tfrac12\sum_{\{z,w\}:|z-w|=1}(u(w)-u(z))^2.
\]

For \(\lambda>0\), set \(H_\lambda=\lambda I-\mathcal S\), and

\[
 Q_{A,\lambda}(u)=\langle u,H_\lambda u\rangle
          +\langle Au,H_\lambda^{-1}Au\rangle.
\]

The symmetric part of the inverse satisfies

\[
 \tfrac12\bigl[(H_\lambda-A)^{-1}+(H_\lambda+A)^{-1}\bigr]
   =(H_\lambda-AH_\lambda^{-1}A)^{-1}.
 \tag{1}
\]

To verify this, conjugate by \(H_\lambda^{1/2}\). With
\(B=H_\lambda^{-1/2}AH_\lambda^{-1/2}\), \(B^*=-B\), and the symmetric
part of \((I-B)^{-1}\) is \((I-B^2)^{-1}\). All operators here are bounded;
\(H_\lambda\ge\lambda I\) makes the inverses legitimate.

The quadratic variational formula for a positive inverse now gives

\[
 G_{A,\lambda}(o,o)
  =\sup_{u\in\ell^2}\{2u(o)-Q_{A,\lambda}(u)\}.
 \tag{2}
\]

Optimizing only over scalar multiples of a fixed finitely supported \(u\) gives

\[
 G_{A,\lambda}(o,o)\ge
       \frac{u(o)^2}{Q_{A,\lambda}(u)}.
 \tag{3}
\]

In particular, if \(u_N(o)=1\), the supports are finite, and
\(\mathcal E(u_N)+\langle Au_N,H_\lambda^{-1}Au_N\rangle\)
tends to zero uniformly in \(\lambda>0\), then first choosing \(N\), then
\(\lambda\) small enough that \(\lambda\|u_N\|_2^2\) is negligible proves
\(G_{A,\lambda}(o,o)\to\infty\). Monotone convergence applies to its
nonnegative transition-kernel integral. Finally, Poissonization gives

\[
 \int_0^\infty p_t(o,o)\,dt=\tfrac12\sum_{n\ge0}p_n(o,o).
 \tag{4}
\]

This argument does not require irreducibility.

### 2. Face streams and their energy bound

Index a unit face by its lower-left vertex \((x,y)\), and put

\[
 h(x,y)=\tfrac12[S(y)-T(x)].
\]

The antisymmetric rate on the positively directed horizontal edge at height \(y\)
is \(e_y/2=h(x,y)-h(x,y-1)\). On the positive vertical edge at column \(x\)
it is \(f_x/2=h(x-1,y)-h(x,y)\). Thus these rates are the discrete curl of \(h\).

For a face with counterclockwise vertices \(z_0,z_1,z_2,z_3\), define

\[
 E_q(u)=\sum_{i=0}^3(u(z_{i+1})-u(z_i))^2,
 \qquad W_h(u)=\sum_qh(q)^2E_q(u),
\]

with indices modulo four. Summing edge terms face by face gives

\[
 \langle u,Av\rangle
   =\sum_q h(q)\sum_i[u(z_i)v(z_{i+1})-u(z_{i+1})v(z_i)].
 \tag{5}
\]

The inner sum equals

\[
 (u_0-u_2)(v_1-v_3)-(u_1-u_3)(v_0-v_2).
\]

Its absolute value is at most \(2\sqrt{E_q(u)E_q(v)}\), by
Cauchy–Schwarz and the two-edge paths across each diagonal. Every undirected
edge belongs to two faces, so \(\sum_qE_q(v)=4\mathcal E(v)\). Therefore

\[
 |\langle u,Av\rangle|
       \le4\sqrt{W_h(u)\mathcal E(v)}.
 \tag{6}
\]

For finitely supported \(u\), all stream-weighted terms are finite even if
\(h\) is unbounded. Approximation extends the bound from finitely supported
\(v\) to \(\ell^2\). By the dual formula for the inverse quadratic form,

\[
 \langle Au,H_\lambda^{-1}Au\rangle
       \le16W_h(u),\qquad \lambda>0.
 \tag{7}
\]

Indeed, \(\langle v,H_\lambda v\rangle\ge\mathcal E(v)\) and optimization
of \(2\langle Au,v\rangle-\langle v,H_\lambda v\rangle\) gives (7).
The constants are deliberately nonoptimal.

### 3. Proof of A

Write \(\widetilde A=A+D\). Under (A), the face stream \(h_D\) of \(D\)
is bounded. Since \(W_{h_D}(u)\le4\|h_D\|_\infty^2\mathcal E(u)\), (7) yields

\[
 \|Du\|_{-1,\lambda}^2\le K\mathcal E(u),\qquad
 K=64\|h_D\|_\infty^2,
\]

where \(\|w\|_{-1,\lambda}^2=\langle w,H_\lambda^{-1}w\rangle\).
Using the squared triangle inequality and then reversing the roles of the fields,

\[
 C^{-1}Q_{A,\lambda}(u)\le Q_{\widetilde A,\lambda}(u)
       \le C Q_{A,\lambda}(u),\qquad C=2+2K.
 \tag{8}
\]

The bounds hold first on a dense core, then on all \(\ell^2\), uniformly in
\(\lambda\). Formula (2), with scalar rescaling, implies

\[
 C^{-1}G_{A,\lambda}(o,o)\le G_{\widetilde A,\lambda}(o,o)
       \le C G_{A,\lambda}(o,o).
 \tag{9}
\]

Taking \(\lambda\downarrow0\) proves A at every site. Finite line flips change
the primitives by bounded amounts, so they are included. No irreducibility or
stationary environmental law is needed.

### 4. Proof of B

Let \(r(z)=\|z\|_\infty\). Take \(u_N=1\) for \(r\le1\); on each annulus
\(2^m\le r\le2^{m+1}\), \(0\le m\le N\), decrease it linearly in \(r\)
by a nonnegative amount \(d_m\); set it to zero beyond \(2^{N+1}\).
Require \(\sum_{m=0}^Nd_m=1\).

There are \(O(2^{2m})\) edges in such an annulus, with squared gradients at
most \(d_m^2/2^{2m}\). Every incident face has its coordinates in a box of
radius \(2^{m+3}\), and \(h(q)^2\le M(2^{m+3})^2/2\). Accounting for
boundary faces and both incident annuli gives the explicit form of the bound

\[
 \mathcal E(u_N)+16W_h(u_N)
     \le C_0\sum_{m=0}^N[1+M(2^{m+3})^2]d_m^2,
 \tag{10}
\]

for an absolute finite \(C_0\) (for instance 4096). One can obtain (10) directly by assigning each
edge to the annulus of its smaller endpoint radius: the two radii differ by at
most one; \(u_N\) is constant at any common radial boundary; each edge has two
incident faces. Thus there is no omitted boundary contribution.

Put \(w_m=1+M(2^{m+3})^2\),
\(D_N=\sum_{m=0}^Nw_m^{-1}\), and \(d_m=w_m^{-1}/D_N\).
The right side of (10) is \(C_0/D_N\). Removing finitely many terms and shifting
the dyadic index do not change divergence of (B), so \(D_N\to\infty\).
Equations (3), (7) prove recurrence at the origin.

The same cutoffs equal one at any fixed site once the inner radius is enlarged;
alternatively translate the origin. For a fixed shift the new normalized
primitives differ from the original shifted ones by constants, and their envelopes
are bounded by \(M(r+c)+C_c\). Since \(r+c\le2r\) eventually, (B) still
holds. Hence every site is recurrent.

For (B1), \(M(2^m)^2=O(m)\), leaving a divergent harmonic series. Bounded
primitives leave a series bounded below by a positive constant. The necessary
condition for transience is the contrapositive of B.

There are aperiodic examples with unbounded primitives in this theorem. On
positive indices pair the signs as \((e_{2k-1},e_{2k})=(+1,-1)\), except replace
them by \((+1,+1)\) at \(k=2^{m^2}\), \(m\ge1\). Keep alternating signs on
nonpositive indices. Then \(S(2K)=2\#\{m:2^{m^2}\le K\}\), so
\(M_S(r)=O(\sqrt{\log(2+r)})\), and it is unbounded. Do the same for \(f\),
for example at \(k=2^{2m^2}\). Both primitives are unbounded; B proves recurrence.

### 5. The circulating field and proof of C

First take \(e_y=g(y)\), \(f_x=-g(x)\). The useful radius is

\[
 R(x,y)=|x+1/2|+|y+1/2|\in\{1,2,\ldots\}.
\]

For a finitely supported radial profile \(u(x,y)=\phi(R(x,y))\), set
\(a_r=\phi(r+1)-\phi(r)\). There are \(8r\) undirected lattice edges between
levels \(r\) and \(r+1\). Edges within a level contribute zero. Consequently

\[
 \mathcal E(u)=4\sum_{r\ge1}r a_r^2.
 \tag{11}
\]

Away from the two pairs of central coordinate lines, the two central differences
in \(Au\) cancel. On each level \(r\ge2\), it is a sum of the following four
adjacent dipoles, each with coefficient \(a_{r-1}/2\):

\[
 \begin{split}
 Au={}&\tfrac12\sum_{r\ge2}a_{r-1}\big[
  (\delta_{(r-1,0)}-\delta_{(r-1,-1)})
 +(\delta_{(-r,-1)}-\delta_{(-r,0)})\\
 &\hspace{41mm}
 +(\delta_{(-1,r-1)}-\delta_{(0,r-1)})
 +(\delta_{(0,-r)}-\delta_{(-1,-r)})\big].
 \end{split}
 \tag{12}
\]

At the four sites of level one it is zero. Formula (12) follows by substitution
in \(A\); for instance at \((r-1,0)\), twice \(Au\) equals
\((\phi(r+1)-\phi(r-1))-(\phi(r+1)-\phi(r))=a_{r-1}\).
The four supporting edges per level, and those for different levels, are distinct.
Thus Cauchy–Schwarz on these edges gives

\[
 |\langle Au,v\rangle|^2
    \le2\Bigl(\sum_{r\ge1}a_r^2\Bigr)\mathcal E(v),
 \quad
 \langle Au,H_\lambda^{-1}Au\rangle\le2\sum_{r\ge1}a_r^2.
 \tag{13}
\]

Let \(h_N=\sum_{r=1}^N1/r\). Choose \(\phi_N(1)=1\),
\(a_r=-1/(r h_N)\) for \(1\le r\le N\), and zero thereafter.
Then \(\phi_N\) is zero from level \(N+1\) onward and

\[
 \mathcal E(u_N)=4/h_N,\qquad
 \langle Au_N,H_\lambda^{-1}Au_N\rangle
     \le\frac{\pi^2}{3h_N^2}.
 \tag{14}
\]

The resolvent test proves recurrence at \((0,0)\). This field is irreducible:
each allowed edge lies on an oriented rectangle whose opposite sides straddle
both central coordinate lines. Because the underlying undirected lattice is
connected, the directed rectangles allow every edge to be traversed in reverse
by an allowed path. Thus all sites are recurrent. The opposite circulation is
its image under the reflection \(x\mapsto-1-x\), and has the same type.

For the saddle \(e_y=g(y)\), \(f_x=g(x)\), the quadrants
\(\{x,y\ge0\}\) and \(\{x,y<0\}\) are closed and point outward.
Inside either, \(x+y\), respectively \(-(x+y)\), increases by one every step.
In either remaining quadrant, the steps reduce the finite distance to one of
these two closed quadrants by one each time. Every start therefore reaches an
outward quadrant in a deterministically bounded number of steps and cannot
return indefinitely. The reflected saddle with both signs reversed is likewise
transient.

If either orientation sequence is constant, its coordinate is monotone and
cannot participate in any positive-time return: after only moves in the other
coordinate, that coordinate moves monotonically too until the first move in the
constant direction. Hence every positive-time return probability is zero.

For an eventually constant field, replace the finite intermediate sets of lines
by a constant or a single-sign-change sequence with the same tails. The
classification just proved and A give exactly (C).

For the two fields in (C1), the primitive of \(g\) is
\(S(n)=n\) for \(n\ge0\), \(S(-n)=n-2\) for \(n\ge1\).
Their vertical primitives are respectively \(-S\) and \(S\). Absolute values
therefore agree exactly, including on the negative tail. This proves the
magnitude counterexample, and also proves that convergence in (B) is not sufficient
for transience.

### 6. Mixed fields and the polynomial obstruction

Bosi's Theorem 9(i) gives a probability-one set of horizontal iid fields transient
when \(f_x=(-1)^x\). For any other \(f\) with bounded primitive, the primitive
difference from this alternating field is bounded. Apply A separately to each
field in that same probability-one set. There is no uncountable intersection of
probability-one events: A applies deterministically to every bounded perturbation.
This proves D.

For E, use Bosi's Theorem 9(iii) with alternating vertical orientations and

\[
 e_y=(1-\lambda_y)(-1)^y+\lambda_y\xi_y,
 \qquad \mathbb P(\lambda_y=1)=p_y\asymp |y|^{-\beta},\quad 0<\beta<1,
 \tag{15}
\]

where the replacements and the symmetric signs are independent. Take \(p_y\)
monotone on each tail, with the power formula outside a finite set. The mean
partial sums are bounded by the alternating-series test. The variance of each
centered increment is at most \(2p_y\), giving cumulative variance
\(O(N^{1-\beta})\). Kolmogorov's maximal inequality yields

\[
 \mathbb P\!\left(\max_{k\le2^m}
    \left|\sum_{y=1}^k(e_y-\mathbb E e_y)\right|>2^{ma}\right)
 \le C2^{m(1-\beta-2a)}.
 \tag{16}
\]

For any given \(a>0\), choose \(\max(0,1-2a)<\beta<1\). The right side is
summable. Borel–Cantelli, on both tails, proves \(M_S(r)=O(r^a)\) almost surely,
while the mixed walk is transient almost surely by Bosi. Fix any realization
in the intersection to obtain a deterministic example; existence, rather than a
computable selected realization, is what this argument supplies. The other
primitive is bounded. Interchange coordinates to treat \(b>0\).
Bounded primitives give recurrence by B; alternating/alternating fields belong
to every nonnegative upper-bound class. This proves E.

For iid signs, a pointwise eventual bound \(|S(n)|\ge c\sqrt n\) is not a
property of typical environments: the one-dimensional sign sum returns to zero
infinitely often. Variance, typical fluctuations, a maximal envelope, and an
eventual lower bound are different hypotheses. No necessary-and-sufficient
criterion based on an unspecified notion of “grows like” has been asserted.

### 7. All periodic fields

If \(e\) has period \(p\) and \(f\) period \(q\), the walk is recurrent if
and only if \(\sum_{y=0}^{p-1}e_y=\sum_{x=0}^{q-1}f_x=0\).
Sufficiency follows from B. For necessity, project onto
\((\mathbb Z/q\mathbb Z)\times(\mathbb Z/p\mathbb Z)\). Its transition matrix
is irreducible: a directed horizontal row cycle reaches any column, then a directed
vertical column cycle reaches any row. Each site has two incoming and two outgoing
edges, counting multiplicity, so the invariant law is uniform. The ergodic theorem
for this finite chain, together with the strong law for bounded martingale
increments, gives

\[
 \frac{(X_n,Y_n)}{n}\longrightarrow
 \left(\frac{1}{2p}\sum_{y=0}^{p-1}e_y,
       \frac{1}{2q}\sum_{x=0}^{q-1}f_x\right)\quad\hbox{almost surely}.
\]

A nonzero limiting velocity implies transience. This finite-state argument is
standard; no novelty is claimed for the periodic classification.

## Literature audit

Searches and source retrieval were performed on 13 November 2026. A negative
literature search is not a proof that no prior theorem exists. I found no full
characterization of the coupled Manhattan model. The distinctions in the last
column matter: several complete classifications concern a different model.

All cited PDF page numbers below refer to the exact plaintext copies in
`sources/`, which contain `===== PDF PAGE n =====` markers. Printed page numbers
are included when checked. No PDF, page image, or scan was retained.

| Source and locator | What was checked | Relation to I0003 |
| --- | --- | --- |
| [Bou-Rabee–Peres, arXiv:2609.07621v1](https://arxiv.org/abs/2609.07621), Theorems 1.1–1.2, printed/PDF p.2; §1.4 pp.4–5; Proposition 6.2 and Problem 3 p.14 | iid fair orientations in both directions give almost-sure transience and a finite annealed continuous-time Green function. Proposition 6.2 gives a uniform continuous-time kernel upper bound \(2/(t+2)\), which alone is not summable. | Exactly the present model. Problem 3 remains a characterization question. Its related irrational-rotation paragraph concerns the partially oriented model and must be read with Brémont's earlier results below. |
| [Bosi, thesis (2019)](https://amsdottorato.unibo.it/id/eprint/8914/), Appendix A, Theorem 9(i)–(iii), printed/PDF pp.72–73; perturbation definition (2.12)–(2.13), p.40 | One direction alternates. Opposite iid signs give transience; zero-mean periodic orientations give recurrence; random replacements of a zero-mean periodic field with probability \(c|y|^{-\beta}\) give transience for \(\beta<1\), recurrence for \(\beta>1\). | Exactly the coupled Manhattan walk. The exponent here describes defect probabilities, not primitive growth. Equality \(\beta=1\) is not covered by that theorem. |
| [Beaton–Holmes (2023)](https://researchers.ms.unimelb.edu.au/~mholmes1%40unimelb/Manhattan_short.pdf), author manuscript, Theorem 1 and unnumbered following discussion, PDF p.2 | Alternating orientations in both directions: \(\lfloor X_{2n}/2\rfloor\) is planar simple random walk; recurrence is attributed to Guillotin-Plantard. Theorem 1 gives exact mean and mean-square displacement formulas. | Exactly the alternating Manhattan field; the recurrence observation is not a separately numbered theorem in this paper. |
| [Campanino–Petritis (2003), arXiv:math/0111305v1](https://arxiv.org/abs/math/0111305), Theorems 1.6, 1.7, 1.8, PDF p.5 | Alternating horizontal orientations recurrent; half-plane orientations transient; iid horizontal signs almost surely transient. Journal: *Markov Processes Related Fields* 9, 391–412. | Vertical edges are bidirectional; three possible moves. These results do not transfer automatically to two oriented axes. |
| [Guillotin-Plantard–Le Ny, *Transient random walks on 2d-oriented lattices*](https://web.ma.utexas.edu/mp_arc/c/06/06-4.pdf), Theorem 1, PDF p.4, hypothesis (2.3); rotation discussion pp.13–14 | Dynamically generated orientation probabilities with mean \(1/2\) and \(\int [f(1-f)]^{-1/2}\,d\mu<\infty\) give almost-sure transience. Deterministic half-circle indicators fail that integrability hypothesis. | Partially oriented model, not a theorem for a deterministic rotation field in the coupled Manhattan model. Published English version: *Theory Probab. Appl.* 52 (2008), 699–711. |
| [Guillotin-Plantard–Le Ny (2008), *A functional limit theorem for a 2d-random walk with dependent marginals*](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/1386/1709.pdf), Theorem 2, printed p.339 / PDF p.3 | Joint functional limit with horizontal scale \(n^{3/4}\), vertical scale \(n^{1/2}\); limiting coordinates are dependent. | Partially oriented model. A functional limit is not a return-probability estimate. |
| [Castell–Guillotin-Plantard–Pène–Schapira (2011)](https://math.univ-lyon1.fr/~guillotin/AOP606.pdf), Theorem 20 and Remarks 21–22, printed p.2106 / PDF p.28 | Lattice return local limit with the required arithmetic assumptions; for the Campanino–Petritis model the even-time return probability has order \(n^{-5/4}\). | Partially oriented model. This is a summable Green-function estimate, but its independent skeleton assumption is unavailable for two mutually driven coordinates. |
| [Pène (2009)](https://www.numdam.org/item/10.1051/ps%3A2008019.pdf), Theorem 1, p.418 / PDF p.2; Theorem 2, p.419 / PDF p.3 | Transience under explicit stationary decorrelation hypotheses; Theorem 2 gives sufficient \(\alpha\)-mixing assumptions, including \(\sup n^6\alpha_n<\infty\). | Partially oriented model; stationarity and centering alone are not the theorem's assumptions. |
| [Devulder–Pène, arXiv:1110.4865v2](https://arxiv.org/abs/1110.4865), Theorem 1, PDF p.2; Theorem 2 pp.3–4 | For nonconstant iid horizontal-stay probabilities \(p_k\) with \(\mathbb E(1-p_0)^{-\alpha}<\infty\), some \(\alpha>1\), transience holds for any fixed orientation sequence. Further assumptions give functional limits. | Both vertical directions are available; stay probabilities vary by layer. It does not imply that every deterministic Manhattan field is transient. |
| [Campanino–Petritis (2014), arXiv:1204.5297](https://arxiv.org/abs/1204.5297), Theorem 1.5 and Proposition 1.8, PDF p.4 | Sparse random defects of zero-mean periodic orientations: transient below defect exponent 1, recurrent above; finite deterministic defects preserve recurrence. | Partially oriented model. Bosi 9(iii), rather than this theorem alone, is the relevant mixed Manhattan version. |
| [Brémont (2017), published version](https://alea.impa.br/articles/v14/14-36.pdf), Theorem 2.4 p.754 / PDF p.4; Proposition 7.1 p.790 / PDF p.40 | A full recurrence criterion in directional flux-variance functions for the stratified model. Proposition 7.1 proves the half-circle rotation orientation recurrent for Lebesgue-a.e. angle. | This settles the a.e.-angle version of the source paper's related partially oriented example, not Problem 3's coupled model. |
| [Brémont, *Planar random walk in a stratified quasi-periodic environment*, arXiv:2007.01573v2](https://arxiv.org/abs/2007.01573), Proposition 3.1 and Theorem 3.2, PDF p.4; Proposition 3.3 p.5 | Periodic drift criterion; a continued-fraction sufficient recurrence condition for centered piecewise Lipschitz observables; exceptional super-approximable angles giving transience for a.e. phase. Published in *MPRF* 27 (2021), 755–788. | Again stratified. The exact conditions are recorded immediately below. |
| [Brémont, *Random walk in a stratified independent random environment*, arXiv:1811.07562v1](https://arxiv.org/abs/1811.07562), Theorem 1.3, PDF p.3 | In a centered nonconstant iid vertical random environment, the critical local horizontal drift scale is roughly \(\exp(-\sqrt{|n|})\), with explicit exponent margins in the theorem. Published *ECP* 24 (2019), no.47. | Vertical skeleton is a Sinai-type walk; neither these scales nor its criterion can be substituted into the Manhattan model. |
| [Gaudillière–Landim, arXiv:1111.2445v1](https://arxiv.org/abs/1111.2445), Theorem 2.4 PDF p.5; Lemma 5.5 pp.25–26 | Nonreversible Dirichlet principle; recurrence of planar asymmetric networks under a uniform second-moment bound on the face-stream weights relative to symmetric conductance. Published *PTRF* 158 (2014), 55–89. | Bounded deterministic streams satisfy the lemma directly. Criterion B explicitly extends the cutoff estimate to a class of unbounded deterministic streams. The method itself is established literature. |
| [Ledger–Tóth–Valkó (2018), arXiv:1802.01558v2](https://arxiv.org/abs/1802.01558), Theorem 1.1, PDF p.2 | Mean-square-displacement Laplace bounds in dimensions two and three; the bounds are explicitly time-averaged. | Exactly the iid Manhattan model, but displacement bounds do not decide recurrence. |
| [Nguyen (2026), arXiv:2608.21701](https://arxiv.org/abs/2608.21701), Theorem 1.1, PDF p.3 | Three-dimensional iid Manhattan mean-square-displacement Laplace transform has \(\lambda^{-2}\sqrt{|\log\lambda|}\) growth up to specified log-log factors. | Dimension three and a displacement estimate; no two-dimensional orientation classification. |
| [Guillotin-Plantard–Pène–Watbled (2025), arXiv:2504.08485v2](https://arxiv.org/abs/2504.08485), Theorem 1.1, PDF p.3 | Joint functional limit for a three-dimensional iterated-scenery model, with scales \(n^{1/2},n^{3/4},n^{5/8}\). | A different three-dimensional model; it does not decouple the two-dimensional Manhattan walk. |

For Brémont's Theorem 3.2, write the rotation angle
\(\theta=[0;a_1,a_2,\ldots]\). Its recurrence condition is

\[
 \sum_{n\ge1}\frac{\log(1+a_n)}{a_1+\cdots+a_n}=\infty.
\]

Under the paper's uniform transition hypotheses, with symmetric vertical
probabilities and centered piecewise Lipschitz weighted horizontal drift
\(F(x+n\theta)\), recurrence follows for every phase \(x\). The condition
holds for almost every angle. Proposition 3.3 instead assumes \(a_1\) odd,
\(a_n\) even for \(n\ge2\), and \(a_{n+1}\ge a_n^\delta\) eventually for
some \(\delta>1\). For the half-circle observable it gives transience for
almost every phase. It does not assert transience at phase zero for each such
angle. Thus “all irrational rotations recurrent” is not what this literature says.

Additional 2025–2026 screening: [Armstrong–Bou-Rabee–Kuusi,
arXiv:2601.22142](https://arxiv.org/abs/2601.22142) concerns continuum incompressible
flows in a perturbative small-Hurst-exponent regime (Theorem A, PDF p.5); [Gu–Hao,
arXiv:2609.19498](https://arxiv.org/abs/2609.19498) concerns deterministic mirror
trajectories on the alternating Manhattan lattice (Theorems 1.1–1.2, PDF p.2). Their models and conclusions
do not furnish the requested classification. The latter distinction is already
visible in its abstract; no numerical localization result was treated as a theorem
about this random walk. Bosi–Hu–Peres' *Recurrence and windings of two revolving
random walks* also concerns different graphs with bidirectional vertical edges
away from one axis (Theorem 4, PDF p.5); it is not the circulating field in C1.

Pène's 2020 survey, *Random walks in random sceneries and related models*,
[DOI 10.1051/proc/202068003](https://doi.org/10.1051/proc/202068003), was identified.
The publisher blocked full-text retrieval (HTTP 403), including a host variant.
Its abstract and the source paper's reference to §3.5 were checked; I do not claim
to have inspected that section. Pène's 2009 primary paper and the other primary
papers above were obtained in full. Brémont's 2016 author manuscript was also
identified, but its host failed certificate verification; its later published
2017 criterion and 2020 quasi-periodic treatment were read directly. These access
limits are part of the literature audit, not silently filled from memory.

## What was checked and how

The mathematical conclusions above do not use simulated return frequencies.
The proofs were audited in three ways: the discrete generator and face signs were
re-derived from the jump rates; the lower resolvent formula was checked by a
separate finite-matrix calculation; and the circulating-field identities were
checked with exact rational arithmetic, including the central four sites and the
outer support boundary. The distinction between the two-sided bounds and a
one-sided partial sum was maintained throughout.

`code/checks.py` performs 100 integer checks of (5), its diagonal identity, and
the sector bound. It checks (1) on a 6-by-6 torus at three positive resolvent
parameters: the largest matrix-entry discrepancy is below \(5.3\cdot10^{-14}\).
It also checks the uniform quotient invariant measure for all 784 pairs of
balanced sign words with periods drawn from \(\{2,4,6\}\).
`code/check_quadrants.py` checks (11) and (12) for 12 random rational radial
profiles, without floating-point tolerance. All passed.

For periodic examples, integer transfer on the unwrapped lattice counts every
length-\(n\) horizontal/vertical coin word, so the resulting return probability
is exactly `return_count / 2**n`. Total counts were checked to equal \(2^n\) at
every step. These counts agree with exhaustive word enumeration through time 12
and an independent dense torus convolution through time 32. The convolution
torus is larger than twice that time horizon, and its circumference is a multiple
of both environmental periods; thus it introduces no wrapped return paths.
Full counts through time 128 are in `data/exact_returns.csv`.

| Horizontal word | Vertical word | \(p_{128}(0,0)\) | \(\sum_{n=0}^{128}p_n(0,0)\) |
| --- | --- | ---: | ---: |
| `+-` | `+-` | 0.00493488874013 | 1.58842257862 |
| `++--` | `+-` | 0.00220063586109 | 1.49138886229 |
| `++--` | `+++---` | 0.00182891651060 | 1.33413991722 |
| `++-` | `+-` | 0.000358898245094 | 1.30938242561 |

The first three are recurrent and the last is transient by the periodic proof,
not by this finite table. In particular, a finite, slowly growing Green sum is
not a transience test.

`code/monte_carlo.py` uses 2,048 independent paths per field, each through time
2,048, conditional on one fixed field per case. It saves the environment arrays,
seeds, and finite-horizon summaries. At that horizon, the mean number of returns
excluding time zero, with one Monte Carlo standard error, was:

| Fixed field | Mean returns through 2,048 | Standard error |
| --- | ---: | ---: |
| alternating / alternating | 1.01758 | 0.03066 |
| iid / iid | 0.37012 | 0.01625 |
| iid / alternating | 0.69629 | 0.02270 |
| two sparse logarithmic-defect fields from B | 0.32227 | 0.01412 |

These errors measure path sampling in those environments, not environmental
variation or an infinite-time extrapolation. The last field is recurrent by B,
even though its observed return count is smaller than that of the sampled iid
environment, whose almost-sure transience follows from the literature. The
experiment illustrates a limitation of short simulations.

Reproduce the checks from this directory with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/checks.py
python3 code/check_quadrants.py
python3 code/monte_carlo.py
```

The scripts preserve inherited nice 20, which is lower scheduling priority than
nice 10; if needed they request priority at least nice 10. Numerical thread counts
are fixed at one. Recorded peak numerical resident memory was below 42 MB. No
large sweep, parallel workers, publication, push, or external write was performed.
Source PDF bytes were decoded in memory using `pypdf`; only text was saved.
Source URLs, retrieval versions, byte hashes and text hashes are in
`data/source_manifest.jsonl`. Access failures and subsequent mirrors are logged.

## Limits and remaining questions

This work gives an exact class C, a sufficient criterion B, a stability theorem,
and the mixed class D. It does not give a necessary-and-sufficient test for all
orientation fields, optimal logarithmic exponents, general quasi-periodic fields
with both axes oriented, or all exact sublinear power-law pairs \((a,b)\).
The deterministic tail fields in C do not themselves provide translation-invariant random laws with a uniformly distributed centre. They should not be mistaken for a classification of stationary ergodic mean-zero environmental laws. Even linear absolute primitive asymptotics admit both types by C1. A general
answer must therefore retain signed geometry or more environmental information
than two growth exponents.

The iid Manhattan return exponent \(4/3\) remains a prediction in the source
paper. Its Theorem 1.1 proves transience, not that local limit. The one-scenery
\(5/4\) local limit and the two mutually coupled scenery expressions cannot be
combined by multiplying marginal densities. Neither limiting fluctuations nor
finite numerical return sums supply the missing local estimates.

Task: “Open problem I0003” — 13 November 2026, about 19:57 Asia/Tbilisi.
