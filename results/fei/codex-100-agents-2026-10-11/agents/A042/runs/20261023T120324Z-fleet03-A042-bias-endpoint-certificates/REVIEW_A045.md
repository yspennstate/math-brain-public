# Independent reconstruction: A045 multiselector complete seed transfer

Source: A045-MULTISELECTOR-COMPLETE-SEED-TRANSFER@1,
statement b0bc6ab9bc58cc039ef5489e96ea00076dc18f31a0fcf9a88b461d2f0c46f82f,
PROOF.md ae8d09f4aa98954bb38096c7b52e5ac851cd62f9cefbf16964bf5cacc10fbce3,
run 20261023T111726Z-fleet03-A045-biased-realizability-referee.
The original claim/author/hypotheses are preserved in CLAIMS.json with a
separate review record. No substantive repair is supplied.

## Fresh proof from the selector placement law

Let e=product_j e_j, e_j=2^-k_j, A_sel=product X_j. Put
nu(U)=product_(j in U)(1-e_j) product_(j notin U)e_j. This is a genuine
probability law. Direct half-differences of F=1+A_sel(g-1) give, for every
nonempty seed label T and selector label U,

c_F(U,T)=c_T 2^-|U| product_(j notin U)e_j,
P_F(U,T)=e nu(U)P_T.

For T empty and U nonempty, the same difference is
-a 2^(1-|U|)product_(j notin U)e_j and its square mass is
4a^2 e nu(U). All factors other than c_T or a are exact powers of two;
the index shifts in the source follow with zero carry. Their powers are
nonnegative on the labels where used, including all boundaries.

Write D=E_nu[|U|+sum_(j notin U)k_j], L=E_nu|U| and K=sum k_j.
The seed sector contributes e J_g+ln4 e V D. The pure selector sector
contributes ln4 4a^2 e[(j_a-1)(1-e)+D-eK]. Since V+4a^2=4a,
their sum is exactly the source formula(M). The full physical influence is
e I_g+4ae L, obtained either by the degree sum or by direct pivotal events.
Subtracting Var(F)=4ae(1-ae) gives the stated deficit split.

For each occupied seed label, W_F(U,T)=e nu(U)W_T; for pure selectors,
W_F(U,empty)=4b e nu(U). Hence Z_F=eZ_g+4be(1-e), and BOTH actual
and reference laws have the same placement law nu in the seed sector and
nu/(1-e) in the nonempty pure-selector sector. On the latter sector the
remaining likelihood ratio is s/t. On the former it is
[(1-s)/(1-t)] [P_T/V]/[W_T/Z_g]. The full empty ratio is one.
This proves K_F=eK_g+w d_Bern(s||t), without discarding either full law.

The genuine outer gate uses an actual independent seed-output wire. Its
influence on that wire divided by V equals e. Composing the two COMPLETE
references therefore gives K_tree=K_outer+eK_g by the same pointwise
sampling factorization. Replacing Z_g by V in the outer normalizer yields
the exact signed conversion in the source. Since Z_outer>=w and Z_g>=V,
ln x<=x-1 proves its positive first term <=e(Z_g-V); it is charged once.

Iterating the one-selector sharp3ln4 bound with its actual edge weights
proves the sharp outer J bound and conditional finite-depth corollary.
Only the outer gate is funded: no arbitrary seed J estimate appears.
At fixed selector product the displayed Z_F and K_F depend only on that
product. This invariance is for the ALL-NONEMPTY-rounded flat reference;
it is not an assertion about the new singleton-preserving Q_* or an
arbitrarily chosen sequential reference. Distinct physical wires are
essential. Constant/deterministic cases contract before conditional laws
are formed; multiple selectors with negative constant seed form an AND
sign rather than a literal. These admissions are part of acceptance.

## Validation and scope

REVIEW_SPEC.json freezes192 actual roots and a16-case pilot. Our separable
mean/half-difference transform is independent of the source's Mobius/moment
implementation. code/review.py checks every physical coefficient shift,
full spectrum, scale/deficit formula, sharp outer payment and both complete
references. It verifies ordinary KL by exact prime-log expressions and
the sector factorization pointwise. Source code was neither copied nor run.
Outputs and counts are in out/REVIEW_CHECKS.json and out/REVIEW_PILOT.json.
Acceptance is at the stated exact transfer/conditional scope, contingent
on those executed outputs passing. It does not accept a universal seed
supplier or full FEI. The new paid-sector obstruction in PROOF.md is a
different charge/reference; it does not repair or refute this source.
