from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    notice_list = find_news()
    # Find news traz tudo do banco, com isso!
    # preciso apenas popular meu array \/ abaixo
    title_url_list = []
    # print(notice_list, title)

    for notice in notice_list:
        if notice["title"] == title or notice["title"].upper() == title:
            title_url_list.append((notice["title"], notice["url"]))

    return title_url_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    # date = datetime.date.fromisoformat(date)
    notice_list = find_news()
    # print(notice_list, date)
    title_url_list = []

    for notice in notice_list:
        try:
            # fromisoformat( date_string ) ¶
            # Retorne um datecorrespondente a um date_string fornecido
            # no formato YYYY-MM-DD:
            # https://docs.python.org/3/library/datetime.html
            datetime.date.fromisoformat(date)
            # gambiarra cabulosa quiz
            # fazer bonito fiz feito 0 é true -1 e false
            # 31/01/2020 revisão de código
            # se ele não encontrar a data vai no formato valido estora um erro
            # apenas capturei o erro e emiti a mensagem
            # mas a documentação
            # indica que foi passada um data não transformavel
            # erro começa na linha 35
            if notice["timestamp"].find(date) == 0:
                title_url_list.append((notice["title"], notice["url"]))
        except ValueError:
            raise ValueError("Data inválida")

    return title_url_list


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    notice_list = find_news()
    # print(notice_list, source)
    title_url_list = []

    for notice in notice_list:
        for fonte in notice["sources"]:
            if fonte.upper() == source.upper():
                title_url_list.append(
                    (notice["title"], notice["url"]))

    return title_url_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    notice_list = find_news()
    # print(notice_list, source)
    title_url_list = []

    for notice in notice_list:
        for categ in notice["categories"]:
            if categ.upper() == category.upper():
                title_url_list.append((notice["title"], notice["url"]))

    return title_url_list
