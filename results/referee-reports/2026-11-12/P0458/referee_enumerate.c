/* All orderings of the independent edge scores, n=4 and n=5. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int n,e,ea[10],eb[10],order[10],used[10];
static uint64_t total,hd[5][5],id[5][5],sd[5],sd2[5];

static void visit(void) {
    int rank[5][5]={{0}},nr[5]={0};
    for(int p=0;p<e;p++) {
        int a=ea[order[p]],b=eb[order[p]];
        rank[a][b]=++nr[a]; rank[b][a]=++nr[b];
    }
    for(int k=1;k<n-1;k++) {
        int d=0,in=0;
        for(int v=1;v<n;v++) {
            in += (rank[v][0]<=k);
            d += (rank[v][0]<=k && rank[0][v]<=k);
        }
        hd[k][k-d]++; id[k][in-d]++;
        sd[k]+=d; sd2[k]+=d*d;
    }
    total++;
}

static void permute(int p) {
    if(p==e) {visit();return;}
    for(int j=0;j<e;j++) if(!used[j]) {
        used[j]=1;order[p]=j;permute(p+1);used[j]=0;
    }
}

int main(int argc,char **argv) {
    n=argc>1?atoi(argv[1]):5;
    if(n<3 || n>5) return 2;
    for(int a=0;a<n;a++) for(int b=a+1;b<n;b++) {
        ea[e]=a;eb[e]=b;e++;
    }
    permute(0);
    printf("n=%d total=%llu\n",n,(unsigned long long)total);
    for(int k=1;k<n-1;k++) {
        printf("k=%d sumD=%llu sumD2=%llu Hcounts=",k,
               (unsigned long long)sd[k],(unsigned long long)sd2[k]);
        for(int h=0;h<n;h++) printf("%s%llu",h?",":"",(unsigned long long)hd[k][h]);
        int ok=1;
        for(int h=0;h<n;h++) if(hd[k][h]!=id[n-1-k][h]) ok=0;
        printf(" complementary_ID_law=%s\n",ok?"PASS":"FAIL");
        if(!ok) return 1;
    }
    return 0;
}
