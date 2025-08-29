const openBtns = document.querySelectorAll(".openModal");
// querySelectorAllは、openModalクラスのボタンをすべて取得して
// openBtns という配列のようなリストに入れる
// querySelectorAllは指定したclassの値に一致するすべての要素を取得するためのメソッド

// モーダルの要素取得
// getElementByIdは指定したIDを持つHTML要素を取得するためのメソッド
const modal = document.getElementById("modalDelete");
const messageElement = document.getElementById("u_msg");
const deleteBtn = document.getElementById("delete");
const cancelBtn = document.getElementById("cancel");

let targetForm = null;
// このあと削除対象にするフォームを一時的に入れる変数（nullからスタート）

// モーダルを開く
openBtns.forEach((btn) => {
  // forEachはリストから1つずつ取り出して実行するforループのような処理
  //openBtnsの値が引数のbtnに入る
  btn.addEventListener("click", () => {
    targetForm = btn.closest("form");
    // 押されたボタンに最も近いフォームをtargetFormに入れる
    // closest()は直近の要素を親要素として返すメソッド
    
    // クリックされたボタンのdata-message属性からメッセージを取得
    // getAttributeは指定した要素の特定の属性の値を取得するためのメソッド
    const message = btn.getAttribute("data-message");

    // モーダルにメッセージを設定
    //textContentは要素内のテキストを簡単に取得・設定するための便利なプロパティ
    messageElement.textContent = message;

    modal.style.display = "flex";
    // モーダルを表示する
  });
});

// 削除ボタンをクリックしたとき
deleteBtn.addEventListener('click', () => {
  if (targetForm) targetForm.submit();
  modal.style.display = "none";
  // モーダルを閉じる
  targetForm = null;
  // 変数を空にする
});

// キャンセルボタンをクリックしたとき
cancelBtn.addEventListener('click', () => {
  modal.style.display = "none";
});

// モーダル外（背景）をクリックしたら閉じる
addEventListener('click', (e) => {
    // (e)は "click"というイベントの情報（イベントオブジェクト）を、addEventListenerから渡される
    // どこをクリックしたか、要素はなにか、などの情報が(e)に入る
    if (e.target === modal) {
      // クリックされた要素(e.target)が modal（半透明部分） なら閉じる
      modal.style.display = "none";
    }
});