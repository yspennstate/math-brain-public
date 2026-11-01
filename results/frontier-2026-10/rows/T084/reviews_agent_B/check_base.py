import sympy as sp, sys
sys.argv=[sys.argv[0],"0"]
src=open(r"(local file)",encoding="utf-8").read().split("out = {")[0]
exec(src)
want={4:t**4*(2+4*t),5:t**4*(2+24*t+84*t**2+100*t**3),6:t**4*(2+48*t+462*t**2+2172*t**3+5184*t**4+5184*t**5)}
for n,w in want.items():
    _,Z,E,L,D=quantities(n); bZ,bE,bL,bD=brute(n)
    print(n, sp.expand(E**2-Z*D-w)==0, sp.expand(bE**2-bZ*bD-w)==0)
