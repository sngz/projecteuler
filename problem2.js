var x=1;
var y=2;
var fibsum = 0;
var answersum = 2;

while( y < 4000000) {
    fibsum = x+y;
    if(fibsum % 2 === 0) {
        answersum += fibsum;
    }
    x = y;
    y = fibsum;
}
console.log(answersum);