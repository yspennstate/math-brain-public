SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B10, 2026-09-23T18:47:44Z.
attacking: the ultra-coloop rank-three survivor; preserve the heavy original hub as an independent scalar and derive a product-safe transverse/longitudinal structural receiver or a sharp obstruction, using the newest fleet02/B10 near-coloop result at an actual inequality.

# fleet01/B10 — shared-hub transverse pair volume and the entropy barrier for fully-disjoint triple Fresnel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T184744Z-fleet01-B10-QFORM-auto11`  
Status: `ESSENTIAL_STEP_APPLIED / NEW_EXACT_STRUCTURAL_IDENTITY / NEW_INFORMATION-THEORETIC_BARRIER / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
Execution: `scheduled_automation / WITHOUT_VERIFIED_BRAIN`.

The unrestricted exact-rank-three theorem and the full owner conjecture remain **OPEN / NOT PROVED / NOT DISPROVED**. No new continuity assertion is made in this run. The advance is structural: in the ultra-coloop survivor, essentially all third-order physical determinant mass sits in triples containing the heavy hub, and that mass has a dimension-free entropy/disjointness certificate on the two nonhub coordinates. At the same time, any determinant-entropy argument that insists on two completely disjoint three-coordinate bases must pay an unavoidable information-theoretic penalty tending to zero as the hub leverage tends to one. Thus the next analytic receiver should permit the two bases to share the one physical hub while keeping their transverse leaf pairs disjoint.

## 1. Fresh source state and inherited survivor


The newest Claude continuation actually read was

`yspennstate/math-open-problems@d90d878c081d95b90b874dac2690b790ef71b01b`,

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`.

It gives an additive two-mechanism decomposition for a model hub-that-sees-P situation, but explicitly leaves the general rough-law split `(SP)` open. The final anonymous manuscript checkpoint at `d2f970d33fa7084f8de55412189402ac609e4da6` likewise keeps unrestricted QFORM open.

We work in the exact-rank-three representation

`A=U M U^T`, `U^T U=I_3`, `D=|det M|>=1`,                       (1.1)

with every eigenvalue of the real symmetric invertible `M` having modulus at least one. The inherited B10 ultra-coloop state has one ORIGINAL coordinate, labelled `0`, whose spectral row is

`u_0=sqrt(h) r`, `||r||=1`,                                       (1.2)

and leaf rows

`u_i=t_i r+p_i`, `p_i perpendicular r`.                           (1.3)

Parseval gives

`sum_i t_i^2=1-h`,
`sum_i p_i p_i^T=I_(r^perp)`,
`sum_i t_i p_i=0`.                                                 (1.4)

The immediately preceding B10 run reduced the still-unpaid chamber to

`h>4095/4096`,
`tau_i:=||p_i||^2<1/4` for every leaf,
`D^2(1-h)<2^(-12)`,                                                (1.5)

along with the separate near-null scalar condition `|r^T M r|D<2^(-12)`. Only (1.4)-(1.5) are needed for the new geometry below.

## 2. Designated partner result applied at an actual inequality

The newest completed designated `fleet02/B10` theorem used here is

`QFORM-NEARCOLOOP-ONEHUB-CURRENCY-BARRIER-v1`,

at full source commit

`yspennstate/math-open-problems@bf1ec1482020bc1da89f7f888057b70269df650d`,

whose canonical report is under the fleet02/B10 fleet path for its `20260923T170933Z` run.

For every disjoint leaf split `I,J`, the one-original-hub projected-crossing currency factors as

`V_3(0;I,J)=h D^2 det(S_I) det(G_J)`,                               (2.1)

and the partner proves the sharp structural upper bound

`V_3(0;I,J)<=h D^2(1-h)`.                                          (2.2)

Apply (2.2) in the present ultra-coloop state (1.5): for **every** leaf split,

`boxed: V_3(0;I,J)<2^(-12).`                                      (2.3)

Thus no optimization of the leaf-only one-hub projected-crossing partition can produce a scale-free lower bound in this survivor. This is an inequality-level use of the designated partner theorem, not merely a citation.

The rest of this report identifies where the missing third-rank mass actually went.

## 3. The transverse pair-volume law is a probability measure

Choose an oriented orthonormal basis of the two-plane `r^perp`. For leaves `i<j`, set

`w_ij:=det(p_i,p_j)^2`.                                             (3.1)

By two-dimensional Cauchy--Binet and (1.4),

`sum_(i<j) w_ij = det(sum_i p_i p_i^T)=1`.                         (3.2)

Hence

`nu({i,j})=w_ij`                                                    (3.3)

is a probability law on unordered leaf pairs.

### Exact row marginals

For a fixed leaf `i`, let `J` denote rotation by ninety degrees in `r^perp`. Then

`det(p_i,p_j)=(J p_i).p_j`,

so using (1.4),

`sum_(j!=i) det(p_i,p_j)^2`
` =(Jp_i)^T (sum_j p_jp_j^T)(Jp_i)`
` =||p_i||^2=tau_i`.                                                (3.4)

Therefore the inclusion marginal of coordinate `i` under `nu` is exactly

`boxed: P_nu(i in B)=tau_i.`                                       (3.5)

As a check, summing (3.5) gives `sum_i tau_i=2`, the trace of the transverse Parseval identity.

This identity is stronger than a mere bound on pair volumes: the same transverse leverages that are already known to be `<1/4` are *exactly* the volume-sampling marginals.

## 4. Two transverse pair bases are disjoint with probability >1/2

Let `B,B'` be iid with law `nu`. Since two unordered pairs that intersect share either one or two coordinates,

`1_{B cap B' != emptyset} <= |B cap B'|`.

Taking expectations and using (3.5),

`P(B cap B' != emptyset)`
` <=sum_i P(i in B)P(i in B')`
` =sum_i tau_i^2`
` <=tau_* sum_i tau_i`
` =2 tau_*`,                                                       (4.1)

where `tau_*:=max_i tau_i`. Thus

`boxed: delta_perp:=P(B cap B'=emptyset)>=1-2tau_*>1/2.`           (4.2)

This is a literal original-coordinate statement. It does not rotate the random variables and does not infer independence of spectral projections. It says that the transverse two-volume can be sampled twice with a uniformly positive chance that the two samples use four distinct original leaves.

## 5. All hub-containing physical triple determinant mass is explicit

For a physical triple `S={0,i,j}`, the `3 x 3` principal block is

`A_S=U_S M U_S^T`.

Hence

`|det A_S|=D det(U_S)^2`.                                          (5.1)

Because the first row of `U_S` is `sqrt(h)r`, expansion along that row kills the longitudinal pieces `t_i r,t_j r` and gives

`det(U_{0ij})^2=h det(p_i,p_j)^2=h w_ij`.                           (5.2)

Therefore

`boxed: |det A[{0,i,j}]|=Dh w_ij.`                                (5.3)

Summing over all leaf pairs and using (3.2),

`boxed: sum_(i<j)|det A[{0,i,j}]|=Dh.`                            (5.4)

In the live chamber,

`boxed: sum_(i<j)|det A[{0,i,j}]|>4095/4096.`                     (5.5)

Compare (5.5) with the partner bound (2.3): the ultra-coloop state is **not** deficient in physical third-order determinant mass. It is deficient only for proof topologies that first force that mass into a hub-free leaf Gram. The hub-containing packet is order one.

## 6. Exact determinant-entropy currency of the shared-hub packet

The identity (5.3) has an entropy consequence. If `B~nu`, then

`H(nu)+sum_B nu_B log |det A_{0B}|`
` =H(nu)+sum_B nu_B[log(Dh)+log nu_B]`
` =log(Dh).`                                                       (6.1)

Equivalently,

`boxed: exp(H(nu)+E_nu log |det A_{0B}|)=Dh.`                      (6.2)

So arbitrary fragmentation into tiny individual physical triples causes **zero entropy loss** at the aggregate level.

We can additionally impose disjointness of the two leaf pairs without losing more than a factor two. Let

`mu = Law((B,B') | B cap B'=emptyset)`.                             (6.3)

By symmetry its two marginals agree; call the common marginal `q`. If

`alpha_i=P_(C~q)(i in C)`,

then the two pairs in a `mu`-sample are disjoint, so

`2 alpha_i=P(i in B|E)+P(i in B'|E)<=1`,

hence

`boxed: alpha_i<=1/2 for every leaf i.`                            (6.4)

Moreover

`D_KL(mu || nu tensor nu)=log(1/delta_perp)`.                       (6.5)

Data processing under projection to the first pair gives

`D_KL(q||nu)<=log(1/delta_perp)`.                                  (6.6)

Define the shared-hub physical determinant entropy

`Z_sh:=exp(H(q)+sum_B q_B log |det A_{0B}|)`.                       (6.7)

Using (5.3),

`log Z_sh=log(Dh)-D_KL(q||nu)`,                                    (6.8)

and therefore

`boxed: Z_sh>=Dh delta_perp>Dh/2>4095/8192.`                       (6.9)

This is the central constructive output of the run. There exists a probability distribution on hub-containing physical triples `{0,i,j}` such that

* the hub is present with marginal one;
* every nonhub original coordinate has marginal at most one half;
* the determinant-entropy currency is bounded below by `4095/8192`, independently of dimension, fragmentation, `1-h`, and the small Rayleigh coefficient.

The only nonstandard feature relative to the usual determinant-entropy Fourier compiler is that the one physical hub is deliberately **shared** rather than split into two disjoint source triples.

## 7. Information-theoretic barrier for fully-disjoint three-basis Fresnel

The preceding shared-hub construction suggests asking whether a more clever weighting of ordinary full three-coordinate bases could avoid sharing the hub. It cannot avoid a quantitative coloop tax.

Let

`p_S:=det(U_S)^2`, `|S|=3`.                                        (7.1)

Cauchy--Binet gives `sum_S p_S=1`; this is the projection-volume law on physical triples. From (5.2)-(3.2),

`P_p(0 in S)=sum_(i<j)h w_ij=h`.                                  (7.2)

Now let `q_3` be **any** probability law on physical triples for which every coordinate incidence marginal is at most one half:

`alpha_k:=P_(S~q_3)(k in S)<=1/2`.                                 (7.3)

This marginal condition is exactly the condition that makes the scalar `L^{1/alpha_k}` Fourier input available with exponent at least two in the weighted determinant-entropy method.

Define

`Z_U(q_3):=exp(H(q_3)+sum_S q_3(S) log p_S)`.                       (7.4)

If `q_3` charges a zero-volume triple, then `Z_U=0`; otherwise

`Z_U(q_3)=exp(-D_KL(q_3||p))`.                                     (7.5)

Apply data processing to the indicator `1_{0 in S}`. Under `p` it is Bernoulli(`h`), while under `q_3` it is Bernoulli(`alpha_0`) with `alpha_0<=1/2`. Since `h>1/2`, the Bernoulli relative entropy is minimized over `alpha_0<=1/2` at `alpha_0=1/2`. Therefore

`D_KL(q_3||p)`
` >= d_Bern(alpha_0 || h)`
` >= d_Bern(1/2 || h)`
` =-(1/2) log(4h(1-h)).`                                           (7.6)

Combining (7.5)-(7.6),

`boxed: Z_U(q_3)<=2 sqrt(h(1-h)).`                                 (7.7)

For physical principal determinants `|det A_S|=D p_S`, the corresponding currency is

`Z_A(q_3):=exp(H(q_3)+sum_S q_3(S)log|det A_S|)=D Z_U(q_3)`,        (7.8)

so

`boxed: Z_A(q_3)<=2D sqrt(h(1-h)).`                               (7.9)

In the current ultra-coloop chamber `D^2(1-h)<2^(-12)`, this implies

`boxed: Z_A(q_3)<1/32.`                                            (7.10)

More importantly, along valid coloop limits with bounded `D`, the right side of (7.9) tends to zero. Thus no optimization of the ordinary *fully-disjoint three-basis determinant-entropy architecture* can turn the order-one packet (5.5) into a uniform currency: the requirement `alpha_0<=1/2` itself forces a KL penalty because the true volume law places mass `h->1` on triples containing the hub.

This is a proof-method obstruction, not a QFORM counterexample. It does not rule out a different Fourier, coarea, or real-variable argument.

## 8. Why this changes the next analytic target

The new geometry sharply separates two facts:

1. Full-disjoint triple sampling is intrinsically ill-conditioned in the coloop limit by (7.9).
2. Shared-hub transverse-pair sampling is uniformly well-conditioned: it has leaf marginals at most one half and determinant entropy `Z_sh>4095/8192` by (6.9).

The newest completed mixed-basis triple-Fresnel theorem (`yspennstate/math-open-problems@3d991ad3ab91593155b0b465007f4938968a14bf`) explains the exact remaining analytic issue. Its weighted Brascamp--Lieb step can spend coordinates whose incidence marginals are at most one half, but a hub present in every basis has incidence one and would demand a scalar Fourier `L^1` input, which is false for arbitrary cap-one laws. The live phase-Wiener correction forbids hiding this loss inside an absolute Fourier integral.

At the exact-null boundary, fleet03/B10's completed theorem

`QFORM-NULL-HUB-TRANSVERSE-LEVERAGE-CLOSURE-v1`,

source `yspennstate/math-open-problems@dc9d69f51688728122da9fd35835593beaa694c7`,

shows how special null shear/Fresnel structure overcomes precisely this shared-hub difficulty and gives

`||p_Q||_infinity<=3*2^(4/3)(hD)^(-1/3)`                           (8.1)

with a continuous density. What remains in the punctured collar is to make that hub treatment stable for nonzero Rayleigh coefficient without dividing by the small scalar pivot.

The newest Claude continuation `d90d878...` reaches the same qualitative frontier from the real-variable side: a hub that sees the auxiliary projection needs a combination of spread and parabola-incidence mechanisms; the general rough-law split is still open. The new certificate (6.9) supplies a quantitative product-frame object for that missing receiver.

## 9. First unpaid implication after this run

The next precise target is

`QFORM-SHARED-HUB-PAIR-ENTROPY-RECEIVER-v1`:

> Let an exact-rank-three physical form have one original hub `0` and suppose there is a probability law `q` on leaf pairs such that every leaf incidence marginal is at most `1/2` and
> `exp(H(q)+E_q log|det A_{0ij}|)>=zeta>0`.
> Prove a dimension-free density bound depending only on `zeta` (and universal constants), while allowing the same physical hub to occur in every determinant basis, arbitrary cap-one hub law, arbitrary signs, arbitrary within-leaf curvature, and arbitrary affine terms arising from conditioning.

For the entire B10 ultra-coloop survivor, the present theorem gives the uniform input

`zeta>4095/8192`.                                                   (9.1)

A receiver of this scope would therefore close the remaining B10 collar without any reciprocal local-minor selection and without treating small deterministic coefficients as small random errors.

## 10. Scope and status

Proved this run:

`QFORM-TRANSVERSE-PAIR-VOLUME-LAW-v1`: equations (3.2)-(4.2).

`QFORM-SHARED-HUB-TRIPLE-ENTROPY-v1`: equations (5.3)-(6.9), including the explicit live constant `4095/8192`.

`QFORM-FULLY-DISJOINT-TRIPLE-ENTROPY-COLOOP-BARRIER-v1`: equations (7.6)-(7.10).

Applied designated partner theorem: equations (2.2)-(2.3).

Not proved: the shared-hub analytic receiver in Section 9, arbitrary exact rank three, the full three-large-eigenvalue conjecture, or full-target continuity.

All random-coordinate independence claims in the proof refer only to literal disjoint original-coordinate banks. The pair-volume and entropy arguments themselves are deterministic coefficient identities and finite probability-law calculations on index sets.

## 11. Publication integrity

Prepublication controls and corrections were refreshed after the substantive derivation. Changed-file allowlist for this run is restricted to this fleet01/B10 run directory in `math-open-problems` and the corresponding fleet01/B10 handoff/memory/status files in `math-research-brain`. No task, cadence, enabled/paused state, email/push setting, public repository status, workflow, credential, permission, or unrelated data was changed. Repository use is not native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
