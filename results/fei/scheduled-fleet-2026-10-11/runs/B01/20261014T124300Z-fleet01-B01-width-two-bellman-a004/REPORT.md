# B01 / A004 — width-two Bellman reduction after the full-block obstruction

**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim:** `B01-A004-WIDTH-TWO-BELLMAN-REDUCTION-v1`  
**Status:** **STRICTLY LOCAL SUFFICIENT INEQUALITY PROVED; UNIVERSAL SIGN OPEN**  
**Universal GU / full FEI:** **OPEN**

## Exact candidate

Use the reviewed producer constant

\[
c_* = \frac{29}{2}+\frac4{\ln2}
\]

and define `L=M+2U-c_*I`.  For an inherited physical block `Y` of size at
most two, define the width-two Bellman residual

\[
\begin{aligned}
\mathcal E_2(f,Y)=\min_x\{&\Delta_xL(f)+2\Theta_Y(f)\\
&-\max_{|Z_+|\le2}\Theta_{Z_+}(f_{x=+1})
-\max_{|Z_-|\le2}\Theta_{Z_-}(f_{x=-1})\}.
\end{aligned}
\]

The sole unpaid inequality is

\[
\boxed{\mathcal E_2(f,Y)\le0}
\tag{W2B}
\]

for every nonconstant genuine Boolean `f` and every inherited `|Y|<=2`.
The child blocks and queried coordinate are chosen adaptively.

## Exact implication

If (W2B) holds, recursively choose its minimizing query and maximizing child
blocks.  Dimension decreases at every step, so the resulting physical
restriction tree terminates in constants.  The signed opening/reveal terms
telescope exactly and give

\[
L(f)+2\Phi(f)\le0.
\]

Since `Phi>=0` and the reviewed pair-entropy bound gives `B<=2I`,

\[
\boxed{G(f)\le(c_*+2)I(f)
=\left(\frac{33}{2}+\frac4{\ln2}\right)I(f).}
\]

Thus (W2B) would prove universal GU with

\[
(a,b)=\left(\frac{33}{2}+\frac4{\ln2},0\right)
\]

and FEI with

\[
H(f)\le\left(35+\frac8{\ln2}\right)I(f).
\]

This is a conditional reduction, not a proof of (W2B).

## Why this is the surviving target

The source-bound B05 point-defect calculation proves that repeatedly keeping
the whole surviving block requires coefficient
`4r-3+4/ln(2)+o(1)` at rank `r`; the memoryless full-block aggregate is
therefore false.  The same source proves that a sliding width-two block pays
the complete point-defect hierarchy with a uniform coefficient below `c*`.
Accordingly, branch-adapted width two survives the mandatory rare-event test
while the stronger-looking full-block policy does not.

## Finite evidence and exact limitation

`CHECK_BELLMAN.py` exhaustively tested all complement-reduced Boolean truth
tables through four inputs and every inherited block of size at most two:

- 361,356 nonconstant `(f,Y)` states;
- zero positive Bellman residuals;
- worst best charge `-0.982280804536408` bits.

The computation chooses both child blocks independently and retains the full
signed node charge.  It is floating diagnostic evidence only; it does not
prove the all-dimensional sign.

## Next action

Expand `E_2` using `Delta U=B-Gamma+KL` and seek an aggregate transport that
pays the positive `K` part by the two chosen child orbit maxima without
reusing either block at another ancestor.  The first falsification target is
dimension five, where every `(f,Y)` state—not a fixed transition—must be
searched.

Model: Codex. Reasoning-effort metadata: UNKNOWN.
