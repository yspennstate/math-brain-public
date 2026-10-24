# P0162 referee-integrator attempt, 2026-10-10

## Exact target and status

The FEI conjecture asks for one dimension-independent C with H_2(fhat^2)<=C I(f) for all Boolean f on every uniform cube. The author-hosted O'Donnell–Wright–Zhou paper states the exact quantifiers and definitions. The 2026 González–MacManus–Pereyra and Potapov papers checked here give selected classes, not a universal proof. Owner memory `fei_opus_wave1_reduction_small_influences_gates_and_ltf_2026_09_23` says the full target was open on 23 September; `fei_plateaued_constant_four_is_potapovs_theorem_not_ours_2026_09_30` assigns plateaued constant four to Potapov. Current October global openness is UNKNOWN from this bounded search, and no novelty is claimed.

## Proved reduction and the single missing input

For any coordinate i, Delta_i(f)=H(f)-[H(f_i^+)+H(f_i^-)]/2 and I(f)=Inf_i(f)+[I(f_i^+)+I(f_i^-)]/2. If one universal K guaranteed **at least one** positive-influence i with Delta_i(f)<=K Inf_i(f) for every nonconstant Boolean f, induction would give FEI with C=K. This is a conditional reduction, already identified by González–MacManus–Pereyra. Its premise is the single hardest missing lemma in this route. It must hold again for every restriction reached by induction.

## Attempt and obstruction

I independently rederived the exact Fourier-pair entropy identity in w504 C001 and w505 C002. With q=Inf_i(f), Jensen and J(t)<=t^2 give Delta_i(f)<=h_2(q)+4q(1-q). This is rigorous but leaves a logarithmic Delta_i/q loss as q tends to zero. The owner F4 work had a sharper high-influence estimate and already reduces the general question to small influences. Selecting a largest-influence coordinate does not close that regime; the owner's prior work reports a counterexample to that selector rule.

The natural stronger lemma requiring Delta_i<=C Inf_i for **every** coordinate is false. w505's bent-point selector family has one selector coordinate with Delta_y/Inf_y>=log_2((2^m-1)^2+1), diverging with m. I independently checked the exact Walsh algebra and ran `python -X utf8 test_selector.py`, obtaining ratios 4.867668747, 8.030013847, 10.255970235 for m=1,2,3. w504's complementary calculation shows every base coordinate of the same family has Delta_j<4 Inf_j; I rederived its spectra and Jensen sign and ran `python -X utf8 test_w504.py` at m=2,4,6,8. These calculations are consistent with the existential coordinate input, but they do not prove it for arbitrary Boolean f.

The canonical prior attempt card `claim_06b0c09db7e28efc6febd3962e234332a00c2ba45a17792cc4d83fdbc6752fba` already shows why an arbitrary subset-law argument cannot finish FEI: uniform mass on the n singleton subsets has H=log_2 n and mean size one, but would give a linear Boolean function with at least two nonzero linear coefficients, and its square has a nonzero cross coefficient, contradicting f²=1. This source was read from the store in read-only mode. It confirms that any remaining route must use the Boolean convolution identities, not entropy subadditivity alone.

No theorem, formal-check receipt, or finite computation here establishes the universal FEI inequality. A meaningful next proof step is to attack the small-influence regime with a Boolean spectral convolution constraint that forces some coordinate's ratio Delta_i/Inf_i to stay bounded, or construct a family where the minimum over relevant i diverges. A bound on one preselected coordinate is already refuted.

w504's later C006 makes the remaining regime precise. The exact defect identity gives `0<=Delta_i<=2`; if any influence is at least `1/16`, that coordinate has ratio at most 32. Thus the unresolved suitable-coordinate claim can be confined to Boolean functions with every influence below `1/16`. I independently checked this conditional reduction. It does not establish the required K_0 on that class, and owner F4 already had a sharper related localization.

NEXT: Test any proposed structural coordinate-selection lemma against the bent selector and the owner F4 maximal-influence counterexample before trying induction.
