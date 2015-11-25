# Description:
#   Example tests for the checkers unit test framework.

licenses(["notice"])  # Apache v2.0

exports_files(["LICENSE"])

test_suite(
    name = "smoke_tests",
    tags = [
        "-enormous",
        "-large",
    ],
    visibility = ["//visibility:public"],
)

py_test(
    name = "example1_test",
    srcs = ["example1_test.py"],
    deps = [
        "//testing/pybase",
        "//third_party/py/checkers:checkers_proto",
        "//third_party/py/checkers/python:checkers",
        "//third_party/py/checkers/python/integrations:hamcrest",
        "//third_party/py/checkers/python/integrations/pyunit",
        "//third_party/py/gflags",
    ],
)

py_test(
    name = "example2_test",
    srcs = ["example2_test.py"],
    deps = [
        "//testing/pybase",
        "//third_party/py/checkers/python:checkers",
        "//third_party/py/checkers/python/integrations:hamcrest",
        "//third_party/py/checkers/python/integrations/pyunit",
        "//third_party/py/gflags",
    ],
)

py_test(
    name = "example3_test",
    srcs = [
        "add_tests.py",
        "example3_test.py",
        "subtract_tests.py",
    ],
    deps = [
        "//testing/pybase",
        "//third_party/py/checkers/python:checkers",
        "//third_party/py/checkers/python/integrations:hamcrest",
        "//third_party/py/checkers/python/integrations/pyunit",
        "//third_party/py/gflags",
    ],
)

py_test(
    name = "example4_test",
    srcs = [
        "calculator.py",
        "example4_test.py",
    ],
    deps = [
        "//testing/pybase",
        "//third_party/py/checkers/python:checkers",
        "//third_party/py/checkers/python/integrations:hamcrest",
        "//third_party/py/checkers/python/integrations/pyunit",
        "//third_party/py/gflags",
    ],
)

py_test(
    name = "example5_test",
    srcs = [
        "calculator.py",
        "divide_tests.py",
        "example5_test.py",
    ],
    deps = [
        "//testing/pybase",
        "//third_party/py/checkers/python:checkers",
        "//third_party/py/checkers/python/integrations:hamcrest",
        "//third_party/py/checkers/python/integrations/pyunit",
        "//third_party/py/gflags",
    ],
)

py_test(
    name = "example6_test",
    srcs = ["example6_test.py"],
    deps = [
        "//testing/pybase",
        "//third_party/py/checkers/python:checkers",
        "//third_party/py/checkers/python/integrations:hamcrest",
        "//third_party/py/checkers/python/integrations/pyunit",
        "//third_party/py/gflags",
    ],
)

py_test(
    name = "example7_test",
    srcs = [
        "calculator.py",
        "divide_tests.py",
        "example7_test.py",
    ],
    deps = [
        "//testing/pybase",
        "//third_party/py/checkers/python:checkers",
        "//third_party/py/checkers/python/integrations:hamcrest",
        "//third_party/py/checkers/python/integrations/pyunit",
        "//third_party/py/gflags",
    ],
)

py_test(
    name = "example8_test",
    srcs = [
        "calculator.py",
        "example8_test.py",
    ],
    deps = [
        "//testing/pybase",
        "//third_party/py/checkers/python:checkers",
        "//third_party/py/checkers/python/integrations:hamcrest",
        "//third_party/py/checkers/python/integrations/pyunit",
        "//third_party/py/gflags",
    ],
)

# example9_test has been depricated.

py_test(
    name = "example10_test",
    srcs = [
        "example10_test.py",
        "multiply_tests.py",
    ],
    deps = [
        "//testing/pybase",
        "//third_party/py/checkers/python:checkers",
        "//third_party/py/checkers/python/integrations:hamcrest",
        "//third_party/py/checkers/python/integrations/pyunit",
        "//third_party/py/gflags",
    ],
)

py_test(
    name = "example11_test",
    srcs = [
        "example11_test.py",
    ],
    deps = [
        "//testing/pybase",
        "//third_party/py/checkers/python:checkers",
        "//third_party/py/checkers/python/integrations:hamcrest",
        "//third_party/py/checkers/python/integrations/pyunit",
        "//third_party/py/gflags",
    ],
)
