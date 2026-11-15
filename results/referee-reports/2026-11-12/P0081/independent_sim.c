/* Independent Gillespie simulator. Uniformization of rate-one vertex clocks.
   PCG32, not the authors' RNG. Exact waiting-time integration of <M>.
   No time-overshoot event is applied. Single threaded, O(vertices) memory.
   cycle L T R seed
   line V T R seed buffer: path with V vertices, discard buffer vertices at ends.
   graph T R seed: K4, with a nonzero kernel charge on a square.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>
static uint64_t rngstate;
static uint32_t rnd(void) {
    uint64_t old=rngstate;
    rngstate=old*6364136223846793005ULL+1442695040888963407ULL;
    uint32_t x=(uint32_t)(((old>>18)^old)>>27), r=(uint32_t)(old>>59);
    return (x>>r)|(x<<((-r)&31));
}
static double unif(void) { return ((double)rnd()+0.5)/4294967296.0; }
static int sign(int e) { return (e&1)?-1:1; }
int main(int argc,char **argv) {
    (void)argc;
    int line=!strcmp(argv[1],"line"), graph=!strcmp(argv[1],"graph");
    int V=graph?4:atoi(argv[2]), E=graph?6:(line?V-1:V);
    double T=atof(argv[graph?2:3]); int R=atoi(argv[graph?3:4]);
    rngstate=strtoull(argv[graph?4:5],0,10)+0x123456789abcdefULL;
    for(int j=0;j<10;j++) rnd();
    int buffer=line?atoi(argv[6]):0;
    int *a=calloc(E,sizeof(int)), *b=calloc(E,sizeof(int));
    int *deg=calloc(V,sizeof(int)), *inc=calloc(3*V,sizeof(int));
    int *sig=calloc(E,sizeof(int));
    double *n=calloc(E,sizeof(double)), *rate=calloc(V,sizeof(double));
    double *integ=calloc(V,sizeof(double)), *last=calloc(V,sizeof(double));
    if(graph) {
        int aa[]={0,0,0,1,1,2}, bb[]={1,2,3,2,3,3}, ss[]={1,-1,0,0,-1,1};
        for(int e=0;e<E;e++){a[e]=aa[e];b[e]=bb[e];sig[e]=ss[e];}
    } else for(int e=0;e<E;e++){a[e]=e;b[e]=(e+1)%V;sig[e]=sign(e);}
    for(int e=0;e<E;e++){inc[3*a[e]+deg[a[e]]++]=e;inc[3*b[e]+deg[b[e]]++]=e;}
    printf("mode,V,T,rep,M,Q,logcharge,altmean,shape_rms,vertex_rms,meanmass,qrate,p,optional\n");
    for(int rep=0;rep<R;rep++) {
        for(int e=0;e<E;e++)n[e]=1;
        for(int v=0;v<V;v++) {
            double sv=deg[v], z=0;
            for(int j=0;j<deg[v];j++){int e=inc[3*v+j];z+=sig[e]*sig[e]/n[e];}
            rate[v]=line?(deg[v]==2?1.:0.):z/sv;
            integ[v]=last[v]=0;
        }
        double t=0,M=0,optional=0,next=1;
        while(t<T) {
            double dt=-log(unif())/V;
            double stop=t+dt;
            /* Snapshot output for line, including exact integral to snapshot. */
            if(line) while(next<=T && next<=stop) {
                double sum=0,rr=0,hsum=0;int nmax=1;
                for(int e=buffer;e<V-buffer;e++)if(n[e]>nmax)nmax=(int)n[e];
                double *hh=calloc(nmax+1,sizeof(double));
                for(int j=1;j<=nmax;j++)hh[j]=hh[j-1]+1./((double)j*j);
                for(int v=buffer;v<V-buffer;v++){
                    sum+=integ[v]+(next-last[v])*rate[v];rr+=rate[v];hsum+=hh[(int)n[v]-1];
                }
                printf("line,%d,%.12g,%d,0,%.12g,0,0,0,0,0,%.12g,0,%.12g\n",V,next,rep,
                       sum/(V-2*buffer),rr/(V-2*buffer),hsum/(V-2*buffer));
                free(hh);
                next*=10;
            }
            if(stop>T)break;
            t=stop;
            int v=(int)(unif()*V); double sv=0;
            for(int j=0;j<deg[v];j++)sv+=n[inc[3*v+j]];
            double z=unif()*sv;int e=inc[3*v];
            for(int j=0;j<deg[v];j++) {e=inc[3*v+j];z-=n[e];if(z<0)break;}
            int ends[2]={a[e],b[e]};
            for(int k=0;k<2;k++){int w=ends[k];integ[w]+=(t-last[w])*rate[w];last[w]=t;}
            M+=sig[e]/n[e];optional+=(double)(sig[e]*sig[e])/(n[e]*n[e]);n[e]++;
            for(int k=0;k<2;k++) {
                int w=ends[k]; double s=0,q=0;
                for(int j=0;j<deg[w];j++){int f=inc[3*w+j];s+=n[f];q+=sig[f]*sig[f]/n[f];}
                rate[w]=line?(deg[w]==2?1./(n[inc[3*w]]*n[inc[3*w+1]]):0.):q/s;
            }
        }
        if(line)continue;
        double Q=0,sl=0,am=0,mass=0,vr=0,shape=0;
        for(int v=0;v<V;v++) {
            Q+=integ[v]+(T-last[v])*rate[v];double s=0;
            for(int j=0;j<deg[v];j++)s+=n[inc[3*v+j]]/T;
            vr+=(s-2)*(s-2);
        }
        for(int e=0;e<E;e++){sl+=sig[e]*log(n[e]);am+=sig[e]*n[e]/T;mass+=n[e]/T;}
        am/=V;
        for(int e=0;e<E;e++){double d=n[e]/T-1-sign(e)*am;shape+=d*d;}
        double p=0;
        if(!graph && V==4)p=(n[0]+n[2])/(4*T);
        printf("%s,%d,%.12g,%d,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,0,%.12g,%.12g\n",
               graph?"K4":"cycle",V,T,rep,M,Q,sl,am,sqrt(shape/E),sqrt(vr/V),mass/V,p,optional);
    }
    free(a);free(b);free(deg);free(inc);free(sig);free(n);free(rate);free(integ);free(last);
    return 0;
}
