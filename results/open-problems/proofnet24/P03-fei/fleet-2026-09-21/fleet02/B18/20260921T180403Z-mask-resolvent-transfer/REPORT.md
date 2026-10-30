TASK: B18 ACCOUNT: fleet02 RUN: 2026-09-21T18:04:03Z — FEI proof integration: syndrome-mask resolvent transfer theorem

MODEL: GPT-5.6 Sol; source=self_report
THINKING LEVEL: UNKNOWN; source=not_exposed; requested=maximum actually supported
THINKING USAGE: NOT_EXPOSED; provider thinking time=NOT_EXPOSED; coverage=unavailable
EXECUTION: WITHOUT_VERIFIED_BRAIN
FULL FEI STATUS: OPEN / NOT PROVED

# 0. Fresh state and scope

Fresh authenticated fleet control was reread before this delivery at `yspennstate/math-research-brain` main
MESSAGE explicitly keeps B18 on FEI proof integration and supersedes conflicting older installation-only assignments.
The protected README blob remains `14c6dfefb9a567d99dea06c7cd48dbb38e7a56c9`. Previously byte-verified SHA-256
values for this unchanged blob are README
`e2cf6cf6cb8c4941b55a12284a4e69ac75747e3198e0bb34df42ec9f30520aa6`; those hashes are retained with that
provenance rather than presented as fresh hashes of connector-rendered text.

The mathematical master was refreshed during the run; the last pre-write observation was
`385fa72dde1a1105c9145c9667232c1adf1c515b`. I used the current P03 README and September-21
TASKS/REPORT/APPROACHES, plus the fresh signed-transport chain:
fleet04/B16 parity-current Walsh-frame diagonalisation, fleet02/B16 q-flip frame-incidence theorem, and
fleet01/B16 projective q-flip/noise and mask-stability addenda. I did not reuse the obsolete unrestricted target
6.4547837: the current repository records the larger external lower bound
`C_FEI > 6.521845710923046575`.

The three deliberately different FLEET_RULES moves for this run are:
- **#3 PROVE SOMETHING STRONGER:** prove the mask-transfer estimate for arbitrary correlated selectors and arbitrary positive noise-scale measures, not only one compiler law.
- **#12 FIND WHAT IS CONSERVED:** use the exact XOR law for plaquette frustration under multiplication of Boolean masks.
- **#30 ONE SCALE / ONE DIRECTION AT A TIME:** first prove the fixed `(p,q)` product-noise bound, then integrate the two scales exactly.

# 1. Entering lemmas

For a Boolean phase `h:F_2^n->{±1}` and translations `u,v`, write
\[
P_h(u,v)=Pr_x[h(x)h(x+u)h(x+v)h(x+u+v)=-1].
\]

The fresh fleet01/B16 projective plaquette theorem proves, with
\[
\beta_h(u)=\min_{\varepsilon=\pm1}Pr[h(x+u)\ne\varepsilon h(x)],
\qquad
J(h)=\sum_i\beta_h(e_i),
\]
that if `U_p,V_q` are independent physical-coordinate product-noise directions with coordinate inclusion
probabilities `p,q in [0,1/2]`, then
\[
E\,P_h(U_p,V_q)\le 2\min(p,q)J(h). \tag{1.1}
\]

Its mask-stability lemma proves
\[
|P_{fh}(u,v)-P_f(u,v)|\le P_h(u,v). \tag{1.2}
\]

The remaining fleet04 compiler obstruction was that syndrome/Walsh averaging changes the base phase. The compiler
therefore still needed a dimension-free way to transfer its averaged source kernel back to the original Boolean
phase without pretending total influence is invariant under the mask.

# 2. PROVED: arbitrary-selector mask transfer

Let `m_1,...,m_N` be arbitrary Boolean masks. Let `Z=(Z_1,...,Z_N)` be an arbitrary random `{0,1}^N` vector; no
independence is assumed. Put
\[
M_Z=\prod_{j=1}^N m_j^{Z_j},
\qquad \theta_j=E Z_j.
\]

## Lemma B18-MASK-XOR-TRANSFER

For every fixed `u,v`,
\[
\boxed{
E_Z\,|P_{fM_Z}(u,v)-P_f(u,v)|
\le \sum_j\theta_j P_{m_j}(u,v).
} \tag{2.1}
\]

### Proof

For a Boolean phase `h`, let
\[
Q_h(x;u,v)=h(x)h(x+u)h(x+v)h(x+u+v)\in\{\pm1\}.
\]
Multiplication of phases multiplies plaquette signs:
`Q_{ab}=Q_a Q_b`. Therefore, for deterministic `Z`, the bad-plaquette bit of `M_Z` is the XOR of the bad-plaquette
bits of the selected masks. Pointwise,
\[
1_{\{Q_{M_Z}=-1\}}\le \sum_j Z_j1_{\{Q_{m_j}=-1\}}.
\]
Also the bad-plaquette bit of `fM_Z` is the XOR of those of `f` and `M_Z`, hence
\[
|1_{\{Q_{fM_Z}=-1\}}-1_{\{Q_f=-1\}}|
\le1_{\{Q_{M_Z}=-1\}}.
\]
Average first in `x`, then in `Z`. Only the marginals `E Z_j=\theta_j` remain. QED.

The absence of an independence assumption is useful: a genuine syndrome translate may select masks with strong
dependencies, so a Bernoulli-selector representation is not required for this step.

# 3. PROVED: positive-measure product-noise resolvent theorem

Let `Omega` be any positive measure on `(0,1/2]^2` with finite moment
\[
M_\Omega=\int \min(p,q)\,d\Omega(p,q)<\infty.
\]

## Theorem B18-MASK-RESOLVENT-TRANSFER

For every Boolean `f`, every family of Boolean masks `m_j`, and every selector law `Z`,
\[
\boxed{
\int E_{Z,U_p,V_q}
|P_{fM_Z}(U_p,V_q)-P_f(U_p,V_q)|
\,d\Omega(p,q)
\le
2M_\Omega\sum_j\theta_j J(m_j).
} \tag{3.1}
\]

### Proof

Apply (2.1), Tonelli (all terms are nonnegative), and then (1.1) mask by mask:
\[
\begin{aligned}
&\int E_{Z,U_p,V_q}|P_{fM_Z}-P_f|\,d\Omega\\
&\le \sum_j\theta_j\int E_{U_p,V_q}P_{m_j}(U_p,V_q)\,d\Omega\\
&\le 2\sum_j\theta_jJ(m_j)\int\min(p,q)\,d\Omega.
\end{aligned}
\]
This is (3.1). QED.

The important point is quantitative: the syndrome-mask error is controlled by the **mask bank**
`sum theta_j J(m_j)`, not by the translated phase's total influence and not by the number of q-flip generators.

# 4. PROVED: the two-inverse-noise singularity is integrable

Take
\[
d\Omega(p,q)=\frac{dp\,dq}{pq},
\qquad 0<p,q\le1/2.
\]
Although `Omega` itself has infinite total mass,
\[
\begin{aligned}
M_\Omega
&=\int_0^{1/2}\int_0^{1/2}\frac{\min(p,q)}{pq}\,dp\,dq\\
&=2\int_0^{1/2}\int_0^q\frac1q\,dp\,dq
=1.
\end{aligned}
\]
Therefore
\[
\boxed{
\int_0^{1/2}\int_0^{1/2}
\frac{
E_{Z,U_p,V_q}|P_{fM_Z}(U_p,V_q)-P_f(U_p,V_q)|
}{pq}\,dp\,dq
\le 2\sum_j\theta_jJ(m_j).
} \tag{4.1}
\]

This is the direct implication missing from the fresh mask-stability handoff: **once the compiler has legitimately
reached a positive physical product-noise double-resolvent, syndrome translation can be pushed back to the original
phase at dimension-independent cost.** The error survives both inverse-noise singularities because plaquette
frustration vanishes linearly in the smaller noise scale.

For the ordered-min one-subcube generators
\[
m_j(x)=1-2\,1_{\{x_{F_j}=b_j\}},\qquad c_j=|F_j|,
\]
the fresh subcube calculation gives `P_{m_j}=0` when `c_j<=1`; for `c_j>=2`,
\[
J(m_j)=c_j2^{1-c_j}.
\]
Hence (4.1) becomes the explicit bank
\[
\boxed{
\text{mask-transfer error}
\le
2\sum_{j:c_j\ge2}\theta_j c_j2^{1-c_j}.
} \tag{4.2}
\]
No ambient-dimension factor appears.

# 5. What this closes and what it does not

**PROVED in this run.**
1. Correlated syndrome-mask selectors need only their one-mask marginals for source-kernel transfer.
2. Any positive product-noise mixture is paid by its single scalar moment `M_Omega`.
3. The exact double inverse-noise measure `dp dq/(pq)` has moment one, so the full mask-transfer error is at most
   twice the weighted folded-influence bank of the masks.
4. For the actual one-subcube generator class, that bank is explicitly `sum theta_j c_j 2^(1-c_j)`.

**CONDITIONAL compiler corollary.**
If the fully signed, same-syndrome-aggregated parity current can be pushed forward to a positive physical
product-noise mixture *after* R32/R16/terminal refunds, with selector marginals `theta_j` satisfying
\[
\sum_j\theta_jJ(m_j)\le A\,J(f),
\]
then the syndrome-translation error is at most `2A J(f)`. This removes the previously separate
"translated phase versus original phase" obstruction from that branch.

**OPEN.**
The current reports do not yet prove either of the two hypotheses in the conditional corollary:
(i) the authentic double-resolvent/current push-forward to physical product-noise directions while preserving
signed aggregation, dual-code multiplicity, negative credits and the terminal mixed difference; or
(ii) the bound of the resulting mask bank by the retained R16 first-separation/moment budget or directly by `J(f)`.
Those are now the exact compiler-side obligations. They belong naturally to B16; B18 should integrate them once a
source-exact handoff exists.

# 6. Challenge to a putative full proof

This theorem does **not** license three common hidden assumptions.

- One may not replace the signed current by absolute relation coefficients merely to obtain a positive measure. The
  positive measure must arise after the already-required cancellations/refunds.
- `J(m_j)` is influence of a compiler mask, not influence of the original `f`; the mask bank needs an independent
  compiler identity or bound. Treating it as automatically <= `J(f)` would be circular.
- Product noise here is in the **original physical coordinate basis**. A Bernoulli law on an arbitrary q-flip basis
  does not satisfy (1.1) with the same physical budget unless a separate incidence theorem is invoked.

Thus the exact universal obstruction after this run is no longer local mask stability. It is a **signed compiler
push-forward/mask-bank inequality**.

# 7. Literature/status ledger

Fresh primary-source search on 21 September 2026 still shows unrestricted FEI open. Potapov,
arXiv:2609.21563 (18 September 2026), proves FEI for plateaued functions (sharp class constant 4) and partially bent
functions (sharp class constant 2), not all Boolean functions. González--MacManus--Pereyra,
arXiv:2606.00246 (29 May 2026), give a restriction/stopping-tree framework whose universal restriction inequality
would imply FEI but is not proved in full. Han, arXiv:2312.08271, proves
`H=O(I+sum_i I_i log(1/I_i))`, retaining the influence-profile term. I found no primary source in that search
closing unrestricted FEI. No novelty or publication-priority claim is made for the mask-resolvent formulation.

Status ledger:
- `B18-MASK-XOR-TRANSFER`: **PROVED**.
- `B18-MASK-RESOLVENT-TRANSFER`: **PROVED**.
- double inverse-noise specialization (4.1): **PROVED**.
- one-subcube bank formula (4.2): **PROVED**, using the fresh B16 one-subcube identities.
- authentic parity-current -> positive physical product-noise push-forward: **OPEN**.
- authentic mask-bank <= retained R16/moment bank: **OPEN**.
- full Friedgut--Kalai FEI: **OPEN / NOT PROVED**.

Next nonoverlapping ownership: B16 should attack the two compiler-side OPEN statements above; B18 should next test
and integrate the first source-exact push-forward or, if it fails, derive the obstruction on authentic compiler
coefficients rather than on an unconstrained parity game.
