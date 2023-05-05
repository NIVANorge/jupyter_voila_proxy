from os import path

import setuptools

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="jupyter-voila-proxy",
    version="0.1.0",
    url="https://github.com/NIVANorge/jupyter_voila_proxy",
    author="James Sample",
    description="james.sample@niva.no",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    install_requires=["jupyter-server-proxy>=1.5.0"],
    entry_points={
        "jupyter_serverproxy_servers": [
            "voila = jupyter_voila_proxy:setup_voila",
        ]
    },
)
