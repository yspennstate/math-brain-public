# Independent obstruction, saved before reading the paired proof

2026-10-10. No proof by w360 has been read at this checkpoint.

Consider the square graph with opposite corners s and t. Its two s-t paths have iid edge weights X1,X2 and Y1,Y2, each uniform on {1,2}. Select the X path on ties. Set E={X1+X2 <= Y1+Y2}. All weights are positive, so these two paths are the only simple contenders.

The four possibilities (X1,X2)=(1,1),(1,2),(2,1),(2,2) have respectively 4,3,3,1 compatible Y assignments on E. Hence P(E)=11/16 and

P(X1=2 | E)=P(X2=2 | E)=4/11,
P(X1=X2=2 | E)=1/11 != (4/11)^2.

Thus conditioning on the selected geodesic destroys independence even between two distinct iid edges on that geodesic. Cov(X1,X2 | E)=-5/121.

Unconditionally, let C1,C2 be the successive edge costs of the selected path. Their joint probabilities for (1,1),(1,2),(2,1),(2,2) are 7/16,4/16,4/16,1/16. Therefore Cov(C1,C2)=-9/256 and Var(C1+C2)=23/64, whereas Var(C1)+Var(C2)=55/128. Optimization creates a nonzero covariance term.

Scope: this refutes an independence inference based only on disjoint underlying edges after global path selection. It does not refute the KPZ conjecture or the independence of costs defined on fixed disjoint edge sets. The necessary repair is a proved factorization under the actual selection conditioning, or a covariance/martingale argument valid for the selected costs.

Status: proved special case, author derived, pending independent referee w362. Exact exhaustive verification is the next step. No novelty claim.

## Tie-free control

For four iid Exp(1) weights, the two paths tie with probability zero. Write E={X1+X2 < Y1+Y2}. Since the other path has Gamma(2,1) cost, its survival probability at s is exp(-s)(1+s), and P(E)=1/2. The conditional density of the upper costs is

2 exp(-2(x+y))(1+x+y), x,y>0.

Using integral_0^infinity x^k exp(-2x) dx = k!/2^(k+1) gives E[X1|E]=E[X2|E]=5/8 and E[X1 X2|E]=3/8. Therefore Cov(X1,X2|E)=-1/64. Unique geodesics do not repair the selection-dependence inference.

## Exact repair premise

Let U,V be independent with laws mu,nu and let E be any event of probability Z>0. Define w(u,v)=P(E|U=u,V=v). The selected conditional law has density w/Z relative to mu times nu. U,V remain independent given E if and only if

w(u,v) = a(u)b(v)/Z almost everywhere,

where a(u)=integral w(u,v) nu(dv) and b(v)=integral w(u,v) mu(du). This follows by comparing the joint density with the product of its two marginal densities. For discrete variables it is the rank-one condition on the selection-likelihood matrix. Merely identifying disjoint underlying coordinates does not establish this premise.

Exact receipt COUNTEREXAMPLE_RECEIPT.json was produced by `python -X utf8 -B verify_counterexample.py`. The discrete calculation checked all 16 assignments in 0.001382 seconds; the continuous control uses exact gamma integrals. Fixed unselected costs have covariance 0 as a negative control. These checks support the finite calculation; they are neither an independent referee report nor an asymptotic FPP proof.
