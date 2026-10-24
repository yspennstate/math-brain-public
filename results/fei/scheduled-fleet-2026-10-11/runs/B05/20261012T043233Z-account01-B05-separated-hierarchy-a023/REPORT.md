# B05 / A023 — retained credit for separated changing-core hierarchies

**Run:** `20261012T043233Z-account01-B05-separated-hierarchy-a023`  
**Primary packet:** A023, amortized rarity budget  
**Stable gap:** `B05_RARE_REFUNDS` / `G-UPPER-SET-ASYMMETRY`  
**Status:** arbitrary-depth scoped theorem author-proved, pending A087/A094
review. Full FEI remains **OPEN**.

## 1. Frozen objective and previous value

The preceding B05 theorem handled one fresh rare activation with an
arbitrary fixed terminal core:

`U(F)-pU(g) <= C_* I_ctl`, with `C_*<4.947`.

It retained the terminal packet once but did not permit the active Boolean
core to change from ancestor to ancestor. The neighboring B01 transfer
showed that treating such changes one layer at a time can add a fixed
constant at every layer.

This run freezes the first genuinely changing-core hierarchy: every node is
a fresh one-word rare switch between two arbitrary Boolean child subtrees,
and the complete physical variable sets of the two siblings are disjoint.
The bounded objective is a retained-leaf `U` payment with a constant
independent of depth, rarity, leaf dimension, leaf spectrum, and the number
of core changes.

## 2. PROVED: exact two-core formula

Let `g_0,g_1` be arbitrary Boolean functions on disjoint input blocks,
`r_i=Pr[g_i=-1]`, `theta=r_0+r_1-2r_0r_1`, `d>=1`, and `p=2^-d`. Define

```text
F=g_1 at one fresh d-bit control word,
F=g_0 otherwise.
```

The full formula for `U(F)` is equation (2) of
`SEPARATED_HIERARCHY_PAYMENT.tex`. It contains:

- the exact weighted endpoint packets `(1-p)U(g_0)+pU(g_1)`;
- the scalar mean/empty-frequency Jensen term;
- both child variance packets;
- the exact control-depth term;
- the scalar interaction
  `4(p-p^2)(r_1-r_0)^2 log_2(theta/(r_1-r_0)^2)`.

No spectral detail beyond the two endpoint `U` packets survives because the
nonempty Fourier supports of disjoint sibling blocks are separated. Direct
Walsh expansion proves the identity, including deterministic endpoints.

## 3. PROVED: uniform node payment

Revealing the control block has complete signed charge

```text
J=U(F)-(1-p)U(g_0)-pU(g_1).
```

Its physical selector influence is exactly

```text
I_ctl=2 p d theta.
```

The scalar estimates on the page prove

```text
J <= C_sep I_ctl,
C_sep = 3 + 4(1+2/e)/ln2 + 2/ln2 + 2/(e ln2)
      < 16.964.                                             (N)
```

This is an upper bound on the complete signed charge, not on every
nodewise positive component of `B-Gamma+KL`.

## 4. PROVED: arbitrary-depth changing-core hierarchy

Consider any finite physical tree in which every internal node uses a fresh
one-word control block, its two child subtrees have disjoint complete
variable sets, and leaves are arbitrary genuine Boolean functions. Let
`w_v` and `w_l` be node and leaf reach probabilities.

The node charges and physical selector influences telescope without reuse:

```text
sum_v w_v J_v
  = U(F_root)-sum_l w_l U(g_l),

sum_v w_v I_ctl,v = I_sel(F_root).
```

Therefore

```text
U(F_root)-sum_l w_l U(g_l) <= C_sep I_sel(F_root).           (T)
```

Each rare logarithm, selector coordinate, endpoint packet, and leaf packet
is used exactly once. This is the first A023 upper-set theorem here that
allows arbitrarily many core changes with no depth-dependent constant.

If every leaf belongs to a class satisfying `U<=K I`, then

```text
U(F_root) <= max(C_sep,K) I(F_root).
```

Thus the theorem is a genuine closure result, while arbitrary hard leaves
remain honestly retained rather than assumed paid.

## 5. Controls and computation

`verify_separated_hierarchy.py` independently recomputes integer Walsh
spectra, exact rational upper masses, every `U`, and physical coordinate
influences. It checks:

- all 1,936 pairs of Boolean cores through two variables and depths 1–4;
- point defects, parity, a quadratic bent core, a 2-address/4-data
  multiplexer, a disjoint tensor, and an overlap-product terminal core;
- 40 seeded random four-bit terminal cores;
- 200 direct multi-level chains and balanced trees.

All checks passed at 70-decimal precision; the largest formula residual was
`9e-69`. The analytic proof, not floating computation, establishes the
all-parameter theorem.

Mandatory scope distinctions:

| Control | Result |
|---|---|
| Rare restrictions / sparse defects | Covered at arbitrary depths and retained at leaves |
| Bent and nonflat cores | May appear as arbitrary leaves |
| Near tensors | May appear inside a leaf; leaf `U` is retained |
| Addressing | An addressing function may be a leaf, but shared address bits across siblings are not covered |
| Prime Boolean gates | Arbitrary at leaves; no claim that the whole class contains every prime gate |
| Shared-variable products | May be leaves, but overlapping sibling spectra remain outside the theorem |

## 6. Exact movement and remaining gap

**Previous tracked quantity:** naive layerwise handling could charge a fixed
constant once per changing core, producing a coefficient linear in tree
depth.

**New value:** for separated sibling cores, the full all-depth coefficient
is the absolute constant

`C_sep<16.964`,

independent of depth and all activation probabilities.

**First unsupported line:** when sibling cores share variables or reuse
address bits, their nonempty Fourier coefficients interfere inside the same
upper masses. The exact separated formula then acquires a distributional
overlap defect. A universal proof must bound the total positive overlap
defect by nonreused physical pivotal events or show a signed telescope.

The next attempt should freeze the two-core shared-variable switch
`g_0+a(z)(g_1-g_0)`, derive the exact overlap defect relative to equation
(2), and test it on one-point bent surgery, whole-set addressing, and
overlap products. Full FEI remains open.

## 7. Sources and review status

- Owner control: `math-research-brain` commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`, revision 2026-10-12.1.
- B05 contract blob: `05447e6d999437bb82a266b427bd76a4b37266b6`.
- Preceding B05 source: canonical commit
  `e64b7c886026c13828fe4833dfadd133c0ac4de6`, proof blob
  `881573731c3785022914a7ef8231eda5948c9dc6`.
- Neighboring B01 transfer: canonical commit
  `8344aa4aa688790494e3ebd46bb94b13f659ce18`, proof blob
  `fd291e847f0f7a21591398af6b415fa00787cd17`.

No external novelty or priority claim is made. Independent A087/A094
review remains pending. Scheduler/graph mutation: none. Native Brain
ingestion: not claimed. Full FEI: **OPEN**.
