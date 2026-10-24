# Final handoff: solo attempt on the full Fourier entropy--influence conjecture

Research window requested: 2026-09-17T22:58:53Z through
2026-09-18T08:58:53Z.  
Status at final handoff: **the full conjecture remains open**.  
Method: one solo track; no subagents, delegated workers, other models, or
independent audits were used. Runtime model/reasoning metadata: **UNVERIFIED**.

This handoff is self-contained at the level needed to continue the work. Full
proofs, counterexamples, exact scripts and raw certificates are in the files
named below.

## 1. Target and exact reductions

For a Boolean function `f:{+1,-1}^n->{+1,-1}`, let

    p_S=fhat(S)^2,
    H(f)=sum_S p_S log_2(1/p_S),
    I(f)=sum_S |S|p_S.

If `X` is the random spectral subset with law `p`, define

    B(f)=sum_i H(X_i|X_(-i)).

`ERASURE_REDUCTION.md` proves

    B(f)<=H(f),
    H(f)<=B(f)+(2/ln2)I(f).                              (1)

Thus a universal `B<=K I` would prove FEI with constant `K+2/ln2`.

The exact logarithmic edge functional

    K_log(f)=sum_{unordered cube edges {S,T}}
       min(p_S,p_T)|log_2(p_S/p_T)|

satisfies

    K_log(f)<=B(f)<=K_log(f)+(2/ln2)I(f).                (2)

Equivalently one may target

    L(f)=sum_S p_S sum_(i in S) log_2(1+p_(S-i)/p_S),
    L<=B<=L+I/ln2.                                      (3)

Booleanity is exactly the signed convolution system

    sum_S fhat(S)fhat(S xor U)=1_(U=empty).              (4)

Equations (1)--(4) are reformulations and reductions, not a solution.

## 2. Rigorous results proved during the window

### 2.1 Criticality and certified counterexamples

* A rational interval certificate gives an explicit 80-variable Boolean
  function with

      4.007 < B(f)/I(f) < 4.008.

  Therefore the provisional universal constant four for `B/I` is false.
* An explicit recursive family has absolute adjacent-amplitude overlap divided
  by influence growing linearly with recursion depth. Hence absolute overlap
  cannot majorize the logarithmic functional with a universal constant.
* A bent/addressing family has

      I=(m+2)/2,
      T_gamma=(m+1+2^(gamma m))/2

  for every fixed `gamma>0`. Every positive-power replacement of the
  logarithm therefore fails, even while this family's actual `H/I` remains
  bounded. More generally, every superlinear function of the log mass ratio
  fails along this family. The logarithm in (2)--(3) is genuinely critical.

Full details: `ADDRESSING_BARRIER_2026-09-18.md` and
`runs/2026-09-18T00-18-56Z_logarithmic-criticality.md`.

### 2.2 Restriction, erasure and parity barriers

* A single selector bit can mix two restriction spectra with `B=0` into a
  bent spectrum with `B=m+1`. No dimension-free restriction recursion for
  `B+lambda(H-B)` with fixed `lambda<1` can hold.
* The parity lift

      F(x,z)=g(x_1z,...,x_nz)

  has `B(F)=K_log(F)=0`, `H(F)=H(g)`, and `I(F)<=2I(g)`. Thus FEI on the
  even-Fourier-support subclass, where the live erasure functional vanishes,
  is already equivalent to full FEI up to factor two.
* For any restricted physical block `A`, an exact identity separates the
  entropy increment into

      H(Z_A|Z_(A^c)) + I(X_A;D),

  with the channel term at most `(2/ln2)I_A(f)`. The unproved part is a
  useful proper-block selection controlling the first term.
* Every conditioned parity branch is a normalized Fourier projection of a
  partial Boolean function, and every partial Boolean function occurs as one
  such branch of a Boolean parent. A universal normalized partial-Boolean FEI
  theorem would imply full FEI by tensor amplification.

Full details: `ERASURE_SYNERGY_AND_DUALITY_2026-09-18.md`,
`BLOCK_RESTRICTION_IDENTITY_2026-09-18.md`, and
`SIGNED_BALANCE_AND_LINEAR_BASIS_BARRIER_2026-09-18.md`.

### 2.3 Signed cancellation: exact but not scale-local

For every nonzero spectral translation `U`, the total absolute coefficient
overlap on same-sign pairs equals that on opposite-sign pairs. A one-point
defect family nevertheless puts all logarithmic edge cost on one
opposite-sign scale while same-sign edges have zero log ratio. The signed
identity alone therefore supplies no magnitude-scale transport.

The same family has generalized influence `2/2^n` in every nonzero direction.
Every fixed spanning family of linear spectral coordinates incurs a marginal
entropy loss unbounded relative to actual influence. Fixed changes of basis
cannot repair marginal coding.

### 2.4 A contracting logarithmic potential for disjoint NAND

For an indicator `A` of mean `alpha`, singleton-square mass `Q_A`, and
indicator logarithmic edge functional `K_A`, define

    V(A)=K_A-2Q_A log_2(alpha)+(2/ln2)Q_A.              (5)

If `A'=1-product_j A_j` on disjoint variable blocks and
`w_j=product_(l!=j) E A_l`, then

    V(A')<=sum_j w_j V(A_j),
    I(A')=sum_j w_j I(A_j).                            (6)

Consequently every read-once NAND/De Morgan formula satisfies

    K_log/I <= 2+2/ln2.                                (7)

FEI for read-once formulas was known from composition results; the retained
advance is the explicit unequal-child potential (5)--(6), not a new full
solution.

### 2.5 Sharp barriers to extending that potential by restriction

No fixed singleton correction `U+cQ` makes the NAND potential compatible
with dimension-free one-coordinate restriction. A bent function with one
physical marker gives normalized defect

    [1/4+1/(2ln2)+o(1)]m.                              (8)

The transitive symmetric family

    A_n(x)=1_{|x| mod 8 in {0,1,2}}

defeats favorable-coordinate selection and aggregate coordinate averaging:
every coordinate has

    defect/influence=(0.19751... )n+o(n)               (9)

for every fixed `c`. Equation (9) is proved by an eighth-root spectral
decomposition and checked with exact rational intervals through `n=64`.

### 2.6 Positive class theorems: parity multiplexers

If selector space is partitioned into subcubes and each cell chooses a
distinct signed data parity, then

    H(f)=2H(J)<=4I_x(f)<=4I(f).                        (10)

Ordinary addressing has `H/I=4m/(m+2)->4`, so constant four is sharp within
this class. For an arbitrary parity multiplexer, even without subcube cells,
the data erasure obeys

    B_y(f)<=H(D)<=2I_x(f).                              (11)

If data parities repeat, let `q_A` be the coherently combined selector
spectrum at label `A`, `m_A` its incoherent cell mixture, and

    Lambda=max_(A,S:m_A(S)>0) q_A(S)/m_A(S).

For boundary-separated subcube-character cells,

    H(f)<=4Lambda I_x(f).                              (12)

If every label is used at most `R` times, `Lambda<=R`.

### 2.7 Final structural result: interference patching

The last continuation generalized (12) to arbitrary cells and arbitrary sign
functions. Put `v_j=1_(C_j)sigma_j`, let `delta_j=Pr(C_j)`, and let `E_j` be
the entropy of the normalized spectrum `vhat_j^2/delta_j`. Then

    H(f)
      <=Lambda H(J)-(Lambda-1)H(D_J)
        +Lambda sum_j delta_j E_j
      <=Lambda[H(J)+sum_j delta_j E_j].                (13)

If every cross-cell selector edge separates the two data fibers on at least
half of the data cube, the local Dirichlet energies satisfy the exact
nonreuse bounds

    sum_j D(v_j)<=I_x(f),
    H(J)<=2I_x(f).                                     (14)

Therefore any uniform local leaf estimate

    E_j<=C D(v_j)/delta_j                              (15)

patches to

    H(f)<=Lambda(C+2)I_x(f).                           (16)

For subcube cells whose free-coordinate leaf functions satisfy FEI with
constant `C_0`, one may take `C=max(2,C_0)`. This is a genuine closure
principle with no repeated influence charge. It still requires a constructive
bounded-`Lambda`, boundary-separated decomposition and so does not prove full
FEI.

Full proof: `INTERFERENCE_PATCHING_THEOREM_2026-09-18.md`.

## 3. What is only experimental or computationally suggested

* Early random search through dimensions 5--10 and hill climbing supplied
  examples and falsification targets, but no asymptotic theorem.
* Floating calculations for recursive disjoint NANDs of lexicographic seeds
  produced `B/I` around `4.30`. This motivated abandoning constant four, but
  only the separate 80-variable rational interval certificate is rigorous.
* Exact finite enumeration in older P03 work reported finite-dimension metric
  6. It was preserved as a prior reported fact and was not re-audited or
  extended in this solo track.
* All checker scripts in this folder are self-checks. They support algebraic
  derivations but are not independent audits and cannot establish universal
  statements by enumeration.

## 4. Routes now closed by explicit obstructions

Do not restart the following routes without a genuinely new ingredient.

1. **Positive-power or absolute-overlap majorants:** explicitly unbounded.
2. **Universal local restriction payment:** bent-marker obstruction (8).
3. **Choosing a favorable coordinate or averaging coordinate defects:**
   transitive mod-8 obstruction (9).
4. **A fixed potential `B+lambda(H-B)`, `lambda<1`:** parity erasure synergy.
5. **Bounding only `H-B`:** the even-support parity lift is FEI-complete.
6. **Any fixed linear spectral basis followed by marginal coding:** the
   one-point defect has an unbounded coding loss in every basis.
7. **Independent induction on partial-Boolean branches:** that class is
   FEI-hard, and projections cease to be partial Boolean after iteration.
8. **Using unweighted signed cancellation alone:** cancellation is not local
   in coefficient magnitude.
9. **Composition stability without a seed theorem:** the NAND potential
   propagates bounds but cannot create a bound for arbitrary seeds.
10. **Uncontrolled parity-cell collisions:** point cells with a common label
    already encode arbitrary Boolean functions; `Lambda` can be unbounded.

## 5. Exact remaining gap

No finite universal constant has been proved for any of the equivalent live
targets

    B(f)<=C I(f),
    K_log(f)<=C I(f),
    L(f)<=C I(f).                                      (17)

No Boolean counterexample family with an unbounded ratio has been found
either. Full FEI is therefore unresolved.

The two most sharply formulated surviving routes are:

1. **Signed multiscale transport:** use (4) to transport opposite-sign
   cancellation across coefficient scales while charging each unit of the
   degree budget only once, directly proving `K_log<=CI`.
2. **Constructive interference decomposition:** decompose every Boolean
   function into boundary-separated parity cells with uniformly bounded
   `Lambda`, and leaves satisfying a uniform local bound (15). Then (16)
   would finish FEI. The decomposition must not hide FEI in a single leaf or
   reuse selector boundaries.

A third, less developed option is a proper-block selection theorem for the
conditional entropy term in the exact block-restriction identity. It must
survive the bent-marker, parity-synergy, and transitive mod-8 barriers.

## 6. Reproduction map

The principal exact scripts are:

    python certify_nand80.py
    python check_addressing_barrier.py
    python check_logarithmic_structures.py
    python check_erasure_synergy.py
    python check_block_restriction.py
    python check_signed_basis_barrier.py
    python check_unequal_nand_potential.py
    python check_shannon_potential_barrier.py
    python check_favorable_coordinate_separation.py
    python check_symmetric_mod8_restriction.py
    python check_subcube_parity_multiplexers.py
    python check_bounded_collision_parity_multiplexers.py
    python check_interference_patching.py

The scripts use exact rational Walsh coefficients and, where logarithms occur,
160-bit outward rational intervals. `experiments.py` and
`composition_search.py` contain exploratory floating computations and are
labelled accordingly.

## 7. Literature and novelty caveat

The closest identified sources include the O'Donnell--Tan composition theorem
(`arXiv:1304.1347`), Wan--Wright--Wu on decision-tree protocols
(`arXiv:1312.3003`), Han's influence-profile bound (`arXiv:2312.08271`), and
González--MacManus--Pereyra's stopping-tree restriction framework
(`arXiv:2606.00246v2`). Keyword searches did not identify the exact erasure,
NAND-potential, or interference-patching statements recorded here, but no
complete literature review or independent audit occurred. Novelty is
**UNVERIFIED**.

## 8. Execution accounting

The scheduled window spanned ten wall-clock hours, but the work was performed
in separated continuations. Before this final continuation, the report
checkpoints account for approximately 1 hour 55 minutes 53 seconds of elapsed
retrieval, derivation, checking and writing intervals, using the supplied
start times recorded in each report. GitHub delivery generally occurred after
those checkpoints and is excluded. Gaps between runs are not claimed as work,
and no claim of ten continuous hours is made. The final run's measured interval
is recorded in its timestamped report.
That final interval was 6 minutes 24 seconds, bringing the approximate sum of
all reported checkpoint intervals to 2 hours 2 minutes 17 seconds. The first
session contributes an approximate 21 minutes, so this aggregate is itself
approximate; it is an honest wall-clock accounting, not continuous compute.

## 9. Preservation status

Each substantive continuation was committed to `master` by a non-force
current-head update and read back from the resulting commit. The final commit
and byte-for-byte readback receipt are recorded in the final timestamped run
report. Files outside this solo folder were not modified.
