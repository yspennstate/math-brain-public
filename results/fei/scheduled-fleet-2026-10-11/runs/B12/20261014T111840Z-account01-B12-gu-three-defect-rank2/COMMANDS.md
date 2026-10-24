# Commands and deterministic scope

```text
python3 CHECK.py | tee OUTPUT.txt
python3 CERTIFY.py | tee CERTIFICATE.txt
```

`CHECK.py` uses exact `Fraction` Walsh coefficients, laws, upper masses, and
influences.  Binary logarithms are used only for the exploratory ratios.

`CERTIFY.py` replaces every logarithm by a rational interval.  For
`1<=x<2`, it uses

`ln x = 2 sum_{j>=0} z^(2j+1)/(2j+1), z=(x-1)/(x+1)`,

with 80 terms and tail at most
`2 z^(161)/(161(1-z^2))`; powers of two reduce arbitrary rational arguments
to this interval.  There is no seed or floating-point acceptance decision.

