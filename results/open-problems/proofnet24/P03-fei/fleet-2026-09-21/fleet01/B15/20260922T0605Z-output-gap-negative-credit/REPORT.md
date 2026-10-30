# B15 — empty-atom mutual-information refund and an unequal-output rare-pivot collar

**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.

**Full unrestricted uniform-cube Fourier entropy-influence:** **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Fresh repository controls and exact mathematical source files were read directly; no authenticated cognitive-brain receiver/context entered the derivation.

## 0. Live candidate, full conditional chain, and exact peer inputs

The current source-exact all-gate target is

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u).
\tag{0.1}
\]

The fixed candidate is the immutable `LIMIT-PRIME-GATE-LIFT-v1` candidate from

`fleet01/B18/20260922T0325Z-addressing-star-cdagger/REPORT.md`
(report blob `6deb28dc6f2e8f36da01fdc7ac24f600f7553a5c`):

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(u)=\Gamma_0(u)+0.268204856\,u(1-u).
\tag{0.2}
\]

The complete conditional deduction remains:

1. prove `D_{Gamma^dagger}(P;p)>=0` for every finite composition-prime Boolean gate and every interior product bias;
2. use the exact nonnegative gate-composition cocycle to obtain the same for every Boolean gate;
3. apply the all-gate reformulation to obtain `H(f)<=C^dagger I(f)` for every uniform-cube Boolean `f`.

Only step 1 remains universal and unpaid.

Two exact other-account results are consumed and applied here.

* `fleet04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`, blob `d32321447c5f30282f243d9a2907ec719d483c92`, proves the exact one-pivot cocycle and the mandatory information credit
  \[
  D_\Gamma(G)=qD_\Gamma(G_0)+tD_\Gamma(G_1)+\mathcal R_{\Gamma,j}+\mathcal C_j,
  \qquad
  \mathcal C_j=H(B\mid S)+I(S;J).
  \tag{0.3}
  \]
* `fleet03/B15/20260922T052547Z-arity5-bias-tube/REPORT.md` proves, from the committed h96 source bounds, the source-valid Lipschitz estimate
  \[
  |(\Gamma^\dagger)'(r)|<85
  \quad\text{for }r\in[1/64,63/64].
  \tag{0.4}
  \]
  The derivation of (0.4) depends only on the source potential and this scalar interval, not on five-input structure.

The immediate predecessor in this same B15 line is
`fleet01/B15/20260922T053153Z-sharp-biased-joint-credit/REPORT.md`. It proved

\[
\mathcal C_j\ge H(B\mid S)
\ge \Psi\!\left(\sqrt{V_t}\,|1-2\delta|\right),
\tag{0.5}
\]
where
\[
\Psi(z)=h_2\!\left({1-\sqrt{1-z^2}\over2}\right),
\qquad
\delta=\Pr(G_0\ne G_1),
\tag{0.6}
\]
and used this negative posterior-entropy credit to exclude rare biased pivots with balanced children, `min(t,1-t)<=1/64`, `delta>=1/4`.

The old first missing implication was to retain enough negative information credit when the two child output measures are unequal. This report gives an additional exact mutual-information refund tied to the empty Fourier atom and then uses the existing posterior credit to prove an explicit unequal-output collar.

## 1. Exact empty-atom mutual-information refund

Fix a physical pivot `j` of bias `t`, put `q=1-t`, and expand the two actual Boolean restrictions in the common biased Walsh basis:

\[
f_0=\sum_S a_S\chi_S,
\qquad
f_1=\sum_S b_S\chi_S.
\tag{1.1}
\]

As in the exact cocycle, define

\[
T_S=q a_S^2+t b_S^2,
\qquad
\theta_S={tq(b_S-a_S)^2\over T_S}
\quad(T_S>0).
\tag{1.2}
\]

Under the associated joint law, `S` has distribution `T` and the vertical Fourier-layer bit `J` satisfies

\[
\Pr(J=1\mid S)=\theta_S,
\qquad
\mu:=\Pr(J=1)=\operatorname{It}_j=V_t\delta.
\tag{1.3}
\]

Write the child output measures as

\[
r_b=\Pr(G_b=1),
\qquad
m_b=1-2r_b=\widehat f_b(\varnothing),
\qquad
d=|r_1-r_0|.
\tag{1.4}
\]

The probability of the empty spectral atom under `T` is

\[
\boxed{s=q m_0^2+t m_1^2.}
\tag{1.5}
\]

When `s>0`, its conditional vertical-layer probability is exactly

\[
\boxed{
\theta_0={tq(m_1-m_0)^2\over s}
={V_t d^2\over s}.
}
\tag{1.6}
\]

Let `E=1_{\{S=\varnothing\}}`. Because `E` is a deterministic function of `S`, data processing gives

\[
I(S;J)\ge I(E;J).
\tag{1.7}
\]

For `0<s<1`, the conditional vertical-layer probability on the nonempty group is forced by the total mean:

\[
\boxed{
\nu={\mu-s\theta_0\over1-s}
={V_t(\delta-d^2)\over1-s}.
}
\tag{1.8}
\]

This is a genuine probability because it is an actual conditional mean; algebraically `d<=delta` also gives `delta-d^2>=0`.

Therefore the coarsened mutual information is exactly

\[
\boxed{
I_0:=I(E;J)
=h_2(\mu)-s h_2(\theta_0)-(1-s)h_2(\nu)\ge0.
}
\tag{1.9}
\]

At `s=0` or `s=1`, define `I_0` by the actual conditional law (equivalently by continuity); then `I_0=0` at either degenerate endpoint.

Combining (0.5), (1.7), and (1.9) proves the first new source-exact credit theorem:

### Theorem 1.1 — posterior plus empty-atom joint credit

For every actual Boolean restriction pair and every interior pivot bias,

\[
\boxed{
\mathcal C_j
\ge
\Psi\!\left(\sqrt{V_t}\,|1-2\delta|\right)+I_0.
}
\tag{1.10}
\]

This adds no arbitrary spectral law and no uncharged label: `I_0` is a data-processing lower bound on the **existing** exact term `I(S;J)`.

There is a useful fully scalar corollary. In bits, Pinsker gives

\[
D_2(\operatorname{Ber}(x)\Vert\operatorname{Ber}(y))
\ge {2\over\ln2}(x-y)^2.
\]

Since `mu=s theta_0+(1-s)nu`, applying this to the two conditional laws yields

\[
\boxed{
I_0
\ge
{2V_t^2\over\ln2}
{(d^2-s\delta)^2\over s(1-s)}
\qquad(0<s<1).
}
\tag{1.11}
\]

Thus unequal child means generate an explicit extra information currency unless the empty/nonempty split happens to carry no information about the vertical layer.

## 2. Exact insertion into the local all-gate cocycle

The exact fleet04/B17 local term is

\[
\begin{aligned}
\mathcal R_{\Gamma,j}={}&
q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(r)\\
&+\delta\bigl(\Gamma(t)+h_2(V_t)\bigr)
-h_2(t)-h_2(V_t\delta),
\end{aligned}
\tag{2.1}
\]
where `r=qr_0+tr_1`.

For the live candidate, set

\[
u=\min(t,1-t),\qquad V=4u(1-u).
\]
The predecessor report proved that the scalar part

\[
F_u(\delta)=
\delta\bigl(\Gamma^\dagger(u)+h_2(V)\bigr)
-h_2(u)-h_2(V\delta)
+\Psi\!\left(\sqrt V\,|1-2\delta|\right)
\tag{2.2}
\]
satisfies, for `u<=1/64` and `delta>=1/4`,

\[
\boxed{F_u(\delta)>0.4194\,u.}
\tag{2.3}
\]

Indeed that report proves `F_u` is increasing in `delta` on `[1/4,1]` and

\[
{F_u(1/4)\over u}>0.2274\log_2(1/u)-0.945\ge0.4194.
\]

The new credit theorem therefore gives the strengthened source-exact local lower bound

\[
\boxed{
\mathcal R_{\Gamma^\dagger,j}+\mathcal C_j
\ge
q\Gamma^\dagger(r_0)+t\Gamma^\dagger(r_1)-\Gamma^\dagger(r)
+F_u(\delta)+I_0.
}
\tag{2.4}
\]

Equation (2.4) is the precise negative-entropy insertion required by the current route. The old balanced-child proof simply set the first line to zero and discarded `I_0`; neither simplification is made in the theorem above.

## 3. New theorem — an explicit unequal-output rare-pivot collar

Assume

\[
0<u=\min(t,1-t)\le{1\over64},
\qquad
\delta\ge{1\over4},
\tag{3.1}
\]
and suppose the two child output measures lie in the source-valid interior band

\[
\boxed{r_0,r_1\in[1/64,63/64].}
\tag{3.2}
\]

Let
\[
d=|r_1-r_0|.
\]
Because the whole segment between `r_0` and `r_1` remains inside (3.2), the consumed fleet03/B15 source theorem (0.4) gives

\[
\begin{aligned}
q\Gamma^\dagger(r_0)+t\Gamma^\dagger(r_1)-\Gamma^\dagger(r)
&\ge
-q\,85|r-r_0|-t\,85|r_1-r|\\
&=-170tq\,d\\
&\ge-170u\,d.
\end{aligned}
\tag{3.3}
\]

Insert (2.3) into (2.4), and retain the new exact credit only with its safe sign `I_0>=0`:

\[
\boxed{
\mathcal R_{\Gamma^\dagger,j}+\mathcal C_j
>
u(0.4194-170d).
}
\tag{3.4}
\]

Consequently:

### Theorem 3.1 — rare-pivot unequal-output tube

For every actual Boolean physical pivot satisfying (3.1)-(3.2), if

\[
\boxed{|r_1-r_0|\le{1\over512},}
\tag{3.5}
\]
then

\[
\boxed{
\mathcal R_{\Gamma^\dagger,j}+\mathcal C_j
>
{13979\over160000}\,u
=0.08736875\,u>0.
}
\tag{3.6}
\]

The exact arithmetic is

\[
0.4194-{170\over512}
={2097\over5000}-{85\over256}
={13979\over160000}.
\]

The clean constant `1/512` is conservative; the same proof works for every

\[
|r_1-r_0|<{2097\over850000}=0.0024670588\ldots.
\tag{3.7}
\]

This strictly extends the predecessor B15 theorem from equal-output children (in particular balanced children) to a genuine unequal-output neighborhood. It is a local exclusion theorem in the exact restriction cocycle, so a minimum-essential-arity counterexample cannot use such a pivot as a negative gluing step.

Notice that (3.6) does **not** spend the new `I_0` quantitatively; it only keeps it nonnegative. Hence (1.10)-(1.11) remain available to enlarge the output tube further, especially where the empty Fourier atom distinguishes the vertical layer strongly.

## 4. Boundary and adversarial checks

The proof preserves all exact signs and has the expected degenerate behavior.

* If `r_0=r_1`, the potential Jensen term in (2.4) vanishes for **any** common child output measure, not only `1/2`. Thus the previous rare-pivot theorem automatically extends from balanced children to every equal-output pair; (3.6) is a quantitative neighborhood of that larger equality locus.
* For a literal node, `r_0=0,r_1=1,delta=1`; here `s=1`, the coarsened `I_0` is zero, while the posterior term in (1.10) becomes the full `h_2(t)` credit required for exact equality. Thus the new bound does not destroy the known literal cancellation.
* The theorem uses an actual Boolean pair through the signed overlap input behind `Psi`; arbitrary subset/spectral probability laws are not admitted.
* Addressing, sparse-defect, tribes, recursive-majority, tensor, and biased-limit obstructions that killed credit-free or coordinatewise bounds do not alter the identity (1.9). No claim is made that (1.10) alone controls them globally.

## 5. Old/new missing implications

**Old missing implication.** For the fixed `Gamma^dagger`, close LOCAL-GLUING with the exact `H(B|S)+I(S;J)` credit when child output measures are unequal, or construct a genuine Boolean violating gate. The previous B15 theorem only stated its explicit rare-pivot exclusion for balanced children.

**New proved inference.** The unused part `I(S;J)` contains the explicit empty-atom refund (1.9), with quantitative Pinsker form (1.11), and the already-proved posterior credit plus the source-valid potential Lipschitz theorem close the unequal-output collar (3.1)-(3.6).

**New first missing implication.** Enlarge or remove the restrictions `|r_1-r_0|<=1/512` and `r_b in[1/64,63/64]`, preferably by spending `I_0` quantitatively against the source-potential Jensen deficit instead of discarding it. Separately, pivots with `delta<1/4` and intermediate pivot bias still remain.

**Implication to full FEI.** This is a genuine reduction of the exact local gluing obstruction for the fixed candidate, but it does not establish LOCAL-GLUING universally, the all-prime-gate inequality, or full FEI.

**Classification:** `ESSENTIAL_STEP_APPLIED`.

No novelty or publication-priority claim is made.
