from nicegui import ui, native
from random import randint


def root():
    """
    Passed later in ui.run()

    Nicegui requires either root() or decorated pages to be defined if you want to package
    the program as a stand-alone application. 'Script mode' (going without either) works in 
    debugger but throws an error once packaged as a single file.

    https://nicegui.io/documentation/section_configuration_deployment#package_for_installation
    """

    word_list = [
        "the", "be", "to", "of", "and", "a", "in", "that", "have",
        "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
        "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
        "or", "an", "will", "my", "one", "all", "would", "there", "their", "is",
        "are", "was", "were", "been", "has", "had", "can", "could", "should", "may",
        "might", "must", "who", "what", "when", "where", "why", "how", "which", "if",
        "than", "then", "them", "these", "those", "because", "so", "up", "out", "about",
        "into", "over", "after", "before", "between", "through", "during", "without",
        "under", "again", "still", "very", "just", "only", "also", "even", "most", "much",
    ]

    def pick_new_word() -> None:
        index = randint(0, len(word_list)-1)
        prompt.text = word_list[index]

    def check_for_match() -> None:
        if prompt.text == input_box.value:
            #input_box.style('background-color: #21ba45')
            ui.notify("Correct!", type="positive")
            pick_new_word()
            if delete_hint.content == "":
                delete_hint.content = "**Great job!** Now say \"Clear Line\" to clear the text box."

    ui.add_head_html('''
    <style>
    body {
        background-color: #f9f9f9;
    }
    </style>
    ''')

    with ui.column().classes("items-center"):

        ui.html("<h4>Talon Skills: The Alphabet", sanitize=False)

        with ui.element('div').classes('p-2 bg-blue-100 align-center'):
            ui.markdown("""
            The first step to learning Talon is learning Talon's phonetic alphabet. \n
            Let's practice writing words one letter at a time.\n
            If you need a hint, say **\"customize alphabet\"** to open your customizable list of phonetic letters.
            """).classes("text-center")

        prompt = ui.label("").style("font-size: 2em")
        #Initialize newly made prompt with a random word
        pick_new_word()

        with ui.card():
            input_box = ui.input("Write the word above.", on_change=lambda: check_for_match()).style("font-size: 2em")

        with ui.element('div'):
            delete_hint = ui.markdown("")

ui.run(root, title="Talon Skills: The Alphabet", favicon="🦉", reload=False, native=True, port=native.find_open_port())
