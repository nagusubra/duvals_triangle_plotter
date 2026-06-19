from setuptools import setup, find_packages

setup(
    name='duvals_triangle_plotter',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'plotly',
    ],
    entry_points={
        'console_scripts': [
            'duvals_triangle_plotter=duvals_triangle_plotter.__main__:main',
        ],
    },
    include_package_data=True,
    author='Subramanian Narayanan',
    author_email='snarayan@nagusubra.com',
    description="Duval's Triangle Plotter — Python library for generating Duval's Triangle plots for DGA",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://nagusubra.github.io/duvals-triangle-plotter/',
    project_urls={
        'Source Code': 'https://github.com/nagusubra/duvals-triangle-plotter',
        'Bug Tracker': 'https://github.com/nagusubra/duvals-triangle-plotter/issues',
    },
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Scientific/Engineering :: Visualization',
        'Intended Audience :: Science/Research',
    ],
)