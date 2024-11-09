Feature: 既存会員でログインし、プランの予約を行う

  Scenario Outline: reserve_plan
    Given HOTELPLANISPHEREのホームページにアクセスする
    When ログインボタンを押下する
    And email、パスワード欄に「<email>」、「<password>」と入力しログインボタンを押下する
    And ページの見出しが「マイページ」であることを確認する
    And 宿泊予約リンクを押下する
    And ページの見出しが「宿泊プラン一覧」であることを確認する
    And 「<plan_name>」カードのこのプランで予約ボタンを押下する
    And ページの見出しが「宿泊予約」であることを確認する
    And 宿泊日欄に今日の日付を入力する
    And 宿泊数欄に「<stay_num>」を入力する
    And 人数欄に「<people_num>」を入力する
    And 朝食プランのチェックボックスを「<flag_morning>」にする
    And 昼からチェックインプランのチェックボックスを「<flag_noon_checkin>」にする
    And お得な観光プランのチェックボックスを「<flag_reasnable_sightseeing>」にする
    And 確認のご連絡リストを「<confirm_contact>」に選択する
    And 合計欄が「<total_bill>」であることを確認する
    And 予約内容を確認するボタンを押下する
    Then ページの見出しが「宿泊予約確認」であることを確認する
    And 合計金額が「<total_bill>」であることを確認する
    And プラン名が「<plan_name>」であることを確認する
    And 期間が 今日から「<stay_num>」を足した日までであることを確認する
    And 追加プランが「<additional_plan>」であることを確認する
    And お名前が「<name>」であることを確認する
    And 確認のご連絡が「<confirm_contact>」であることを確認する
    And ご要望・ご連絡事項等が「<comment>」であることを確認する
    And この内容で予約するボタンを押下する
    And ページの見出しが「宿泊予約確認」であることを確認する


    Examples:
    | name | email | password | plan_name | stay_num | people_num | flag_morning | flag_noon_checkin | flag_reasnable_sightseeing | confirm_contact | total_bill | additional_plan | comment |
    | 山田一郎 | ichiro@example.com | password | おすすめプラン | 1 | 1 | False | False | False | 希望しない | 8,750 | なし | なし |