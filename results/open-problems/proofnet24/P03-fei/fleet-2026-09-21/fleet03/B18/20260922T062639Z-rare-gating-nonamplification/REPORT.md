# fleet03/B18 — rare gating cannot amplify a balanced FEI excess above max{4, core}

**Run:** `fleet03-B18-20260922T062639Z-r11`  
**Common candidate:** `LIMIT-PRIME-GATE-LIFT-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / RARE-GATING_AMPLIFICATION_CLOSED`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact target and peer artifact consumed

The live all-gate candidate remains

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),
\]

with the still-unproved universal implication

\[
D_{\Gamma^\dagger}(P;p)\ge0
\tag{0.1}
\]

for every finite composition-prime Boolean gate `P`, every arity, and every interior product-bias vector. At a balanced uniform gate this is

\[
C^\dagger[I(P)-1]-H(P)\ge0.
\tag{0.2}
\]

The named completed other-account result consumed substantively is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T061440Z-mesoscopic-defect-codimension/REPORT.md`.

Its Theorem 1.1 gives an exact rare-gating transform. For a balanced Boolean core `f`, add `m>=1` fresh gate bits, let `delta=2^{-m}`, flip exactly the `f=-1` fibre when all gate bits are zero, and multiply by one fresh unbiased character. The resulting actual balanced Boolean function `G_m` satisfies

\[
\boxed{I(G_m)-1=\delta[I(f)+m]}
\tag{0.3}
\]

and

\[
\boxed{H(G_m)=\delta H(f)+4m\delta-2m\delta^2+e_0(\delta)},
\qquad
e_0(\delta)=(1-\delta)^2\log_2\frac1{(1-\delta)^2}.
\tag{0.4}
\]

That peer used these identities to refute the stronger statement that physical defect density tending to zero forces slope `4`: a growing self-composed core retains its core excess ratio asymptotically. The exact question left open for this mechanism was whether rare gating can **amplify** a core that is already safe at the live center into a violation.

## 1. New theorem: exact rare-gating nonamplification

For a balanced Boolean function `u`, define its `C`-excess slack

\[
S_C(u):=C[I(u)-1]-H(u).
\tag{1.1}
\]

### Theorem 1.1

Let `f` be any balanced Boolean function and let `G_m` be the source-exact rare-gating transform above. For every real `C>=4` and every integer `m>=1`,

\[
\boxed{
S_C(G_m)
\ge
\delta\left[S_C(f)+C-\frac2{\ln2}+(C-4)m\right]
+2m\delta^2.
}
\tag{1.2}
\]

In particular,

\[
\boxed{S_C(f)\ge0\quad\Longrightarrow\quad S_C(G_m)>0}
\tag{1.3}
\]

for every `m>=1` and every `C>=4`.

Thus rare gating behind any number of fresh zero bits can never turn a `C`-safe balanced core into a `C`-unsafe function once `C>=4`.

### Proof

Substitute the exact peer identities (0.3)--(0.4):

\[
\begin{aligned}
S_C(G_m)
&=C\delta[I(f)+m]
 -\delta H(f)-4m\delta+2m\delta^2-e_0(\delta)\\
&=\delta\left[S_C(f)+C+(C-4)m\right]
 +2m\delta^2-e_0(\delta).
\end{aligned}
\tag{1.4}
\]

It remains to control the single empty-atom entropy term without discarding its sign. Since `0<delta<=1/2`,

\[
-\ln(1-\delta)\le\frac{\delta}{1-\delta},
\]

and therefore

\[
\begin{aligned}
\frac{e_0(\delta)}{\delta}
&=\frac{2(1-\delta)^2[-\ln(1-\delta)]}{\delta\ln2}\\
&\le\frac{2(1-\delta)}{\ln2}
<\frac2{\ln2}.
\end{aligned}
\tag{1.5}
\]

Combining (1.4) and (1.5) gives (1.2). If `S_C(f)>=0` and `C>=4`, every term on the right of (1.2) is nonnegative and the constant term is strictly positive because

\[
4-\frac2{\ln2}>1.1146.
\]

This proves (1.3). `QED`

No non-Boolean relaxation, unsigned spectrum, missing coordinate label, or asymptotic approximation occurs in this proof; the exact source formula is used before the one elementary logarithm estimate.

## 2. Ratio form

If `f` is balanced and noncharacter, set

\[
R(f)=\frac{H(f)}{I(f)-1}.
\]

Taking `C=max{4,R(f)}` in Theorem 1.1 gives the clean structural consequence

\[
\boxed{
R(G_m)<\max\{4,R(f)\}
\qquad(m\ge1).
}
\tag{2.1}
\]

If `f` is a balanced character, then `H(f)=0`, `I(f)=1`; the same proof with `C=4` gives

\[
H(G_m)<4[I(G_m)-1].
\tag{2.2}
\]

So the transform has a strict nonamplification principle at the exact excess normalization relevant to the balanced all-gate target.

## 3. Application to the peer's growing-support obstruction

The peer takes the certified balanced 18-input seed `B` with

\[
I_0=\frac{261}{128},
\qquad
\rho_0:=\frac{H_0}{I_0-1}
=6.5218457109230465756581\ldots,
\tag{3.1}
\]

self-composes it to `f_k=B^{\circ k}`, and rare-gates with `m=k`. Balanced self-composition preserves the exact excess ratio, so

\[
S_{\rho_0}(f_k)=0.
\]

Theorem 1.1 therefore upgrades the peer's asymptotic statement to the finite, strict statement

\[
\boxed{
\frac{H(G_k)}{I(G_k)-1}<\rho_0
< C^\dagger
\qquad\text{for every }k\ge1.
}
\tag{3.2}
\]

Indeed the quantitative slack is

\[
S_{\rho_0}(G_k)
\ge
2^{-k}\left[
\rho_0-\frac2{\ln2}+(ho_0-4)k
\right]
+2k\,4^{-k}>0.
\tag{3.3}
\]

Thus the family that correctly refutes “vanishing density implies slope 4” is nevertheless **never** a counterexample to the live center at any finite stage. It merely transports the pre-existing core ratio toward the boundary from below.

The same conclusion holds for **any** balanced rare-gated core already safe at `C^dagger`; from (1.2),

\[
S_{C^\dagger}(G_m)
\ge
\delta\left[
S_{C^\dagger}(f)
+3.6364611322
+2.521851214\,m
\right]
+2m\delta^2.
\tag{3.4}
\]

The constants displayed in (3.4) are only decimal renderings of
`C^dagger-2/ln 2` and `C^dagger-4`; the proof uses their exact expressions.

## 4. What this changes in the common proof search

The previous fleet03/B18 theorem proved slope `4` for a **fixed finite** balanced defect pattern under dummy dilution. Fleet02/B17 then correctly showed that growing support can retain a high core ratio. Theorem 1.1 now separates retention from amplification:

* fixed-pattern dummy dust has asymptotic incremental slope `4`;
* growing rare-gated support can retain the core excess ratio above `4`;
* but rare gating itself **cannot increase** the relevant excess constant above `max{4, core ratio}`.

Hence an adversary to `LIMIT-PRIME-GATE-LIFT-v1` cannot be created by taking a `C^dagger`-safe balanced core and placing its negative fibre behind an increasingly rare all-zero gate. If that construction is unsafe, the core was already unsafe before rare gating.

This is stronger than the peer's exponential-codimension safety theorem on this particular structured mechanism, because it has no ambient-dimension threshold and holds for every `m>=1`. It does not replace the peer's geometry-free theorem for arbitrary character-defect sets.

## 5. Exact old/new missing implications

**Old missing implication.** The full universal prime-gate inequality (0.1) remains unpaid. Within the growing-support adversary left by the previous B18 run, it was not known whether the exact rare-gating mechanism of fleet02/B17 could amplify a safe core into a violation at finite depth.

**New proved inference.** For every balanced Boolean core and every `C>=4`, the exact rare-gating transform obeys (1.2). In particular `C`-safety is preserved strictly for every finite gate depth, and the peer's high-ratio growing-support family lies strictly below its core ratio at every finite stage.

**Exact failed stronger claim retained.** “Defect density tending to zero forces slope 4” remains **REFUTED** by fleet02/B17. Theorem 1.1 does not revive it; it proves only nonamplification.

**Replacement obligations.** A surviving growing-support adversary must use a mechanism genuinely different from one rare all-zero cylinder over a safe core: for example an intrinsically unsafe core, overlapping/reused gates, a non-cylindrical character defect outside the peer's geometry-free safe regime, or an off-centre composition-prime gate. The all-arity/all-bias prime-gate implication is still the decisive universal step.

**Consumed peer artifact.** `fleet02/B17/20260922T061440Z-mesoscopic-defect-codimension/REPORT.md`, specifically its exact Theorem 1.1.

**Next recipients.** `fleet02/B17` should remove rare-gating amplification from its adversary list and concentrate on non-cylindrical/off-centre prime mechanisms; `fleet01/B16` can use the result when converting central prime gaps into neighborhoods, since rare cylinders cannot manufacture a worse center from a safe child; all-gate builders should treat rare gating as a strict slack-preserving operation for every center `C>=4`.

**Implication to full FEI.** Direct but partial: one infinite growing-support adversarial mechanism is now closed exactly. No universal bound on every composition-prime gate and bias is proved. Full FEI remains **OPEN / NOT PROVED**.

Scoped privacy review: this report contains only FEI mathematics, logical account/slot labels, source-bound repository identifiers, and nonsecret numerical constants. It contains no credentials, scheduler identifiers, machine paths, unrelated private transcripts, email/Drive action, paid/remote model use, workflow dispatch, or permission changes.
