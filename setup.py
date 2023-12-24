from setuptools import setup, find_packages

setup(
    name='duvals_triangle_plotter',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'plotly',
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'duvals_triangle_plotter=duvals_triangle_plotter.__main__:main',
        ],
    },
    include_package_data=True,
    author='Subramanian Narayanan',
    author_email='your.email@example.com',
    description="Duval's Triangle Plotter - Python library for generating Duval's Triangle plots",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/duvals_triangle_plotter',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)