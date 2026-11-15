VERDICT: PARTIAL an endpoint boundary-score reduction and sharpness of the comparison coefficient for nested increasing events

The round 5 result holds under independent verification. Random shifted
sampling and a Fourier-symbol interpolation calculation rederive

    kappa R <= cap(B_R) <= kappa(R+1/2).

The face decrement and the coefficient (log 2)^2/(8 kappa) also check
out. The brief web check found no later lattice resolution; the recent
papers opened concern cable systems. Sources are in LITERATURE.md.

The new piece identifies the boundary statistic that the missing
connection estimate must control, and proves a sharp obstruction for
the broader class of nested increasing events.

Write a_R=cap(B_R), e_R for equilibrium measure, and
M_R=sum_x e_R(x)phi_x. PROOF.md shows that M_R is a Gaussian boundary
martingale with independent increments and Brownian covariance
Cov(M_R,M_S)=a_min(R,S). For actual one-arm events A_R(h),

    -d/dh log p_R(h) = E[M_R | A_R(h)],
    d/dh E[M_R | A_R(h)] = a_R-Var(M_R | A_R(h)) <= a_R.

Thus the earlier uniform near-critical score target reduces to an
endpoint bound. If the as yet unproved quantity

    M=limsup_R E[M_R | A_R(h_*)]/sqrt(a_R)

is finite, then

    liminf_(t->0) t^2 L_rel(t)
      >= (sqrt(M^2+2 log 2)-M)^2/kappa > 0.

Section 4 gives an exact residual-path-threshold formula for this M.
This is a conditional reduction, not a proof that M is finite.

The unconditional sharpness theorem uses artificial events D_R on the
same lattice field. They are increasing in field coordinates, nested
as R grows, and satisfy P(D_R)>=R^(-2-epsilon) eventually for every
epsilon>0, yet their translated relative radius obeys

    liminf_(t->0) t^2 log(1/t) L_D(t)=(log 2)^2/(8 kappa),
    liminf_(t->0) t^2 L_D(t)=0.

These are not connection events. The theorem strengthens the earlier
half-space obstruction: nesting, monotonicity, the exact boundary
martingale and the available polynomial probability bound still allow
the logarithmic loss and attain the old coefficient. An improved arm
bound must use additional information about paths.

AUDIT.md rederives the probability lower bound through independent
increments instead of association, and the half-ratio through a
Gaussian bridge instead of the full-vector likelihood. It checks all
intermediate radii and rederives each leading constant. The new result
is analytic. No numerical script or numerical workload was run; the
sparse radii are symbolic, not computed.

Commands: files were discovered with `OMP_NUM_THREADS=1 nice -n 15
rg --files <folders>` and read with the same prefix followed by
`cat <paths>`. Final read-only checks use `wc -l`, `head -n 1`, `rg -n`
and `date`, with command/output recorded in LOG.md. The sandbox denied
the priority adjustment; no numerical work followed. All authored files
are confined to this folder. No git, subagents, or earlier-folder edits
were used.

What failed or remains uncertain: no endpoint score bound for actual
arms was obtained, and no conventional correlation length was compared
with L_rel. No lattice critical exponent, existence of one, critical
nonpercolation, or agreement with cable exponents is proved. Novelty of
the elementary identities or the sparse construction is not established.

Next worker: try to bound the ratio in PROOF.md (18) at h_* using the
geometry of the residual bottleneck T_R, or derive another genuinely
connection-specific estimate of E[M_R|A_R(h_*)]. It is enough to work
at the endpoint: (15) supplies the nearby-level upper bound. A universal
logarithm-free bound using only nestedness, coordinate monotonicity and
polynomial critical probability is ruled out by section 6. Further
capacity constants cannot alter that obstruction.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, first retained local clock reading 10:48:09 +0400
(Asia/Tbilisi).
