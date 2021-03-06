
  // global variables that will be loaded/initialized later
  let canvas, ctx, gravity, ball, friction, p1, p2, key, aniFrame

  // runs once at the beginning
  // loads any data and kickstarts the loop

  function draw_rect(x,y,w,h,color){
      ctx.fillStyle = color
      ctx.fillRect(x,y,w,h)
      ctx.fill()
  }

  function draw_ball(){
    ctx.beginPath()
    ctx.fillStyle = 'white'
    ctx.arc(
      ball.x, ball.y,
      ball.radius,
      0, Math.PI * 2
    )
    ctx.fill()
  }

  function init () {
    // *load data here*
    // our canvas variables
    canvas = document.getElementById('gameCanvas')
    ctx = canvas.getContext('2d')

    // set the canvas size
    canvas.width = 900
    canvas.height = 500

    // world/scene settings
    friction = 0.995

    // starting objects
    key = {
    'w':false,
    's':false,
    'u':false,
    'd':false,
    }  //For the sake of taking in multiple key inputs at the same time

    ball = {
      bounce: 1.01, // energy lost on bounce (25%)
      radius: 15,
      x: canvas.width / 2,
      y: canvas.height / 2,
      velX: (Math.random() * 2 + 2) * (Math.floor(Math.random() * 2) || -1),
      velY: (Math.random() * 2 + 2) * (Math.floor(Math.random() * 2) || -1)
    }

    p1 = {
        x:10,
        y:100,
        w:20,
        h:100,
    }

    p2 = {
        x:870,
        y:100,
        w:20,
        h:100,
    }
    let left = $('#gameCanvas').offset().left
    $('#p1').css({'left':`${canvas.width/2 + left - 100}px`})
    $('#p2').css({'left':`${canvas.width/2 + left + 75}px`})

    // begin update loop
  }

  // draws stuff to the screen
  // allows us to separate calculations and drawing
  function draw () {
    // clear the canvas and redraw everything
    draw_rect(0,0,canvas.width, canvas.height,'black')

    for (let i = 0; i < 13; i++){
      draw_rect(canvas.width/2,i*40,10,30,'white')
    }

    draw_rect(p1.x,p1.y,p1.w,p1.h,'white')
    draw_rect(p2.x,p2.y,p2.w,p2.h,'white')

    draw_ball()

  }

  function game_over(winner){
    let score = $(`#${winner}`).text() 
    score = parseInt(score)
    $(`#${winner}`).text(score + 1)
    window.cancelAnimationFrame(aniFrame)
    init()

  }

  // the main piece of the loop
  // runs everything
  function update () {
    // queue the next update
    aniFrame = window.requestAnimationFrame(update)

    // bottom bound / floor
    if (ball.y + ball.radius >= canvas.height) {
      ball.velY *= -ball.bounce    // To increase speed after every bounce
      ball.y = canvas.height - ball.radius
      ball.velX *= friction
    }
    // top bound / ceiling
    if (ball.y - ball.radius <= 0) {
      ball.velY *= -ball.bounce
      ball.y = ball.radius
      ball.velX *= friction
    }

    // left bound
    if (ball.x - ball.radius <= p1.w + p1.x) {
      if (ball.y  > p1.y && ball.y< p1.y + p1.h){
        ball.velX *= -ball.bounce
        ball.x = (p1.w + p1.x) + ball.radius
      }
      else{
        game_over('p2')
      }
    }
    // right bound
    if (ball.x + ball.radius >= p2.x) {
      if (ball.y  > p2.y && ball.y< p2.y + p2.h){
        ball.velX *= -ball.bounce
      ball.x = p2.x - ball.radius
      }
      else{
        game_over('p1')
      }
    }

    // reset insignificant amounts to 0
    if (ball.velX < 0.01 && ball.velX > -0.01) {
      ball.velX = 0
    }
    if (ball.velY < 0.01 && ball.velY > -0.01) {
      ball.velY = 0
    }

    // update ball position
    ball.x += ball.velX
    ball.y += ball.velY

    // draw after logic/calculations
    draw()
  }

  // start our code once the page has loaded

  $(document).keydown(function (e){
    switch(e.key){
      case 'l':
        window.cancelAnimationFrame(aniFrame)
        // window.cancelAnimationFrame(aniFrame)
        break
      case 'Enter':
        window.requestAnimationFrame(update)
        // window.requestAnimationFrame(update)
        break
      case 'ArrowUp':
        key.u = true
        break
      case 'ArrowDown':
        key.d = true
        break
      case 'w':
        key.w = true
        break 
      case 's':
        key.s = true
        break
    }

    
    if (key.s){
        if (p1.y + p1.h <= canvas.height - 10){
            p1.y += 25
        }
    }
    if (key.w){
        if (p1.y + p1.h >= $('#gameCanvas').offset().top + 20){
            p1.y -= 25
        }
    }
    if (key.d){
        if (p2.y + p2.h <= canvas.height - 10){
            p2.y += 25
        }
    }
    if (key.u){
        if (p2.y + p2.h >= $('#gameCanvas').offset().top + 20){
            p2.y -= 25
        }
    }     
  })

  $(document).keyup(function(e){

  if (e.key == 'w'){
      key.w = false
  }
  if (e.key == 's'){
      key.s = false
  }
  if (e.which == 38){
      key.u = false
  }
  if (e.which == 40){
      key.d = false
  }
})

document.addEventListener('DOMContentLoaded', init)
document.addEventListener('DOMContentLoaded', draw)