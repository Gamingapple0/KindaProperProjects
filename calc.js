$(document).ready(function() {
    var re = $("#resu").text(); 
    if(re == "") {
        $('#resu').addClass('res1')
        $('#resu').removeClass('res2')
    }
});
var result, num1
$('.op').click(function(){
    var clicked = $(this).text()
    num1 = parseFloat($('input').val())
    //Repeat this process
    if (clicked == '+'){
        $('input').val('')
        key ='p'
    }
    else if (clicked == '-'){
        $('input').val('')
        key ='s'
    }
    else if (clicked == '/'){
        $('input').val('')
        key ='d'
    }
    else if (clicked == 'x'){
        $('input').val('')
        key ='m'
    }
    else if (clicked == '='){
        $('#resu').text('')
        $('input').val('')
        $('#resu').addClass('res1')
        $('#resu').removeClass('res2')
        $('#fin').text(result)
        result = undefined
        key = undefined
    }
})
$('.num').click(function (){
    var og = $('input').val()
    var clicked = $(this).text()
    no2 = og + clicked
    if (num1 != undefined){
        if (key != undefined){
            $('#resu').addClass('res2')
            $('#resu').removeClass('res1')
        // Main Shit
        if (key == 'p')  {
            if (result == undefined || no2.length > 1){
                result = num1 + parseFloat(no2)
                $('#resu').text(result)
            }
            else{
                result += parseFloat(no2)
                $('#resu').text(result)
            }
        }
        else if (key == 's')  {
            if (result == undefined || no2.length > 1){
                result = num1 - parseFloat(no2)
                $('#resu').text(result)
            }
            else{
                result -= parseFloat(no2)
                $('#resu').text(result)
            }
        }
        else if (key == 'd')  {
            if (result == undefined || no2.length > 1){
                result = num1 / parseFloat(no2)
                $('#resu').text(result)
            }
            else{
                result /= parseFloat(no2)
                $('#resu').text(result)
            }
        }
        else if (key == 'm')  {
            if (result == undefined || no2.length > 1){
                result = num1 * parseFloat(no2)
                $('#resu').text(result)
            }
            else{
                result *= parseFloat(no2)
                $('#resu').text(result)
            }
        }
        }
        
    }

    $('input').val(og + clicked)
    if (result == 69){
        $('#resu').text('Nice!')
    }
    else if (result == 420){
        $('#resu').text('Smoke Weed Everydayy!')
    }
})
$('.other').click(function(){
    var clicked = $(this).text()
    var inp = $('input').val()
    if (clicked =='AC'){
        $('input').val('')
        $('#resu').text('')
        $('#fin').text('')
        $('#resu').addClass('res1')
        $('#resu').removeClass('res2')
        result = undefined
        key = undefined
    }
    else if (clicked == 'X'){
        out = inp.slice(0,-1)
        $('input').val(out)
        var og = $('input').val()
    var clicked = ''
    no2 = og + clicked
    if (num1 != undefined){
        if (key != undefined){
            $('#resu').addClass('res2')
        $('#resu').removeClass('res1')
        // Main Shit
        if (key == 'p')  {
            if (result == undefined || no2.length > 1){
                result = num1 + parseFloat(no2)
                $('#resu').text(result)
            }
            else{
                result += parseFloat(no2)
                $('#resu').text(result)
            }
        }
        else if (key == 's')  {
            if (result == undefined || no2.length > 1){
                result = num1 - parseFloat(no2)
                $('#resu').text(result)
            }
            else{
                result -= parseFloat(no2)
                $('#resu').text(result)
            }
        }
        else if (key == 'd')  {
            if (result == undefined || no2.length > 1){
                result = num1 / parseFloat(no2)
                $('#resu').text(result)
            }
            else{
                result /= parseFloat(no2)
                $('#resu').text(result)
            }
        }
        else if (key == 'm')  {
            if (result == undefined || no2.length > 1){
                result = num1 * parseFloat(no2)
                $('#resu').text(result)
            }
            else{
                result *= parseFloat(no2)
                $('#resu').text(result)
            }
        }
        }
        
    }

    $('input').val(og + clicked)
    }
})
