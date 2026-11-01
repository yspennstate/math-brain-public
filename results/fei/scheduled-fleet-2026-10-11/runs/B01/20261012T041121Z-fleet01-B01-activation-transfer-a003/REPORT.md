# B01 / A003 — fresh-activation transfer for the upper-set potential

**Run:** `20261012T041121Z-fleet01-B01-activation-transfer-a003`  
**Primary packet:** A003, minimal target formulation  
**Stable gap:** `G-UPPER-SET-ASYMMETRY`  
**Status:** all-parameter restricted endpoint and GU' transfer author-proved,
pending A086/A094 review. Full FEI remains **OPEN**.

## 1. Frozen target and prior status

For `p(S)=hat f(S)^2`, `pi(S)=sum_{T superset S}p(T)`, and

`U(f)=sum_S p(S) log_2(pi(S)/p(S))`, define

`G(f)=sum_i [U(f)-E U(f|x_i)]`.

The current B01 target is a universal `GU'` inequality

`G(f) <= a I(f)+b U(f)` with absolute `a<infinity` and `b<1`.

Before this run, the source-pinned identities established `H<=2I+2U`,
the sufficiency of GU', and the coordinate formula
`Delta_i U=B_i-Gamma_i+KL_i`; no dimension-independent bound on the
aggregate asymmetry/KL mismatch was known. B05 had separately derived an
exact retained-`U` formula for a fresh one-point activation, pending
independent review.

This run independently rederives that activation formula from the Walsh
atoms and asks whether its nonaffine mismatch can be summed without losing
the rare logarithm.

## 2. PROVED: exact one-layer decomposition

Let `g` be any genuine Boolean core, `r=Pr[g=-1]`, `d>=1`, `p=2^-d`, and
let `F` equal `g` at one word of `d` fresh control bits and equal `1`
elsewhere. Put

`M(t)=(1-2t)^2 log_2(1/(1-2t)^2)`.

Direct Walsh summation proves

```text
U(F)=pU(g)+Q_{p,d}(r),
Q_{p,d}(r)=M(pr)+2rpd-pM(r)
           +4pr^2 log_2(1/r)-4p^2r^2 log_2(1/(pr)).
```

After removing the affine term, `R_p(r)=Q_{p,d}(r)-2rpd`, the complete
aggregate restriction charge is

```text
G(F)=pG(g)+d delta_d(r)
     +sum_j [R_p(r)-{R_p(r_{j,+})+R_p(r_{j,-})}/2],
```

where `r=(r_{j,+}+r_{j,-})/2` and

```text
delta_d(r)=M(pr)-M(2pr)/2+2pr
           +4p^2r^2(log_2(1/(pr))-2).
```

This separates the physical control payment from the signed data-core
Jensen gaps. It retains the full rare logarithm and includes all endpoint
cases.

## 3. PROVED: dimension- and rarity-independent transfer

The scalar derivative bounds in `ACTIVATION_TRANSFER.tex` give

```text
|R_p'(r)| <= p L_R,
L_R = 4 + 14(1+2/e)/ln 2,
K_act=L_R/2 < 19.530,
C_star=1+2(1+1/e)/ln 2 < 4.947.
```

Using `|r_{j,+}-r_{j,-}|<=Inf_j(g)` and the exact physical influence
identity `I(F)=pI(g)+I_ctl`, `I_ctl=2rpd`, proves

```text
G(F) <= pG(g)+K_act pI(g)+C_star I_ctl.                 (T)
```

Thus if a restriction-closed base class satisfies
`G(g)<=aI(g)+bU(g)` for `0<=b<1`, every fresh one-point activation satisfies
the same contraction coefficient `b` and

```text
G(F)<=a'I(F)+bU(F),
a'=max{a+K_act, C_star+b(K_act-1)}.                     (GU'-transfer)
```

This is not a restatement of FEI: it is an exact class-extension theorem
with explicit constants, arbitrary Boolean terminal core, arbitrary data
dimension, and arbitrary activation depth/probability.

## 4. PROVED restricted endpoint

Let `A` contain constants, signed parities, and one fresh activation of any
signed parity, with arbitrary parity dimension and arbitrary number of
control bits. The class is restriction-closed: restricting a control bit
either kills the activation or reduces `d`, while restricting a data bit
leaves a signed parity.

Since signed parities have `U=G=0`, (T) gives

```text
G(F) <= K_act I(F),
U(F) <= K_act I(F),
H(F) <= (2+2K_act) I(F) < 41.059 I(F).
```

The constant is independent of data dimension, control depth, activation
probability, parity support, and sign. The class contains arbitrarily rare
one-point defects and arbitrarily rare activated nonflat parity cores.

## 5. Mandatory falsifiers and computation

`verify_activation_transfer.py` recomputes the full Walsh law, every upper
mass, every physical coordinate restriction, `U`, `G`, and `I`. It checks:

- every Boolean core through three variables;
- the two-address/four-data multiplexer;
- a four-bit point defect;
- disjoint-tensor and shared-variable overlap products;
- 24 seeded random five-bit cores;
- every signed parity support size through five data variables.

Across 1,476 arbitrary-core activation cases and 168 parity-class cases,
the exact decomposition and transfer inequalities passed at 70-decimal
precision. The maximum identity residual was below `2e-67`. Computation is
only a normalization/sign/endpoint check; the theorem is analytic for all
parameters.

## 6. Exact movement and remaining universal obstruction

**Previous tracked status:** cancellation at a single rare node was known,
but changing coherent cores across a hierarchy had no uniform payment.

**New status:** the entire one-layer signed charge has an absolute transfer
bound, and the contraction coefficient `b<1` is preserved for arbitrary
fresh one-point suspensions. This proves GU and hence FEI on the expanding
restriction-closed parity-core class above.

**Unpaid line:** iterating the transfer naively adds `K_act` to `a` at every
coherent core change. A universal theorem still requires a single-use
credit or signed cancellation preventing this linear-in-depth accumulation.
The result therefore does not prove full FEI, does not handle reused
selectors, and does not turn weighted examples into Boolean
counterexamples.

## 7. Source pins and review status

- Control order and case targets: Brain commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`, revision 2026-10-12.1.
- B01 contract: `assignments/B01.json`, blob
  `ac038a028831d59ad053dd56b2b527e2a71ffdee`.
- Upper-set source notes: blob
  `5797e9cc38598cbee391cc99d4b1abcd554b662e` in
  `<private-repo>`.
- Relevant B05 original: commit
  `e64b7c886026c13828fe4833dfadd133c0ac4de6`, report blob
  `279e884...`; its formula is rederived here rather than imported as an
  accepted theorem.
- Latest neighboring A003 report: commit
  `a6ae2ec5c8a178d13d3be703f9c0da414b50f107`, report blob
  `d9957761642a39adf96f54ae4ce3b5a845e81f58`.

No literature-priority claim is made. Independent review is still required
from A086/A094. Full FEI remains **OPEN**.
