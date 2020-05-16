document.querySelectorAll('.code_button').forEach(code_button => {

    let div = document.createElement('div'),
        letters = code_button.textContent.trim().split('');

    function elements(letter, index, array) {

        let element = document.createElement('span'),
            part = (index >= array.length / 2) ? -1 : 1,
            position = (index >= array.length / 2) ? array.length / 2 - index + (array.length / 2 - 1) : index,
            move = position / (array.length / 2),
            rotate = 1 - move;

        element.innerHTML = !letter.trim() ? '&nbsp;' : letter;
        element.style.setProperty('--move', move);
        element.style.setProperty('--rotate', rotate);
        element.style.setProperty('--part', part);

        div.appendChild(element);

    }

    letters.forEach(elements);

    code_button.innerHTML = div.outerHTML;

    code_button.addEventListener('mouseenter', e => {
        if(!code_button.classList.contains('out')) {
            code_button.classList.add('in');
        }
    });

    code_button.addEventListener('mouseleave', e => {
        if(code_button.classList.contains('in')) {
            code_button.classList.add('out');
            setTimeout(() => code_button.classList.remove('in', 'out'), 950);
        }
    });

});