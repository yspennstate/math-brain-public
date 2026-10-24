# Round 353

Round 353 splits the eighth prefix-record profile from Round 352 into a
persistent prefix profile plus adjacent return-spread terms.

Round 352 left
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i}.
\]
Applying the short prefix-record persistent-or-returning split with
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le{}&
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]
Here
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}.
\]

Substitution into the Round 352 finite ladder replaces
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
by the same coefficient times
\[
\begin{aligned}
  &P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}\\
  &\quad+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]
The long-run coefficient
\(A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\) is
unchanged.  The eighth bridge-return family, the older adjacent return-spread
families, all earlier bridge-return and return-spread families,
staircase/local bridge, enlarged spread-return, and exact-level return terms
are retained.

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the ninth persistent prefix profile
\(P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}\),
which should next be converted to a bounded-gap prefix-pair profile,
paralleling Round 348.

No external literature refresh was performed in this round; the Round 339
source-checked status remains the latest external status.
