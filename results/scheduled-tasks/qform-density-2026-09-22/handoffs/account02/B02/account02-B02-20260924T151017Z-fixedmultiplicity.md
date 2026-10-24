# account02/B02 fixed-multiplicity handoff

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Fresh control was read from `math-research-brain` main, initially `d67a7ce285e76a86c9c905279f7362daed42d40f`; a later main refresh observed `620f0e982d796d74abe54f881cf0ee8b2a6c2c74` and its new nine-400 handoff was consumed. Prior B02 receiver memory at brain commit `b0c40c0b1e00ed23580d0ac0a88617420b54d74b` was also read and used.

## Baseline manuscript

Pinned baseline snapshot actually read: `math-open-problems@6241df6fc911c10cc7ee925dc4ca566f8c12cff0`, root `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/`. Manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 790 lines. README, delivery status, manifest, full manuscript, audit, proof map, verify script and checks were read. Full B02 audit verdict: mathematical PASS for the written 17-eigenvalue theorem; bibliography attribution only UNCHECKED. Product-projection zero-marginal line is valid after inserting the harmless inequality over surviving factors.

Immutable baseline audit commit: `53893b97edc60885b9c3f385a1a6da7e4d62415e`.

## New nine-400 source consumed and independently reviewed

Fresh concurrent source identified by the later brain handoff:

- candidate `QFORM-NINE-EIGENVALUES-400-20260924`;
- source commit `eeb752c8943536541b34b42b8bf48e924f4d3d2f`;
- `paper.tex` blob `19fb119877426b640b2c0dae19ec2f78a399fe11`;
- SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`;
- 955 lines / 60,749 bytes.

All 955 lines plus manifest, proof map and author self-audit were read. Independent review verdict: **mathematical PASS with one local presentation repair**. In the hyperbolic-pair negative-tail paragraph, the proof says to use the `w` vector but reuses the positive-tail coordinate symbol controlled by `u`. Repair by choosing separate original coordinates `i_+` and `i_-` maximizing `u` and `w` respectively. Since `|u|=|w|`, both cutoffs and every displayed constant remain unchanged. No fatal gap found.

The grouped mollified-L2 argument, physical-row promotion, `E3` density receiver, `E2` half-potential receiver, full pair half-potential `16D^{-1/4}`, retuned interpolation, final branch constants, and overlap theorem were independently reconstructed. The overlap theorem

`W^cross_(r,1)+(r+1)^2 V_(r+1) >= V_r sum_(j>3r) s_j(A)^2`

is valid for arbitrary real square `A`; its `s_8` corollary is supporting structure only, not an eight-eigenvalue density proof.

Immutable independent review commit: `1b284444c91119a0bcefdc082ec6ad4c86a8afb9`.

## New B02 constant retuning

Using the now-reviewed nine-direction proof, a new rational retuning gives

`||p_Q||_infinity < 361 K^2/s` under `s_9(A)>=s`.

Parameters:

`d=47/625`, `p=57/20000`, `h=sqrt(kappa)=411/5000`.

No-pivot off-diagonal bound uses `sqrt(p+d^2)<923/10000`. The interpolation diagonal-dominance margins are exactly `5037/10000` for `r=1` and `1/2500` for `r=2`. Sharper rational constants used are

`C3 < 232551/15680`, `C2<13`,
`pi<22/7`, `log2<347/500`, `log5<161/100`.

Normalized branch bounds:

- no pivot: `9689625/26852 = 360.8530... <361`;
- scalar pivot / no-pivot Schur: `<234`;
- scalar pivot / pair-pivot Schur: `<270`;
- scalar pivot / scalar-pivot Schur: `473915/1316 = 360.1177... <361`;
- definite pair: `<59`;
- indefinite pair: `1804/5=360.8<361`.

Immutable `<361` candidate commit: `baceb2437589748f5a439541cc81b93ee93811fd`. This new constant has only this one complete review and must remain candidate/not release-validated until a genuinely separate complete review passes it.

An earlier same-run `<536` immutable note at commit `c8497fa5040e32b1f170b9ebeb58f8ab2c7abec9` is preserved but numerically superseded first by the independently reviewed `400` source and then by the new `<361` candidate.

## B02 exact-law obstruction

For cap-one Gaussian `f(x)=exp(-pi x^2)`, `fhat(t)=exp(-t^2/(4*pi))` and exactly `int |fhat|^q = 2*pi/sqrt(q)`. Thus the scalar Fourier-power exponent is sharp; only constants can improve there. For independent cap-one `Unif[-1/2,1/2]`, `X^2` has density `s^-1/2` on `(0,1/4)`, so `X_1^2-X_2^2` has infinite density at zero. Therefore an `E2`-only bounded-density endpoint is impossible; an eight-direction theorem must use the overlap/shared-coordinate structure rather than only sharpening scalar-Fourier or `E2` constants.

## Frontier

- 17 baseline: PASS.
- 9 / constant 400 standalone source: independent B02 PASS after local notation repair; do not self-award the two-review release gate.
- 9 / constant <361: new candidate, one review only.
- 8: OPEN/GAP; new overlap theorem gives stronger algebraic mass but no general dependence-safe receiver yet.
- unrestricted 3-eigenvalue QFORM: OPEN; never claim solved.

Model self-report: GPT-5.6 Sol. Configured reasoning effort: UNKNOWN. Provider reasoning-token/thinking-time telemetry: null / not exposed. Programme-local execution context: VERIFIED_BRAIN because authenticated repository retrieval and prior B02 receiver-memory use both occurred; `full_brain_connected=false`.
