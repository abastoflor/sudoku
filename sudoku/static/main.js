function val_length(element) {
    let max_length = 1;
    if (element.value.length > max_length) {
        element.value = element.value.slice(0, max_length);
    }
}


function verificar_fila_columna(valor = 0, id, url) {
    let [fil, col] = id.split('');
    if (valor === 'e') {
        valor == ''
    }
    data = {
        'valor': valor,
        'fil': fil,
        'col': col,
    }

    let csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0];
    let form = document.createElement('form');
    form.action = url;
    form.method = 'POST';
    let inp = document.createElement('input');
    inp.type = 'hidden';
    inp.name = 'data';
    inp.value = JSON.stringify(data)
    form.appendChild(csrftoken);
    form.appendChild(inp);

    document.body.appendChild(form);
    form.submit();
}

const tabler = JSON.parse(document.currentScript.nextElementSibling.textContent);
for (let i = 0; i < tabler.length; i++) {
    for (let j = 0; j < tabler[i].length; j++) {
        if (tabler[i][j] !== 0) {
            let fila = (i + 1).toString()
            let col = (j + 1).toString()
            let val = tabler[i][j]
            ide = `${fila}${col}`
            document.getElementById(ide).value = val;

        }
    }
}

