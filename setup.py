from setuptools import setup, find_packages

setup(
    name="asyncua",
    version="0.5.1",
    description="Pure Python OPC-UA client and server library",
    author="Olivier Roulet-Dubonnet",
    author_email="olivier.roulet@gmail.com",
    url='http://freeopcua.github.io/',
    packages=find_packages(),
    provides=["asyncua"],
    license="GNU Lesser General Public License v3 or later",
    install_requires=["aiofiles", "python-dateutil", "pytz", "lxml", 'cryptography'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        'console_scripts': [
            'uaread = asyncua.tools:uaread',
            'uals = asyncua.tools:uals',
            'uabrowse = asyncua.tools:uals',
            'uawrite = asyncua.tools:uawrite',
            'uasubscribe = asyncua.tools:uasubscribe',
            'uahistoryread = asyncua.tools:uahistoryread',
            'uaclient = asyncua.tools:uaclient',
            'uaserver = asyncua.tools:uaserver',
            'uadiscover = asyncua.tools:uadiscover',
            'uacall = asyncua.tools:uacall',
            'uageneratestructs = asyncua.tools:uageneratestructs',
        ]
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
