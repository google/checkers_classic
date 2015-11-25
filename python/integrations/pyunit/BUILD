# Description:
#   Integration of Python's standard pyunit module with checkers.

licenses(["notice"])  # Apache v2.0

exports_files(["LICENSE"])

py_library(
    name = "pyunit",
    testonly = 1,
    srcs = [
        "pyunit.py",
    ],
    visibility = ["//visibility:public"],
    deps = ["//testing/pybase"],
)
