load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_library(
    name = "app_lib",
    srcs = [
        "__init__.py",
        "config.py",
        "models.py",
        "monitoring.py",
        "schemas.py",
    ],
    deps = [
        "//deps:fastapi",
        "//deps:transformers",
        "//deps:torch",
        "//deps:prometheus_client",
    ],
)

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        ":app_lib",
        "//deps:uvicorn",
    ],
)

# Define deps as a library
py_library(
    name = "deps",
    srcs = glob(["deps/**/*.py"]),
    data = glob(["deps/**/*"], exclude=["deps/**/*.py"]),
    imports = ["deps"],
)