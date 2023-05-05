# Jupyter Server Proxy with Voila

pip-installable package to add a Voila server button to JupyterLab's Launcher menu using [jupyter-server-proxy.](https://github.com/jupyterhub/jupyter-server-proxy). Modified from the example [here](https://github.com/vnijs/jupyter-gitgadget-proxy).

## Setup

First make sure Voila is properly installed in your JupyterLab environment and available on the system path. Next, install `jupyter-server-proxy` using either `conda` or `pip` (see link above), then

    pip install git+https://github.com/NIVANorge/jupyter_voila_proxy.git

A button to launch Voila should be added to the JupyterLab Launcher menu.
