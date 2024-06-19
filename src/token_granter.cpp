#include "../include/token_granter.hpp"

TokenGranter::TokenGranter(const std::string &token_granter_url) : token_granter_url_(token_granter_url) {}

std::string TokenGranter::grant_access_token(const std::string &username, const std::string &password, const bool temporary) const
{
    nlohmann::json j;
    j["username"] = username;
    j["password"] = password;
    j["temporary"] = temporary;

    try
    {
        nlohmann::json response = this->make_post_request(this->token_granter_url_ + "/token/grant", j);
        return response["token"];
    }
    catch (const std::exception &e)
    {
        return "";
    }
}

bool TokenGranter::validate_token(const std::string &username, const std::string &token) const
{
    nlohmann::json j;
    j["username"] = username;
    j["token"] = token;

    try
    {
        nlohmann::json response = this->make_post_request(this->token_granter_url_ + "/token/validate", j);
        int errorCode = response["ErrorCode"];

        return errorCode == 0;
    }
    catch (const std::exception &e)
    {
        return false;
    }
}

// PRIVATE METHODS HERE
nlohmann::json TokenGranter::make_post_request(const std::string &request_url, nlohmann::json &request) const
{
    try
    {
        CURL *curl;
        CURLcode res;
        std::string readBuffer;

        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers, "Content-Type: application/json");

        curl = curl_easy_init();

        if (curl)
        {
            curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
            curl_easy_setopt(curl, CURLOPT_URL, request_url.c_str());
            curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, post_request_callback);
            curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

            std::string json_data = request.dump();

            curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json_data.c_str());

            res = curl_easy_perform(curl);
            if (res != CURLE_OK)
                fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
            curl_easy_cleanup(curl);
        }

        curl_slist_free_all(headers);
        curl_global_cleanup();

        nlohmann::json json_response = nlohmann::json::parse(readBuffer);
        return json_response;
    }
    catch (const std::exception &e)
    {
        std::cerr << e.what() << '\n';
        throw;
    }
}

size_t TokenGranter::post_request_callback(void *contents, size_t size, size_t nmemb, std::string *userp)
{
    userp->append((char *)contents, size * nmemb);
    return size * nmemb;
}
