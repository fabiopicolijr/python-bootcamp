from datetime import datetime
import codecs
import random
import requests
import smtplib

from config import FILES_PATH, TEMPLATES_PATH

MY_NAME = "Fábio Picoli Jr."
MY_EMAIL = "fabiopicolijr.developer@gmail.com"
MY_PASSWORD = "cngmonqjhrljkdrv"


class BirthdateWisher:

    def execute(self):
        # TODO: needs refactor.
        today = datetime.now()
        today_tuple = (today.month, today.day)

        friends = self.get_friends()

        for friend in friends:
            if today_tuple == (friend["month"], friend["day"]):
                letter_path = f"{TEMPLATES_PATH}/letter_{random.randint(1, 3)}.txt"

                with codecs.open(f"{FILES_PATH}/quotes.txt", encoding='utf-8') as quote_file:
                    all_quotes = quote_file.readlines()
                    quote = random.choice(all_quotes)

                with codecs.open(letter_path, encoding='utf-8') as letter_file:
                    contents = letter_file.read()
                    contents = contents.replace("[NAME]", friend["name"])
                    contents = contents.replace("[MYNAME]", MY_NAME)
                    contents = contents.replace("[HANDLING]", friend["handling"])
                    contents = contents.replace("[QUOTE]", quote)

                try:
                    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                        connection.starttls()
                        connection.login(MY_EMAIL, MY_PASSWORD)
                        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=[friend["email"], "fabiopicolijr@gmail.com"],
                            msg=f"Subject:Feliz aniversárioooo!!!\n\n{contents}".encode('utf-8'),
                        )
                except TimeoutError as error:
                    print(f"[BIRTHDAY-WISHER] Falha ao tentar enviar o email. {error}")

                print(f"[BIRTHDAY-WISHER] E-mail sent to {friend['name']}!")

    @staticmethod
    def get_friends() -> list:
        sheety_get_endpoint = "https://api.sheety.co/c3871954a0a3d4a8077e875026d8e2c8/myFriends/friends"

        response = requests.get(url=sheety_get_endpoint)
        response.raise_for_status()
        friends = response.json()["friends"]

        return friends
