
const openBtns = document.querySelectorAll(".openModal");
// querySelectorAllは、openModalクラスのボタンをすべて取得して
// openBtns という配列のようなリストに入れる
const modal = document.getElementById("modalDelete");
const deleteBtn = document.getElementById("delete");
const cancelBtn = document.getElementById("cancel");

let targetForm = null;
// このあと削除対象にするフォームを一時的に入れる変数（nullからスタート）

// モーダルを開く
openBtns.forEach((btn) => {
  // forEachはリストから1つずつ取り出して実行するforループのような処理
  btn.addEventListener("click", () => {
    targetForm = btn.closest("form");
    // 押されたボタンに最も近いフォームをtargetFormに入れる
    // closest()は直近の要素を親要素として返すメソッド
    modal.style.display = "flex";
    // モーダルを表示する
  });
});

// 削除ボタンをクリックしたとき
deleteBtn.addEventListener('click', () => {
  targetForm.submit();
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