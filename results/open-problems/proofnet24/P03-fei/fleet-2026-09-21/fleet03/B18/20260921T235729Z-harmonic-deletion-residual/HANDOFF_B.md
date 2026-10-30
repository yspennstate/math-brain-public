# Campaign B lead handoff — common target B-HARMONIC-DELETE-v2

**Source:** fleet03/B18 `20260921T235729Z-harmonic-deletion-residual/REPORT.md`.  
**Status:** `ESSENTIAL_STEP_APPLIED`; full FEI **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## Common candidate

For a Boolean Fourier spectral sample `S` with `p_A=P(S=A)`, define the uniform-prefix shadows

\[
v_A=\sum_{S\supseteq A}\frac{p_S}{\binom{|S|}{|A|}},
\qquad t_A=v_A-p_A.
\]

The new exact reduction is

\[
H(f)=H(J)+T_{\rm stop}+D_{\rm del},
\]

where fleet02/B12 already proves

\[
H(J)\le4.8588229680899335\,I,
\]

this run proves

\[
T_{\rm stop}:=\sum_{A\ne\varnothing}v_A h_2(p_A/v_A)\le I,
\]

and the sole unpaid signed residual is

\[
\boxed{
D_{\rm del}:=
\sum_{\substack{A\ne\varnothing\\i\notin A}}
\frac{v_{A+i}}{|A|+1}
\log_2\frac{v_A-p_A}{v_{A+i}}.
}
\]

At level `a`, if `Q_{a+1}=P(|S|>=a+1)`, `V_{a+1}(B)=v_B/Q_{a+1}` and `T_a(A)=t_A/Q_{a+1}`, then exactly

\[
D_a=Q_{a+1}[H(V_{a+1})-H(T_a)].
\]

Negative edge/level contributions are legal information credits and must not be discarded.

## Full-proof implication

The exact common Campaign-B target is now:

> **B-HARMONIC-DELETE-v2:** prove `D_del(f)<=C_del I(f)` for every Boolean `f` and one finite dimension-independent `C_del`.

This closes FEI with

\[
H(f)\le(5.8588229680899335+C_{\rm del})I(f).
\]

Conversely FEI itself implies a finite bound on `D_del`, so this residual is quantitatively FEI-equivalent up to the already-paid constant.

## Peer inputs consumed

- fleet02/B12 `20260921T232119Z-harmonic-root-marked-spectrum/REPORT.md`, blob `1a0ff3b828a377afde3461e6f130d46255ed1de5`: supplies the root theorem, exact harmonic recursion, mixed-prefix Boolean constraints and the controlled-majority refutation of rowwise harmonic FEI.
- fleet02/B17 `20260921T231240Z-recursive-majority-hierarchical-code/REPORT.md`, blob `be4735ca18bda8d3598708324565ac16f912a280`: supplies the genuine recursive-majority refutation of every finite one-level global CFC constant. The new residual escapes that exact obstruction because `D_del=H-H(J)-T_stop<=H<4I` on that family.

## Builder/adversary alignment

- **fleet02/B17:** attack exactly `B-HARMONIC-DELETE-v2` on recursive/odd majority, addressing, tensors, biased defects and sparse defects. Do not attack the retired one-level CFC instead.
- **fleet02/B12 and fleet04/B12:** apply the true mixed-prefix / thinned-source constraints directly to the signed level increment `Q[H(V)-H(T)]`.
- **fleet01/B12 and fleet03/B15:** preserve factorial and conditional-KL rebates in this exact residual; do not introduce a second normalized target.

`old_missing_implication`: whole harmonic continuation `(8.1)=O(I)`.  
`new_proved_inference`: continuation `=T_stop+D_del` exactly and `T_stop<=I`.  
`remaining_implication`: `D_del<=C_del I`.  
`next_recipients`: fleet02/B17, fleet02/B12, fleet04/B12, fleet01/B12, fleet03/B15.
