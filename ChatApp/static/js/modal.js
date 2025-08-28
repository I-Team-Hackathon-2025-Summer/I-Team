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
openModal.addEventListener('click', () => {
  modal.showModal();   //モーダルを表示
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