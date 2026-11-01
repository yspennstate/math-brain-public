# B14 — the arity-5 quarter-slice equality family is only a lifted 4-bit prime class

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_STRUCTURAL_REDUCTION`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Candidate version and newest correction

The live target is the all-gate inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

for one symmetric nonnegative finite-cap potential `Gamma`, every Boolean gate,
every arity and every product bias vector.  Full FEI remains open.

The old read-once fixed-point potential is no longer a viable universal
candidate: the current source-exact lower-bound work contains genuine balanced
Boolean gates with excess ratio above its cap, and the newer recursive
shared-core construction raises the certified balanced floor further to

\[
C_{\rm FEI}\ge
6.521850763518463531668608228451477683404661344\ldots.
\]

Accordingly this report does **not** try to restore the refuted old cap.  The
statement below is structural and is valid for **any** symmetric potential
`Gamma`; it therefore survives changes to the candidate envelope.

### Exact candidate `QEQ-FAC-v1`

Classify the essential equality cases in the already-certified five-input,
uniform-input, quarter-output theorem

\[
H(G)\le 6I(G)-4.
\tag{0.1}
\]

The prior suggested adversarial step was to perturb the input biases away from
`1/2` at an equality case and test whether a genuinely five-input margin can
rise.  `QEQ-FAC-v1` asserts that this cannot be a genuinely five-input source:
every essential equality gate factors through one literal and one member of a
single four-input composition-prime class.

## 1. Exact peer results consumed

Two completed inputs are used.

1. Same-account source theorem:
`fleet03/B17/20260922T003133Z-gate5-dyadic-unbalanced/REPORT.md`, report blob
`e654f9fe9cde273f6311a039b5fe9db69b00fd76`.  It proves (0.1) for **all**
`C(32,8)=10,518,300` quarter-output truth tables and, by exact integer
verification, proves that there are exactly **1,920** essential equality cases,
all with

\[
I=\frac54,\qquad H=\frac72.
\tag{1.1}
\]

It proposed perturbing one or two biases at a representative equality gate as
the next adversarial attack.

2. Required named other-account result:
`fleet04/B17/20260922T004252Z-gate-margin-repair/REPORT.md`, report blob
`cf92d6d1219b6ba4ee048b90205024c8075b41df`.  For every symmetric potential
`Gamma` and every disjoint block composition `F=A(B_1,...,B_m)`, it proves the
exact cocycle

\[
D_F=D_A+\sum_j\alpha_jD_{B_j},\qquad
W_F=W_A+\sum_j\alpha_jW_{B_j},
\tag{1.2}
\]

where `W=I/4-p_out(1-p_out)>=0` and `alpha_j>=0`.  Hence, whenever the
currencies are nonzero,

\[
c_F=\frac{W_Ac_A+\sum_j\alpha_jW_{B_j}c_{B_j}}
{W_A+\sum_j\alpha_jW_{B_j}},
\qquad c=-D/W,
\tag{1.3}
\]

with the zero-currency boundary handled directly.  Thus a composition cannot
create a larger required margin than all of its factors.

## 2. One equality gate and its exact four-bit factor

Take the equality support reported by B17,

\[
A_0=\{0,1,2,3,4,5,8,10\}\subset Q_5.
\tag{2.1}
\]

Every point in `A_0` has fifth bit zero.  Therefore, in `{0,1}` indicator
notation,

\[
\mathbf1_{A_0}(x_1,\ldots,x_5)
=\mathbf1_{\{x_5=0\}}\,B_0(x_1,\ldots,x_4),
\tag{2.2}
\]

where the balanced four-bit support of `B_0` is again

\[
\{0,1,2,3,4,5,8,10\}\subset Q_4.
\tag{2.3}
\]

The exact Walsh data are

\[
|\widehat B_0|_{\rm unnorm}:\quad
4^{\times8},\ 8^{\times2},
\]

and hence

\[
H(B_0)=3,\qquad I(B_0)=\frac32,
\tag{2.4}
\]

with coordinate influences

\[
\left(\frac14,\frac14,\frac12,\frac12\right).
\tag{2.5}
\]

The adjacent exact checker also proves `B_0` is composition-prime.  For every
nontrivial coordinate block of size two or three, the family of cofactors has
at least three distinct members, whereas compression through one Boolean block
bit would allow at most two.

For the lifted five-bit gate the exact Walsh magnitude signature is

\[
4^{\times16},\ 8^{\times4},\ 16^{\times2},
\]

so

\[
H(G_0)=\frac72,\qquad I(G_0)=\frac54,
\tag{2.6}
\]

and its influences are

\[
\left(\frac18,\frac18,\frac14,\frac14,\frac12\right).
\tag{2.7}
\]

Thus it is an all-five-coordinates-essential equality case of (0.1), despite
being a nontrivial disjoint composition.

## 3. PROVED: all 1,920 essential equality cases are this one orbit

Apply all five input-coordinate permutations and all five literal flips to
`A_0`.  They preserve output mass `1/4`, exact `H`, exact `I`, equality in
(0.1), and structural decomposability.  The checker constructs the orbit and
finds exactly

\[
\boxed{1920}
\tag{3.1}
\]

distinct truth sets.

Moreover every one lies in a **unique** coordinate face.  Each of the ten
coordinate-literal faces contains exactly

\[
\boxed{192}
\tag{3.2}
\]

members.  Therefore each orbit element has a unique decomposition

\[
\mathbf1_A=L\cdot B,
\tag{3.3}
\]

where `L` is a literal and `B` is input-NPN-equivalent to the single four-bit
prime gate `B_0`.

The peer theorem says there are exactly 1,920 essential equality cases in the
entire quarter slice.  Since (3.1) gives 1,920 distinct equality cases, the two
sets coincide.  Hence:

### Theorem — complete quarter-equality factorization

Every essential five-input, uniform-input, quarter-output gate satisfying
`H=6I-4` is input-NPN-equivalent to (2.2).  In particular, every such gate is a
binary AND/OR-type composition of one literal and the same four-bit
composition-prime NPN class.

This uses the already-certified exhaustive equality count plus a new exact
orbit/factorization certificate; it is not inferred from random search.

## 4. PROVED: arbitrary bias perturbation reduces globally to arity four

The factorization in (3.3) is a truth-table identity, so it remains valid under
**every** product bias vector, not only at the uniform point.  Let `q` be the
output bias of the four-bit factor `B`, and regard the gate as a binary outer
AND/OR-type gate `A` fed by the literal and `B`.  Apply the other-account
cocycle (1.2)--(1.3).  For every symmetric potential `Gamma`,

\[
\boxed{
 c_G(p_1,\ldots,p_5)
 \le
 \max\{c_{A}(p_L,q),\ c_B(p_1,\ldots,p_4)\}.
}
\tag{4.1}
\]

The identity remains valid in the zero-currency boundary cases by the direct
form of (1.2).

Consequently, if any bias perturbation of any one of the 1,920 equality gates
exceeds a threshold `T`, then either the binary outer gate already exceeds `T`
or the single four-bit prime factor class already exceeds `T`.  The five-input
lifting itself cannot be the first source of the excess.

This directly retires the proposed search strategy of treating the equality
family as a genuinely new arity-five adversarial region.  Its correct target is
one four-input prime NPN class.

## 5. Attempted refutation and dead route

The natural refutation of `QEQ-FAC-v1` would be an essential equality set not
contained in any coordinate face.  The exact construction found none:

- constructed equality orbit size: `1920`;
- peer-certified total essential equality count: `1920`;
- every constructed member has exactly one containing coordinate face;
- members per literal face: `192` each.

Therefore the counterexample attempt fails exactly, not numerically.

**Dead route:** broad five-dimensional bias perturbation of these 1,920
quarter-slice equality gates as if they were prime arity-five candidates.
Equation (4.1) shows that any success there was already a binary or four-bit
success.

## 6. Remaining implication and next recipient

This reduction does **not** prove a finite universal FEI constant and does not
rescue any already-refuted fixed cap.  The current all-gate programme still
needs a finite-cap `Gamma` satisfying (G) for every gate and every bias.

For this exact equality family, the next obligation is now small and precise:
for the live successor potential `Gamma`, certify the all-bias margin of the
single four-bit prime class `B_0` with support (2.3).  Either

\[
 c_{B_0}(p)\le T\quad\text{for all }p\in(0,1)^4
\tag{6.1}
\]

at the intended live threshold `T`, in which case (4.1) controls the entire
1,920-member five-bit family once the binary outer gate is paid, or find a
bias vector violating (6.1), which is already an arity-four obstruction.

**Next recipient:** `fleet04/B17`, with (4.1) and the exact `B_0` truth table.
This also fits the owner's smaller interval-arithmetic arity-three/four job.

## 7. Verification

`CHECK_EQUALITY_FACTORIZATION.py` is standard-library only.  It uses exact
integer Walsh transforms and `Fraction`, verifies the exact Fourier signatures,
`H`, `I`, all coordinate influences, the composition-prime cofactor condition,
the 1,920-element input-NPN orbit, unique face containment, and the 192-per-face
count.

Executed checker SHA-256:

`6313b9e7f90e8e36bdaef6575e152d4896521b1373139cb23ab53289b5f85702`

Captured clean stdout SHA-256:

`036c60aafdf4f2234316f92abcd622d2cd3fc807344f48b781ef33e506ca06c4`

The checker exit status was zero.  No floating-point sign decides the theorem.
No paid/remote compute, workflow dispatch, email, Drive operation, scheduler
mutation, public posting, credential, or unrelated private source was used.
