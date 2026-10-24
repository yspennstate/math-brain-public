# Proof: two exceptional points with reused parity mask

## 1. Fourier law

Translate the input so `z_0=0`, put `D=z_0 xor z_1`, and ignore the global
sign.  Let `N=2^n`, `rho=4/N`, `p=(1-rho)^2`, and `q=rho^2`.
For the unmasked two-defect function, the nonconstant Fourier amplitude is

\[
-\frac2N(1+\chi_T(D)).
\]

It has magnitude `4/N` exactly when `|T cap D|` is even, and vanishes
otherwise.  Multiplication by `chi_A` translates Fourier indices by
symmetric difference with `A`.  Hence

\[
p_f(A)=p,qquad
p_f(T)=q\quad(T\ne A,\ |(T\triangle A)\cap D|\text{ even}),\tag{1}
\]

with zero mass elsewhere.  Since `|E_D|=N/2`,
`p+(N/2-1)q=1`.

## 2. Exact upper masses

For a fixed `S`, count supersets `T` satisfying the parity constraint in
(1).  If some coordinate of `D` is not in `S`, that coordinate toggles the
parity and exactly half of the `2^(n-|S|)` supersets qualify.  If `D subseteq
S`, the parity is fixed, and all or none qualify according as
`d=|D|` has the same parity as `t=|A cap D|`.  Therefore

\[
C_{A,D}(S)=
\begin{cases}
2^{n-|S|-1},&D\nsubseteq S,\\
2^{n-|S|},&D\subseteq S,\ d\equiv t\pmod2,\\
0,&D\subseteq S,\ d\not\equiv t\pmod2.
\end{cases}\tag{2}
\]

The count assigns mass `q` also to the translated zero element `A`; replace
that one mass by `p` when `S subseteq A`.  Thus

\[
\pi_f(S)=qC_{A,D}(S)+(p-q)1_{S\subseteq A}.\tag{3}
\]

Equations (1)--(3) determine `U` exactly, including all zero-mass endpoints.

## 3. Physical restriction law

Let `V_{n,d,r,t}` be the `U` determined by (1)--(3), where
`r=|A|` and `t=|A cap D|`.  Let `P_{m,s}` denote the `U` of a one-point
defect on `m` variables with mask weight `s`.

There are four physical coordinate types.

1. `i in A cap D` (`t` coordinates): each child contains one defect and has
   mask weight `r-1`, contributing `P_{n-1,r-1}` after averaging.
2. `i in D\A` (`d-t` coordinates): both children contain one defect with
   mask weight `r`, contributing `P_{n-1,r}`.
3. `i in A\D` (`r-t` coordinates): one child contains both defects with
   parameters `(n-1,d,r-1,t)`; the other is a pure character with `U=0`.
4. The remaining `n-d-r+t` coordinates: the active two-defect child has
   parameters `(n-1,d,r,t)` and the other child is a character.

Consequently

\[
\begin{aligned}
G={}&nV_{n,d,r,t}-tP_{n-1,r-1}-(d-t)P_{n-1,r}\\
&-\frac{r-t}{2}V_{n-1,d,r-1,t}
-\frac{n-d-r+t}{2}V_{n-1,d,r,t}.
\end{aligned}\tag{4}
\]

Both signs are retained in types 1 and 2; (4) does not project to a chosen
sign.  Types 3 and 4 retain the terminal character before using its exact
zero `U`.

## 4. Sharp unmasked estimate

Set `A=empty`.  Directly summing (3) gives

\[
U_{n,d}=p\log_2(1/p)+qL_{n,d},\tag{5}
\]

where

\[
L_{n,1}=(n-1)(N/4-1),\tag{6}
\]

and, for `d>=2`,

\[
L_{n,d}=(n-2)N/4-(n-1)+1_{d\text{ even}}2^{n-d}.\tag{7}
\]

The influence is

\[
I_{n,1}=4(n-1)/N,\qquad I_{n,d}=4n/N\quad(d>=2).\tag{8}
\]

Every one of the `d` separating coordinates has two point-defect children;
every other coordinate has one two-defect child and one constant.  If `P_m`
denotes unmasked point-defect `U` in dimension `m`, then

\[
G_{n,d}=nU_{n,d}-dP_{n-1}-\frac{n-d}{2}U_{n-1,d}.\tag{9}
\]

The identity `U_{n,1}=P_{n-1}` shows that `G_{n,1}` is precisely the
point-defect `G` in dimension `n-1`.  Also `L_{n,2}=L_{n,1}`, giving

\[
G_{n,2}=\frac{n-2}{n-1}G_{n,1}.\tag{10}
\]

For `d>=3`, define

\[
\delta_{n,d}=L_{n,1}-L_{n,d}
=\begin{cases}N/4,&d\text{ odd},\\N/4-2^{n-d},&d\text{ even}.
\end{cases}
\]

It is nonnegative and `delta_{n-1,d}=delta_{n,d}/2`.  Substitution in (9)
gives the exact signed correction

\[
G_{n,d}=\frac{n-d}{n-1}G_{n,1}-dq\delta_{n,d}.\tag{11}
\]

The accepted point-defect theorem has

\[
G_{n,1}/I_{n,1}\le
\kappa_{pd}=\frac14+\frac94\log_2\frac{16}{9}.
\]

Using (8), (10), and (11),

\[
\frac{G_{n,d}}{I_{n,d}}
\le\frac{n-d}{n}\frac{G_{n,1}}{I_{n,1}}
\le\kappa_{pd}\qquad(d>=2).\tag{12}
\]

The complete unmasked two-defect family therefore has the same sharp
constant; equality is inherited at `(n,d)=(4,1)`.

## 5. Arbitrary same-block parity mask

Assume `A` is nonempty.  The heavy atom in (1) contributes `|A|p` to
influence, so `I(f)>=p`.  Since every child `U` is nonnegative,

\[
G(f)\le nU(f)\le nH(p_f).\tag{13}
\]

The entropy of (1) depends only on `n`:

\[
H(p_f)=-p\log_2p-(N/2-1)q\log_2q.\tag{14}
\]

For `n=2`, every such function is a character or constant and `G=0`.  For
`n=3`, (1) has at most four supported atoms, hence
`nH<=6<=8=32p`.  For `n>=4`, `rho<=1/4`, and

\[
H(p_f)\le\frac{1-p}{\ln2}+\frac2\rho\rho^2\,2(n-2)
\le\rho(4n-5).\tag{15}
\]

The sequence `n(4n-5)/2^(n-2)` decreases for `n>=4`, since
`4n^2-13n+1>0`, and begins at 11.  Meanwhile
`32p>=32(3/4)^2=18`.  Therefore `nH<=32p<=32I`; together with (13),

\[
G(f)\le32I(f).\tag{16}
\]

## 6. Closure and limitation

Disjoint products add `U,G,I` exactly.  Restrictions of a two-defect factor
produce either two one-defect children or a two-defect child plus a
character.  Including the previously proved one-defect class and characters
makes the generated product class restriction closed.  Thus (16) yields
`U<=32I`, and the reviewed entropy reduction gives `H<=66I`, on this class.

An arbitrary negative set has two unrelated multi-defect children, which is
not reduced by this theorem.  The next bridge is the three-defect recursion
(one-defect versus two-defect), followed by a normalized arbitrary-set score
whose constant must not grow with defect count.

