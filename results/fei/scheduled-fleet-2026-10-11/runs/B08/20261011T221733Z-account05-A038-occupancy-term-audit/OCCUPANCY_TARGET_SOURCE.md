# A038 occupancy target: source and correction chain

All entropies and KL divergences are in bits; D_2 means base-two KL, not order-two Renyi divergence.

The current Brain checkpoint was fetched at fc8276da09123d9f7ede195ad8ac27ed5768306f and then from the default branch. Both returned blob 1c31b4afdb0b9c89296bce65580145c3d7df59f8. Original mathematical definition: account02/B15, 20260922T0829Z-influence-iprojection-kl/REPORT.md, Theorem 2.1 and Section 4, retrieved at 2bf247373576eb406ca91bb3ea5f3ce5e5ab8588, blob 5ce14eaaec34f0d91f2d430dba576e19dddc6894. Full local copies are in out/sources.

For a nonconstant Boolean gate at an interior product bias, let v=Var(f), P+(S)=fhat_p(S)^2/v for nonempty S, and r_i=I_i^p/v. Here I_i^p is spectral influence in the biased orthonormal basis. Put mu=sum r_i>=1. For mu=1 the law is uniquely supported on singletons. For mu>1, c in (0,1] uniquely solves 1-c=prod_i(1-c r_i). Q_r is independent Bernoulli(c r_i) conditioned on nonempty. Deterministic coordinate boundaries are interpreted on the forced support.

Hmax(r)=[sum h_2(c r_i)-h_2(c)]/c,
K_occ=D_2(P+||Q_r)=Hmax(r)-H(P+).

For an arbitrary symmetric potential Gamma and V_u=4u(1-u), put
a_i=[Gamma(p_i)+h_2(V_p_i)]/V_p_i,
a_q=[Gamma(q)+h_2(v)]/v.
The exact residual is R_Gamma=sum r_i a_i-a_q-H(P+)=B_inf^Gamma+K_occ. Its canonical unpaid debt is
[Hmax(r)+a_q-sum r_i a_i]_+.
The balanced uniform slice has v=1 and debt [Hmax(r)-C(I-1)]_+, C=Gamma(1/2), which is full-FEI strength. No full candidate-potential bytes were reconstructed or certified here; this audit does not refute a surviving shaped Gamma.

The archived fixed positive reserve D_Gamma>=lambda v K_occ for fixed lambda>0 is already false for every finite potential center. Source: account01/B01 at 63a1d889005602ab5ed5f15497243c70186689a1, REPORT.md Sections 3-7, blob 748dbfcb20b3dc236200d5351b74bf3edb2f4158. Correction event blob c26eac20a54275195fdc868bd8f566d16eb14a4a is archived too. Its actual balanced antipodal two-flip dictator has delta=2^(2-n), I-1=(n-2)delta, H<=7(I-1), K_occ>=(n-8)(I-1), so D_Gamma-lambda K_occ<0 when n>8+C/lambda. This prior result is source-imported, not counted as new progress. The exact signed recursion survives. Our proposed cross-law substitution is a different, explicitly frozen inequality and is refuted below; it does not revive the reserve.

A036 uses K_full=D_2(P_all||prod Bern(d_i)), d_i=v r_i, not K_occ. Its collision statistic uses amplitudes b_S=sign(fhat(S))*sqrt(Q_d(S)), actual signs and unconditioned Q_d. No completion is needed for our full-support point-defect family. A036 explicitly did not identify its K with occupancy credit; we attribute no false statement to A036.

Frozen changed target: K_occ>=T/4-kappa I (or v K_occ in its place), with A036's unconditioned collision T and one fixed finite kappa. Exact named debt: [T/4-kappa I]_+. This cross-law target has a new obstruction ID and is not the canonical all-gate debt. The correction Delta below must remain separate, with the root normalization and coordinate marginals retained.

