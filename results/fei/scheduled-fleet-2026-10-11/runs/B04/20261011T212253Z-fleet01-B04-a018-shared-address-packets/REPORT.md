# B04 / A018 — collision interface and shared-address packet compression

**Run:** `20261011T212253Z-fleet01-B04-a018-shared-address-packets`  
**Primary packet:** A018 (Shared-data collision law)  
**Attempt:** `A018-PACKET-COMPRESSION-1`  
**Claim version:** `B04-A018-SHARED-ADDRESS-PACKET-v1`  
**Gap:** `G-LOWSEL-COLLISION`  
**Status:** baseline interface source-pinned; new explicit packet theorem PROVED
pending independent review. Full FEI remains OPEN.

## Result

The exact shared-data collision identity was reconstructed from its original
source with all normalizations, zero-mass exclusions, and the empty data set
retained.  For `F(x,y)=g_x(y)` and the conditional laws `r_T, nu_T`, define

```
B_W = sum_T R_T H(nu_T),
M_W = a - sum_T R_T H(r_T).
```

Then

```
H(F) - 2^(-a) sum_b H(g_b) = B_W + M_W,
0 <= M_W <= (2/ln 2) I_sel(F).
```

This is a source-pinned baseline rather than a novelty claim.

The mathematical delta is an exact joint packetization of the scalable
shared-address family

```
F_{t,k}(x,y) = product_{r=1}^k y_{r,x}.
```

For every integers `t,k>=1`, its spectral law is uniform on the `2^(2t)`
atoms `(S,D_b)`, with `b` an address and `S` an address Fourier subset.
Consequently

```
H(F_{t,k}) = 2t,
I(F_{t,k}) = t/2 + k,
B_W = M_W = t.
```

The lossless cover encodes the packet label `b` once (cost `t`), then the
conditional address subset `S` (cost `t`); its data set is deterministic in
the packet.  Its expected rank is exactly `t/2+k`.  Although each address
coordinate appears in all `2^t` packet descriptions, its probability-weighted
spectral congestion is `1/2`; each data coordinate has congestion `2^-t`.

This contrasts with the coordinatewise marginal-entropy budget

```
sum_i h2(I_i) = t + k 2^t h2(2^-t).
```

For `k=t`, this divided by influence grows as `(2/3)t+O(1)`, while the true
FEI ratio is exactly

```
H/I = 2t/(3t/2) = 4/3.
```

Thus the coordinatewise estimate is refuted for every finite constant.  Its
failure is repeated payment of a common address label; the packet code
charges that label once.

## Boundary and falsifier checks

- **Identical branches:** `r_T` is uniform and `nu_T` is a point mass, so
  `B_W=M_W=0`; the whole selector alphabet cancels.
- **Selector-character signs:** the point mass moves but the same entropy
  cancellation holds.
- **Shared-address packets:** `r_T` is a point mass and `nu_T` is uniform,
  giving `B_W=M_W=t` exactly.
- **Bent splice:** the source family has `I_sel=2^-m` and
  `Delta_sel H/I_sel >= m-1`, so packetization does not imply a universal
  selector-only payment.
- **Signed-dictator embedding:** for `g_b(y)=h(b)y`, the remaining packet
  entropy is `H(h)` and selector influence is `I(h)`.  A universal bound at
  this unrestricted scope is exactly FEI, so claiming it as an auxiliary
  low-energy lemma would be circular.
- **Addressing / near tensors:** the displayed family is an exact disjoint
  data-block tensor conditioned on one common address.  No overlap-product
  subadditivity is used.

## Acceptance and limitations

`COLLISION_BLOCK_INTERFACE.tex` supplies the exact A018 interface plus the
constructive cover, all label costs, all rank costs, and the failure scope.
`COLLISION_CONTROLS.json` records the controls.  The exact integer Walsh
checker passed 205 assertions on six nontrivial finite instances.

The result advances the B03 overlap lane by giving an explicit family with
unbounded worst-case read and bounded fractional spectral congestion.  It
does **not** provide a new low-selector-energy class, because this family has
`I_sel/t=1/2`, already inside the positive-energy closure.  The live gap is
to find structure excluding the signed-dictator embedding while retaining a
nontrivial class with `I_sel/a -> 0`.

## Source pins

- B04 compact contract blob: `e60aaacf97770ecfeb5b9ab7f04a5143cc0f94ce`.
- Original collision proof:
  `reports/fei-2026-10-11/source_material/reductions/paper/multiplexers.tex`,
  blob `0c20fb66450849b6b7ddd4a9e955e6c6112c008e`.
- Independent internal collision audit:
  `research_pushes/2026-10-11-full-fei-100-agents/supporting/shared_data_delta_independent_audit.md`,
  blob `926652cd21c62a477bbf4e17bebffce93c41392b`.
- Bent-splice original:
  `reports/fei-2026-10-11/source_material/reductions/paper/restrictions.tex`,
  blob `55986205ce92bf93bbb2863b5064af001829844a`.
- Inspected open-problems head: `3428cf1d55810b1792ce2e38898f99229f6e428f`.

## Next handoff

Route the packet theorem to A014/B03 as its requested unbounded-worst-read,
bounded-fractional-congestion example.  A019 should seek a structural
condition that pays `B_W` when selector energy vanishes while provably
excluding `g_b(y)=h(b)y`.  Independent review targets are A091 and A090.
