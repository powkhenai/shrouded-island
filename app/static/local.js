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
		    //$("#skill_list").text(arr_skills[0].name);
		    if (typeof arr_skills !== 'undefined')
		    {
			$("#skill_list").empty();
			$.each( arr_skills, function(i){
			    var skill = JSON.parse(arr_skills[i]);
			    $("#test_out").append('<br>' + skill.name + '<br>' + skill.id)
			    $("#skill_list").append($('<option>', {value: skill.id, text: skill.name}))
			//$("#skill_list").selectpicker('refresh')
			});
		    }
		    else
		    {
			$("#skill_list").empty()
		    }
		}
	    });
    });
});
