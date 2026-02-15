from setuptools import setup, find_packages

setup(
    name='bugbuddy',
    version='1.0.0',
    description='An AI-powered bug detection and resolution platform for developers',
    author='mehrshud',
    author_email='mehrshud@example.com',
    url='https://github.com/mehrshud/bugbuddy',
    packages=find_packages(),
    install_requires=[
        # List dependencies here, e.g.
        # 'numpy',
        # 'pandas',
        # 'scikit-learn'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='bug detection bug resolution ai-powered',
    project_urls={
        'Documentation': 'https://bugbuddy.readthedocs.io',
        'Funding': 'https://donate.bugbuddy.com',
        'Say Thanks!': 'http://saythanks.io/to/mehrshud',
        'Source': 'https://github.com/mehrshud/bugbuddy',
        'Tracker': 'https://github.com/mehrshud/bugbuddy/issues'
    }
)
