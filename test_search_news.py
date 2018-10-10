from .news_search import *


def test_search_1():
    query_str = "Care Quality Commission"
    query_type = "OR"
    result = search(query_str, query_type)
    assert result == [0, 1, 2, 3, 4, 5, 6]

def test_search_2():
    query_str = "September 2004"
    query_type = "OR"
    result = search(query_str, query_type)
    assert result == [9]

def test_search_3():
    query_str = "general population generally"
    query_type = "OR"
    result = search(query_str, query_type)
    assert result == [6, 8]

def test_search_4():
    query_str = "Care Quality Commission admission"
    query_type = "AND"
    result = search(query_str, query_type)
    assert result == [1]

def test_search_5():
    query_str = "general population Alzheimer"
    query_type = "AND"
    result = search(query_str, query_type)
    assert result == [6]

def test_search_wrong_query_type():
    query_str = "Care Quality Commission"
    query_type = "ORR"
    result = search(query_str, query_type)
    assert result == []

def test_search_empty_query_str():
    query_str = ""
    query_type = "OR"
    result = search(query_str, query_type)
    assert result == []