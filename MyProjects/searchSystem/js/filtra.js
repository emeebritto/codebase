import getPhasesList from './phasesList.js'

var campoFiltro = document.querySelector("#filtrar-tabela");

const phasesList = getPhasesList()

const createLine = (phase) => {
    var p = document.createElement("p");
    p.textContent = phase
    return p
}

campoFiltro.addEventListener("input", function() {
    var root = document.getElementById('root')
    root.innerHTML = ''
    var selected = []

    if (this.value.length > 0) {
        for (var i = 0; i < phasesList.length; i++) {
            var expressao = new RegExp(this.value, "i")
            var phase = phasesList[i]

            if (expressao.test(phase)) {
                var index = phase.indexOf(this.value);    
                var phaseResumed = phase.slice(index);
                selected.push(phaseResumed)
            }
        }

        var boxPhases = document.createElement("div");
        selected.forEach(phase => {
            boxPhases.appendChild(createLine(phase))
            
        })
        root.appendChild(boxPhases)
    }
});

var botaoAdicionar = document.querySelector("#adicionar-paciente");

botaoAdicionar.addEventListener("click", function(event) {
    event.preventDefault();

    var form = document.querySelector("#form-adiciona");

    var phase = form.nome.value

    phasesList.push(phase);

    form.reset();
    
});