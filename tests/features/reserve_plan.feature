Feature: 既存会員でログインし、プランの予約を行う

  Scenario Outline: reserve_plan
    Given HOTELPLANISPHEREのホームページにアクセスする
    When ログインボタンを押下する
    And ログイン画面で「<login_input>」を入力しログインボタンを押下する
    And ページの見出しが「マイページ」であることを確認する
    And 宿泊予約リンクを押下する
    And ページの見出しが「宿泊プラン一覧」であることを確認する
    And 「<plan_name>」カードのこのプランで予約ボタンを押下する
    And ページの見出しが「宿泊予約」であることを確認する
    And 宿泊予約画面で「<reserve_input>」を入力する
    And 各項目が「<reserve_validate>」であることを確認する
    And 予約内容を確認するボタンを押下する
    Then ページの見出しが「宿泊予約確認」であることを確認する
    And 宿泊予約画面の各項目が「<confirm_validate>」であることを確認する
    And この内容で予約するボタンを押下する
    And ページの見出しが「宿泊プラン一覧」であることを確認する


    Examples:
    | login_input | plan_name | reserve_input | reserve_validate | confirm_validate |
    | {"ログイン情報_入力": {"email": "ichiro@example.com", "password": "password"}} | お得な特典付きプラン | {"予約情報_入力": {"stay_num":"1", "people_num":"1", "flag_morning": "False", "flag_noon_checkin": "False", "flag_reasnable_sightseeing": "False", "reserve_contact":"希望しない"}} | {"予約情報_検証": {"total_bill_weekday": "7,000", "total_bill_holiday": "8,750"}}  | {"予約確認情報_検証":{"total_bill_weekday":"7,000", "total_bill_holiday": "8,750", "reserve_plan_name":"お得な特典付きプラン" ,"stay_num":"1" ,"additional_plan":"なし" ,"name":"山田一郎" ,"people_num":"1" , "confirm_contact":"希望しない","comment":"なし"}} |