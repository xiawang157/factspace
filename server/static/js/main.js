(function(){

    $body = $("body");
    $(document).on({
        ajaxStart: function() { $body.addClass("loading");},
        ajaxStop: function() { $body.removeClass("loading"); }
    });

    vegaOptMode = {
	  "actions": true,
	  "renderer": "svg",
	  "hover": false,
	  "tooltip": true
	};

})();
