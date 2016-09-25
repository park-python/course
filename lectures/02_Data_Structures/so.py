#!/usr/bin/env python
"""
This is a simple example how to use stackoveflow.com API to get answers on
your questions directly in terminal.

Actually more robust tools doing the same already exist but here our goal
to demonstrate working with real data in API response on real example.
"""
import sys
import requests
import re
from bs4 import BeautifulSoup


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 ' \
             'Safari/537.36'

# All StackExchange API available via this endpoint.
# See docs at https://api.stackexchange.com/docs
SE_API_ENDPOINT = "https://api.stackexchange.com"

# Here we want to get answers from stackoverflow.com but it's possible to
# just change this const to search on any StackExchange site (security.stackexchange
# for example)
SE_SITE = "stackoverflow"


class SoException(Exception):
    pass


def _get_response(endpoint, params=None):
    headers = {'User-Agent': USER_AGENT}
    try:
        resp = requests.get(endpoint, headers=headers, params=params, timeout=5)
    except requests.RequestException as e:
        raise SoException(e)
    if resp.status_code != 200:
        raise SoException("wrong status code")
    return resp


def _get_response_text(endpoint, params=None):
    resp = _get_response(endpoint, params=params)
    return resp.text


def _get_response_json(endpoint, params=None):
    resp = _get_response(endpoint, params=params)
    return resp.json()


def _get_question_answers(question_id):
    params = {
        "site": SE_SITE,
        "filter": "withbody"
    }
    url = SE_API_ENDPOINT + "/questions/{ids}/answers".format(ids=question_id)
    data = _get_response_json(url, params=params)
    return data.get("items")


def _get_question_id_from_google(query):
    search_for = "{site} {query}".format(site=SE_SITE, query=query)
    params = {"q": search_for}
    html = _get_response_text("https://www.google.com/search", params=params)
    soup = BeautifulSoup(html, "html.parser")
    for elem in soup.findAll("h3", {"class": "r"}):
        link = elem.find("a")
        href = link.attrs["href"]
        if "://{site}.com/questions".format(site=SE_SITE) not in href:
            continue
        match = re.search(r'\d+', href)
        if match:
            return match.group()
    return None


def get_best_answer(query):
    """Given a string query returns best answer object from Stackoverflow"""
    question_id = _get_question_id_from_google(query)
    if not question_id:
        return None

    answers = _get_question_answers(question_id)
    if not answers:
        return None

    best_score = -1
    best_answer = None

    for answer in answers:
        score = answer["score"]
        if score > best_score:
            best_answer = answer
            best_score = score
        if answer["is_accepted"]:
            best_answer = answer
            break

    if not best_answer:
        return None

    return best_answer


def _main():
    try:
        query_text = " ".join(sys.argv[1:])
    except IndexError:
        print("Ask your question")
        sys.exit(1)

    try:
        answer = get_best_answer(query_text)
    except SoException as err:
        print("Error:", err)
        sys.exit(1)

    if not answer:
        print("Answer not found")
        sys.exit(1)

    # strip HTML tags for better look in terminal.
    soup = BeautifulSoup(answer["body"], "html.parser")
    print(soup.get_text())
    print("\nhttps://{site}.com/questions/{q_id}".format(
        site=SE_SITE, q_id=answer["question_id"]
    ))


if __name__ == "__main__":
    _main()
