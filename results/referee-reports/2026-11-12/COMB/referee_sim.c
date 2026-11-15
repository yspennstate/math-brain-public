/* Independent, non-lazy SRW on a one-sided random comb. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <time.h>
#include <inttypes.h>

typedef struct { uint64_t s; } RNG;
static uint64_t mix(uint64_t z) {
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    return z ^ (z >> 31);
}
static uint64_t draw(RNG *r) {
    r->s += UINT64_C(0x9e3779b97f4a7c15);
    return mix(r->s);
}
#define WIDTH 262145
#define CENTER 131072
static int heights[WIDTH];
static uint64_t envseed;
static double gam;
static int height(int x) {
    if (x < -CENTER || x > CENTER) { fprintf(stderr,"coordinate overflow\n"); exit(2); }
    int *p = heights + x + CENTER;
    if (!*p) {
        uint64_t h = mix(envseed ^ mix((uint64_t)(int64_t)x + UINT64_C(0x6a09e667f3bcc909)));
        double u = ((h >> 11) + 0.5) * 0x1.0p-53;
        double v = pow(u, -1.0/gam);
        *p = v > 100000001.0 ? 100000001 : (int)floor(v);
    }
    return *p;
}
typedef struct { int x,y,h; } Walk;
static void step(Walk *w, RNG *r) {
    uint64_t u = draw(r);
    if (w->y == 0) {
        /* Rejection removes modulo bias; all teeth have height at least 1. */
        while (u == UINT64_MAX) u = draw(r);
        int a = (int)(u % 3);
        if (a == 0) { --w->x; w->h=height(w->x); }
        else if (a == 1) { ++w->x; w->h=height(w->x); }
        else ++w->y;
    } else if (w->y == w->h) --w->y;
    else w->y += (u & 1) ? 1 : -1;
}
static void profile(uint64_t s) {
    envseed = s;
    for (int i=0;i<WIDTH;i++) heights[i]=0;
}
static int inside(Walk w,int radius,int ceiling) {
    return abs(w.x)<=radius && w.y<=ceiling;
}
int main(int argc,char **argv) {
    if(argc!=4) { fprintf(stderr,"usage: referee_sim long|moments gamma output\n"); return 2; }
    gam=atof(argv[2]);
    FILE *f=fopen(argv[3],"w"); if(!f) return 2;
    time_t start=time(NULL);
    fprintf(f,"# Independent non-lazy comb simulation; gamma=%.12g; H=floor(U^(-1/gamma)); t=0 excluded.\n",gam);
    if(argv[1][0]=='l') {
        int checkpoints[]={100000,200000,500000,1000000,2000000,5000000,10000000,20000000,50000000,100000000};
        fprintf(f,"profile,time,all_collisions,backbone_collisions,collision_episodes,max_abs_x,max_y\n");
        for(int p=0;p<6;p++) {
            profile(UINT64_C(18444453)+p*UINT64_C(1000003));
            RNG a={UINT64_C(4723289)+p*1234},b={UINT64_C(874872391)+p*1777};
            Walk x={0,0,height(0)},y=x;
            uint64_t all=0,back=0,episodes=0; int prev=1,j=0,mx=0,my=0;
            for(int t=1;t<=100000000;t++) {
                step(&x,&a); step(&y,&b);
                int meet=x.x==y.x && x.y==y.y;
                all+=meet; back+=meet && x.y==0; episodes+=meet && !prev; prev=meet;
                if(abs(x.x)>mx)mx=abs(x.x);if(abs(y.x)>mx)mx=abs(y.x);
                if(x.y>my)my=x.y;if(y.y>my)my=y.y;
                if(t==checkpoints[j]) {
                    fprintf(f,"%d,%d,%"PRIu64",%"PRIu64",%"PRIu64",%d,%d\n",p,t,all,back,episodes,mx,my);fflush(f);
                    if(++j==10)break;
                    if(time(NULL)-start>235) {fprintf(f,"# TIME LIMIT\n");fclose(f);return 3;}
                }
            }
        }
    } else {
        int ns[]={4,8,16,32,64};
        fprintf(f,"# Hprime uses explicit surrogate constants cl=1,cu=2,b=4; paper does not specify numerical constants.\n");
        fprintf(f,"N,profile,replicates,mean,second,second_over_mean_squared,second_over_mean,prob_positive,mean_se,second_se,killed_fraction\n");
        for(int i=0;i<5;i++)for(int p=0;p<6;p++) {
            int N=ns[i],nrep=N==64?400:1200;
            int ceiling=(int)floor(pow(4.0*N,1.5));
            profile(UINT64_C(18444453)+p*UINT64_C(1000003));
            long double s=0,s2=0,s4=0;int pos=0,killed=0;
            for(int rep=0;rep<nrep;rep++) {
                RNG a={UINT64_C(32141231)+i*14771+p*777+rep*UINT64_C(100000007)},b={UINT64_C(789121313)+i*1987+p*397+rep*UINT64_C(100000037)};
                Walk x={0,0,height(0)},y=x;int h=0;
                for(int t=1;t<=2*N*N*N;t++) {
                    step(&x,&a);step(&y,&b);
                    if(!inside(x,4*N,ceiling)||!inside(y,4*N,ceiling)){killed++;break;}
                    if(t>=N*N*N && x.x==y.x && x.y==0 && y.y==0 && abs(x.x)<=N)h++;
                }
                s+=h;s2+=(long double)h*h;s4+=(long double)h*h*h*h;pos+=h>0;
            }
            long double mean=s/nrep,second=s2/nrep;
            fprintf(f,"%d,%d,%d,%.9Lg,%.9Lg,%.9Lg,%.9Lg,%.9g,%.9Lg,%.9Lg,%.9g\n",N,p,nrep,mean,second,mean?second/(mean*mean):NAN,mean?second/mean:NAN,(double)pos/nrep,sqrtl(fmaxl(0,second-mean*mean)/nrep),sqrtl(fmaxl(0,s4/nrep-second*second)/nrep),(double)killed/nrep);fflush(f);
            if(time(NULL)-start>235){fprintf(f,"# TIME LIMIT\n");fclose(f);return 3;}
        }
    }
    fprintf(f,"# elapsed_seconds=%ld\n",(long)(time(NULL)-start));
    fclose(f);return 0;
}
