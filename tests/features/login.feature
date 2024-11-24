Feature: HOTEL_PLANISPHEREログイン

  Scenario Outline: login
    Given HOTELPLANISPHEREのホームページにアクセスする
    When ログインボタンを押下する
    And ログイン画面で「<login_input>」を入力しログインボタンを押下する
    Then ページの見出しが「マイページ」であることを確認する
    And マイページ画面で各項目が「<mypage_validate>」であることを確認する
    And マイページ画面でログアウトボタンを押下する

    Examples:
    | login_input | mypage_validate |  
    | {"ログイン情報_入力": {"email": "ichiro@example.com", "password": "password"}} | {"マイページ情報_検証":{"email": "ichiro@example.com" ,"name": "山田一郎" ,"rank": "プレミアム会員", "address":"東京都豊島区池袋", "phone":"01234567891", "gender":"男性", "birthday":"未登録", "check_flag":"受け取る"}} | 
    | {"ログイン情報_入力": {"email": "sakura@example.com", "password": "pass1234"}} | {"マイページ情報_検証":{"email": "sakura@example.com" ,"name": "松本さくら" ,"rank": "一般会員","address":"神奈川県横浜市鶴見区大黒ふ頭", "phone":"未登録", "gender":"女性", "birthday":"2000年4月1日","check_flag":"受け取らない"}} | 
    | {"ログイン情報_入力": {"email": "jun@example.com", "password": "pa55w0rd!"}} | {"マイページ情報_検証":{"email": "jun@example.com" ,"name": "林潤" ,"rank": "プレミアム会員","address":"大阪府大阪市北区梅田", "phone":"01212341234", "gender":"その他", "birthday":"1988年12月17日","check_flag":"受け取らない"}} | 
    | {"ログイン情報_入力": {"email": " yoshiki@example.com", "password": "pass-pass"}} | {"マイページ情報_検証":{"email": " yoshiki@example.com" ,"name": "木村良樹" ,"rank": "一般会員","address":"未登録", "phone":"01298765432", "gender":"未登録", "birthday":"1992年8月31日","check_flag":"受け取る"}} | 