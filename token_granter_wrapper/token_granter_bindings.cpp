#include "../include/token_granter.hpp"

// EXTERNAL IMPORTS START HERE
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
// EXTERNAL IMPORTS END HERE

namespace py = pybind11;

PYBIND11_MODULE(token_granter, m)
{
    py::class_<TokenGranter>(m, "TokenGranter")
        .def(py::init<const std::string &>())
        .def("grant_access_token", &TokenGranter::grant_access_token)
        .def("validate_token", &TokenGranter::validate_token);
}