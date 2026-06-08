from urllib.parse import urlparse
import re


def extract_features(url):
    url = str(url).lower()

    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("www.", "")
    url = url.replace("[", "")
    url = url.replace("]", "")

    try:
        parsed_url = urlparse("http://" + url)
        domain = parsed_url.netloc
        path = parsed_url.path
    except:
        domain = url.split("/")[0]
        path = ""

    features = {
        "url_length": len(url),
        "domain_length": len(domain),
        "path_length": len(path),
        "count_dots": url.count("."),
        "count_hyphen": url.count("-"),
        "count_at": url.count("@"),
        "count_question": url.count("?"),
        "count_equal": url.count("="),
        "count_slash": url.count("/"),
        "count_digits": sum(char.isdigit() for char in url),
        "has_https": 1 if "https" in url else 0,
        "has_ip_address": 1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0,
        "has_suspicious_words": 1 if any(word in url for word in ["login", "verify", "bank", "secure", "account", "update"]) else 0
    }

    return list(features.values())