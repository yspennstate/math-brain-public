import sympy as S,json,pathlib
c=S.symbols('c',real=True);I=S.I
L=S.Matrix([[S.Rational(1,4),I/4,c],[I/4,S.Rational(1,4),I/4],[c,I/4,S.Rational(1,4)]])
u=S.diag(-I-1,-2,I-1)
d=S.factor((S.eye(3)+u*L).det());print('det =',d)
P=pathlib.Path('.')
# Values of the relevant Fourier coefficient from the prior numerical implementation.
src=(P/'distinct_fusion_checks.py').read_text(encoding='utf-8-sig').split('start=time.time();G=kernel_grid(128)')[0];exec(compile(src,'distinct_fusion_definitions','exec'))
for N in [64,128,256,512]:
 G=kernel_grid(N);print('N',N,'c=',1j*G((2,1)),'G30',G((3,0)))
(P/'local_fusion_symbolic.txt').write_text('For L=[[1/4,i/4,c],[i/4,1/4,i/4],[c,i/4,1/4]] and u=(-i,-1,i), det(I+diag(u-1)L)='+str(d)+'\n',encoding='utf8')
