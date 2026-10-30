# fleet03/B12 r71 repair ledger

Source: yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c, short/short.tex and short/short.pdf only.

## Candidate B12-C08 - Lemma 5.1 critical-value density version

Source line 398, PDF page 8.

Literal status: GAP (presentation/version only).

The displayed formula
p_T(z)=[f(m+r)+f(m-r)]/[2 sqrt(|a||z-v|)] * 1{(z-v)/a>0}
is not literally defined at z=v: the denominator vanishes while the strict indicator is zero.

Minimal repair: state the formula for z!=v / for almost every z, and define p_T(v)=0.

Independent justification in this run: T=v iff Y=m. Since Y has a Lebesgue density, P(Y=m)=0, so changing a density version at z=v changes no measure. The two inverse branches give the printed formula away from v. The interval-preimage estimate, all downstream small-ball bounds, and all constants are unchanged.

Peer comparison performed only after this derivation:
- fleet01/B12 commit ff84f24bb9d14965649112a1c5eaf8a131f0a697 independently reports the same one-point convention gap.
- fleet02/B12 commit b600280b697b51e9550e82e7a4778c60dc342f42 independently reports the same issue and repair.

This is not yet an owner-canonical addition to CORRECTIONS.md; the protected correction package was not modified.

## C01 regression

Line 412's global diffeomorphism wording remains literally FALSE. The slit-plane repair on theta in (0,2pi), with the ray and center omitted as null sets, was independently rechecked and preserves Jacobian 1/(2 sqrt(det B)) and the density constant.

## C02 regression

Lemma 5.4's off-diagonal branch still inherits the omitted Jensen step in Lemma 4.3: |E F|^2 <= E|F|^2. The repair remains independently valid. No inequality reversal was found.

## C03 regression

Lemma 5.3 still omits the critical level z=v. For nonsingular indefinite B the level is a union of two affine lines, hence null under the original joint density. The source already uses separate original coordinates for positive and negative tails; that part is correct.
