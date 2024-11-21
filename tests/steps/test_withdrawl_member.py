import re, json
from pages.home import HomePage
from pages.signup import SignUpPage
from pages.mypage import MyPage
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers

# ガーキンファイルの読み込み
scenarios('withdrawl_member.feature')

# conftestに移管
""" @given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()

@when('会員登録リンクを押下する')
def step_when(home_page: HomePage):
    home_page.click_signup()

@when(parsers.parse('ページの見出しが「会員登録」であることを確認する'))
def step_when(signup_page: SignUpPage):
    expect(signup_page.signup_heading).to_contain_text("会員登録")

@when(parsers.parse('会員登録画面で「{signup_input}」を入力する'))
def step_when(signup_page: SignUpPage, signup_input):

    # JSONを辞書に格納
    signup_input_dictionaly = json.loads(signup_input)
    name = signup_input_dictionaly['会員情報_入力']['name']
    email = signup_input_dictionaly['会員情報_入力']['email']
    password = signup_input_dictionaly['会員情報_入力']['password']
    password_confirm = signup_input_dictionaly['会員情報_入力']['password_confirm']
    rank = signup_input_dictionaly['会員情報_入力']['rank']
    address = signup_input_dictionaly['会員情報_入力']['address']
    phone = signup_input_dictionaly['会員情報_入力']['phone']
    gender = signup_input_dictionaly['会員情報_入力']['gender']
    birthday = signup_input_dictionaly['会員情報_入力']['birthday']
    check_flag = signup_input_dictionaly['会員情報_入力']['check_flag']
    
    # 各入力欄の入力
    signup_page.fill_email(email)
    signup_page.fill_password(password)
    signup_page.fill_password_confirm(password_confirm)
    signup_page.fill_name(name)
    signup_page.select_rank(rank)
    signup_page.fill_address(address)
    signup_page.fill_phone(phone)
    signup_page.select_gender(gender)
    signup_page.fill_birthday(birthday)
    signup_page.check_notification(check_flag)

@when(parsers.parse('登録ボタンを押下する'))
def step_when(signup_page: SignUpPage):
    signup_page.click_signup()

@when(parsers.parse('ページの見出しが「マイページ」であることを確認する'))
def step_when(my_page: MyPage):
    expect(my_page.mypage_heading).to_contain_text("マイページ")

@when(parsers.parse('退会するボタンを押下'))
def step_when(my_page: MyPage):
    my_page.withdraw_member()

@then(parsers.parse('タイトルに「HOTEL PLANISPHERE」が含まれていることを確認'))
def step_then(home_page: HomePage):
    expect(home_page.page).to_have_title(re.compile("HOTEL PLANISPHERE")) """











