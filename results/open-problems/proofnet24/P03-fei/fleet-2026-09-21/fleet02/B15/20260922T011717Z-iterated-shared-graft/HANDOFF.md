# B15 handoff — center-cap obstruction raised by iterated shared-core graft

**Source run:** `20260922T011717Z-b15-iterated-shared-graft`  
**Full FEI:** OPEN.

The live old implication was the 162-graft-scale scalar-lift / PRIME-GATE-LIFT candidate. It is false at its old center cap.

Using the source-bound 18-bit host skeleton and the certified 162-bit shared graft \(F\), take the balanced monotone gadget \(h=F^{\circ4}\). The nine reusable outer-core singleton coefficients of \(F\) are exactly

\[
\ell=14593/65536.
\]

Choose the nested leaf of \(h\), whose singleton coefficient is

\[
b=\ell^4=
45350108441011201/18446744073709551616.
\]

Insert one copy of \(h\) in each of the nine old host edges, reusing that leaf coordinate as the host pivot. The general exact graft ledger is

\[
H(T(h))=H_0+\frac9{256}H(h)+K(b),
\qquad
I(T(h))-1=(I_0-1)+\frac9{256}(I(h)-1).
\]

A rational-log certificate proves \(K(b)>0\) and gives a finite balanced monotone
\(6,198,727,824\)-variable Boolean function \(G\) with

\[
I(G)=
784028312243315011737/
295147905179352825856
\]

and

\[
\frac{H(G)}{I(G)-1}
\ge
6.521850763518463531668608228451477683404661343868474608138632.
\]

The previous 162-bit obstruction has certified upper endpoint

\[
6.521850083658612443633672199029299526203969334599290679529011,
\]

so the strict gain exceeds \(6.7985985\times10^{-7}\).

By the completed balanced-excess equivalence (fleet01/B18), this raises the source-bound FEI lower bound to

\[
C_{\rm FEI}>6.5218507635184635316686082284514776834\ldots
\]

via balanced recursive amplification. It does **not** refute FEI. It does refute every all-gate potential whose center cap is at most the previous 162-graft cap, including the then-minimal scalar lift. No off-center shape can repair that failure because the witness is balanced at uniform input bias.

The useful next question is whether the exact shared-core functional
\[
K(b)
\]
can be iterated/optimized with heterogeneous gadgets or larger free faces to give either a finite universal envelope or a genuinely unbounded sequence.

See `REPORT.md`, `verify_iterated_shared_graft.py`, and `verification_output.json` in the same run folder.
