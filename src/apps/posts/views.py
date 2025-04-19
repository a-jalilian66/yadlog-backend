from django.views.generic import TemplateView, DetailView
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
        category_published = Category.objects.with_published_posts()[:8]
        context['categories'] = category_published
        context['hero_title'] = "YadLog"
        context['hero_subtitle'] = "آنچه می‌آموزم، می‌نویسم — از نکات ریز تا تجربه‌های فنی"

        # Popular Content Section
        context['popular'] = Post.published.order_by('-publication_date')[:5]

        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hero_title'] = self.object.title
        context["toc"] = self.object.toc or []
        context['hero_subtitle'] = ""
        return context

    def get_queryset(self):
        return Post.published.all()
