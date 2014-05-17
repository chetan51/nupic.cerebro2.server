#!/usr/bin/env python
# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2014, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

import numpy

from cerebro2.patcher import Patcher
from nupic.encoders.base import defaultDtype
from nupic.encoders.coordinate import CoordinateEncoder



def run():
  n = 999
  w = 25
  encoder = CoordinateEncoder(name='coordinate',
                              n=n,
                              w=w)
  Patcher().patchCoordinateEncoder(encoder, encoder.name)

  encode(encoder, numpy.array([10, 20]), 5)
  encode(encoder, numpy.array([10, 21]), 5)
  encode(encoder, numpy.array([10, 22]), 5)
  encode(encoder, numpy.array([10, 23]), 5)
  encode(encoder, numpy.array([10, 23]), 7)
  encode(encoder, numpy.array([10, 23]), 9)
  encode(encoder, numpy.array([10, 26]), 9)
  encode(encoder, numpy.array([10, 35]), 10)
  encode(encoder, numpy.array([10, 40]), 15)
  encode(encoder, numpy.array([10, 50]), 30)
  encode(encoder, numpy.array([10, 70]), 30)
  encode(encoder, numpy.array([30, 70]), 30)
  encode(encoder, numpy.array([50, 70]), 30)
  encode(encoder, numpy.array([70, 70]), 30)
  encode(encoder, numpy.array([90, 70]), 30)



def encode(encoder, coordinate, radius):
  output = numpy.zeros(encoder.getWidth(), dtype=defaultDtype)
  encoder.encodeIntoArray((coordinate, radius), output)
  print "===== " + str(coordinate) + " / " + str(radius) + " ====="
  print output.nonzero()[0]
  print
  return output



if __name__ == "__main__":
  run()
