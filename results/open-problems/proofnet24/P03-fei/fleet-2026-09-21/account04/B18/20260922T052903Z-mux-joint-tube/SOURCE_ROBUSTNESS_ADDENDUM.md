# Source-robustness addendum for the unequal-data MUX tube

This addendum removes any need to extend the **upper** printed wobble bound of the h96 node table beyond its finite grid. The theorem in `REPORT.md` survives with wider constants using only the globally source-used slope bound `|G'|<31`, the exact center value `G(1)=2C_0=12.9096`, and the inherited account01/B18 reserve.

On the small side, `Gamma_0(u)=uG(x)` with `x=log_2(1/u)`. Since `G(1)=2C_0` and `|G'|<31`, for every `x>=1`,

\[
|G(x)|\le 12.9096+31(x-1)<31x.
\]

Hence, using `1/ln2<3/2` and `a^dagger<1`,

\[
|({\Gamma^\dagger})'(u)|
\le |G(x)|+{|G'(x)|\over\ln2}+a^\dagger
<31x+47.
\tag{A.1}
\]

Along the data perturbation interval the symmetric small-side coordinate is at least `q/2`, so `x<=L+1`, `L=log_2(1/q)`. Combining (A.1) with the entropy derivative estimate already proved in the report,

\[
\left|{d\over du}h_2(V_u)\right|\le4(L+1),
\]
gives the coarser but source-robust bound

\[
|B'(u)|<35L+82,
\qquad B(u)=\Gamma^\dagger(u)+h_2(V_u).
\tag{A.2}
\]

Since the address tube has `t<0.501`, the changed data-price costs less than

\[
(18L+42)|\eta|.
\tag{A.3}
\]

For every center point encountered by the address/output biases we may take `x<2`, so (A.1) gives `|Gamma'|<109`. Therefore the output-potential perturbation is `<55|eta|`. The same derivative bound from `1/2` shows `B(t)<8`. Thus the non-spectral loss is bounded by

\[
(18L+105)|\eta|.
\tag{A.4}
\]

The six-mass Fannes bound from the report is unchanged:

\[
|\Delta H|<5|\eta|\log_2{3\over|\eta|}.
\tag{A.5}
\]

At `|eta|<=q^2/2^18`, (A.4)-(A.5) give total loss at most

\[
{q^2\over2^{18}}
\left[28L+195+5\log_2 3\right].
\tag{A.6}
\]

Using `qL<=1`, `q<=1/2`, and `log_2 3<8/5`, this is strictly less than

\[
{q\over2^{18}}\left(28+{195+8\over2}\right)
={259\over524288}q
<{q\over2000}.
\tag{A.7}
\]

The inherited account01/B18 complementary-data reserve is

\[
D_{\Gamma^\dagger}(M;t,q,1-q)>{89\over4096}q.
\]
Since

\[
{89\over4096}-{1\over2000}-{1\over48}
={607\over1536000}>0,
\tag{A.8}
\]
we again obtain, with no use of a global upper wobble extension,

\[
\boxed{
D_{\Gamma^\dagger}(M;t,q,1-q+\eta)>{q\over48}>0.
}
\]

The margin conclusion `c_M<a^dagger-1/27` is unchanged because it only uses the exact Poincare-currency identity and `W_M<9q/16`.

**Status:** this addendum strengthens the provenance of Theorem 4.1; it does not enlarge its parameter tube and does not close the full unequal-data MUX or full FEI.
