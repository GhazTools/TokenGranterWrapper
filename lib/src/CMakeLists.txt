cmake_minimum_required(VERSION 3.23)
project(TokenGranterWrapper)

set(CMAKE_CXX_STANDARD 17)

set(CURL_LIBRARY "-lcurl") 
find_package(CURL REQUIRED)

add_library(token_granter STATIC token_granter.cpp)

target_link_libraries(token_granter ${CURL_LIBRARIES})
set_target_properties(token_granter PROPERTIES POSITION_INDEPENDENT_CODE ON)
