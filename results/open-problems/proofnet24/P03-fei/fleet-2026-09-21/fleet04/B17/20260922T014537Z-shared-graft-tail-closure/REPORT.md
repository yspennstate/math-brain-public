# B17 — close the fixed depth-four shared-graft tail, and push the exact Boolean lower bound one step

**Run:** `20260922T014537Z-b17-fei-r16`  
**Outcome:** `ESSENTIAL_STEP_APPLIED` to the newest shared-graft replacement obligation; one additional rigorously positive Boolean round plus a uniform tail bound for the entire fixed-depth-four iteration.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. Repository sources were read through the authorized connector, but no authenticated mathematical-brain retrieval/context was consumed.

## 1. Live target and predecessor actually consumed

The current owner control supersedes the stale packet/remainder-only wording and asks all FEI workers to converge on the equivalent all-gate potential inequality

\[
\Gamma(p_{out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{1.1}
\]

for one symmetric nonnegative `Gamma` and every Boolean gate and product bias vector. At uniform bias for a balanced gate this reduces exactly to

\[
H(G)\le \Gamma(1/2)(I(G)-1).
\tag{1.2}
\]

Thus

\[
R(G):=\frac{H(G)}{I(G)-1}
\tag{1.3}
\]

is a direct lower-bound adversary for the center cap. Relative to the owner's historical read-once reference `C0=6.4548`, the comparable balanced gate margin is

\[
c_G=4(R(G)-C_0).
\tag{1.4}
\]

The newest compatible other-account B15 result actually consumed is

`fleet03/B15/20260922T012556Z-iterated-shared-graft/REPORT.md`, blob `aff93b999538a8b8baeab270ff739f405c79ee7c`.

It iterates fleet01/B18's exact balanced shared-coordinate construction and certifies the actual finite Boolean gate `F6` with

\[
R(F_6)>6.5218509495504481848401605388605.
\tag{1.5}
\]

Its stated replacement obligation is to analyze or upper-control the iterated shared-core family before freezing another all-gate center cap. This run attacks that obligation directly rather than repeating the earlier witness.

No KL/relative-entropy credit from the older arithmetic remainder route is discarded or set to zero here: the later owner target bypasses that representation and this construction is evaluated as an exact Boolean gate in the all-gate normalization itself.

## 2. General depth-`d` shared-core recurrence

Fleet01/B18 proves the source-exact nine-host transform for any balanced monotone Boolean gadget `f` with influence `I`, ratio `R=H/(I-1)`, and a selected singleton Fourier coefficient `c`. Put

\[
\alpha=\frac9{256},\qquad
B=\frac{257}{256},\qquad
d_0=\frac{133}{128},
\]

and

\[
K(b)=H_{core}(b)+\alpha\left[-\phi(b^2)+16(1-b^2)\right],
\qquad \phi(t)=-t\log_2 t.
\tag{2.1}
\]

Before applying that transform, take a depth-`d` balanced disjoint self-composition. The standard exact identities are

\[
I(f^{\circ d})=I^d,\qquad
H(f^{\circ d})=R(I^d-1),
\qquad c(f^{\circ d})=c^d
\tag{2.2}
\]

for the selected singleton path. Substituting these into the source transform gives, for every integer `d>=1`,

\[
\boxed{
R'_d-R=
\frac{K(c^d)-d_0R}{\alpha I^d+B}
}
\tag{2.3}
\]

and

\[
\boxed{
I'_d=\frac{261}{128}+\alpha(I^d-1),
\qquad
c'_d=\frac{57}{256}+\frac{c^d}{256}.
}
\tag{2.4}
\]

This is not a spectral relaxation: disjoint self-composition and the nine-host graft both preserve an actual finite balanced monotone Boolean gate. Equation (2.3) also shows that the *sign* of a candidate gain depends only on `R,c,d`; the large influence only suppresses its magnitude through the denominator.

For the predecessor's fixed choice `d=4`, equations (2.3)-(2.4) are exactly the B15 recurrence.

## 3. One more certified Boolean round: `F7`

The checker reconstructs the shared-core Fourier data through the exact multiplicities of its 19 `(A_S,Q_S)` Walsh-numerator classes, uses exact `Fraction` arithmetic for all coefficients and influences, and encloses all logarithms with 100-digit outward-rounded Decimal intervals and a finite atanh series with explicit remainder. It starts from the same certified `F2` value widened by `1e-45` on each side that fleet03/B15 used, then independently reruns `F3` through `F7`.

It certifies

\[
\begin{aligned}
R(F_7)&>6.5218509495504481848401605388605115013503296799038586768578,\\
R(F_7)&<6.5218509495504481848401605388605115013503296832418414558148,
\end{aligned}
\tag{3.1}
\]

with strictly positive last gain

\[
R(F_7)-R(F_6)
>6.1680811597963207635280857963576421\times10^{-38}.
\tag{3.2}
\]

The same exact recurrence gives

\[
I(F_7)>3.668970596844139410010095536630\times10^{30}.
\tag{3.3}
\]

Therefore balanced disjoint self-composition of `F7` yields finite Boolean functions whose ordinary `H/I` ratios approach `R(F7)`, and hence

\[
\boxed{
C_{FEI}>6.521850949550448184840160538860511501350329679.
}
\tag{3.4}
\]

In the owner's comparable old-reference margin units this is

\[
\boxed{
c_{F_7}>0.2682037982017927393606421554420460054013187196.}
\tag{3.5}
\]

This is a lower bound / candidate obstruction, not a universal FEI upper bound.

## 4. New tail theorem: repeating the same depth-four mechanism is now closed

The predecessor left open whether continuing the exact depth-four map could keep forcing a materially larger center cap. It cannot.

For the shared core, the exact multiplicity table in the checker gives the Parseval polynomial

\[
\sum_S\left(\widehat a(S)+b\widehat Q(S)\right)^2
=1-\alpha+\alpha b^2\le1,
\qquad 0\le b\le1.
\tag{4.1}
\]

There are 512 Fourier masses. If their total mass is `m<=1`, concavity gives

\[
H_{core}(b)\le m\log_2(512/m)\le9.
\tag{4.2}
\]

Also `-phi(b^2)<=0` and `1-b^2<=1`, so uniformly

\[
\boxed{K(b)\le9+16\alpha=\frac{153}{16}.}
\tag{4.3}
\]

Let

\[
D_{r+1}:=I(F_{r+1})-1=\alpha I(F_r)^4+B.
\tag{4.4}
\]

Regardless of the sign of the exact numerator in (2.3), every *positive* future increment satisfies

\[
(R_{r+1}-R_r)_+\le\frac{153/16}{D_{r+1}}.
\tag{4.5}
\]

From (3.3),

\[
D_8>\alpha 10^{120}.
\]

Since `(153/16)/alpha=272`, the first possible positive increment after `F7` is therefore less than

\[
2.72\times10^{-118}.
\tag{4.6}
\]

Moreover

\[
D_{r+1}=\alpha(D_r+1)^4+B\ge\alpha D_r^4,
\tag{4.7}
\]

so the successive upper bounds in (4.5) decrease by a factor at most

\[
\frac1{\alpha D_r^3}<\frac12
\]

from `D8` onward (in fact vastly smaller). Summing the geometric majorant gives the uniform infinite-tail estimate

\[
\boxed{
\sum_{r\ge7}(R(F_{r+1})-R(F_r))_+<5.44\times10^{-118}.
}
\tag{4.8}
\]

Consequently every later gate in **this fixed depth-four shared-graft iteration** satisfies

\[
R(F_r)
< R(F_7)_{upper}+5.44\times10^{-118}
\qquad(r\ge7).
\tag{4.9}
\]

The interval width in (3.1), about `3.34e-45`, is already enormously larger than the entire possible post-`F7` positive tail. Thus continuing the same depth-four recurrence is mathematically exhausted: it cannot produce a meaningfully larger FEI lower bound.

This is the requested replacement after the finite-cap witness failed: instead of freezing at `F6` or rerunning the same witness, the entire fixed-depth-four family is now controlled.

## 5. What this refutes, and what remains

**Refuted / closed at stated scope:**

1. Any all-gate potential with `Gamma(1/2)` at or below (3.4) is impossible, because `F7` is an actual balanced Boolean gate.
2. Repeating the *same depth-four shared-core graft* cannot materially raise the obstruction after `F7`; the entire remaining positive tail is below `5.44e-118`.
3. Therefore another run that simply computes `F8,F9,...` under the same map would be mathematically redundant.

**Not refuted:** the all-gate reformulation itself, finite FEI, a different self-composition depth, a different shared host/core, or a biased product point. The general identity (2.3) provides the exact comparison formula for testing a different integer depth without losing Boolean realizability or normalization.

The next adversarial search should therefore change mechanism while staying on the same owner target: optimize the exact numerator `K(c^d)-d_0R` over a genuinely different integer depth / host construction, or search a biased prime gate. It should not spend another substantive run on the now-closed fixed-`d=4` tail.

## 6. Reproduction and status

Scientific base observed before the writes: `42478ebb3356e8327133e8e0a60370ac02109f7b` on `master`.

Artifacts in this run folder:

- `CHECKER.py`: Git blob `58864b56c52f0f2ef76d59be4e8878fba1fdd187`; executed-byte SHA-256 `a4793a74d1d98b982c412ae6e063f225fea9d15ac362cc177cef3d6938a3e262`.
- `CHECK_OUTPUT.txt`: Git blob `242aaefdf503a13a308c504bc718dfc882a6bcd2`; byte SHA-256 `084c344470f5ad4b4f3dfc51b773cf27e3d3cceb351f7674ae63fb8fec1bbd0d`.

The checker exits successfully and records `PASS`, the `F7` interval, the old-reference margin, and the fixed-depth-four tail bound. The calculation is self-checked and source-bound; it has not yet received an independent end-to-end peer review.

Scoped privacy/provenance review: the new files contain only mathematical formulas, exact rational/core data already present in the consumed scientific construction, source hashes, and sanitized logical paths. No credentials, scheduler identifiers, machine paths, unrelated private material, email/Drive actions, paid compute, workflow dispatch, benchmark gold, or public-release instruction is included.

**Final status:** `ESSENTIAL_STEP_APPLIED` for the shared-graft replacement obligation; **full FEI remains OPEN / NOT PROVED**.
