from pages.home import HomePage
from pages.signup import SignUpPage
from pages.mypage import MyPage
from pages.icon import IconPage
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers
import datetime, json

# ガーキンファイルの読み込み
scenarios('set_icon.feature')

# conftestに移管
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

@when('ページの見出しが「マイページ」であることを確認する')
def step_when(my_page: MyPage):
    expect(my_page.mypage_heading).to_contain_text("マイページ")

@when('アイコン設定ボタンを押下する')
def step_when(my_page: MyPage):
    my_page.click_set_icon()

@when('ページの見出しが「アイコン設定」であることを確認する')
def step_when(icon_page: IconPage):
    expect(icon_page.iconpage_heading).to_contain_text("アイコン設定")

@when(parsers.parse('アイコン画面で「{icon_input}」を入力する'))
def step_when(icon_page: IconPage, icon_input):
    #JSONを辞書に読み込み
    icon_page_dictionaly = json.loads(icon_input)
    img_path = icon_page_dictionaly['アイコン情報_入力']['img_path']
    slider_value = icon_page_dictionaly['アイコン情報_入力']['slider_value']
    RGB_value = icon_page_dictionaly['アイコン情報_入力']['RGB_value']

    # 各項目の入力
    icon_page.upload_img(img_path)
    icon_page.set_scaling(slider_value)
    icon_page.fill_color(RGB_value)

@when('確定ボタンを押下する')
def step_when(icon_page: IconPage):
    icon_page.click_confirm()

@then('ページの見出しが「マイページ」であることを確認する')
def step_then(my_page: MyPage):
    expect(my_page.mypage_heading).to_contain_text("マイページ")

@then('アイコンが存在することを確認する')
def step_then(my_page: MyPage):
    expect(my_page.icon).to_be_visible()

@then(parsers.parse('アイコンの枠の色が「{validate_RGB_value}」であることを確認する'))
def step_then(my_page: MyPage, validate_RGB_value):
    expect(my_page.icon).to_have_css("background-color", validate_RGB_value)

@then(parsers.parse('アイコンのスクリーンショットを撮影し、「{screenshot_path}」に格納する'))
def step_then(my_page: MyPage, screenshot_path):
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    my_page.icon.screenshot(path=screenshot_path + now + "_icon_screenshot.png")

@then('マイページをログアウトする')
def step_then(my_page:MyPage):
    my_page.click_logout() """







