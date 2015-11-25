# Description:
#   Checkers python unit test framework.

licenses(["notice"])  # Apache v2.0

exports_files(["LICENSE"])

# vvv Migrate to cloudprint or clouddevices
load("/devtools/blueprint/build_defs/blueprint_test", "blueprint_tests")

exports_files(
    ["checkers.blueprint"],
    visibility = ["//visibility:public"],
)

blueprint_tests(
    name = "checkers_blueprint_tests",
    srcs = ["checkers.blueprint"],
)

test_suite(
    name = "config_tests",
    tests = [
        ":checkers_blueprint_tests",
    ],
)
# ^^^ Migrate to cloudprint or clouddevices

proto_library(
    name = "checkers_proto",
    testonly = 1,
    srcs = ["checkers.proto"],
    py_api_version = 2,
    visibility = ["//visibility:public"],
)

test_suite(
    name = "smoke_tests",
    tests = [
        "//third_party/py/checkers/examples/quickstart:smoke_tests",
    ],
    visibility = ["//visibility:public"],
)
