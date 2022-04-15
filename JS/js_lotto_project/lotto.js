// 클라이언트가 버튼클릭하면 로또번호 뽑기
// 로또번호 하나씩 시간차두고 나오도록.

const lotto = [];

// 사용자가 버튼 누르면 새로 뽑는 함수.
function select() {
    // lotto 배열안의 값이 6개일 때까지 반복.
    while (lotto.length < 6 ) {
        // 1~46미만의 수 랜덤 선택 ; 소수점 버리고 정수형으로 바꾸는 과정(parseInt) 통해
        var num = parseInt(Math.random() * 45 + 1)
        // 기존 배열안에 없는 값이면 배열에 추가 ; 중복제거
        if (lotto.indexOf(num) == -1) {
            // js에서 push는 python에서 append와 같다고 생각. ; 모두 리스트에 값 추가함.
            lotto.push(num);
        }
    }
    // 오름차순 정렬
    lotto.sort((a,b)=>a-b);
    // lotto에 들어간 값 나타냄.
    console.log(lotto)
    var num1 = document.querySelector('.num1')
    num1.innerHTML = lotto[0];
    var num2 = document.querySelector('.num2')
    // setTimeout으로 지연시간 뒤에 실행될 코드 설정 ; 1번 번호 뽑히고 1초간격으로 다음 번호 나타나도록.
    setTimeout(function() {num2.innerHTML = lotto[1]}, 1000);
    var num3 = document.querySelector('.num3')
    setTimeout(function() {num3.innerHTML = lotto[2]}, 2000);
    var num4 = document.querySelector('.num4')
    setTimeout(function() {num4.innerHTML = lotto[3]}, 3000);
    var num5 = document.querySelector('.num5')
    setTimeout(function() {num5.innerHTML = lotto[4]}, 4000);
    var num6 = document.querySelector('.num6')
    setTimeout(function() {num6.innerHTML = lotto[5]}, 5000);
}

var button = document.getElementById("button");
button.addEventListener("click", select);
console.log('Working');


