# Independent reconstruction of A034 quadratic affine-row admission

Verdict: **HOLDS at the exact scope of A034-QUADRATIC-AFFINE-ROW-CONDITIONAL v1.** This receipt is local. No shared claim registry or original A034 file has been changed. A079 supplied no repair and is not a contributor to that version.

Source read: A034/runs/20261011T223816Z-fleet05-A034-phase-energy-transfer/{REPORT.md,CLAIMS.json,CONDITIONAL_PHASE_THEOREM.tex}. The proof file's stated SHA256 is 6368edaba63c3044e26cc3c38a0d8e88a0b367bba77390f7ce82072f3b9a4541; the current byte hash is recorded independently in out/source_receipts.json. A034's next-stage directory had no REPORT.md or CLAIMS.json when first inspected; no theorem from that incomplete directory is assumed.

## Reconstruction by signed translations and frequency orbits

Take an affine cell A=a+V in an m-bit physical Y cube, codimension k, and a quadratic phase u(y)=1_A(y)(-1)^q(y). Work with Q(v)=q(a+v). Its polar form beta on V has rank r and kernel K of dimension m-k-r.

For w in K, translating u by w preserves its support and changes its sign by a constant linear character ell(w)=Q(w)+Q(0). Thus any occupied Fourier frequency t satisfies t dot w=ell(w). The Fourier support lies in a nonempty affine coset L of K-perp, of dimension k+r.

The coefficient magnitudes are invariant under frequency translations in V-perp, since characters with those frequencies are constant on A. Translating u by any v in V also multiplies its phase by a character whose restriction to V is beta(v,·), plus a constant sign. Taking Fourier transforms shows invariance of coefficient magnitudes under any extension of beta(v,·) to the ambient space. The image of the polar map has dimension r, and, together with V-perp, these frequency translations span K-perp. They act transitively on L.

Parseval gives nonzero total mass alpha=2^-k. Hence every frequency in L is occupied with the same squared coefficient 2^(-2k-r). The normalized row law is uniform on 2^(k+r) frequencies. This establishes A034's flat affine row law without relying on its squared-Walsh kernel-average argument.

If a' physical spectral coordinates vary on L and b' are fixed to one, the expected spectral degree is a'/2+b'. The dimension of the translation space of L is k+r, and a' coordinates support that space, so a'>=k+r. Thus each normalized row has H=k+r<=2 expected degree.

Distinct X labels assign the original disjoint physical cells to distinct partial Fourier rows. The row masses alpha_j sum to one. Therefore H(S_X)=sum alpha_j k_j, H(S_Y|S_X)=sum alpha_j(k_j+r_j)<=2 I_Y, and H(F)=sum alpha_j(2k_j+r_j)<=4I_Y. Empty labels, constants, zero phase rank and zero data influence require no exception to this calculation.

## Stability and tensor guards

An arbitrary physical Y restriction intersects each affine cell with a coordinate affine subspace and restricts its quadratic phase; empty cells disappear and the others still partition the remaining cube. An X restriction deletes coordinates from the label characters and contributes constant signs. This preserves admission exactly when projected labels remain distinct; no claim of arbitrary X-restriction closure follows.

If an admitted function factors as h(X,Y)g(Z) with Z a fresh Boolean sign factor, take a nonzero partial X row and fix a point Y=y0 in its support. The original unit quadratic row now restricts to a constant sign times g(Z). Thus g is a quadratic phase. This proves the fresh-factor guard and does not assume FEI.

Conversely, ordinary addressing F(X,Y)=X_Y is admitted for every address dimension. Restricting all physical X data bits to an arbitrary Boolean truth table g(Y) produces g(Y). Therefore a class containing all these examples and closed under all X restrictions contains every Boolean function. A conditional bound on that full hereditary closure has full-FEI scope. This closure obstruction is part of the original theorem, not an error in it.

## Independent exact finite check

Before execution, out/A034_REVIEW_FROZEN_SPEC.json fixed m=3, all 128 degree-at-most-two binary phases, every nonzero hyperplane normal and both affine cosets, plus full-cell rows. Command:

    python -X utf8 runs\20261012T044009Z-fleet05-A079-correlated-auxiliaries\code\check_a034_review.py

The 1,920 Boolean fixtures passed 31,232 exact assertions in 0.5342968999999584 seconds. The separate checker computes the polar rank on an enumerated direction-space basis, verifies raw row norms, affine-law flat cardinality, exact normalized entropy, physical varying/fixed coordinate energy, and the conditional/joint chain rule. It uses integer Walsh transforms, Fraction arithmetic and exact prime-log expressions, not numerical entropy inequalities. The all-dimensional acceptance rests on the signed-translation reconstruction above, not the finite sample.

## Application to A079

The actual partial row of the character-tag construction is (-1)^(a dot b) ghat(v+c_b). Every noncharacter seed produces an intermediate row magnitude at an untagged B-value, violating A034's unit-row requirement. Character seeds are admitted precisely when the zero-code B-support is affine. The first-stage point-specific tags have one small admitted case k=1,m=2; their other cases fail unit amplitude or affine support. These are hypothesis checks, not counterexamples to the accepted theorem.

The unproved application remains payment after label collisions or nonquadratic/intermediate-magnitude rows. Neither A034's accepted scope nor the present paired stopping ledger supplies that payment.
