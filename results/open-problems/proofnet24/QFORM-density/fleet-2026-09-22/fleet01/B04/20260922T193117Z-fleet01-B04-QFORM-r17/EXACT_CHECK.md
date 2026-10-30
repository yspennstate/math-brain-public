# Exact spectral check for the Section 6 example

For the rational matrix

```
A=[[0,1,0,0,3/10],
   [1,0,0,0,-1/5],
   [0,0,0,1,1/4],
   [0,0,1,0,3/20],
   [3/10,-1/5,1/4,3/20,2]],
```

exact symbolic expansion gives

`det(lambda I-A)=(lambda-1)(lambda+1)(200 lambda^3-400 lambda^2-243 lambda+409)/200`.

Thus `+1` and `-1` are exact eigenvalues. For the cubic factor `h(lambda)=200 lambda^3-400 lambda^2-243 lambda+409`,

`h(2)=-77<0`, while `h(3)=1480>0`.

Hence a third eigenvalue lies strictly in `(2,3)`. Therefore the matrix satisfies the target hypothesis of at least three eigenvalues of modulus at least one without relying on floating-point rounding. Numerically its spectrum is

`(-1.043308655226..., -1, 0.925565716565..., 1, 2.117742938661...)`.

The exact determinant is `409/200=2.045`.
