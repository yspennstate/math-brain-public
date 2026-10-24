# C0033: concavity for every two-site kernel with fixed diagonals

Label: proof, awaiting w346. This proves a restricted class of the finite-kernel conjecture; it does not settle varying diagonals or higher dimensions.

Let K(z)=[[a,z],[conjugate(z),b]], with fixed a,b in [0,1]. It is a Hermitian positive contraction exactly when |z|^2 <= min(ab,(1-a)(1-b)). This follows from the principal-minor criteria for K and I-K.

Put r=|z|^2, A=ab, B=(1-a)(1-b), C=a(1-b), D=(1-a)b. The four subset probabilities are A-r, B-r, C+r, D+r. They follow from P({1,2} subset X)=det(K) and the one-site inclusion probabilities a,b; they are nonnegative and sum to one. Also AB=CD.

For interior probabilities let F(r) be their Shannon entropy using natural logarithms. Direct differentiation gives

F'(r)=log((A-r)(B-r)/((C+r)(D+r))) <= 0,

F''(r)=-1/(A-r)-1/(B-r)-1/(C+r)-1/(D+r) < 0.

The first inequality uses AB=CD and r>=0: each numerator factor decreases and each denominator factor increases. Thus F is concave and nonincreasing on the feasible interval; continuity, with 0 log 0 = 0, includes the endpoints. If the feasible interval consists only of zero, the conclusion is immediate.

For complex z0,z1 and 0<=t<=1, |t z0+(1-t)z1|^2 <= t|z0|^2+(1-t)|z1|^2. Applying the monotonicity and then concavity of F proves

H(P_K(t z0+(1-t)z1)) >= t H(P_K(z0))+(1-t) H(P_K(z1)).

In particular H(P_K(z)) <= H(P_K(0)) = h(a)+h(b). The step that remains for the complete two-site conjecture is simultaneous variation of a,b and z; this proof does not supply that step.
