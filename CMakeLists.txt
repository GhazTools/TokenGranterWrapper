cmake_minimum_required(VERSION 3.23)
project(TokenGranterWrapperBindings)
set(CMAKE_CXX_STANDARD 17)

add_subdirectory(./lib/include/pybind11)
add_subdirectory(./lib/src)

set(SOURCE_DIR "src/token_granter_wrapper")
set(SOURCES "${SOURCE_DIR}/token_granter_bindings.cpp")

pybind11_add_module(token_granter_bindings ${SOURCES})
target_link_libraries(token_granter_bindings PRIVATE token_granter)
