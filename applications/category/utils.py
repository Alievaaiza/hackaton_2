import re

from transliterate import slugify


def slug_generator(title):
    slug = title.lower()
    if bool(re.search('[а-яА-Я]', slug)):
        slug = slugify(slug)
    else:
        slug = slug.replace(' ', '-')
    return slug