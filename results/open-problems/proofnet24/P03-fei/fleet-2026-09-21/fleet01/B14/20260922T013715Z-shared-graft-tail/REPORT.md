# B14 — rigorous exhaustion of the fixed-depth-four shared-graft obstruction family

**Run:** `20260922T013715Z-fleet01-B14-fei-r11`  
**Outcome:** **ESSENTIAL_STEP_APPLIED (candidate-family closure).** Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were consumed directly; no authenticated cognitive-brain retrieval/context is claimed.

## 0. Why this is the live target

A final fresh owner-control read in this invocation contains a later FEI convergence message than the older reset assignment: every FEI worker is to work the all-gate reformulation, either proving the claimed AND/decomposable extremality or falsifying it. The older restriction-selector calculation from this invocation is preserved in its own immutable report, but the substantive terminal result below follows this later owner direction.

The source-exact gate reformulation is

`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`, blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`.

For one symmetric nonnegative potential `Gamma`, full FEI is equivalent to requiring, for every Boolean gate `G` and product bias vector,

\[
\Gamma(p_{out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u).
\tag{G}
\]

At uniform bias for a balanced gate this reduces exactly to

\[
H(G)\le \Gamma(1/2)[I(G)-1].
\tag{0.1}
\]

Thus

\[
R(G):=\frac{H(G)}{I(G)-1}
\tag{0.2}
\]

is a source-valid lower bound on the necessary center cap. Relative to the old read-once reference center `C_0=6.4548`, the owner's comparable gate margin is

\[
c_G=4(R(G)-C_0)
\tag{0.3}
\]

at such a balanced point.

The exact named other-account result consumed and applied is fleet03/B15,

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260922T012556Z-iterated-shared-graft/REPORT.md`, scientific commit `40b07cf4782e07b247e8370832a2c3abe5c33c1b`, report blob `aff93b999538a8b8baeab270ff739f405c79ee7c`.

It starts from fleet01/B18's actual balanced monotone shared-coordinate gate `F_2` and proves four further positive source-valid rounds, ending with

\[
R(F_6)
\in
[6.521850949550448184840160538860511501288648868305895\ldots,
 6.521850949550448184840160538860511501288648871643878\ldots].
\tag{0.4}
\]

Its explicit next obligation is to analyze the *entire iterated family* before freezing another center cap. This report closes that obligation for the fixed depth-four map.

## 1. Exact recurrence

For each current balanced monotone gadget, let `I_m` be its influence, `R_m=H_m/(I_m-1)`, and `c_m` the designated singleton Fourier coefficient. Fleet01/B18/fleet03/B15 prove the exact update

\[
\alpha=\frac9{256},\qquad
B=\frac{257}{256},\qquad
d_0=\frac{133}{128},
\]

\[
I_{m+1}=\frac{261}{128}+\alpha(I_m^4-1),
\tag{1.1}
\]

\[
c_{m+1}=\frac{57}{256}+\frac{c_m^4}{256},
\tag{1.2}
\]

\[
R_{m+1}-R_m
=
\frac{K(c_m^4)-d_0R_m}{\alpha I_m^4+B},
\tag{1.3}
\]
where

\[
K(b)=H_{core}(b)+\alpha[-\phi(b^2)+16(1-b^2)],
\qquad \phi(t)=-t\log_2t.
\tag{1.4}
\]

A useful exact identity, not exploited in the finite report, is

\[
\boxed{
\alpha I_m^4+B=I_{m+1}-1.
}
\tag{1.5}
\]

Hence the denominator in the ratio update is literally the next gate's excess influence.

## 2. Uniform bound on the numerator source term

The `H_core(b)` term is the Shannon entropy contribution of at most `512=2^9` squared Fourier masses belonging to the no-fresh-coordinate sector of the actual Boolean graft. Their total mass `M` is at most one. For any subprobability vector `(m_s)_{s<=512}` of total mass `M<=1`,

\[
\sum_s -m_s\log_2m_s
\le M\log_2(512/M)\le9.
\tag{2.1}
\]

The first inequality is entropy maximization at equal masses for fixed `M`; the second follows because `M log_2(512/M)` is increasing on `[0,1]` (its derivative is at least `9-1/ln2>0`). Therefore

\[
H_{core}(b)\le9.
\tag{2.2}
\]

Also `-phi(b^2)<=0` and `16(1-b^2)<=16`. Thus, uniformly for every actual iterate,

\[
\boxed{
K(c_m^4)\le9+\frac9{16}=\frac{153}{16}.
}
\tag{2.3}
\]

Since every `R_m>=0`, (1.3) immediately gives the one-sided increment bound

\[
\boxed{
R_{m+1}-R_m
\le
\frac{153/16}{I_{m+1}-1}.
}
\tag{2.4}
\]

This remains valid even if future iterates cease to increase: negative increments only make the desired upper envelope smaller.

## 3. The influence denominator explodes fast enough to make the whole tail summable

The exact `F_2` influence from fleet01/B18 is

\[
I_2=\frac{784028312243315011737}{295147905179352825856}>\frac{53}{20}=2.65.
\tag{3.1}
\]

Applying the monotone recurrence (1.1) gives the following completely rational lower chain:

\[
I_3>3.73,\qquad
I_4>8.8,\qquad
I_5>210,\qquad
I_6>68,000,000.
\tag{3.2}
\]

For example the successive margins obtained by inserting the displayed lower bound into (1.1) are positive:

\[
F(2.65)-3.73=\frac{313529}{40960000}>0,
\]
\[
F(3.73)-8.8=\frac{231907769}{25600000000}>0,
\]
\[
F(8.8)-210=\frac{453489}{160000}>0,
\]
\[
F(210)-68,000,000=\frac{95290513}{256}>0.
\]

Put

\[
D_m:=I_m-1.
\]

Then (1.5) and (3.2) imply

\[
\boxed{
D_7>\frac9{256}(68,000,000)^4
=751689000000000000000000000000.
}
\tag{3.3}
\]

Moreover, once `D_m>=16/3`,

\[
D_{m+1}=\frac9{256}(D_m+1)^4+\frac{257}{256}
\ge D_m^2,
\tag{3.4}
\]

because `(9/256)D_m^4>=D_m^2`. Hence after `D_7` the denominators at least square at every round.

## 4. PROVED: the entire infinite fixed-depth-four family is already exhausted after F6

Sum (2.4) from `m=6` onward. By (3.4),

\[
D_{7+k}\ge D_7^{2^k}.
\]

Therefore

\[
\begin{aligned}
\sup_{N\ge6}(R_N-R_6)
&\le \frac{153}{16}\sum_{k\ge0}\frac1{D_{7+k}}\\
&\le \frac{153}{16}\left(\frac1{D_7}+\frac1{D_7^2}+\frac1{D_7^4}+\cdots\right)\\
&<\frac{153}{8D_7}\\
&<\boxed{
\frac1{39304000000000000000000000000}
}
<2.545\times10^{-29}.
\end{aligned}
\tag{4.1}
\]

Combining this analytic tail bound with the *certified upper endpoint* for `R(F_6)` from fleet03/B15's outward-rounded checker gives the rigorous whole-family envelope

\[
\boxed{
\sup_{m\ge2}R(F_m)
<6.521850949550448184840160538886.
}
\tag{4.2}
\]

(The earlier iterates are all below `F_6` by the certified strict gains through round six.)

Thus no amount of further iteration of this **same fixed depth-four shared-core transform** can raise the balanced FEI lower bound by even `2.545e-29` beyond the certified `F_6` value.

In the owner's gate-margin units,

\[
\boxed{
\sup_m c_{F_m}
<0.268203798201792739360642155544.
}
\tag{4.3}
\]

This family therefore already falsifies the old AND/read-once extremality by a very large margin, but its own infinite tail is now rigorously bounded.

## 5. The singleton coefficient has no hidden instability

The coefficient map

\[
T(c)=\frac{57}{256}+\frac{c^4}{256}
\]

maps `[0,1]` into `[57/256,58/256]` and

\[
|T'(c)|=\frac{c^3}{64}\le\frac1{64}.
\]

So it is a contraction with a unique fixed point `c_*` solving

\[
256c_*=57+c_*^4.
\tag{5.1}
\]

Thus the exhaustion in (4.1) is not hiding an oscillatory or unstable singleton parameter. The only reason the finite gains become microscopic is the exact quartic explosion of the excess-influence denominator.

## 6. Exact old/new missing implications

**Old missing implication.** After fleet03/B15 certified four further positive shared-graft rounds, it was unknown whether repeatedly applying the same source-valid depth-four transform could continue to force materially larger center caps, so another finite cap could not responsibly be frozen.

**New proved inference.** The entire infinite fixed-depth-four shared-graft family is bounded by (4.2); all future possible upward movement after `F_6` totals less than `2.545e-29`. This is an analytic all-round theorem, not a finite extrapolation.

**What this does NOT prove.** It does not upper-bound arbitrary Boolean gates, arbitrary product biases, other shared-coordinate grafts, or transforms using a different self-composition depth. Hence it does not prove FEI and does not restore AND extremality, which is already refuted by the explicit `F_m` gates.

**Replacement obligation.** A successor universal potential may safely choose its *balanced center* above the envelope (4.2) with respect to this one obstruction family, but must still survive every other gate and every bias. The next falsification attack should therefore change mechanism: vary the shared-graft host or self-composition depth, or search a genuinely different shared-coordinate prime gate. Re-running more depth-four rounds is mathematically exhausted.

**Classification:** `ESSENTIAL_STEP_APPLIED (candidate-family closure)`. **Full FEI remains OPEN.**

## 7. Scoped review

Only source-bound mathematics, artifact identifiers and sanitized provenance are included. No credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive actions, public-posting instructions, permission changes, workflows or paid/remote-compute instructions are present.
