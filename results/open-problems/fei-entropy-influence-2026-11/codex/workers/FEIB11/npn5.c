/* Generate one representative of every 5-variable NPN orbit, independently.
   Complement-normalized truth tables are in [0,2^31); visited uses 256 MiB.
   Permutation images use four byte lookup tables; translations follow a Gray code. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <inttypes.h>
static uint32_t lut[120][4][256];
static int perms[120][5], np;
static void permute(int depth,int used,int *p){
 if(depth==5){for(int j=0;j<5;j++)perms[np][j]=p[j];np++;return;}
 for(int j=0;j<5;j++)if(!(used&(1<<j))){p[depth]=j;permute(depth+1,used|(1<<j),p);}
}
static uint32_t translate(uint32_t t,int i){
 const uint32_t masks[5]={0x55555555,0x33333333,0x0f0f0f0f,0x00ff00ff,0x0000ffff};
 int d=1<<i; return ((t&masks[i])<<d)|((t&~masks[i])>>d);
}
int main(void){
 int p[5];permute(0,0,p);
 for(int k=0;k<120;k++)for(int b=0;b<4;b++)for(int v=0;v<256;v++){
  uint32_t t=0;for(int j=0;j<8;j++)if(v&(1<<j)){
   int x=8*b+j,y=0;for(int i=0;i<5;i++)if(x&(1<<i))y|=1<<perms[k][i];t|=1u<<y;
  }lut[k][b][v]=t;
 }
 uint64_t *seen=calloc(1ull<<25,sizeof(uint64_t));if(!seen)return 2;
 FILE *out=fopen("npn5.txt","w"); if(!out)return 3;
 uint64_t count=0,covered=0;clock_t start=clock();
 for(uint64_t w=0;w<(1ull<<25);w++)while(seen[w]!=UINT64_MAX){
  uint32_t t=(uint32_t)(64*w+__builtin_ctzll(~seen[w]));
  fprintf(out,"%08x\n",t);count++;
  for(int k=0;k<120;k++){
   uint32_t u=lut[k][0][t&255]|lut[k][1][(t>>8)&255]|lut[k][2][(t>>16)&255]|lut[k][3][t>>24];
   for(int a=0;a<32;a++){
    if(a)u=translate(u,__builtin_ctz(a));
    uint32_t v=(u&0x80000000u)?~u:u; seen[v>>6]|=1ull<<(v&63);
   }
  }
  if(count%100000==0){fflush(out);fprintf(stderr,"classes=%"PRIu64" last=%08x cpu_seconds=%.2f\n",count,t,(double)(clock()-start)/CLOCKS_PER_SEC);}
 }
 for(uint64_t w=0;w<(1ull<<25);w++)covered+=__builtin_popcountll(seen[w]);
 fclose(out);free(seen);
 printf("classes=%"PRIu64" complement_normalized_tables_covered=%"PRIu64" allocated_bytes=%llu cpu_seconds=%.3f\n",count,covered,256ull*1024*1024,(double)(clock()-start)/CLOCKS_PER_SEC);
 return count==616126 && covered==(1ull<<31)?0:4;
}
