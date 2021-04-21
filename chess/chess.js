// Generates board with unique id for each square

var alphabets_count = 1
const board = $('.board')
var alphabets_count = 0
const alphabets = ['#','a','b','c','d','e','f','g','h']
const colors = ['w','b']
var square_number = 8
for (var j = 0; j < 4; j ++){
    for (var i = 0; i < 4; i++){
        alphabets_count ++
        board.append('<div class="green_square" id="' + alphabets[alphabets_count] +  square_number + '"></div>')
        alphabets_count ++
        board.append('<div class="white_square" id="' + alphabets[alphabets_count] +  square_number  + '"></div>')
    }
    board.append(`<div class="number-notations">${square_number}</div>`)
    square_number --
    if (alphabets_count >= 8) {alphabets_count = 0}
    for (var a = 0; a < 4; a++){
        alphabets_count ++
        board.append('<div class="white_square" id="' + alphabets[alphabets_count] +  square_number  + '"></div>')
        alphabets_count ++
        board.append('<div class="green_square" id="' + alphabets[alphabets_count] +  square_number  + '"></div>')
    }
    board.append(`<div class="number-notations">${square_number}</div>`)
    if (alphabets_count >= 8) {alphabets_count = 0}
    square_number --
}
for (let i = 1; i <= 8; i++){
    board.append(`<div class="alphabet-notations">${alphabets[i]}</div>`)
}

//Executes show function at drag end 
var og;
$( function() {
    $( ".piece" ).draggable(
        {start: function(event, ui) {og = ui}}, // Passes the original position to og
        {stop: function(event, ui) {show($(this).attr('id'),$(this),og)
    } }
        )
})                                            

var is_colliding = function( $div1, $div2 ) {

    var d1_offset             = $div1.offset();
    var d1_height             = $div1.outerHeight( true )-23;
    var d1_width              = $div1.outerWidth( true )-23;
    var d1_distance_from_top  = d1_offset.top-23 + d1_height;
    var d1_distance_from_left = d1_offset.left-23+ d1_width;

    var d2_offset             = $div2.offset();
    var d2_height             = $div2.outerHeight( true )-23;
    var d2_width              = $div2.outerWidth( true )-23;
    var d2_distance_from_top  = d2_offset.top + d2_height-23;
    var d2_distance_from_left = d2_offset.left + d2_width-23;
    
    if ($($div1).attr('id') == $($div2).attr('id')) {return false}

    var not_colliding = ( d1_distance_from_top < d2_offset.top || d1_offset.top > d2_distance_from_top || d1_distance_from_left < d2_offset.left || d1_offset.left > d2_distance_from_left );

    // Return whether it IS colliding

    return  ! not_colliding;
};

function show(id, div, og_pos){
    if (id[0] == 'w'){
            var opp = $(`.black`)
            var sem = $(`.white`)
        }
        else {
            var opp = $('.white')
            var sem = $(`.black`)
        }

    // Pawn Promotion

    if (id[1] == 'P' && id[0] == 'w'){
        if (div.offset().top < 30){
            $(div).html('<img src="../chess/media/Chess_qlt60.png" alt="P">')
        }
    }
    else if (id[1] == 'P' && id[0] == 'b'){
        if (div.offset().top  > 500){
            $(div).html('<img src="../chess/media/Chess_qdt60.png" alt="P">')
        }
    }

    // Checks piece collision

        for (let i = 0; i < opp.length; i++){
            var colided_opp = is_colliding($(div), $(opp[i]))
            var colided_sem = is_colliding($(div),$(sem[i]))
            if (colided_sem){
                $(div).css({position:'absolute', top: og_pos.offset.top, left: og_pos.offset.left, width: '76px'})
            }
            else if (colided_opp){
                $(opp[i]).css({display: 'none'})
                break
            }

        }
}

// Piece classes

class Piece{
    constructor(color, position_x, position_y){
        this.color = color
        this.position_x = position_x
        this.position_y = position_y
}
    init(role, img=''){
        if (this.color == 'w'){
            var col = 'white'
        }
        else {
            var col = 'black'
        }
        $(`#${this.position_x}${this.position_y}`).append(`<div class="${col} piece ui-widget-content" id="${this.color}${role}${this.position_x}">${img}</div>`)
    }
}
class Pawn extends Piece{
    constructor(color,x,y){
        super(color,x,y)
        this.role = 'P'
        if (this.color == 'w'){this.img = '<img src="../chess/media/Chess_plt60.png" alt="P">'}
        else {this.img = '<img src="../chess/media/Chess_pdt60.png" alt="P">'}
        
        this.init(this.role, this.img)
        
    }
}
class King extends Piece{
    constructor(color,x,y){
        super(color,x,y)
        this.role = 'K'
        if (this.color == 'w'){this.img = '<img src="../chess/media/Chess_klt60.png" alt="K">'}
        else {this.img = '<img src="../chess/media/Chess_kdt60.png" alt="K">'}
        
        this.init(this.role, this.img)
    }
}
class Queen extends Piece{
    constructor(color,x,y){
        super(color,x,y)
        this.role = 'Q'
        if (this.color == 'w'){this.img = '<img src="../chess/media/Chess_qlt60.png" alt="Q">'}
        else {this.img = '<img src="../chess/media/Chess_qdt60.png" alt="Q">'}
        
        this.init(this.role, this.img)
    }
}
class Pope extends Piece{
    constructor(color,x,y){
        super(color,x,y)
        this.role = 'B'
        if (this.color == 'w'){this.img = '<img src="../chess/media/Chess_blt60.png" alt="B">'}
        else {this.img = '<img src="../chess/media/Chess_bdt60.png" alt="B">'}
        
        this.init(this.role, this.img)
    }
}
class Horsie extends Piece{
    constructor(color,x,y){
        super(color,x,y)
        this.role = 'H'
        if (this.color == 'w'){this.img = '<img src="../chess/media/Chess_nlt60.png" alt="H">'}
        else {this.img = '<img src="../chess/media/Chess_ndt60.png" alt="H">'}
        
        this.init(this.role, this.img)
    }
}
class Rock extends Piece{
    constructor(color,x,y){
        super(color,x,y)
        this.role = 'R'
        if (this.color == 'w'){this.img = '<img src="../chess/media/Chess_rlt60.png" alt="R">'}
        else {this.img = '<img src="../chess/media/Chess_rdt60.png" alt="R">'}
        
        this.init(this.role, this.img)
    }
}

// Creates instances for all the pieces

for(let i = 1; i <= 8; i++){
    window['pawn_w'+i] = new Pawn('w',alphabets[i],2); 
    window['pawn_b'+i] = new Pawn('b',alphabets[i],7); 
}
let pos = 1
for(let i = 0; i <= 1; i++){
    window['king'+'_'+colors[i]] = new King(colors[i],'e',pos); 
    window['queen'+'_'+colors[i]] = new Queen(colors[i],'d',pos); 
    pos += 7
}
let bruh = 1
for(let i = 0; i <= 1; i++){
    if (bruh > 1){
        window['pope_w'+(i+1)] = new Pope('w',alphabets[bruh-2],1); 
        window['horsie_w'+(i+1)] = new Horsie('w',alphabets[bruh-1],1); 
        window['rock_w'+(i+1)] = new Rock('w',alphabets[bruh],1); 
    }else{
        window['pope_w'+(i+1)] = new Pope('w',alphabets[bruh+2],1); 
        window['horsie_w'+(i+1)] = new Horsie('w',alphabets[bruh+1],1); 
        window['rock_w'+(i+1)] = new Rock('w',alphabets[bruh],1); 
    }
    bruh += 7
}
bruh = 1
for(let i = 0; i <= 1; i++){
    if (bruh > 1){
        window['pope_b'+(i+1)] = new Pope('b',alphabets[bruh-2],8); 
        window['horsie_b'+(i+1)] = new Horsie('b',alphabets[bruh-1],8); 
        window['rock_b'+(i+1)] = new Rock('b',alphabets[bruh],8); 
    }else{
        window['pope_b'+(i+1)] = new Pope('b',alphabets[bruh+2],8); 
        window['horsie_b'+(i+1)] = new Horsie('b',alphabets[bruh+1],8); 
        window['rock_b'+(i+1)] = new Rock('b',alphabets[bruh],8); 
    }
    bruh += 7
}