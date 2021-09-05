def get_pagination_data(data):
    try:
        return {
                "page": data.page,
                "has_prev": data.has_prev,
                "pages": data.pages,
                "per_page": data.per_page,
                "has_next": data.has_next,
                "next_num": data.next_num,
                "prev_num": data.prev_num,
                "total_count": data.total
            }
    except:
        return None
