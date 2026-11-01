# C088 arithmetic refinement — still before checker code

The U070 theorem is unchanged. For the concrete C088 class, replace the initial transcendental-floor choice by the completely arithmetic sequence

\[
d_N:=1+\lfloor\log_2 N\rfloor,\qquad
b_N:=\left\lfloor\frac{N^3}{d_N}\right\rfloor,
\qquad N\ge2.
\]

This keeps the intended near-cubic scale while making the construction/checker exact from integers alone:

\[
\frac{b_N}{N^3}\le\frac1{d_N}\to0,
\qquad b_N\to\infty.
\]

Thus U070 applies.

At N=4, `d_4=3`, `b_4=21`. For the active mark x=3/4,

\[
\left\lfloor 21\frac{\log 3}{\log 4}\right\rfloor=16
\]

is certified without floating point by

\[
4^{16}\le 3^{21}<4^{17}.
\]

Therefore

\[
p_3=\frac{3^{21}}{3^{21}+4^{16}}
=\frac{10460353203}{14755320499}.
\]

With p_1=1/4, p_2=1/2 and clocks (2/3,1/2,2/3), exact arithmetic gives

\[
q(1,3)=
\frac{671719225794208878674503239067708227939609}
{3033713490564534526429152960383315213952064},
\]

\[
q(2,2)=
\frac{504051268651873282255855271645250407701495}
{3033713490564534526429152960383315213952064},
\]

\[
\Lambda_{\rm root}=
\frac{4199030709132455361465578771206584134862921}
{3033713490564534526429152960383315213952064},
\]

and

\[
P_{C088}(2\mid2)=
\frac{504051268651873282255855271645250407701495}
{1399676903044151787155192923735528044954307}.
\]

Against source CTCS(4),

\[
P_{C088}(2\mid2)-\frac3{11}
=
\frac{1345533246038150743348829216891170349853524}
{15396445933485669658707122161090808494497377}>0.
\]

Against C087,

\[
P_{C088}(2\mid2)-\frac{5387590087}{13835074771}
=
-\frac{12070179098456533246249065760074943130593557184512}
{412013502316118244458837691081087896406601843052951}\ne0.
\]

This refined C088 is the version to certify in code and report.