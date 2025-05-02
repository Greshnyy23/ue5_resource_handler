from setuptools import setup, find_packages

setup(
    name="ue5_resource_handler",
    version="1.0.0",
    description="Обработка ресурсов Unreal Engine 5 (.pak, .ucas, .utoc, .ubulk) через CLI и GUI",
    author="Greshnyy23",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "tkinter",
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "ue5-handler=src.cli:main"
        ]
    }
)