# Fourier entropy for support with bounded ascending paths

Date: 2026-10-02. **Complete proof; independently audited internally.** This
note proves a restricted Fourier entropy–influence theorem. It does not
resolve the conjecture for all Boolean functions, and no novelty claim
has been certified. The operator inequality used below is the classical
Haagerup–de la Harpe nilpotent numerical-radius theorem; it is credited
explicitly and proved again here by a finite-dimensional dilation.

## The theorem and the class

Work on the uniform cube \(\{-1,1\}^n\). Fourier entropy and physical
influence are
\[
 H(f)=\sum_{S\subseteq[n]}\widehat f(S)^2
       \log_2\frac1{\widehat f(S)^2},\qquad
 I(f)=\sum_i\Pr[f(X)\ne f(X^{\oplus i})].
\]
Zero summands in the entropy are zero. Let \(E\) be either label class of
a Boolean function; write \(f=1-2\mathbf1_E\), changing the global sign
if necessary. An ascending path in \(E\) is a sequence of distinct
vertices in \(E\), each obtained from the preceding vertex by changing
one coordinate from \(-1\) to \(+1\). Its length here is its **number of
vertices**, not its number of edges.

Suppose every ascending path in \(E\) has at most \(k\) vertices, for an
integer \(k\ge1\). Then
\[
 \boxed{H(f)\le4(k+1)^2 I(f).}
\tag{1}
\]
The refinement proved below improves this to
\[
 \boxed{H(f)\le4\cot^2\!\left(\frac{\pi}{2(k+1)}\right)I(f).}
\tag{1a}
\]
The label class \(E\) need not be the minority class. If \(E\) is empty or is the whole
cube, \(f\) is constant and (1) is immediate. Dimension zero is also
constant and is handled this way. All subsequent arguments concern
\(n\ge1\), \(0<\Pr(E)<1\).

A \(k\)-Sperner family has no inclusion chain containing \(k+1\)
members, after identifying a cube vertex with its set of positive
coordinates. Every ascending path is an inclusion chain, so (1) holds
for arbitrary \(k\)-Sperner label classes. The path hypothesis is weaker:
it forbids only chains connected by cube edges inside the family. The
theorem does not require a symmetric family or a union of Hamming layers.
For example, the family of all even-rank vertices has upward path bound
\(k=1\), while it contains inclusion chains of unbounded length as the
dimension grows.

When \(k=1\), there is a sharper bound
\[
 \boxed{H(f)\le4I(f).}
\tag{2}
\]
This case includes every label class inducing no cube edge, hence every
antichain. A constant function can always be dealt with before defining
the largest nonempty path length.

## A support energy bound

Put \(p=\Pr(E)\), \(r=\min(p,1-p)\), and \(K=(k+1)^2\). We will prove
\[
 nr\le\frac K2 I(f).
\tag{3}
\]
For a minority support, \(p=r\), this is \(np\le KI(f)/2\).

Equip the vertex space with the inner product
\(\langle u,v\rangle=2^{-n}\sum_x\overline{u(x)}v(x)\).
Let \(A\) be cube adjacency, and let
\(L=(n\operatorname{Id}-A)/2\). With the Walsh basis,
\(L\chi_S=|S|\chi_S\), and
\[
 \langle u,Lu\rangle=\sum_S |S|\,|\widehat u(S)|^2
 =\frac14\sum_i\mathbb E|u(X)-u(X^{\oplus i})|^2.
\tag{4}
\]
For Boolean \(f\), this energy equals \(I(f)\). Since
\(f=1-2\mathbf1_E\), it also equals
\(4\langle\mathbf1_E,L\mathbf1_E\rangle\).

Let \(U\) be the raising operator: it sends a coordinate vector at a
vertex to the sum of coordinate vectors at its upward neighbors. Thus
\(A=U+U^*\). Its block from Hamming layer \(s\) to layer \(s+1\) has norm
at most \(\sqrt{(s+1)(n-s)}\). Indeed, each output is a sum of \(s+1\)
input values, so Cauchy–Schwarz and the fact that each input occurs in
\(n-s\) outputs give the square of this bound. Equality holds on constant
vectors on the two layers. Different layer blocks have orthogonal input
and output spaces. Therefore
\[
 \|U\|=\max_{0\le s<n}\sqrt{(s+1)(n-s)}\le\frac{n+1}{2}.
\tag{5}
\]

Let \(P_E\) be the orthogonal projection onto vertices in \(E\), and
let \(U_E=P_EUP_E\), acting on that subspace. The entries of \(U_E^j\)
count upward paths with \(j\) edges whose every vertex lies in \(E\).
The hypothesis thus implies precisely
\[
 U_E^k=0.
\tag{6}
\]
The exponent is \(k\) because such a path would have \(k+1\) vertices.
Also \(\|U_E\|\le\|U\|\).

For an operator \(T\), write
\(w(T)=\sup_{\|v\|=1}|\langle Tv,v\rangle|\).
The classical nilpotent numerical-radius inequality says
\[
 T^k=0\quad\Longrightarrow\quad
 w(T)\le\|T\|\cos\frac{\pi}{k+1}.
\tag{7}
\]
A self-contained proof follows in the next section. Applying it to
\(U_E\) and using self-adjointness of \(A_E=U_E+U_E^*\) gives
\[
 \|A_E\|\le2w(U_E)
 \le(n+1)\cos\frac{\pi}{k+1}.
\tag{8}
\]
Since \(\|\mathbf1_E\|_2^2=p\), (4) and (8) yield
\[
 I(f)=2\bigl[np-\langle\mathbf1_E,A\mathbf1_E\rangle\bigr]
 \ge2\left[n-(n+1)\cos\frac{\pi}{k+1}\right]p.
\tag{9}
\]

If \(n\ge K\), use
\[
 1-\cos\frac{\pi}{k+1}
 =2\sin^2\frac{\pi}{2(k+1)}\ge\frac2{(k+1)^2}=\frac2K.
\]
Here \(\sin t\ge2t/\pi\) on \([0,\pi/2]\). Consequently
\[
 n-(n+1)\cos\frac{\pi}{k+1}
 \ge\frac{2(n+1)}K-1\ge\frac nK,
\]
where the last inequality follows from \(n+2\ge K\). Thus
\(np\le KI(f)/2\), which implies (3) because \(r\le p\).

If \(n<K\), Poincare on the cube gives
\[
 I(f)\ge\operatorname{Var}(f)=4r(1-r)\ge2r.
\]
This proves \(nr\le nI(f)/2\le KI(f)/2\), and establishes (3) in
every dimension. For \(k=1\), the family induces no cube edge, so
\(\langle\mathbf1_E,A\mathbf1_E\rangle=0\) and, more sharply,
\[
 I(f)=2np\ge2nr.
\tag{10}
\]

## Proof of the classical operator inequality

For completeness, take a contraction \(T\) with \(T^k=0\), and put
\(D=(\operatorname{Id}-T^*T)^{1/2}\). Define
\[
 Vh=(Dh,DTh,\ldots,DT^{k-1}h)
\]
in the orthogonal sum of \(k\) copies of the original Hilbert space.
The telescoping identity
\[
 \|Vh\|^2
 =\sum_{j=0}^{k-1}(\|T^jh\|^2-\|T^{j+1}h\|^2)
 =\|h\|^2
\]
shows that \(V\) is an isometry. Let the backward shift be
\(B(h_0,\ldots,h_{k-1})=(h_1,\ldots,h_{k-1},0)\).
Nilpotency gives \(VT=BV\), hence
\(w(T)\le w(B)\).

For any phase \(\theta\), the self-adjoint operator
\(\operatorname{Re}(e^{i\theta}B)\) is unitarily equivalent, by diagonal
coordinate phases, to \((B+B^*)/2\). The latter is one-half the adjacency
matrix of the path on \(k\) vertices, tensored with the identity. The
vectors with scalar coordinates \(\sin(j\ell\pi/(k+1))\),
\(1\le j\le k\), have eigenvalues
\(\cos(\ell\pi/(k+1))\), \(1\le\ell\le k\).
It follows that \(w(B)=\cos(\pi/(k+1))\). Scaling by \(\|T\|\) proves
(7); the zero operator is immediate. This also covers \(k=1\), when
\(T=0\) and the cosine is zero.

The inequality (7) is **not a new operator theorem**. It is Theorem 1 of
U. Haagerup and P. de la Harpe, *The numerical radius of a nilpotent
operator on a Hilbert space*, Proceedings of the American Mathematical
Society **115** (1992), 371–379, DOI
[10.1090/S0002-9939-1992-1072339-6](https://doi.org/10.1090/S0002-9939-1992-1072339-6).
The [University of Geneva author archive](https://archive-ouverte.unige.ch/unige:12076)
provides the [published primary PDF](https://access.archive-ouverte.unige.ch/access/metadata/2e3d55fc-f7d2-42af-95ae-6c06df864dbb/download).
Theorem 1 is on printed page 372. The proof above supplies every part of
the particular finite-dimensional use needed here.

## An elementary entropy bound for a minority label

This step does not use the path hypothesis. For any nonconstant Boolean
function let \(r\le1/2\) be its minority probability and put
\(q=\operatorname{Var}(f)=4r(1-r)\). The empty Fourier coefficient has
squared mass \(1-q\); all other coefficients have total mass \(q\).
Splitting this spectral probability law gives
\[
 H(f)\le h_2(q)+q\log_2(2^n-1)\le h_2(q)+qn.
\tag{11}
\]
For \(q=1\), the same identity uses \(h_2(1)=0\). Write
\(R=\log_2(1/r)\); the nonempty minority class has \(r\ge2^{-n}\), so
\(1\le R\le n\). The inequality
\(-(1-q)\log_2(1-q)\le q\log_2e\) gives, for all \(0<q<1\),
\[
 h_2(q)\le q[\log_2(1/q)+\log_2e].
\]
If \(r\le1/4\), then \(4(1-r)\ge3>e\), and therefore
\[
 h_2(q)\le q\left[R+\log_2\frac{e}{4(1-r)}\right]
 \le qR\le4rR.
\]
If \(r\ge1/4\), instead use
\(h_2(q)\le1\le4r\le4rR\). This also covers \(q=1\). Hence always
\(h_2(q)\le4rR\le4nr\). Combining this with (11) and \(q\le4r\) proves
the elementary universal bound
\[
 \boxed{H(f)\le8nr.}
\tag{12}
\]
Combining (12) with (3) proves (1); combining it with (10) proves (2).
All normalizations are explicit, and no existing FEI subclass theorem
is an input to this argument.

## Refinement using both energy lower bounds

Keep \(c=\cos(\pi/(k+1))\), so \(0\le c<1\), and define
\[
 n_* =\frac{1+c}{1-c}
     =\cot^2\!\left(\frac{\pi}{2(k+1)}\right).
\]
Poincare and (12) imply \(H(f)/I(f)\le4n\). Whenever
\(d_n=n-(n+1)c>0\), (9), \(p\ge r\), and (12) also imply
\[
 \frac{H(f)}{I(f)}\le\frac{4n}{d_n}.
\]
If \(n\le n_*\), the first bound is at most \(4n_*\). If
\(n\ge n_*\), then \(d_n\ge d_{n_*}=1\), and
\[
 \frac{d}{dn}\frac{n}{n(1-c)-c}
 =\frac{-c}{[n(1-c)-c]^2}\le0.
\]
The second bound is therefore at most its value \(4n_*\) at
\(n=n_*\). This proves (1a), including \(k=1\), where \(c=0\),
\(n_*=1\), and the second ratio is exactly 4.

Equivalently, the same two energy bounds prove the sharper support
estimate \(nr\le n_*I(f)/2\). For orientation about constants,
\(\tan t\ge t\) for \(0<t<\pi/2\) gives
\[
 4\cot^2\!\left(\frac{\pi}{2(k+1)}\right)
 \le\frac{16}{\pi^2}(k+1)^2 < 1.622(k+1)^2.
\]
The simple polynomial constant in (1) remains a valid corollary.

## Sharpness for supports inducing no cube edge

For a single-vertex support in dimension \(n\), put \(p=2^{-n}\). Its
influence is exactly \(I(f)=2np\), its empty Fourier coefficient is
\(1-2p\), and its other \(2^n-1\) coefficients have squared mass
\(4p^2\). Thus, with \(e(t)=t\log_2(1/t)\),
\[
 H(f)=e((1-2p)^2)+(2^n-1)4p^2(2n-2).
\tag{13}
\]
The second term divided by \(2np\) is
\(4(1-p)(1-1/n)\), which tends to 4. The first term is nonnegative,
and (2) bounds the whole ratio by 4. Therefore
\[
 \lim_{n\to\infty}\frac{H(f)}{I(f)}=4.
\]
The uniform constant 4 in (2) cannot be decreased.

## A weighted-band corollary with arbitrary internal labels

Suppose \(w_i\ge a>0\), and a label class \(E\) is contained in
\[
 \left\{x:t\le\sum_iw_ix_i\le t+D\right\},\qquad D\ge0.
\]
No condition is imposed on which vertices inside that band belong to
\(E\). Along an ascending path with \(j\) edges, the score increases
by at least \(2aj\). Thus every such path has at most
\(k=\lfloor D/(2a)\rfloor+1\) vertices. Theorem (1) gives
\[
 H(f)\le4\left(\left\lfloor\frac{D}{2a}\right\rfloor+2\right)^2 I(f).
\tag{14}
\]
If \(D<2a\), there is no internal edge and the sharper bound is
\(H(f)\le4I(f)\). The closed endpoints used here make the integer
rounding valid even when \(D/(2a)\) is integral. Coordinate sign flips
preserve Fourier entropy and influence, so the same statement holds
for nonzero signed weights after flipping those coordinates and taking
\(a\le\min_i|w_i|\). This corollary concerns containment of an entire
label class, rather than a perturbation of an unrelated threshold.

## Scope and verification

The result covers either bounded-path label class, including arbitrary
\(k\)-Sperner families and their global complements. The value of \(k\)
is the number of vertices along an induced upward path; it can depend on
the function. A universal FEI bound results only for a class with a
uniform bound on \(k\). This does not claim a strong
\(H\le C[I-\operatorname{Var}]\) inequality or unrestricted composition
closure, and it does not solve full Boolean FEI.

The [author checker](verify_bounded_ascending_path_support.py) and
[report](bounded_ascending_path_support_checks.json) verify every one of
the 65,814 label supports through dimension four and 368 further
structured or random supports in dimensions five through twelve. The
influence/Walsh normalizations and (3) are checked with integer
arithmetic; selected compressed raising matrices are powered explicitly
to check nilpotency. Entropy and selected adjacency bounds are checked
numerically, with tolerance \(3\cdot10^{-11}\). This includes 890
nonconstant cases with \(n\ge(k+1)^2\), 26,503 cases whose specified
label is not the minority, and 881 cases with \(k=1\). The script also
checks 128 weighted-band rounding cases and the single-vertex entropy
ratio through dimension 512.

The [independent full analytic audit](bounded_ascending_path_support_heat_audit.md)
read the original candidate and this sharpened final proof, independently
checked the published operator source, and passed every step, including
the cotangent refinement, arbitrary weighted-band labels, and sharp
single-vertex limit. Its [separate implementation](verify_bounded_ascending_path_support_heat.py)
and [report](bounded_ascending_path_support_heat_checks.json) cover 66,060
supports through dimension sixteen, including 7,468 whose maximum
inclusion chain exceeds their induced ascending-path height. The audit
also verifies 27 independent nonnormal contraction dilations. The root
agent independently rederived the analytic energy argument and both
entropy refinements. These are internal checks, not external peer review.

The [original candidate](bounded_ascending_path_support_fei_candidate.md)
is preserved separately. Finite verification supplements the analytic
proof. Historical priority and novelty remain unverified, and full
Boolean FEI remains open.
