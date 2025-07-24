from ..common.model import Links


def add_link(https_link, name_link):
    Links.create(https_link = https_link, name_link=name_link)

def get_link(name):
    link = Links.get(Links.name_link == name)
    return link.https_link

def delete_link(name_link):
    Links.get(name_link==name_link).delete_instance()
