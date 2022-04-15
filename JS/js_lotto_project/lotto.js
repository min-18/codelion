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

    // if문으로 배열안에 6개 숫자까지 넣을 수 있기 때문에 버튼 누를때마다 반복해서 새로 뽑으려면 배열을 비우는 작업이 필요.
    // 근데 그냥 비우면 번호가 표시되기도 전에 비워지기 때문에 번호가 다 뜨고난 후 함수가 동작하도록 해야한다.
    // 시간지연을 활용하거나 콜백함수 쓰면되겠다 판단.
    // 근데 시간지연setTimeout을 쓰면 사용자가 반복해서 클릭했을 때 오류가 뜬다... 물론 번호가 다 뜨고난 후 새로뽑기 버튼을 누르는 것이 이상적이지만.
    setTimeout(function() {lotto.length = 0}, 5000)
    console.log(lotto)

}

var button = document.getElementById("button");
button.addEventListener("click", select);

console.log('Working');


