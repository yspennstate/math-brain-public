# Bounded Fourier interference for subcube parity multiplexers

Status: proved below and self-checked; publication novelty **UNVERIFIED**. This
extends the distinct-label theorem in `SUBCUBE_PARITY_MULTIPLEXERS_2026-09-18.md`
to bounded reuse of data parities. It is not a proof of the full
Friedgut--Kalai conjecture.

All logarithms are base two.

## 1. The theorem

Partition the selector cube into nonempty subcubes

    {+1,-1}^m = disjoint union over j of C_j.

Let `delta_j=2^(-r_j)` be the density of `C_j`, where `r_j` is its
codimension. Assign a data parity `D_j subseteq [k]` and, on each cell, a
signed selector character

    sigma_j(x)=s_j chi_(T_j)(x).

Define

    f(x,y)=sigma_j(x) chi_(D_j)(y),  x in C_j.          (1)

The labels `D_j` may now repeat. Put

    R=max_A |{j:D_j=A}|.                               (2)

There is a sharper interference parameter. Define `q_A,m_A` as in
(14)--(15) below, and put

    Lambda_A=max_(S:m_A(S)>0) q_A(S)/m_A(S),
    Lambda=max_A Lambda_A.                             (3)

Both laws have total mass one, so `1<=Lambda_A`; Cauchy--Schwarz gives
`Lambda_A<=|{j:D_j=A}|`, and hence `Lambda<=R`.

Assume also that the partition representation is **boundary-separated**:
whenever a selector edge has endpoints `x in C_j` and `x' in C_l`, with
`j!=l`,

    Pr_y[f(x,y)!=f(x',y)] >= 1/2.                      (4)

Condition (4) is automatic when adjacent cells have different data-parity
labels. When their labels coincide, it says that the two endpoint signs must
be opposite.

Then the sharper bound is

    H(f) <= 2 Lambda H(J)-(Lambda-1)H(L)
         <= 2 Lambda H(J)
         <= 4 Lambda I_x(f)
         <= 4R I(f),                                   (5)

where `J(x)=j` is the selector-cell label and `L=D_J` is its coarse
data-parity label. Thus the loss is controlled by the actual pointwise
Fourier interference, and in particular bounded collision of at most `R`
subcube spectra loses at most the factor `R`.

For `R=1`, the earlier sharper identity `H(f)=2H(J)` is recovered. The new
content is that exact nonoverlap is unnecessary: pointwise domination of the
coherent spectrum by an incoherent mixture suffices.

## 2. Entropy lemma for a dominated distribution

**Lemma.** Let `q=(q_z)` and `m=(m_z)` be probability distributions on a
finite set. If

    q_z <= R m_z                                                   (6)

for every `z`, where `R>=1`, then

    H(q)<=R H(m).                                                  (7)

**Proof.** Set `theta_z=q_z/(R m_z)` when `m_z>0`, and zero otherwise.
Then `0<=theta_z<=1` and

    sum_z m_z theta_z=1/R.                                        (8)

Writing `phi(t)=t log(1/(Rt))`, with `phi(0)=0`, gives

    H(q)
      =R sum_z m_z theta_z log(1/m_z)
        +R sum_z m_z phi(theta_z).                                (9)

The first term is at most `R H(m)`. The function `phi` is concave on
`[0,1]`, so Jensen and (8) give

    sum_z m_z phi(theta_z)<=phi(1/R)=0.                           (10)

This proves (7). Notice that no additive `log R` loss appears.  QED.

## 3. Coherent groups and their incoherent majorants

Put

    v_j(x)=1_(C_j)(x)sigma_j(x),
    G_A={j:D_j=A},
    v_A=sum_(j in G_A) v_j,
    delta_A=sum_(j in G_A) delta_j.                               (11)

The physical supports of the `v_j` are disjoint. Consequently Parseval gives

    ||v_A||_2^2=delta_A.                                          (12)

The data Fourier subset `Y` of (1) therefore has law

    Pr[Y=A]=delta_A.                                              (13)

Conditional on `Y=A`, define the actual, coherently combined selector law

    q_A(S)=|sum_(j in G_A) vhat_j(S)|^2/delta_A,                  (14)

and the incoherent mixture

    m_A(S)=sum_(j in G_A) |vhat_j(S)|^2/delta_A.                 (15)

Both are probability laws by (12). If `r_A=|G_A|`, Cauchy--Schwarz gives,
pointwise in `S`,

    q_A(S)<=r_A m_A(S)<=R m_A(S).                                (16)

By the definition of `Lambda_A`, the entropy lemma gives the sharper

    H(q_A)<=Lambda_A H(m_A)<=Lambda H(m_A).                       (17)

Let `w_j=delta_j/delta_A` inside group `A`. Each normalized component law

    |vhat_j(S)|^2/delta_j

is uniform on `2^(r_j)` points, because `C_j` is a codimension-`r_j`
subcube and `sigma_j` is a character. Introduce a latent component label
with law `w`. Forgetting that label cannot increase joint entropy, so

    H(m_A)<=H(w^A)+sum_(j in G_A) w_j r_j.                        (18)

This upper bound remains valid even if the component Fourier supports
overlap.

## 4. Summing the groups

Let `L=D_J` be the coarse data-parity label. By (13)--(14), the full squared
Fourier law obeys

    H(f)=H(L)+sum_A delta_A H(q_A).                               (19)

Using (17)--(18),

    H(f)
      <=H(L)+Lambda sum_A delta_A H(w^A)
        +Lambda sum_j delta_j r_j.                               (20)

The elementary chain rule and the subcube densities give

    H(J)=H(L)+sum_A delta_A H(w^A),
    sum_j delta_j r_j=H(J).                                      (21)

Substitution into (19) yields the slightly sharper form

    H(f)<=2Lambda H(J)-(Lambda-1)H(L)<=2Lambda H(J).              (22)

This proves the first inequality in (5).

## 5. Paying for cell boundaries

For selector direction `i`, set

    eta_i=Pr_x[J(x)!=J(x flipped at i)].                          (23)

Applying edge isoperimetry to every cell and dividing by two because every
cross-cell edge is counted twice gives

    H(J)=sum_j delta_j log(1/delta_j)<=sum_i eta_i.               (24)

Under boundary separation (4), every cross-cell edge contributes at least
one half to the corresponding selector influence. Hence

    I_x(f)>=1/2 sum_i eta_i>=H(J)/2.                             (25)

Combining (22) and (25) proves (5).

## 6. Why both hypotheses matter

The collision and boundary assumptions address different obstructions.

* Without bounded collision, Cauchy--Schwarz has an unbounded multiplicity
  loss. Indeed, a point-cell representation in which every cell uses the
  same data label contains an arbitrary Boolean selector function. A
  universal theorem for that unrestricted representation would include the
  full FEI conjecture.
* Without boundary separation, the chosen partition can encode entropy that
  the function does not see. Two adjacent cells can carry the identical
  fiber, producing a cell boundary with zero influence. Merging all such
  cells need not preserve the subcube-cell hypothesis.
* Without subcube cells and character signs, (17) becomes a Fourier-entropy
  bound for normalized partial Boolean functions. Earlier notes show that
  class is FEI-hard.

Thus (5) is a genuine controlled-interference extension, but it does not
provide a bounded-collision decomposition of arbitrary Boolean functions.
That decomposition, with boundary costs not reused, is the remaining missing
step for this route.

`check_bounded_collision_parity_multiplexers.py` checks all identities,
pointwise domination, boundary separation and the theorem for explicit
repeated-label examples using exact rational Walsh arithmetic and outward
rational logarithm intervals. The universal assertions are proved above;
the finite computations are self-checks, not an independent audit.

## 7. Prior-art check

Searches on 2026-09-18 for combinations of “Fourier entropy influence”,
“parity multiplexer”, “addressing function”, “subcube”, “bounded overlap” and
“coherent mixture” found the O'Donnell--Tan composition theorem
(`arXiv:1304.1347`), O'Donnell--Wright--Zhou's read-once decision-tree class,
Shalev's read-k decision-tree bound (`arXiv:1806.03646`), Han's general
influence-profile bound (`arXiv:2312.08271`), and the recent
restriction-induction paper (`arXiv:2606.00246`). No retrieved source stated
the theorem above. This was a limited keyword search, not a literature
review; publication novelty remains **UNVERIFIED**.
