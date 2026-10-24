# Addendum — minimum-distance bonus for the relation-resolved Borel payment

**Status:** proved strengthening of the centered relation theorem; full FEI remains OPEN / NOT PROVED.

The main report used only the universal fact that every nonzero relation in `RM(1,n)^perp` has size at least four. The same argument retains the actual minimum relation size and yields a sharper terminal-code version.

Let every relation coordinate in the packet satisfy

\[
|A|\ge d\ge4.
\]

Define

\[
S_{N,d}(x)=\sum_{k=d}^N k\binom Nkx^k(1-x)^{N-k}.
\]

Then, exactly,

\[
\boxed{
S_{N,d}(x)=Nx\Pr[\operatorname{Bin}(N-1,x)\ge d-1].
}
\tag{A.1}
\]

Using the `(d-1)`-st falling factorial,

\[
\Pr[B\ge d-1]
\le\frac{\mathbb E(B)_{d-1}}{(d-1)!},
\]

so

\[
\boxed{
S_{N,d}(x)
\le
\frac{N(N-1)\cdots(N-d+1)}{(d-1)!}x^d
\le
\frac{N^d}{(d-1)!}x^d.
}
\tag{A.2}
\]

Together with `S_{N,d}(x)<=Nx`, choose

\[
s_0=((d-1)!)^{1/(2d-2)}\sqrt N.
\]

Since `d<=N`, one has `s_0<=N`. For `x=sin^2(s/N)`, the three Borel ranges give

\[
4\int_0^{s_0}\frac{S_{N,d}}{s^3}ds
\le\frac{2}{(d-1)N},
\tag{A.3}
\]

\[
4\int_{s_0}^{N}\frac{S_{N,d}}{s^3}ds
\le
\frac{2\log N-\frac{2}{d-1}\log((d-1)!)}{N},
\tag{A.4}
\]

and

\[
4\int_N^\infty\frac{S_{N,d}}{s^3}ds
\le\frac2N.
\tag{A.5}
\]

Hence the full centered relation packet satisfies the stronger theorem

\[
\boxed{
4\int_0^\infty
\frac{\mathbb E\|V_s-\mathbb EV_s\|_2^2}{s^3}ds
\le C_{N,d}J(f),
}
\tag{A.6}
\]

with

\[
\boxed{
C_{N,d}
=
\frac{
2\log N+2+\frac{2}{d-1}
-\frac{2}{d-1}\log((d-1)!)
}{N}.
}
\tag{A.7}
\]

At `d=4`, (A.7) is exactly the main-report constant

\[
C_{N,4}
=\frac{2\log N+\frac83-\frac23\log6}{N}.
\]

Thus any retained/terminal relation code with minimum distance strictly larger than four receives a free quantitative improvement, without changing the no-reuse live/high/outside ledger and without spending a terminal or R16 credit. The theorem remains a payment only for the physical-translation-centered relation sector; the mean-sector obstruction and q-flip mean identity in the main report are unchanged.
