#!/usr/bin/env python

def perrin ( n ):

#*****************************************************************************80
#
## PERRIN returns the first N values of the Perrin sequence.
#
#  Discussion:
#
#    The Perrin sequence has the initial values:
#
#      P(0) = 3
#      P(1) = 0
#      P(2) = 2
#
#    and subsequent entries are generated by the recurrence
#
#      P(I+1) = P(I-1) + P(I-2)
#
#    Note that if N is a prime, then N must evenly divide P(N).
#
#  Example:
#
#    0   3
#    1   0
#    2   2
#    3   3
#    4   2
#    5   5
#    6   5
#    7   7
#    8  10
#    9  12
#   10  17
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ian Stewart,
#    "A Neglected Number",
#    Scientific American, Volume 274, pages 102-102, June 1996.
#
#    Ian Stewart,
#    Math Hysteria,
#    Oxford, 2004.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1999.
#
#  Parameters:
#
#    Input, integer N, the number of terms.
#
#    Output, integer P(N), the first N terms of the sequence.
#
  import numpy as np

  p = np.zeros ( n )

  if ( 0 < n ):
    p[0] = 3

    if ( 1 < n ):
      p[1] = 0

      if ( 2 < n ):
        p[2] = 2

        for i in range ( 3, n ):
          p[i] = p[i-2] + p[i-3]

  return p

def perrin_test ( ):

#*****************************************************************************80
#
## PERRIN_TEST tests PERRIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print

  n = 20

  print ''
  print 'PERRIN_TEST'
  print '  PERRIN computes the Perrin numbers.'

  p = perrin ( n )

  i4vec_print ( n, p, '  The Perrin sequence:' )
#
#  Terminate.
#
  print ''
  print 'PERRIN_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perrin_test ( )
  timestamp ( )
