#include "codewheel.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 */

int decode(char *raw_str, char **encoded_str) {1;}

/*
 */

int encode(char *raw_str, char **encoded_str) {

  char *raw_cursor, *encoded_cursor, raw_buffer[3] = "\0\0\0";
  int raw_len, chunk_count, raw_rem, encoded_len, pad_index, chunk_num, last_iter;

  raw_len = strlen(raw_str);
  raw_rem = raw_len % 3;
  chunk_count = (int) raw_len/3 + (raw_rem == 0 ? 0 : 1);
  encoded_len = 4 * chunk_count;

  *encoded_str = (char *) malloc((encoded_len+1) * sizeof(char));
  (*encoded_str)[encoded_len] = '\0';

  raw_cursor = raw_str;
  encoded_cursor = *encoded_str;

  for (chunk_num=1; chunk_num <= chunk_count; chunk_num++) {

    last_iter = (chunk_num == chunk_count) ? 1 : 0;

    if (last_iter) {
      strcpy(raw_buffer, raw_cursor);
      raw_cursor = raw_buffer;
    }

    encoded_cursor[0] = alphabet[(raw_cursor[0] >> 2)];
    encoded_cursor[1] = alphabet[(((raw_cursor[0] & 0x3) << 4) | (raw_cursor[1] >> 4))];
    encoded_cursor[2] = alphabet[(((raw_cursor[1] & 0xf) << 2) | (raw_cursor[2] >> 6))];
    encoded_cursor[3] = alphabet[raw_cursor[2] & 0x3f];

    if (last_iter && raw_rem > 0) {
      for (pad_index=0; pad_index < 3-raw_rem; pad_index++) {
	encoded_cursor[3-pad_index] = '=';
      }
    }

    raw_cursor += 3;
    encoded_cursor += 4;

  } /* for */

}

int main(int argc, char *argv[]) {

  char *encoded_str;

  if (argc < 2)
    exit(0);

  encode(argv[1], &encoded_str);
  printf("%s\n", encoded_str);
  free(encoded_str);
  exit(0);
}

