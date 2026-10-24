# HARD10-03 — append-only receipt / certificate addendum

The full `d=3` conjecture remains **OPEN / PARTIAL**. This addendum does not overwrite the mathematical checkpoint. It records exact delivery/readback receipts, the finite-state certificate, and one immediate corollary of `NEW-L64`.

## 1. Main checkpoint receipt

Main report:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T06-18-10Z__report.md`

Create-file commit:

`71c0a325cbe50f586a6b8d6af8fbe76a3b8a01ee`

Exact-commit readback blob:

`6ca72461ee1ee8452c97ff30d851e39f2e631fb0`

The report was fetched back using that exact commit ref and contains `NEW-L61`--`NEW-L64`. Delivery status: **VERIFIED**.

## 2. Finite-state checker receipt

Checker:

`proofnet24/HARD10-03/artifacts/2026-09-16T06-31-00Z__projection_fejer_check.py`

Commit:

`be804449960c28b228c980c5bec3a74c87651c53`

Exact-commit readback blob:

`9350f694e586a33c585499ed649b1a103f219bf7`

Delivery status: **VERIFIED**.

The checker enumerates all 24 permutation states of interchange on `C4`, computes the exact finite-state law at time `t=0.7` by matrix exponentiation, and checks:

1. `NEW-L61` divisor/Möbius inversion for all possible root-cycle lengths on `C4`;
2. the direct kernel `G(x)` against the point-shift autocorrelation representation in `NEW-L62`;
3. the Fourier transform of `G` against the nonnegative cycle form factor in `NEW-L62`;
4. the pathwise Fejér inequality `NEW-L63` for every permutation, all four Fourier modes and every `1<=H<=6`.

This is a finite-state sanity check only, not the analytic proof.

## 3. Executed checker output

Executed output:

`proofnet24/HARD10-03/artifacts/2026-09-16T06-31-00Z__projection_fejer_check_output.json`

Commit:

`0eb5efd483b7a4b29447e367e4a11b2025b3f576`

Exact-commit readback blob:

`7c3d9485470cc7e8d0de949f1f9880b04e66192e`

Delivery status: **VERIFIED**.

The executed output records `pass: true`. Numerical residuals were:

* Möbius inversion maximum error: `1.6653345369377348e-16`;
* projection/autocorrelation maximum error: `2.7755575615628914e-17`;
* Fourier form-factor maximum error: `1.1102230246251565e-16`;
* largest positive Fejér violation over 576 checked cases: `1.1102230246251565e-16`;
* minimum computed form-factor value: `0.4447520109783707`.

The root-cycle probabilities at `t=0.7` were

`P(L=1,2,3,4) = (0.38850099762710755, 0.29269783112397757, 0.18552633073859967, 0.13327484051031485)`,

while the first four cyclic power-return probabilities were

`a_1,...,a_4 = (0.38850099762710755, 0.6811988287510852, 0.5740273283657072, 0.8144736692614002)`,

illustrating directly why raw power returns contain divisor contamination and require Möbius cancellation to isolate primitive cycle lengths.

## 4. Immediate confinement corollary of NEW-L64

`NEW-L64` states

\[
S_\beta(M)
:=
\mathbb E\left[
\mathbf1_{\{L<\infty\}}
\frac{|C_0\cap B_\infty(M)|}{L}
\right]
\le
8p_\infty(\beta)
+C\beta^{-1/4}\sqrt{1+M^2/\beta}.
\]

On the event that the complete finite root cycle is contained in `B_infty(M)`, the fraction in the expectation equals one. Therefore

\[
\boxed{
\mathbb P\bigl(
L<\infty,\ C_0\subseteq B_\infty(M)
\bigr)
\le
8p_\infty(\beta)
+C\beta^{-1/4}\sqrt{1+M^2/\beta}.}
\tag{A.1}
\]

In particular, along any hypothetical counterexample sequence with

\[
p_\infty(\beta)=0,
\]

and for every fixed `epsilon>0`, taking

\[
M=\beta^{3/4-\epsilon}
\]

gives

\[
\boxed{
\mathbb P\left(
C_0\subseteq
B_\infty(\beta^{3/4-\epsilon})
\right)
\le C_\epsilon\beta^{-\epsilon}.}
\tag{A.2}
\]

So an all-finite large-time phase would force the root cycle itself, with probability tending to one, to have spatial radius at least `beta^(3/4-epsilon)` for every fixed `epsilon>0`; `NEW-L64` is stronger still because it says that not merely one exceptional vertex but an asymptotically vanishing **fraction** of the cycle may remain inside that radius.

This is a conditional geometric consequence, not a proof of infinite cycles.

## 5. Final status

No GitHub approval/security denial occurred. No prior or peer file was overwritten. No workflow, setting, permission, email, Drive file, public resource, third-party channel, or paid compute was used.

The strongest genuinely new result of this checkpoint is the Fourier/Fejér estimate `NEW-L64`: if a sequence of large times had no infinite cycles, then the finite root cycles would have to be superdiffuse in the sense that the fraction of their vertices within every `o(beta^(3/4))` neighborhood of a typical root tends to zero.

No independent human or formal verification is claimed.