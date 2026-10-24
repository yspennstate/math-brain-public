# B18 final-freshness integration note — B16 central Radon square payment into the KL-refunded restriction toll

**Run:** `2026-09-21T15:34:36.140986Z`  
**Status:** **CONDITIONAL BRIDGE PROVED; unrestricted FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

After the main B18 report was written, `math-open-problems` master advanced to
`43dcc832af6944b9c6c733579c9d8dc9a87a1ddf`, adding the account01/B16 central-Radon energy theorem. This note integrates that fresh result rather than freezing B18 at the earlier peer frontier.

## 1. Inputs, at their exact proved scopes

B18 proved for a restriction-maximal Boolean core `g` and every fixed target dimension `q` that the exact descent toll is

`Gamma_q(g) = [Rcal_q(g)-K_q(g)] / I(g)`,                            (1.1)

where

`K_q = T-(n/q) Tbar_q`                                               (1.2)

is the KL total-correlation density lost under random q-coordinate projection. The quantity

`UNPAID_q := Rcal_q-K_q >= 0`                                        (1.3)

is therefore the exact remaining restriction obstruction at that scale.

The fresh B16 theorem works in the character-folded gauge, with

`J(g)=sum_i min(Inf_i(g),1-Inf_i(g)) <= I(g)`.                       (1.4)

For a family of translation-invariant source kernels `K_{i,t}` whose nonzero Walsh modes are odd and satisfy the dimension-independent multiplier envelope

`|Khat_{i,t}(U)| <= M t^{|U|}`                                       (1.5)

for odd `U`, B16 proves

`sum_i int_0^(1/2) t(1/2-t) [D_i^K(t)]^2 dt
 <= (M^2/1080) J(g)`.                                                (1.6)

For the canonical prefix-minus-suffix source kernel, `M=2`, recovering the sharper specialized payment `sum_i S_i <= J/270`.

B16 explicitly does **not** prove that the fully refunded compiler divergence equals such a source operator; that is its stated remaining bridge.

## 2. PROVED conditional closure theorem: the compiler only needs to dominate the KL-refunded remainder

### Theorem B18-RADON-KL-COMPILER-01

Fix one restriction-maximal core `g` and one target dimension `q`. Suppose there is a dimension-independent constant `Lambda_q >= 0` and source kernels satisfying B16's odd-multiplier condition with envelope `M_q` such that the **already KL-refunded** recombination toll obeys

`Rcal_q(g)-K_q(g)
 <= Lambda_q * sum_i int_0^(1/2) t(1/2-t) [D_i^K(t)]^2 dt`.           (2.1)

Then there exists a q-dimensional physical restriction child `h` for which

`H(h)/I(h) >= H(g)/I(g) - Lambda_q M_q^2/1080`,                      (2.2)

with the usual convention that the assertion is trivial when `I(g)=0`. Equivalently,

`Gamma_q(g) <= Lambda_q M_q^2/1080`.                                (2.3)

#### Proof

Combine the exact B18 identity (1.1) with (2.1), then B16's source payment (1.6):

`Gamma_q
 <= [Lambda_q/I(g)] * (M_q^2/1080) J(g)
 <= Lambda_q M_q^2/1080`,                                           (2.4)

because `J(g)<=I(g)`. The B18 descent theorem supplies a q-dimensional child losing at most `Gamma_q` in entropy/influence ratio. QED.

### Corollary B18-RADON-KL-COMPILER-02 — multiscale Bellman closure

Consider a valid restriction/peeling descent

`g_0 -> g_1 -> ... -> g_L`

with dimensions decreasing at each restriction step. If step `s` satisfies (2.1) with constants `Lambda_s,M_s`, then

`H(g_0)/I(g_0)
 <= H(g_L)/I(g_L) + (1/1080) sum_{s=0}^{L-1} Lambda_s M_s^2`.        (2.5)

Consequently, if a universal descent rule reaches a class with FEI constant `C_0` and has

`sum_s Lambda_s M_s^2 <= B`                                         (2.6)

for a dimension-independent `B`, then full FEI follows with constant

`C = C_0 + B/1080`.                                                  (2.7)

This is a genuine sufficient theorem, not a proof that (2.1) holds.

## 3. Why the target in (2.1) is sharper than the raw B16 compiler target

The fresh B16 report asks for a bounded multiplier for the **fully refunded** q-flip-to-physical-cut compiler and stresses that the raw ordered-min kernel has growing low modes. B18's new identity identifies one exact global refund that must already be applied before asking the source theorem to pay anything:

`K_q = T-(n/q)Tbar_q`.                                               (3.1)

Therefore a compiler proof need not, and should not, try to dominate raw `Rcal_q` by the Radon square. It only needs to dominate

`UNPAID_q = Rcal_q-K_q`.                                             (3.2)

This distinction is forced by the B15 packet/product bridge as well: the large bridge KL and `log Z` can cancel before they produce the small actual total correlation, and only the scale-q contraction of that total correlation is spendable. A raw-source comparison that ignores this refund risks both a false growing mode and double counting.

The precise cross-worker bridge is now:

> **Compiler target.** Express or upper-bound the KL-refunded physical recombination remainder `UNPAID_q` by a fully refunded central odd source operator with a dimension-independent Walsh multiplier envelope.

If the B16 refund algebra and the B18 `K_q` subtraction turn out to represent overlapping cancellations, they must be identified before summing them; (2.1) is deliberately formulated after the KL subtraction to prevent a duplicated credit.

## 4. Current exact ledger after the fresh B16 theorem

**PROVED:** B18-KL-PROJECTION-01, B18-KL-RECOMBINATION-02, and the conditional compiler implications (2.3) and (2.5).

**PROVED inherited:** B16 central source-square payment and odd-multiplier criterion at their source-side scope; B15 packet/product bridge; B14 disjoint-composition erasure identities; B17 structural normal forms at their stated hypotheses.

**OPEN:** establish (2.1) for an unrestricted Boolean restriction step with dimension-independent or summably bounded `Lambda_q M_q^2`; equivalently derive the actual multiplier of the fully refunded compiler acting on `UNPAID_q`.

**REFUTED/FORBIDDEN shortcut:** apply B16's `J/270` source payment directly to raw restriction recombination `Rcal_q` without proving the compiler map and without subtracting/reserving the exact KL term. That would change representations and can double count a refund.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.
