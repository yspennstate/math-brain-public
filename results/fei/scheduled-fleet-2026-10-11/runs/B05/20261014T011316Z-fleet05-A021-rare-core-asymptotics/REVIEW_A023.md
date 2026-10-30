# Scoped independent review: A023 single-separator reserve

Source: A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER v2, statement hash
ceb0a37e4a74494589bdfd8efddf7cdad84f842cfba3ba3f1bc6932b12d9fc9c,
run 20261013T223305Z-fleet05-A023-amortized-rarity-budget,
SEPARATOR_RESERVE_PROOF.md. Reviewer A021 supplied no repair.

Verdict: HOLDS for the single-separator entropy/face theorem: directional
boundary identity, exact physical influence partition, root face <= one
remaining control-plus-terminal influence reserve, descendant threshold-4
goodness, and resulting max(5+2/ln2,C0+1) entropy bound when the terminal
has H(g)<=C0 I(g). This is not acceptance of the entire bundled v2 claim
or all its source computation.

Independent reconstruction is DERIVATION.md section 5: directional edge
cuts of B=WUV and C=U OR V are disjoint, so J(C-B)=J(B)+J(C).
Root product is 1+(C-B)(g-1). Balance gives
c_X=[J(B)+J(C)+(EC-EB)I(g)]/2. Since (EC-EB)/2<=pi=(EB+EC)/2,
c_X<=Jrem+pi I(g)=I(F)-d_X. Every physical account is named once;
the root reserve is not available for renewed descendant reservation.

code/check.py independently generates all direct control truth tables
for L,R,T=1..3 and two balanced actual cores, counts edges of C-B,
and checks the child-product influence and reserve inequality.
All 54 reconstructions PASS, saved in out/A023_boundary_certificates.json.
No A023 code or saved numeric output is imported. The exact proof handles
all positive widths; finite cases corroborate, not extrapolate, that proof.

For descendant erasure, sum all empty-selector row packets before the
constant-row separation in DERIVATION.md section 1. Their derivative
mass is rho^2 gamma and total mass <=1, yielding
B/d<=2(1-rho)+rho log2(e/(rho^2 gamma)). Source disagreement gamma is
(1-r)/2>=1/4 for the active two-event branch and 1/2 for a single-point
branch. With rho=2^-l this is <=2+2^-l(c+2l)<4. Thus the descendant
claim is reconstructed analytically, not left as a conditional premise.
Adding its entropy costs to the one-use root reserve proves the source
single-separator theorem. The balanced bent-selector terminal conclusion
follows from H<=m+1 and I=1+m/2+(m+1)2^-m, giving H/I<2<3.

The earlier bundled unbalanced-core two-event theorem, entire v2 claim,
source's full retained-KL computation, and arbitrary-depth reservations
are excluded from this review. The new threshold-7 result independently
handles all point-block separator widths and arbitrary terminal core bias;
it is not a repair to the correct one-bit source theorem.

A023's independent review of A021 v1 is consumed at its recorded scope:
five-bit witness and arbitrary-balanced-core CONTROL B,d transfer only.
It does not close review of A021's tensor exposure or 680-controller census.
