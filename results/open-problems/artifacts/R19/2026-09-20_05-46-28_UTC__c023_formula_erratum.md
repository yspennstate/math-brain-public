# R19-I0084-C023 formula erratum

This is a readback correction to the immutable run report

`runs/R19/2026-09-20_05-46-28_UTC__i0084-mode-location-expansion_c023_m5c12p29.md`

created at commit `4a8d206f2fee4f862f29060736f7eb2564b6da4b`.

The mathematical statements C023A/B/C are unchanged. Two transcription errors occurred in the report body and are corrected here without modifying the immutable report.

## 1. Display (C023.2)

The line rendered as

```tex
+
rac{k''''(m)}{6k''(m)}\frac{\kappa_3}{s^2}
```

must read

```tex
+\frac{k''''(m)}{6k''(m)}\frac{\kappa_3}{s^2}.
```

Thus the intended formula is

\[
M_s
=sm+a
-\frac{k'''(m)}{2k''(m)}\frac{\sigma^2}{s}
+\frac{k''''(m)}{6k''(m)}\frac{\kappa_3}{s^2}
+o(s^{-2}).
\]

## 2. Formal coefficient equations (C023.8)--(C023.9)

Starting from

\[
0=\mathbb E\,k'(m+q(\Delta(q)-Z)),
\qquad q=s^{-1},
\]

the Taylor expansion is

\[
0=Aq\Delta(q)
+\sum_{j\ge2}
\frac{k^{(j+1)}(m)}{j!}
q^j\,\mathbb E[(\Delta(q)-Z)^j].
\tag{C023.8-corrected}
\]

After division by `q`, the correct equation is

\[
0=A\Delta(q)
+\sum_{j\ge2}
\frac{k^{(j+1)}(m)}{j!}
q^{j-1}\,\mathbb E[(\Delta(q)-Z)^j].
\tag{C023.9-corrected}
\]

The immutable report accidentally omitted the factor `q` multiplying `A\Delta(q)` in its first display and consequently printed `A\Delta(q)/q` in the second. The subsequent coefficient calculation in the report used the **corrected** equation above: at order `q`,

\[
Ac_1+\frac{k'''(m)}2\sigma^2=0,
\]

and at order `q^2`,

\[
Ac_2-\frac{k''''(m)}6\kappa_3=0.
\]

Therefore

\[
c_1=-\frac{k'''(m)}{2k''(m)}\sigma^2,
\qquad
c_2=\frac{k''''(m)}{6k''(m)}\kappa_3,
\]

exactly as used in C023A/B/C.

## 3. Minor notation

Where the report prints `\nu_s\to m` immediately after defining `u_s=M_s/s`, read this as

\[
u_s\to m.
\]

No theorem statement, metric, status, or audit claim changes under these corrections.
