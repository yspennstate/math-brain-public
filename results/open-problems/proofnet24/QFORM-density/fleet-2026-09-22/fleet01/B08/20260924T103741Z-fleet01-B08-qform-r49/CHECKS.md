# fleet01/B08 r49 exact arithmetic checks

These are exact/radical checks supporting `REPORT.md`; no simulation or Monte Carlo is used.

1. Balanced-frame deviation threshold:

`47/96-3/10 = 91/480`.

The second-moment/Markov bound is

`(1/64)(480/91)^2 = 3600/8281 = 0.4347301050...`.

2. Two-sided star Chebyshev gate:

`Var Z < B^4/1024`, and the failure of either `Z>=2B^2/5` or `B^2-Z>=2B^2/5` implies `|Z-B^2/2|>B^2/10`. Hence

`P(star bad)<100/1024=25/256=0.09765625`.

The union bound is

`3600/8281+25/256 = 1128625/2119936 = 0.5323863550597754... <1`.

3. Inherited partner scale:

`sigma=(1/2)sqrt(67/800)=0.14469796128487783...`,

so

`sigma/8=0.01808724516060973...`.

4. Bilateral nonalignment crossing gate, using

`rho=0.0006247538095703261` and `sqrt(2/5)=0.6324555320336759...`:

`kappa_bi=[sigma^2 (sqrt(2/5)rho/2)]^(1/3)
          =0.016052570248452247...`.

Therefore

`6^(4/3)/kappa_bi = 679.1886525488995... <679.189`.

5. Four-bank mass threshold:

`1/4-5/512=123/512`,

`a=sqrt(123/512)=sqrt(246)/32=0.49013709816744133...`.

For two bad banks,

`2(a-1/8)^2=(131-4sqrt(246))/256
            =0.2666502009162794... >1/4`.

The strict inequality is equivalent to `67>4sqrt(246)`; squaring gives `4489>3936`.

6. Five-large-eigenvalue induction cost:

`1/sigma=sqrt(3200/67)=6.91094740465088... <6.911`.

`QFORM_B08_R49_CHECK_PASS`
