#include <gmp.h>
#include <stddef.h>
// Little-endian byte strings; caller provides a zero-filled output buffer.
size_t multiply_bytes(const unsigned char *a,size_t na,const unsigned char*b,size_t nb,unsigned char*out){
 mpz_t x,y,z;mpz_inits(x,y,z,NULL);
 mpz_import(x,na,-1,1,0,0,a);mpz_import(y,nb,-1,1,0,0,b);mpz_mul(z,x,y);
 size_t count=0;mpz_export(out,&count,-1,1,0,0,z);mpz_clears(x,y,z,NULL);return count;
}
