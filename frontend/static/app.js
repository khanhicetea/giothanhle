require.config({
    paths: {
        handlebars: "libs/handlebars",
        text: "libs/text",
        hbs: "libs/hbs"
    }
});
define('app', ['js/router', 'js/utils'], function(Router, Utils) {
	Router.init();
	var f7 = new Framework7({
		modalTitle: 'Contacts7',
		swipePanel: 'left',
        animateNavBackIcon: true
	});
    var mainView = f7.addView('.view-main', {
        dynamicNavbar: true
    });
	return {
		f7: f7,
		mainView: mainView,
		router: Router,
		utils: Utils
	};
});