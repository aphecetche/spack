# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyopenssl(PythonPackage):
    """High-level wrapper around a subset of the OpenSSL library.

    Note: The Python Cryptographic Authority strongly suggests the use of
    pyca/cryptography where possible. If you are using pyOpenSSL for anything
    other than making a TLS connection you should move to cryptography and
    drop your pyOpenSSL dependency."""

    homepage = "https://pyopenssl.org/"
    pypi = "pyOpenSSL/pyOpenSSL-19.0.0.tar.gz"

    version('21.0.0', sha256='5e2d8c5e46d0d865ae933bef5230090bdaf5506281e9eec60fa250ee80600cb3')

    version('19.0.0', sha256='aeca66338f6de19d1aa46ed634c3b9ae519a64b458f8468aec688e7e3c20f200')

    depends_on('py-setuptools', type='build')
    depends_on('py-cryptography@2.3:', when='@:21.0.0', type=('build', 'run'))
    depends_on('py-cryptography@3.3:', when='@21.0.0:', type=('build', 'run'))
    depends_on('py-six@1.5.2:', type=('build', 'run'))
