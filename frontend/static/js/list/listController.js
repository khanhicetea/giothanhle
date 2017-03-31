define(["app", "/backend/areas.js", "/backend/churches.js", "js/churchModel","js/list/listView"], function(app, AreasData, ChurchesData, Church, ListView) {

	/**
	 * Bindings array. Bind DOM event to some handler function in controller
	 * @type {*[]}
	 */
	var bindings = [{
		element: '.church-add-link',
		event: 'click',
		handler: openAddPopup
	}, {
		element: '.list-panel-all',
		event: 'click',
		handler: showAll
	}, {
		element: '.list-panel-favorites',
		event: 'click',
		handler: showFavorites
	}
	];

	var state = {
		isFavorite: false
	};

    function init() {
		var churches = loadChurches();
		ListView.render({
			bindings: bindings,
			model: churches
		});
	}

	function openAddPopup() {
		app.router.load('churchEdit', { 'isFavorite': state.isFavorite });
	}

	function showAll() {
		state.isFavorite = false;
		var churches = loadChurches();
		ListView.reRender({ model: churches, header: "Churches" });
	}

	function showFavorites() {
		state.isFavorite = true;
		var churches = loadChurches({ isFavorite: true });
		ListView.reRender({ model: churches, header: "Favorites" });
	}

	function loadChurches(filter) {
		var f7Churches = localStorage.getItem("f7Churches");
		var churches = f7Churches ? JSON.parse(f7Churches) : tempInitializeStorage();
		if (filter) {
			churches = _.filter(churches, filter);
		}
		churches.sort(churchSort);
		churches = _.groupBy(churches, function(church) { return church.area; });
		churches = _.toArray(_.mapValues(churches, function(value, key) {
			return { 'letter': AreasData.data[key], 'list': value };
		}));
		return churches;
	}

	function tempInitializeStorage() {
		localStorage.setItem("f7Churches", JSON.stringify(ChurchesData.data));
		return JSON.parse(localStorage.getItem("f7Churches"));
	}

	function churchSort(a, b) {
		if (a.name > b.name) {
			return 1;
		}
		if (a.name === b.name && a.area >= b.area) {
			return 1;
		}
		return -1;
	}

    return {
        init: init
    };
});
