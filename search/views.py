from django.template.response import TemplateResponse
from algoliasearch_django import raw_search
from wagtail.models import Page
from products import models
from django.utils.text import slugify

def search(request):
    search_query = request.GET.get("query", None)
    params = {"hitsPerPage": 100}

    if search_query:
        response = raw_search(models.Product, search_query, params)
        search_results = response.get("hits", [])
        total_hits = response.get("nbHits", 0)

        # Generate slugs for each search result
        for result in search_results:
            result['slug'] = slugify(result['title'])

    else:
        search_results = []
        total_hits = 0

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
            "total_hits": total_hits,
        },
    )
