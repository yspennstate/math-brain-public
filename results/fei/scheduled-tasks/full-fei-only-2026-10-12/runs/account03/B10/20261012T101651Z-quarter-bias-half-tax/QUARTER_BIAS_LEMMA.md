# B10 / A046: a dimension-free quarter-bias strengthening of physical-reveal uncertainty

**Status:** AUTHOR-PROVED, UNVERIFIED BY INDEPENDENT REVIEW. **Full FEI: OPEN.**
**Programme:** FULL-FEI-ONLY-20261012, revision 2026-10-12.1.
**Exact target:** the existing frozen \`B10-A046-HALF-BIAS-TAX@1\` potential (not a new FEI conjecture).

## The restricted theorem

Let \`n>=1\` and \`f:{0,1}^n->{-1,1}\` be any genuine Boolean sign function. Under any independent product distribution with all coordinate biases in \`(0,1)\`, reveal one physical coordinate \`i\` whose probability of value one is **exactly 1/4 or 3/4**. Put \`Z=X_i\`. Draw a parent spectral set \`S\` from its squared normalized product-biased Fourier coefficients and let \`T=S\setminus{i}\`. In the natural physical-restriction coupling, draw a conditional child spectral set \`T'\` by first drawing \`Z\`, then squared Fourier coefficients of \`f|_{X_i=Z}\`. The laws of \`T\` and \`T'\` coincide; use \`T\` for this common marginal. Define in **bits**:

\`M_i=H(1_{i in S}|T)\`, \`J_i=I(Z;T')\`, and
\`delta(p)=h_2(p)+log_2(max(p,1-p))\`.

Then
\[
J_i\le M_i+\tfrac12\delta(p)-\varepsilon_\star,\qquad
\varepsilon_\star=\frac{37}{32}-\frac{45}{128\ln 2}
                 -\left(2-\frac78\log_2 3\right)>0.
\]
In particular, the frozen half-tax candidate holds **strictly**, with an explicit universal margin for this fixed-bias, singleton-reveal class. Numerically \`epsilon_star=0.03589471281848533\` bits. There is no lower bound on any OTHER coordinate bias, and no restriction on dimension or f.

The statement has no implication that the whole p-continuum, a multicoordinate block, global nonreusing payment, or FEI is proved.

## Step 1: exact two-basis spectral fibers

Write \`a_T\` and \`b_T\` for the real normalized biased Fourier coefficients of the two Boolean restrictions \`f|_{Z=0}\` and \`f|_{Z=1}\` on the remaining coordinates, and \`q_T=(1-p)a_T^2+p b_T^2\`. Parseval gives \`sum_T q_T=1\`. For each \`q_T>0\`, the real vector
\[
v_T=\frac{(\sqrt{1-p}\,a_T,\sqrt p\,b_T)}{\sqrt{q_T}}
\]
has Euclidean norm one. The two squared coordinates of \`v_T\` give the posterior law \`Z|T\` in the physical child coupling. The orthogonal matrix
\[
U_p=\begin{pmatrix}\sqrt{1-p}&\sqrt p\\-\sqrt p&\sqrt{1-p}\end{pmatrix}
\]
gives the parent's coordinate-i Fourier coefficients: \`((1-p)a_T+p b_T,\sqrt{p(1-p)}(b_T-a_T))\`. Consequently,
\[
M_i=\sum_{T:q_T>0}q_T H((U_pv_T)^2),\qquad
J_i=h_2(p)-\sum_{T:q_T>0}q_T H(v_T^2).
\]
Here \`H((u_0,u_1)^2)\` means \`h_2(u_1^2)\` for unit u. A zero-mass fiber contributes zero and is **never normalized**. Thus any scalar bound
\[
H(v^2)+H((U_pv)^2)\ge L
\]
implies \`J_i-M_i<=h_2(p)-L\`, with no assumption about the number or relative sizes of the nonzero fibers.

## Step 2: a self-contained scalar lemma at overlap cos(pi/6)

For every **real** unit vector \`v\` and for \`p=1/4\`,
\[
H(v^2)+H((U_pv)^2)\ge
L:=\frac{37}{32}-\frac{45}{128\ln2}.
\]
The same statement holds at \`p=3/4\`. Proof follows without using any unproved FEI estimate.

Define \`g(x)=h_2((1+x)/2)\`, \`s=x^2\`, and \`t=ln2-7/12\`. The convergent series with the convention \`0 log0=0\` is
\[
g(x)=1-\frac1{\ln2}\sum_{k=1}^\infty
\frac{x^{2k}}{(2k)(2k-1)},\qquad |x|\le1.
\]
Since \`s^k<=s^3\` for \`k>=3\` and \`0<=s<=1\`,
\[
g(x)\ge1-\frac{Q(s)}{\ln2},\qquad
Q(s)=\tfrac12s+\tfrac1{12}s^2+t s^3. \tag{1}
\]
The series telescopes at \`x=1\`, so \`t\` is the exact nonnegative tail sum. Also \`0<t<1/6\`: \`ln2<3/4\` follows from \`exp(3/4)>1+3/4+(3/4)^2/2>2\`.

Write the two Bloch imbalances of the real qubit as \`cos(theta)\` and \`cos(theta-pi/3)\`, because the rotation by \`pi/6\` on state vectors doubles its angular effect on squared amplitudes. Set \`s_1=cos^2(theta)\`, \`s_2=cos^2(theta-pi/3)\`, and \`c=cos(2theta-pi/3)\`. Exact trigonometry gives
\[
u=s_1+s_2=1+\tfrac12c,\quad
v=s_1s_2=\tfrac14(c+\tfrac12)^2,\quad -1\le c\le1.
\]
Using \`s_1^2+s_2^2=u^2-2v\` and \`s_1^3+s_2^3=u^3-3uv\`,
\[
F(c):=Q(s_1)+Q(s_2)=
-\tfrac t4c^3-(\tfrac{3t}8+\tfrac1{48})c^2
+(\tfrac{21t}{32}+\tfrac7{24})c
+\tfrac{13t}{16}+\tfrac{55}{96}.
\]
Its derivative is concave as a quadratic in \`c\`:
\[
F'(c)=-\tfrac{3t}4c^2-(\tfrac{3t}4+\tfrac1{24})c
+\tfrac{21t}{32}+\tfrac7{24}.
\]
The minimum of a concave function on \`[-1,1]\` occurs at an endpoint, and
\[
F'(-1)=\tfrac13+\tfrac{21t}{32}>0,\qquad
F'(1)=\tfrac14-\tfrac{27t}{32}>
\tfrac14-\tfrac{27}{192}>0.
\]
Thus \`F(c)<=F(1)=27(1+t)/32\`. Substitution in (1) gives
\[
g(\cos\theta)+g(\cos(\theta-\pi/3))
 \ge 2-\frac{27(1+t)}{32\ln2}
 =\frac{37}{32}-\frac{45}{128\ln2}=L.
\]
For \`p=3/4\`, the two state measurement bases have angle \`pi/3\` and Bloch-axis angle \`2pi/3\`; changing the sign of one binary imbalance leaves entropy invariant and replaces their relative angle by \`pi/3\`. The identical proof applies.

## Step 3: strict margin, proved with rational log bounds

At either quarter bias \`delta(p)=log_2(3)/4\` and
\[
h_2(p)-\tfrac12\delta(p)=2-\tfrac78\log_2 3=:T.
\]
The inequality \`L>T\` is exactly \`112 ln3 - 108 ln2 >45\`. Both inequalities below are elementary and strict:
\[
\ln3=2\sum_{k=0}^\infty\frac{2^{-(2k+1)}}{2k+1}
>1+\tfrac1{12}+\tfrac1{80},\qquad \ln2<\tfrac7{10}.
\]
The latter follows since \`exp(7/10)>1+7/10+(7/10)^2/2+(7/10)^3/6>2\`. Therefore
\[
112\ln3-108\ln2 >
112(1+\tfrac1{12}+\tfrac1{80})-108\tfrac7{10}
=\frac{707}{15} 
\]
The correct *difference from 45* is \`32/15>0\` (equivalently the preceding expression is \`707/15=47.133333...\`), establishing \`epsilon_star>0\` without decimal certification. Combining the scalar lemma and Step 1 completes the restricted theorem.

## Counterfactual, gaps and boundaries

This is a **restricted fixed-reveal-bias theorem**, not an assertion of universal \`kappa=1/2\`. The B09 corrected two-bit gate still refutes the **zero**-tax proposal; the source’s rare-boundary coefficient \`1/2\` concerns \`p downarrow0\`, not \`p=1/4\`. No passage to \`p->0\`, arbitrary physical blocks, non-product measures, differential entropy, or an actual FEI proof is justified. The proof uses a uniform sum of fiberwise 2D entropy bounds; it does not read or alter held evaluation banks. All logs in the qubit lemma are natural, while final Shannon entropy and \`J,M,delta\` are bits. Constant f and zero Fourier fibers require no division by influence or by zero mass.

**Next mathematical target:** quantify \`L(p)\` for a *continuous interval* around \`p=1/4\` and its image under \`p->1-p\`, using perturbation of the exact qubit overlap, not a fixed-\`p\` lower bound near \`p=0\`. Test whether the strengthened interval reaches the two-bit rare saturation mechanism; if not, state the singular obstruction exactly. Independently ask A087/A092 to reconstruct the scalar polynomial and the spectral posterior coupling.

**Source/priority ledger:** The accepted B09 product-biased Maassen--Uffink fiber theorem supplies the conservative coefficient-one comparison. The \`B10-A046-HALF-BIAS-TAX@1\` frozen candidate and the author-checked account01/B10/A047 two-bit endpoints were read at the source paths and blob SHAs in \`SOURCES.json\`. This proof is a separately scoped, self-checked all-dimensional one-bias extension; no novelty versus external mathematical literature or independent mathematical acceptance is certified.
