#include <stdio.h>
#include <string.h>

char *fragments[] = {
  "object Prototype {",
  "def main(args: Array[String]) {",
  "println(\"PROTOTYPE\");",
  "}",
  "}"
};

int main(int argc, char *argv[]) {
  int i;
  FILE *out_stream;
  out_stream = fopen("prototype.scala", "w");
  for(i=0; i < 5; i++) {
    fprintf(out_stream, "%s\n", fragments[i]);
  }
  fclose(out_stream);
  printf("Invoke \"scalac prototype.scala\" to compile and \"scala Prototype\" to execute.\n");
}
