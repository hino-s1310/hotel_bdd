Feature: HOTEL_PLANISPHEREログイン

  Scenario Outline: login
    Given HOTELPLANISPHEREのホームページにアクセスする
    When ログインボタンを押下する
    And ログイン画面で「<login_input>」を入力しログインボタンを押下する
    Then ページの見出しが「マイページ」であることを確認する
    And マイページの各項目が「<login_validate>」であることを確認する
    And マイページをログアウトする

    Examples:
    | login_input | login_validate |  
    | {"ログイン情報": {"email": "ichiro@example.com", "password": "password"}} | {"マイページ情報":{"email": "ichiro@example.com" ,"name": "山田一郎" ,"rank": "プレミアム会員"}} | 
    | {"ログイン情報": {"email": "sakura@example.com", "password": "pass1234"}} | {"マイページ情報":{"email": "sakura@example.com" ,"name": "松本さくら" ,"rank": "一般会員"}} | 
    | {"ログイン情報": {"email": "jun@example.com", "password": "pa55w0rd!"}} | {"マイページ情報":{"email": "jun@example.com" ,"name": "林潤" ,"rank": "プレミアム会員"}} | 
    | {"ログイン情報": {"email": " yoshiki@example.com", "password": "pass-pass"}} | {"マイページ情報":{"email": " yoshiki@example.com" ,"name": "木村良樹" ,"rank": "一般会員"}} | 