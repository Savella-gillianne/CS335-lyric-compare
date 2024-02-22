from setuptools import setup

setup(
    name="lyric_compare",
    version="0.1.0",
    py_modules=['lyric_compare'],
    install_requires=[
        "click",
        "pandas",
        "scikit-learn",
        "tabulate",
    ],
    entry_points={
        "console_scripts": [
            "lyric_compare = lyric_compare:cli"
        ],
    },
)
