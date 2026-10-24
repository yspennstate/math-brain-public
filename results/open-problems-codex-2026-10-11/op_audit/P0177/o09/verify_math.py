from pathlib import Path
import json
import sympy as S
import mpmath as mp

ROOT=Path(__file__).resolve().parent
z,u,R,x,s=S.symbols('z u R x s', positive=True)
v,c3,c4,c5=S.symbols('v c3 c4 c5')
identity=S.factor((1-3*z)/(1+z)**3-(1-6*z))
assert S.simplify(identity-z**2*(15+17*z+6*z**2)/(1+z)**3)==0
assert S.simplify(S.diff(1/(R+(u-x)**2),u,2)+2*(R-3*(u-x)**2)/(R+(u-x)**2)**3)==0
r=1-v*s+(c4-v*v)*s*s
uf=-2*c3*s+(3*c5-14*v*c3)*s*s
q3=uf**3+3*v*uf-c3
q5=uf**5+10*v*uf**3-10*c3*uf**2+5*c4*uf-c5
assert S.series(uf-2*s/r*q3+3*s*s/r**2*q5,s,0,3).removeO().expand()==0
mf=S.series(uf+uf/r-s/r**2*q3+s*s/r**3*q5,s,0,3).removeO().expand()
assert S.simplify(mf-(-3*c3*s+(5*c5-22*v*c3)*s*s))==0
hc=-c3*s/2+(c5-6*v*c3)*s*s/8
assert S.series(-hc-s/2*(c3-3*v*hc-hc**3)+s*s/8*(c5-5*c4*hc+10*c3*hc**2-10*v*hc**3-hc**5),s,0,3).removeO().expand()==0
print('Exact identity, F_uu, and both expansion checks PASS', flush=True)

mp.mp.dps=65
laws=[('skew_two',[-1,2],[mp.mpf(2)/3,mp.mpf(1)/3]),
      ('skew_three',[-5,0,3],[mp.mpf(1)/10,mp.mpf(6)/10,mp.mpf(3)/10]),
      ('remote_tiny',[-1,0,1000],[mp.mpf('0.3'),mp.mpf('0.699999'),mp.mpf('0.000001')]),
      ('symmetric',[-4,0,4],[mp.mpf('0.2'),mp.mpf('0.6'),mp.mpf('0.2')])]
output=[]
for name,xs,ws in laws:
    mean=sum(w*x for w,x in zip(ws,xs)); ys=[mp.mpf(x)-mean for x in xs]
    E=lambda f: sum(w*f(y) for w,y in zip(ws,ys))
    vv=E(lambda y:y*y); m3=E(lambda y:y**3); m5=E(lambda y:y**5)
    B=(mp.sqrt(2)+2)*mp.sqrt(vv); A=B*B+vv
    times=[8*A,mp.mpf(10)**5,mp.mpf(10)**6,mp.mpf(10)**7]
    for t in times:
        h=mp.findroot(lambda h:E(lambda y:(y-h)*mp.exp(-(y-h)**2/(2*t))),0)
        def eq(uu,rr):
            return E(lambda y:1/(rr+(uu-y)**2))-1/t,E(lambda y:(uu-y)/(rr+(uu-y)**2)**2)
        uu,rr=mp.findroot(eq,(0,t-vv),tol=mp.mpf('1e-60'),maxsteps=100)
        physical=uu+t*E(lambda y:(uu-y)/(rr+(uu-y)**2))
        cc=-m3/(2*t)+(m5-6*vv*m3)/(8*t*t)
        ff=-3*m3/t+(5*m5-22*vv*m3)/(t*t)
        assert abs(uu)<=B and rr>=t-vv and rr<=t
        assert abs(physical)<=64*(B**3+E(lambda y:abs(y)**3))/t
        # Fixed-height concavity throughout the interval containing all maxima.
        grid=[-B+2*B*i/100 for i in range(101)]
        max_curvature=max(-2*E(lambda y:(rr-3*(q-y)**2)/(rr+(q-y)**2)**3) for q in grid)
        assert max_curvature<0
        record={'law':name,'t':str(t),'classical':str(h),'free':str(physical),'t3_classical_error':str(t**3*(h-cc)), 't3_free_error':str(t**3*(physical-ff)), 'max_Fuu':str(max_curvature),'residual':str(max(abs(a) for a in eq(uu,rr)))}
        output.append(record)
        print(name,'t=',mp.nstr(t,7),'t^3 errors=',mp.nstr(t**3*(h-cc),10),mp.nstr(t**3*(physical-ff),10),flush=True)
(ROOT/'independent_math_results.json').write_text(json.dumps({'exact_checks':'PASS','numeric':output},indent=2),encoding='utf-8')

# Direct pointwise inequality / Taylor remainder stress checks on log-spaced z.
for zz in [mp.mpf(0)]+[mp.power(10,mp.mpf(k)/10) for k in range(-100,101)]:
    assert (1-zz)*mp.exp(-zz/2)>=1-3*zz/2-mp.mpf('1e-60')
    assert abs(1/(1+zz)-(1-zz+zz*zz))<=zz**3+mp.mpf('1e-60')
    assert abs(1/(1+zz)**2-(1-2*zz+3*zz*zz))<=4*zz**3+mp.mpf('1e-60')
print('Pointwise inequalities and remainder stress checks PASS',flush=True)

# Read-only numbered snapshots of the requested claimant text, in the audit folder.
claim=Path('~/brain_workers/TRIO_1011/op/P0177')
for name in ['ATTEMPT.md','STATUS.md','CLAIMS.jsonl','LITERATURE.md']:
    lines=(claim/name).read_text(encoding='utf-8').splitlines()
    (ROOT/(name+'.numbered.txt')).write_text('\n'.join(f'{i}: {line}' for i,line in enumerate(lines,1)),encoding='utf-8')
print('Read-only dossier snapshots saved',flush=True)
