/* Referee's event-exact simulation. PCG32, exact rotations and diagonal flows.
   Distinct source and RNG from the submission. One process, one thread. */
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
static uint64_t state, inc;
static uint32_t pcg(void) {
    uint64_t old=state;
    state=old*UINT64_C(6364136223846793005)+inc;
    uint32_t x=(uint32_t)(((old>>18u)^old)>>27u),rot=old>>59u;
    return (x>>rot)|(x<<((-rot)&31));
}
static double uniform(void) {
    uint64_t a=pcg()>>5,b=pcg()>>6;
    return (a*67108864.0+b+0.5)/9007199254740992.0;
}
static void seed_rng(uint64_t s) {state=0;inc=(s<<1u)|1;pcg();state+=s^UINT64_C(0xcafefeeddeadbeef);pcg();}
static void cycle(double r,double *x,double *y,double *duration,double *gain) {
    double t0=-log(uniform())/r,t1=-log(uniform())/r;
    double c=cos(t0),s=sin(t0),xx=c*(*x)-s*(*y),yy=s*(*x)+c*(*y);
    /* exp(A1*t1) = exp(1.25*t1)*diag(1,exp(-4*t1)). */
    double z=yy*exp(-4*t1),norm=hypot(xx,z);
    *gain=-.75*t0+1.25*t1+log(norm);
    *duration=t0+t1;*x=xx/norm;*y=z/norm;
}
int main(int argc,char **argv) {
    long perblock=argc>1?atol(argv[1]):50000;
    double rates[]={.1,5,20};
    printf("r,replicate,block,cycles,time,log_growth,exponent\n");
    for(int ri=0;ri<3;ri++)for(int rep=0;rep<3;rep++) {
        seed_rng(UINT64_C(91876123)+ri*17371+rep*104729);
        double x=.6,y=.8,t,g;
        for(long n=0;n<100000;n++)cycle(rates[ri],&x,&y,&t,&g);
        for(int b=0;b<100;b++) {
            double time=0,reward=0;
            for(long n=0;n<perblock;n++) {cycle(rates[ri],&x,&y,&t,&g);time+=t;reward+=g;}
            printf("%.17g,%d,%d,%ld,%.17g,%.17g,%.17g\n",rates[ri],rep,b,perblock,time,reward,reward/time);
            fflush(stdout);
        }
    }
    return 0;
}
