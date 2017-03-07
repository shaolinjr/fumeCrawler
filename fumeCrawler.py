from selenium import webdriver
from selenium.webdriver.support.ui import Select
from collections import OrderedDict
from clint.textui import puts, colored

class FumeCrawler (object):

    def __init__ (self, RA="", password=""):
        self.RA = RA
        self.password = password

    def run(self):

        puts(colored.green("Bem vindo ao FUMECrawler!\n", bold=True))

        print("Atualmente, você tem 2 opções: \n\t1)Buscar horário de aulas\n\t2)Buscar data de provas")
        choice = input("O que deseja fazer?: ")

        while choice not in {'1', '2'}:
            choice = input("Valor inválido, digite novamente!: ")

        if len(self.RA) == 0:
            self.RA = input("Digite seu RA: ")
            while not len(self.RA) == 11:
                puts(colored.red("RA Inválido!"))
                self.RA = input("Digite seu RA novamente: ")

        if len(self.password) == 0:
            self.password = input("Digite sua senha: ")
            while not len(self.password) > 0:
                puts(colored.red("Senha não pode ficar em branco!"))
                self.password = input("Digite sua senha novamente: ")

        browser = webdriver.PhantomJS('/usr/local/bin/phantomjs')
        browser.get('https://ww2.fumec.br/sinefmobile/')

        browser.implicitly_wait(5)

        login_field = browser.find_element_by_xpath('//*[@id="contact-form"]/div[3]/label/input')
        pass_field = browser.find_element_by_xpath('//*[@id="contact-form"]/div[4]/label/input')
        login_button = browser.find_element_by_xpath('//*[@id="contact-submit"]')

        login_field.send_keys(self.RA)
        pass_field.send_keys(self.password)
        login_button.click()
        browser.implicitly_wait(5)

        if choice == '1':

            print(colored.blue("\nBuscando horários: \n"))
            browser.get('https://ww2.fumec.br/sinefmobile/academico/horario_aula')  # we got the schedule

            days = browser.find_elements_by_css_selector('table.table tr td.footable-first-column')
            # print(browser.page_source)

            schedule = OrderedDict()
            for day in days:
                day.click()
                schedule.update({day.text: ''})
                schedule.move_to_end(day.text, last=False)

            subjects = [subject.text.split('\n') for subject in browser.find_elements_by_css_selector(
                '#content > div > div > div > div > div.well-content.no-search > div.responsive_table_scroll > table > tbody > tr > td > div')]

            segunda = subjects[0]
            terca = subjects[1]
            quarta = subjects[2]
            quinta = subjects[3]
            sexta = subjects[4] if not subjects[4] == [
                ''] else []  # ternario pra ver se o array de sexta é == a '', que aparentemente no python, != []
            schedule["Segunda"] = segunda
            schedule["Terca"] = terca
            schedule["Quarta"] = quarta
            schedule["Quinta"] = quinta
            schedule["Sexta"] = sexta

            schedule = OrderedDict(reversed(schedule.items()))

            for key in schedule:
                if not len(schedule[key]) == 0:
                    puts(colored.cyan("{0}:".format(key)))

                    for v in schedule[key]:
                        horario = v[:13]
                        sala = v[-12:]
                        materia = v[13:-12] #pegando as strings que vem e tratando para pegar o que interessa

                        print("{0}".format(colored.green(horario) + colored.blue(materia) + colored.magenta(sala)))
                else:
                    pass
        else:
            puts(colored.blue("\nBuscando datas de provas:\n"))
            browser.get('https://ww2.fumec.br/sinefmobile/academico/data_avaliacao')
            select = Select(browser.find_element_by_id('selectDataAvaliacao'))
            select.select_by_index(0)
            provas = browser.find_elements_by_class_name('bloco-titulo-simple')
            datas_provas = browser.find_elements_by_class_name('simple-block-resposta')
            # print(provas[0].text)
            # print(datas_provas[0].text)

            for index,prova in enumerate(provas):
                puts(colored.blue(prova.text)+colored.magenta(" ==> ")+colored.green(datas_provas[index].text))

        browser.quit()

FumeCrawler().run()