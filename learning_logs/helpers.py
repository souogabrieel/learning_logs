from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def paginate(request, obj_list, num_items=10):
    page = request.GET.get("pagina", 1)
    paginator = Paginator(obj_list, num_items)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj


def search_topics(request, topics_list):
    search_term = request.GET.get("q") or ""

    if search_term:
        topics_list = topics_list.filter(Q(title__istartswith=search_term))

    return search_term, topics_list
