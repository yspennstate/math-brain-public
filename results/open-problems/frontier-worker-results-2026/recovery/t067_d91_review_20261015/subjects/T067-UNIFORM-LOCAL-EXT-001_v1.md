# Three-state critical local radius x<=1/10 for every d>=42

T067-UNIFORM-LOCAL-EXT-001 v1. Status: proof (unaudited).
No priority assertion. The reviewed UNIFORM-LOCAL-001 v1 remains unchanged.

For integer d>=42, lambda=1/sqrt(d), let mu be a permutation-invariant,
uniform-mean posterior-law BP fixed point for the three-state ferromagnetic
Potts process on the regular d-ary tree. If x=E||3p-1||^2/9<=1/10,
then mu is the uniform point mass. This is a local fixed-point statement;
it asserts neither global canonical entry nor an unqualified cutoff42.

Use the exact prefix drift criterion (11),(12) of UNIFORM-LOCAL-001 v1,
with Mstar=9/10 and delta=1/20. In its notation,

  (1-delta)g_k-Mstar A_k-Mstar^2 B_k>=0,                (1)

implies M_k<=kM/d-delta g_k M^2<kM/d for 0<M<=Mstar,
where g_k=k(k-1)/(12d^2)>0 and k=2,...,d. Induction on k and the final
fixed-point equality M_d=M give a contradiction. The derivation of this
criterion uses only the reviewed CUBIC-FUSION and TERNARY-MOMENTS F2,C
inequalities, actual lambda<=2887/5000, and nonnegative coefficients for
integer 2<=k<=d. These hypotheses hold throughout our parameter range.

Here we extend only the exact rectangle on which (1) is certified. Write
l=lambda, d=1/l^2, k=2+r(d-2), 0<=r<=1, and l=Lz, 0<=z<=1.
Take L=39/250. Clearing denominators in (1) multiplies it by
1920(1-l)^3(1+l)^3>0 for actual l>0. The resulting polynomial in (z,r)
has bidegree (17,6). All its tensor Bernstein coefficients on [0,1]^2
are nonnegative:120 strictly positive and6 zero. Thus (1) holds on the
whole closed rectangle, including every actual integer pair (d,k) considered.
At z=0 only the continuous polynomial certificate is used; no infinite d
is substituted into a probabilistic recurrence.

Since 42(39/250)^2=63882/62500>1, every d>=42 has critical lambda<=L.
This covers all these d at once, not merely sampled or square degrees.

The first feasibility calculation rescaled the previously certified raw
polynomial H(z,r) to H((39/25)z,r). This is exact because the only change
is l=(1/10)z to l=(39/250)z, while Mstar and delta stay fixed. It is not
the basis of the final claim alone: a fresh full rational/symbolic rebuild
with the new L reproduced120 positive and6 zero coefficients.

The separate checker uniform_local_extension_independent.py imports no
producer or computer-algebra package. It cancels powers of l in the prefix
sums first, reconstructs their numerator as a Fraction coefficient dictionary,
and proves coefficientwise equality to the fresh raw polynomial after the
recorded positive normalizations. It independently redoes both power-to-
Bernstein transformations by exact rational dot products. It also checks
the unsummed prefix recurrence at32 pairs from d=49,64,81,100,121,144,225,400.
Those finite checks validate encoding; the complete rectangle proves the
unbounded degree assertion. Both original reviewed sources are left intact.

Reproduction:

  python -X utf8 checks/uniform_local_certificate.py --M 9/10 --lambda-max 39/250 --margin 1/20 --name radius01_d42
  python -X utf8 checks/uniform_local_extension_independent.py

Receipts are uniform_local_radius01_d42_{raw,bern1,bern2,report,
fast_independent}.json under checks/. Their hashes accompany the submission.
This is a same-worker reconstruction, not an independent external audit.
