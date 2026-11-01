TASK: B17 ACCOUNT: fleet02 RUN: 2026-09-21T14:40:20.429200Z — quadratic-leaf peeling, articulation obstruction, and a folded-slack core reduction

Status: PARTIAL. Full Friedgut–Kalai Fourier entropy-influence (FEI) conjecture remains OPEN / NOT PROVED.
Brain status: WITHOUT_VERIFIED_BRAIN.
Role: FEI new proof mechanisms.
Live sprint scope: fleet02/B17, support-deficit transfer and its actual sharp obstruction.
Scientific source at entry: yspennstate/math-open-problems master 7572f80714866112f28fbfedc1f4c1c8696601bd.
Normalization: Boolean values ±1 on the uniform cube; normalized Walsh coefficients; base-2 spectral entropy
    H(f)=sum_S fhat(S)^2 log2(1/fhat(S)^2),
and total influence
    I(f)=sum_i Inf_i(f)=sum_S |S| fhat(S)^2.

FLEET_RULES moves executed this run, deliberately different from the preceding support-deficit run:
- #18 SAY IT IN ANOTHER LANGUAGE: pass from restriction debt to the algebraic-normal-form phase polynomial P with f=(-1)^P.
- #20 FIND WHY THE ALGORITHM FAILS: attack the tempting articulation/max-parent decomposition before trying to prove it.
- #30 ONE SCALE / ONE DIRECTION AT A TIME: isolate one quadratic ANF leaf and derive its exact entropy/influence transfer before considering a whole interaction core.

## 1. What changed

The preceding fleet02/B17 run reduced a bad equal-density restriction step to a constant influence charge plus one half of the physical boundary of the pivotal set. Its remaining universal gap was to pack those second-order boundary debts without repeatedly charging the same influence.

This run isolates a substantial part of that second-order geometry which can be removed exactly: **quadratic leaf fringes in the algebraic normal form**.

For a Boolean phase f=(-1)^P, suppose a variable x occurs in exactly one nonlinear ANF monomial and that monomial is the quadratic term tx. Then, after an irrelevant linear-character twist in x, f has the exact form

    G(t,x,z) = F(t,z) (-1)^(t x).

Write the folded influence
    j_i(f)=min(Inf_i(f),1-Inf_i(f)),
    J(f)=sum_i j_i(f).

For every C and every Boolean F I prove the exact folded-slack transfer

    [C J(G)-H(G)] - [C J(F)-H(F)]
      = C(1-j_t(F)) - 2 + Delta_t H(F),                 (1.1)

where
    Delta_t H(F)=H(F)-[H(F_{t=0})+H(F_{t=1})]/2 >= 0.

Therefore for every C>=4,

    C J(G)-H(G) >= C J(F)-H(F).                          (1.2)

The threshold 4 is sharp for this **universal slack-monotonicity statement**: an exact three-variable Boolean F has j_t=1/2 and Delta_t H=0, making the increment exactly C/2-2.

Since universal FEI with I is equivalent, constant-for-constant, to H<=C J under Walsh-character folding, (1.2) gives a genuine universal reduction:

> At every target C>=4, quadratic ANF leaves may be peeled iteratively. To prove FEI for all Boolean functions at C, it is enough to prove it for the residual quadratic-leaf cores.

This applies even when the residual core has arbitrary high-degree ANF terms; it is not a theorem merely about quadratic/partially-bent functions.

I also attack and refute a stronger but tempting decomposition lemma. A cut vertex in the ANF interaction graph does **not** make H/I (or H/J) bounded by the worst attached factor. There is an exact k-arm tree family in which every arm separately has H/J=4/3, while the shared-control product has

    H/J = 4k/(2k+1) -> 2.

This is a genuine Boolean counterexample to max-parent articulation closure, not to FEI. The same family explains the obstruction: a one-time connector activation is amortized across many arms. The leaf-slack identity preserves that activation credit rather than falsely tensorizing factors.

At the current recovered unrestricted lower-bound scale
    C_ext = 6.521845710923046575,
every peeled quadratic leaf increases folded C_ext-slack by at least

    C_ext/2 - 2 = 1.2609228554615232875 bits.             (1.3)

Thus quadratic tree fringes are not part of the remaining hard boundary-packing problem at this scale. The unresolved core consists of variables which cannot be removed by this quadratic-leaf pruning — in particular quadratic 2-core structure and variables participating in higher-degree ANF monomials.

Full FEI remains OPEN.

## 2. Character folding, stated at the exact scope used here

For a coordinate i let alpha_i=Inf_i(f). Multiplying f by the Walsh character x_i toggles disagreement on every i-edge and leaves every j-edge, j!=i, unchanged. Hence

    Inf_i(x_i f)=1-alpha_i,
    Inf_j(x_i f)=alpha_j  (j!=i),

while multiplication by any Walsh character only permutes/signs Fourier coefficients and therefore preserves spectral entropy.

Choosing independently every coordinate with alpha_i>1/2 gives a character chi with

    I(chi f)=J(f):=sum_i min(alpha_i,1-alpha_i).           (2.1)

Consequently, for any fixed C,

    H(f)<=C I(f) for every Boolean f
iff
    H(f)<=C J(f) for every Boolean f.                      (2.2)

The forward implication applies FEI to the minimizing character twist; the reverse implication uses J(f)<=I(f).

Character folding is inherited FEI machinery rather than a novelty claim. It is useful here because a linear ANF term in a leaf variable can be removed without changing H or J.

## 3. PROVED: exact quadratic-leaf transfer identity

Let F:{0,1}^{1+m}->{±1} have distinguished coordinate t and residual coordinates z. Add a fresh bit x and set

    G(t,x,z)=F(t,z)(-1)^(t x).                             (3.1)

For each residual Fourier index S subseteq z write

    u_S = Fhat(S),
    v_S = Fhat(S union {t}).

The two t-restrictions have normalized Fourier coefficients

    widehat(F_{t=0})(S)=u_S+v_S,
    widehat(F_{t=1})(S)=u_S-v_S                           (3.2)

(up to the harmless choice of which binary value is called 0/1).

The quadratic leaf q(t,x)=(-1)^(tx) has four Walsh coefficients of magnitude 1/2, with one negative sign. Convolution in Fourier space gives, for each fixed residual S, four coefficients of G whose signed values are

    (u_S+v_S)/2, (u_S+v_S)/2,
    (u_S-v_S)/2, -(u_S-v_S)/2.                            (3.3)

### Entropy identity

Let a=(u+v)^2 and b=(u-v)^2. The contribution of (3.3) to H(G) is

    -2(a/4) log2(a/4) - 2(b/4) log2(b/4)
      = -(a/2)log2 a -(b/2)log2 b + a+b.

Summing over S, the first two terms are exactly the average child entropy, while

    sum_S (a+b)
      = 2 sum_S (u_S^2+v_S^2)
      = 2

by Parseval. Hence

    H(G)
      = [H(F_{t=0})+H(F_{t=1})]/2 + 2
      = H(F)-Delta_t H(F)+2.                              (3.4)

The September-20 exact restriction identity writes Delta_t H as a sum of nonnegative fibre terms Psi, so

    Delta_t H(F)>=0.                                      (3.5)

No FEI assumption is used.

### Influence identity

For a residual coordinate z_j, the leaf phase is independent of z_j, so

    Inf_{z_j}(G)=Inf_{z_j}(F).                            (3.6)

Flipping x changes (-1)^(tx) iff t=1, so

    Inf_x(G)=1/2.                                         (3.7)

Flipping t changes G by the XOR of the t-disagreement indicator of F and the fresh uniform bit x. Conditional on every z, XOR with a uniform bit is unbiased, so

    Inf_t(G)=1/2.                                         (3.8)

Therefore, with j_t(F)=min(Inf_t(F),1-Inf_t(F)),

    J(G)=J(F)-j_t(F)+1.                                  (3.9)

Combining (3.4) and (3.9) gives the exact slack identity (1.1):

    Slack_C^J(G)-Slack_C^J(F)
      = C(1-j_t(F))-2+Delta_t H(F).

Since j_t<=1/2 and Delta_t H>=0,

    Slack_C^J(G)-Slack_C^J(F) >= C/2-2.                  (3.10)

This proves monotonicity for every C>=4.

## 4. Sharpness of the C=4 leaf-transfer threshold

The lower bound (3.10) cannot be improved uniformly by replacing 4 with a smaller threshold.

Take

    F_*(t,a,b)=(-1)^{ t + a + t b + a b }.                (4.1)

Its truth table in integer order t+2a+4b has mask 6:
    [1,-1,-1,1,1,1,1,1].

Its Walsh-square law is uniform on four atoms, so

    H(F_*)=2.

Every physical coordinate has influence 1/2, hence

    J(F_*)=3/2,
    j_t(F_*)=1/2.

Both t-restrictions also have uniform four-atom Walsh-square law and entropy 2, hence

    Delta_t H(F_*)=0.

Attach one quadratic leaf x as in (3.1). Equation (3.4) gives H(G_*)=4 and (3.9) gives J(G_*)=2. Therefore

    Slack_C^J(G_*)-Slack_C^J(F_*) = C/2-2.               (4.2)

It is negative for every C<4, zero at C=4, and positive for C>4.

This sharpness concerns the **leaf-extension slack transfer**, not the optimal FEI constant. Neither F_* nor G_* is FEI-hard.

## 5. PROVED: quadratic-leaf core reduction

Write every Boolean function uniquely as

    f(x)=(-1)^{P(x)}

with P the multilinear algebraic normal form over F_2.

Call x a **quadratic leaf** if among all nonlinear monomials of P containing x, the only one is x t for one other variable t. A linear term a x is allowed.

Then

    P(x,t,z)=P_0(t,z)+a x+x t.

Multiplication by the character (-1)^{a x} removes a x while preserving H and J, reducing exactly to (3.1).

### Corollary 5.1 — one peel

For every C>=4,

    Slack_C^J((-1)^P) >= Slack_C^J((-1)^{P_0}).           (5.1)

### Corollary 5.2 — iterative core

Repeat the operation whenever a quadratic leaf exists. For any finite sequence of valid peels ending at a core P_core,

    Slack_C^J((-1)^P) >= Slack_C^J((-1)^{P_core})
    for every C>=4.                                      (5.2)

Therefore, because the class of leaf-cores is invariant under adding linear characters, proving standard FEI H<=C I for every quadratic-leaf core at some C>=4 proves FEI for every Boolean function at the same C.

The reduction is exact and dimension-independent. No assumption is made on the degree or structure of P_core.

### Geometric interpretation

For a leaf x with unique nonlinear term xt,

    partial_x P = a+t.

Thus the x-pivotal set is exactly a halfcube and its physical boundary lies in the single t-direction. The second-order debt identified in the previous B17 report is therefore localized to one connector and is paid exactly once by the transfer identity.

More generally, any purely quadratic tree fringe attached to an arbitrary higher-degree core can be stripped from its outside leaves inward. At C>=4 the folded slack never decreases during this stripping. Hence the unresolved pivotal-boundary packing problem can be restricted to the nonlinear core left after this pruning.

For a pure quadratic forest this proves a coarse constant-4 statement; Potapov's September-2026 theorem for partially bent functions gives the stronger sharp constant 2 on that pure class. The point here is the **arbitrary-core shared-variable transfer**, not a new bound for quadratic phases.

## 6. REFUTED: max-parent articulation closure

A very tempting strengthening of the core reduction is false:

> False lemma. If the ANF interaction graph has an articulation vertex and f is the product of Boolean factors on the resulting shared-control blocks, then H/J of f is at most the maximum H/J of the factors.

Here is an exact Boolean counterexample family.

Define the three-variable arm

    A(t,x,y)=(-1)^{ t+x+t y+x y }.                        (6.1)

Its nonlinear interaction graph is the path

    t -- y -- x.

It has a uniform four-point spectral law, so

    H(A)=2.

Every variable has influence 1/2, hence

    J(A)=I(A)=3/2,
    H(A)/J(A)=4/3.                                       (6.2)

Now take k disjoint copies of (x,y) but share the same t:

    F_k(t,x_1,y_1,...,x_k,y_k)
      = product_{ell=1}^k A(t,x_ell,y_ell).               (6.3)

Its ANF interaction graph is a tree consisting of k length-two arms at t, so t is an articulation as soon as k>=2.

The phase polynomial is quadratic. Its polar bilinear matrix is the adjacency matrix of this tree over F_2. A kernel vector satisfies, for every ell,

    z_{y_ell}=0,
    z_{x_ell}=z_t,

and the t-row is then automatic. Hence the kernel is one-dimensional and the rank is

    rank = (2k+1)-1 = 2k.                                (6.4)

For a quadratic Boolean phase with polar rank r, the Walsh-square law is uniform on an affine set of 2^r frequencies; equivalently this follows from the standard quadratic Walsh transform/autocorrelation calculation. Therefore

    H(F_k)=2k.                                           (6.5)

Every vertex of the interaction tree has a nonconstant affine derivative, so every physical coordinate has influence 1/2. Thus

    I(F_k)=J(F_k)=(2k+1)/2.                              (6.6)

Consequently

    H(F_k)/J(F_k)=4k/(2k+1) -> 2.                        (6.7)

For k=2 this is already 8/5>4/3.

So shared articulation can raise the ratio strictly above every arm's ratio, and the gap approaches

    2 - 4/3 = 2/3.

This does **not** refute FEI; the whole family stays below 2. It refutes only the stronger factorwise max closure.

### What the obstruction says

The factors all reuse the same connector t. The connector's one-half influence is paid only once in the product, while spectral rank contributed by distinct arms accumulates. A factorwise max argument charges the connector once per arm and therefore loses the cancellation/amortization.

The quadratic-leaf theorem is the valid replacement: it does not tensorize arm ratios. It tracks the connector through j_t and the exact restriction decrement Delta_t H. At C>=4 the resulting folded slack is monotone even though the raw H/J ratio can rise.

## 7. Optional block strengthening: a whole quadratic star is paid by one activation

The one-leaf calculation also gives a useful exact grouped version.

For fresh leaves x_1,...,x_k, k>=1, set

    G_k(t,x,z)
      = F(t,z)(-1)^{t(x_1+...+x_k)}.                     (7.1)

When t=0 the new leaf block is the constant character; when t=1 it is the full parity character. Their Fourier supports in the fresh block are disjoint. Consequently the same coefficient calculation gives

    H(G_k)
      = [H(F_{t=0})+H(F_{t=1})]/2 + 2
      = H(F)-Delta_t H(F)+2,                             (7.2)

independent of k as soon as k>=1.

Every fresh leaf has influence 1/2 and the control t is again randomized to influence 1/2, hence

    J(G_k)=J(F)-j_t(F)+(k+1)/2.                          (7.3)

Therefore

    Slack_C^J(G_k)-Slack_C^J(F)
      = C[(k+1)/2-j_t(F)] - 2 + Delta_t H(F)
      >= C k/2 - 2.                                      (7.4)

The entropy activation cost is paid once, while each additional quadratic leaf contributes another one-half folded influence. This exact star identity is the simplest model of the “group enough boundary coordinates” mechanism requested by the previous run.

Again, it covers a specific ANF geometry rather than the full pivotal-boundary ledger.

## 8. Exact finite checker

`verify_quadratic_leaf_peeling.py` uses integer Walsh transforms and `fractions.Fraction`.

It exhaustively checks the leaf transform for every Boolean base F with distinguished t and at most two residual variables:
- 4 functions with only t;
- 16 functions on t plus one residual bit;
- 256 functions on t plus two residual bits;
for 276 functions total.

No floating logarithm decides the entropy identity. For every F the checker compares exact squared-Walsh probability multisets and verifies that the attached function has exactly two copies of every child spectral mass divided by four. It also verifies all influence and folded-J identities with exact rational arithmetic.

The checker verifies the sharp mask-6 witness exactly:
    H(F_*)=2, J(F_*)=3/2, Delta_t H=0,
    H(G_*)=4, J(G_*)=2,
so the slack increment is C/2-2.

Finally it verifies the k-arm family for k=1,...,5 by exact Walsh arithmetic:
    spectral support size = 2^(2k),
    every nonzero squared mass = 2^(-2k),
    every one of 2k+1 influences = 1/2.

It also verifies the cubic-leaf obstruction exactly: base truth mask 1, attached spectral masses {9/16,1/16 x7}, attached influences (3/4,3/4,1/4), and the exact folded-J drop 1 -> 3/4.

Finite checks establish only their tested scope; Sections 3–7 are the analytic argument.

Checker SHA-256:
    ced13f3e222d06d177e2d8b58e63c2ed07b27fa591c2ee82dc9167003fab9993

Output SHA-256:
    3faeb8571b730c88072ece56919e45f9b2cd29d38d4ab5c2fd2e147404469660

## 9. REFUTED: direct degree-3 leaf peeling fails for every nonnegative C

The quadratic theorem is genuinely degree-specific. The most obvious extension to a leaf occurring only in one cubic monomial fails in the strongest possible way.

Take the two-variable base

    B(t,u) = -1 at (t,u)=(0,0), and +1 elsewhere.

Equivalently its ANF phase is

    P_B = 1+t+u+tu.

Its spectral law is uniform on four atoms, so

    H(B)=2.

Both influences are 1/2, hence

    J(B)=1.

Now add a fresh leaf x through the unique cubic term xtu:

    G(t,u,x)=B(t,u)(-1)^(x t u).                         (9.1)

The Walsh transform of G is, up to ordering/sign,

    (2,-2,-2,-6,2,-2,-2,2).

Thus its exact spectral law has one atom of mass 9/16 and seven atoms of mass 1/16. Therefore

    H(G)
      = -(9/16)log2(9/16)-7(1/16)log2(1/16)
      = 4-(9/8)log2 3.                                  (9.2)

Its physical influences are exactly

    (3/4, 3/4, 1/4),

so after folding

    J(G)=1/4+1/4+1/4=3/4.                               (9.3)

Hence the folded C-slack change is

    Slack_C^J(G)-Slack_C^J(B)
      = C(3/4-1) - [4-(9/8)log2 3 - 2]
      = (9/8)log2 3 - 2 - C/4.                         (9.4)

Because (9/8)log2 3 < 2, expression (9.4) is **strictly negative for every C>=0**.

So there is no analogue of quadratic-leaf slack monotonicity for arbitrary cubic leaves at any nonnegative universal constant.

This is not an FEI counterexample:
    H(G)/J(G)
      = 16/3 - (3/2)log2 3
      = 2.9558895822...,
well below the recovered unrestricted lower-bound scale.

But it is a decisive obstruction to extending the peeling algorithm by simply replacing a quadratic leaf xt with a higher-order leaf xtu. A cubic leaf can simultaneously **increase spectral entropy and decrease folded influence**.

This identifies the next mechanism a valid higher-order peeling theorem would have to preserve: the joint two-control state (t,u), not only the leaf's own pivotal boundary or a scalar folded influence. In other words, the quadratic leaf is paid by one connector activation, while a cubic leaf can create destructive influence folding across two controls.

## 10. Literature and applicability check

Current primary literature checked this run:

1. O'Donnell–Tan, “A composition theorem for the Fourier Entropy-Influence conjecture” (2013, arXiv:1304.1347). Their composition theorem is for inner functions on disjoint variable sets. The quadratic-leaf operator here deliberately shares the control t with the existing core, so the exact transfer above is not obtained merely by invoking the disjoint composition theorem.

2. González–MacManus–Pereyra, “Further evidence towards the Fourier Entropy-Influence conjecture” (arXiv:2606.00246, submitted 29 May 2026). Their restriction/stopping-tree framework is directly relevant to Delta_t H and to the preceding B17 local-payment obstruction. The present identity supplies one exactly peelable shared-variable geometry inside that broader stopping picture.

3. Vladimir N. Potapov, “On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions” (arXiv:2609.21563, 18 Sep 2026). Potapov proves sharp constant 4 for plateaued functions and sharp constant 2 for partially bent functions. Pure quadratic phases in the articulation family are in the easy partially-bent regime, so I do not claim a new FEI bound for them. The useful scope here is an arbitrary Boolean core with a shared quadratic leaf/tree fringe.

I did not locate, in this targeted check, a primary-source statement of the exact folded-slack leaf transfer (3.1)–(3.10). That is not a publication-priority claim; the identity is elementary once the correct shared-control Fourier transform is written.

## 11. Before / after and remaining universal gap

Before:
- fleet02/B17 had an exact Bellman recurrence;
- every prescribed split was refuted;
- equal-density local entropy debt was reduced to a constant influence term plus one half of a pivotal-set physical boundary;
- no dimension-independent packing theorem for those second-order boundaries was available.

After:
- every quadratic ANF leaf has an exact folded-slack transfer;
- at every target C>=4 it can be peeled without decreasing folded FEI slack;
- the C=4 threshold for this monotonicity is exactly sharp;
- arbitrary quadratic tree fringes attached to a high-degree core are therefore fully packable/peelable;
- a stronger max-parent articulation lemma is refuted by an exact Boolean tree family whose ratio rises from 4/3 per arm to 4k/(2k+1)->2;
- the failure is traced to one-time connector activation rather than FEI hardness.

At the current recovered unrestricted lower-bound scale C_ext, each individual quadratic leaf contributes at least 1.2609228554615232875 bits of *positive* folded slack beyond its core. Hence no candidate counterexample at that scale needs quadratic tree fringe to be retained.

The remaining universal obstruction is now narrower:

> control the restriction/pivotal-boundary ledger on the quadratic-leaf core, where every surviving variable either belongs to a higher-degree ANF monomial or lies in the quadratic 2-core, without discarding the signed cancellation terms.

The direct degree-3 analogue has now been refuted by (9.1)–(9.4), so the next B17 attack should not retry scalar leaf slack. A sharper target is a **two-control state potential** for a cubic leaf xtu: retain the full four-state restriction law on (t,u), derive its exact Fourier transfer, and ask whether the negative folded-influence change in (9.4) is compensated by a nonnegative control-pair potential that telescopes under hypergraph-core peeling. Any candidate must first survive the exact mask-1 obstruction above and the bent-swap prescribed-coordinate obstruction from the preceding run.

Full FEI remains OPEN / NOT PROVED.
