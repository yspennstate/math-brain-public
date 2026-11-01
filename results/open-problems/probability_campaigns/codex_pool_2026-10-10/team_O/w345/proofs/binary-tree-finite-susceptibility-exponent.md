# C0065: Exact supercritical finite susceptibility on the degree-three tree

Label: proof; author checked only. Independent audit: PENDING w347.

For Bernoulli bond percolation on the infinite degree-three tree, 1/2<p<1, write chi_f(p)=E_p[|C_o|*1_{|C_o|<infinity}]. Then chi_f(p)=((1-p)/p)^3*(2-p)/(2*p-1), and (p-1/2)*chi_f(p)->3/4 as p decreases to 1/2. Below criticality chi(p)=(1+p)/(1-2*p), with (1/2-p)*chi(p)->3/4. Thus the finite-susceptibility exponents agree and equal one on this tree.

Assumptions: The infinite degree-three tree; Independent Bernoulli bond percolation; Susceptibility uses the unconditioned finite-cluster first moment

Let t be the probability that a directed edge does not lead to infinity. Independence of the two forward branches gives t=1-p+p*t^2; the smaller root for p>1/2 is t=(1-p)/p. The root cluster is finite exactly when all three outward edge branches fail, an event of probability t^3. Conditional on such failure, each edge is open and has a finite forward subtree with probability r=p*t^2/t=p*t=1-p. The finite cluster therefore has root offspring Binomial(3,r), then Binomial(2,r) offspring thereafter. The mean total size conditional on finiteness is 1+3*r/(1-2*r)=(2-p)/(2*p-1). Multiplication by t^3 proves the formula and the limit. For p<1/2 all branches die, and the same offspring computation with r=p gives the subcritical formula.

Limits: This is a branching-tree special case. It proves neither the high-dimensional lattice result nor the spatial correlation-length exponents; graph distance on a tree has different geometry.

Existing card: math:probability.percolation:open-problem-c0065-existence-and-equality-of-the-supercritical-exponents-gamma-nu-nu-2-in
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:1912
