const textbox = document.getElementById("jasoseol");

// addEventListener로 사용자가 어떤 동작할 때마다 함수발동하도록 설계.
// 추가로 알게 된 건 addEventListener에서는 onkeydown이 아니라 keydown. ; event종류 잘 체크하기.
textbox.addEventListener("keydown", counter);

function counter() {
    // 근데 여기 innerHTML을 써버린다면? 이것은 값을 넣어줄 때 쓰는 것 같다.
    var content = document.getElementById("jasoseol").value;
    // 글자수가 200글자가 넘는다면 잘라내는 부분.
    if (content.length > 100) {
        // 200글자까지가 content 변수에 저장.
        content = content.substring(0,100)
        // html 텍스트상자부분에 200글자까지 저장된 content내용 들어감. ; 200글자 넘기면 안써짐.
        document.getElementById("jasoseol").value = content 
    }
    // js에서는 파이썬과는 달리 다른 데이터종류라 하더라도(문자, 숫자 조합도 Ok) +로 연결할 수 있음.
    // 텍스트의 길이를 넣어줌.
    document.getElementById("count").innerHTML = "(" + content.length + "/100)";
}
counter()