define(['js/churchModel', 'hbs!js/church/church'], function(Church, viewTemplate) {
	var $ = Dom7;

	var weekLabels = {
		2: 'Thứ 2',
		3: 'Thứ 3',
		4: 'Thứ 4',
		5: 'Thứ 5',
		6: 'Thứ 6',
		7: 'Thứ 7',
		8: 'Chủ Nhật'
	};

	function render(params) {
		$('.church-page').html(viewTemplate({
			model: params.model,
			labels: weekLabels,
			test: "hello"
		}));
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