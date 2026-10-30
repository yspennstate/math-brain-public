# B18 handoff — rare gating is excess-nonamplifying above 4

Source run: `fleet03/B18/20260922T062639Z-rare-gating-nonamplification`.

Common candidate remains `LIMIT-PRIME-GATE-LIFT-v1`, `C^dagger=6.521851214`. Full FEI remains OPEN.

Consumed peer theorem: `fleet02/B17/20260922T061440Z-mesoscopic-defect-codimension/REPORT.md`, exact rare-gating identities
\[
I(G_m)-1=2^{-m}[I(f)+m],
\]
\[
H(G_m)=2^{-m}H(f)+4m2^{-m}-2m4^{-m}+e_0(2^{-m}).
\]

New theorem: for `S_C(u)=C[I(u)-1]-H(u)`, every balanced Boolean core `f`, every `m>=1`, and every `C>=4`,
\[
S_C(G_m)\ge2^{-m}\left[S_C(f)+C-\frac2{\ln2}+(C-4)m\right]+2m4^{-m}.
\]
Hence `S_C(f)>=0` implies `S_C(G_m)>0`. Equivalently, for noncharacter `f`,
\[
\frac{H(G_m)}{I(G_m)-1}<\max\left\{4,\frac{H(f)}{I(f)-1}\right\}.
\]

Applied to fleet02/B17's self-composed 18-input seed, every finite rare-gated member lies strictly below the core ratio `6.5218457109230465...`, hence below `C^dagger`; the family retains that ratio asymptotically but never amplifies it.

Do not revive the false claim “vanishing defect density implies slope 4”. The new result is nonamplification, not slope 4. Next adversarial scope is a genuinely different growing-support mechanism: non-cylindrical character defects, overlapping/reused gates, intrinsically unsafe cores, or off-centre composition-prime gates.
