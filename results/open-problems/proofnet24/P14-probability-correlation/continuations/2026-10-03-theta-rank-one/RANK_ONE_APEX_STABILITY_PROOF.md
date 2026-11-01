# Rank-one weighted `K_{2,3}` apex stability

## Status

**Proved, conditional only on standard published stability criteria.**  This is
a finite symbolic theorem, not a solution of the general forest negative
association conjecture.  The proof below has an exact author checker and a
separately written audit/checker.

## The theorem

Let `G=K_{2,3}` have endpoint side `{0,1}` and arm side `{2,3,4}`.  Give its
six edges the positive weights

\[
 w_{02}=pa,\quad w_{03}=pb,\quad w_{04}=pc,\qquad
 w_{12}=qa,\quad w_{13}=qb,\quad w_{14}=qc,
\]

where `p,q,a,b,c>0`.  Add an apex `*` adjacent to every vertex of `G`, and let
`z_i` be the weight of the apex edge `*i`.  Then the spanning-forest
polynomial

\[
 P(z)=\sum_{F\text{ forest of }G+*}
       \prod_{e\in F\cap E(G)}w_e\prod_{*i\in F}z_i
\]

is real stable.

Consequently, the five apex-edge indicators form a strongly Rayleigh measure
after arbitrary positive external fields.  In particular they are negatively
associated, and this persists under conditioning on any positive-probability
pattern of apex edges.

This strictly contains the earlier three-parameter family
`(pr,p,p;qr,q,q)`: here all three arm multipliers are independent.  It is the
full positive rank-one `2 x 3` edge-weight matrix, up to a redundant global
rescaling.

## 1. Polynomial construction

For a backbone forest `A` of `G`, with connected components `C`, the permitted
apex edges choose either no vertex or exactly one vertex from each `C`.  Thus

\[
 P(z)=\sum_{A\text{ forest of }G}w(A)
       \prod_{C\in\operatorname{comp}(A)}\left(1+\sum_{i\in C}z_i\right).
\]

There are 54 backbone forests, 32 spoke monomials, and 712 augmented forests
at unit weights.  The checker constructs `P` from this formula without using a
precomputed coefficient table.

For `i != j`, put

\[
 \Delta_{ij}=P_iP_j-PP_{ij}.
\]

The multiaffine Rayleigh criterion says that `P` is real stable exactly when
every `Delta_ij` is nonnegative on `R^5`.  Arm permutations and interchange of
the endpoints reduce the ten pairs to three templates: `(0,1)`, `(0,2)`, and
`(2,3)`.

We repeatedly use the elementary fact that
`A t^2+B t+C >= 0` for all real `t` if `A>0` and
`B^2-4AC<=0`; when `A=0`, the boundary is checked directly.

## 2. Positive forms used in the certificates

Set `s=p+q` and

\[
 R(u,v)=1+s(u+v)+pq(u^2+v^2)+s^2uv+pqs\,uv(u+v).
\]

Every coefficient of `R` is positive.  Also set

\[
\begin{aligned}
 S(a,b,c)={}&1+s(a+b+c)+pq(a^2+b^2+c^2)
 +s^2(ab+ac+bc)\\
 &+pqs\sum_{u\ne v\in\{a,b,c\}}u^2v
 +pqs^2abc(a+b+c)+s^3abc.
\end{aligned}
\]

Again every displayed summand is positive.

The following binary-form test is used throughout.  For
`Q=Ux^2+2Vxy+Wy^2`, positivity of `U` and `UW-V^2` makes `Q` positive
definite.  All determinant identities below are exact polynomial identities.

## 3. Endpoint--endpoint pair

Write

\[
 x=z_3+1+bs,\qquad y=z_4+1+cs,
\]

and regard `Delta_01` as a quadratic in `t=z_2`.  Its leading coefficient is

\[
 A_{01}=pq\{c^2(cp+1)(cq+1)x^2
       +2b^2c^2pqxy+b^2(bp+1)(bq+1)y^2\}.
\]

The determinant of this binary form is

\[
 b^2c^2p^2q^2R(b,c)>0.
\]

Its quadratic discriminant has the factorization

\[
 D_{01}=-4a^2p^2q^2x^2y^2\Phi(x,y),
\]

where

\[
 \Phi=c^2R(a,c)x^2+2b^2c^2pq(1+as)xy+b^2R(a,b)y^2.
\]

The determinant of `Phi` is

\[
 b^2c^2(ap+1)(aq+1)S(a,b,c)>0.
\]

Hence `A_01>0` away from `(x,y)=(0,0)` and `D_01<=0`.  On the axes the
complete expressions are

\[
\begin{aligned}
 \Delta_{01}|_{x=0}&=b^2pq(bp+1)(bq+1)y^2(t+1+as)^2,\\
 \Delta_{01}|_{y=0}&=c^2pq(cp+1)(cq+1)x^2(t+1+as)^2.
\end{aligned}
\]

This includes the origin and proves `Delta_01>=0` everywhere.

## 4. Endpoint--internal pair

Use the same `x,y`, but regard `Delta_02` as a quadratic in `t=z_1`.  Exact
expansion gives

\[
 A_{02}=ap(ap+1)x^2y^2,\qquad D_{02}=D_{01}.
\]

When `xy != 0`, the preceding certificate finishes the proof.  The two
degenerate axes are not inferred by continuity; they are checked exactly:

\[
\begin{aligned}
 \Delta_{02}|_{x=0}&=ab^2pq^2(bq+1)(2+s(a+b))y^2,\\
 \Delta_{02}|_{y=0}&=ac^2pq^2(cq+1)(2+s(a+c))x^2.
\end{aligned}
\]

Thus `Delta_02>=0`.  Endpoint interchange proves the three pairs incident to
endpoint 1, and arm permutations prove all six endpoint--internal pairs.

## 5. Internal--internal pair

Now put

\[
 x=z_0+1+p(a+b+c),\qquad
 y=z_1+1+q(a+b+c),
\]

and view `Delta_23` as a quadratic in the **unused arm variable** `t=z_4`.
This choice is essential.  The leading coefficient is

\[
 A_{23}=ab\{q^2(aq+1)(bq+1)x^2
       +2abp^2q^2xy+p^2(ap+1)(bp+1)y^2\},
\]

whose determinant is

\[
 a^2b^2p^2q^2R(a,b)>0.
\]

The discriminant is

\[
 D_{23}=-4a^2b^2c^2p^2q^2\Omega(x,y).
\]

The form `Omega=U x^2+2Vxy+W y^2` has coefficient-positive diagonal entries
`U,W` (51 monomials each; the exact checker extracts them from `P`, rather
than trusting a transcription).  Its determinant simplifies to

\[
 UW-V^2=p^2q^2(2+s(a+b))(2+s(a+c))(2+s(b+c))S(a,b,c)>0.
\]

Thus `Omega` and `A_23` are positive definite.  At their only common
degenerate point, `x=y=0`, direct substitution gives the positive constant

\[
 \Delta_{23}=abc^2p^2q^2(2+s(a+c))(2+s(b+c)).
\]

Therefore `Delta_23>=0` everywhere.  Arm permutations cover all three
internal--internal pairs.

The three templates cover all ten pairs, so the Rayleigh criterion proves the
theorem.

## 6. Reproduction and audit boundary

Run:

```bash
python theta_rank_one_apex_stability_exact.py
python theta_rank_one_apex_stability_k_independent.py
```

The author checker verifies thirteen structural identities, the four
positive-definite form certificates, and all pair reductions.  Its largest
determinant has 411 expanded positive monomials.  The independent checker uses
a separately constructed polynomial and exact rational profiles.

This proof says nothing about six arbitrary positive weights on `K_{2,3}`;
rank one is used in every determinant factorization.  It also does not settle
the famous forest negative-correlation conjecture for arbitrary graphs.
