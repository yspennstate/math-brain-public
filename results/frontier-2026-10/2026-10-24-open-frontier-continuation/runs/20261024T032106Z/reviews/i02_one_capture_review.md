# Independent review of ONE_CAPTURE.md

**Disposition: valid deterministic corollary of the selected reflected law.** I checked the claimed switch criterion, equality case, face action, and no-release barrier independently. The result is specific to the same-sign sector's single selected population and inherited positive endpoint. It does not simplify the general initially mixed law.

Write \(Q=\begin{psmallmatrix}a&\beta\\\beta&d\end{psmallmatrix}=C+PG\), \(\beta=C_{12}+\rho P>0\), after ordering the first-crossed residual axis as \(b=1\). The inherited normal \(B_1=(GI^a)_1\) is positive at the residual crossing \(\tau\), since \(I^a_j(\tau)>0\). Its tangential companion satisfies \(B_2-\rho B_1=(1-\rho^2)I^a_2>0\), so support 2 is positive up to any first normal face. Hence all selected endpoints really remain fully active and \(r^a=e^{-Qt}R\) remains the correct residual until that first face; the residual-axis crossing alone changes no gate.

For \(t\ge\tau\), the active residual is strictly mixed and \(k=-r^a_1/r^a_2\) obeys
\[
k'=\beta+(d-a)k-\beta k^2,\qquad k(\tau)=0.
\]
The two roots have opposite signs. Factoring the quadratic shows that \(k\) rises strictly toward its positive root \(\kappa\), without reaching it at a finite time. Since \(B_1'=r^a_2(\rho-k)\) and \(r^a_2>0\), \(B_1\) either rises forever when \(\kappa\le\rho\), or has exactly one maximum and a strictly decreasing tail when \(\kappa>\rho\). Its limit is \(\ell_1=(GQ^{-1}R)_1\). Starting from \(B_1(\tau)>0\), it therefore reaches zero at a unique finite time exactly when \(\ell_1<0\). If \(\ell_1=0\), the decreasing tail stays strictly positive and tends to zero only at infinity. At a finite contact, \(k(\sigma)>\rho\), so \(B_1'(\sigma)<0\): the contact is transversal. The same calculation applies with coordinates swapped.

The proposed face matrix \(Q_s=C+P(1-\rho^2)e_2e_2^T\) has the correct output action: with reflected normal held at zero, the supporting endpoint moves at speed \((1-\rho^2)r_2\). Its mixed ratio field \(f_s\) satisfies the exact identity
\[
f_s(\rho)
=C_{12}(1-\rho^2)+\rho(C_{22}-C_{11})
  +P\rho(1-\rho^2)
=f_a(\rho).
\]
Finite contact implies \(\kappa>\rho\), hence \(f_a(\rho)>0\). Scalar ODE uniqueness and the inward-pointing field at \(k=\rho\) keep a face trajectory starting at \(k(\sigma)>\rho\) strictly above \(\rho\) for every finite later time. \(Q_s\) has a positive off-diagonal, so the mixed residual signs and \(r_2>0\) persist. The normal driver \(r_1+\rho r_2=r_2(\rho-k)\) consequently stays negative: the Skorokhod regulator holds the normal at zero permanently, while the support increases. This establishes self-consistency of the two-matrix trajectory and, by uniqueness of the previously proved reflected Volterra equation, identifies it with the actual-GD selected limit.

I also checked the strict example exactly. For \(\rho=1/2\), \(P=1\), \(C=\begin{psmallmatrix}1&1\\1&3\end{psmallmatrix}\), and \(R=(1,10)\), \(Q=\begin{psmallmatrix}2&3/2\\3/2&4\end{psmallmatrix}\) and \(Q^{-1}R=(-44/23,74/23)\). Thus \((GQ^{-1}R)_1=-7/23<0\). The stated two positive ray masses \(2\mp2/\sqrt3\) for the \(15^\circ/75^\circ\) input pair reproduce this \(C\) exactly, so the example is compatible with the initialization support. Its exact prescribed parameter point has probability zero; the strict inequalities persist on a positive-probability neighborhood.

The negative initial quadrant is a genuine sign mirror. For \(s=-r>0\) and \(z<0\), the endpoint update is \(|z|G D(v)s\), while its signed output is \(-|z|q_+\). Negating the residual identity therefore gives \(s=S-C\int s-P_-V_s\), with \(S=-R>0\), exactly the positive-branch equation. The one-capture proof applies to \(s\) and negating it back gives the stated original residual.

The proof relies on the already established same-sign entrance and inherited-reflection matching. It does not imply that finite-width binary pre-step Grams converge to \(Q_s\) in \(L^1\), nor that arbitrary mixed initial residuals have a single permanent capture.
