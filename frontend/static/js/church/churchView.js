define(['js/churchModel', 'hbs!js/church/church'], function(Church, viewTemplate) {
	var $ = Dom7;

	function render(params) {
		console.log(params);
		$('.church-page').html(viewTemplate({ model: params.model }));
		bindEvents(params.bindings);
	}

	function bindEvents(bindings) {
		for (var i in bindings) {
			$(bindings[i].element).on(bindings[i].event, bindings[i].handler);
		}
	}

	return {
		render: render
	}
});