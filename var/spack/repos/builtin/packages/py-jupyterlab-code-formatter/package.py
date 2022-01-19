# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

class PyJupyterlabCodeFormatter(PythonPackage):
    """A universal code formatter for JupyterLab."""

    homepage = "https://jupyterlab-code-formatter.readthedocs.io/en/latest/index.html"
    pypi     = "jupyterlab_code_formatter/jupyterlab_code_formatter-1.4.10.tar.gz"

    version('1.4.10', sha256='1645fd80b99d590d60fe0f3c078c9101ad62dfdbfac5e78b4c2d334896ab526f')

    depends_on('py-jupyterlab', type=('build', 'run'))
    depends_on('py-jupyter-packaging', type='build')
    #depends_on('py-black',type='run')
    #depends_on('py-isort',type='run')

    def setup_run_environment(self,env):
        env.prepend_path("JUPYTER_PATH",self.prefix.share.jupyter)
        env.prepend_path("JUPYTER_CONFIG_PATH",self.prefix.etc.jupyter)

