// STL IMPORTS STARTS HERE
#include <iostream>

// THIRD PARTY IMPORTS HERE
#include <curl/curl.h>
#include "../include/json.hpp"

using json = nlohmann::json;

#pragma once

class TokenGranter
{
public:
    TokenGranter(const std::string &token_granter_url);

    // PUBLIC METHODS HERE
    std::string grant_access_token(const std::string &username, const std::string &password, const bool temporary) const;
    bool validate_token(const std::string &username, const std::string &token) const;

private:
    std::string token_granter_url_;

    // PRIVATE METHODS HERE
    nlohmann::json make_post_request(const std::string &request_url, nlohmann::json &request) const;
    static size_t post_request_callback(void *contents, size_t size, size_t nmemb, std::string *userp);
};