# HARD8-05 — part 2: the reciprocal modulus-40 pair is not universal

**Status:** exact strategic obstruction; full Erdős–Straus conjecture still open.

The main report in this run proposed studying the zero-exception branches of the reciprocal `(2,5)/(5,2)` modulus-40 portals. A concrete hard-prime example shows that the correct goal is **not** to prove those branches impossible. They genuinely occur simultaneously, even on a classical Mordell hard residue class, and must instead be rescued by additional portal moduli.

## 1. Exact example `n=1201`

The integer

\[
n=1201
\]

is prime and

\[
1201\equiv361\pmod{840},
\]

so it lies in the classical six-class hard residue set.

For the `(2,5)` portal,

\[
N_1=2n+5=2407=29\cdot83.
\]

Modulo 40,

\[
29\equiv29,\qquad83\equiv3.
\]

Both residues lie in

\[
K_3=\{1,3,7,9,21,23,27,29\}
=\ker\left(\frac{-5}{\cdot}\right),
\]

which avoids `-1=39`. Indeed the complete divisor set of `2407` is

\[
\{1,29,83,2407\},
\]

with residues

\[
1,29,3,7\pmod{40};
\]

none is 39. Thus the `(2,5)` portal fails, and it fails in a **zero-exception** quadratic-kernel branch.

For the reciprocal `(5,2)` portal,

\[
N_2=5n+2=6007,
\]

and `6007` is prime. Its only divisor residues modulo 40 are

\[
1,7,
\]

again never 39. Since `7` lies in both `K_3` and `K_5`, this reciprocal portal also fails in a zero-exception branch.

Therefore

\[
\boxed{
\text{both modulus-40 reciprocal portals fail at the hard prime }n=1201.
}
\tag{1.1}
\]

This rigorously refutes the prospective sub-strategy “prove that one of `(2,5)` or `(5,2)` always succeeds on the Mordell hard fibers.”

## 2. Exact rescue by a different portal

The same `n=1201` is immediately solved by the `(a,u)=(4,1)` portal, whose modulus is 16:

\[
4n+1=4805=5\cdot31^2.
\]

Take

\[
s=31\equiv-1\pmod{16}.
\]

Then

\[
q=\frac{4n+1}{31}=155,
\qquad
 t=\frac{31+1}{16}=2.
\]

The exact Type-II identity gives

\[
x=uqt=310,
\]

\[
y=anqt=4\cdot1201\cdot155\cdot2=1,489,240,
\]

\[
z=anut=4\cdot1201\cdot1\cdot2=9,608.
\]

Hence

\[
\boxed{
\frac4{1201}
=
\frac1{310}
+
\frac1{1,489,240}
+
\frac1{9,608}.
}
\tag{2.1}
\]

Cross multiplication gives exactly

\[
4xyz=1201(yz+xz+xy).
\]

So the zero-exception modulus-40 obstruction is real, but it is not an obstruction to Erdős–Straus itself; it is only an obstruction to that portal pair.

## 3. Consequence for the next proof architecture

This example changes the priority of the next attack.

The affine relation

\[
5A-2B\in\{3,21\}
\]

should no longer be used primarily to seek a contradiction to simultaneous zero-exception modulus-40 failure. Such failures exist. Instead the target should be a **portal-transfer theorem**:

> if both reciprocal modulus-40 portals fail with their prime factors trapped in the `K_3/K_5` kernels (plus the bounded exceptional factors from the main report), then one of a controlled list of auxiliary portals—starting with modulus 16 `(4,1)` and then moduli 48/60—must succeed, or the factor structure becomes strictly more rigid.

The example `1201` shows exactly what such a theorem would need to capture: support in `K_3` at modulus 40 forces no direct contradiction, but `4n+1` contains the target divisor `31 == -1 mod16`.

A useful next finite/symbolic experiment is therefore to classify simultaneous modulus-40 failures by which auxiliary maximal-escape subgroup traps `4n+1`, `n+4`, `3n+4`, and `3n+5`. The new exact subset-product budgets from the main report keep each auxiliary failure within a bounded exceptional-residue hierarchy.

## 4. Claim boundary

Equation (1.1) is an exact counterexample only to the **reciprocal-portal sub-strategy**, not to the Erdős–Straus conjecture. Equation (2.1) explicitly solves Erdős–Straus for this `n`. No universal portal-transfer theorem has yet been proved.