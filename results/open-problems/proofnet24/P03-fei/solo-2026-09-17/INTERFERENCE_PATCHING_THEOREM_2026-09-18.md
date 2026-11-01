# An interference patching theorem for Fourier entropy

Status: proved below and self-checked; publication novelty **UNVERIFIED**.
This is a closure principle for structured Boolean functions, not a proof of
the full Friedgut--Kalai Fourier entropy--influence conjecture.

All logarithms are base two.

## 1. Setup

Split the variables as `x in {+1,-1}^m` and `y in {+1,-1}^k`. Partition the
selector cube into arbitrary nonempty cells `C_j`. On each cell choose an
arbitrary sign function `sigma_j:C_j->{+1,-1}` and a data parity
`D_j subseteq [k]`, and define

    f(x,y)=sigma_j(x) chi_(D_j)(y),  x in C_j.          (1)

Extend each signed cell by zero:

    v_j(x)=1_(C_j)(x)sigma_j(x),
    delta_j=Pr[C_j].                                   (2)

Let `J(x)=j`, let `L=D_J`, and define the normalized squared-Fourier law and
entropy of cell `j` by

    rho_j(S)=vhat_j(S)^2/delta_j,
    E_j=H(rho_j).                                      (3)

For each data label `A`, put

    G_A={j:D_j=A},  delta_A=sum_(j in G_A)delta_j,
    q_A(S)=|sum_(j in G_A)vhat_j(S)|^2/delta_A,
    m_A(S)=sum_(j in G_A)vhat_j(S)^2/delta_A.           (4)

The disjoint physical supports of the `v_j` make both `q_A` and `m_A`
probability laws. Define the pointwise coherent-interference constant

    Lambda=max_(A,S:m_A(S)>0) q_A(S)/m_A(S).            (5)

Then `1<=Lambda<=R`, where `R=max_A |G_A|`, by equality of total masses and
Cauchy--Schwarz.

Finally, call (1) boundary-separated if every selector edge crossing between
two different cells has

    Pr_y[f(x,y)!=f(x^i,y)]>=1/2.                       (6)

This holds automatically if adjacent cells have distinct parity labels.

## 2. Exact patching inequality

**Theorem 1 (spectral patching).** In the setup above,

    H(f)
      <=Lambda H(J)-(Lambda-1)H(L)
        +Lambda sum_j delta_j E_j
      <=Lambda [H(J)+sum_j delta_j E_j].               (7)

**Proof.** Conditional on the data Fourier label `A`, the actual selector
spectrum is `q_A`. The entropy decomposition is therefore

    H(f)=H(L)+sum_A delta_A H(q_A).                     (8)

The dominated-distribution lemma proved in
`BOUNDED_COLLISION_PARITY_MULTIPLEXERS_2026-09-18.md` says that `q<=c m`
implies `H(q)<=cH(m)`. Hence

    H(q_A)<=Lambda H(m_A).                             (9)

Within group `A`, the incoherent law `m_A` is the mixture of `rho_j` with
weights `w_j=delta_j/delta_A`. Introducing and then forgetting the mixture
label gives

    H(m_A)<=H(w^A)+sum_(j in G_A)w_j E_j.              (10)

Since

    H(J)=H(L)+sum_A delta_A H(w^A),                    (11)

substitution of (9)--(11) into (8) proves the first line of (7). The second
uses `Lambda>=1` and `H(L)>=0`. QED.

## 3. Local Dirichlet energies do not reuse global influence

For any real function `v` on the selector cube write

    D(v)=sum_S |S| vhat(S)^2
        =(1/4)sum_i E_x[(v(x)-v(x^i))^2].              (12)

**Theorem 2 (nonreuse).** If (1) is boundary-separated, then

    sum_j D(v_j)<=I_x(f),                              (13)
    H(J)<=2I_x(f).                                     (14)

**Proof of (13).** Fix a directed selector edge `(x,x^i)`. If both endpoints
belong to the same cell `j`, then

    (1/4)sum_l (v_l(x)-v_l(x^i))^2

is zero or one according as the two signs agree or disagree. This is exactly
the fraction of data inputs on which the two fibers of `f` disagree. If the
endpoints belong to different cells, precisely two extended cell functions
are nonzero, so the displayed quantity is `1/2`; boundary separation says
the fiber disagreement is at least `1/2`. Average over `x` and sum over `i`
to obtain (13). QED.

**Proof of (14).** Let

    eta_i=Pr[J(x)!=J(x^i)].

Cube edge isoperimetry applied to each cell, followed by summing and dividing
by two because every cross-cell edge is counted twice, gives

    H(J)=sum_j delta_j log(1/delta_j)<=sum_i eta_i.    (15)

Every such edge has fiber disagreement at least `1/2`, so
`I_x(f)>=sum_i eta_i/2`. This proves (14). QED.

## 4. Closure theorem

**Corollary 3.** Suppose every normalized partial cell spectrum satisfies

    E_j<=C D(v_j)/delta_j                              (16)

for one constant `C`. If the representation is boundary-separated, then

    H(f)<=Lambda(C+2) I_x(f)<=R(C+2)I(f).              (17)

**Proof.** Multiply (16) by `delta_j`, sum, and use (13). Use (14) for the
other term in the second line of (7). QED.

This is the promised patching principle: coherent interference costs only
`Lambda`, partition description costs two units of selector influence, and
all local spectral entropies are paid by Dirichlet energies that add without
reuse.

## 5. Subcube mosaics with nontrivial FEI leaves

Suppose now each `C_j` is a codimension-`r_j` subcube. Identify its free
coordinates with a smaller cube and let `g_j` be the Boolean function equal
to `sigma_j` there. The normalized spectrum of `v_j` is the product of a
uniform law on `2^(r_j)` fixed-coordinate frequencies and the squared-Fourier
law of `g_j`. Therefore

    E_j=r_j+H(g_j),
    D(v_j)/delta_j=r_j/2+I(g_j).                       (18)

If every leaf obeys `H(g_j)<=C_0 I(g_j)`, then

    E_j<=max(2,C_0) D(v_j)/delta_j.                    (19)

Corollary 3 gives the recursive closure bound

    H(f)<=Lambda[max(2,C_0)+2]I_x(f).                  (20)

The previous signed-character theorem is the case in which each `g_j` is a
character. Then its spectrum is a point mass after a translation, and (18)
directly gives `E_j<=2D(v_j)/delta_j`; (17) recovers

    H(f)<=4Lambda I_x(f).                              (21)

Thus the earlier class result is one leaf case of a more general closure
principle.

## 6. Exact scope and surviving gap

The theorem is useful only if the decomposition simplifies the cells while
keeping `Lambda` and `C` bounded and preserving boundary separation. None of
those properties is automatic.

* With one cell, (16) is the original FEI inequality.
* Point cells make `C=2`, but if their data labels collide then `Lambda` can
  grow with the number of points; equal neighboring fibers also violate
  boundary separation.
* A universal normalized entropy bound for arbitrary `{0,+1,-1}`-valued
  cell functions is FEI-hard by the selector-lift and tensor-amplification
  argument already proved in this folder.

Consequently (17) does not solve FEI. It isolates a precise constructive
target: find a canonical recursive parity-cell decomposition with bounded
interference and boundary separation, whose leaves lie in a known FEI class,
without charging any selector edge more than once.

`check_interference_patching.py` verifies (7), (13)--(17), and the exact
Fourier decompositions on an irregular-cell example and on a genuinely
coherent repeated-label example using rational Walsh arithmetic and outward
rational logarithm intervals. These are self-checks, not an independent
audit.

## 7. Prior-art boundary

The closest retrieved results are the O'Donnell--Tan disjoint-block
composition theorem (`arXiv:1304.1347`), the Wan--Wright--Wu decision-tree
protocol bounds (`arXiv:1312.3003`), and the González--MacManus--Pereyra
stopping-tree restriction framework (`arXiv:2606.00246`). The present proof
uses a different physical-cell/coherent-interference decomposition, but a
keyword search cannot establish novelty or non-equivalence to those methods.
No publication novelty is claimed without a full literature comparison.
