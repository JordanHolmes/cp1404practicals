import wikipedia

# wikipedia.search("Barack")
# wikipedia.suggest("Barak Obama")
#
# wikipedia.search("Ford", results=3)
#
# wikipedia.summary("GitHub")
# wikipedia.summary("Apple III", sentences=1)
#
# wikipedia.summary("Mercury")
# try:
#     mercury = wikipedia.summary("Mercury")
# except wikipedia.exceptions.DisambiguationError as e:
#     print(e.options)
# wikipedia.summary("zvv")
#
# ny = wikipedia.page("New York")
# print(ny.title)
# print(ny.url)
# print(ny.content)
# print(ny.images[0])
# print(ny.links[0])
#
# wikipedia.set_lang("fr")
# print(wikipedia.summary("Francois Hollande"))
#
# print('en' in wikipedia.languages())
# print(wikipedia.languages()['es'])

page_title = input("Page title: ")
while page_title != "":
    try:
        user_page = wikipedia.page(page_title)
        print(user_page.title)
        print(user_page.summary)
        print(user_page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

    page_title = input("Page title: ")
