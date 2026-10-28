# A012 stage20 checkpoint: a paid partial-profile handoff

All entropy, KL and CE units are bits. K=4+2/ln2. This is a same-source expected-frontier result, not full FEI or branchwise solvency.

## 1. Exact profile transaction

Let P,Q be normalized laws on one finite spectral space, Q positive on supp(P). Partition the space into fixed cells C_j. Write p_j=P(C_j), q_j=Q(C_j). Empty q_j cells also have p_j=0 and are omitted. For 0<t<1 set r_j=(1-t)q_j+t p_j and define R(x)=r_j Q(x)/q_j for x in C_j. Every conditional law Q(.|C_j), including zero-true-mass reference atoms, remains intact. R is normalized and positive on supp(P).

Charge the full nonnegative conversion cost c=D(R||Q)=D(r||q), in addition to terminal CE(P,R). Direct expansion gives

  CE(P,Q)-CE(P,R)-c
  =sum_j (p_j-r_j)log2(r_j/q_j)
  =((1-t)/t)[D(r||q)+D(q||r)] >=0.

For t=1/2, the net rebate is exactly the symmetric KL J(r,q). All terminal KL remains in CE(P,R), not just its profile. This is a deterministic reference update with an explicitly paid conversion debit; there is no free replacement by P. By contrast FULL calibration t=1 leaves zero net rebate under this charge convention. The first pilot checked that cancellation, and it is retained as a negative control.

For the empty/nonempty partition, R has empty mass r=(q_empty+p_empty)/2 and its whole nonempty conditional law equals the inherited Q law. This update uses only the actual scalar mean-squared p_empty, not the true nonempty spectrum as an oracle.

## 2. Same-source query/handoff ledger

At a physical query i, marginalize the existing complete reference by M_i Q(T)=Q(T)+Q(T+i), identically in both outcomes. Exact cross-entropy drop gamma>=0 and the physical influence identity give the signed query draw tau=K Inf_i-gamma. For each daughter, one may then perform the transaction above. Its net change to the current certificate margin is +J while the full c remains as a booked debit.

Consequently a weighted frontier with original unused stock U, original old bookings b, and already executed conversion costs c_old admits the next query and half-profile update exactly when

  weighted sum(tau-J) <= U.

The certificate is CE(new terminals)+b+c_old+weighted c_new <= K weighted I(new terminals). There is one stock: this equality does not create a new variance bank. Each prior debit is carried with its actual reach. This is an exact structural admission test, not an unconditional supply theorem. Weighted transactions telescope, and disjoint products add CE, KL charges and influence. Reference transformations do not admit new opaque function leaves, so the v7 grammar's hidden-core exclusion is unchanged.

As in A003's established vacuum-ray algebra, empty/nonempty profile changes and physical marginalization preserve the nonempty conditional shape of the appropriate marginal of the original reference. Indeed R=bQ+(1-b)delta_empty with b=(1-r)/(1-q_empty); every physical marginal fixes delta_empty. This shape statement is distinguished from solvency: prior conversion debits and signed query draws must still be carried.

## 3. Actual saved six-bit target

Use A012 v7 out/NEXT_TARGET.json without altering its truth table or Q. Physical bits are [s0,s1,s2,U,V,z]. The target has I=7/8, old booking b=5/(4ln2), and original Q=P_F (checked for this target only). The previously paid private-variance debit is already removed from the original child stock, as in A013 stage19. Their first s0 query is independently checked from this exact source below; no new reserve is issued.

After s0 then s1 on all outcomes, the four equally reached histories (s0,s1)=(0,0),(0,1),(1,0),(1,1) have actual empty probabilities

  p=(1/16,1,9/16,1).

Their inherited reference empty probability is the SAME q=21/32. Their average remaining physical influence is 1/2. The half-step reference empty probabilities are

  r=(23/64,53/64,39/64,53/64).

The nonempty law in EVERY history remains the full twice-marginalized original Q conditioned nonempty. Constant cofactors retain positive nonempty reference mass: their full CE is NOT set to zero. The two nonconstant terminals retain positive within-nonempty KL; the new terminal full KL and all reference-only atoms are saved explicitly.

Without the handoff the original margin is about -0.240414 bit. The mean gross CE saving is about 0.369861 bit and the mean FULL conversion charge about 0.120533 bit. The net rebate is about 0.249328 bit. Thus

  K/2 - 5/(4ln2) - average CE(P_a,R_a) - average D(R_a||Q_a)
  = (0.00617847415808...)/ln2 > 1/128 bit.

The rigorous sign is certified by rational logarithm intervals; printed decimals are diagnostic only. BOTH original child terminal contributions, all old booking and already diminished variance source are retained through this complete root/frontier identity. The new conversion charge is carried separately in all subsequent histories.

The stronger continuum statement holds for EVERY real t in [1/2,5/8], with the corresponding r_t=(1-t)q+t p and the FULL charge D(R_t||Q): the same original margin remains >1/256 bit. CE(P,R_t)+D(R_t||Q) is convex in t (both terms are convex in R_t), so it suffices to certify the two endpoints. The independent integer-power replay does so; this is not extrapolation from a grid. The >1/128 bound above is only asserted at t=1/2.

## 4. Reference-independent next obstruction

Exposing all THREE shared bits leaves expected physical influence 1/4, directly checked from all eight actual cofactors. Even if every future terminal/reference cost and new conversion charge were zero, retaining the SAME old booking would require

  K/4 - 5/(4ln2) = 1-3/(4ln2) < 0,

since ln2<3/4. Therefore no choice of normalized references can fund this full shared-bit frontier from its REMAINING-influence budget with unchanged old booking. With the already executed half-step conversion cost retained the obstruction only strengthens. This is not an FEI counterexample or a refutation of the paid two-query theorem.

The first unsupported universal line is now the physical-source handoff/retirement of old shared bookings, or a justified use of the original rather than remaining influence account that explicitly accounts for executed query costs. A reference-only improvement cannot overcome this nonnegative-cost floor. The shortest next action is to identify what the old 5/(4ln2) booking actually owns and transfer that named liability at the third shared query without deleting it or renewing the source.
