from datetime import datetime
import codecs
import pandas
import random
import smtplib

from config import FILES_PATH, TEMPLATES_PATH

MY_NAME = "Fábio Picoli Jr."
MY_EMAIL = "fabiopicolijr.developer@gmail.com"
MY_PASSWORD = "cngmonqjhrljkdrv"


class BirthdateWisher:

    @staticmethod
    def execute():
        # TODO: needs refactor.
        today = datetime.now()
        today_tuple = (today.month, today.day)

        data = pandas.read_csv(f"{FILES_PATH}/birthdays.csv")
        data.dropna(how="all", inplace=True)  # remove blank lines
        birthdays_dict = data.to_dict('records')

        for birthday_person in birthdays_dict:
            if today_tuple == (birthday_person["month"], birthday_person["day"]):
                letter_path = f"{TEMPLATES_PATH}/letter_{random.randint(1, 3)}.txt"

                with codecs.open(f"{FILES_PATH}/quotes.txt", encoding='utf-8') as quote_file:
                    all_quotes = quote_file.readlines()
                    quote = random.choice(all_quotes)

                with codecs.open(letter_path, encoding='utf-8') as letter_file:
                    contents = letter_file.read()
                    contents = contents.replace("[NAME]", birthday_person["name"])
                    contents = contents.replace("[MYNAME]", MY_NAME)
                    contents = contents.replace("[QUOTE]", quote)

                try:
                    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                        connection.starttls()
                        connection.login(MY_EMAIL, MY_PASSWORD)
                        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=[birthday_person["email"], "fabiopicolijr@gmail.com"],
                            msg=f"Subject:Feliz aniversárioooo!!!\n\n{contents}".encode('utf-8'),
                        )
                except TimeoutError as error:
                    print(f"Falha ao tentar enviar o email. {error}")

                print(f"1.[BIRTHDAY-WISHER] E-mail sent to {birthday_person['name']}!")
