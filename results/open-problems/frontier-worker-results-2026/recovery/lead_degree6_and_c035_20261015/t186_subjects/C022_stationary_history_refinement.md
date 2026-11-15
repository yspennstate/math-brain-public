# C022 v1: stationary finite-history refinements remain subcritical

Status: proof (unaudited), auxiliary ideal-tree result for target 3. No finite-graph threshold or uniform-in-history-length estimate is claimed.

Setup. Let H be a finite alphabet with a terminal map ell:H->{0,1,2,3}. Let Psi be a deterministic multiset update with

    ell(Psi(S)) = M(ell(S)) for every finite multiset S.

Here M is the monotone update of C005. Let Q be a fixed point of the Poisson history recursion: Psi(N) has law Q for N~Pois(c Q). Discard histories with Q_h=0. Its terminal law pi=ell_*Q is assumed interior. Let T be C009's 24-type stationary downward-change mean matrix for pi, with rho(T)<1.

Use the compatible C021 types

    (A,a,b,d), ell(A)=a, 0<=b<a, Q_A Q_d>0.

Define B by the C021 formula, with denominator Q_d=P_d. A child (A',u,v,z) has ell(A')=u by the commuting identity, so this type space is closed. Then rho(B)<1.

Proof by a projection of the recursive tree process. A history-labelled Galton--Watson cavity tree can be sampled recursively as follows. Give a root prescribed reverse history d; its children histories form a Poisson(c Q) multiset conditioned on Psi(N)=d. Conditional on these histories, their descendant trees are independent and have the corresponding conditional laws. At any finite depth this construction has the same law as first drawing independent Poisson descendant templates and conditioning their root output; the fixed-point equation makes these finite-depth distributions consistent. Kolmogorov consistency therefore defines the process. Degree means conditional on d are finite since Q_d>0.

If the root history d is instead first drawn according to Q, forgetting all history information except terminal messages gives the recursive terminal-message tree with independent Poisson(c pi) inputs. Conditioning only ell(d)=j gives that same terminal tree conditioned on its outgoing message being j. This follows at every finite depth by summing the full-history labels before applying the deterministic commuting projection.

Fix an incoming boundary history A with ell(A)=a and a new terminal value b<a. Sample the root history d from Q conditioned on ell(d)=j. On the sampled full tree propagate the terminal perturbation a->b. Its terminal cascade depends only on the terminal-labelled tree and a,b, not on the other coordinates of A. For each reached child the unchanged incoming history is Psi(the other inputs plus A), and the outgoing reverse history is its own subtree history. Conditional on those histories, descendant subtrees have exactly the conditional laws above: the incoming boundary history was computed outside that child's descendant subtree, and any constraint at its parent uses that subtree only through its outgoing history. Thus the full-type cascade is the branching process with mean B. Its terminal cascade, with the root history averaged as specified, has exactly C009's law started from type (a,b,j). This comparison is a distributional statement after averaging hidden histories at the root; no per-parent-type lumpability is asserted.

To make all refined starting types have positive mass, choose each of the six terminal pairs (a,b) with probability 1/6, choose A with law Q_A/pi_a conditional on ell(A)=a, and choose d independently with law Q_d. This gives a strictly positive initial vector x on the finite refined type space. The projected initial vector is y_(a,b,j)=pi_j/6. For every generation r>=0 the coupling just described gives

    1^T B^r x = 1^T T^r y.

As rho(T)<1, summing the right side over r gives a finite number. Since x has strictly positive coordinates, the expected total progeny from each individual refined type is finite as well. A finite nonnegative matrix for which all these sums are finite has spectral radius below one: the series sum_r B^r converges entrywise, and any nonnegative Perron vector with eigenvalue >=1 would contradict that convergence. This proves the claim.

Concrete augmented histories. On the same Poisson tree let X_t be the top-initialized message at round t and X_infty its monotone limit from C005. For fixed t use the history (X_0,...,X_t,X_infty). The update Psi sets X_0=3, shifts the finite-round coordinates using M, and updates the last coordinate using M on the incoming limiting messages. Finite degrees ensure M commutes with the monotone limit, so this history law Q is a fixed point and the terminal projection to X_infty commutes with the update. Therefore the claim applies for every fixed t at the certified C009 points. The trace's finite-round terminal X_t is distinguished from its limiting terminal X_infty; no false equality between them is required.

What is still unpaid. This gives no bound uniform in t on the refined weights, contraction gap or rare-history denominators. The actual finite graph has finite top-initialized histories, not observable X_infty labels. A proof must transfer the augmented stationary law to its exploration and bound the weighted mass of history discrepancies, multiple hits and baseline instabilities. Simply making the unweighted discrepancy probability small while allowing refined weights to grow is insufficient. Thus this removes an ideal-tree subcriticality concern but does not yet discharge the finite WP conditional-law and error-budget input.
