# B06 / A028 — a fully paid stopping tree with genuine LTF terminals

**Run:** `20261012T023651Z-account01-B06-a028-ltf-terminal`  
**Primary packet:** A028 (Stopping-tree payment)  
**Attempt:** `A028-LTF-TERMINAL-MODULATION-1`  
**Claim:** `B06-A028-LTF-TERMINAL-STOPPING-v1`  
**Gap:** `G-R-MISMATCH`  
**Status:** restricted all-dimensional stopping theorem PROVED pending
independent review; packet's universal target and full FEI remain OPEN.

## Exact result

Start from any genuine Boolean linear threshold function `f_0`.  At level
`ell`, introduce a fresh physical block `Z_ell` and replace every current
input `u_j` by `u_j q_{m_ell}(Z_ell)`, where `q_m` is the Boolean point defect
that is `-1` at one input and `+1` elsewhere.  Repeat for arbitrary depth.

Query the blocks from newest to oldest.  This is a complete physical
restriction tree.  Every leaf is an input-sign flip of `f_0`, hence is an
actual LTF (negate the corresponding weights), not merely a function assigned
an informal terminal label.

If `P_ell` is the squared Fourier mass of `f_{ell-1}` on odd sets, then

```
H(f_L) = H(f_0) + sum_ell P_ell H(q_{m_ell}),
I(f_L) = I(f_0) + sum_ell P_ell I(q_{m_ell}).
```

These are simultaneously the complete reach-weighted path/leaf entropy
ledger and the single root-influence ledger.  Every fresh block appears once;
terminal influence and queried influence are disjoint.  There is no reused
refund.

For `N=2^m`, `r=2/N`,

```
I(q_m) = m r,
H(q_m) = -(1-r)^2 log2((1-r)^2) + r(2-r)(2m-2) < 4 m r.
```

The strict inequality follows from
`-(1-r)^2 log2((1-r)^2) <= 2r(1-r)/ln(2) < 4r`, while the gap between
`4mr` and the second term is `4r+r^2(2m-2)>4r`.

The owner-approved threshold paper proves the terminal bound with

```
C_LTF = log2(4+e) + 2 log2(e*pi) < 8.937.
```

Therefore the entire hierarchy satisfies

```
H(f_L) <= max(4,C_LTF) I(f_L) = C_LTF I(f_L)
```

for every depth, all block sizes, and all base dimensions.

## Movement relative to A027

A027 proved proper newest-block selection for modulation hierarchies and kept
an abstract terminal `f_0`.  This A028 result supplies the packet's missing
terminal-class bridge: it chooses the published all-LTF class, proves actual
leaf membership under every sign pattern, combines path and leaf costs, and
identifies their one nonoverlapping root-influence budget.  It also sharpens
the point-defect path constant from the prior certified `9/2` to `<4`.

This is a fully paid stopping theorem on an unbounded-depth, unbounded-
dimension genuine Boolean family.  It is not a universal stopping theorem.

## Mandatory controls and first unpaid line

- **Rare defects:** their logarithmic spectral cost is the explicit
  `P_ell H(q_m)` path term; it is not discarded as a negligible event.
- **Long plateaux:** replacing `q_m` by a character gives zero added entropy;
  whole-block querying crosses the plateau while preserving the terminal.
- **Near tensors:** disjoint path and terminal influence remain separate.
- **Addressing:** it may occur only if already covered by the chosen terminal
  class; no generic addressing representation is assumed.
- **Bent splice/shared interference:** unequal branch squared spectra destroy
  the common-modulator identity.  Such a first exit block is outside this
  theorem and remains the universal obstruction.
- **Activation equivalence:** the base is required to be an LTF.  An arbitrary
  core is not declared easy by making its activation rare.

The first unpaid universal statement is: every Boolean function has a
physical stopping tree whose nonterminal blocks admit a bounded path payment
and whose leaves enter a published uniformly controlled class, with both
costs paid from one root influence budget.  No such assertion is made here.

## Verification

Command:

`python3 verify_ltf_terminal.py`

The deterministic checker made 121 assertions with no randomness and no
failures.  It checked point-defect Fourier formulas through dimension 12 by
exact rational Walsh transforms, the strict `<4` bound through dimension 40,
12 one-step LTF/modulator instances, four two-level hierarchies, exact
influence telescopes, and branch squared-spectrum preservation.  The maximum
floating entropy residual was `4.441e-16`.  The all-dimensional theorem is
the proof in `TERMINAL_CLASS_STOPPING.tex`, not an inference from this finite
sweep.

## Source pins and routing

- B06 contract blob: `4fdf4fe492970e589446cc141b90f7b88a81ff2d`.
- Execution protocol blob: `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- A027 report blob: `b60891374b632476414b559358d6581fef43804a`;
  canonical readback commit `c0714d4209871d2b0b46c6aee01da50c92750762`.
- Current source head inspected before the run:
  `4fa89c32748c17c91aeca56c55c7a054b760ba6e`.
- Published LTF source: repository
  `yspennstate/fourier-entropy-threshold-functions`, commit
  `b38ba0ab49618ccbe6d1518a34c141dcec9f247c`, `paper/main.tex` SHA256
  `85e9c4f36026eb5890be5686d03bf5264e524144686ee203ed799e3d41ac7017`.

Route the exact theorem to A059 and A065; route independent reconstruction to
A087 and A094.  No independent acceptance, native Brain ingestion, literature
novelty, or full-FEI conclusion is claimed.
