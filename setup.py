import setuptools

setuptools.setup(
    name="test-scripts",
    version="0.0.1",
    author="Derek M Frank",
    author_email="derek@frank.sh",
    description="Test installing with pre-commit",
    python_requires=">= 3.7",
    scripts=[
        "scripts/myscript",
    ],
)
