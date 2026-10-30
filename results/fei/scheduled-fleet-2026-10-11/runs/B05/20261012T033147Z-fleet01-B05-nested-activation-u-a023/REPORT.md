# B05 / A023 — retained `U` credit for a fresh nested rare activation

**Run:** `20261012T033147Z-fleet01-B05-nested-activation-u-a023`  
**Primary packet:** A023, amortized rarity budget  
**Stable gap:** `B05_RARE_REFUNDS`  
**Status:** scoped theorem author-proved, independent A087/A094 review pending; full FEI remains **OPEN**.

## 1. Exact target and previous status

The independently accepted A023 baseline pays the complete `L+Q` positive
credit for arbitrary finite disjoint products of point defects with constant
24.  It does not allow an arbitrary terminal Boolean core and it does not
specialize the newer upper-set potential

\[
 U(f)=\sum_S\widehat f(S)^2\log_2\frac{\pi_f(S)}{\widehat f(S)^2},
 \qquad \pi_f(S)=\sum_{T\supseteq S}\widehat f(T)^2,
\]

where the empty set is included.

This run freezes one new proposition: put an arbitrary Boolean terminal core
behind a fresh depth-`d` rare conjunction, reveal the controls first, retain
the terminal `U` packet exactly once, and bound the complete **signed** control
charge by unused physical control influence with a constant independent of
`d`, the activation probability, the core dimension, and the core spectrum.

## 2. PROVED theorem

Let `g:{-1,1}^n->{-1,1}` be arbitrary, let

\[
 r=\Pr[g=-1],\qquad \mu=\mathbb E g=1-2r,
\]

and let `a` be the indicator of one fixed point of a fresh `d`-cube,
`d>=1`, with `p=2^{-d}`.  On disjoint control and data variables define

\[
 F(z,x)=1-2a(z)\frac{1-g(x)}2.
\]

Thus `F=1` off the unique active control point and `F=g` on it.  Define

\[
 M(t)=(1-2t)^2\log_2\frac1{(1-2t)^2},
\]

with the continuous convention `M(1/2)=0`.  Then

\[
\boxed{
\begin{aligned}
U(F)={}&M(pr)+2rpd+p[U(g)-M(r)]\\
 &+4pr^2\log_2\frac1r
 -4p^2r^2\log_2\frac1{pr},\\
I(F)={}&pI(g)+2rpd.
\end{aligned}}
\tag{2.1}
\]

Reveal the `d` controls in any deterministic order, stop immediately at the
inactive constant child, and stop at `g` after all controls are active.  If
`w_v` is the physical reach probability and `i_v` the queried control, then

\[
\boxed{
 \mathcal C_d:=\sum_v w_v\Delta_{i_v}U(F_v)
   =U(F)-pU(g)
   \le C_* I_{\rm ctl}(F),
}\tag{2.2}
\]

where

\[
 I_{\rm ctl}(F)=2rpd,
 \qquad C_*=1+\frac{2(1+e^{-1})}{\ln2}<4.947.
\tag{2.3}
\]

Every control coordinate is fresh and its physical influence is used once.
The terminal packet is retained with its exact reach weight `p`; no hypothesis
on `U(g)/I(g)` is made.  The theorem therefore remains noncircular even when
`g` is a hypothetical hard FEI core.

Equivalently, if a class of terminal cores obeys `U(g)<=K I(g)`, then its fresh
rare suspensions obey

\[
 U(F)\le \max\{C_*,K\}I(F).
\tag{2.4}
\]

The quantifiers cover every finite terminal dimension, every Boolean terminal
truth table, every depth `d>=1`, every active control point, and every control
order.  Mixed nested fresh activation blocks collapse to the same single
point in the union of their controls, so their individual activation scales
are also covered.

## 3. Exact complete signed node charge

Let `F_m` denote the same construction with `m` unrevealed controls and put
`p_m=2^{-m}`.  At its unique continuing node the inactive child is constant
and the active child is `F_(m-1)` (with `F_0=g`).  Direct specialization of

`Delta_i U = B_i - Gamma_i + KL_i`

gives the complete signed charge

\[
\boxed{
\begin{aligned}
\delta_m:=\Delta_iU(F_m)
={}&M(p_mr)-\tfrac12M(2p_mr)+2p_mr\\
 &+4p_m^2r^2\left(\log_2\frac1{p_mr}-2\right).
\end{aligned}}
\tag{3.1}
\]

The remarkable point is what is absent: neither `U(g)` nor any nonconstant
Fourier coefficient of `g` occurs.  The `B_i` rare logarithm, `Gamma_i`
refund, and KL asymmetry term have combined into a scalar depending only on
`r`.  The physical reach-weighted charges telescope exactly:

\[
 \sum_{m=1}^d2^{m-d}\delta_m=U(F_d)-2^{-d}U(g).
\tag{3.2}
\]

This is the requested single-use refund: the arbitrary coherent core is
transported to the terminal leaf rather than recharged once per ancestor.

## 4. Proof of the exact identity

Put `q=(1-g)/2`, and write `alpha_R=hat a(R)`, `beta_T=hat q(T)`.  For every
nonempty pair `(R,T)`,

\[
 \widehat F(R,T)=-2\alpha_R\beta_T.
\]

If

\[
 A_R=\sum_{R'\supseteq R}\alpha_{R'}^2,
 \qquad Q_T=\sum_{T'\supseteq T}\beta_{T'}^2,
\]

then every upper set above a nonempty `(R,T)` avoids the exceptional empty
coefficient, and hence

\[
 \pi_F(R,T)=4A_RQ_T.
\]

The empty coefficient is `1-2pr` and contributes exactly `M(pr)`.  Summing
the two logarithms over all pairs and subtracting the excluded empty pair
gives

\[
 U(F)=M(pr)+4\{rU_*(a)+pU_*(q)-p^2r^2\log_2(1/(pr))\},\tag{4.1}
\]

where `U_*(h)=sum_R hat h(R)^2 log_2(H_R/hat h(R)^2)` for a real function.
For a one-point indicator,

\[
 U_*(a)=I(a)=\frac{pd}{2}.
\]

For `q=(1-g)/2`, the nonempty Fourier coefficients are `-hat g(T)/2`, while
the empty coefficient is `r`; therefore

\[
 U_*(q)=\frac14[U(g)-M(r)]+r^2\log_2(1/r).
\]

Substitution proves the first line of (2.1).  Parseval on the two disjoint
blocks gives

\[
 I_{\rm data}(F)=pI(g),\qquad
 I_{\rm ctl}(F)=4rI(a)=2rpd,
\]

proving the second line.  Equation (3.1) follows by subtracting
`U(F_(m-1))/2` from `U(F_m)`; (3.2) is then the ordinary physical restriction
telescope.

## 5. Uniform retained-credit bound

From (2.1), dropping only nonpositive terms,

\[
 \mathcal C_d\le M(pr)+I_{\rm ctl}(F)+4pr^2\log_2(1/r).
\]

For `0<=x<=1/2`, set `y=1-2x`.  The elementary inequality
`-ln y <= (1-y)/y` yields

\[
 M(x)=\frac{-2y^2\ln y}{\ln2}\le\frac{4x}{\ln2}.
\]

Also `r log_2(1/r)<=1/(e ln2)`.  Dividing the two remaining positive terms by
`I_ctl=2rpd` gives respectively `2/(d ln2)` and
`2/(de ln2)`.  This proves (2.2)-(2.3).  The cases `r=0`, `r=1`, and
`pr=1/2` follow by the displayed continuous conventions.

## 6. Case extension and falsifier controls

| Item | Prior coverage | New coverage / outcome |
|---|---|---|
| Terminal core | Point-defect factors in a complete `L+Q` product packet | Every genuine Boolean `g`; its full `U(g)` is retained once |
| Activation depth/probability | Arbitrary defect dimensions, but scalar product cores | Every `d>=1`, `p=2^-d`, and every grouping of fresh nested activation blocks |
| Constant | 24 for the accepted disjoint point-defect `L+Q` theorem | `C_*<4.947` for the signed `U` control charge |
| Sparse defect | Covered, including `g` constant `-1` | Formula specializes correctly and keeps the empty coefficient |
| Near tensor / spectators | Disjoint products accepted | Arbitrary spectator structure may live inside `g`; charged only at the terminal |
| Addressing | Not covered globally | An arbitrary addressing core may be terminal, but `pU(g)` remains unpaid; this is not addressing closure |
| Shared variables | Not covered | Fresh disjoint controls are essential |
| Changing coherent cores | Not covered | Different cores at different ancestors do not collapse to one `g`; this is the first unsupported line |

The theorem is strictly broader in terminal-core complexity, while narrower
in its fresh-control geometry.  It does not prove a bound for arbitrary
hierarchies and does not solve FEI.

## 7. Verification

Command:

`python3 verify_nested_activation.py`

Observed result: **PASS**, 6,275 assertions, no randomness.  The checker
exhausts all Boolean terminal cores through three variables, adds 37
deterministic structured four-variable terminals, and tests depths 1 through
5.  It independently verifies direct Walsh computation of `U(F)`, (2.1), the
node telescope (3.1)-(3.2), the influence formula, and the analytic constant.
The largest observed signed-charge/control-influence ratio was
`2.234955531214230` at depth one and `r=3/8`; the proved constant is
`4.946865772624014`.  Floating logarithms make this a transcription check,
not the all-parameter certificate; the written proof is analytic.

## 8. Movement, exact remaining gap, and next action

**Previous status:** the newer `U` route had one-node rare-log cancellation,
while the accepted A023 theorem handled only point-defect products in a
different complete packet.  No result transported an arbitrary Boolean core
through an unbounded fresh rare hierarchy with a depth-independent signed
`U` charge.

**New status:** for the declared fresh nested activation family,

\[
 \frac{\sum_vw_v\Delta_{i_v}U(F_v)}{I_{\rm ctl}(F)}<4.947
\]

for every depth and activation probability, and the arbitrary terminal packet
is exactly `pU(g)`.

**First unsupported line:** allow the active core to change with the ancestor
(or reuse a control/data coordinate) and prove a distribution-valued analogue
of (4.1) whose interference terms have single-use physical ownership.  The
next attempt should treat two nested fresh activations with distinct cores
`g_0,g_1` and isolate the coherent cross term before considering arbitrary
depth.  Whole-set addressing and bent-core surgery remain mandatory
falsifiers.

## 9. Sources and status distinctions

- Owner overlay: `math-research-brain` commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`,
  `scheduled_tasks/work/shared/full-fei-only-2026-10-12/ORDER.md` and
  `CASE_TARGETS.json`, control revision `2026-10-12.1`.
- `U` source: `<private-repo>`,
  `12_cognitive_architecture/math/fei_campaign_2026_10/opus/U-universal/NOTES.md`,
  source blob `5797e9cc38598cbee391cc99d4b1abcd554b662e`; in particular Theorem U-loc.
- Accepted prior A023 theorem: author commit
  `9ddbf20daf52b3939ef6cd277677ee380ba993da`; independent B19 review commit
  `34a9fd4b50f25c67c132c663f4b5edfd11027589`.
- Current B05 contract blob `05447e6d999437bb82a266b427bd76a4b37266b6`;
  execution protocol revision `2026-10-11-execution-v2`.

No external novelty or priority claim is made.  Model: Codex as exposed by
this run; separate model-version and reasoning-effort metadata were not
exposed.  Subagents: none.  Scheduler/graph mutation: none.  Native Brain
ingestion: not claimed.  Full FEI: **OPEN**.

