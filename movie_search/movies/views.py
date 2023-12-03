from django.shortcuts import render
from .forms import MovieSearchForm
from .utils import get_movie_details_by_title

def movie_search_view(request):
    if request.method == 'POST':
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            # Replace 'YOUR_API_KEY' with your actual OMDb API key
            api_key = '2853f67b'
            movie_details = get_movie_details_by_title(api_key, title)
            return render(request, 'movies/results.html', {'details': movie_details})
    else:
        form = MovieSearchForm()
    return render(request, 'movies/search.html', {'form': form})
