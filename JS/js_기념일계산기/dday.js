// 현재시간 객체 생성; 빈상태로 두면 현재시간으로 계산.
var now = new Date();
// 사귄날시간 객체 생성
var start = new Date('2020-05-16');
// 현재와 시작한 날의 두 시간차 담긴 객체 생성 ; getTime()메서드는 주로 시간차를 구할 때 주로 사용한다.
var timeDiff = now.getTime() - start.getTime();
// 그 시간차(ms)를 일수로 변환하고 객체에 담기.
// floor()메서드는 정수형으로 바꿔줌.
var day = Math.floor(timeDiff / (1000 * 60 * 60 * 24) + 1);
console.log(day)
// jquery이용하여 html 변경
// $('#love').text('사귄지 ' + day + "일째");

// jquery대신 순수js로 html변경하는 방식. ; 노마드 선생님은 이걸 더 선호.
var loveDay = document.getElementById("love");
// innerHTML을 통해 내부 텍스트 바꾸기.
loveDay.innerHTML = '사귄지 ' + day + "일째";

// 어린이날까지 남은 날 구하기
// 어린이날 객체 생성
var childDay = new Date('2022-05-05');
// 오늘부터 어린이날까지 시간차 담긴 객체 생성 
var timeDiff2 = childDay.getTime() - now.getTime();
// 시간차를 일수로 바꾸는 객체 생성
var day2 = Math.floor(timeDiff2 / (1000 * 60 * 60 * 24));
console.log(day2)
// jquery로 html 디데이 조정
// $('#child_day').text(day2 + '일 남음.')

// 순수js로 html변경하는 방식.
var childDay = document.getElementById('child_day')
childDay.innerHTML = day2 + '일 남음.';

// 1000일이 언제인지 구하기
// 1000일째 되는 날 ms 담긴 객체 생성
var thousandms = start.getTime() + 999 * (1000 * 60 * 60 * 24);
// 1000일 되는 날이 담긴 객체 생성
var thousandDay = new Date(thousandms);
// 위의 객체에서 1000일이 되는 날의 연,월,일 정보 얻어 객체 생성.
var thousandDate = thousandDay.getFullYear() + "." + (thousandDay.getMonth()+1) + "." + thousandDay.getDay();
// jquery이용하여 html 변경
// $('#thousand-date').text(thousandDate);

// 순수js로 html변경하는 방식.
var thousandInfo = document.getElementById('thousand-date');
thousandInfo.innerHTML = thousandDate;

// 1000일 디데이 구하기
// 1000일과 오늘 시간차 구하는 객체 생성.
var timeDiff3 = thousandms - now.getTime();
// 시간차를 일로 변환하는 객체 생성.
var day3 = Math.floor(timeDiff3 / ((1000 * 60 * 60 * 24) + 1));

// jquery이용하여 html 변경
// $('#thousand').text(day3 + '일 남음.')

// 순수js로 html변경하는 방식.
var thousandDday = document.getElementById('thousand');
thousandDday.innerHTML = day3 + '일 남음.';