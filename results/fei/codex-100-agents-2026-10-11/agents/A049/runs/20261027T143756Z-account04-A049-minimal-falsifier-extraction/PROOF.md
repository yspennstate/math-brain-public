# A calibrated reference still has to pay its first query

All laws are finite and normalized; logs are base two. Boolean functions are signs on the uniform cube. Full FEI remains open. The equality theorem below applies to arbitrary positive laws, while its minimal witness is the spectrum of an actual Boolean circuit.

## 1. The exact equality boundary

Let n>=2. Let P,Q be strictly positive laws on all subsets of [n]. Assume Q(empty)=P(empty), and for every T with |T|<=n-2 assume

    sum_{S containing T} Q(S) = sum_{S containing T} P(S).

The T=empty condition is normalization. Write E_i for deterministic deletion of coordinate i and define the actual erasure contraction

    L_i=D(P||Q)-D(E_i P||E_i Q).

Then L_i=0 for ANY ONE coordinate i if and only if Q=P. Equivalently, every nontrivial such Q has L_i>0 at EVERY coordinate. This is an equality/strictness theorem, not a quantitative influence upper bound.

Proof. The finite KL chain rule expresses L_i as the E_i P-weighted average of the binary conditional divergences on the fibers {U,U+i}. Every P and Q atom and every fiber mass is positive. Thus L_i=0 if and only if Q(U)/P(U)=Q(U+i)/P(U+i) on every fiber. At the vacuum fiber, Q(empty)=P(empty)>0 forces Q({i})=P({i}); therefore E_i Q(empty)=E_i P(empty).

Set m=n-1 and d(U)=E_i Q(U)-E_i P(U). All proper inclusion moments of d vanish: sum_{U containing T}d(U)=0 for |T|<=m-1. Finite Möbius inversion on the subset lattice gives

    d(U)=(-1)^(m-|U|) c,  c=d([m]).

One may also derive this by descending induction on |U|: normalization and every proper upper sum are zero, so the full atom is the only free parameter. Since d(empty)=0, c=0. Thus the erased laws coincide. Together with equality of their within-fiber conditional laws this implies Q=P atomwise. The converse is immediate. No passage through a limit, continuous parameter search, or unverified Boolean realization enters this argument.

Each condition has a role: positivity justifies fiber ratios and the equality criterion; matching the vacuum pins the empty fiber; moments of orders up to n-2 determine the remaining erased law after its vacuum is pinned. Controls for dropping assumptions appear in the separate audit. The strictness theorem uses the complete erasure loss, which is shared by both projection inheritance and coherent-kernel inheritance. Their child references are different and are not substituted for each other here.

## 2. A minimal actual Boolean certificate

On three bits let f(x)=-1 only at x=000, and +1 elsewhere. Its circuit is the three-input point sign, or 1-2*1[x=000]. Direct Walsh expansion gives

    P(empty)=9/16,  P(S)=1/16 for all seven nonempty S,
    H(f)=4-(9/8)log2(3),  Inf_i=1/4,  I(f)=3/4.

Define the strictly positive reference by cardinality:

    64 Q(S) = 36 if |S|=0, 5 if |S|=1,
               2 if |S|=2, 7 if |S|=3.

There is no free parameter. Its masses sum to 64/64; its vacuum is 9/16 and each marginal influence is (5+2*2+7)/64=1/4. Hence it already satisfies vacuum, total-influence and every individual-influence calibration. Any information projection imposing only these already matched affine constraints leaves Q unchanged and has fee/release zero. The inclusion conditions of section1 are precisely those first moments when n=3. Q is not P, so every L_i is strictly positive.

Here are the complete exact prices, identical for each coordinate by permutation invariance. Let R=E_i P and Z=E_i Q, with residual labels empty, first singleton, second singleton, full. Then

    R=(40,8,8,8)/64,  Z=(41,7,7,9)/64,
    A=D(P||Q)=log2(2048/875)/16,
    D(R||Z)=(5/8)log2(40/41)+(1/4)log2(8/7)
                              +(1/8)log2(8/9),
    L_i=A-D(R||Z)>7/100,    L_i>(15/16)A.

The strict signs are exact integer product comparisons after clearing the rational coefficients of prime logarithms. No floating-point estimate establishes a sign. Their vectors and regeneration command are in out/CHECK.json and code/check.py.

For coherent inheritance, the active AND2 child and constant child have actual REFERENCE outcome masses 39/80 and 41/80. The true outcomes have weights 1/2 each. The normalized inherited active reference is (41,35,35,45)/156, whereas its true law is uniform on four atoms; the constant child's reference equals its true law. Consequently

    O_i=D(fair||(39/80,41/80))=log2(1600/1599)/2>0,
    A=L_i+O_i+(A_active+A_constant)/2.

Every query consumes most of the ORIGINAL mismatch even before a fresh floor is requested. A projection-inheritance policy instead gives BOTH children reference Z; its exact identity is average D(P_child||Z)=D(R||Z)+JS_child. Neither version permits deleting L_i or refreshing A. The source remains affordable: CE(P,Q)=H+A<3=4I. Therefore this is a counterexample to the proposed zero-loss selection shortcut after moment matching, NOT to the supplied rate4 source or full FEI.

Minimality is global for this exact shortcut, not just the full-support examples. On two bits normalization, the vacuum and both individual marginals uniquely determine every atom: the full atom is determined by their sum minus total nonempty mass, then the singletons are determined. On one or zero bits the same is immediate. Thus for n<=2 a normalized reference matching the vacuum and all individual influences necessarily equals P, even with source zeros. No nontrivial query-loss counterexample exists there. The three-bit actual Boolean example attains the minimum.

## 3. Independent review of A050's repeated vacuum calibration

Source: A050-VACUUM-CALIBRATED-HEREDITARY-REFERENCE@1, hash e91fa893eb1ba02faa445155ebd683aa7bc9245a8f0a43ecdf502ec0e3b5f88d, run20261027T005654Z-account04-A050-repair-with-scope. Verdict HOLDS at the printed finite supplied-source scope, without repair.

At a raw child write r=P(empty), z=Q(empty). Keeping the nonempty conditional law and matching the vacuum uniquely gives Q*(empty)=r, Q*(S)=(1-r)Q(S)/(1-z) off empty, with Q*=P if r=1. Covering and the positive true-law component imply 1-z>=b(1-r)>0 whenever r<1. Direct subtraction of the complete atomwise cross entropies yields CE(P,Q*)-CE(P,Q)=-D(Bern(r)||Bern(z)), including r=0 and r=1. Ghost reference masses are scaled with their cell; they cannot be omitted before this subtraction.

For a representation Q=bP+sum c_j delta_Wj, set k=(1-r)/(1-z), b*=kb. Its positive true-law component satisfies b*<=1. Scale each nonempty witness by k and put the remaining empty coefficient at r(1-b*). The sum is exactly one. At most one reusable empty slot is added, and physical deletion never turns an empty slot nonempty. The endpoint r=1 has b*=1. Zero-weight slots need no kernel evaluation.

Under coherent inheritance, exact source/reference joint-law expansion first gives A=E+O+average A_child. Put B=H(P)-H(E_i P), J=H(E_i P)-average H(P_child). Inserting the calibration identity gives

    B+average CE(P_child,Q*_child)
      =CE(P,Q)-J-E-O-average d_child.

All reaches are the actual physical probabilities, not the reference outcome probabilities. Finite tree induction telescopes the displayed identity while retaining erasures, normalizers, calibration releases, full terminal cross entropies, old debits and the original capacity. No optional-stopping theorem is needed. This independently reconstructs A050 without contribution to that version. It cannot provide the initial CE price or a new positive nonempty floor. Section2 illustrates precisely why its zero calibration debit is compatible with a positive query bill.

## 4. Checks that could fail

The primary checker recomputes every spectrum from truth tables, checks all scalar normalizers, and retains ghost rows with a declared fair fallback on zero-source fibers. It verifies both KL and full CE identities through query plus vacuum calibration, including constant and character endpoints. All278 small tables and all804 singleton queries are checked. On all128 full-support three-bit Boolean tables, the declared rational moment-preserving deformation stays positive and all384 coordinate erasure losses are strictly positive. The explicit witness uses a second, direct Walsh computation, exact prime-log prices and exact integer signs. Full finite-tree universality comes from node identities and finite induction, not from pretending the singleton census enumerates every adaptive history.

The separate audit tests the finite Möbius step, one actual Boolean counterexample when full support is dropped, and positive-law controls for dropping vacuum or moment constraints. The controls are not proposed as new FEI spectra. Any Lean result certifies only its explicitly identified finite algebra/sign statement, not the universal entropy theorem.

## 5. First unsupported universal line

The original arbitrary-core complete source must still be priced by O(I), with a useful stopping/terminal policy or a justified stricter profile paid from the SAME diminished original owner. Matching increasingly many moments does not create a zero-cost query: at the equality boundary above it excludes every zero-loss coordinate unless the reference is already the true spectrum, whose complete cross entropy is H. A paid global query ledger remains valid; no repeated reset, local influence multiplier, or finite Boolean census closes that initial-source line.
