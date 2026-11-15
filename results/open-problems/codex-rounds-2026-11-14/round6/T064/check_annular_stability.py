#!/usr/bin/env python3
"""Small deterministic audits for PROOF.md; no file writes or sampling.

env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
    nice -n 15 python3 -B check_annular_stability.py
"""
import ctypes
import itertools
import math
import os
import resource
import sys
import time


def guard():
    libc = ctypes.CDLL(None, use_errno=True)
    libc.getpriority.argtypes = (ctypes.c_int, ctypes.c_uint)
    libc.getpriority.restype = ctypes.c_int
    ctypes.set_errno(0)
    priority = libc.getpriority(0, 0)
    assert not ctypes.get_errno() and priority >= 15, priority
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    print(f'niceness={priority}; threads=1; CPU cap=60s')
    try:
        jn = libc.jn
    except AttributeError:
        from ctypes import util
        jn = ctypes.CDLL(util.find_library('m')).jn
    jn.argtypes = (ctypes.c_int, ctypes.c_double)
    jn.restype = ctypes.c_double
    return jn


def close(x, y, tol=2e-11):
    assert abs(x-y) <= tol, (x, y, abs(x-y), tol)


def zeros(n):
    return [[0.]*n for _ in range(n)]


def outer_add(matrix, vec, scale=1.):
    for i, x in enumerate(vec):
        for j, y in enumerate(vec):
            matrix[i][j] += scale*x*y


def cholesky(matrix):
    n = len(matrix)
    result = zeros(n)
    for i in range(n):
        for j in range(i+1):
            value = matrix[i][j]-math.fsum(
                result[i][k]*result[j][k] for k in range(j))
            if i == j:
                assert value > 0, (i, value)
                result[i][j] = math.sqrt(value)
            else:
                result[i][j] = value/result[j][j]
    return result


def solve_chol(lower, vector):
    n = len(vector)
    y = [0.]*n
    x = [0.]*n
    for i in range(n):
        y[i] = (vector[i]-math.fsum(lower[i][k]*y[k]
                    for k in range(i)))/lower[i][i]
    for i in reversed(range(n)):
        x[i] = (y[i]-math.fsum(lower[k][i]*x[k]
                    for k in range(i+1,n)))/lower[i][i]
    return x


def condition(matrix, selected, remaining):
    sub = [[matrix[i][j] for j in selected] for i in selected]
    lower = cholesky(sub)
    # Density of the selected centered Gaussian at zero.
    density = (2*math.pi)**(-len(selected)/2)/math.prod(
                lower[i][i] for i in range(len(selected)))
    regression = [solve_chol(lower, [matrix[i][j] for j in selected])
                  for i in remaining]
    cond = [[matrix[i][j]-math.fsum(matrix[i][k]*regression[b][c]
                for c,k in enumerate(selected))
                for b,j in enumerate(remaining)] for i in remaining]
    return cond, density


def conditional_mean(matrix, selected, remaining, target):
    lower = cholesky([[matrix[i][j] for j in selected] for i in selected])
    solution = solve_chol(lower,target)
    means = [math.fsum(matrix[i][j]*solution[k]
                for k,j in enumerate(selected)) for i in remaining]
    multiplier = math.exp(-.5*math.fsum(a*b for a,b in zip(target,solution)))
    return means,multiplier


def mode_vectors(n, r, jn):
    value = jn(n, r)
    prime = (jn(n-1, r)-jn(n+1, r))/2
    second = (jn(n-2, r)-2*value+jn(n+2, r))/4
    scale = 1. if n == 0 else math.sqrt(2)
    # Coordinates are h, h_r, h_tau, (h_rr-h_tautau)/2, h_rtau.
    cosine = [scale*value, scale*prime, 0., scale*(second+value/2), 0.]
    sine = [0., 0., scale*n*value/r, 0.,
            scale*n*(prime/r-value/r**2)]
    return cosine, sine


def covariance_subtraction(r, jn):
    # Independent stationary spectral-angle moments, with n=0,1 removed.
    stationary = zeros(5)
    for i, value in enumerate((1., .5, .5, .125, .125)):
        stationary[i][i] = value
    c0,_ = mode_vectors(0,r,jn)
    c1,s1 = mode_vectors(1,r,jn)
    for vec in (c0,c1,s1):
        outer_add(stationary,vec,-1.)
    c2,s2 = mode_vectors(2,r,jn)
    # Full coordinates A, B, h, h_r, h_tau, X, Z2.
    full = zeros(7)
    full[0][0] = full[1][1] = 1.
    for i in range(5):
        full[0][i+2] = full[i+2][0] = c2[i]
        full[1][i+2] = full[i+2][1] = s2[i]
        for j in range(5):
            full[i+2][j+2] = stationary[i][j]
    return full


def covariance_modes(r, jn):
    # Direct retained-mode sum, without invoking the addition identity.
    full = zeros(7)
    cutoff = math.ceil(r)+80+math.ceil(10*r**(1/3))
    for n in range(2,cutoff+1):
        cosine,sine = mode_vectors(n,r,jn)
        a,b = (1.,0.) if n == 2 else (0.,0.)
        outer_add(full,[a,b]+cosine)
        outer_add(full,[b,a]+sine)
    return full


def gauss_polynomial_integral(cov):
    # Three-point standard-normal quadrature integrates degree <=5
    # in each variable exactly. This checks the fourth-moment identity.
    lower = cholesky(cov)
    nodes = ((-math.sqrt(3),1/6),(0.,2/3),(math.sqrt(3),1/6))
    terms = []
    for row in itertools.product(nodes,repeat=4):
        z = [item[0] for item in row]
        weight = math.prod(item[1] for item in row)
        a,b,x,y = [math.fsum(lower[i][j]*z[j] for j in range(i+1))
                   for i in range(4)]
        terms.append(weight*(a*a+b*b)*(x*x+y*y)/2)
    return math.fsum(terms)


def simpson(fun,a,b,n=2048):
    step = (b-a)/n
    return step/3*math.fsum((fun(a),fun(b),
        4*math.fsum(fun(a+i*step) for i in range(1,n,2)),
        2*math.fsum(fun(a+i*step) for i in range(2,n,2))))


def intensities(r, full, jn):
    w = 1-jn(0,r)
    ci,p2 = condition(full,[2,3,4],[0,1,5,6])
    cholesky(ci)
    e2 = ((ci[0][0]+ci[1][1])*(ci[2][2]+ci[3][3])/2
          +sum(ci[i][j]**2 for i in (0,1) for j in (2,3)))
    independent_e2 = gauss_polynomial_integral(ci)
    close(e2,independent_e2)
    cb,p1 = condition(full,[2,4],[0,1,3,5])
    # Remaining coordinates A,B,h_r,X. V=h_ss=-X-h_r/r.
    var_v = cb[3][3]+2*cb[2][3]/r+cb[2][2]/r**2
    cov_av = -cb[0][3]-cb[0][2]/r
    cov_bv = -cb[1][3]-cb[1][2]/r
    q = (cov_av**2+cov_bv**2)/var_v
    trace = cb[0][0]+cb[1][1]
    e1 = math.sqrt(2*var_v/math.pi)*(trace+q)/2
    # Regress A,B on V and directly integrate the folded-normal moment.
    quadrature_e1 = simpson(lambda z:
        (trace-q+q*z*z)*math.sqrt(var_v)*z*
        math.exp(-z*z/2)/math.sqrt(2*math.pi),0.,12.)
    close(e1,quadrature_e1,1e-11)
    # The curvature-free formula is deliberately different at finite r.
    var_flat = cb[3][3]
    q_flat = (cb[0][3]**2+cb[1][3]**2)/var_flat
    e1_flat = math.sqrt(2*var_flat/math.pi)*(trace+q_flat)/2
    return w*p2*e2,w*p1*e1,w*p1*e1_flat,abs(e2-independent_e2),abs(e1-quadrature_e1)


def independent_spectral_moments():
    count = 2048
    functions = (lambda a:1., lambda a:math.cos(a)**2,
        lambda a:math.sin(a)**2,lambda a:math.cos(2*a)**2/4,
        lambda a:math.sin(2*a)**2/4)
    values = [math.fsum(fun(2*math.pi*i/count) for i in range(count))/count
              for fun in functions]
    for got,want in zip(values,(1.,.5,.5,.125,.125)):
        close(got,want)
    print('stationary free-jet spectral variances:',
          ' '.join(f'{v:.12f}' for v in values))


def split_normal_integral(fun,breaks):
    points=sorted(set([-12.,12.]+[x for x in breaks if -12<x<12]))
    return math.fsum(simpson(fun,a,b,4096) for a,b in zip(points,points[1:]))


def nonzero_intensities(r,v,full,jn):
    """One-dimensional quadrature after analytic integration of Z2.

    The absolute determinant kink is integrated exactly in Z2 using
    truncated normal moments. No Gaussian tensor mesh or random samples.
    """
    w=1-jn(0,r)
    ci,p20=condition(full,[2,3,4],[0,1,5,6])
    m,mult=conditional_mean(full,[2,3,4],[0,1,5,6],
                            [v*w,v*jn(1,r),0.])
    ma,mb,mx,my=m
    close(mb,0.);close(my,0.)
    for i,j in ((0,1),(0,3),(1,2),(2,3)):
        close(ci[i][j],0.)
    sx,sy=math.sqrt(ci[2][2]),math.sqrt(ci[3][3])
    kx,ky=ci[0][2]/ci[2][2],ci[1][3]/ci[3][3]
    residual_trace=ci[0][0]+ci[1][1]-kx*kx*sx*sx-ky*ky*sy*sy
    # D2w has trace J0 and radial traceless coordinate J0/2-J1/r.
    shift=v*(jn(0,r)/2-jn(1,r)/r)
    def integrand(z):
        x=mx+sx*z
        c=v*v/4-(x-shift)**2
        f0=sy*sy-c
        f2=3*sy**4-c*sy*sy
        if c>0:
            a=math.sqrt(c)/sy
            phia=math.exp(-a*a/2)/math.sqrt(2*math.pi)
            moment0=math.erf(a/math.sqrt(2))
            moment2=sy*sy*(moment0-2*a*phia)
            moment4=sy**4*(3*moment0-2*(a**3+3*a)*phia)
            f0+=2*(c*moment0-moment2)
            f2+=2*(c*moment2-moment4)
        q0=(residual_trace+(ma+kx*sx*z)**2)/2
        return (q0*f0+ky*ky*f2/2)*math.exp(-z*z/2)/math.sqrt(2*math.pi)
    cuts=[(shift-abs(v)/2-mx)/sx,(shift+abs(v)/2-mx)/sx]
    e2=split_normal_integral(integrand,cuts)
    k2=w*p20*mult*e2

    cb,p10=condition(full,[2,4],[0,1,3,5])
    m,mult=conditional_mean(full,[2,4],[0,1,3,5],[v*w,0.])
    ma,mb,mr,mx=m
    mv=-v*w/2-mx-mr/r
    var=cb[3][3]+2*cb[2][3]/r+cb[2][2]/r**2
    ca=-cb[0][3]-cb[0][2]/r
    cc=-cb[1][3]-cb[1][2]/r
    sigma=math.sqrt(var)
    residual_trace=cb[0][0]+cb[1][1]-(ca*ca+cc*cc)/var
    e1=split_normal_integral(lambda z:
        (residual_trace+(ma+ca/sigma*z)**2+(mb+cc/sigma*z)**2)/2*
        abs(mv+sigma*z)*math.exp(-z*z/2)/math.sqrt(2*math.pi),[-mv/sigma])
    return k2,w*p10*mult*e1


def alpha(v):
    return math.exp(-v*v/2)/math.sqrt(2*math.pi)*(v*v-1+2*math.exp(-v*v))/(4*math.pi)


def beta(v):
    return math.exp(-v*v/2)/math.sqrt(2*math.pi)*(
        math.exp(-v*v)/(2*math.pi)+v*math.erf(v)/(2*math.sqrt(math.pi)))


def beta_prime(v):
    return -v*beta(v)+math.exp(-v*v/2)/math.sqrt(2*math.pi)*math.erf(v)/(2*math.sqrt(math.pi))


def main():
    jn = guard()
    started = time.monotonic()
    independent_spectral_moments()
    alpha0 = 1/(4*math.pi*math.sqrt(2*math.pi))
    beta0 = 2*alpha0
    max_cov_error=max_gh_error=max_fold_error=0.
    print('r, k2(r,0), k1(r,0), k2/alpha(0), k1/beta(0):')
    for r in (4.,8.,16.,64.,256.,1024.):
        covariance = covariance_subtraction(r,jn)
        independent = covariance_modes(r,jn)
        cholesky(covariance)
        err = max(abs(covariance[i][j]-independent[i][j])
                  for i in range(7) for j in range(7))
        assert err < 2e-12, (r,err)
        max_cov_error=max(max_cov_error,err)
        k2,k1,flat,gh,fold = intensities(r,covariance,jn)
        alternative = intensities(r,independent,jn)
        close(k2,alternative[0]);close(k1,alternative[1])
        assert k2>0 and k1>0
        assert abs(k1-flat)>1e-10, 'curvature audit must detect a change'
        # Independently differentiate the circular Fourier mode twice.
        for n in (0,1,2):
            cosine,_=mode_vectors(n,r,jn)
            value,radial,_,traceless,_=cosine
            hss=-value/2-traceless-radial/r
            close(hss,-n*n*value/r**2)
        max_gh_error=max(max_gh_error,gh)
        max_fold_error=max(max_fold_error,fold)
        print(f'{r:g} {k2:.12g} {k1:.12g} {k2/alpha0:.9f} {k1/beta0:.9f}')
    print(f'max low-mode-subtraction / retained-mode covariance error={max_cov_error:.3e}')
    print(f'max Wick / tensor Gauss quadrature error={max_gh_error:.3e}')
    print(f'max folded-normal formula / quadrature error={max_fold_error:.3e}')
    print('six circle-curvature corrections detected; both covariance constructions agree')

    # Test the sharper local expansions at signed levels. In particular,
    # the interior trace is -v, not -v*w; this changes the leading J0 term.
    max_even=max_zero=0.
    max_scaled2=max_scaled1=0.
    for r in (8.,32.,128.,512.):
        full=covariance_subtraction(r,jn)
        for v in (0.,.2,.7,1.):
            k2,k1=nonzero_intensities(r,v,full,jn)
            negative=nonzero_intensities(r,-v,full,jn)
            max_even=max(max_even,abs(k2-negative[0]),abs(k1-negative[1]))
            if v==0:
                direct=intensities(r,full,jn)
                max_zero=max(max_zero,abs(k2-direct[0]),abs(k1-direct[1]))
                close(k2,direct[0]);close(k1,direct[1])
            b2=(v*v-1)*alpha(v)
            b1=-beta(v)-v*beta_prime(v)
            max_scaled2=max(max_scaled2,r*abs(k2-alpha(v)-b2*jn(0,r)))
            max_scaled1=max(max_scaled1,r*abs(k1-beta(v)-b1*jn(0,r)))
        # Independent Helmholtz trace cancellation with Bessel ODE.
        w=1-jn(0,r);wp=jn(1,r)
        wpp=(jn(0,r)-jn(2,r))/2
        close(w+wpp+wp/r,1.)
    assert max_even<2e-11
    assert max_scaled2<.1 and max_scaled1<.1  # Audit range only, not a theorem constant.
    print(f'32 signed-level quadratures: max evenness error={max_even:.3e}; zero-level cross-check={max_zero:.3e}')
    print(f'max tested r*|k2-alpha-b2*J0|={max_scaled2:.6g}; r*|k1-beta-b1*J0|={max_scaled1:.6g}')
    print('four independent Bessel-ODE trace cancellations passed')
    for r,s in ((4.,8.),(16.,32.),(64.,128.)):
        integral=simpson(lambda x:x*jn(0,x),r,s,4096)
        endpoint=s*jn(1,s)-r*jn(1,r)
        close(integral,endpoint,2e-8)
    print('three oscillatory area integrals agree with [r*J1] endpoints')

    # Check the asymptotic constants independently using an independent
    # A,B pair and the stationary free-jet covariance, with curvature zero.
    independent = zeros(7)
    for i,v in enumerate((1.,1.,1.,.5,.5,.125,.125)):
        independent[i][i]=v
    ci,p2 = condition(independent,[2,3,4],[0,1,5,6])
    stationary2 = p2*gauss_polynomial_integral(ci)
    stationary1 = (1/(2*math.pi*math.sqrt(.5)))*math.sqrt(2*.125/math.pi)
    close(stationary2,alpha0)
    close(stationary1,beta0)
    print(f'limiting densities independently recovered: {stationary2:.12f} {stationary1:.12f}')

    # Deliberately omit U to expose the incorrect Gaussian replacement.
    cov = covariance_subtraction(4.,jn)
    ci,p2 = condition(cov,[2,3,4],[0,1,5,6])
    weighted = intensities(4.,cov,jn)[0]
    unweighted = (1-jn(0,4.))*p2*(ci[2][2]+ci[3][3])
    assert abs(weighted-unweighted)>1e-5
    print(f'r=4: weighted k2={weighted:.12g}; incorrectly unweighted={unweighted:.12g}')

    # The flow argument requires both circle terms. This deterministic
    # example has no interior critical point on 1<=r<=2. Its first
    # alternating-arm event changes at a boundary tangency at level zero.
    # g(r,theta)=r-1+cos(2theta) has grad_r=1 everywhere.
    # Its minimum along the radial ray theta=pi/2 is r-2.
    # The outer-circle tangency occurs at r=2,theta=pi/2, g=0.
    r,angle=2.,math.pi/2
    g=r-1+math.cos(2*angle)
    gs=-2*math.sin(2*angle)/r
    gss=-4*math.cos(2*angle)/r**2
    close(g,0.);close(gs,0.);close(gss,1.)
    # For t=.1, rays at angles 0,pi/2,pi,3pi/2 give four arms.
    # For t=-.1, g>=0 on the entire outer circle, so no negative arm.
    assert min(rr-1+1 for rr in (1.,2.))>.1
    assert max(rr-1-1 for rr in (1.,2.))<.1
    print('boundary-only tangency audit: value=0, tangent derivative=0, second derivative=1, radial derivative=1')

    # Direct determinant of the quotient Hessian vs the scaled formula.
    # Construct h=wY from unrelated numerical jets; enforce grad Y=0.
    for v in (-1.,0.,.7):
        w=.8;dw=(.12,-.05);hw=((.03,.02),(.02,-.07))
        hy=((.4,.13),(.13,-.2))
        hh=[[w*hy[i][j]+v*hw[i][j] for j in range(2)] for i in range(2)]
        determinant=lambda m:m[0][0]*m[1][1]-m[0][1]*m[1][0]
        difference=[[hh[i][j]-v*hw[i][j] for j in range(2)] for i in range(2)]
        close(determinant(hy),determinant(difference)/w**2)
    print('three signed quotient-Hessian determinant factors passed')
    elapsed=time.monotonic()-started
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib=rss/(1024**2) if sys.platform=='darwin' else rss/1024
    assert rss_mib<1024 and elapsed<60
    print(f'PASS; elapsed={elapsed:.3f}s; peak RSS={rss_mib:.2f} MiB')


if __name__=='__main__':
    main()
