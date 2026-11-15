/* Independent synchronous urn on the dual cycle: choices in a round use old N.
   This is the cycle version of the discrete edge-to-endpoint update rule. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <math.h>
static uint64_t state;
static double unif(void){state=state*2862933555777941757ULL+3037000493ULL;return ((state>>11)+.5)*0x1p-53;}
int main(int argc,char **argv){
    (void)argc;
    int L=atoi(argv[1]), steps=atoi(argv[2]), R=atoi(argv[3]);state=strtoull(argv[4],0,10);
    int *n=calloc(L,sizeof(int)),*add=calloc(L,sizeof(int));
    printf("L,steps,rep,M,Z,p\n");
    for(int r=0;r<R;r++){
        for(int e=0;e<L;e++)n[e]=1;
        double M=0;
        for(int k=0;k<steps;k++){
            for(int e=0;e<L;e++)add[e]=0;
            for(int v=0;v<L;v++){
                int a=(v+L-1)%L;
                if(unif()*(n[a]+n[v])<n[a])add[a]++;else add[v]++;
            }
            for(int e=0;e<L;e++)for(int j=0;j<add[e];j++){
                M+=((e&1)?-1.:1.)/n[e];n[e]++;
            }
        }
        double p=0,logcharge=0;
        for(int e=0;e<L;e++){if(!(e&1))p+=(double)n[e]/(L*steps);logcharge+=((e&1)?-1.:1.)*log(n[e]);}
        printf("%d,%d,%d,%.12g,%.12g,%.12g\n",L,steps,r,M,logcharge/sqrt(L),p);
    }
    free(n);free(add);return 0;
}
