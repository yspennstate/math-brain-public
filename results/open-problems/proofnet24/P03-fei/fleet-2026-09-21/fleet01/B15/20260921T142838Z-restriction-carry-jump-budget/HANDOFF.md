# B15 handoff — packet carry jumps are influence-paid; cross-magnitude mergers remain

Full FEI remains **OPEN / NOT PROVED**. This run is `WITHOUT_VERIFIED_BRAIN` and does not rerun the settled read-once certificate.

## New proved packetwise result

For one signed equal-magnitude packet

`V=sum_{S in A} eps_S chi_S`

of exact carry depth `r>=1`, split at coordinate `i` as `V_+=P+Q`, `V_-=P-Q`, where `P` contains packet indices without `i` and `Q` those with `i` (with `i` removed).

The exact upper-incidence moments transform by

`M_R^(s)=M_R+(s-1) M_{R union {i}}`.

Both restrictions retain depth at least `r`, and at least one retains exact depth `r`. If the other branch gains a carry level, then

`r(P)=r(Q)=r-1`.

Hence both packet halves have at least `2^(r-1)` coefficients. If `J_a` is the set of coordinates where magnitude packet `a` gains a carry level on one branch, then universally

`sum_{a:r_a>=1} 2^(r_a-1) a^2 |J_a| <= I(f)`.

This is a genuine dimension-free influence budget for **packetwise carry jumps**.

## Exact obstruction that survives

Actual child packets are formed only after coefficients from different parent magnitudes are added. This can create carry from scratch.

Minimal exact Boolean example for the formal property: the 3-bit one-point function `f(000)=+1`, `f=-1` elsewhere has parent Walsh vector

`[-6,2,2,2,2,2,2,2]`.

Its magnitude-6 and magnitude-2 parent packets both have depth 0. Restrict one coordinate to the half containing `000`; the child Walsh vector is

`[-2,2,2,2]`,

which is one magnitude-2 packet of carry depth 1. The child empty coefficient is `(-6+2)/2=-2`, so unequal parent magnitudes are genuinely merged.

The exact checker enumerates all Boolean functions for `n=1,2,3`: no witness exists for `n<=2`, while 128 of 256 three-bit functions satisfy the stated property. Thus dimension 3 is minimal for this precise packet-merger obstruction.

## Next B15 target

Do not try to pay child carry solely by transporting parent packet depths; that lemma is false. The remaining arithmetic object is the **cross-magnitude merger graph** for

`fhat_s(T)=fhat(T)+s fhat(T union {i})`.

The next useful universal inequality must jointly charge merger-created primitive layers and the simultaneous magnitude/free-energy change. Stress-test every candidate first on the 3-bit one-point merger and then on the exact n=18 Numaro packet profile. Preserve the already proved packetwise jump budget as one term, not as the whole induction.
