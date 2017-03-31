define(['hbs!js/list/church-list-item'], function(template) {
    var $ = Dom7;

	function render(params) {
        $('.churches-list ul').html(template(params.model));
        $('.searchbar-cancel').click();
		bindEvents(params.bindings);
    }

	function reRender(params) {
		$('.churches-list ul').html(template(params.model));
		$('.churches-list-header').text(params.header);
        $('.searchbar-cancel').click();
	}

	function bindEvents(bindings) {
		for (var i in bindings) {
			$(bindings[i].element).on(bindings[i].event, bindings[i].handler);
		}
	}

    return {
        render: render,
		reRender: reRender
    };
});