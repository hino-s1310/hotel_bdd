from components.header import Header
from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage
from pages.plans import PlansPage
from pages.reserve import ReservePage
from pages.confirm import ConfirmPage
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers
import pytest, json

# ガーキンファイルの読み込み
scenarios('reserve_plan.feature')

@given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()

@when('ログインボタンを押下する')
def step_when(home_page: HomePage):
    home_page.click_login()

@when(parsers.parse('ログイン画面で「{login_input}」を入力しログインボタンを押下する'))
def step_when_login(login_page:LoginPage, login_input):

    # JSONを辞書に格納
    login_input_dictionaly = json.loads(login_input)
    email = login_input_dictionaly['ログイン情報_入力']['email']
    pwd = login_input_dictionaly['ログイン情報_入力']['password']

    #　ログインボタンを押下する
    login_page.submit_login(email,pwd)

@when('ページの見出しが「マイページ」であることを確認する')
def step_when(my_page:MyPage):
    expect(my_page.mypage_heading).to_contain_text("マイページ")

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
    flag_morning = reserve_input_dictionaly['予約情報_入力']['flag_morning']
    flag_noon_checkin = reserve_input_dictionaly['予約情報_入力']['flag_noon_checkin']
    flag_reasnable_sightseeing = reserve_input_dictionaly['予約情報_入力']['flag_reasnable_sightseeing']
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
