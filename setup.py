import setuptools

setuptools.setup(
    name="st_stylish",
    version="0.0.1",
    author="Kellen Busby Software LLC",
    author_email="kellenbusby@gmail.com",
    description="A collection of custom components and helper functions for Streamlit that are focused on providing advanced styling functionality.",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
