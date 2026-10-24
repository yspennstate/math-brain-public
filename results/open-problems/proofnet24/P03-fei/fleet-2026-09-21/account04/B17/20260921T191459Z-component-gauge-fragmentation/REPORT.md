# B17 FEI mechanism: component gauges, transverse curl, and fragmentation payment

Status: **PARTIAL; full FEI remains OPEN / NOT PROVED.**  Execution context: **WITHOUT_VERIFIED_BRAIN**.

This run deliberately changes proof mechanism from the preceding affine/quadratic/shear calculations.  The named obstruction is the following: a pivot derivative can carry a large Fourier-entropy-changing phase at **zero instantaneous influence cost**.  The new observation is that all zero-cost phases are exactly gauges on connected components of the pivot-sensitive set, and the entropy of that component label is quantitatively paid by transverse second-order sensitivity.  What remains is a connected-component spectral term; an explicit connected example below shows that the most optimistic coefficient-2 boundary payment for that residual is false.

No publication-priority claim is made here.  The result is an internal proof mechanism/counterexample package for the active FEI programme.

## 1. Setup and exact pivot decomposition

Write a Boolean function on `m+1` bits as

\[
 f(x,y)\in\{-1,1\},\qquad x\in\{0,1\}^m,\quad y\in\{0,1\}.
\]

Let `f_0,f_1` be its two restrictions and set

\[
 a={f_0+f_1\over2},\qquad b={f_0-f_1\over2}.
\]

Then `a,b` have disjoint physical supports, `a(x)^2+b(x)^2=1`, and

\[
 A:=\{x:f_0(x)\ne f_1(x)\}=\operatorname{supp}b,
 \qquad p:=\mu(A)=\operatorname{Inf}_y(f).
\]

On `A`, `b=s1_A` for a sign function `s:A->+-1`.  With `\mathcal H(u)` denoting the Fourier entropy of the squared normalized Walsh coefficients of a nonzero real function `u`, and

\[
 \mathcal E(u)=\sum_S |S|\widehat u(S)^2
 ={1\over4}\sum_i \mathbb E (u(x)-u(x^{\oplus i}))^2,
\]

the split into Fourier fibres with and without `y` gives the exact identities

\[
\boxed{
 H(f)=h_2(p)+(1-p)\mathcal H\!\left({a\over\sqrt{1-p}}\right)
       +p\mathcal H\!\left({b\over\sqrt p}\right)
}
\tag{1}
\]

and

\[
\boxed{I(f)=p+\mathcal E(a)+\mathcal E(b).}
\tag{2}
\]

Zero-mass terms are omitted in (1).

## 2. Exact influence cost of a derivative-row phase

For any Boolean phase `h(x)=(-1)^{phi(x)}`, the triangular input bijection

\[
 \tau_h(x,y)=(x,y\oplus\phi(x))
\]

leaves `a` fixed and sends `b` to `hb`.  Since `b=s1_A`, define

\[
 F_A(s):=\sum_i\Pr[x,x^{\oplus i}\in A,\ s(x)\ne s(x^{\oplus i})].
\]

A direct edge calculation gives

\[
\boxed{\mathcal E(s1_A)=\mathcal E(1_A)+F_A(s).}
\tag{3}
\]

Indeed, support-boundary edges cost the same for `s1_A` and `1_A`; an internal edge with opposite signs contributes exactly one extra unit in the oriented Dirichlet normalization, while an internal equal-sign edge contributes zero extra cost.

Consequently the minimum transverse influence over the complete triangular-shear orbit is `\mathcal E(1_A)`, and it is achieved **exactly when the sign is constant on every connected component of the induced cube graph on `A`**.  Thus the entire zero-influence-cost gauge group is the set of independent signs on the connected components of `A` (modulo the irrelevant global sign).

This identifies the source of the zero-influence-drop phenomenon from the preceding B17 shear run: it is not an isolated four-bit accident; disconnected pivot-sensitive sets support genuine entropy-changing gauge freedom at no influence cost.

## 3. Transverse square-curl identity pays fragmentation

Let

\[
 \eta_y(x)=1_A(x)
\]

be the indicator that the `y`-edge at base point `x` is sensitive.  For a transverse coordinate `i`, let `\eta_i^0(x)` and `\eta_i^1(x)` be the indicators that the `i`-edge is sensitive in the `y=0` and `y=1` slices.  On every `(i,y)` square, the parity of sign changes around the square is even, hence pointwise

\[
\boxed{
 \eta_y(x)\oplus\eta_y(x^{\oplus i})
 =\eta_i^0(x)\oplus\eta_i^1(x).
}
\tag{4}
\]

Therefore, if

\[
 \delta_i:=\Pr[\eta_i^0\ne\eta_i^1],
 \qquad
 B(A):=\sum_i\Pr[1_A(x)\ne1_A(x^{\oplus i})],
\]

then

\[
\boxed{B(A)=\sum_i\delta_i.}
\tag{5}
\]

So the edge boundary of the pivot-sensitive set is exactly a second-order `curl` quantity: the total probability that transverse sensitivity changes when the pivot bit is flipped.

Let the connected components of `A` be `A_1,...,A_k`, with cube densities `p_j=\mu(A_j)`, total density `p=\sum_jp_j`, and conditional component weights `w_j=p_j/p`.  Distinct components have no cube edges between them.  Applying the standard edge-isoperimetric inequality to each component separately gives

\[
\begin{aligned}
 B(A)
 &\ge 2\sum_j p_j\log_2{1\over p_j}\\
 &=2p\left(\log_2{1\over p}+H(w)\right).
\end{aligned}
\tag{6}
\]

Hence

\[
\boxed{
 H(w)\le {B(A)\over2p}-\log_2{1\over p}.
}
\tag{7}
\]

The `extra` boundary beyond the density-only isoperimetric term therefore pays the entropy of the zero-cost component gauge.

The inequality is sharp: if `A` is one parity class in the 3-cube, then `p=1/2`, its four vertices are isolated components, `H(w)=2`, and

\[
 B(A)=3=2p(1+2).
\]

## 4. Component-phase compression lemma

Normalize each component indicator by

\[
 \psi_j={1_{A_j}\over\sqrt{p_j}},
\]

and let `q_j` be its spectral law.  For a component-constant gauge `\epsilon=(\epsilon_1,...,\epsilon_k)`, the normalized derivative row is

\[
 \psi_\epsilon=\sum_j\epsilon_j\sqrt{w_j}\,\psi_j.
\]

Average over independent Rademacher component signs.  All Fourier cross terms vanish, so

\[
\boxed{
 \mathbb E_\epsilon q_\epsilon=\bar q:=\sum_jw_jq_j.
}
\tag{8}
\]

By concavity of Shannon entropy, some component gauge satisfies

\[
\boxed{
 \mathcal H(\psi_\epsilon)\le H(\bar q).
}
\tag{9}
\]

Introduce a random component label `J~w` and, conditionally on `J=j`, a spectral index `S~q_j`.  Then exactly

\[
 H(\bar q)=H(w)+\sum_jw_jH(q_j)-H(J\mid S).
\tag{10}
\]

Combining (7)--(10), there is an **influence-minimizing triangular shear** for which

\[
\boxed{
 p\,\mathcal H(\psi_\epsilon)
 \le {B(A)\over2}-p\log_2{1\over p}
     +p\sum_jw_jH(q_j)-pH(J\mid S).
}
\tag{11}
\]

Equation (11) is the useful new comparison mechanism.  It separates the pivot-row entropy into:

1. a component-label term paid by the exact transverse square-curl budget `B(A)=sum delta_i`;
2. within-component spectral entropy; and
3. an **overlap refund** `H(J|S)` when the component spectra fail to reveal the physical component label.

For an independent-set sensitive support, every component is a singleton, every `q_j` is the uniform law on all Walsh frequencies, and the component label is completely hidden from `S`.  Thus `H(J|S)=H(w)` and `H(\bar q)=m`.  In particular there is a minimum-influence shear with

\[
 p\,\mathcal H(\psi_\epsilon)\le pm={B(A)\over2}=2\mathcal E(1_A).
\]

This is an infinite structured class of exact local payments.  It is **not** a proof of universal FEI.

## 5. Exact admissible Boolean obstruction: one bit of entropy at zero influence cost

Take three base bits and

\[
 A=\{x:x_0\oplus x_1\oplus x_2=0\}.
\]

Thus `A` is an independent set of four isolated vertices.  Define two four-bit Boolean functions:

\[
 f_{\rm low}(x,y)=
 \begin{cases}
 1,&x\notin A,\\
 (-1)^y,&x\in A,
 \end{cases}
\]

and

\[
 f_{\rm high}(x,y)=
 \begin{cases}
 1,&x\notin A,\\
 (-1)^{y+x_0x_1},&x\in A.
 \end{cases}
\]

They differ by the nonlinear triangular shear `y -> y xor (x_0 x_1)`.  Since every point of `A` is its own component, both signings are already influence-minimizing gauges.  Exact integer Walsh arithmetic gives

\[
 H(f_{\rm low})=2,\quad I(f_{\rm low})=2,
\]

and

\[
 H(f_{\rm high})=3,\quad I(f_{\rm high})=2.
\]

The squared unnormalized Walsh multiplicities are respectively

- low: `64` four times and `0` twelve times;
- high: `64` twice, `16` eight times, and `0` six times.

Thus an admissible Boolean shear changes Fourier entropy by **one full bit while changing total influence by exactly zero**.  Tensoring `k` disjoint copies makes the entropy gap `k` bits while the two endpoints still have identical influence `2k`.

Therefore no universal descent proof can charge an entropy-lowering component-gauge move only to its instantaneous decrease in total influence.  Any such argument needs a separate fragmentation/gauge bank, such as the square-curl term above, or another state potential.

## 6. A tempting connected-component closure is already false at coefficient 2

The component-gauge lemma leaves the spectral entropy of connected component indicators.  A natural optimistic guess would be

\[
 H(q_A)\stackrel{?}{\le}{B(A)\over p}
\tag{12}
\]

for connected `A`, i.e. coefficient `2` relative to `B(A)/(2p)`.  This is false even for a cube with one deleted vertex.

Let `A=Q_m\setminus\{0\}`.  It is connected for `m>=2`, `p=(2^m-1)/2^m`, and

\[
 {B(A)\over2p}={m\over2^m-1}.
\]

The normalized indicator spectrum has mass `p` at frequency `0` and the remaining mass `2^{-m}` uniformly over the `2^m-1` nonzero frequencies.  Hence

\[
 H(q_A)=h_2(2^{-m})+2^{-m}\log_2(2^m-1).
\]

At `m=5`,

\[
 H(q_A)=0.3554409590123045,
\qquad {B(A)\over p}=0.3225806451612903,
\]

so (12) fails; equivalently

\[
 {H(q_A)\over B(A)/(2p)}=2.203733945876288>2.
\]

This does not refute a larger dimension-independent constant, and of course does not refute FEI.  It says that the connected residual cannot be closed by the most naive coefficient-2 boundary estimate.

## 7. Exact finite checks

`verify_component_gauge.py` uses standard-library exact integer Walsh transforms and `Fraction` arithmetic for the algebraic/energy identities.  It checks:

- all `6,560` nonzero ternary derivative rows on three base bits for the exact phase-frustration identity (3);
- all `255` nonempty supports on three bits for the componentwise isoperimetric inequality and the component-gauge entropy comparison;
- the square-curl identity (4) on all `65,536` four-bit Boolean functions, all ordered coordinate-square instances: `6,291,456` exact checks;
- the explicit zero-influence-cost entropy gadget above; and
- equality in the parity-fragmentation bound.

The recorded verification status is `PASS`.  The largest numerical excess in the concavity comparison is `4.44e-16`, consistent with floating evaluation of logarithms after exact rational spectral weights; the combinatorial and Walsh identities themselves are exact.

Checker SHA-256 (executed bytes):

`9accaf2dfc8267764da9270777e79ca432baf99e30d7934ca82aeb7effa8792b`

Recorded verification-output SHA-256:

`c6ddb50c5941e423f7b561a072fbd26c14ce948b1ef1b81c08aad2701dd9ebc8`

Git readback blobs:

- `verify_component_gauge.py`: `06f0353169f4b63d5df1481adaf6f8b949318fcf`
- `verification.json`: `691f24512f7d2040b6a50724725b488440f584bf`

## 8. Residual universal obligation and next attack

The mechanism reduces the zero-cost phase issue to a much sharper residual.  The component selector itself is not free: its entropy is paid by transverse changes of sensitivity through (5)--(7).  What remains is the Fourier entropy internal to connected sensitive components, minus the overlap refund in (10).

A useful next target is therefore a **connected-row / overlap-refund dichotomy**: for a pivot row, either

- the connected-component spectral laws overlap strongly enough that `H(J|S)` refunds most of the component-label cost, or
- the component spectra are distinguishable, in which case their physical separation should force a summable transverse sensitivity/crossing payment beyond the bare boundary.

The deleted-vertex example proves that the residual cannot simply be assigned coefficient `2` times normalized boundary.  Any successful universal inequality must exploit more of the Boolean square compatibility, a multiscale boundary profile, or a nonlocal restriction payment.

This is compatible with, but intentionally distinct from, the concurrent curvature-refunded posterior-crossing handoff: the present object is the exact zero-cost gauge structure of a *single pivot derivative support* and its transverse square-curl fragmentation cost.
