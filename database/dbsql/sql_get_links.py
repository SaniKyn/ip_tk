from ..common.model import Links


def add_link(https_link, name_link):
    Links.create(https_link = https_link, name_link=name_link)

def delete_link(name_link):
    Links.get(name_link==name_link).delete_instance()
