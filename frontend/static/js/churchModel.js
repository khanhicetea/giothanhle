define(['app'],function(app) {

    function Church(values) {
		values = values || {};
		this.id = values['id'] || app.utils.generateGUID();

		this.name = values['name'] || '';
		this.address = values['address'] || '';
		this.area = values['area'] || 0;
		this.location = values['location'] || { "lat": 0, "long": 0 };
		this.website = values['website'] || '';
		this.isFavorite = values['isFavorite'] || false;
    }

    return Church;
});
