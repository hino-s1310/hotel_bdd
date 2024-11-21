import json
from pages.home import HomePage
from pages.signup import SignUpPage
from pages.mypage import MyPage
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers

# ガーキンファイルの読み込み
scenarios('signup.feature')

# conftestbに移管
""" @given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()

@when('会員登録リンクを押下する')
def step_when(home_page: HomePage):
    home_page.click_signup()

@when('ページの見出しが「会員登録」であることを確認する')
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

@when('登録ボタンを押下する')
def step_when(signup_page: SignUpPage):
    signup_page.click_signup()

@then('ページの見出しが「マイページ」であることを確認する')
def step_then(my_page: MyPage):
    expect(my_page.mypage_heading).to_contain_text("マイページ")

@then(parsers.parse('マイページ画面で各項目が「{signup_validate}」であることを確認する'))
def step_then(my_page: MyPage, signup_validate):

    # JSONを辞書に格納
    signup_validate_dictionaly = json.loads(signup_validate)
    name = signup_validate_dictionaly['会員情報_検証']['name']
    email = signup_validate_dictionaly['会員情報_検証']['email']
    rank = signup_validate_dictionaly['会員情報_検証']['rank']
    address = signup_validate_dictionaly['会員情報_検証']['address']
    phone = signup_validate_dictionaly['会員情報_検証']['phone']
    gender = signup_validate_dictionaly['会員情報_検証']['gender']
    birthday = signup_validate_dictionaly['会員情報_検証']['birthday']
    check_flag = signup_validate_dictionaly['会員情報_検証']['check_flag']

    # 各表示項目の検証
    expect(my_page.email_text).to_have_text(email)
    expect(my_page.username_text).to_have_text(name)
    expect(my_page.rank_text).to_have_text(rank)
    expect(my_page.address_text).to_have_text(address)
    expect(my_page.phone_text).to_have_text(phone)
    expect(my_page.gender_text).to_have_text(gender)
    expect(my_page.birthday_text).to_have_text(birthday)
    expect(my_page.notification_text).to_have_text(check_flag) 

@then('マイページ画面でログアウトボタンを押下する')
def step_then(my_page: MyPage):
    my_page.click_logout() """






