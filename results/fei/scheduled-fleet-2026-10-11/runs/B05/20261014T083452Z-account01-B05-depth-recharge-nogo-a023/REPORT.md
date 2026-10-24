# B05 / A023 — fixed-dimension depth recharge no-go

**Run:** `20261014T083452Z-account01-B05-depth-recharge-nogo-a023`  
**Primary packet:** A023  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim:** `B05-A023-DEPTH-RECHARGE-NOGO-v1`  
**Status:** **PROVED ROUTE OBSTRUCTION, PENDING INDEPENDENT REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Frozen candidate and GU implication

For a sequence of two-coordinate blocks with consecutive one-coordinate
overlap, define the positive variation

\[
V^+(f;{\cal X})=
\sum_t[\widetilde\Lambda_{X_{t+1}}(f)
-\widetilde\Lambda_{X_t}(f)]_+.
\]

The candidate was a dimension- and depth-independent estimate

\[
V^+(f;{\cal X})\le CI(f). \tag{PV}
\]

Together with an existing \(a_0I+bU\), \(b<1\), payment for the other
node terms, (PV) would yield GU with \((a,b)=(a_0+C,b)\) on the reused
overlap hierarchy.  It is therefore an exact assembly helper, not GU
itself.

## Result

(PV) is false even for one fixed four-variable Boolean sign.  Let

\[
f(y,x,z,u)=x\ (y=1),\qquad f(y,x,z,u)=zu\ (y=-1),
\]

and alternate

\[
X=\{y,x\},\qquad Y=\{y,z\}.
\]

Exact orbit accounting gives

\[
\widetilde\Lambda_Y(f)-\widetilde\Lambda_X(f)=\frac1{\ln2},
\qquad I(f)=2,
\]

with every coordinate influence equal to \(1/2\).  Along
\(X,Y,X,Y,\ldots,X,Y\) with \(2r-1\) swaps,

\[
\boxed{V^+(f;{\cal X}_r)=\frac r{\ln2}\to\infty.}
\]

Thus neither total influence paid once nor all union-block influences paid
once can control a memoryless nonnegative per-swap ledger.

The signed ledger behaves completely differently:

\[
\sum_t(\widetilde\Lambda_{X_{t+1}}-widetilde\Lambda_{X_t})
=\frac1{\ln2},
\]

independent of \(r\).  The precise surviving mechanism is therefore signed
refund retention or persistent packet ownership.

## Delta from the reviewed one-swap obstruction

The reviewed majority family showed an unbounded one-swap cost as private
dimension grows.  This run fixes the dimension, function, influence, and
orbit energies and instead proves unbounded recharge with overlap depth.
It rules out arbitrary-depth memoryless assembly, not merely a local fee at
one transition.

It does not rule out acyclic reveal trees, persistent ownership, signed
\(K-\Gamma\) cancellation, GU, or FEI.

## Verification and next action

Exact Fraction Walsh reconstruction verifies every coefficient, orbit
energy, and influence.  The symbolic identity
\(q(1/2)-1/2=1/\ln2\) proves the sign.

The next A023 attempt must implement persistent ownership at the level of
the entire transported slice and prove that, on an acyclic physical reveal
tree, each packet is closed exactly once while the retained negative swap
refund matches an actual \(\Gamma_i-K_i\) credit.

Fresh independent review is required from A087 or A090.  Model: Codex;
reasoning effort metadata: UNKNOWN.

