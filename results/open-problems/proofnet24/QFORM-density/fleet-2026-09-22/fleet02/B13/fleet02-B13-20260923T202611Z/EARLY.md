SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T20:26:11.610970Z.
attacking: the shared-input third-smoothing endpoint after the diffuse symmetric-rank-two rough-tail reduction; force every external physical hub coupling into the same actual rank-two cross plane at slab scale, then test whether any absolute twisted-Wiener bridge survives vanishing leakage.

# Early substantive calculation

Let a slab witness have ratio rho. Use the completed aggregate third-volume estimate inherited from fleet03/B13 r30:

    e3(B^T B) <= (C3/rho)^6,      C3=9 sqrt(3e),

for every disjoint physical cross block B.

Fix disjoint physical banks I,J and M=A[I,J]. Let its singular values be s1>=s2>=..., with left singular vectors u1,u2,..., and let P be the projection onto span(u1,u2). For a further physical coordinate h outside I union J put c=A[I,{h}] and N=[M c]=A[I,J union {h}]. Then exact exterior algebra gives

    e3(N^T N)
      = e3(M^T M)
        + sum_{r<s} s_r^2 s_s^2 ||P_{span(u_r,u_s)^perp} c||_2^2.

In particular, with tau_h=||(I-P)c||_2,

    s1^2 s2^2 tau_h^2 <= e3(N^T N) <= (C3/rho)^6,

hence

    tau_h <= C3^3 /(rho^3 s1 s2) <= C3^3 /(rho^3 s2^2).          (E1)

The same argument applied to M itself yields

    sum_{r>=3} s_r^2 <= C3^6 /(rho^6 s1^2 s2^2),

so the best rank-two Frobenius tail of M is at most the same right side in (E1).

For the fleet03/B13 r33 diffuse rank-two branch, its physical paving has s2(M)>=21 sigma/64. Therefore every external hub h obeys

    tau_h <= 157678.505 sigma^(-2) rho^(-3),

and if H has at most four physical hubs then

    ||(I-P) A[I,J union H]||_F
       <= sqrt(5) * 157678.505 sigma^(-2) rho^(-3)
       < 352580 sigma^(-2) rho^(-3).                              (E2)

Thus a high-density witness cannot retain an O(1), or even O(rho^-3/2), genuinely transverse shared-input hub direction once the rank-two cross bank is nondegenerate: every hub column is forced into the same *actual physical* singular two-plane up to O(rho^-3).

Pinned-source application: before using the aggregate gate removal, the immutable e5f71d... D' theorem applied directly to N says that if its natural squared-third-minor row marginals are <=2/3, then

    rho <= 9 sqrt(3e) e3(N^T N)^(-1/6)
        <= 9 sqrt(3e) (s1 s2 tau_h)^(-1/3).

So (E1) is exactly the gate-free completion of a real pinned Fourier obstruction, not a spectral heuristic.

Next: prove the scaling falsifier showing that coefficient-small transverse leakage still does not justify a universal absolute twisted-Wiener L1 estimate for arbitrary cap-one rough laws; then isolate the genuinely phase-sensitive aligned-hub lemma that remains.
