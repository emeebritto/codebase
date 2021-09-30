#Data Binding


##Property binding

permite que um valor de uma variável seja atribuído ao elemento HTML

Com esse binding é possível associar uma propriedade de um elemento a um atributo da nossa classe Typescript.

                                                              |
                                                              v
<input class="form-field__input" id="destino" type="text" [ngModel]="destino" name="destino" />

##Two-way data binding

garante uma comunicação bidirecional entre o componente e o DOM.

Com esse binding é possível manter uma comunicação de duas vias entre uma propriedade de um elemento a um atributo da nossa classe Typescript.

<div class="form-field">                                         |
  <label class="form-field__label" for="destino">Destino</label> v
  <input class="form-field__input" id="destino" type="text" [(ngModel)]="destino" name="destino" />
</div>

##Event binding

permite que um evento do DOM seja atribuído a um método do

Com esse binding é possível associar um evento de um elemento a um método da nossa classe Typescript.

                               |
                               v
<form class="formulario" (ngSubmit)="transferir()">
	<h2 class="formulario__titulo">Nova Transferência</h2>
[...]