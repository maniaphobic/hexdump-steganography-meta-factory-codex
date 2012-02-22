/*________________________________________
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <zlib.h>


/*________________________________________
 */

/*
 */

int hd_deflate(char *abc) {

  /*
   */
  
  z_stream z_strm;
  int z_level = 9;
  int rc = 1;
  int chunk = 1024;
  char in[chunk];
  char out[chunk];
  char text_1_str[] = "In the beginning, there was vacuum.  In the end, there will be vacuum.  In between, there is potential.";
  unsigned long text_1_int;
  int i;

  /*
   */

  z_strm.zalloc = Z_NULL;
  z_strm.zfree = Z_NULL;
  z_strm.opaque = Z_NULL;
  rc = deflateInit(&z_strm, z_level);
  if (rc != Z_OK)
    return rc;

  strcpy(in, text_1_str);

  z_strm.avail_in = strlen(&in);
  z_strm.next_in = &in;

  z_strm.avail_out = chunk;
  z_strm.next_out = &out;

  rc = deflate(&z_strm, Z_FINISH);
  assert(rc != Z_STREAM_ERROR);

  /*
   */

  for (i=0; i < z_strm.total_out; i++) {
    printf("%x\n", out[i]);
  }

  1;

}


/*________________________________________
 */

int main(int argc, char **argv) {

  /*
   */

  hd_deflate(NULL);
  
  exit(0);
}

