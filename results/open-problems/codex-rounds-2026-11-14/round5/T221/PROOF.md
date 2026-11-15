# Stationarity of collision types

All logarithms are natural. The results concern a finite relaxation of
the local entropy calculation. They do not resolve RBS.

## 1. The window and its admissible types

Index the words by

\[
 (w_0,\ldots,w_6)=(1,a,b,aa,ab,ba,bb).
\]

A type is a partition \(\pi\) of these seven positions. Its canonical
encoding is the tuple of class labels, starting with label zero and
assigning new labels in order of first occurrence. Put

\[
 K_0=(0,1,2),\qquad K_a=(1,3,4),\qquad K_b=(2,5,6).
\]

Right word evaluation means \(T_{uv}=T_v\circ T_u\).
Admissibility says that the maps prescribed on classes by

\[
 a:(0,1),(1,3),(2,5),\qquad
 b:(0,2),(1,4),(2,6)
\]

are well defined and injective. Equivalently, for each of these two lists
of edges and any two edges \((u,x),(v,y)\),

\[
 \pi_u=\pi_v\quad\Longleftrightarrow\quad\pi_x=\pi_y.
 \tag{1}
\]

This condition is necessary because generator maps are permutations.
It is sufficient at a single root: on the finite set of classes, extend
each injective partial map by any bijection from its unused sources to
its unused targets. Start at class \(\pi_0\). Following each word in
the window gives its prescribed class. Thus no further identifications
occur. This rederives the preceding session's completion lemma for this
window. It gives no assertion about frequencies of types at other roots.

There are 877 partitions and 103 admissible types; denote their set by
\(\mathcal T\). The scripts certify these counts by two different
partition enumerations and two different implementations of (1).

Give the classes of \(\pi\) independent fair bits \(X_q\), and define

\[
 R=X_{\pi_0},\quad
 E=X_{\pi_0}X_{\pi_1}X_{\pi_2},\quad
 N=\left(\prod_{i\in K_0}X_{\pi_i},
          \prod_{i\in K_a}X_{\pi_i},
          \prod_{i\in K_b}X_{\pi_i}\right),
 \qquad C_\pi=H(E)+H(R\mid N).
 \tag{2}
\]

The finite information inequality from the preceding session follows
directly. For independent labels \(U_v\) on a finite model, let
\(Z_v=U_vU_{T_a(v)}U_{T_b(v)}\) and
\(N_v=(Z_v,Z_{T_a(v)},Z_{T_b(v)})\). Since \(Z_V\) is a function
of \(U_V\), and each \(N_v\) is a function of \(Z_V\),

\[
 |V|\log2=H(Z_V)+H(U_V\mid Z_V)
 \leq\sum_v\{H(Z_v)+H(U_v\mid N_v)\}
 =\sum_v C_{\pi_v}.
 \tag{3}
\]

The first inequality uses subadditivity and removal of conditioning.
Thus the earlier information argument holds independently of its script.

## 2. The stationarity equations and their rank

For \(t=0,a,b\), let \(s_t(\pi)\) be the canonical restriction of
\(\pi\) to \(K_t\). The five possible triple patterns are

\[
 \Sigma=\{000,001,010,011,012\}.
\]

For \(g=a,b\), \(\sigma\in\Sigma\), define

\[
 D_{g,\sigma}(\pi)
 =1_{\{s_0(\pi)=\sigma\}}-1_{\{s_g(\pi)=\sigma\}}.
 \tag{4}
\]

Let \(\mathcal S\) consist of all vectors \((x_\pi)_{\pi\in\mathcal T}\)
satisfying

\[
 x_\pi\geq0,\qquad \sum_\pi x_\pi=1,\qquad
 \sum_\pi x_\pi D_{g,\sigma}(\pi)=0
       \quad(g=a,b,\ \sigma\in\Sigma).
 \tag{5}
\]

Every finite permutation model gives such a vector by taking its type
frequencies. Indeed, at root \(v\), the triple at positions
\((a,aa,ab)\) is the root triple at \(T_a(v)\), and likewise for
\(b\). Each generator permutes the uniformly sampled roots, proving (5).

The ten stationarity rows have rank exactly four. To see the upper bound,
the following four rows vanish identically on admissible types:

\[
 D_{a,000}=D_{a,001}=D_{b,000}=D_{b,010}=0.
 \tag{6}
\]

For example, equality of the first two positions in the \(a\)-child
triple means \(T_a(v)=T_a(T_a(v))\). Injectivity implies
\(v=T_a(v)\). Then the entire child triple equals the root triple.
The converse is immediate. This proves both \(a\)-identities in (6).
Use the first and third positions and injectivity of \(T_b\) for the
other two. In addition, summing (4) over all five patterns gives zero,
separately for each generator. At most four independent rows remain.

For the lower bound, use rows
\((D_{a,010},D_{a,011},D_{b,001},D_{b,011})\) and columns

\[
\begin{split}
 &(0,0,1,0,1,2,0),\quad (0,0,1,0,1,2,2),\\
 &(0,1,0,0,2,1,0),\quad (0,1,0,2,2,1,0).
\end{split}
\]

Each column is admissible by (1), and the corresponding minor is

\[
 \begin{pmatrix}
 0&0&1&1\\0&0&0&-1\\1&1&0&0\\0&-1&0&0
 \end{pmatrix}.
\]

Its determinant is one: the only nonzero term of the determinant
expansion uses column sequence \((2,3,0,1)\), in zero-based indices,
and has sign and product both positive. Thus the rank is at least four.
The all-equal type has every stationarity entry zero, so normalization
adds an independent row. The augmented rank is five.

## 3. Exact fair-AND extrema on the relaxation

The following finite result is certified by the tables and exact-arithmetic
verification described below:

\[
 \boxed{\min_{x\in\mathcal S}\sum_\pi x_\pi C_\pi=\log2,
 \qquad
 \max_{x\in\mathcal S}\sum_\pi x_\pi C_\pi=\tfrac32\log2.}
 \tag{7}
\]

Define

\[
\begin{split}
 \alpha&=\tfrac12\log2-\tfrac34\log3
                   -\tfrac7{16}\log7+\tfrac{11}{16}\log11,\\
 \beta&=-\log2-\tfrac58\log5+\tfrac78\log7,
\end{split}
 \tag{8}
\]

and put \(A_\pi=D_{a,011}(\pi)\),
\(B_\pi=D_{b,001}(\pi)\). The exact dual certificate is

\[
 C_\pi\geq\log2+\alpha A_\pi+\beta B_\pi
                      \qquad(\pi\in\mathcal T).
 \tag{9}
\]

Multiplying (9) by \(x_\pi\) and summing cancels both stationarity
terms by (5). It proves the lower bound in (7). The singleton mass on
the all-equal type is in \(\mathcal S\) and has cost \(\log2\),
which proves attainment.

For the upper bound, \(N\) contains \(E\), so

\[
 H(E)+H(R\mid N)\leq H(E)+H(R\mid E)
                  =H(R)+H(E\mid R).
\]

When \(R=0\), \(E=0\). When \(R=1\), \(E\) is the product of
\(j\in\{0,1,2\}\) distinct remaining fair bits. Thus

\[
 C_\pi\leq\log2+\tfrac12 h(2^{-j})\leq\tfrac32\log2.
\]

On two points, take both generators to be the transposition. Every root
has type \((0,1,1,0,0,0,0)\), and all three outputs equal the product
of the two labels. Its cost is \(\tfrac32\log2\). Its frequency vector
belongs to \(\mathcal S\), proving attainment and the upper equality.

The same reasoning explains why stationarity cannot improve the
preceding session's unrestricted upper cap for any Bernoulli parameter
\(p\): both generators equal to a transposition attain
\(h(p)+p h(p)\) at every root; opposite three-cycles attain
\(h(p)+p h(p^2)\) at every root. Both are actual finite models, hence
stationary. Their maximum is the preceding cap.

### Exact verification of (9)

The finite part of this proof uses enumeration. Full rational logarithm
forms for all 103 costs and certificate slacks are in
`stationarity_table.json` and `stationarity_certificate.json`.
The following table compresses the check: it gives the exact minimum
cost among types with each possible pair \((A_\pi,B_\pi)\).

| Pair | A minimizing type | Minimum cost |
|---|---|---|
| \((-1,-1)\) | \((0,1,2,0,0,2,1)\) | \(\frac{11}4\log2-\frac38\log3+\frac58\log5-\frac78\log7\) |
| \((-1,0)\) | \((0,1,2,0,0,3,1)\) | \(\frac52\log2-\frac{21}{16}\log7+\frac{11}{16}\log11\) |
| \((0,-1)\) | \((0,1,2,0,1,2,0)\) | \(2\log2+\frac58\log5-\frac78\log7\) |
| \((0,0)\) | \((0,0,0,0,0,0,0)\) | \(\log2\) |
| \((0,1)\) | \((0,0,1,0,1,2,2)\) | \(\frac74\log2-\frac98\log3+\frac58\log5\) |
| \((1,0)\) | \((0,1,1,2,3,2,3)\) | \(\frac32\log2-\frac34\log3-\frac7{16}\log7+\frac{11}{16}\log11\) |

There are no other pairs. At the three pairs \((0,-1),(0,0),(1,0)\),
the displayed minimum equals the right side of (9). For the remaining
three pairs, after clearing denominators and exponentiating, the
required strict inequalities are respectively

\[
 2^{20}11^{11}>3^{18}7^7,\qquad
 2^{16}11^{11}>3^6 7^{14},\qquad
 2^{14}5^{10}>3^9 7^7.
 \tag{10}
\]

These are integer comparisons. The scripts also check all 103 slacks
directly; exactly three vanish.

For completeness, the certificate enumeration has the following explicit
steps. Enumerate all restricted-growth strings of length seven; retain
exactly those satisfying (1). For each retained string, enumerate its
independent class bits, form \((R,E,N)\) as in (2), and compute
\(H(E)+H(R,N)-H(N)\). Expand each rational probability term
\(-q\log q\) by factoring numerator and denominator. This gives
\(C_\pi\) and the slack in (9) as rational combinations of logarithms
of primes. If a slack is \(\sum_\ell r_\ell\log\ell\), choose a
common denominator \(d\) of the rational coefficients and compare

\[
 \prod_{r_\ell>0}\ell^{d r_\ell}
 \quad\hbox{with}\quad
 \prod_{r_\ell<0}\ell^{-d r_\ell}.
 \tag{11}
\]

Both products are integers, so no numerical entropy tolerance enters
the signs or equalities.

An independent verifier constructs the class laws without enumerating
bit assignments. Define coordinate sets

\[
 Q_R=\{\pi_0\},\qquad
 Q_E=\{\pi_j:j\in K_0\},\quad
 Q_A=\{\pi_j:j\in K_a\},\quad
 Q_B=\{\pi_j:j\in K_b\},
\]

where the first set is the root event and the other three are the
output events. For any prescribed zero/one pattern on these four
events, let \(I\) index the events prescribed one and \(J\) those
prescribed zero. Inclusion-exclusion gives its probability as

\[
 \sum_{K\subseteq J}(-1)^{|K|}
       2^{-|\bigcup_{i\in I\cup K}Q_i|}.
 \tag{12}
\]

The union is empty when no event is required, in which case the power
is one. This formula follows because any selected collection of AND
events all equal one exactly when all bits in its union equal one.
Inclusion-exclusion removes the forbidden one-events. It remains valid
when sets coincide or contain one another. Marginalizing (12) gives
the three laws in \(H(E)+H(R,N)-H(N)\).

`verify_certificate.py` independently enumerates the admissible types,
recomputes these laws by (12), verifies every reported cost and slack
by rational products, and verifies the rank minor by the determinant
expansion. It needs only the Python standard library and the saved JSON
artifacts; the optimizer is not needed for certificate verification.

The coefficients in (8) have separate short derivations. For type
\(\pi^+=(0,1,1,2,3,2,3)\), write its four independent bits as
\(R,V,S,T\). The output and child output are \(RV\) and \(VST\).
The nonzero counts of \((R,RV,VST)\), out of sixteen assignments, are
\(7,1,4,3,1\); the counts of \((RV,VST)\) are \(11,1,3,1\).
Together with \(H(RV)=2\log2-\frac34\log3\), this yields the last
row's cost, and \(\alpha=C_{\pi^+}-\log2\).

For \(\pi^-=(0,1,2,0,1,2,0)\), the outputs are
\((RUV,RU,RV)\). The first is the product of the latter two.
The pair \((RU,RV)\) has probabilities \((5,1,1,1)/8\).
Only its zero pair leaves uncertainty about \(R\), whose conditional
one-probability there is \(1/5\). Consequently

\[
 C_{\pi^-}=h(1/8)+\tfrac58 h(1/5)
            =2\log2+\tfrac58\log5-\tfrac78\log7,
\]

and \(\beta=\log2-C_{\pi^-}\). In particular, the unconstrained
table minimum is approximately \(0.6895216759678042<\log2\).
The stationarity lower bound is a strict improvement over using this
minimum separately at each root.

## 4. Stationarity still misses a necessary constraint

Consider the type

\[
 \pi^*=(0,1,2,3,0,4,5).
 \tag{13}
\]

The prescribed maps are
\(a:0\mapsto1,1\mapsto3,2\mapsto4\) and
\(b:0\mapsto2,1\mapsto0,2\mapsto5\), both injective.
For example, on six points their completions are

\[
 a=(1,3,4,0,2,5),\qquad b=(2,0,5,1,3,4),
\]

in image-list notation. At root zero their word images have exactly
type (13). All three restrictions \(s_0,s_a,s_b\) are \(012\).
Thus the singleton distribution concentrated on \(\pi^*\) belongs
to \(\mathcal S\).

It cannot be the frequency distribution of a finite permutation model.
For any two permutations \(A,B\), the permutations \(BA\) and
\(AB\) are conjugate, since

\[
 A(BA)A^{-1}=AB.
\]

They have the same number of fixed points. In word notation every
actual frequency vector must therefore satisfy

\[
 \sum_\pi x_\pi 1_{\{\pi_0=\pi_4\}}
 =\sum_\pi x_\pi 1_{\{\pi_0=\pi_5\}}.
 \tag{14}
\]

For the singleton in (13), the two sides are one and zero. The same
identity rules out a limit of actual frequency vectors, because it is
a closed linear equality. Its fair-AND cost is approximately
\(0.9175228381506644>\log2\), so adding (3) to triple stationarity
still does not exclude it. It is an example of a missing compatibility
condition, not a group pattern or an entropy-lowering RBS witness.

## 5. Use with a hypothetical entropy witness

For a general finite code on this window, let \(C_\pi\) be its
collision cost, \(C_0\) its intended group cost, and
\(\delta=H(p)-C_0\). Let \(m_j(\pi)\) indicate failure of a
specified word test, and let \(q_j\) be its model frequency.
Stationarity permits the following extension of the preceding weighted
defect certificate. If \(\omega_j\geq0\) and arbitrary real
\(y_{g,\sigma}\) satisfy

\[
 C_\pi-C_0\leq\sum_j\omega_jm_j(\pi)
          +\sum_{g,\sigma}y_{g,\sigma}D_{g,\sigma}(\pi)
             \quad(\pi\in\mathcal T),
 \tag{15}
\]

then every finite model obeys

\[
 \delta\leq\sum_j\omega_jq_j.
\]

Indeed, average (15), cancel the stationarity terms using (5), and use
the finite information inequality \(H(p)\leq\sum x_\pi C_\pi\).
This is a finite linear program with free stationarity multipliers.
Alternatively impose specified defect tolerances directly on (5) and
optimize its entropy cost. Only necessary conditions on model
frequencies are obtained, as (13)--(14) demonstrate.

No genuine positive-gap code is supplied here. The example remains
the AND code from the preceding session, and it gives no new group
known to satisfy or violate RBS. Priority of this finite refinement has
not been established. The local entropy approach itself is prior work;
see Lewis Bowen and Michael Chapman, *Surjunctivity does not characterize
cosoficity of invariant random subgroups*,
[arXiv:2511.06586v1](https://arxiv.org/html/2511.06586v1), and the
original RBS formulation in Brandon Seward, *Krieger's finite generator
theorem for actions of countable groups II*,
[arXiv:1501.03367v4](https://arxiv.org/abs/1501.03367v4).
