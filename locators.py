
## поле имя на странице регистрации
name_imput = '//label[text()="Имя"]/following-sibling::input'

## поле емэйл
email_input_login = '//label[text()="Email"]/following-sibling::input'

## поле пароль
password_input_login = '//label[text()="Пароль"]/following-sibling::input'

################################## BUTTONS ############################################

## кнопка на странице регистрации
registration_button = '//button[text()="Зарегистрироваться"]'

## кнопка входа на главной странице
login_button_on_main = '//button[text()="Войти в аккаунт"]'

#кнопка личный кабинет на главной
personal_account = '//a[@href="/account"]'
#//label[text()='Email']/following-sibling::input

# кнопка перехода на страницу регистрации на странице вход
registration_page = "//a[text()='Зарегистрироваться']"

## logo
logo = '//a[@href="/"]'

## кнопка войти на странице входа
login_button_on_login_page = '//button[text()="Войти"]'

## раздел соусов
sause_chapter = '//span[text()="Соусы"]/parent::div'

##раздел булок
bun_chapter = '//span[text()="Булки"]/parent::div'

##раздел начинок
topping_chapter = '//span[text()="Начинки"]/parent::div'

##сообщение об некорректном пароле
uncorrect_password_msg = '//p[text()="Некорректный пароль"]'

##кнопка выхода из личного кабинета
logout_button = '//button[text()="Выход"]'

##кнопка войти на странице регистрации
login_button_on_reg_page = '//a[text()="Войти"]'

##кнопка для перехода на страницу восстановления пароля со страницы входа
password_recover_button = '//a[text()="Восстановить пароль"]'

## Текст в поле формы данных профиля
profile_data_form_text = "//label[text()='Логин']"