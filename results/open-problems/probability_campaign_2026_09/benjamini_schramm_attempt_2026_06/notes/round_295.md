# Round 295

Round 295 keeps the few-start multiplicity before exact-start localization is
spent.

The first new corollary is
```tex
\begin{corollary}[Few-start chains with enough levels are record spread]
\label{cor:few-start-chains-with-enough-levels-are-record-spread}
```
It says that if
\[
  \ell>\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H ,
\]
then every \(q\)-start chain profile is already bounded by the prefix-record
outward-spread profile.  This follows because \(q\ge1\) gives at least one
exact start, and a single exact-start chain of such length supplies enough
record crossing levels.

The main large-window consequence is
```tex
\begin{corollary}[Large-window exceptions retain surplus starts]
\label{cor:large-window-exceptions-retain-surplus-starts}
```
Let
\[
  A_r=\frac{\theta_{\lambda,\sigma,\beta}}{4K_{r+1}}L_H,
  \qquad q_{r,p}=\lfloor A_r\rfloor+1,
\]
and
\[
  \mathcal E_r=\{h\in\{1,\ldots,B_r\}:\ell_r+h\le A_r\}.
\]
Then
\[
\begin{aligned}
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le&
  \sum_{h\in\mathcal E_r}
  P^{\rm chain,qstart}_{j,K_{r+1},L,\ell_r+h,q_{r,p}}
\\
  &+
  B_r P^{\rm pre,out,rec}_{j,K_{r+1},L}.
\end{aligned}
\]

For every exceptional \(h\), one has
\[
  q_{r,p}>\ell_r+h,\qquad q_{r,p}\in\{4,5\}.
\]
Thus the only remaining exceptional few-start types are
\[
  (\ell_r+h,q_{r,p})\in\{(3,4),(3,5),(4,5)\}.
\]

This is stronger than the Round 294 exact-start exception statement in two
ways:

- the exception retains surplus-start multiplicity rather than becoming a
  single exact-start profile;
- the record-spread coefficient is \(B_r<W_{\beta,p}\), rather than the
  residual-localized \(O(W_{\beta,p}^2)\) coefficient.

The large-window novelty is now reduced to at most two finite surplus-start
profiles of types \((3,4)\), \((3,5)\), and \((4,5)\).
