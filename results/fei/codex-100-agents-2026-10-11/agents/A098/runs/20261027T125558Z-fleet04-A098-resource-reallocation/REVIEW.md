# A098 stage22: full query fees, affine calibration and the interface boundary

Units are bits. Full FEI is open. This reviews the exact two A097 stage22 claims and the newly completed A093 forward-fee guard, not the entire A012 bundled claim or the A011 v5 statement.

## Exact source versions

A097 run20261027T092641Z-fleet04-A097-cross-route-transfer, PROOF sections1--3:

- A097-AFFINE-PROJECTION-HISTORY-TRANSFER@1, statement hash bc46cd1b3062fcf914edfcc89275c6e7391645eecd0edb7194defb5ea8e05035.
- A097-HIGH-MOMENT-MATCHED-QUERY-LOSS@1, statement hash f3b5c69ef59c7d95ba81cee06034cdf49115a0a5036e75101f19a6ba1bd7064d.

The dependency reconstruction uses A012 run20261027T062634Z DERIVATION sections2--4, specifically its projection convention, scalar bound and ledger. Its activation source reduction is not independently reviewed here. A011 run20261027T025625Z v6 and A094 run20261026T232939Z locate the distinct true-kernel/old-v5 accounting boundary; their numerical reserves are not accepted anew.

## Affine information projection: support and boundary conditions

Let q be a finite normalized reference covering p. Restrict to supp(q); any feasible finite-divergence law vanishes outside it. A nonempty closed affine slice of the simplex containing p is compact. The function sum v log(v/q) is continuous with 0log0=0, and strictly convex on this simplex, giving a unique minimizer u.

Every atom positive in any feasible law must be positive under u. Otherwise mix u toward that feasible law: newly positive atoms contribute a strictly negative multiple of t log(1/t), while changes at previously positive atoms are O(t). Finitely many atoms justify the comparison. In particular supp(p) is contained in supp(u). On supp(u), u+t(p-u) is nonnegative for sufficiently small t of either sign; outside it both laws vanish. Both signs also retain the affine equalities. Therefore first variation at zero gives

    sum (p-u) log2(u/q)=0.

The normalization derivative cancels, hence

    D(p||q)-D(p||u)=D(u||q).

This is an equality, including boundary feasible moments; there is no unsupported full-support assumption on u. A scalar subprobability mass s>0 is unchanged, so replacing sq by su retains the entire -log2(s) CE penalty and the same divergence difference. If the fee is the FULL normalized D(u||q), its bracket D_after-D_before+fee is exactly zero. No negative release is credited twice.

## Physical queries and the exact original-source ledger

For parent spectral law P and physical query i, let R=pi_i P and V=pi_i Q. Literal restriction coefficients imply R=(P_0+P_1)/2. Both child true laws are covered by V. Define

    L=D(P||Q)-D(R||V),
    J=[D(P_0||R)+D(P_1||R)]/2.

Fiber disintegration gives L>=0. The finite mixture identity gives

    average D(P_t||V)-D(P||Q)=J-L.

The CE difference is separately

    average CE(P_t,V)-CE(P,Q)=-B_i-L,
    B_i=H(P)-H(R).

Thus a generic claim that the CE difference is merely -L drops B_i. This corrects a proof-text shorthand; it does not change A098 stage21's direct signed-terminal subtraction.

For completeness, in natural units set e(a,b)=[a^2 ln(2a^2/(a^2+b^2))+b^2 ln(2b^2/(a^2+b^2))]/2. Replacing a,b by their absolute values leaves e unchanged and weakly decreases (a-b)^2. Write the nonnegative amplitudes as m(1+t),m(1-t). The second derivative of j(t)=e(1+t,1-t) is 2ln((1-t^2)/(1+t^2))+4/(1+t^2)<=4 on(-1,1). Since j(0)=j'(0)=0 and j is even, twice integrating gives j<=2t^2. Homogeneity and endpoint continuity give e(a,b)<=(a-b)^2/2, including zero amplitudes. Summing over frequency rows gives J<=(2/ln2)Inf_i.

At every node, all affine update brackets vanish. A012's optional partial-profile update brackets are nonpositive: for r=(1-t)q+t p and unchanged within-cell conditionals, their released remainder is ((1-t)/t)[D(r||q)+D(q||r)] for 0<t<1, with endpoints handled directly. These are fees for specified updates, not arbitrary resets.

Multiply each local identity by the actual physical reach and sum the finite tree. Internal divergences cancel, giving the exact form

    E D_terminal + sum w L + sum w fee
      = D_root + sum w J - sum w update_slack.

Here update_slack is zero for affine projections and nonnegative for allowed partial profiles. The physical influence identity telescopes independently:

    sum w Inf_i = I_root-E I_terminal.

Consequently the additive cost can be bounded by (2/ln2)(I_root-E I_terminal), and hence by (2/ln2)I_root as in the source statement. Adding SIGNED entropy increments and complete terminal CE leaves H_root plus the displayed KL account. A fixed old booking U remains added on both sides. All branches, nonconstant optional-stop terminals, reference-only atoms and scalar mass penalties are retained. The original source is never renewed. This proves A097's registered transfer statement without mathematical repair.

Neither positive-part clipping of entropy increments nor a mandatory new floor is included. Finite adaptivity permits history-dependent constraints; feasibility must hold at each update. There is no infinite stopping-time or dimension-limit interchange in this theorem.

## High-order moments do not pay a local query

For every even n>=4 let f be a product of n/2 disjoint two-bit signs negative at(++). Each factor has four squared Walsh coefficients1/4, so the genuine Boolean spectrum P is uniform on all2^n sets, H=n, I=n/2 and every coordinate influence is1/2.

On the face of sets containing n, perturb the uniform reference by alternating parity of the first n-1 coordinates. With epsilon=2^(-4n), half the face atoms have Q=2^-n epsilon, half have Q=2^-n(2-epsilon); outside the face Q=P. This law is positive and normalized, and its vacuum matches P.

Every inclusion moment involving at most n-2 coordinates leaves an unconditioned parity coordinate, unless it forces the face to be absent (then the perturbation is zero). Summing that coordinate cancels the perturbation. Inclusion-exclusion therefore proves equality of every full marginal on up to n-2 coordinates. For every i<n the entire erased reference equals the erased P, so

    L_i=D(P||Q)=n-(1/4)log2(2-epsilon).

Since1<2-epsilon<2, n-1/4<L_i<n, and CE=n+L_i<2n=4I. Dividing by Inf_i=1/2 yields the claimed divergent local ratio. Q itself is already feasible for every calibration using only these matched moments; its information-projection release is zero by strict positivity of divergence. The initial mismatch D_root pays the first projection loss in the valid full ledger; it cannot also be reused as spare money. H/I=2, so there is no FEI counterexample. This proves the second registered source statement unchanged.

## Interface counterexample and correction propagation

An actual AND2 sign has uniform root spectrum. At a physical query, the projected reference from Q=P is(1/2,1/2). One actual child is constant; true-kernel inheritance from the matched root gives(1,0). The projected law has positive singleton mass where the true-kernel law vanishes, so D(projected||true-kernel)=infinity. No numerical approximation is involved. A projection-history theorem cannot silently replace a prescribed true-kernel interface.

A094's old-v5 query-loss objection is not a refutation of A011v6's inherited-policy payment. A097/A012 instead pay a different explicitly defined projection interface with full contractions. Keep the old-v5 objection open only for a proposed locally rebuilt/fresh-floor interpretation that still omits that loss. Stop asking the repaired inherited policy to repair an equation it no longer uses.

## Rung and exact unpaid line

Rung: independent analytic reconstruction with exact finite checks. Both A097 statements hold unchanged. The A012 dependency is accepted only for DERIVATION2--4; no blanket acceptance of its bundled activation reduction or unrelated original-source claims. No Lean proof is claimed: current disk-critical compute state rules out launching a compiler here.

The remaining universal step is a noncircular Booleanity-based initial payment or a well-founded selected descent retaining every genuine child reserve, together with a useful compatible terminal policy. Merely prescribing CE(P,Q)<=C I for every Boolean function is already FEI-equivalent by CE>=H and Q=P, so that formulation is not progress by itself. Further moment matching, inherited history enumeration, or an uncharged interface swap cannot supply the missing payment.

## Exact forward-fee guard (A093's completed source)

The infinite reverse divergence does not imply an infinite forward conversion fee. On the AND2 constant child, the forward fee D(true-kernel||projected) is exactly1 bit. Its update bracket is zero, because that target equals the true child spectrum. The earlier reverse-infinity observation remains valid in its own direction.

For actual AND3 with a uniform root reference, the projected child reference V is uniform on four atoms. One physical child is constant; the other has true spectrum p=(1/4,1/4,1/4,1/4). The true-kernel reference on this latter child is u=(1/16,5/16,5/16,5/16), from the actual kernel and reference outcome normalizer. The paid-update bracket for a FORWARD fee is

    D(p||u)-D(p||V)+D(u||V)
       = sum (u-p)log2(u/V) = (3/16)log2(5)>0.

The constant-child bracket is zero. Averaging BOTH actual outcomes gives(3/32)log2(5)>0. Independently, exponentiating16 times the nonconstant bracket gives the exact integer125. The completed A093 run20261027T124307Z DERIVATION sections1--3 and CLAIMS were subsequently read in full and byte-pinned in out/NEW_A093_SOURCE_RECEIPTS.json. This independently certifies A093-FORWARD-TRUE-KERNEL-HANDOFF-DEFICIT@1 unchanged (statement hash291b4429e2ae930044be8521ea95b4699c21ec26f27b41924b91f7cc884de33b), rather than treating a board summary as a proof. Input translations and output complementation change Fourier signs without changing the squared laws; they can swap the two actual children. Coordinate permutations preserve the symmetric AND3 law and uniform reference. Thus the full16-table/3-coordinate source scope follows analytically from the explicit fixture; our helper does not claim a48-query exhaustive replay. No novelty is asserted. The two-fixed-fixture helper records23 assertions separately from the main census.

Thus a general true-kernel replacement is not automatically a paid affine projection. A required replacement must add its ACTUAL positive update bracket to the same original account. This finite guard does not refute A097's explicitly affine operation class, show an original reserve insolvent, or refute FEI.
