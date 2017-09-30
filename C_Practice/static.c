#include <stdio.h>
#include <stdlib.h>


int checkStatic( int value );

void main() {
  
  int i;
  for( i = 0; i < 20; i++ ) {
    (void) printf( "Static value is now: %d\n", checkStatic(i) );
  }
}

int checkStatic( int value ) {
  
  static int number = 0;
  
  number = number + value;

  return number;
}

