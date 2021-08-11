MAX_PAGE_SIZE = 1000


def parse_pagination_params(request):
    page = int(request.args.get("page", 1))
    if page < 1:
        raise ValueError("Page parameter must be positive.")
    perpage = int(request.args.get("perpage", 100))
    if perpage > MAX_PAGE_SIZE:
        raise ValueError("Page size exceeded maximum.")
    return page, perpage
