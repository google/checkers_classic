# Description:
#   Core python module of the checkers unit test framework.

licenses(["notice"])  # Apache v2.0

exports_files(["LICENSE"])

py_library(
    name = "checkers",
    testonly = 1,
    srcs = [
        "checkers.py",
        "component_registry.py",
        "context.py",
        "logging.py",
        "test_case.py",
        "test_data.py",
        "test_result.py",
        "test_run.py",
        "test_suite.py",
        "utilities.py",
        "validation.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//net/proto2/python/public",
        "//testing/pybase",
        "//third_party/py/checkers:checkers_proto",
        "//third_party/py/gflags",
    ],
)
