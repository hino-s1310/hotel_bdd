import pytest, re, json, datetime
from components.header import Header
from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage
from pages.plans import PlansPage
from pages.reserve import ReservePage
from pages.confirm import ConfirmPage
from pages.signup import SignUpPage
from pages.icon import IconPage
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, sync_playwright, expect
from distutils.util import strtobool

@pytest.fixture
def new_page():
    pytest.new_page = None

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def header(page: Page) -> Header:
    return Header(page)

@pytest.fixture
def home_page(page: Page, header: Header) -> HomePage:
    return HomePage(page, header)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def my_page(page: Page, header: Header) -> MyPage:
    return MyPage(page, header)

@pytest.fixture
def plans_page(page: Page, header:Header) -> PlansPage:
    return PlansPage(page,header)

@pytest.fixture
def reserve_page(page: Page) -> ReservePage:
    return ReservePage(page)

@pytest.fixture
def confirm_page(page: Page) -> ConfirmPage:
    return ConfirmPage(page)

@pytest.fixture
def signup_page(page: Page) -> SignUpPage:
    return SignUpPage(page)

@pytest.fixture
def icon_page(page: Page) -> IconPage:
    return IconPage(page)


@given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()

@when('ログインボタンを押下する')
def step_when_login(home_page: HomePage):
    home_page.click_login()

@when(parsers.parse('ログイン画面で「{login_input}」を入力しログインボタンを押下する'))
def step_when_login(login_page:LoginPage, login_input):

    # JSONを辞書に格納
    login_input_dictionaly = json.loads(login_input)
    email = login_input_dictionaly['ログイン情報_入力']['email']
    pwd = login_input_dictionaly['ログイン情報_入力']['password']

    #　ログインボタンを押下する
    login_page.submit_login(email,pwd)

@then(parsers.parse('ページの見出しが「{heading}」であることを確認する'))
def step_then(my_page:MyPage, heading):
    expect(my_page.mypage_heading).to_have_text(heading)

@when('ページの見出しが「マイページ」であることを確認する')
def step_when(my_page:MyPage):
    expect(my_page.mypage_heading).to_contain_text("マイページ")

@then(parsers.parse('マイページの各項目が「{login_validate}」であることを確認する'))
def step_then(my_page:MyPage, login_validate):

    # JSONを辞書に格納
    login_validate_dictionaly = json.loads(login_validate)
    email = login_validate_dictionaly['マイページ情報_検証']['email']
    name = login_validate_dictionaly['マイページ情報_検証']['name']
    rank = login_validate_dictionaly['マイページ情報_検証']['rank']

    # 各項目を検証
    expect(my_page.email_text).to_have_text(email)
    expect(my_page.username_text).to_have_text(name)
    expect(my_page.rank_text).to_have_text(rank)

@then('マイページをログアウトする')
def step_then(my_page:MyPage):
    my_page.click_logout()

@when('宿泊予約リンクを押下する')
def step_when(my_page:MyPage):
    my_page.click_reserve()

@when('ページの見出しが「宿泊プラン一覧」であることを確認する')
def step_when(plans_page:PlansPage):
    expect(plans_page.plans_heading).to_contain_text("宿泊プラン一覧")

@when(parsers.parse("「{plan_name}」カードのこのプランで予約ボタンを押下する"))
def step_when(plans_page:PlansPage, plan_name):
    
    # ページハンドリング
    with plans_page.page.context.expect_page() as new_page_info:
        plans_page.click_this_reserve(plan_name),
    pytest.new_page = new_page_info.value
    plans_page.page.on("new_page", handle_page)

@when('ページの見出しが「宿泊予約」であることを確認する')
def step_when(reserve_page:ReservePage):
    reserve_page = ReservePage(pytest.new_page)
    expect(reserve_page.reserve_heading).to_contain_text("宿泊予約")

@when(parsers.parse('宿泊予約画面で「{reserve_input}」を入力する'))
def step_when(reserve_page:ReservePage, reserve_input):
    # ページインスタンスの引き継ぎ
    reserve_page = ReservePage(pytest.new_page)

    # JSONを辞書に格納
    reserve_input_dictionaly = json.loads(reserve_input)
    stay_num = reserve_input_dictionaly['予約情報_入力']['stay_num']
    people_num = reserve_input_dictionaly['予約情報_入力']['people_num']
    flag_morning = strtobool(reserve_input_dictionaly['予約情報_入力']['flag_morning'])
    flag_noon_checkin = strtobool(reserve_input_dictionaly['予約情報_入力']['flag_noon_checkin'])
    flag_reasnable_sightseeing = strtobool(reserve_input_dictionaly['予約情報_入力']['flag_reasnable_sightseeing'])
    reserve_contact = reserve_input_dictionaly['予約情報_入力']['reserve_contact']

    # 各項目を入力する
    reserve_page.click_tomorrow()
    reserve_page.fill_term(stay_num)
    reserve_page.fill_head_count(people_num)
    reserve_page.controll_mvc_checkbox(flag_morning)
    reserve_page.controll_ncc_checkbox(flag_noon_checkin)
    reserve_page.controll_rsc_checkbox(flag_reasnable_sightseeing)
    reserve_page.select_contact(reserve_contact)

@when(parsers.parse('合計欄が「{reserve_total_bill}」であることを確認する'))
def step_when(reserve_page:ReservePage, reserve_total_bill):
    # ページインスタンスの引き継ぎ  
    reserve_page = ReservePage(pytest.new_page)

    #　土日料金か判定し、金額検証
    reserve_total_bill = calc_holiday_price(reserve_total_bill)
    expect(reserve_page.total_bill).to_contain_text(reserve_total_bill)

@when(parsers.parse('予約内容を確認するボタンを押下する'))
def step_when(reserve_page:ReservePage):
    # ページインスタンスの引き継ぎ
    reserve_page = ReservePage(pytest.new_page)

    reserve_page.click_confirm_reserve_button()

@then(parsers.parse('ページの見出しが「宿泊予約確認」であることを確認する'))
def step_then(confirm_page:ConfirmPage):
    # ページインスタンスの引き継ぎ
    confirm_page = ConfirmPage(pytest.new_page)

    expect(confirm_page.confirm_heading).to_contain_text("宿泊予約確認")

@then(parsers.parse('宿泊予約画面の各項目が「{confirm_validate}」であることを確認する'))
def step_then(confirm_page:ConfirmPage, confirm_validate):
    # ページインスタンスの引き継ぎ
    confirm_page = ConfirmPage(pytest.new_page)

    # JSONを辞書に格納
    confirm_validate_dictionaly = json.loads(confirm_validate)
    confirm_total_bill = confirm_validate_dictionaly['予約確認情報_検証']['confirm_total_bill']
    reserve_plan_name = confirm_validate_dictionaly['予約確認情報_検証']['reserve_plan_name']
    stay_num = confirm_validate_dictionaly['予約確認情報_検証']['stay_num']
    additional_plan = confirm_validate_dictionaly['予約確認情報_検証']['additional_plan']
    name = confirm_validate_dictionaly['予約確認情報_検証']['name']
    people_num = confirm_validate_dictionaly['予約確認情報_検証']['people_num']
    confirm_contact = confirm_validate_dictionaly['予約確認情報_検証']['confirm_contact']
    comment = confirm_validate_dictionaly['予約確認情報_検証']['comment']

    # 各項目の検証
    confirm_total_bill = calc_holiday_price(confirm_total_bill)
    expect(confirm_page.total_bill).to_contain_text(confirm_total_bill)
    expect(confirm_page.plan_name).to_have_text(reserve_plan_name)

    stay_term = confirm_page.calc_term(stay_num)
    expect(confirm_page.term).to_have_text(stay_term)
    
    expect(confirm_page.plans).to_have_text(additional_plan)

    validate_name = name + "様"
    expect(confirm_page.username).to_have_text(validate_name)

    expect(confirm_page.contact).to_have_text(confirm_contact)
    expect(confirm_page.comment).to_have_text(comment)

@then('この内容で予約するボタンを押下する')
def step_then(confirm_page:ConfirmPage):
    confirm_page = ConfirmPage(pytest.new_page)
    confirm_page.click_confirm()

@then('ページの見出しが「宿泊プラン一覧」であることを確認する')
def step_then(plans_page:PlansPage):
    expect(plans_page.plans_heading).to_have_text("宿泊プラン一覧")

def handle_page(page):
    page.wait_for_load_state()
    print(page.title())

def calc_holiday_price(price) -> str:

    today = datetime.datetime.now()
    tomorrow = today  + datetime.timedelta(days= 1)
    # 翌日の曜日を取得し、土日かどうか判定
    if tomorrow.weekday() >= 5:
        # 料金を1.25倍にする
        return str(int(price) * 1.25)
    else:
        return price
    
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
    my_page.click_logout()

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

@when(parsers.parse('退会するボタンを押下'))
def step_when(my_page: MyPage):
    my_page.withdraw_member()

@then(parsers.parse('タイトルに「HOTEL PLANISPHERE」が含まれていることを確認'))
def step_then(home_page: HomePage):
    expect(home_page.page).to_have_title(re.compile("HOTEL PLANISPHERE"))