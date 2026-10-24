# P0297 independent route (w519)

2026-10-10, preregistered before reading any peer proposed proof.

Target title supplied: Exact Hausdorff dimension of Liouville quantum gravity. Complete mathematical target and current status pending primary-source recovery.

Route: separate the deterministic LFPP normalization exponent from local heat-kernel/time-change exponents. Seek a genuinely metric observable (annulus crossing ratios or metric-ball volume growth) whose exact scaling determines d_gamma. Check whether any claimed spectral-dimension-to-Hausdorff-dimension inference needs a walk dimension that is itself unknown. Use normalization invariance as the first audit obstruction; do not infer metric exponents from GMC mass exponents alone.

First result W519-L1 (elementary normalization lemma): If positive a(epsilon) satisfies log a(epsilon)/log epsilon -> alpha and b(epsilon)=a(epsilon)L(epsilon), with log L(epsilon)/log epsilon -> 0, then log b(epsilon)/log epsilon -> alpha. Hence multiplying crossing normalizations by subpower factors cannot identify the missing exponent. Proof: log b/log epsilon = log a/log epsilon + log L/log epsilon. This is an elementary lemma, not a solution of P0297.

Hardest remaining gap (provisional): derive the exact LFPP crossing exponent or an equivalent metric walk/ball-volume exponent from a proved geometric estimate. No such estimate has been proved here.

## Exact target and prior-attempt digest (completed after route preregistration)

The precise target is in STATEMENT.md. Primary sources are Gwynne--Miller arXiv:1905.00383v3, Problem 7.1, and the original ledger's Rhodes--Vargas survey, arXiv:2509.21053v1 Section 3, also published 13 July 2026 at https://epubs.siam.org/doi/10.1137/25M1803632. The 2026 publication still lists the general metric dimension as open. A bounded local check is not an exhaustive owner solved/retired or novelty certification.

The stored September attempt, brain_bundle_C006a05.json at-p0297, used constant field shifts to recover the necessary identity xi*d_gamma=gamma, while explicitly leaving xi unknown. The D intake duplicates this target as D0049. Its D0049-A001 attempt discusses first-passage normalization but mistakenly writes d_gamma=2Q/xi twice; CORRECTIONS.md and patches/01_intake_D_lqg_dimension_identity.diff propose the precise correction. D0052's numerical elimination of affine interpolation and small-gamma Watabiki discussion are prior work; this packet does not repeat those computations. Targeted P0297/Liouville/Watabiki searches found no matching H/I proof attempt or Lean proof, and Team O's board had no P0297 row. These absences are scoped search results, not exhaustive claims about all owner work.

Our route is the killed-disk Green potential, rather than constant-shift volume matching or the peers' covering/thick-point calculations. The peer snowflake example is retained as a sanity control here; a duplicate snowflake brain card is deliberately omitted from our bundle.

## Substantive attempt

For a fixed sample of a positive Radon measure mu, the centered Brownian disk Green potential is

T_x(r)=(1/pi) integral_{B_E(x,r)} log(r/|x-y|) mu(dy).

W519-L2 proves that a positive local mass exponent a gives the same exponent for T_x. Its proof is an exact Tonelli identity plus two deterministic power bounds, so it neither assumes independence across scales nor multiplies conditional probabilities. W519-L5 imports the exact-dimensionality theorem for subcritical disk GMC under its actual hypotheses, giving a=2-gamma^2/2 for GMC-almost every interior x. Multiplication by a locally positive continuous weight preserves the conclusion without independence from the field. The constant 1/pi corresponds to Brownian generator (1/2)Delta; GFF covariance normalization is separately fixed to log singularity. These two normalizations must not be confused.

If a valid Brownian PCAF/Revuz occupation identity identifies T_x with the quenched mean exit clock, the Euclidean mean-clock exponent is therefore explicit. This is a statement about a quenched expectation, not concentration of the realized clock and not exit from a metric ball. The occupation framework is recorded in Garban--Rhodes--Vargas arXiv:1301.2876, Sections 2.1 and 2.3--2.4; the deterministic potential and GMC statements do not require importing a diffusion theorem for an unmatched field model.

Try to convert to a metric radius delta(r). Under a separately proved local metric scaling delta(r)=r^(xi*(Q-alpha)+o(1)) and mass exponent gamma*(Q-alpha)>0, W519-L4 gives log T_x(r)/log delta(r) -> gamma/xi. At a gamma-thick quantum-typical point, the putative exponents are a=gamma*(Q-gamma)=2-gamma^2/2 and b=xi*(Q-gamma). Their ratio is gamma/xi=d_gamma. This cancellation returns the unknown; it does not solve an equation for it. The actual random-point metric scale limit is an input here, not a lemma proved by this packet.

The spectral shortcut also fails at the level of the displayed exponents: W519-L3 supplies metrics on R^2 with the same standard Brownian diagonal spectral dimension 2 and six different metric dimensions in the scalar controls. These auxiliary snowflakes are not length metrics when theta<1, so they do not refute the strong-LQG axioms. The entire embedded field or full measure law contains more information than these exponents alone. No universal spectral-to-Hausdorff conversion is imported without a proved metric walk law.

## Exact stopping point and saved results

W519-L1 through L5 have full elementary or source-backed derivations in their named files. W519-L1 has a KEEP receipt independently rederived by w521; L2--L5 and source correction C2 are submitted for review, not independently certified by this author. The scalar checks and draft preflight are not formal proof receipts. No formal checker was invoked and no axioms/admitted placeholders are presented as a proof.

G1 is the hardest remaining gap: evaluate a genuine metric-scale exponent b_gamma, under a specified typical-point law, without assuming its expression through the unknown xi. The possible next proof step is a noncircular bound on actual D_h distances to shrinking Euclidean circles, using metric geometry rather than GMC mass scaling alone. No explicit value has been obtained. Current mathematical outcome: proved scope-limited lemmas and a corrected intake identity; no proof of P0297 and no novelty claim.
