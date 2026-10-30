# A087 restriction review: point-defect terminal hierarchy

## Verdict

**ACCEPTED WITH A LOCAL REPAIR, AT THE STATED RESTRICTED-CLASS SCOPE.**

Target claim: `B06-A028-LTF-TERMINAL-STOPPING-v1`, from
`runs/B06/20261012T023651Z-fleet01-B06-a028-ltf-terminal/` at open-problems
commit `458cdd8acd656eb6ba36a28a5415bd3332d577d0`.

The exact spectral telescopes, the physical block-restriction tree, its leaf
class, terminal entropy, and nonreuse of fresh-block influence all reconstruct.
The written proof has one endpoint gap: its logarithmic estimate divides by
`1-r` when `m=1` and `r=1`.  That case is repaired separately because `q_1`
is a signed dictator, so `H(q_1)=0` and `I(q_1)=1`.  No change to the theorem
statement or constant is required.

Because this review supplies that repair, it is contributor evidence rather
than an independent acceptance receipt.  A fresh uninvolved reviewer remains
required by the campaign protocol.  Full FEI remains open.

## Sources reconstructed

- Original theorem and proof: `TERMINAL_CLASS_STOPPING.tex`, blob
  `490eff8d5d49a1999dd0a4cc6b5019cc7679737a`.
- Upstream frozen block ledger: A027 `BLOCK_CONTROLS.md`, blob
  `0ae9486f38c44449a82ec6ee46cdc835ecf5bc2e`.
- Published LTF input: owner-approved `paper/main.tex` at commit
  `b38ba0ab49618ccbe6d1518a34c141dcec9f247c`, blob
  `1a9af8c62a32566a6ad1b7323a84d103a8375e93`; lines 600--637 derive
  `H(f) <= (log_2(4+e)+2 log_2(e pi)) D(f)`, hence the weaker bound by total
  influence used here.
- Author checker and output were inspected but not treated as independent
  proof.  `audit_terminal_stopping.py` is a new exhaustive small-cube
  reconstruction.

## Independent reconstruction

Let `g:{-1,1}^N->{-1,1}` and let `h` be Boolean on a fresh block `Z`.  Put

`F(u,z)=g(u_1 h(z),...,u_N h(z))`.

The Fourier expansion is

`F = sum_{|S| even} ghat(S) chi_S(u)
   + sum_{|S| odd,T} ghat(S) hhat(T) chi_S(u) chi_T(z)`.

The labels `(S,T)` are disjoint, so with
`P_odd(g)=sum_{|S| odd} ghat(S)^2`, exact expansion of the Shannon functional
and expected degree gives

`H(F)=H(g)+P_odd(g) H(h)`,

`I(F)=I(g)+P_odd(g) I(h)`.

These are identities, including `P_odd=0`, so there is no division by a
zero mismatch or odd mass.

For each physical block value `z=a`,

`F_a(u)=g(u_1 h(a),...,u_N h(a))`.

Its Fourier coefficients are `ghat(S) h(a)^|S|`; therefore every physical
child has exactly the predecessor's squared spectrum.  Consequently

`H(F)-E_a H(F_a)=P_odd(g) H(h)`,

`I(F)-E_a I(F_a)=P_odd(g) I(h)`.

The expectation is over the actual uniform block assignment.  Thus the
claimed payment is the exact root-minus-mean-child decrement for the proper
fresh block.  It is not a literal physical reach probability: every block is
reached with probability one.  The factor `P_odd` is spectral odd mass.  The
source phrase “reach-weighted” should be read or replaced accordingly.

Iterating from newest to oldest is legitimate even though the newest common
modulator flips variables in older auxiliary blocks.  Conditional on a newer
block, the predecessor is composed with a global input sign flip.  This
preserves its squared spectrum.  Once every auxiliary block is fixed, the
leaf is `f_0` with a global input sign flip, hence an actual LTF with the same
squared Fourier spectrum.  Therefore expected terminal entropy is exactly
`H(f_0)`, not a discarded debt.

Fresh blocks are disjoint.  In the influence identity, `I(g)` contains all
older-coordinate influence and `P_odd I(h)` contains exactly the new block's
influence.  Iteration partitions the final total influence into the base term
and one term per physical block; no block is charged twice.

## Boundary repair

Write `r=2/2^m`.  For `m>=2`, the source proof is valid:

`H(q_m)=-(1-r)^2 log_2(1-r)^2+r(2-r)(2m-2)` and `I(q_m)=mr`,

and `-log(1-r)<=r/(1-r)` yields `H(q_m)<4 I(q_m)`.

At `m=1`, that displayed logarithmic bound is undefined because `r=1`.
Directly, the one-point defect on one bit is a signed dictator.  Its only
nonzero Fourier coefficient has squared mass one at level one, hence
`H(q_1)=0<4=4I(q_1)`.  This closes the only failed endpoint.

Combining the exact telescopes, `H(q_m)<4I(q_m)`, and the published all-LTF
bound gives

`H(f_L) <= max{4,C_LTF} I(f_L) = C_LTF I(f_L)`,

where `C_LTF=log_2(4+e)+2log_2(e pi)<8.937`.

## Controls and scope

- Rare point defect: the rare Fourier/logarithmic cost is retained inside
  the exact `H(q_m)` term.
- Zero odd mass: both entropy and influence increments vanish.
- Addressing/near-tensor base: the theorem only inherits a base-class bound;
  it does not prove one.
- Bent or unequal-spectrum children: outside the common-modulator class.
- Arbitrary Boolean inputs: no block-selection theorem is proved.

This is a genuine all-depth Boolean result for a narrow hereditary modulation
hierarchy.  It is not a universal stopping theorem and does not prove FEI.

## Required next action

Route the repaired theorem and this audit to an uninvolved A094 or A085
reviewer.  The reviewer should check the `m=1` case, the meaning of
“reach-weighted,” and the two-level sign flip of older auxiliary variables.
