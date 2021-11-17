class BoggleGame {


    constructor(boardId, secs = 60){
        this.secs = secs //game length

        this.score = 0
        this.words = new Set ()
        this.board = $('#' + this.boardId)

        //every 1000 msc, 'tick'
        this.timer = setInterval(this.tick.bind(this), 1000)

        $('.add-word', this.board).on('submit', this.handleSubmit.bind(this))
    }

    //Show score
    showScore(score, cls){
        $('.score', this.board)
        .text(this.score)
    }


    //Show a status message
    showMessage(msg,cls){
        $('.msg', this.board)
        .text(msg)
        .removeClass()
        .addClass(`msg ${cls}`)
    }

    /* handle submission of word: if unique and valid, score & show */
    async handleSubmit(evt){
        evt.preventDefaukt()
        const $word = ('.word', this.board)

        let word = $word.val()
        if(!word) return;

        if(this.words.has(word)){
            this.showMessage(`Already found ${word}`, 'err')
        }
       
        const resp = await axios.get('/check-word', {params: {word : word}})
        if(resp.data.result == 'not-word'){
            this.showMessage(`${word} is not valid English word`, 'err')
        } else if(resp.data.result == 'not-on-board'){
            this.showMessage(`${word} is not a valid word on this board`, "err")
        } else {
            this.showMessage(`Added ${word}`, 'ok')
            this.score += word.length
            this.showScore()
        }
    }

    
}