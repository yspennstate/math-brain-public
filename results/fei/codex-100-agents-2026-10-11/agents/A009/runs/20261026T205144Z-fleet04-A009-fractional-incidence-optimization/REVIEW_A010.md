# Independent reconstruction of A010's complete two-core bundle

Verdict: HOLDS, unchanged at its explicitly fixed-law scope. Source claim A010-INTERSECTING-CORES-VARIATIONAL-OBSTRUCTION-AND-JOINT-REPAIR@1, statement SHA256 8f66c6f6cf4318b27d7507bb4916fa9e078d9a1017b5f9c0a48944c18ad16dab. Sources: TWO_CORES.md and JOINT_CORE_REPAIR.md in A010's 20261023T131928Z run. This reconstruction supplies no repair to that version and imports no A010 code. RETUNED.md is a separate extension outside its fixed-law hypotheses.

## Physical identities

Expand private indicators A_X,A_Y, each of mean a=(3/4)^r. In zero/one notation the actual Boolean event is z1 OR [(z0 OR A_X)(z2 OR A_Y)]. With s=(1+a)/2, conditioning on z1 shows its influence is 1-s^2. In either independent side the outer bit contributes 1-a and the private coordinates total (2r/3)a. The gate from the other side and z1 averages to s/2. Thus total I=1-s^2+s[1-a+(2r/3)a], equal to A010's formula. The coefficient on {z0,z2} is the product of the two outer coefficient magnitudes (1-a)/2, the middle-zero probability 1/2, and sign-conversion factor 2, giving magnitude (1-a)^2/4. Physical private-sector mass is the conditional-variance calculation in RETUNED.md. No shared coordinate is cloned.

At r>=4, ra<=81/64 and a<=81/256<1/3. Expanding I-5/4 as a(r/3-1/2)+a^2(r/3-3/4) makes positivity immediate. Dropping negative terms bounds I<5/4+(81/64)(4/9)=29/16<2. Target mass exceeds 1/81 since 1-a>2/3.

## Full mass and variational lower bound

Compute the output E={z0,z2} by multiplying generating polynomials for each group. In one group a compatible local draw is empty (p=15/16) or its outer singleton (c=1/240); set b=p+c=113/120. Nonempty union mass is b^r-p^r; total occupation in that group is r c b^(r-1). Product differentiation for BOTH groups gives occupation mass 2r c b^(r-1)(b^r-p^r). Dividing by actual anchor normalizer rho=r/8 gives exactly Q(E)=(1/15)b^(r-1)(b^r-p^r). This counts every compatible allocation and its actual anchors. Independently, code/check.py builds the full physical union-occupation arrays without this target formula and checks equality.

The integer inequality 2*113^16<120^16 gives -log2 Q(E)>(2r-1)/16. Any distribution on subsets of individual K1 or K2 gives E zero mass. Therefore every allowed mixture R satisfies R(E)<=Q(E), including optimal posteriors, so C_R/I>(2r-1)/2592. Strictness under infimum follows from the same stronger exact bound P(E) log(1/Q(E))/I for every R; it is strictly larger than the stated bound. Alpha=0 gives infinite cost; this endpoint does not invalidate the argument. This lower bound does not allow retuning Q.

## Entropy part of the bundle

For any private indicator W of mean q, normalized squared indicator spectrum nu_W, and one independent core bit z, expand 2(z OR W)-1 into its two z sectors. Their coefficients are q and 1-q on the two empty-private slots and opposite copies of each nonempty private coefficient. Combining their logarithms gives exactly H=2q H(nu_W)+2(1-q)h2(q). The normalized spectrum of A_X is a product of r four-point laws (3/4,1/12,1/12,1/12), hence entropy<2r. Thus H(2(z0 OR A_X)-1)<4ra+2. For S=z0 OR A_X, its normalized indicator spectrum has empty probability s; converting its nonempty mass to the sign spectrum gives H(nu_S)=h2(s)+[H(2S-1)-h2(4s(1-s))]/(4s). Here s>=1/2 so the denominator is positive. The two sides are independent. Applying the first identity again at z1 yields H(f)<=6+H(2S-1)<8+4ra<=209/16. Divide by I>5/4 to get H/I<209/20<11. All sums are finite; no limit interchange is used.

## Joint upper bound

Any physical set has a compatible tuple with at least one active entry and all local probabilities >=1/240, so Q(A)>=(1/240)^(2r)/(r/8). The fixed mixture with uniform mass 1/7 on each nonempty three-core set gives pure-core cost<4, private cost<17r. The latter follows from log240<8, log r<=r and r>=4; retaining its negative -2 constant only improves the bound. The true private mass is M=a(1-a)+(a^2/2)(1-a^2)<7a/6. Consequently C<4+(119/6)ra<=3725/128, and dividing by I>5/4 gives C/I<3725/160<24. This uses mass LOWER bounds for an upper cost, whereas the obstruction uses the full mass UPPER bound. The code verifies full normalization and costs for r=1,2; the all-r conclusion is the analytic argument just reconstructed.

## Checks that could fail

Shared-coordinate pivotal gates, coefficient sign-conversion, target full-law rather than selected-event mass, anchor normalization, zero-prior endpoint, strict infimum, and the entropy-to-indicator conversion were checked separately above. Integer Walsh versus physical flips, full output DP versus target generating function, and exact private-sector Parseval versus core conditioning provide finite cross-checks. Constants are verified by rational arithmetic and certified logarithmic intervals. The hypotheses of disjoint private pairs and fixed width-four local law are used explicitly. Growing widths and arbitrary retuning are excluded from the source obstruction. Full FEI and arbitrary-core influence payment remain open. This is an independent mathematical proof reconstruction, not Lean acceptance or shared-registry adoption.
