# account04/B17 — exact character-cofactor gluing threshold: 6.3876 -> 5.1, with a Boolean obstruction below 4.8723

**Run:** `20260922T061604Z-b17-fei-a11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_BOOLEAN_ADVERSARY / ALL_GATE_REPLACEMENT`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Control resolution and exact live target


\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr),
\qquad V_u=4u(1-u),
\tag{G}
\]

with the current lifted candidate centered at about `6.521851214`.  The historical arithmetic/Shannon interface-D files were read as requested, including account02/B15 `20260922T054027Z-packet-price-kl-numaro`, but this run does **not** reopen that superseded branch.  The newest compatible all-gate B15 result consumed substantively is account03/B15

`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T052547Z-arity5-bias-tube/REPORT.md`,

which proves every five-input Boolean gate safe for the live candidate in the full bias tube `max_i |p_i-1/2| <= 10^-7`.  I also use the source-exact conditional-information cocycle from account01/B15

`proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260922T053153Z-sharp-biased-joint-credit/REPORT.md`

and its predecessor account02/B15

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T050513Z-sector-kl-character-split/REPORT.md`.

The last report proves that, at a uniform physical pivot with balanced Boolean restrictions and one restriction a character, the local gluing step is safe whenever the potential center satisfies

\[
C\ge C_{\rm sec}=6.387646448685102\ldots .
\]

That number came from several separate coarse estimates.  This run keeps the same exact Boolean source and the same KL credits, derives the exact one-variable threshold, and materially lowers the universal local threshold.

## 1. Exact Boolean character-cofactor geometry

Let the uniform pivot be `t`, and let both restrictions be balanced Boolean functions.  Assume

\[
f_0=\chi_A,
\qquad
f_1\in\{-1,+1\},
\qquad
 d=\Pr[f_0\ne f_1]\in(0,1/2].
\tag{1.1}
\]

Then

\[
b:=\widehat f_1(A)=\mathbb E[f_0f_1]=1-2d,
\qquad
m={1+b^2\over2}=1-2d+2d^2.
\tag{1.2}
\]

For the exact restriction cocycle, the branch posterior entropy and vertical mutual information are not merely lower-bounded: they are

\[
H(B\mid S)
=m\,h_2\!\left({b^2\over1+b^2}\right),
\tag{1.3}
\]

\[
I(S;J)
=h_2(d)-m\,h_2\!\left({d^2\over m}\right)-(1-m).
\tag{1.4}
\]

Indeed, the shared Fourier mode `A` has mixture mass `m`; every nonshared mode is supported in exactly one branch.  For the vertical layer, the shared mode has posterior `d^2/m`, while every nonshared mode has posterior `1/2`, with total nonshared mixture mass `1-m=2d(1-d)`.  These identities use the actual Boolean restrictions and preserve the full negative conditional-information credit.

Since both children and the parent are balanced, a symmetric potential enters only through its center `C=Gamma(1/2)`, and the local potential remainder is

\[
\mathcal R_C(d)=Cd-1-h_2(d).
\tag{1.5}
\]

Therefore the **exact** local center requested by this Boolean gluing geometry is

\[
\boxed{
Q(d)=
{2-m-m h_2\!\left({b^2\over1+b^2}\right)
+m h_2\!\left({d^2\over m}\right)\over d}.
}
\tag{1.6}
\]

Equivalently,

\[
\mathcal R_C+H(B\mid S)+I(S;J)=d\,[C-Q(d)].
\tag{1.7}
\]

Thus there is no hidden multidimensional remainder for this class: the exact local obstruction is the single scalar `Q(d)`.

## 2. A rigorous universal replacement: `Q(d) < 5.1`

The exact threshold (1.6) can be bounded without discarding the vertical KL logarithm.  Use only

\[
h_2(x)\ge4x(1-x)
\tag{2.1}
\]

for the branch entropy and

\[
h_2(x)\le x\log_2{e\over x}
\tag{2.2}
\]

for the remaining shared vertical posterior.  Then

\[
Q(d)\le U(d),
\tag{2.3}
\]

where

\[
\boxed{
U(d)=
{4(1-d)(d^2-d+1)\over 2d^2-2d+1}
+d\log_2{e(2d^2-2d+1)\over d^2}.
}
\tag{2.4}
\]

The key new point is that `U` has a strong global concavity estimate on the whole Boolean range:

\[
\boxed{U''(d)\le-16\qquad(0<d\le1/2).}
\tag{2.5}
\]

A direct differentiation gives

\[
U''(d)=-{2P(d)\over d(2d^2-2d+1)^3\ln2},
\]

with

\[
\begin{aligned}
P(d)={}&1-4d+6d^2-4d^3\\
&+\ln2\,(8d^4-24d^3+12d^2).
\end{aligned}
\]

After subtracting the amount needed for `-16`, one obtains

\[
P(d)-8d(2d^2-2d+1)^3\ln2=(1-2d)Q_1(d).
\tag{2.6}
\]

If the coefficient of `ln 2` in `Q_1` is nonnegative, then `Q_1>0` immediately.  If it is negative, use `ln2<7/10`; the resulting lower polynomial is

\[
{1\over5}
\bigl(112d^6-280d^5+364d^4-280d^3+164d^2-38d+5\bigr).
\tag{2.7}
\]

In the Bernstein basis on `t=2d in [0,1]`, the numerator in (2.7) has coefficients

\[
5,\quad {11\over6},\quad {7\over5},\quad {39\over20},\quad
{13\over4},\quad {41\over8},\quad {31\over4},
\tag{2.8}
\]

all strictly positive.  This proves (2.5), including the endpoint by continuity.

At `d_0=1/4`,

\[
U(d_0)= {39\over10}+{1\over4}{\ln(10)+1\over\ln2},
\tag{2.9}
\]

and

\[
U'(d_0)= -{34\over25}+{\ln(10)-7/5\over\ln2}.
\tag{2.10}
\]

Using only the elementary rigorous bounds

\[
0.69<\ln2<0.70,
\qquad
2.302<\ln10<2.303,
\tag{2.11}
\]

gives

\[
U(d_0)<5.096739130434783,
\qquad
-0.071429<U'(d_0)<-0.051304.
\tag{2.12}
\]

Strong concavity then gives, for every `d`,

\[
U(d)\le U(d_0)+U'(d_0)(d-d_0)-8(d-d_0)^2
\le U(d_0)+{|U'(d_0)|^2\over32}
<5.096899<5.1.
\tag{2.13}
\]

Therefore:

### Theorem B17-CHARACTER-COFACTOR-5.1

For every balanced Boolean character-cofactor split (1.1) at a uniform pivot,

\[
\boxed{C\ge5.1\quad\Longrightarrow\quad
\mathcal R_C+H(B\mid S)+I(S;J)>0.}
\tag{2.14}
\]

The current live center `6.521851214` is far above this threshold.  Consequently this entire source-realizable MUX-like class cannot be the first negative gluing node for the live candidate.

There is also a direct extremal consequence.  If `F` is the parent and `f_1` the noncharacter balanced child, the exact cocycle and the character base case imply

\[
D_C(F)={1\over2}D_C(f_1)+d[C-Q(d)].
\tag{2.15}
\]

Hence for the balanced uniform ratio `R(f)=H(f)/(I(f)-1)`, whenever the denominator is positive,

\[
\boxed{R(F)\le\max\{R(f_1),5.1\}.}
\tag{2.16}
\]

So above `5.1` this gluing operation cannot manufacture a new record: any parent record must already be present in the noncharacter child.  This is a genuine extremal reduction toward the owner's all-gate/decomposition target, not another independent remainder.

## 3. Exact Boolean adversary: the local threshold cannot be pushed below `4.8723`

The improvement to `5.1` is not a license to replace the exact KL credit by an arbitrarily smaller constant.  Take ten residual bits `x in Q_10`, an independent character bit `y`, and choose any Boolean `g(x)` which is `-1` on exactly 235 of the 1024 residual points and `+1` elsewhere.  Put

\[
f_0(y,x)=(-1)^y,
\qquad
f_1(y,x)=(-1)^y g(x).
\tag{3.1}
\]

Both restrictions are exactly balanced, and

\[
d=\Pr[f_0\ne f_1]={235\over1024}.
\tag{3.2}
\]

The adjacent rational-log checker proves

\[
\boxed{
4.872321043042353\ldots<Q(235/1024)<4.872321043042355\ldots .
}
\tag{3.3}
\]

Thus at the perfectly admissible Boolean center `C=4.8723`, the exact local gluing term is **negative**.  Any universal character-cofactor local theorem below `4.8723` is therefore false.  This is an actual finite Boolean witness on the pivot `t`, character bit `y`, and ten residual bits; it is not a non-Boolean spectral law.

The gap

\[
4.8723<C_{\rm char}<5.1,
\qquad
C_{\rm char}:=\sup_{0<d\le1/2}Q(d),
\tag{3.4}
\]

is now rigorous.  Floating diagnostics place the true scalar maximum near `d=0.22944` and `4.8723210718`, but that diagnostic is **not** used as a theorem here.

## 4. Exact checker and scope

`CHECKER.py` uses only the Python standard library and exact `Fraction` arithmetic.  Logarithms are enclosed by the positive atanh series with an explicit geometric tail.  It independently certifies `0.69<ln2<0.70`, `2.302<ln10<2.303`, the dyadic Boolean obstruction (3.3), the positive Bernstein coefficients (2.8), the `5.1` global upper certificate, and the literal balanced Boolean realization on 12 bits.

Executed checker SHA-256:

`4e7287910fcef1f8eec72249a0d2ae46b56d2a9753f0b2ecf6ac9802c9f9df51`

Executed output SHA-256:

`b39eca8799fd8197c1f218527c203ba95cc8bd878dff9da6ccdee9581024566f`

The checker prints `PASS`.

## 5. What changed and what remains open

- **Old compatible B15 bound:** zero-child-subsidy character-cofactor safety was proved only at `C >= 6.387646448685102...`.
- **New proved inference:** exact Boolean posterior geometry collapses the class to `Q(d)` and proves the universal replacement `C >= 5.1`.
- **Exact failed stronger claim:** a universal local center `C <= 4.8723` is impossible; the `d=235/1024` Boolean witness makes the exact gluing term negative.
- **Application to the live all-gate candidate:** since `6.521851214 > 5.1`, this entire character-cofactor family is excluded as a first negative gluing node; above `5.1` it cannot create a larger balanced-uniform record than its child.
- **Still open:** arbitrary composition-prime gates, arbitrary interior product biases, and the full all-gate inequality.  No finite universal FEI constant is proved here.

A next useful adversary should therefore leave the character-cofactor geometry: at a uniform pivot both restrictions must have genuinely multi-mode overlap, or at biased pivots it must leave the already-proved rare collars/center tube.  Repeating packet-only interface-D work would violate the later owner convergence order.

## 6. Privacy / provenance

This report contains only mathematical formulas, logical account/slot labels, source-bound repository paths and public scientific constants already present in the FEI programme.  It contains no credentials, scheduler identifiers, machine paths, benchmark gold, unrelated private data, email/Drive actions, paid or remote compute, workflow dispatch, notification changes, or public-release instruction.
