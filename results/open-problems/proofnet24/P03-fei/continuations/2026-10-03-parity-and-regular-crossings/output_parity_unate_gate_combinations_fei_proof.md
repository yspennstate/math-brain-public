# Output parity of arbitrary combinations of unate gates

Date: 2026-10-02. **Complete proof; independently audited internally.**
The gates in this theorem may share all their input variables and may
have different monotonicity orientations. No FEI premise on the outer
Boolean function is assumed. This note leaves previous stable proofs
unchanged. Novelty and external peer review remain unverified; ordinary
FEI for arbitrary Boolean functions is not resolved.

## The theorem

Let \(g_1,\ldots,g_m:\{-1,1\}^n\to\{-1,1\}\) be unate, and let
\(F:\{-1,1\}^m\to\{-1,1\}\) be arbitrary. Put
\[
 g(x)=F(g_1(x),\ldots,g_m(x)),\qquad
 h(x)=\chi_T(x)g(x),\qquad q=n-|T|.
\]
For \(m\ge1\), define
\[
 t_m=\left(\frac{m+\sqrt{m^2+1}}2\right)^2.
\]
Then, with base-two Fourier entropy and physical bit-flip influence,
\[
 \boxed{H(h)=H(g)\le4(q+t_m)I(h).}
\tag{1}
\]
In particular, full output parity gives the dimension-independent bound
\[
 H(\chi_{[n]}g)\le(m+\sqrt{m^2+1})^2 I(\chi_{[n]}g).
\tag{2}
\]
The dependence on \(q\) in (1) is linear. Constant gates can be removed
before choosing \(m\). When \(m=0\), \(g\) is constant, \(h\) is a
parity up to a global sign, and its entropy is zero. Dimension zero is
also immediate.

Every LTF is unate after orienting each coordinate according to its
weight. Therefore (1) applies to parity outputs of **arbitrary Boolean
combinations of \(m\) halfspaces**, with unrelated weights, arbitrary
thresholds, and completely shared inputs. It also applies to arbitrary
unate gates that are not thresholds. The gates need not admit one common
orientation in which they are all increasing.

For \(m=1\), the sharper
[separate unate parity bound](output_parity_bounded_alternation_fei_proof.md)
gives constant 2 under full parity, and \(q+2\) when \(|T|\ge2\).
No claim is made that the constants in (1) are optimal.

## A universal parity inequality from an influence-vector bound

For any Boolean \(g\), let
\[
 \rho=\left(\sum_i I_i(g)^2\right)^{1/2}.
\]
The following stronger formulation does not require a representation by
gates: for any \(M\ge\rho\),
\[
 H(\chi_Tg)\le
 4\left[q+\left(\frac{M+\sqrt{M^2+1}}2\right)^2\right]I(\chi_Tg).
\tag{3}
\]
If \(M=0\), all influences vanish, hence \(g\) is constant by
connectivity of the cube, and (3) is immediate. It remains to prove (3)
for \(M>0\).

As in the [separate parity identity proof](output_parity_bounded_alternation_fei_proof.md),
Fourier multiplication translates indices by \(T\), so \(H(h)=H(g)\),
and
\[
 I(h)=\ell+\sum_{i\notin T}I_i(g)-\sum_{i\in T}I_i(g),
 \qquad \ell=|T|.
\tag{4}
\]
Cauchy–Schwarz and nonnegativity of the outside influences imply
\[
 I(h)\ge\ell-M\sqrt\ell.
\tag{5}
\]

Two elementary entropy bounds are used. The spectral law has \(2^n\)
atoms, so \(H(h)\le n\). Also
\[
 H(h)\le4nI(h).
\tag{6}
\]
Here is a full proof of (6). For nonconstant \(h\), let
\(r\in[2^{-n},1/2]\) be its minority probability,
\(v=4r(1-r)\), and \(R=\log_2(1/r)\le n\). Splitting off the empty
spectral coefficient gives \(H(h)\le h_2(v)+vn\). For \(r\le1/4\),
\[
 h_2(v)\le v[\log_2(1/v)+\log_2e]
 =v\left[R+\log_2\frac{e}{4(1-r)}\right]
 \le vR\le4rR,
\]
because \(4(1-r)\ge3>e\). For \(r\ge1/4\), use
\(h_2(v)\le1\le4r\le4rR\). Thus \(H(h)\le8nr\).
Fourier Poincare gives
\(I(h)\ge\operatorname{Var}(h)=4r(1-r)\ge2r\), proving (6).
Constant \(h\) and dimension zero have zero entropy and are handled
before divisions by influence.

Set
\[
 t=\left(\frac{M+\sqrt{M^2+1}}2\right)^2,
 \qquad d(\ell)=\ell-M\sqrt\ell.
\]
Then \(\sqrt t>M\) and \(d(t)=1/4\). If \(\ell\le t\), (6)
gives \(H(h)/I(h)\le4n=4(q+\ell)\le4(q+t)\).
If \(\ell\ge t\), then \(d(\ell)\ge d(t)=1/4\) because
\(d'(\ell)=1-M/(2\sqrt\ell)>0\) there. The bounds \(H(h)\le n\)
and (5) give
\[
 \frac{H(h)}{I(h)}\le\frac{\ell+q}{\ell-M\sqrt\ell}.
\]
On this range the derivative of the last ratio has the sign of
\[
 -q-\frac M2\sqrt\ell+\frac{Mq}{2\sqrt\ell}
 =-\frac M2\sqrt\ell-q\left(1-\frac{M}{2\sqrt\ell}\right)<0.
\]
It is consequently at most its value at \(\ell=t\), namely
\((t+q)/(1/4)=4(q+t)\). This proves (3). Maximizing over a real
variable \(\ell\) gives a valid upper bound for the integer subset size;
no integrality assumption about \(t\) is needed.

## Unate gates give a dimension-independent influence-vector bound

For a unate gate \(g_j\), let \(\varepsilon_{j,i}\in\{-1,1\}\)
denote an increasing/decreasing orientation of its \(i\)-th coordinate.
Conditioning on the other coordinates yields
\[
 \widehat g_j(\{i\})=\varepsilon_{j,i}I_i(g_j).
\]
An irrelevant coordinate has both sides zero and may be assigned either
orientation. Parseval then gives
\[
 \sum_i I_i(g_j)^2
 =\sum_i\widehat g_j(\{i\})^2
 \le\operatorname{Var}(g_j)\le1.
\tag{7}
\]
There is no requirement that different gates have compatible
orientations.

If an \(i\)-edge changes \(g=F(g_1,\ldots,g_m)\), at least one
of its gate outputs changes on that edge. The pointwise union bound
therefore gives
\[
 I_i(g)\le\sum_{j=1}^m I_i(g_j).
\]
All entries are nonnegative, so monotonicity of the Euclidean norm and
Minkowski, followed by (7), imply
\[
 \rho\le\left\|\sum_j(I_i(g_j))_{i=1}^n\right\|_2
 \le\sum_j\|(I_i(g_j))_i\|_2\le m.
\tag{8}
\]
Apply (3) with \(M=m\) to prove (1). More precisely, one may take
\(M=\sum_j\sqrt{\operatorname{Var}(g_j)}\), or any independently
established upper bound on \(\rho\), in (3).

## Scope

This is an unconditional theorem for the **parity output** \(h\). It
does not prove ordinary FEI for \(F(g_1,\ldots,g_m)\), and does not
assert general closure of FEI under overlapping gate composition.
In particular, with \(T=\varnothing\), \(q=n\) and the bound depends
on the dimension. With full parity, the complementary influence
\(I(h)=n-I(g)\) is the denominator being controlled.

For fixed \(m\) and a bounded number \(q\) of missing parity
coordinates, (1) is dimension independent. This includes any bounded
number of halfspace gates even when no common ascending-path ordering
controls their sign changes. It is distinct in scope from a conditional
Fourier-character multiplication closure theorem: the hypothesis here
is the explicit influence-vector estimate (8), not an assumed FEI bound
for the unmodulated function or all its restrictions.

The [author checker](verify_output_parity_unate_gate_combinations.py) and
[report](output_parity_unate_gate_combinations_checks.json) verify the
universal formulation on all 65,814 Boolean functions through dimension
four and all 1,050,698 corresponding function/parity pairs. They also
check 440 combinations of 1,320 unate gates through dimension twelve,
with 3,155 further parity pairs. Among these are 350 combinations whose
gates use different coordinate orientations and 352 combinations on
shared input coordinates. The coefficient permutations, gate singleton
identities, flip union bounds, and squared influence-vector bounds use
integer arithmetic. Entropy and irrational constants are checked with
a numerical tolerance of \(3\cdot10^{-11}\).

The [independent full analytic audit](output_parity_unate_gate_combinations_heat_audit.md)
read every step, independently rederived the threshold optimization,
and passed the influence-vector, unateness, shared-input, and scope
arguments. This is internal verification, not external peer review.
The proof is elementary after the stated definitions and establishes
no historical-priority claim. Full Boolean FEI remains open.
