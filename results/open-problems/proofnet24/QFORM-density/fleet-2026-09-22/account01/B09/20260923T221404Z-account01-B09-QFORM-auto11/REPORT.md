SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T22:14:04Z.
attacking: the global third-compound spectral resource by decomposing every squared 3x3 minor according to physical row/column overlap, paying the disjoint class by a literal source-coordinate cut, and identifying the exact one-overlap mass required by the 3x2 kernel-derivative mechanism.

# account01/B09 — exact third-compound overlap compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: bilinear block mechanism / analytic derivation and exact structural identities  
Run: `20260923T221404Z-account01-B09-QFORM-auto11`  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING STRUCTURAL THEOREM / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source discipline

The target remains the unrestricted statement for independent ORIGINAL-coordinate real variables with scalar densities bounded by one and arbitrary real symmetric A satisfying `sigma_3(A)>=1`. No Gaussianity, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence hypothesis is introduced.

Fresh brain control at run start had OWNER CONTROL revision `2026-09-22.15`, programme revision `2026-09-22.5`, QFORM as the sole research target and no account01/B09 pause. The continuation request `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` was consumed. In particular, this report does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, positive conditional projection moments, a uniformly good single minor, or deletion of a small matrix coefficient as a small random quadratic error.

Two completed source results are used at actual inequalities:

1. `QFORM-PHYSICAL-D3-NO-MARGINAL-GATE-v1`, source
   `yspennstate/math-open-problems@8a4e6d0048174e047fc3b4ae8cabfbabba3cdc3b`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260923T165154Z-account01-B20-QFORM-auto11/NO_MARGINAL_D3.md`.
   For a literal physical cut I|J and
   `Z3=e3(A[I,J]A[I,J]^T)>0`, it gives a continuous C0 density with

       ||p_Q||_infinity <= C3 Z3^(-1/6),
       C3=3*2^(4/3)*exp(1/3)=10.5501688311... .

2. The designated partner account02/B09 theorem
   `QFORM-3x2-KERNELDERIVATIVE-L1-v1`, source
   `yspennstate/math-open-problems@65ed9ea70175fb28541d756aea01f6aeb491fd6c`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T201318Z-account02-B09-QFORM-r14/REPORT.md`.
   For a literal physical left triple L and right pair R, with `P=A[L,L]`, rank-two `C=A[L,R]`, columns `c1,c2`, `w=c1 x c2`, and `Pw!=0`, it gives

       ||p_Q||_infinity
          <= C_KD (||w|| ||Pw||)^(-1/5),
       C_KD=5*6^(3/5)/2^(11/10)=6.8348306662...,

   with continuous density and the same coefficient multiplying interval length.

The theorem below is an exact structural identity plus a paid branch; it does not claim the full conjecture.

## 2. Fixed physical triple: exact overlap decomposition

Fix a literal original-coordinate triple `T subset [n]`, `|T|=3`. Put

    P=A[T,T],
    C=A[T,T^c],
    G=CC^T.

For each `r in T^c`, let `c_r=A[T,r] in R^3`. For `r<s` in `T^c`, put

    w_rs=c_r x c_s.

Define four nonnegative currencies

    D0(T)=det(G),
    D1(T)=sum_{r<s in T^c} ||P w_rs||^2,
    D2(T)=||adj(P) C||_F^2,
    D3(T)=det(P)^2.

### Theorem `QFORM-THIRD-COMPOUND-OVERLAP-DECOMPOSITION-v1`

For every real symmetric A and every physical triple T,

    boxed:
    det((A^2)[T,T])
      =D0(T)+D1(T)+D2(T)+D3(T).                         (2.1)

Equivalently,

    boxed:
    det(P^2+G)
      =det(G)
       +tr(P^2 adj(G))
       +tr(G adj(P)^2)
       +det(P)^2.                                         (2.2)

Moreover, the four terms in (2.1) are exactly the squared 3x3 minors `det A[S,T]^2` grouped by the physical overlap cardinality `|S intersect T|=0,1,2,3`, respectively.

### Proof

Cauchy--Binet for the n-by-3 matrix `A[:,T]` gives

    det((A^2)[T,T])
      =sum_{|S|=3} det A[S,T]^2,                          (2.3)

because `A[:,T]^T A[:,T]=(A^2)[T,T]`.

**Overlap zero.** If `S subset T^c`, the relevant rows are rows of `C^T`; summing their squared 3x3 determinants is `det(CC^T)=det G` by Cauchy--Binet.

**Overlap one.** Write

    S={k,r,s},  k in T,  r<s in T^c.

By symmetry, the three rows of `A[S,T]` are `e_k^T P`, `c_r^T`, `c_s^T`. Hence

    det A[S,T]
       = +/- e_k^T P(c_r x c_s)
       = +/- (P w_rs)_k.                                  (2.4)

Summing over `k in T` gives `||P w_rs||^2`, and then over `r<s` gives `D1(T)`.

**Overlap two.** Write

    S=(T\{k}) union {r},  k in T, r in T^c.

The matrix `A[S,T]` is obtained from P by replacing its k-th row by `c_r^T`, up to a row permutation. Expansion in that row yields

    det A[S,T]
       = +/- e_k^T adj(P)c_r.                              (2.5)

Summing the square over k and r gives

    sum_r ||adj(P)c_r||^2
      =||adj(P)C||_F^2
      =D2(T).                                               (2.6)

**Overlap three.** The only row triple is `S=T`, giving `det(P)^2`.

This proves (2.1). For the invariant version, second-compound Cauchy--Binet gives

    sum_{r<s} w_rs w_rs^T=adj(G),                          (2.7)

so

    D1(T)=tr(P^2 adj(G)).                                  (2.8)

Also

    D2(T)=tr(G adj(P)^2).                                  (2.9)

Finally `(A^2)[T,T]=P^2+G`, proving (2.2). QED.

## 3. Global third-compound identity

For `j=0,1,2,3`, define

    E_j(A)
      =sum_{|S|=|T|=3, |S intersect T|=j} det A[S,T]^2,    (3.1)

where `(S,T)` is an ordered pair of triples. Summing (2.1) over all column triples T gives

    boxed:
    e3(A^2)=E0(A)+E1(A)+E2(A)+E3(A).                      (3.2)

The one-overlap term is exactly

    boxed:
    E1(A)
      =sum_{|T|=3} sum_{r<s in T^c}
          ||A[T,T](A[T,r] x A[T,s])||^2.                  (3.3)

Thus the `V1(A)` aggregation debt isolated by account02/B09 r14 is not an auxiliary quantity: it is exactly the entire overlap-one sector of the third exterior spectral energy.

If the singular values of A are `sigma_1>=sigma_2>=...`, then

    e3(A^2)=sum_{i<j<k} sigma_i^2 sigma_j^2 sigma_k^2.     (3.4)

Therefore the owner hypothesis `sigma_3(A)>=1` implies

    boxed: e3(A^2)>=1.                                    (3.5)

Consequently at least one overlap class satisfies

    boxed: E_j(A)>=1/4.                                   (3.6)

This is a dimension-free exhaustive structural fork. It does not select an individual minor.

## 4. The disjoint sector is completely paid

Suppose first that

    E0(A)>=eta>0.                                          (4.1)

Take a uniformly random literal physical bipartition `[n]=I disjoint_union J`, each coordinate independently assigned to I or J with probability 1/2. Put

    Z3(I,J)=e3(A[I,J]A[I,J]^T)
           =sum_{S subset I,T subset J, |S|=|T|=3}
              det A[S,T]^2.                               (4.2)

Every ordered disjoint pair `(S,T)` with `|S|=|T|=3` is captured in (4.2) with probability `2^-6`. Hence

    E Z3(I,J)=E0(A)/64.                                   (4.3)

There exists a literal source-coordinate cut with

    Z3(I,J)>=E0(A)/64.                                    (4.4)

Apply the completed no-marginal physical D3 theorem to the actual full Q:

    boxed:
    ||p_Q||_infinity
      <= C3 (E0/64)^(-1/6)
      =2 C3 E0^(-1/6).                                    (4.5)

The density is continuous C0 and

    P{Q in B}<=2 C3 E0^(-1/6)|B|                          (4.6)

for every interval B.

In particular, on the exhaustive fork (3.6), if the winning class is the disjoint class,

    E0>=1/4,

then

    boxed:
    ||p_Q||_infinity
      <=3*2^(8/3)*exp(1/3)
      =26.5847595807... <26.585,                           (4.7)

and

    boxed: P{Q in B}<26.585 |B|.                          (4.8)

This branch has continuous density. There is no square-root probability conversion and no spectral rotation of the random inputs.

## 5. The one-overlap sector is exactly the grouped rank-two currency

For a fixed triple T, suppose the physical cross block `C=A[T,T^c]` has rank two. Let n be a unit vector spanning `ker(C^T)`, and set

    Delta=sigma_1(C)sigma_2(C),
    Delta^2=e2(G).                                         (5.1)

Since G is a rank-two 3x3 positive semidefinite matrix,

    adj(G)=Delta^2 n n^T.                                 (5.2)

By (2.8),

    boxed:
    D1(T)=Delta^2 ||Pn||^2.                               (5.3)

This is exactly the aggregate grouped rank-two kernel-derivative currency from the previous B09 runs. It also identifies the account03/B09 anisotropy parameter without introducing it artificially: at fixed `D1(T)`, small cross area Delta is precisely the regime where `||Pn||` becomes large.

There is a useful exact endpoint classification.

### Proposition `QFORM-RANK2-OVERLAP-ENDPOINT-RANKONE-v1`

Assume `rank(C)=2` and `Pn!=0`. If

    D2(T)=0,
    D3(T)=0,                                                (5.4)

then

    boxed: rank(P)=1.                                      (5.5)

Proof. `D3=0` gives `det P=0`. If `rank P=2`, then `adj(P)` is a nonzero symmetric rank-one matrix whose range equals `ker P`. The identity `D2=||adj(P)C||_F^2=0` says that `adj(P)` annihilates `range C=n^perp`. Since `adj(P)` is symmetric, its range lies in `span(n)`. Hence `ker P=span(n)`, so `Pn=0`, contradiction. Rank three is excluded by `det P=0`; therefore rank P is at most one. Since `Pn!=0`, P is nonzero and rank P=1. QED.

So, for an active rank-two cross triple, the only exact way to have no overlap-two and no principal-third currency is a literal three-coordinate rank-one same-side curvature. This identifies a sharply structured endpoint for grouped-square/hub methods rather than an unexplained degeneracy.

## 6. Random-color localization of the two remaining overlap classes

The global sums `E1,E2` can be localized to actual physical banks without selecting a largest individual minor.

### One-overlap coloring

Color every coordinate independently into three literal banks `H,I,J` with probabilities

    P(H)=1/5,  P(I)=2/5,  P(J)=2/5.                       (6.1)

Define

    Omega1(H,I,J)
      =sum_{h in H}
        sum_{R subset I, |R|=2}
        sum_{C0 subset J, |C0|=2}
          det A[{h} union R, {h} union C0]^2.             (6.2)

Each ordered one-overlap pair has five distinct coordinates: one shared coordinate, two row-exclusive coordinates and two column-exclusive coordinates. It is captured with probability

    (1/5)(2/5)^2(2/5)^2=16/3125.                          (6.3)

Hence some literal three-bank partition satisfies

    boxed:
    Omega1(H,I,J)>=(16/3125)E1(A).                        (6.4)

If `E1>=1/4`, this gives `Omega1>=4/3125`.

### Two-overlap coloring

Color independently with probabilities

    P(H)=1/2,  P(I)=1/4,  P(J)=1/4.                       (6.5)

Define

    Omega2(H,I,J)
      =sum_{K subset H, |K|=2}
        sum_{r in I}
        sum_{c in J}
          det A[K union {r}, K union {c}]^2.              (6.6)

Each ordered two-overlap pair has two shared and two exclusive coordinates, so it is captured with probability

    (1/2)^2(1/4)(1/4)=1/64.                               (6.7)

Thus some literal three-bank partition satisfies

    boxed:
    Omega2(H,I,J)>=E2(A)/64.                              (6.8)

If `E2>=1/4`, this gives `Omega2>=1/256`.

These are exact source-coordinate localization statements. They do not yet provide the missing analytic receiver when the shared anchor coordinate(s) are themselves spread over a large hub bank; claiming such a receiver would be the unsupported step.

## 7. Required designated-partner application to an actual inequality

For `s>0`, on five literal physical coordinates `(Y1,Y2,Y3,Z1,Z2)`, define

    Q_s
      =2s Y1 Y3+2Y1 Z1+2Y2 Z2.                           (7.1)

Its symmetric coefficient matrix is, after reordering, the orthogonal direct sum of

    [[0,s,1],[s,0,0],[1,0,0]]

and

    [[0,1],[1,0]].

Therefore

    spec(A_s)
      ={+sqrt(s^2+1),-sqrt(s^2+1),+1,-1,0}.              (7.2)

The owner spectral hypothesis holds for every `s>0`.

Take the physical left triple `L={Y1,Y2,Y3}` and right pair `R={Z1,Z2}`. Then

    C=[e1,e2],
    w=e3,
    ||w||=1,
    P w=s e1,
    ||P w||=s.                                             (7.3)

Applying the completed account02/B09 theorem at its actual invariant gives

    boxed:
    ||p_Qs||_infinity<=C_KD s^(-1/5).                     (7.4)

At `s=32`,

    boxed:
    ||p_Q32||_infinity
       <=3.4174153331... <3.418,                           (7.5)

and for every interval B,

    boxed:
    P{Q_32 in B}<3.418 |B|.                               (7.6)

This partner branch has a continuous density. In the new overlap language, its anchored one-overlap currency is

    D1(L)=s^2,

while `D0(L)=det(CC^T)=0` because the cross block has rank two. Thus (7.4) is a literal payment of an overlap-one third-compound configuration, not a disjoint-cross surrogate.

## 8. What is now proved and what remains

The new exact global fork is

    e3(A^2)=E0+E1+E2+E3>=1.                               (8.1)

The entire `E0>=1/4` branch is now paid with a universal continuous-density constant `<26.585`. The other three sectors are not interchangeable with E0: they encode actual reuse of one, two, or three physical coordinates between the row and column triples.

The most important conceptual consequence is that the partner's aggregation debt has become a necessary global spectral branch:

    if E0,E2,E3<1/4, then E1>1/4,                         (8.2)

so a universal theorem for the overlap-one aggregate `E1=V1(A)` would close an entire quarter-class in the exact third-compound exhaustion, not merely improve a selected packet.

The first unpaid B09 implication is therefore

`QFORM-OVERLAP1-GLOBAL-AGGREGATE-RECEIVER-OR-ANCHOR-PROMOTION-v1`:

starting from a literal coloring with `Omega1>=4/3125`, convert the aggregate shared-one-index mass into an O(|I|) density bound without choosing one anchor/minor with reciprocal scale; or prove that concentration of the shared-anchor law forces an already-paid physical-hub/fixed-pair/grouped-square exit. The exact rank-two endpoint proposition above says that after fixing a triple, simultaneous disappearance of overlap-two and principal-third currency forces rank-one same-side curvature, which is the natural grouped-square endpoint to exploit.

No valid counterexample to the full conjecture was found. The unrestricted QFORM statement remains OPEN, and continuity is proved only on the paid branches described above.

## 9. Deterministic verification

`CHECKS.md` beside this report records:

- a fixed-seed random 8x8 verification of (2.1) to `2.49e-14`;
- a global all-triples verification of (3.2) against eigenvalue-computed `e3(A^2)` to floating error;
- the exact random-cut constant `<26.585`;
- the exact spectrum and designated-partner `s=32` bound `<3.418`.

The calculations check algebra and arithmetic only.
