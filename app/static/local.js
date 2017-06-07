$(document).ready(function() {
    $('#cat_sel').on('change', function() {
	$.getJSON($SCRIPT_ROOT + '/db/' + $('#cat_sel').val() + '/skills', 
	    {}, 
	    function(data) 
	    {
		if (typeof data !== 'undefined')
		{
		    $("#test_out").text(data);
		    var arr_skills = JSON.parse(data).skills;
		    if (typeof arr_skills !== 'undefined')
		    {
			$("#skill_list").empty();
			$.each( arr_skills, function(i){
			    var skill = JSON.parse(arr_skills[i]);
			    $("#test_out").append('<br>' + skill.name + '<br>' + skill.id)
			    $("#skill_list").append($('<option>', {value: skill.id, text: skill.name}))
			});
		    }
		    else
		    {
			$("#skill_list").empty()
		    }
		}
	    });
    });

    // Enable popovers
    $(function() {
	$('[data-toggle="popover"]').popover()
    });

    // Popover toggle
    $('#char_name').mouseover(function() {
	$('#char_name').popover('toggle');
    })
    .mouseout(function() {
	$('#char_name').popover('toggle');
    });
});
