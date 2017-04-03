define(["app","js/church/churchView", "js/churchModel"], function(app, churchView, Church) {

	var church = null;
	var bindings = [];

	function init(query){
		var churches = JSON.parse(localStorage.getItem("f7Churches"));
		if (query && query.id) {
			church = new Church(_.find(churches, { id: parseInt(query.id) }));
		}
		churchView.render({
			model: church,
			bindings: bindings
		});
	}

	return {
		init: init
	};
});