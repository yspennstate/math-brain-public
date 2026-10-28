TASK: B17 ACCOUNT: account02 RUN: 2026-09-21T23:12:40.164645Z — recursive-majority global-code obstruction and nested branch-surplus coding

MODEL SELF-REPORT: GPT-5.6 Sol
REQUESTED REASONING: maximum actually supported
CONFIGURED / KNOWN REASONING LEVEL: UNKNOWN / NOT_EXPOSED
PROVIDER REASONING USAGE: null / NOT_EXPOSED
BRAIN STATUS: WITHOUT_VERIFIED_BRAIN
STATUS: PARTIAL. Full uniform-cube Friedgut–Kalai Fourier entropy-influence conjecture remains OPEN / NOT PROVED.
NOVELTY / PRIORITY: NOT CLAIMED.

Fresh authenticated control at entry:
`yspennstate/math-research-brain` main
`7bf9a36976d5708320c5d6416a59be71bd627a7f`,
The later shared execution reset
was also read and applied. It assigns account02/B17 to Campaign B as principal adversary for the
common Shannon/harmonic/code inequality, superseding the stale prompt-level emphasis on the
harmonic-Riesz row bridge. Live allocation remains 8 brain B01-B06/B19-B20, 5 benchmark
B07-B11, 7 FEI B12-B18.

Fresh scientific master at entry:
`yspennstate/math-open-problems`
`419ae5558d869ab8298f825fe33c5ecdd1b4ebda`.
It advanced during the run through ordinary peer work; the scientific work below is source-bound
to the exact reports named in §1.

Normalization:
`f:{-1,+1}^n->{-1,+1}`, normalized Walsh transform,
`p_S = fhat(S)^2`,
`H(f)=sum_S p_S log2(1/p_S)`,
`I(f)=sum_S |S| p_S`.
For a spectral sample `S`, write `K=|S|`, `p_i=Pr(i in S)`,
`q_i=p_i/I`.

## 0. Last-three comparison

The last three completed substantive account02/B17 reports before this run are:

1. `20260921T204329Z-interaction-companion-factorization`:
   tensor amplification showed a global harmonic residual is FEI-hard; exact plaquette
   components and a physical skeleton replaced the global payment.
2. `20260921T215432Z-selector-phase-low-plaquette`:
   an address-only Boolean phase destroyed exact physical factorization without changing the
   squared spectrum; low-cross-plaquette approximate multiplicative factorization replaced it.
3. `20260921T224419Z-affine-parity-straightening`:
   connected quadratic cycles made every coordinate-subcube row exceptional despite `M/J=1`;
   invertible affine-parity straightening replaced axis-aligned robustness.

FULL-PROBLEM CHANGE: none. No finite universal FEI constant is proved.

MECHANISM CHANGE: yes. The live 23:06Z execution reset explicitly moved this worker to Campaign B.
This run therefore leaves physical derivative-row geometry and attacks the common spectral code
itself. The strongest one-level code is refuted by an actual recursive Boolean family, and a
different *nested/local* code is proved in the same run.

FLEET_RULES moves used:
- #2 ATTACK THE NEGATION FIRST: test the global code on recursive majority before trying to prove it.
- #18 SAY IT IN ANOTHER LANGUAGE: replace global coordinate names by ancestral branch names.
- #25 COUNT THE SAME THING TWICE: telescope local child surplus to the exact global quantity `I-tau`.

## 1. Named completed other-account result consumed

The main consumed result is:

`account03/B12/20260921T224810Z-local-factorial-hierarchy/REPORT.md`
(blob `96737b71a9bb921b9dbae1051844314a5e96bfbc`).

That report refines the earlier account03/B12 spectral compression theorem. The inherited
one-level ordered-set envelope is

    H(S) <= U(S)
         := H(K) + I H(q) - E log2(K!).                    (1.1)

The newer hierarchy splits the factorial credit into internal and macroscopic pieces and proves
that robust reciprocal internal entropy can be paid by the internal factorial term, leaving a
macroscopic residual. The report explicitly does *not* prove the macro bridge.

I apply (1.1) directly below and use the newer report's central lesson — preserve factorial
credit at the scale on which labels are introduced — to build the replacement after the
one-level bridge fails.

The post-reset Campaign-B lead requested from account03/B18 was not yet present in the refreshed
account03/B18 directory inspected during this run; the newest visible B18 item was
`20260921T230034Z-character-parent-gauge-null`, which predates the 23:06 reset and belongs to the
older parent/gauge interface. Per the reset order, I therefore reconstructed the smallest explicit
Campaign-B candidate from the completed B12 chain instead of waiting.

## 2. PROVED BOOLEAN ADVERSARY: recursive ternary majority refutes every finite one-level CFC constant

Let

    M(x1,x2,x3) = Maj_3(x1,x2,x3)
                = (x1+x2+x3-x1 x2 x3)/2.

Its squared Fourier law is uniform on the four nonempty sets

    {1}, {2}, {3}, {1,2,3}.                              (2.1)

Thus `H(M)=2` and `I(M)=3/2`.

Define recursively `M_0(x)=x` and, for `d>=1`,

    M_d = M(M_{d-1}^{(1)}, M_{d-1}^{(2)}, M_{d-1}^{(3)}), (2.2)

on three disjoint copies at every node. Every `M_d` is a genuine balanced Boolean common
potential on `3^d` leaves.

### 2.1 Exact spectral Galton–Watson law

A spectral sample from `M_d` is generated down the ternary composition tree as follows. Every
active node independently has

    X=1 with probability 3/4,
    X=3 with probability 1/4,                             (2.3)

and in the `X=1` case its unique active child is uniform among the three children.

Let `K_d` be the number of active leaves. Its offspring mean is

    m = E X = 3/2,

so

    I_d := E K_d = (3/2)^d.                               (2.4)

By transitivity of the leaves,

    p_i = I_d/3^d = 2^{-d},

hence the normalized influence profile `q` is uniform on all `3^d` leaves and

    H(q)=d log2 3.                                        (2.5)

Also `E[X(X-1)]=3/2`. The standard branching recurrence gives

    E K_{d+1}^2
      = m E K_d^2 + E[X(X-1)](E K_d)^2
      = (3/2) E K_d^2 + (3/2) I_d^2.

With `K_0=1`, induction yields the exact closed form

    E K_d^2 = 2 I_d^2 - I_d.                              (2.6)

### 2.2 The actual FEI ratio remains bounded

Because all inner blocks are balanced, the Fourier composition law is injective across labelled
blocks. Therefore

    H_d = 2 + (3/2) H_{d-1},  H_0=0,

so exactly

    H(M_d)=4((3/2)^d-1)=4(I_d-1).                         (2.7)

Consequently

    H(M_d)/I_d = 4(1-I_d^{-1}) < 4,

and the ratio tends to 4. This family is emphatically **not** an FEI counterexample.

### 2.3 The one-level ordered code diverges

Apply (1.1) to `M_d`:

    U_d = H(K_d) + I_d d log2 3 - E log2(K_d!).           (2.8)

Using `log2(k!) <= k log2 k` and dropping the nonnegative `H(K_d)`,

    U_d/I_d
      >= d log2 3 - E[K_d log2 K_d]/I_d.                  (2.9)

Under the size-biased law `Pr*(K=k)=k Pr(K=k)/I_d`,

    E[K_d log2 K_d]/I_d = E* log2 K_d
      <= log2(E* K_d)
      = log2(E K_d^2/I_d)
      = log2(2I_d-1),                                     (2.10)

by Jensen and (2.6). Hence

    boxed:
    U_d/I_d >= d log2 3 - log2(2(3/2)^d-1) > d-1.         (2.11)

Therefore

    U_d/I_d -> +infinity.                                 (2.12)

This proves that the universal bridge

    H(K)+I H(q)-E log2(K!) <= beta I                      (CFC_beta)

is false for **every finite beta**, even on the actual balanced Boolean family `M_d`.

At depth 7 the checker gives

    H/I = 3.7658893461...,
    U/I = 7.9237002544...,
    rigorous lower bound from (2.11) = 6.0428488491....

The obstruction is precise: a one-level code pays `d log2 3` leaf-address bits per expected
spectral occurrence; the single global factorial cancellation removes only about
`d log2(3/2)` bits, leaving asymptotically one unpaid bit per recursive scale.

Again, this refutes a stronger bridge, not FEI.

## 3. Replacement mechanism: nested ordered coding on a coordinate partition tree

The failure in §2 says that labels must be introduced and factorial-cancelled at the same scale.

Let `T` be any rooted tree whose leaves are the coordinates `[n]`; every internal node `v`
corresponds to the disjoint union `C_v` of the leaf sets below its children.

For a spectral sample `S`, define

    A_v = 1{S intersects C_v},
    tau_v = Pr(A_v=1).

Conditional on `A_v=1`, let

    Y_v = {u child of v : A_u=1},
    D_v = |Y_v|,
    mu_v = E[D_v | A_v=1].

For a child `u` of `v`, put

    r_{v,u}=Pr(A_u=1 | A_v=1),
    q_{v,u}=r_{v,u}/mu_v.

Then `sum_u q_{v,u}=1`. Define the local ordered envelope

    U_v :=
      H(D_v | A_v=1)
      + mu_v H(q_v)
      - E[log2(D_v!) | A_v=1].                            (3.1)

### Theorem 3.1 — hierarchical ordered-code lemma

For every random subset `S` of `[n]` and every rooted coordinate partition tree `T`,

    boxed:
    H(S) <= h2(tau_root) + sum_{v internal} tau_v U_v.    (3.2)

#### Proof

The leaf subset `S` is in bijection with:
1. the root-activity bit; and
2. for every active internal node, the nonempty active-child subset `Y_v`.

By the Shannon chain rule, the entropy of this hierarchical record is at most the root bit
entropy plus the sum, weighted by the probability that a node is active, of the marginal
conditional entropy `H(Y_v | A_v=1)`.

Apply the account03/B12 ordered-set inequality (1.1) locally to the nonempty subset `Y_v`.
Its mean size is `mu_v`, normalized inclusion profile is `q_v`, and factorial term is
`E log2(D_v!)`. Therefore `H(Y_v|A_v=1)<=U_v`. Summing proves (3.2). QED.

### Theorem 3.2 — exact branch-surplus conservation

For every such `S,T`,

    boxed:
    sum_{v internal} tau_v(mu_v-1) = I - tau_root.        (3.3)

#### Proof

For each internal node,

    tau_v mu_v = sum_{u child of v} tau_u.

Therefore the left side is

    sum_{v internal}(sum_{u child of v}tau_u - tau_v).

All internal nonroot terms cancel. The remaining positive terms are the leaf activities
`sum_i tau_i=sum_i p_i=I`; the remaining negative term is `tau_root`. QED.

Thus the exact global payment bank `I-tau_root` is already decomposed scale by scale in the
same hierarchy that introduces the labels.

## 4. The replacement survives the recursive-majority adversary

Use the natural ternary composition tree for `M_d`.

Conditional on an active node, its child subset is exactly the four-point law (2.1). Thus

    D=1 with probability 3/4,
    D=3 with probability 1/4,
    mu=3/2,
    q=(1/3,1/3,1/3).

The local ordered envelope is the constant

    U_0
      = h2(1/4) + (3/2)log2 3 - (1/4)log2 6
      = 2.542481250360578...                              (4.1)

and local branch surplus is `mu-1=1/2`. Therefore the local code/surplus ratio is

    C_Maj = 2 U_0
          = 5.084962500721156....                         (4.2)

The expected number of active internal nodes through depth `d-1` is

    sum_{t=0}^{d-1}(3/2)^t = 2(I_d-1).

Hence (3.2) on this natural tree gives

    H(M_d)
      <= 2 U_0 (I_d-1)
      < 5.084963 I_d,                                     (4.3)

uniformly in depth.

At depth 7 the nested code has ratio `4.7873515267...`, while the global one-level envelope has
ratio `7.9237002544...`. The nested ratio tends to `5.0849625007...` instead of diverging.

So the mechanism that kills `(CFC_beta)` does **not** kill the hierarchical replacement.

## 5. Tensor and balanced-composition sanity

### 5.1 Tensor products

For `r>=2` balanced tensor factors, choose a root whose `r` children are the factor blocks.
Every factor spectrum is nonempty, so the root active-child set is deterministically all `r`
blocks. Its local cost is

    U_root = r log2 r - log2(r!).                         (5.1)

Using `r! >= (r/e)^r`,

    U_root <= r log2 e <= 2 log2(e)(r-1).                 (5.2)

Thus the hierarchical code introduces only a dimension-free overhead per root branch surplus.
Inside each block one reuses the factor's own hierarchy. This passes the execution-reset tensor
stress test that destroyed several global bridges.

### 5.2 Exact balanced-composition closure for the code functional

Let a balanced outer Boolean function `g` be composed with balanced Boolean functions `f_j`
on disjoint blocks. Choose a hierarchy whose root children are those blocks and whose subtrees are
hierarchies for `f_j`.

Because every inner spectral sample is nonempty, the root active-block subset is exactly the
outer spectral sample. Therefore the hierarchical ordered cost decomposes as

    C_T(g(f_1,...,f_r))
      = U(g) + sum_j p_j(g) C_{T_j}(f_j),                 (5.3)

where `U(g)` is the one-level ordered envelope of the outer spectral law and `p_j(g)` is the
outer spectral inclusion probability of block `j`.

The branch surplus decomposes identically:

    I(g(f_1,...,f_r))-1
      = (I(g)-1) + sum_j p_j(g)(I(f_j)-1).                (5.4)

Hence, if `U(g)<=C(I(g)-1)` and each subtree obeys
`C_{T_j}(f_j)<=C(I(f_j)-1)`, then the composition obeys the same constant `C`.

This is a statement about the new code functional, not a new claim of FEI-composition priority.
O'Donnell–Tan already established a general FEI composition theorem in 2013; their work is
therefore prior art for the composition architecture even though the nested ordered-code
functional here is different.

### 5.3 Biased control

The earlier account03/B12 spectral-compression report already checked the canonical one-point
defect family and found the *star/global* ordered envelope bounded (asymptotic reported ratio
about `4.4427`). The hierarchical optimum is no worse than the star tree, so the replacement
inherits that biased control. This run does not reannounce that calculation as new work.

## 6. New universal target and exact remaining obstruction

Define

    Code_T(f)
      := h2(tau_root) + sum_{v internal} tau_v U_v.       (6.1)

Theorem 3.1 says `H(f)<=Code_T(f)` for every tree.

A direct universal bridge would be:

    TREE-CODE:
    for every Boolean f there exists a source-admissible coordinate partition tree T
    such that
        Code_T(f) <= C_tree I(f)                          (6.2)

for one finite dimension-independent `C_tree`.

For balanced `f`, `tau_root=1`, so the sharper branch-surplus formulation is

    sum_v tau_v U_v <= C_tree (I(f)-1).                   (6.3)

Combined with the standard one-bit balanced suspension, any universal finite constant in (6.3)
would imply full FEI.

The exact remaining obstruction is **singleton routing**. In an arbitrary subset law a node can
have `D_v=1` almost surely while the identity of the unique child has large entropy. Then its
local branch surplus is zero although its label entropy is positive. Therefore no proof of
(6.3) can hold for arbitrary random subset laws.

Booleanity must rule out or amortize this phenomenon. At the global level, an exactly
degree-one Boolean function is only a constant/dictator, so an exact high-entropy random
singleton spectrum is impossible. But conditional node laws in an arbitrary hierarchy are not
themselves automatically Boolean spectra. The missing universal theorem is therefore a
dimension-free *Boolean hierarchical singleton-routing/stability lemma* that chooses the tree
adaptively and transfers near-zero local excess degree into either:
- a near-dictator/character certificate with cheap routing, or
- paid excess degree / negative conditional-information credit at an ancestor.

This is now the named Campaign-B implication. Recursive majority shows why a one-level proof
cannot work; the nested tree shows the same adversary is compatible with a constant local budget.

## 7. Exact checker

`verify_recursive_majority_hierarchical_code.py` was executed.

It checks:
- recursive majority depths 1 through 7;
- exact rational identities `I_d=(3/2)^d`, `E K_d^2=2I_d^2-I_d`,
  and the analytic entropy recurrence;
- numerical global and nested code diagnostics;
- exhaustive Boolean functions through `n<=3` modulo global negation (138 functions),
  with exact Walsh/Fraction arithmetic for branch-surplus telescoping and a hierarchical
  true-local-entropy code check.

Result: PASS.

Checker SHA-256:
`b644e7c34ae599017c72cf711421360032868bf17753a9584b615ff27b7dc580`

Output SHA-256:
`066ef39c93f376024ec0f96465d8afe8cc343521f7c90f6e9413267969447f88`

The finite checks validate only their stated implementation scope. Theorems 3.1 and 3.2 and the
recursive-majority obstruction are proved analytically above.

## 8. Literature/applicability check

Fresh web checks on 2026-09-21 recovered:
- Ryan O'Donnell and Li-Yang Tan, *A composition theorem for the Fourier Entropy-Influence
  conjecture*, arXiv:1304.1347 (2013): established FEI composition for disjoint inner functions
  under a biased-outer hypothesis and read-once bounded-arity formulas.
- Vladimir N. Potapov, arXiv:2609.21563, submitted 2026-09-18: FEI for Boolean plateaued
  functions, sharp class constant 4, and partially bent functions with sharp class constant 2.
- González, MacManus, Pereyra, arXiv:2606.00246, 2026-05-29: restriction/stopping-tree classes
  and an induction framework, not a universal FEI proof.

The retrieved 2026 class papers do not claim the full universal conjecture. A bounded search
does not establish novelty or priority for the nested-code formulation, and no such claim is made.

## 9. Before / after and next attack

Before this run:
- Campaign-B had a strong one-level ordered code `U=H(K)+I H(q)-E log K!`;
- account03/B12 had begun local factorial splitting but the global bridge remained tempting;
- no B17 source-bound recursive-majority refutation of every finite one-level constant was in
  the inspected handoffs.

After this run:
- the global one-level CFC bridge is **rigorously refuted for every finite constant** by actual
  balanced Boolean recursive majority;
- the same family has true FEI ratio `<4`, isolating the failure to the proof bridge;
- a general hierarchical ordered-code theorem and exact branch-surplus telescoping identity are
  proved;
- the replacement is tensor-stable at the root and composition-stable for balanced disjoint
  compositions;
- recursive majority receives the explicit dimension-free nested constant
  `5.084962500721156...`.

FULL-PROBLEM CHANGE: none. Full FEI remains OPEN / NOT PROVED.

MECHANISM CHANGE: yes. The next decisive attack is not another global code inequality. It is to
prove or break the Boolean hierarchical singleton-routing/stability lemma in §6 using actual
Boolean functions, with recursive majority, biased defects, tensors, and a near-dictator family
as mandatory adversaries. A non-Boolean random-singleton obstruction is only a warning and is
not a counterexample to the Boolean target.
