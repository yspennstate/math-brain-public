# Why averaging physical-pair RW2 bounds loses dimension

**Scope.** This is an exact obstruction to two elementary proof mechanisms, not a counterexample to restricted weak-L² or to the quadratic-form density conjecture. It shows that convex averaging of conditioned physical-pair bounds, or a tensorization controlled only by within-pair determinant energies of a disjoint matching, cannot produce a dimension-free constant on a genuinely diffuse three-frame.

Let \(n\geq5\) and \(\theta_j=2\pi j/n\), \(0\leq j<n\). Define three columns of an \(n\times3\) frame by
\[
 l_j=n^{-1/2},\qquad
 v_j=(2/n)^{1/2}\cos\theta_j,\qquad
 p_j=(2/n)^{1/2}\sin\theta_j.
\]
Roots-of-unity orthogonality gives \(l^{\mathsf T}l=v^{\mathsf T}v=p^{\mathsf T}p=1\) and all cross inner products zero. The row leverage is \(3/n\).

For distinct \(i,j\), the physical planar minor of \((l,v)\) is
\[
 d_{ij}=l_iv_j-l_jv_i
       =\frac{\sqrt2}{n}(\cos\theta_j-\cos\theta_i),
 \qquad |d_{ij}|\leq \frac{2\sqrt2}{n}. \tag{1}
\]
By Cauchy–Binet, \(\sum_{i<j}d_{ij}^2=1\). Thus the unit total area is spread across \(\Theta(n^2)\) pairs.

A bank \(B\) satisfies the exact planar condition \(P_B=\alpha L_B+\eta V_B\) precisely when its row points \((\cos\theta_j,\sin\theta_j)\), \(j\in B\), lie on one affine line in \(\mathbb R^2\). A line meets the unit circle in at most two distinct points, so **every exact planar bank has at most two original coordinates**. Consequently the conditioned-bank RW2 estimate with \(M=1/|d_{ij}|\) has constant at least
\[
 4\sqrt2(\sqrt2-1)\min_{i<j}\frac1{|d_{ij}|}
 \geq 2(\sqrt2-1)n, \tag{2}
\]
and its output-density bound is at least \(2n+\tfrac12\). (These are lower bounds on the *method's upper-bound constants*, not lower bounds on the actual RW2 or output densities.)

Taking a convex combination of the physical-pair upper bounds cannot reduce (2): if \(w_{ij}\geq0\) and \(\sum w_{ij}=1\), then \(\sum w_{ij}/|d_{ij}|\geq\min_{ij}1/|d_{ij}|\). Nor can a disjoint matching recover the Cauchy–Binet area using only its within-pair minors: for any matching \(\mathcal M\),
\[
 \sum_{(i,j)\in\mathcal M}d_{ij}^2
 \leq \lfloor n/2\rfloor\,\frac8{n^2}
 \leq\frac4n. \tag{3}
\]
The remaining area lies in **cross-pair** minors. A successful convolution or Rogozin argument would have to exploit those cross-pair interactions or retain the full three-dimensional banks; (3) does not rule out such an argument.

For context, if the original coordinates are independent identical Gaussians with variance large enough that their densities are at most one, then this very same orthonormal frame yields independent Gaussian \(L,V,P\), and the all-target RW2 estimate follows from the independent-leakage theorem with a universal constant. Thus the frame is an obstruction to a pairwise *proof*, not evidence that RW2 itself fails.

Related: [conditioned planar-bank RW2 theorem](https://github.com/yspennstate/math-open-problems/blob/d9a9e74e807d3c4687802a347de2006e130b3938/proofnet24/QFORM-density/interactive/20260923T205000Z-conditioned-planar-bank-rw2/REPORT.md).