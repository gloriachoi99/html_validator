#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    s = []
    balanced = True
    tags = _extract_tags(html)
    for i in range(len(tags)):
        singletag = tags[i]
        if '/' not in singletag: # if not a closing tag
            s.append(singletag)
        else:                    # if a closing tag
            if s == []:
                balanced = False
            else:
                top = s.pop()
                if top[1:] != singletag[2:]:  # if the tags do not match
                    balanced = False # not a match
    if balanced and s == []:
        return True
    else:
        return False

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    list = []
    for i in range(len(html)-1):
        str = ""
        if html[i] == "<":
            str += html[i]
            i += 1
            while html[i] != ">" and i < len(html)-1:
                str += html[i]
                i += 1
            tag = str + ">"
            list.append(tag)
    return list


