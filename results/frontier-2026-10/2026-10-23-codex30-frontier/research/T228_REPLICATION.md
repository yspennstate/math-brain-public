# T228 replication, exact certificate, and overlap correction

The stationary-tail theorem for smooth bounded perturbations of a linear activation was already proved in Brain before this campaign. A17 and PROVENANCE.md identify the prior files. This package retains the independent proofs and checks, while **withdrawing any new-row-solution claim**.

For a concrete independent check, take Gaussian X∈R², Y∼N(0,1), activation φ(z)=z+10^{-3}tanh(z), step η=13/25, and fresh samples in constant-step half-square-loss SGD. Its radial asymptotic multiplier satisfies

\[
M^2=(1-\eta Z^2)^2+\eta^2 Z^2V,\qquad Z^2,V\stackrel{ind}{\sim}\chi^2_1.
\]

Independent rational calculations certify

\[
EM\le\frac{7941802637}{8025437500}<1,
\qquad EM^2=\frac{651}{625}>1.
\]

Thus the positive moment root is strictly between 1 and 2. A fixed-pair expected-distance contraction bound is

\[
E\|F(w)-F(v)\|\le\kappa\|w-v\|,
\qquad \kappa\le\frac{2004230183}{2006359375}<1.
\]

The numerical root 1.8403225889 is descriptive quadrature, not an interval-certified decimal. The (1,2) bracket and contraction are exact. A14 and A20 derive the certificate independently; scripts are in research/code/.

A10–A16 independently check stationarity, density/minorization, radial asymptotic linearity, nonarithmeticity and the nonzero exact tail constant. The ABB limit theorem and positivity proposition are separate. Arbitrary positive tanh coefficient ε remains compatible with the drift/renewal proof, whereas a small ε is used for the explicit radial Lipschitz certificate. These are confirmations or narrow assumption relaxations relative to the prior target, not a fresh heavy-tail discovery.

A03/A06–A09 also derive the sign-symmetric leaky-ReLU affine-kernel reduction, sharp second-moment threshold and minibatch formulas. The transition-kernel identity does not imply pathwise independent gates, and a derivative convention at zero can create an absorbing atom. A09's low-index batch monotonicity counterexample is numerical and should not be promoted to an interval-certified theorem.
