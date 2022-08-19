odoo.define('course.carousel.snippet', function (require) {
   'use strict';
var publicWidget = require('web.public.widget');

publicWidget.registry.books = publicWidget.Widget.extend({
   selector: '.s_course_carousel',
   disabledInEditableMode: false,
   start: function (){
   var self = this;
      this._rpc({
         model: 'course',
         method: 'search_read',
         domain: [],
         fields:['image'],
         orderBy: [{name: 'write_date', asc: false}],
         limit: 3
         }).then(function (course) {
            $('#img_carosouel-1').attr('src', 'data:image/;base64,' + course[0].image)
            $('#img_carosouel-2').attr('src', 'data:image/;base64,' + course[1].image)
            $('#img_carosouel-3').attr('src', 'data:image/;base64,' + course[2].image)
        })
    }
});
});
