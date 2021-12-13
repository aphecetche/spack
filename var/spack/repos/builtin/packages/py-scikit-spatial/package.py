# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class PyScikitSpatial(PythonPackage):
    """Spatial objects and computations based on NumPy arrays."""

    homepage = "https://scikit-spatial.readthedocs.io"
    pypi     = "scikit-spatial/scikit-spatial-6.2.0.tar.gz"


    version('6.2.0', sha256='3ebf19e4f18d216a96e8f5455037f45d0efc1065659db91c13eecf99ee7417f4')

    depends_on('py-poetry-core', type='build')

    # FIXME: Add additional dependencies if required.
    depends_on('py-numpy@1.20:2')
    depends_on('py-matplotlib@3:4')

    # depends_on('py-foo', type=('build', 'run'))

    def global_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py
        # FIXME: If not needed, delete this function
        options = []
        return options

    def install_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py install
        # FIXME: If not needed, delete this function
        options = []
        return options
