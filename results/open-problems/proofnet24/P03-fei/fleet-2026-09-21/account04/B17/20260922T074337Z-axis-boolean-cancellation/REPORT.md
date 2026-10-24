# account04/B17 — Boolean disagreement cancellation sharpens the five-prime axis collar

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_BOOLEAN_ADVERSARY_AND_REPLACEMENT`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  

## 0. Live candidate and newest B15 input

This run keeps the current source-exact all-gate candidate

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger(u)=\Gamma_0(u)+0.268204856\,u(1-u),
\]

and the exact gate defect

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
 [\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

The named newest complete other-account B15 result consumed is

`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T073015Z-axis-child-slack-kl/REPORT.md`,

report blob `fdef8360ab00c36a62d83f907a07045d7cb97bb0`, creation commit
`545d4e87b9c946225b4d33ade8bd636c01819678`.
It proves that every essential composition-prime five-input gate is safe when one
bias moves axially by at most `2e-5`, retaining the exact transport KL credit, and
records that its deliberately coarse envelope is already negative at `2.1e-5`.
That negative envelope is explicitly not a Boolean counterexample.

The present run attacks exactly that apparent boundary.  The `2e-5` statement
survives, and the replacement below increases the rigorously certified radius to

\[
\boxed{|p_k-1/2|\le 2.94\times10^{-5}},
\]

a factor `1.47` larger, without spending the negative KL credit.

## 1. Exact cancellation before taking absolute values

Fix the moving coordinate `k`, put all other biases at `1/2`, and write
`t=1/2+s`, `epsilon=|s|`.  Let `G_0,G_1` be the four-bit restrictions,

\[
I_b=I(G_b),\qquad q_b=\Pr[G_b=-1],\qquad
 d=\Pr[G_0\ne G_1].
\]

Let

\[
A(u)=\Gamma^\dagger(u)+h_2(V_u).
\]

Because the other four inputs are uniform, the gate defect itself is exactly

\[
\boxed{
D_G(t)=C^\dagger[(1-t)I_0+tI_1]
+dA(t)-\Gamma^\dagger((1-t)q_0+tq_1)-\widetilde H_G(t).
}
\tag{1.1}
\]

This is just the definition of the all-gate defect: for `j!=k` the pivotal
probability is the branch mixture, while
`It_k/V_t=d`.

Equation (1.1) matters because the B15 child-slack decomposition had separately
bounded the movement of the child defects, the branch output potentials, and the
branch entropies.  Those three signed movements cancel algebraically to the
single transverse term

\[
C^\dagger s(I_1-I_0).
\tag{1.2}
\]

No child cost is deleted; this is an exact regrouping before any triangle
inequality.  It removes an avoidable worst-case payment from the axial envelope.

Also

\[
|q_1-q_0|\le d,
\tag{1.3}
\]

because the two output indicators can differ only where `G_0` and `G_1` differ.
The source-valid regularity already used by B15, `|(Gamma^dagger)'|<85` on the
relevant interval, therefore charges the two potential motions by at most

\[
170d\,\epsilon.
\tag{1.4}
\]

The same regularity interval remains valid at the new radius: a nonconstant
five-bit gate has central output mass at least `1/32` on the smaller side, and
`1/32-2.94e-5>1/64`.

## 2. Boolean disagreement controls the transverse child cost

For a four-bit Boolean function `g`, let `B(g)` be the number of bichromatic
undirected edges in `Q_4`.  Then

\[
I(g)=B(g)/8.
\]

If two four-bit Boolean functions disagree on `m` vertices, changing those
vertices can affect at most `4m` cube edges.  Hence

\[
|I_1-I_0|\le m/2=8d.
\]

Global sign does not change influence.  Replacing `G_1` by `-G_1` changes the
Hamming disagreement from `16d` to `16(1-d)`, so in fact

\[
\boxed{|I_1-I_0|\le 8\min(d,1-d).}
\tag{2.1}
\]

Here `d=k/16` for an integer `k`.  Essentiality excludes `k=0`.  If `k=16`, then
`G_1=-G_0` pointwise, so the parent is a parity/XNOR composition of the pivot
literal with `G_0` (or a dictator in the degenerate case); it is not an essential
composition-prime gate.  Therefore every gate in the live prime class satisfies

\[
\boxed{k\in\{1,\ldots,15\}.}
\tag{2.2}
\]

This discrete Boolean fact is the first source of new radius.

## 3. A disagreement-sensitive entropy transport bound

Use B15's exact one-coordinate transport notation.  For every subset `A` of the
other four coordinates let

\[
c_A=\widehat G_{1/2^5}(A),\qquad
e_A=\widehat G_{1/2^5}(A\cup\{k\}),
\qquad r=2s.
\]

Then exactly

\[
\widehat G_t(A)=c_A+r e_A,
\qquad
\widehat G_t(A\cup\{k\})=\sqrt{1-r^2}\,e_A.
\tag{3.1}
\]

The Boolean pivot identity gives the sharper Parseval split

\[
\sum_A e_A^2=d,\qquad \sum_A c_A^2=1-d.
\tag{3.2}
\]

Let `w^0,w` be the central and perturbed spectral laws, `J=supp(w^0)`, `zeta`
the mass newly born outside `J`, and `rho` the law `w` conditioned on `J`.  From
(3.1)--(3.2),

\[
\zeta\le r^2d,
\tag{3.3}
\]

and

\[
\|w-w^0\|_1
\le 2|r|\sqrt{d(1-d)}+2r^2d.
\tag{3.4}
\]

There is also a small but exact improvement to the conditioning step.  Since all
mass outside `J` is exactly `zeta`,

\[
(1-\zeta)\|\rho-w^0\|_1
\le \|w-w^0\|_1,
\tag{3.5}
\]

rather than the looser `||w-w0||_1+zeta` bound.

Every nonzero central five-bit Fourier mass is at least `1/256`, so its surprise
lies in `[0,8]`.  The exact Shannon/KL identity on the old support, followed by
(3.4)--(3.5), gives

\[
\boxed{
\begin{aligned}
\widetilde H_G(t)-\widetilde H_G(1/2)
\le{}&8|r|\sqrt{d(1-d)}+12r^2d+h_2(r^2)\\
&-(1-\zeta)D_{\rm KL,2}(\rho\|w^0).
\end{aligned}}
\tag{3.6}
\]

The `12r^2d` consists of `8r^2d` from the old-support transport and at most
`4zeta<=4r^2d` from the at-most-sixteen new atoms.  The relative-entropy term is
retained with its exact favorable sign.

With `|r|=2epsilon`, (3.6) becomes

\[
16\epsilon\sqrt{d(1-d)}+48d\epsilon^2+h_2(4\epsilon^2)
-(1-\zeta)D_{\rm KL,2}(\rho\|w^0).
\tag{3.7}
\]

## 4. Replacement axial remainder

Combining (1.1)--(3.7) with the rigorous central prime reserve
`D_G(1/2)>=delta_0`, where

\[
\delta_0=0.0049065,
\]

gives the new source-valid inequality

\[
\boxed{
\begin{aligned}
D_{\Gamma^\dagger}(G;t)
\ge{}&\delta_0
-\epsilon\Bigl[
8C^\dagger\min(d,1-d)+170d+16\sqrt{d(1-d)}
\Bigr]\\
&-48d\epsilon^2-h_2(4\epsilon^2)
+(1-\zeta)D_{\rm KL,2}(\rho\|w^0).
\end{aligned}}
\tag{4.1}
\]

This is the replacement for the B15 coarse axial envelope.  It keeps the same
Boolean object, same `Gamma^dagger`, same normalization, and same negative KL
credit.

Because `d=k/16`, `1<=k<=15`, the linear coefficient in (4.1) is

\[
L_k={C^\dagger\over2}\min(k,16-k)+{85k\over8}
+\sqrt{k(16-k)}.
\tag{4.2}
\]

For `k<=8`, `L_k<=4C^dagger+93<120`.  For `9<=k<=14`, using only
`sqrt(k(16-k))<=8`, the affine upper bound is increasing in `k` and at `k=14`
is below `164`.  At `k=15`,

\[
L_{15}={C^\dagger\over2}+{1275\over8}+\sqrt{15}
< {C^\dagger\over2}+{1275\over8}+3.873
=166.508925607,
\tag{4.3}
\]

where `3.873^2>15`.  Thus (4.3) is a uniform upper bound over the entire actual
Boolean prime lattice.  Also `48d<=45`.

## 5. Certified radius 2.94e-5

Set

\[
\epsilon_*=2.94\times10^{-5}.
\]

Let `z=4 epsilon_*^2`.  Since `e<3<2^31 z`,

\[
h_2(z)\le z\log_2(e/z)<31z.
\]

The adjacent standard-library checker uses exact rational arithmetic and obtains

\[
L_*\epsilon_*+45\epsilon_*^2+31(4\epsilon_*^2)
=0.0048955084896858,
\]

with `L_*=166.508925607`.  Therefore, without spending any positive KL credit,

\[
\boxed{
D_{\Gamma^\dagger}(G;t)
>1.09915103142\times10^{-5}
+(1-\zeta)D_{\rm KL,2}(\rho\|w^0)>0.
}
\tag{5.1}
\]

Hence:

### Theorem B17-BOOLEAN-AXIS-CANCELLATION

For every essential composition-prime five-input Boolean gate `G`, every input
coordinate `k`, and every interior bias vector with

\[
p_j=1/2\;(j\ne k),\qquad
\boxed{|p_k-1/2|\le2.94\times10^{-5}},
\]

the current candidate satisfies

\[
\boxed{D_{\Gamma^\dagger}(G;p)>0.}
\]

This enlarges B15's source-valid axial radius by exactly a factor `1.47`.
The same refined worst-case envelope turns negative at `2.95e-5`; that is only
the next envelope boundary, not a counterexample to the gate inequality.

## 6. Exact Boolean adversary/stress witness

To make sure the new structural maximum is not an artifact of a relaxed
probability model, the checker uses the actual five-bit Boolean gate `P_*` whose
negative truth-table mask, in lexicographic bit order `x=0,...,31`, is

`0xe72b10d4`.

With the fifth bit as pivot its restrictions satisfy exactly

\[
d={15\over16},\qquad I(P_{*,0})={3\over2},\qquad I(P_{*,1})=2,
\]

so

\[
|I(P_{*,1})-I(P_{*,0})|={1\over2}
=8(1-d).
\]

Thus this genuine Boolean example **exactly saturates** the transverse
influence-difference bound at the worst disagreement lattice point `k=15`.
For its central Fourier pairs,

\[
\sum_A |c_Ae_A|={15\over64},
\]

while Cauchy gives `sqrt(15)/16`; the squared saturation ratio is exactly

\[
{15\over16}.
\]

So the entropy-transport stress is also close to its universal Cauchy ceiling.

The witness is not merely Boolean; it is composition-prime in the disjoint
all-gate sense.  For every proper variable block of size `2`, `3`, or `4`, the
checker forms the response vector on the complementary variables as the block
assignment varies.  A nontrivial Boolean child on such a block would allow at
most two distinct response vectors.  The witness has at least **three** for every
proper block.  All five coordinates are essential.  Hence no proper disjoint
Boolean substitution decomposes `P_*`.

This witness does **not** violate (5.1).  Its role is adversarial: it shows that
the difficult `d=15/16` Boolean/primality corner and near-maximal Fourier-pair
transport are physically realizable, so the replacement theorem is not buying
radius from a non-Boolean relaxation.

## 7. Verification and next missing implication

Checker:
`check_axis_boolean_cancellation.py`, SHA-256
`cc083ee6d0c818d13409ce10df5bb6018195e892dd74031c3e23199b2fd5fd01`.

Captured output SHA-256:
`7e896075d629a9a1d800b446553a08f28332915a2ade1a1b92b0468a17fe4ccd`.

The checker verifies the Boolean witness, essentiality, the exact proper-block
primality criterion, restriction influences, Fourier-pair identities, the
`15/16` Cauchy saturation ratio, all rational constants in the new envelope, the
positive `2.94e-5` reserve, and the negative `2.95e-5` envelope boundary.

**What remains open.** Full FEI is not proved.  To push the axial radius past this
new boundary one must now spend structure that (4.1) deliberately leaves unused:
the retained KL credit, sharper local information about `Gamma^dagger` than the
global slope `85`, or a joint incompatibility between near-saturation of the
potential and Fourier-transport terms.  Alternatively, an actual prime Boolean
gate/bias with negative live defect would falsify the candidate.  Repeating the
old `2e-5` checker or treating the `2.95e-5` envelope failure as a counterexample
would not advance the problem.

No benchmark gold, mocks, paid/remote compute, workflow dispatch, email/Drive,
notification enabling, or unrelated private data were used in this package.
