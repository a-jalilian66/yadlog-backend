from bs4 import BeautifulSoup
from django.utils.text import slugify


def extract_toc_and_ids(html):
    soup = BeautifulSoup(html, 'html.parser')
    toc = []
    counter = 1

    for tag in soup.find_all('div'):
        classes = tag.get('class') or []

        # Only divs with class 'ckeditor-toc'
        level = None
        for cls in classes:
            if cls.startswith("toc-level-"):
                try:
                    level = int(cls.replace("toc-level-", ""))
                    break
                except ValueError:
                    continue

        if level is None:
            continue  # This div has nothing to do with TOC

        text = tag.get('title') or tag.get_text(strip=True)

        if not tag.get('id'):
            base_id = slugify(text, allow_unicode=False)
            tag['id'] = f"{base_id or 'section'}-{counter}"
            counter += 1

        toc.append({
            'text': text,
            'id': tag['id'],
            'level': level
        })

    return str(soup), toc