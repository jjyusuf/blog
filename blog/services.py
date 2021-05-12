from .models import Article


def create_article(title, body, owner, published, promoted):
    article = Article.objects.create(
        title=title,
        body=body,
        owner=owner,
        published=published,
        promoted=promoted
    )

    return article


def update_article(id, title, body):
    article = Article.objects.get(id)
    article.title = title
    article.body = body
    article.save()
    return article