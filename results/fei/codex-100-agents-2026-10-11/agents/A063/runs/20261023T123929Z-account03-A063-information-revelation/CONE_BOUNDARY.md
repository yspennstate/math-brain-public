# Exact first boundary: one selector already leaves the affine reference cone

This is a source-bound consequence of the ACTUAL Boolean family in previous
A063 run 20261023T065336Z, PROOF_OBSTRUCTION.md; no new broad candidate is
introduced. It states exactly what fails when extending PROOF_PREFIX.md.
Use n=2r>=4 data bits u_1,...,u_r,v_1,...,v_r, N=2^n, and one selector.
Its children are the quadratic phases
  g_dense=(-1)^{sum u_j v_j},
  g_sparse=(-1)^{(sum u_j)(sum v_j)}.
The dense spectral law is uniform on all N masks. The sparse law is
uniform on L={empty,U,V,U union V}; both have every data influence 1/2.
Thus the erased ORIGINAL actual full-product reference is uniform on N
masks, including when the selector's own influence is not 1/2.

Query the selector physically, with exactly the shared fair zero-source
convention. Its erased source qbar=(p_dense+p_sparse)/2 is positive
everywhere. Therefore no zero-source choice is involved in this particular
query. Exact actual normalized outcome masses are
  pi_dense=N/(N+4), pi_sparse=4/(N+4).
The normalized dense predicted reference is
  Q_dense(t)=4/N^2             for t in L,
  Q_dense(t)=(N+4)/N^2         for t outside L.
The sparse predicted reference is exactly p_sparse.
These formulas follow directly by multiplying the erased uniform reference
by p_b/(2qbar) and dividing by the displayed outcome mass. They normalize:
4*4+(N-4)*(N+4)=N^2. Both types of dense rows exist for N>=16, and their
densities differ. Since the dense child's actual support is the WHOLE cube,
the only affine subspace containing it is the cube itself. Consequently
Q_dense is NOT a mixture of uniform affine superspaces containing the
actual support. The cone invariant fails at a single cubic selector.

This does NOT disprove an influence-funded extension. On the dense branch,
resetting to its actual product (uniform) costs -KL(p_dense||Q_dense)<0,
so that cone repair itself requires no positive bill. On the sparse branch,
the incoming reference ALREADY belongs to the cone (it equals p_sparse),
but resetting to its actual product costs n-2. Thus cone membership ALONE
does not justify initial product admission or a newly issued r/2 rank owner.
The inherited source KL on the sparse branch is zero although its product
TC is n-2; both must stay explicit. Mean signed product-reset price is
  (n-2-KL(p_dense||Q_dense))/2,
and actual outcome O=KL(fair||pi) is separate. These are the exact costs
already bounded in the earlier local-price obstruction. No local J or B
budget has become available merely by renaming the cone.

The next universal step is therefore to pay the INHERITED ADMISSION GAP
and weighted reference-cone repair from the SAME unused original influence
bank across nonquadratic branching, keeping O/E/K, full terminal H, and old
debits. Requiring the unweighted affine cone itself to survive this selector
is already refuted. Rank-owner eligibility must not be renewed at children.
