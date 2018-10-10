from functools import reduce


def find_line_nums(query_word):
    """
    Method to find line numbers for query_word
    Arg: str
    Return: List[Int]
    """
    found_line_nums = []
    with open('hscic-news.txt', 'r') as news_file:
        for line_num, line in enumerate(news_file, 0):
            if query_word in line:
                found_line_nums.append(line_num)
    return found_line_nums


def search(query_str, query_type):
    """
    Method to search input query_str with query_type in file"
    Arg: str, str
    Return: List[Int] or Empty List
    """
    found_arr = []
    for query_word in query_str.split():
        found_arr.append(find_line_nums(query_word))

    result = []
    if found_arr:
        if query_type == "OR":
            result = sorted(list(set().union(*found_arr)))
        elif query_type == "AND":
            result = sorted(list(reduce(set.intersection, [set(item) for item in found_arr])))
        else:
            pass

    return result