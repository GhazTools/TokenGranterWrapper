cmake_minimum_required(VERSION 3.23)
project(TokenGranterWrapper)

set(CMAKE_CXX_STANDARD 17)

set(CURL_LIBRARY "-lcurl") 
find_package(CURL REQUIRED)

# add_executable(token_granter src/token_granter.cpp)
# target_include_directories(token_granter PRIVATE ${CURL_INCLUDE_DIRS})
# target_link_libraries(token_granter ${CURL_LIBRARIES})

# SHARED LIBRARY COMPILATION HERE
add_library(token_granter_shared SHARED src/token_granter.cpp)
target_link_libraries(token_granter_shared ${CURL_LIBRARIES})
target_link_libraries(token_granter_shared ${CURL_LIBRARIES})


# PYBINDING SHARED LIBRARY COMPILATION HERE
add_subdirectory(./include/pybind11)
pybind11_add_module(token_granter ./src/token_granter_bindings.cpp ./src/token_granter.cpp) 
set_target_properties(token_granter PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/token_granter_wrapper)
target_link_libraries(token_granter PRIVATE pybind11::module)
target_link_libraries(token_granter PRIVATE ${CURL_LIBRARIES})