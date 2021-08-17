const board = document.querySelector('chess-board');

const moves = ["d2-d4", "d7-d5", "d1-d3", "h7-h5", "b1-c3", "c8-g4", "f2-f3", "f7-f5", "c1-g5", "g8-h6", "f3-g4", "h5-g4", "d3-b5", "c7-c6", "b5-b7", "h6-f7", "g5-f4", "e7-e5", "d4-e5", "g7-g5", "f4-g3", "b8-d7", "b7-c6", "f8-b4", "c6-e6", "d8-e7", "e6-f5", "f7-e5", "g3-e5", "d7-e5", "g1-h3", "g4-h3", "e2-e4", "b4-c3", "b2-c3", "d5-e4", "f1-b5", "e8-d8", "a1-d1", "d8-c7"]

var pause = false
var i = 0
play_to_the_end = () => {
    console.log(i)
    setTimeout(function() {
        if (!pause) {
            board.move(moves[i])
            i = i+1
            if (i<moves.length) {
                play_to_the_end()
            }
        }
        
    }, 500)
}

document.querySelector('#play_to_the_end').addEventListener('click', () => {
    pause = false
    play_to_the_end()
});

document.querySelector('#pause').addEventListener('click', () => {
    pause = true
});