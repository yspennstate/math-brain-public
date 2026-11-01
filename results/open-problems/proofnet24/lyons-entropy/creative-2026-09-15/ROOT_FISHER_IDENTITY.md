# Exact two-site fiber identity and failure of entrywise Fisher domination

Root derivation, 15 September 2026. This is supporting research, not one of the 100 worker assignments. It does not settle entropy concavity.

Fix an outside occupation configuration and write its four positive full-atom weights as a=p00, b=p10, c=p01, d=p11. For affine variation of the two diagonal kernel coordinates, the first coordinate derivative has values -(a+b), +(a+b), -(c+d), +(c+d); the second has values -(a+c), -(b+d), +(a+c), +(b+d). The fiber contribution to the Fisher cross entry is therefore

J12=(a+b)(a+c)/a -(a+b)(b+d)/b -(c+d)(a+c)/c +(c+d)(b+d)/d.

Expansion gives the exact identity

J12=(bc-ad)(1/a+1/b+1/c+1/d).

The corresponding frozen entropy-curvature cross entry is

C12=(a+b+c+d) log(bc/(ad)).

For determinantal laws bc>=ad by conditional negative association, but J12>=C12 need not hold. This is an entrywise comparison; it is not a positive-semidefinite comparison of the complete Fisher and curvature matrices.

Take a=c=d=1/100 and b=97/100. This is the atom law of the strict two-site marginal kernel

K=[[49/50, sqrt(6)/25], [sqrt(6)/25, 1/50]].

Its trace is one and determinant is 1/100, so its two eigenvalues lie strictly between zero and one. The atom law follows from p11=det K and the diagonal marginals. Then

J12=7008/2425<3, whereas C12=log 97>4.

The last inequality follows from e<3 and e^4<81<97. Consequently J12-C12<-1. This is an exact obstruction to a proposed entrywise proof, not a counterexample to the known two-site entropy concavity theorem. The full diagonal Fisher entries retain the compensation lost by comparing cross entries separately.

For a general fiber, the diagonal entries that must be retained are

J11=(a+b)^3/(ab)+(c+d)^3/(cd),
J22=(a+c)^3/(ac)+(b+d)^3/(bd).

These formulas suggest integrating the entire rational-minus-logarithmic matrix, as in creative reports C003 and C009, rather than estimating its off-diagonal entries independently. No general matrix-integral positivity theorem is established by this note.
