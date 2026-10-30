SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B17, 2026-09-23T20:42:59Z.
attacking: upgrade the latest fleet03/B17 countable-fragment cone-tip theorem for the exact dense six-variable Householder matrix to a global all-output density barrier.

Early substantive calculation. Let T be the three-pair sum map, B=I-(2/3)11^T and A=T^TBT, so spec_nonzero(A)={1,1,-1}. For arbitrary finite/countable interval-indicator marginals of total support length one, split product cells by Tc=0 (kernel) versus Tc!=0. The partner proves the aggregate kernel bank subdensities h_{j,0} obey h_{j,0}<=h_*(y)=sqrt(2)(1-sqrt(2)|y|)_+. Therefore the entire kernel pushforward measure is dominated, for every Borel output set, by the connected triangular-bank control law; hence p_ker(s)<=p_*(s) a.e. at every output level, not only s=0.

For nonkernel cell-center gap Delta=inf{|Tc|:Tc!=0}, put M=Delta-sqrt(6)/2>0. On the union of nonkernel cells, |Ax|>=M. Partition into six charts by the largest |(Ax)_j|. On chart j, |d_j(x^TAx)|=2|(Ax)_j|>=2M/sqrt(6). For every fixed choice of the other five coordinates and every output s, the quadratic polynomial in x_j has at most two roots, so the one-dimensional delta formula gives chart density <=sqrt(6)/M after integrating the other five cap-one probability laws. Summing charts gives p_nonker(s)<=6sqrt(6)/M uniformly in s.

Thus the candidate global inequality is
||p_Q||_infinity <= ||p_*||_infinity + 6sqrt(6)/(Delta-sqrt(6)/2).
The remaining work in this run is to source-pin the global value of ||p_*||, apply the required e5f71d79... one-sheet theorem at a real inequality, and give an exact finite certificate for the explicit two-fragment stress family.
