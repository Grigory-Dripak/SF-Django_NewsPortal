from django import template


register = template.Library()

blocks = ['exercise', 'substance', 'tennis', 'railway', 'train']

@register.filter()
def censor(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError('Фильтр работает только с текстом')
    else:
        for i in blocks:
            o = '*'*(len(i)-1)
            text = text.replace(f' {i}', f' {i[0]}{o}')
            text = text.replace(f'{i.title()}', f'{i[0].upper()}{o}')
    return text
