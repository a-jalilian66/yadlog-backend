from django.views.generic import TemplateView
from .models import Post, Category


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page = int(self.request.GET.get('page', 1))
        per_page = 15
        start = (page - 1) * per_page
        end = start + per_page
        all_posts = Post.published.all()
        # all_posts = Post.objects.all()
        context['posts'] = all_posts[start:end]
        context['has_next'] = all_posts.count() > end
        context['has_previous'] = page > 1
        context['page_number'] = page

        # Categories section
        context['categories'] = Category.objects.all()[:8]

        # Popular Content Section
        context['popular'] = Post.published.order_by('-publication_date')[:5]

        return context

