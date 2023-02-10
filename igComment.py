from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import emoji


class InstagramComments:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"./geckodriver"
        )
        """ # Coloque o caminho para o seu geckodriver aqui, lembrando que você precisa instalar o firefox e geckodriver na versão mais atual """
        # Link download do geckodriver: https://github.com/mozilla/geckodriver/releases
        # Link download Firefox https://www.mozilla.org/pt-BR/firefox/new/

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/emailsignup/")
        # print("deu certo")
        time.sleep(3)
        # print("acabou o timpe")
        button_login = driver.find_element(By.LINK_TEXT, 'Conecte-se')
        button_login.click()
        time.sleep(3)

        user_element = driver.find_element(By.NAME, 'username')
        user_element.click()
        user_element.clear()
        user_element.send_keys(self.username)

        password_element = driver.find_element(By.NAME, 'password')
        password_element.click()
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)

        time.sleep(5)

        self.automaticComments('imperialufla')

    def type_like_a_person(self, sentence):
        driver = self.driver
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field = driver.find_element(
                By.XPATH, "//textarea[@aria-label='Adicione um comentário...']")
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def automaticComments(self, nome_de_usuario):
        driver = self.driver
        driver.get("https://www.instagram.com/" + nome_de_usuario + "/")
        time.sleep(3)

        driver.get("https://www.instagram.com/p/CoVEmPYgf42/")
        # Caso tenha uma tela grande, isso garante que a imagem está em uma area visivel
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:

            comments = ["Temos que ganhar esse trem aqui hein tropa ", "Hoje batemos 4k?? ", "10k até o fds hein  ", "queria um amor e a Imperial me deu 9923984 comentarios para fazer ", "Não aguento mais comentar viu ", "amo voces pra um caralho ", "Proximo role quanto? "]
            emojisArray = ["👓","🕶️","🕶","🥽","🥼","🦺","👔","👕","👖","🧣","🧤","🧥","🧦","👗","👘","🥻","🩱","🩲","🩳","👙","👚","👛","👜","👝","🛍️","🛍","🎒","🩴","👞","👟","🥾","🥿","👠","👡","🩰","👢","👑","👒","🎩","🎓","🧢","🪖","⛑️","⛑","📿","💄","💍","💎","🔇","🔈","🔉","🔊","📢","📣","📯","🔔","🔕","🎼","🎵","🎶","🎙️","🎙","🎚️","🎚","🎛️","🎛","🎤","🎧","📻","🎷","🪗","🎸","🎹","🎺","🎻","🪕","🥁","🪘","📱","📲","☎️","☎","📞","📟","📠","🔋","🪫","🔌","💻","🖥️","🖥","🖨️","🖨","⌨️","⌨","🖱️","🖱","🖲️","🖲","💽","💾","💿","📀","🧮","🎥","🎞️","🎞","📽️","📽","🎬","📺","📷","📸","📹","📼","🔍","🔎","🕯️","🕯","💡","🔦","🏮","🪔","📔","📕","📖","📗","📘","📙","📚","📓","📒","📃","📜","📄","📰","🗞️","🗞","📑","🔖","🏷️","🏷","💰","🪙","💴","💵","💶","💷","💸","💳","🧾","💹","✉️","✉","📧","📨","📩","📤","📥","📦","📫","📪","📬","📭","📮","🗳️","🗳","✏️","✏","✒️","✒","🖋️","🖋","🖊️","🖊","🖌️","🖌","🖍️","🖍","📝","💼","📁","📂","🗂️","🗂","📅","📆","🗒️","🗒","🗓️","🗓","📇","📈","📉","📊","📋","📌","📍","📎","🖇️","🖇","📏","📐","✂️","✂","🗃️","🗃","🗄️","🗄","🗑️","🗑","🔒","🔓","🔏","🔐","🔑","🗝️","🗝","🔨","🪓","⛏️","⛏","⚒️","⚒","🛠️","🛠","🗡️","🗡","⚔️","⚔","🔫","🪃","🏹","🛡️","🛡","🪚","🔧","🪛","🔩","⚙️","⚙","🗜️","🗜","⚖️","⚖","🦯","🔗","⛓️","⛓","🪝","🧰","🧲","🪜","⚗️","⚗","🧪","🧫","🧬","🔬","🔭","📡","💉","🩸","💊","🩹","🩼","🩺","🩻","🚪","🛗","🪞","🪟","🛏️","🛏","🛋️","🛋","🪑","🚽","🪠","🚿","🛁","🪤","🪒","🧴","🧷","🧹","🧺","🧻","🪣","🧼","🫧","🪥","🧽","🧯","🛒","🚬","⚰️","⚰","🪦","⚱️","⚱","🗿","🪧","🪪","🏧","🚮","🚰","♿","🚹","🚺","🚻","🚼","🚾","🛂","🛃","🛄","🛅","⚠️","⚠","🚸","⛔","🚫","🚳","🚭","🚯","🚱","🚷","📵","🔞","☢️","☢","☣️","☣","⬆️","⬆","↗️","↗","➡️","➡","↘️","↘","⬇️","⬇","↙️","↙","⬅️","⬅","↖️","↖","↕️","↕","↔️","↔","↩️","↩","↪️","↪","⤴️","⤴","⤵️","⤵","🔃","🔄","🔙","🔚","🔛","🔜","🔝","🛐","⚛️","⚛","🕉️","🕉","✡️","✡","☸️","☸","☯️","☯","✝️","✝","☦️","☦","☪️","☪","☮️","☮","🕎","🔯","♈","♉","♊","♋","♌","♍","♎","♏","♐","♑","♒","♓","⛎","🔀","🔁","🔂","▶️","▶","⏩","⏭️","⏭","⏯️","⏯","◀️","◀","⏪","⏮️","⏮","🔼","⏫","🔽","⏬","⏸️","⏸","⏹️","⏹","⏺️","⏺","⏏️","⏏","🎦","🔅","🔆","📶","📳","📴","♀️","♀","♂️","♂","⚧️","⚧","✖️","✖","➕","➖","➗","🟰","♾️","♾","‼️","‼","⁉️","⁉","❓","❔","❕","❗","〰️","〰","💱","💲","⚕️","⚕","♻️","♻","⚜️","⚜","🔱","📛","🔰","⭕","✅","☑️","☑","✔️","✔","❌","❎","➰","➿","〽️","〽","✳️","✳","✴️","✴","❇️","❇","©️","©","®️","®","™️","™","#️⃣","#⃣","*️⃣","*⃣","0️⃣","0⃣","1️⃣","1⃣","2️⃣","2⃣","3️⃣","3⃣","4️⃣","4⃣","5️⃣","5⃣","6️⃣","6⃣","7️⃣","7⃣","8️⃣","8⃣","9️⃣","9⃣","🔟","🔠","🔡","🔢","🔣","🔤","🅰️","🅰","🆎","🅱️","🅱","🆑","🆒","🆓","ℹ️","ℹ","🆔","Ⓜ️","Ⓜ","🆕","🆖","🅾️","🅾","🆗","🅿️","🅿","🆘","🆙","🆚","🈁","🈂️","🈂","🈷️","🈷","🈶","🈯","🉐","🈹","🈚","🈲","🉑","🈸","🈴","🈳","㊗️","㊗","㊙️","㊙","🈺","🈵","🔴","🟠","🟡","🟢","🔵","🟣","🟤","⚫","⚪","🟥","🟧","🟨","🟩","🟦","🟪","🟫","⬛","⬜","◼️","◼","◻️","◻","◾","◽","▪️","▪","▫️","▫","🔶","🔷","🔸","🔹","🔺","🔻","💠","🔘","🔳","🔲","🏁","🚩","🎌","🏴","🏳️","🏳","🏳️‍🌈","🏳‍🌈","🏳️‍⚧️","🏳‍⚧️","🏳️‍⚧","🏳‍⚧","🏴‍☠️"]
            for emojiItem in emojisArray:
                time.sleep(3)
                driver.find_element(
                    By.XPATH, "//textarea[@aria-label='Adicione um comentário...']")
                time.sleep(random.randint(3, 6))
                
                phrase = random.choice(comments)
                self.type_like_a_person(phrase)
                time.sleep(random.randint(3, 7))


                single_input_field = driver.find_element(
                    By.XPATH, "//textarea[@aria-label='Adicione um comentário...']")
                single_input_field.send_keys(emojiItem)

                time.sleep(random.randint(4, 9))

                driver.find_element(By.XPATH, "//div[text()='Publicar']").click()

                time.sleep(random.randint(3, 9))
        except Exception as e:
            print(e)
            time.sleep(5)


imperialComments = InstagramComments("username", "password")
imperialComments.login()
