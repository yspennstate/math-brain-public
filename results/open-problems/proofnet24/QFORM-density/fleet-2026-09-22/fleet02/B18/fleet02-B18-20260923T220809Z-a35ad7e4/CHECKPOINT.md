# fleet02/B18 checkpoint — near-parallel private-bank conditional blowup

Programme: QFORM-DENSITY-3EIG-20260922
Status: supporting obstruction to a proof interface; full QFORM remains open.

Let U1,U2 be independent Uniform[-1/2,1/2] variables and set

B=(U1+U2)/sqrt(2),   V=(U1-U2)/sqrt(2).

The orthogonal change of variables has Jacobian one, so (B,V) has joint density exactly 1 on the diamond

D={ (b,v): |b|+|v| <= 1/sqrt(2) }.

For rho>0 and s!=0 put Z_{rho,s}=rho^2 B^2+sV. Direct coarea in v gives

p_{Z_{rho,s}}(0)
 = |s|^{-1} int 1_D(b,-rho^2 b^2/s) db
 = rho^{-2}[ sqrt(1+4 rho^2/(sqrt(2)|s|)) - 1 ].

Hence for fixed rho,

p_{Z_{rho,s}}(0) ~ 2^(3/4) rho^{-1}|s|^{-1/2}

as s->0. Therefore even for a genuine cap-one product source, and even though the two-dimensional projection (B,V) has joint density cap exactly 1, the quadratic-linear private-bank pushforward cannot have an s-uniform L-infinity bound near zero transverse slope.

This is not a QFORM counterexample. It is a counterexample to the prospective interpolation step that conditions away the complementary sources and then tries to bound the private bank uniformly through the aligned/transverse transition.

Target embedding to be completed in REPORT.md: spread two orthogonal J-directions g,c over many original coordinates, take beta=b0 c+rho B with b0^2+rho^2=1, and

Q=2 X0 G + 2 eta G V + (b0 C+rho B)^2.

In the orthonormal aggregate basis the nonzero spectrum is exactly {-sqrt(1+eta^2),1,sqrt(1+eta^2)}, while conditioning G=g,C=0 leaves the private-bank polynomial Z_{rho,2 eta g}. The pinned ruled one-sheet theorem will be applied to the same target family in the final report.
